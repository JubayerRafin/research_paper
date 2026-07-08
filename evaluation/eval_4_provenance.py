#!/usr/bin/env python3
"""
eval_4_provenance.py — Validate provenance integrity of each Q&A pair.

WHY THIS METRIC
---------------
The pipeline's central claim is that it is *provenance-preserving*: every
generated Q&A pair must trace back correctly to its source location in the
Stage 1 output. This evaluator is the evidence for that claim. It does not
assume provenance is correct — it verifies it.

WHAT IT CHECKS (per pair)
-------------------------
  1. PRESENT   — a provenance record exists with the required fields.
  2. RESOLVES  — the cited page (and element, if any) exists in Stage 1 output.
  3. GROUNDED  — the pair's chunk_text actually matches source text on that page
                 (guards against a chunk pasted from the wrong page).

Each pair gets a status: valid | broken_link | missing_provenance | chunk_mismatch
Aggregate = % of pairs with fully valid provenance.

METHOD
------
Deterministic. Uses the Stage 1 markdown (page-split by <!-- page: N -->) as the
source-of-truth text per page, and the tables/ + images/ dirs to confirm element
references resolve. No LLM, no network.

USAGE
-----
    python eval_4_provenance.py \
        --pairs qa_pairs.jsonl \
        --stage1-md data/canon_manual.md \
        --stage1-dir output/stage1 \
        --output-dir eval_results/

If your provenance record carries an element id (e.g. table_p12_3 / image_p12_1),
pass --element-field <keyname> to verify element links too. Otherwise the check
is page-level (+ chunk grounding), which is still valid.
"""
import argparse, csv, json, re, statistics
from pathlib import Path
from collections import Counter

STOP = set("a an and are as at be by for from has have in is it its of on or that the to was were with".split())

def toks(t):
    return [w for w in re.findall(r"[a-z0-9]+", t.lower()) if len(w) > 2 and w not in STOP]

def extract_qa(pair):
    q=a=""
    for m in pair.get("messages", []):
        if m.get("role")=="user" and not q: q=(m.get("content") or "").strip()
        elif m.get("role")=="assistant" and not a: a=(m.get("content") or "").strip()
    return q,a

def load_pages_md(md_path):
    if not md_path or not Path(md_path).exists():
        return {}
    raw = Path(md_path).read_text(encoding="utf-8")
    parts = re.split(r"<!--\s*page:\s*(\d+)\s*-->", raw)
    pages={}
    for i in range(1,len(parts),2):
        pages[int(parts[i])] = parts[i+1] if i+1<len(parts) else ""
    return pages

def load_elements(stage1_dir):
    tables=set(); images=set()
    if stage1_dir and Path(stage1_dir).exists():
        for f in Path(stage1_dir).glob("tables/table_p*.json"):
            tables.add(f.stem)
        for f in Path(stage1_dir).glob("images/image_p*.png"):
            images.add(f.stem)
    return tables, images

def chunk_grounded(chunk, page_text, min_overlap=0.30):
    if not page_text.strip():
        return None
    c = toks(chunk)
    if not c: return None
    p = set(toks(page_text))
    if not p: return None
    matched = sum(1 for t in c if t in p)
    return (matched/len(c)) >= min_overlap, matched/len(c)

def main():
    ap=argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--pairs", type=Path, required=True)
    ap.add_argument("--stage1-md", type=Path, default=None)
    ap.add_argument("--stage1-dir", type=Path, default=None)
    ap.add_argument("--element-field", default=None)
    ap.add_argument("--output-dir", type=Path, default=Path("eval_results"))
    args=ap.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)

    pairs=[]
    with args.pairs.open(encoding="utf-8") as f:
        for line in f:
            line=line.strip()
            if line: pairs.append(json.loads(line))
    print(f"[info] Loaded {len(pairs)} pairs")

    pages = load_pages_md(args.stage1_md)
    tables, images = load_elements(args.stage1_dir)
    print(f"[info] Stage1 pages: {len(pages)} | tables: {len(tables)} | images: {len(images)}")

    rows=[]
    for i,p in enumerate(pairs):
        prov = p.get("provenance", {})
        q,a = extract_qa(p)
        chunk = p.get("chunk_text","")
        status="valid"; detail=""

        if not prov or prov.get("page") in (None,""):
            status="missing_provenance"
        else:
            page = prov.get("page")
            try: page_int=int(page)
            except (ValueError,TypeError): page_int=None

            if pages and page_int is not None and page_int not in pages:
                status="broken_link"; detail=f"page {page} not in Stage1 output"
            elif args.element_field and prov.get(args.element_field):
                eid=str(prov.get(args.element_field))
                if eid not in tables and eid not in images:
                    status="broken_link"; detail=f"element {eid} not found"

            if status=="valid" and pages and page_int in pages and chunk:
                g = chunk_grounded(chunk, pages[page_int])
                if g is not None and g[0] is False:
                    status="chunk_mismatch"; detail=f"chunk overlap {g[1]:.2f} < 0.30 with page {page}"

        rows.append({
            "idx":i, "page":prov.get("page",""), "category":prov.get("category",""),
            "status":status, "detail":detail, "question":q[:80],
        })

    csv_path=args.output_dir/"provenance_per_pair.csv"
    with csv_path.open("w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)

    n=len(rows)
    counts=Counter(r["status"] for r in rows)
    valid_pct = round(100*counts.get("valid",0)/n,2) if n else 0
    summary={
        "metric":"provenance_integrity",
        "method":"page/element resolution + chunk-to-page grounding (deterministic)",
        "n_pairs":n,
        "valid":counts.get("valid",0),
        "valid_pct":valid_pct,
        "status_counts":dict(counts),
        "status_pct":{k:round(100*v/n,2) for k,v in counts.items()},
        "checks":{
            "page_resolution": bool(pages),
            "element_resolution": bool(args.element_field),
            "chunk_grounding": bool(pages),
        },
        "target_valid_pct":95.0,
        "passes": valid_pct>=95.0,
    }
    (args.output_dir/"provenance_summary.json").write_text(json.dumps(summary,indent=2),encoding="utf-8")

    print(f"\n=== PROVENANCE INTEGRITY ===")
    print(f"  Pairs evaluated:   {n}")
    print(f"  Valid provenance:  {counts.get('valid',0)}  ({valid_pct}%)   target >= 95%   {'PASS' if summary['passes'] else 'FAIL'}")
    for k in ("broken_link","missing_provenance","chunk_mismatch"):
        if counts.get(k): print(f"  {k:20s} {counts[k]:5d}  ({round(100*counts[k]/n,2)}%)")
    if not pages:
        print("  [note] No Stage1 markdown given -> page resolution + grounding skipped (presence-only).")
    print(f"\n[saved] {csv_path}")
    print(f"[saved] {args.output_dir/'provenance_summary.json'}")

if __name__=="__main__":
    main()








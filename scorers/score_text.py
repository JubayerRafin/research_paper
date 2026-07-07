#!/usr/bin/env python3
"""
score_text.py
-------------
Text extraction accuracy: CER, WER, and token-F1.

Compares the extractor's per-page text (parsed from the Stage-1 .md, split on
'<!-- page: N -->' markers) against human ground-truth text files (pNNN.txt).

Only pages that HAVE a ground-truth .txt file are scored.
Markdown noise (image links, JSON table blocks, headings markup) is stripped
from the extracted text before comparison so we score prose, not markup.

Metrics:
  CER = char edit distance / len(reference chars)
  WER = word edit distance / len(reference words)
  token-F1 = F1 over the multiset of words
Aggregated (micro) across scored pages.

Usage:
  python score_text.py --md output/xxx.md --gt_dir text_ground_truth_50
"""
import os, re, glob, argparse


def edit_distance(a, b):
    """Levenshtein distance between two sequences (lists or strings)."""
    n, m = len(a), len(b)
    if n == 0: return m
    if m == 0: return n
    prev = list(range(m + 1))
    for i in range(1, n + 1):
        cur = [i] + [0] * m
        for j in range(1, m + 1):
            cost = 0 if a[i-1] == b[j-1] else 1
            cur[j] = min(prev[j] + 1, cur[j-1] + 1, prev[j-1] + cost)
        prev = cur
    return prev[m]


def clean_md_text(txt):
    """Strip markdown markup so we compare prose to prose."""
    # remove JSON table code blocks
    txt = re.sub(r"```json.*?```", " ", txt, flags=re.DOTALL)
    txt = re.sub(r"```.*?```", " ", txt, flags=re.DOTALL)
    # remove image links ![alt](path)
    txt = re.sub(r"!\[.*?\]\(.*?\)", " ", txt)
    # remove heading hashes and list bullets markup
    txt = re.sub(r"^#{1,6}\s*", "", txt, flags=re.MULTILINE)
    txt = re.sub(r"^[\-\*]\s+", "", txt, flags=re.MULTILINE)
    # remove page comment markers
    txt = re.sub(r"<!--.*?-->", " ", txt)
    return txt


def norm(s):
    s = re.sub(r"\s+", " ", s).strip()
    return s


def parse_md_pages(md_path):
    """Return {page_num: extracted_text} split on page markers."""
    raw = open(md_path, encoding="utf-8").read()
    parts = re.split(r"<!--\s*page:\s*(\d+)\s*-->", raw)
    # parts = [pre, pagenum, content, pagenum, content, ...]
    pages = {}
    for i in range(1, len(parts), 2):
        pg = int(parts[i])
        body = parts[i+1] if i+1 < len(parts) else ""
        pages[pg] = norm(clean_md_text(body))
    return pages


def load_gt_texts(gt_dir):
    """Return {page_num: reference_text} from pNNN.txt files."""
    gt = {}
    for f in glob.glob(os.path.join(gt_dir, "p*.txt")):
        m = re.search(r"p(\d+)\.txt", os.path.basename(f))
        if not m:
            continue
        pg = int(m.group(1))
        gt[pg] = norm(open(f, encoding="utf-8").read())
    return gt


def token_f1(ref, hyp):
    from collections import Counter
    r = Counter(ref.split())
    h = Counter(hyp.split())
    tp = sum((r & h).values())
    P = tp / sum(h.values()) if sum(h.values()) else 0.0
    R = tp / sum(r.values()) if sum(r.values()) else 0.0
    F = 2*P*R/(P+R) if (P+R) else 0.0
    return P, R, F


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--md", required=True, help="Stage-1 markdown output")
    ap.add_argument("--gt_dir", required=True, help="folder of pNNN.txt GT files")
    ap.add_argument("--pages", action="store_true", help="per-page breakdown")
    args = ap.parse_args()

    ext = parse_md_pages(args.md)
    gt = load_gt_texts(args.gt_dir)

    scored = sorted(p for p in gt if gt[p].strip())
    print(f"GT text pages: {len(gt)} | non-empty & scored: {len(scored)}")
    print(f"{'page':>5} {'CER':>6} {'WER':>6} {'F1':>6}")

    tot_cer_num = tot_cer_den = 0
    tot_wer_num = tot_wer_den = 0
    f1s = []
    for pg in scored:
        ref = gt[pg]
        hyp = ext.get(pg, "")
        # CER
        cd = edit_distance(ref, hyp)
        tot_cer_num += cd; tot_cer_den += max(len(ref), 1)
        # WER
        rw, hw = ref.split(), hyp.split()
        wd = edit_distance(rw, hw)
        tot_wer_num += wd; tot_wer_den += max(len(rw), 1)
        # F1
        _, _, F = token_f1(ref, hyp)
        f1s.append(F)
        if args.pages:
            print(f"{pg:>5} {cd/max(len(ref),1):>6.3f} {wd/max(len(rw),1):>6.3f} {F:>6.3f}")

    CER = tot_cer_num / max(tot_cer_den, 1)
    WER = tot_wer_num / max(tot_wer_den, 1)
    F1 = sum(f1s)/len(f1s) if f1s else 0.0
    print(f"\n=== TEXT (micro-aggregated over {len(scored)} pages) ===")
    print(f"  CER:      {CER:.3f}")
    print(f"  WER:      {WER:.3f}")
    print(f"  token-F1: {F1:.3f}")
    print()


if __name__ == "__main__":
    main()

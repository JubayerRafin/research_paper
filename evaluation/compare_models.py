#!/usr/bin/env python3
"""
compare_models.py — Side-by-side Stage 2 evaluation of two generation models.

Runs the full evaluation suite (faithfulness NLI, question quality, diversity,
provenance) on each model's qa_pairs.jsonl, then produces:
  - a combined comparison table (markdown + CSV)
  - publication-quality figures (PNG + PDF) for the paper

Designed for the paper's model-comparison result:
  Mistral 24B (production)  vs  Qwen 3.5 35B (largest)

USAGE
-----
  # 1. First run your eval pipeline on each model's output into separate dirs:
  python evaluate_all.py --pairs mistral_qa.jsonl --output-dir eval_mistral/
  python evaluate_all.py --pairs qwen_qa.jsonl    --output-dir eval_qwen/
  #    (also run eval_4_provenance.py into each dir)

  # 2. Then compare:
  python compare_models.py \
      --model-a "Mistral 24B" --dir-a eval_mistral/ \
      --model-b "Qwen 3.5 35B" --dir-b eval_qwen/ \
      --output-dir comparison/
"""
import argparse, json, csv
from pathlib import Path

# --- publication figure style (grayscale-safe, journal-ready) ---
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

plt.rcParams.update({
    "font.size": 11,
    "font.family": "DejaVu Sans",
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.grid": True,
    "grid.alpha": 0.3,
    "figure.dpi": 150,
})
# two distinguishable, print-safe colors
COLOR_A = "#3B6FB6"   # blue
COLOR_B = "#C6531A"   # orange-brown


def load(dir_path):
    d = Path(dir_path)
    def j(name):
        p = d / name
        return json.loads(p.read_text(encoding="utf-8")) if p.exists() else None
    return {
        "faith_nli": j("faithfulness_nli_summary.json"),
        "faith_tok": j("faithfulness_summary.json"),
        "qquality":  j("question_quality_summary.json"),
        "diversity": j("diversity_summary.json"),
        "provenance": j("provenance_summary.json"),
    }


def metric_rows(a, b, name_a, name_b):
    """Extract comparable metrics. Returns list of (label, val_a, val_b, higher_is_better)."""
    rows = []
    def g(d, *keys):
        cur = d
        for k in keys:
            if cur is None: return None
            cur = cur.get(k)
        return cur

    # Faithfulness NLI — faithful %
    rows.append(("Faithful pairs (NLI) %",
                 g(a["faith_nli"], "verdict_pct", "faithful"),
                 g(b["faith_nli"], "verdict_pct", "faithful"), True))
    # Contradiction rate %
    ca = g(a["faith_nli"], "claim_level", "contradiction_rate")
    cb = g(b["faith_nli"], "claim_level", "contradiction_rate")
    rows.append(("Contradiction rate %",
                 round(ca*100,2) if ca is not None else None,
                 round(cb*100,2) if cb is not None else None, False))
    # Mean faithfulness score
    rows.append(("Mean faithfulness (NLI)",
                 g(a["faith_nli"], "mean_score"),
                 g(b["faith_nli"], "mean_score"), True))
    # Generic questions %
    rows.append(("Generic questions %",
                 g(a["qquality"], "generic", "pct"),
                 g(b["qquality"], "generic", "pct"), False))
    # Mean question length
    rows.append(("Mean question length (words)",
                 g(a["qquality"], "length", "mean_words"),
                 g(b["qquality"], "length", "mean_words"), True))
    # Q-A relevance mean cosine
    rows.append(("Q-A relevance (cosine)",
                 g(a["diversity"], "qa_relevance", "mean_cosine"),
                 g(b["diversity"], "qa_relevance", "mean_cosine"), True))
    # Near-duplicate %
    rows.append(("Near-duplicate Qs %",
                 g(a["diversity"], "question_diversity", "near_duplicates_0.95_pct"),
                 g(b["diversity"], "question_diversity", "near_duplicates_0.95_pct"), False))
    # Provenance valid %
    rows.append(("Valid provenance %",
                 g(a["provenance"], "valid_pct"),
                 g(b["provenance"], "valid_pct"), True))
    return [r for r in rows if r[1] is not None and r[2] is not None]


def fig_grouped_bars(rows, name_a, name_b, out_base):
    """One grouped-bar figure of the % / score metrics (normalized where needed)."""
    # Split into 0-100 metrics and 0-1 metrics for readable axes
    pct = [(l,va,vb,hib) for (l,va,vb,hib) in rows if va>1 or vb>1]
    frac = [(l,va,vb,hib) for (l,va,vb,hib) in rows if va<=1 and vb<=1]

    for subset, title, fname in [(pct,"Percentage / count metrics","_pct"),
                                 (frac,"Score metrics (0-1)","_score")]:
        if not subset: continue
        labels=[l for l,_,_,_ in subset]
        va=[v for _,v,_,_ in subset]; vb=[v for _,_,v,_ in subset]
        import numpy as np
        x=np.arange(len(labels)); w=0.38
        fig,ax=plt.subplots(figsize=(max(6,len(labels)*1.5),4.2))
        ax.bar(x-w/2, va, w, label=name_a, color=COLOR_A)
        ax.bar(x+w/2, vb, w, label=name_b, color=COLOR_B)
        ax.set_xticks(x); ax.set_xticklabels(labels, rotation=25, ha="right", fontsize=9)
        ax.set_title(title, fontsize=11)
        ax.legend(frameon=False)
        for i,(A,B) in enumerate(zip(va,vb)):
            ax.text(i-w/2, A, f"{A:g}", ha="center", va="bottom", fontsize=8)
            ax.text(i+w/2, B, f"{B:g}", ha="center", va="bottom", fontsize=8)
        fig.tight_layout()
        fig.savefig(f"{out_base}{fname}.png", bbox_inches="tight")
        fig.savefig(f"{out_base}{fname}.pdf", bbox_inches="tight")
        plt.close(fig)


def main():
    ap=argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--model-a", required=True); ap.add_argument("--dir-a", type=Path, required=True)
    ap.add_argument("--model-b", required=True); ap.add_argument("--dir-b", type=Path, required=True)
    ap.add_argument("--output-dir", type=Path, default=Path("comparison"))
    args=ap.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)

    a=load(args.dir_a); b=load(args.dir_b)
    rows=metric_rows(a,b,args.model_a,args.model_b)
    if not rows:
        print("[error] No comparable metrics found. Did you run evaluate_all.py + eval_4_provenance.py into each dir?")
        return

    # CSV
    csv_path=args.output_dir/"model_comparison.csv"
    with csv_path.open("w",newline="",encoding="utf-8") as f:
        w=csv.writer(f)
        w.writerow(["metric", args.model_a, args.model_b, "higher_is_better", "winner"])
        for l,va,vb,hib in rows:
            winner = args.model_a if (va>vb)==hib and va!=vb else (args.model_b if va!=vb else "tie")
            w.writerow([l,va,vb,hib,winner])

    # Markdown table
    md=[f"# Model Comparison — {args.model_a} vs {args.model_b}\n",
        f"| Metric | {args.model_a} | {args.model_b} | Better |","|---|---:|---:|:---:|"]
    for l,va,vb,hib in rows:
        if va==vb: better="tie"
        else: better=args.model_a if (va>vb)==hib else args.model_b
        md.append(f"| {l} | {va:g} | {vb:g} | {better} |")
    (args.output_dir/"model_comparison.md").write_text("\n".join(md)+"\n",encoding="utf-8")

    # Figures
    fig_grouped_bars(rows, args.model_a, args.model_b, str(args.output_dir/"model_comparison"))

    print(f"[saved] {csv_path}")
    print(f"[saved] {args.output_dir/'model_comparison.md'}")
    print(f"[saved] {args.output_dir}/model_comparison_pct.(png|pdf)")
    print(f"[saved] {args.output_dir}/model_comparison_score.(png|pdf)")
    print("\n=== COMPARISON ===")
    for l,va,vb,hib in rows:
        better = "=" if va==vb else (args.model_a if (va>vb)==hib else args.model_b)
        print(f"  {l:32s} {va:>8g}  {vb:>8g}   -> {better}")


if __name__=="__main__":
    main()

#!/usr/bin/env python3
"""
score_counts.py
---------------
Count-based Precision / Recall / F1 for image and table DETECTION.

Compares per-page extracted counts against human ground-truth counts
(gt_images, gt_tables) from an .xlsx sheet with columns:
    Page # | gt_text | gt_tables | gt_images

Per page:  TP = min(extracted, gt)
           FP = max(0, extracted - gt)
           FN = max(0, gt - extracted)
Aggregated across all GT pages -> P, R, F1 (reported separately for
images and tables).

Usage:
    python score_counts.py --gt hp_gt.xlsx --output output
       (expects output/images/ and output/tables/ inside --output)
"""
import os, re, glob, argparse
from collections import defaultdict


def load_gt(xlsx_path):
    import openpyxl
    wb = openpyxl.load_workbook(xlsx_path, data_only=True)
    ws = wb.active
    rows = list(ws.iter_rows(values_only=True))
    header = [str(h).strip().lower() if h else "" for h in rows[0]]

    def col(name):
        for i, h in enumerate(header):
            if name in h:
                return i
        return None

    ci_page = col("page")
    ci_img  = col("image")
    ci_tbl  = col("table")
    gt = {}
    for r in rows[1:]:
        if r[ci_page] is None:
            continue
        try:
            page = int(r[ci_page])
        except (ValueError, TypeError):
            continue
        gi = int(r[ci_img]) if (ci_img is not None and r[ci_img] not in (None, "")) else 0
        gt_ = int(r[ci_tbl]) if (ci_tbl is not None and r[ci_tbl] not in (None, "")) else 0
        gt[page] = {"images": gi, "tables": gt_}
    return gt


def count_extracted(folder, pattern):
    """Count files per page matching image_p{N}_* or table_p{N}_*."""
    counts = defaultdict(int)
    for f in glob.glob(os.path.join(folder, pattern)):
        m = re.search(r"_p(\d+)_", os.path.basename(f))
        if m:
            counts[int(m.group(1))] += 1
    return counts


def score(gt, extracted_counts, key):
    TP = FP = FN = 0
    per_page = []
    for page in sorted(gt):
        g = gt[page][key]
        e = extracted_counts.get(page, 0)
        tp = min(e, g)
        fp = max(0, e - g)
        fn = max(0, g - e)
        TP += tp; FP += fp; FN += fn
        if g or e:
            per_page.append((page, g, e, tp, fp, fn))
    P = TP / (TP + FP) if (TP + FP) else 0.0
    R = TP / (TP + FN) if (TP + FN) else 0.0
    F = 2 * P * R / (P + R) if (P + R) else 0.0
    return P, R, F, TP, FP, FN, per_page


def report(name, res, show_pages=False):
    P, R, F, TP, FP, FN, per_page = res
    print(f"\n=== {name} DETECTION ===")
    print(f"  Precision: {P:.3f}")
    print(f"  Recall:    {R:.3f}")
    print(f"  F1:        {F:.3f}")
    print(f"  (TP={TP}  FP={FP}  FN={FN})")
    if show_pages:
        print(f"  {'page':>5} {'gt':>3} {'ext':>3} {'TP':>3} {'FP':>3} {'FN':>3}")
        for page, g, e, tp, fp, fn in per_page:
            flag = "  <-- FP" if fp else ("  <-- FN" if fn else "")
            print(f"  {page:>5} {g:>3} {e:>3} {tp:>3} {fp:>3} {fn:>3}{flag}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--gt", required=True, help="hp_gt.xlsx")
    ap.add_argument("--output", required=True, help="folder containing images/ and tables/")
    ap.add_argument("--pages", action="store_true", help="show per-page breakdown")
    args = ap.parse_args()

    gt = load_gt(args.gt)
    img_counts = count_extracted(os.path.join(args.output, "images"), "image_p*.png")
    tbl_counts = count_extracted(os.path.join(args.output, "tables"), "table_p*.json")

    print(f"GT pages: {len(gt)}  |  output: {args.output}")
    report("IMAGE", score(gt, img_counts, "images"), args.pages)
    report("TABLE", score(gt, tbl_counts, "tables"), args.pages)
    print()


if __name__ == "__main__":
    main()

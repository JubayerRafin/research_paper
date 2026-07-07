#!/usr/bin/env python3
"""
baseline_text.py — TEXT extraction baselines, CER / WER / token-F1.

Baselines (each extracts per-page text, scored vs the human GT .txt files):
  - pdfplumber   : page.extract_text()
  - pymupdf      : fitz page.get_text()
  - pdfminer     : pdfminer.six extract_text per page

Same GT (pNNN.txt) and same metric as the pipeline text scorer.

Usage:
  python baseline_text.py --pdf hp.pdf --gt_dir text_ground_truth_50
"""
import os, re, glob, argparse


def edit_distance(a,b):
    n,m=len(a),len(b)
    if n==0:return m
    if m==0:return n
    prev=list(range(m+1))
    for i in range(1,n+1):
        cur=[i]+[0]*m
        for j in range(1,m+1):
            cost=0 if a[i-1]==b[j-1] else 1
            cur[j]=min(prev[j]+1,cur[j-1]+1,prev[j-1]+cost)
        prev=cur
    return prev[m]


def norm(s): return re.sub(r"\s+"," ",s).strip()


def load_gt(gt_dir):
    gt={}
    for f in glob.glob(os.path.join(gt_dir,"p*.txt")):
        m=re.search(r"p(\d+)\.txt",os.path.basename(f))
        if m: gt[int(m.group(1))]=norm(open(f,encoding="utf-8").read())
    return gt


def token_f1(ref,hyp):
    from collections import Counter
    r=Counter(ref.split()); h=Counter(hyp.split())
    tp=sum((r&h).values())
    P=tp/sum(h.values()) if sum(h.values()) else 0.0
    R=tp/sum(r.values()) if sum(r.values()) else 0.0
    return 2*P*R/(P+R) if P+R else 0.0


def extract_pdfplumber(pdf,pages):
    import pdfplumber
    out={}
    with pdfplumber.open(pdf) as doc:
        for p in pages:
            try: out[p]=norm(doc.pages[p-1].extract_text() or "")
            except: out[p]=""
    return out


def extract_pymupdf(pdf,pages):
    import fitz
    doc=fitz.open(pdf); out={}
    for p in pages:
        try: out[p]=norm(doc[p-1].get_text())
        except: out[p]=""
    return out


def extract_pdfminer(pdf,pages):
    from pdfminer.high_level import extract_text
    out={}
    for p in pages:
        try: out[p]=norm(extract_text(pdf,page_numbers=[p-1]))
        except: out[p]=""
    return out


def score(gt,ext):
    scored=sorted(p for p in gt if gt[p].strip())
    cn=cd=wn=wd=0; f1s=[]
    for p in scored:
        ref=gt[p]; hyp=ext.get(p,"")
        cn+=edit_distance(ref,hyp); cd+=max(len(ref),1)
        rw,hw=ref.split(),hyp.split()
        wn+=edit_distance(rw,hw); wd+=max(len(rw),1)
        f1s.append(token_f1(ref,hyp))
    return cn/max(cd,1), wn/max(wd,1), sum(f1s)/len(f1s) if f1s else 0.0


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--pdf",required=True); ap.add_argument("--gt_dir",required=True)
    a=ap.parse_args()
    gt=load_gt(a.gt_dir); pages=sorted(gt)
    print(f"TEXT baselines | {len([p for p in gt if gt[p].strip()])} scored pages\n")
    for name,fn in [("pdfplumber",extract_pdfplumber),("pymupdf",extract_pymupdf),
                    ("pdfminer",extract_pdfminer)]:
        try:
            ext=fn(a.pdf,pages)
            CER,WER,F=score(gt,ext)
            print(f"  {name:12} CER={CER:.3f} WER={WER:.3f} F1={F:.3f}")
        except Exception as e:
            print(f"  {name:12} ERROR: {e}")
    print()

if __name__=="__main__": main()

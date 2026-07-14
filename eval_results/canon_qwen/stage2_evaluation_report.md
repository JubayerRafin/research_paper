# Stage 2 Q&A Dataset — Evaluation Report

**Source:** `canon_qwen.jsonl`
**Pairs evaluated:** 372
**Evaluation method:** independent of generation LLM (token-overlap + NLI + sentence-transformers)

---

## Headline Numbers

| Metric | Result | Target | Status |
|---|---:|---:|:---:|
| **Faithful pairs (NLI, gold standard)** | **93.57%** | >= 80% | PASS |
| Contradicted claims (NLI) | 2.26% | <= 1% | FAIL |
| Faithful pairs (token-overlap, fast check) | 94.89% | >= 80% | PASS |
| Suspicious pairs (token-overlap) | 0.0% | <= 5% | PASS |
| Generic questions | 2.41% | <= 5.0% | PASS |
| Short questions | 9.92% | <= 10% | PASS |
| Q-A mean cosine | 0.5773 | >= 0.5 | PASS |
| Near-duplicate Qs | 2.95% | <= 5.0% | PASS |

## 1a. Faithfulness — NLI Gold Standard

Method: NLI (DeBERTa-v3-MNLI) on sentence-level claims
Model: `MoritzLaurer/DeBERTa-v3-large-mnli-fever-anli-ling-wanli` (independent of generation LLM, deterministic)

**Claim level** (399 sentences across all answers):
- Entailed by chunk: **375** (93.98%)
- Contradicted: 9 (2.26%)
- Neutral (chunk doesn't say): 15

**Pair level**:
- Mean per-pair score: **0.9437**
- Median per-pair score: 1.0
- Faithful: 349 (93.57%)
- Partial: 4 (1.07%)
- Unfaithful: 20 (5.36%)

## 1b. Faithfulness — Token-Overlap (Fast Cross-Check)

Method: token-overlap (stopwords removed, lightly stemmed); untestable pairs excluded
- Mean overlap score: **0.9143**
- Median overlap score: 1.0
- Faithful (>= 0.70 overlap): **353** (94.89%)
- Partial (0.40-0.70 overlap): 19 (5.11%)
- Suspicious (< 0.40 overlap): 0 (0.0%)

_Both faithfulness methods are reported. NLI is the primary metric. Token-overlap is a fast sanity check — methods should broadly agree._

## 2. Question Quality

- Average question length: **11.8** words (median 11, range 5-24)
- Generic / meta-textual questions: **9** (2.41%)
- Type distribution:
   - how: 192 (51.47%)
   - what: 176 (47.18%)
   - when: 3 (0.8%)
   - other: 1 (0.27%)
   - why: 1 (0.27%)

## 3. Diversity and Q-A Relevance

Embedding model: `sentence-transformers/all-MiniLM-L6-v2`

**Q-A relevance** (does the answer address the question?):
- Mean cosine: **0.5773**
- % above 0.70 (highly relevant): 30.83%
- % below 0.30 (off-topic): 12.33%

**Question diversity** (are questions different from each other?):
- Mean nearest-neighbor cosine: 0.6951
- Near-duplicates (> 0.95): **11** (2.95%)
- Very-close pairs (> 0.90): 30

---

## Methodology Notes

- **Faithfulness (NLI)** uses DeBERTa-v3-MNLI to check whether each answer sentence is entailed by the source chunk. This is the gold-standard signal — catches numerical contradictions and subtle hallucinations that token-overlap misses.
- **Faithfulness (token-overlap)** is a fast sanity check using set intersection of stop-word-removed tokens. Used as a cross-check against the NLI result.
- **Question quality** uses regex patterns and length statistics. Deterministic.
- **Diversity** uses sentence-transformer embeddings (`all-MiniLM-L6-v2`).

**Why no LLM-as-judge?** Using a generative LLM to score another LLM's output introduces evaluator bias, requires API calls (breaks the offline requirement), and produces non-deterministic scores. All metrics in this report are deterministic and run fully locally.

**Comparing across generation LLMs:** Run this same pipeline on each LLM's output. Differences in scores reflect differences in the generators, not differences in the evaluator. The evaluator is the constant.

## Per-Pair Detail

Individual scores for every pair are in:
- `faithfulness_nli_per_pair.csv` (gold standard)
- `faithfulness_per_pair.csv` (token-overlap)
- `question_quality_per_pair.csv`
- `diversity_per_pair.csv`

# Stage 2 Q&A Dataset — Evaluation Report

**Source:** `augmented.jsonl`
**Pairs evaluated:** 196
**Evaluation method:** independent of generation LLM (token-overlap + NLI + sentence-transformers)

---

## Headline Numbers

| Metric | Result | Target | Status |
|---|---:|---:|:---:|
| **Faithful pairs (NLI, gold standard)** | **83.01%** | >= 80% | PASS |
| Contradicted claims (NLI) | 6.53% | <= 1% | FAIL |
| Faithful pairs (token-overlap, fast check) | 85.2% | >= 80% | PASS |
| Suspicious pairs (token-overlap) | 6.12% | <= 5% | FAIL |
| Generic questions | 1.46% | <= 5.0% | PASS |
| Short questions | 6.31% | <= 10% | PASS |
| Q-A mean cosine | 0.4601 | >= 0.5 | FAIL |
| Near-duplicate Qs | 39.32% | <= 5.0% | FAIL |

## 1a. Faithfulness — NLI Gold Standard

Method: NLI (DeBERTa-v3-MNLI) on sentence-level claims
Model: `MoritzLaurer/DeBERTa-v3-large-mnli-fever-anli-ling-wanli` (independent of generation LLM, deterministic)

**Claim level** (199 sentences across all answers):
- Entailed by chunk: **173** (86.93%)
- Contradicted: 13 (6.53%)
- Neutral (chunk doesn't say): 13

**Pair level**:
- Mean per-pair score: **0.8731**
- Median per-pair score: 1.0
- Faithful: 171 (83.01%)
- Partial: 2 (0.97%)
- Unfaithful: 24 (11.65%)
- No_claims: 9 (4.37%)

## 1b. Faithfulness — Token-Overlap (Fast Cross-Check)

Method: token-overlap (stopwords removed, lightly stemmed); untestable pairs excluded
- Mean overlap score: **0.889**
- Median overlap score: 1.0
- Faithful (>= 0.70 overlap): **167** (85.2%)
- Partial (0.40-0.70 overlap): 17 (8.67%)
- Suspicious (< 0.40 overlap): 12 (6.12%)

_Both faithfulness methods are reported. NLI is the primary metric. Token-overlap is a fast sanity check — methods should broadly agree._

## 2. Question Quality

- Average question length: **12.8** words (median 12, range 5-26)
- Generic / meta-textual questions: **3** (1.46%)
- Type distribution:
   - what: 97 (47.09%)
   - other: 43 (20.87%)
   - how: 30 (14.56%)
   - which: 28 (13.59%)
   - yes/no: 4 (1.94%)
   - why: 2 (0.97%)
   - when: 2 (0.97%)

## 3. Diversity and Q-A Relevance

Embedding model: `sentence-transformers/all-MiniLM-L6-v2`

**Q-A relevance** (does the answer address the question?):
- Mean cosine: **0.4601**
- % above 0.70 (highly relevant): 14.56%
- % below 0.30 (off-topic): 22.82%

**Question diversity** (are questions different from each other?):
- Mean nearest-neighbor cosine: 0.9184
- Near-duplicates (> 0.95): **81** (39.32%)
- Very-close pairs (> 0.90): 154

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

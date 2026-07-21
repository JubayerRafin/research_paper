# Stage 2 Q&A Dataset — Evaluation Report

**Source:** `augmented.jsonl`
**Pairs evaluated:** 1597
**Evaluation method:** independent of generation LLM (token-overlap + NLI + sentence-transformers)

---

## Headline Numbers

| Metric | Result | Target | Status |
|---|---:|---:|:---:|
| **Faithful pairs (NLI, gold standard)** | **92.97%** | >= 80% | PASS |
| Contradicted claims (NLI) | 3.83% | <= 1% | FAIL |
| Faithful pairs (token-overlap, fast check) | 92.74% | >= 80% | PASS |
| Suspicious pairs (token-overlap) | 1.69% | <= 5% | PASS |
| Generic questions | 0.68% | <= 5.0% | PASS |
| Short questions | 4.54% | <= 10% | PASS |
| Q-A mean cosine | 0.5678 | >= 0.5 | PASS |
| Near-duplicate Qs | 21.84% | <= 5.0% | FAIL |

## 1a. Faithfulness — NLI Gold Standard

Method: NLI (DeBERTa-v3-MNLI) on sentence-level claims
Model: `MoritzLaurer/DeBERTa-v3-large-mnli-fever-anli-ling-wanli` (independent of generation LLM, deterministic)

**Claim level** (1828 sentences across all answers):
- Entailed by chunk: **1718** (93.98%)
- Contradicted: 70 (3.83%)
- Neutral (chunk doesn't say): 40

**Pair level**:
- Mean per-pair score: **0.9444**
- Median per-pair score: 1.0
- Faithful: 1494 (92.97%)
- Partial: 7 (0.44%)
- Unfaithful: 103 (6.41%)
- No_claims: 3 (0.19%)

## 1b. Faithfulness — Token-Overlap (Fast Cross-Check)

Method: token-overlap (stopwords removed, lightly stemmed); untestable pairs excluded
- Mean overlap score: **0.9048**
- Median overlap score: 0.9459
- Faithful (>= 0.70 overlap): **1481** (92.74%)
- Partial (0.40-0.70 overlap): 89 (5.57%)
- Suspicious (< 0.40 overlap): 27 (1.69%)

_Both faithfulness methods are reported. NLI is the primary metric. Token-overlap is a fast sanity check — methods should broadly agree._

## 2. Question Quality

- Average question length: **13.0** words (median 13, range 4-27)
- Generic / meta-textual questions: **11** (0.68%)
- Type distribution:
   - what: 605 (37.65%)
   - how: 431 (26.82%)
   - other: 359 (22.34%)
   - which: 108 (6.72%)
   - when: 28 (1.74%)
   - yes/no: 27 (1.68%)
   - where: 26 (1.62%)
   - why: 23 (1.43%)

## 3. Diversity and Q-A Relevance

Embedding model: `sentence-transformers/all-MiniLM-L6-v2`

**Q-A relevance** (does the answer address the question?):
- Mean cosine: **0.5678**
- % above 0.70 (highly relevant): 26.14%
- % below 0.30 (off-topic): 8.84%

**Question diversity** (are questions different from each other?):
- Mean nearest-neighbor cosine: 0.9065
- Near-duplicates (> 0.95): **351** (21.84%)
- Very-close pairs (> 0.90): 1053

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

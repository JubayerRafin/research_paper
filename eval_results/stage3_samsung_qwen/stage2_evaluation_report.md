# Stage 2 Q&A Dataset — Evaluation Report

**Source:** `augmented.jsonl`
**Pairs evaluated:** 1934
**Evaluation method:** independent of generation LLM (token-overlap + NLI + sentence-transformers)

---

## Headline Numbers

| Metric | Result | Target | Status |
|---|---:|---:|:---:|
| **Faithful pairs (NLI, gold standard)** | **86.13%** | >= 80% | PASS |
| Contradicted claims (NLI) | 9.52% | <= 1% | FAIL |
| Faithful pairs (token-overlap, fast check) | 93.43% | >= 80% | PASS |
| Suspicious pairs (token-overlap) | 0.57% | <= 5% | PASS |
| Generic questions | 0.52% | <= 5.0% | PASS |
| Short questions | 5.05% | <= 10% | PASS |
| Q-A mean cosine | 0.5289 | >= 0.5 | PASS |
| Near-duplicate Qs | 20.11% | <= 5.0% | FAIL |

## 1a. Faithfulness — NLI Gold Standard

Method: NLI (DeBERTa-v3-MNLI) on sentence-level claims
Model: `MoritzLaurer/DeBERTa-v3-large-mnli-fever-anli-ling-wanli` (independent of generation LLM, deterministic)

**Claim level** (1974 sentences across all answers):
- Entailed by chunk: **1705** (86.37%)
- Contradicted: 188 (9.52%)
- Neutral (chunk doesn't say): 81

**Pair level**:
- Mean per-pair score: **0.8669**
- Median per-pair score: 1.0
- Faithful: 1670 (86.13%)
- Partial: 8 (0.41%)
- Unfaithful: 257 (13.25%)
- No_claims: 4 (0.21%)

## 1b. Faithfulness — Token-Overlap (Fast Cross-Check)

Method: token-overlap (stopwords removed, lightly stemmed); untestable pairs excluded
- Mean overlap score: **0.9197**
- Median overlap score: 1.0
- Faithful (>= 0.70 overlap): **1807** (93.43%)
- Partial (0.40-0.70 overlap): 116 (6.0%)
- Suspicious (< 0.40 overlap): 11 (0.57%)

_Both faithfulness methods are reported. NLI is the primary metric. Token-overlap is a fast sanity check — methods should broadly agree._

## 2. Question Quality

- Average question length: **13.0** words (median 13, range 4-32)
- Generic / meta-textual questions: **10** (0.52%)
- Type distribution:
   - what: 747 (38.53%)
   - how: 513 (26.46%)
   - other: 450 (23.21%)
   - which: 134 (6.91%)
   - when: 34 (1.75%)
   - why: 26 (1.34%)
   - yes/no: 25 (1.29%)
   - where: 10 (0.52%)

## 3. Diversity and Q-A Relevance

Embedding model: `sentence-transformers/all-MiniLM-L6-v2`

**Q-A relevance** (does the answer address the question?):
- Mean cosine: **0.5289**
- % above 0.70 (highly relevant): 19.44%
- % below 0.30 (off-topic): 13.15%

**Question diversity** (are questions different from each other?):
- Mean nearest-neighbor cosine: 0.9016
- Near-duplicates (> 0.95): **390** (20.11%)
- Very-close pairs (> 0.90): 1171

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

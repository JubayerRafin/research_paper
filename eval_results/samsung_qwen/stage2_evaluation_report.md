# Stage 2 Q&A Dataset — Evaluation Report

**Source:** `samsung_qwen.jsonl`
**Pairs evaluated:** 528
**Evaluation method:** independent of generation LLM (token-overlap + NLI + sentence-transformers)

---

## Headline Numbers

| Metric | Result | Target | Status |
|---|---:|---:|:---:|
| **Faithful pairs (NLI, gold standard)** | **85.09%** | >= 80% | PASS |
| Contradicted claims (NLI) | 10.39% | <= 1% | FAIL |
| Faithful pairs (token-overlap, fast check) | 93.56% | >= 80% | PASS |
| Suspicious pairs (token-overlap) | 0.57% | <= 5% | PASS |
| Generic questions | 0.75% | <= 5.0% | PASS |
| Short questions | 6.98% | <= 10% | PASS |
| Q-A mean cosine | 0.5557 | >= 0.5 | PASS |
| Near-duplicate Qs | 0.0% | <= 5.0% | PASS |

## 1a. Faithfulness — NLI Gold Standard

Method: NLI (DeBERTa-v3-MNLI) on sentence-level claims
Model: `MoritzLaurer/DeBERTa-v3-large-mnli-fever-anli-ling-wanli` (independent of generation LLM, deterministic)

**Claim level** (539 sentences across all answers):
- Entailed by chunk: **460** (85.34%)
- Contradicted: 56 (10.39%)
- Neutral (chunk doesn't say): 23

**Pair level**:
- Mean per-pair score: **0.8563**
- Median per-pair score: 1.0
- Faithful: 451 (85.09%)
- Partial: 2 (0.38%)
- Unfaithful: 76 (14.34%)
- No_claims: 1 (0.19%)

## 1b. Faithfulness — Token-Overlap (Fast Cross-Check)

Method: token-overlap (stopwords removed, lightly stemmed); untestable pairs excluded
- Mean overlap score: **0.9208**
- Median overlap score: 1.0
- Faithful (>= 0.70 overlap): **494** (93.56%)
- Partial (0.40-0.70 overlap): 31 (5.87%)
- Suspicious (< 0.40 overlap): 3 (0.57%)

_Both faithfulness methods are reported. NLI is the primary metric. Token-overlap is a fast sanity check — methods should broadly agree._

## 2. Question Quality

- Average question length: **12.3** words (median 12, range 5-28)
- Generic / meta-textual questions: **4** (0.75%)
- Type distribution:
   - what: 263 (49.62%)
   - how: 240 (45.28%)
   - which: 15 (2.83%)
   - other: 6 (1.13%)
   - why: 2 (0.38%)
   - when: 2 (0.38%)
   - yes/no: 1 (0.19%)
   - where: 1 (0.19%)

## 3. Diversity and Q-A Relevance

Embedding model: `sentence-transformers/all-MiniLM-L6-v2`

**Q-A relevance** (does the answer address the question?):
- Mean cosine: **0.5557**
- % above 0.70 (highly relevant): 25.09%
- % below 0.30 (off-topic): 10.38%

**Question diversity** (are questions different from each other?):
- Mean nearest-neighbor cosine: 0.6561
- Near-duplicates (> 0.95): **0** (0.0%)
- Very-close pairs (> 0.90): 16

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

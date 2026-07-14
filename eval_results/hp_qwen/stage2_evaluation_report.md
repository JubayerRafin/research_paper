# Stage 2 Q&A Dataset — Evaluation Report

**Source:** `hp_qwen.jsonl`
**Pairs evaluated:** 441
**Evaluation method:** independent of generation LLM (token-overlap + NLI + sentence-transformers)

---

## Headline Numbers

| Metric | Result | Target | Status |
|---|---:|---:|:---:|
| **Faithful pairs (NLI, gold standard)** | **92.79%** | >= 80% | PASS |
| Contradicted claims (NLI) | 3.95% | <= 1% | FAIL |
| Faithful pairs (token-overlap, fast check) | 92.29% | >= 80% | PASS |
| Suspicious pairs (token-overlap) | 1.59% | <= 5% | PASS |
| Generic questions | 1.35% | <= 5.0% | PASS |
| Short questions | 5.86% | <= 10% | PASS |
| Q-A mean cosine | 0.5913 | >= 0.5 | PASS |
| Near-duplicate Qs | 0.0% | <= 5.0% | PASS |

## 1a. Faithfulness — NLI Gold Standard

Method: NLI (DeBERTa-v3-MNLI) on sentence-level claims
Model: `MoritzLaurer/DeBERTa-v3-large-mnli-fever-anli-ling-wanli` (independent of generation LLM, deterministic)

**Claim level** (506 sentences across all answers):
- Entailed by chunk: **475** (93.87%)
- Contradicted: 20 (3.95%)
- Neutral (chunk doesn't say): 11

**Pair level**:
- Mean per-pair score: **0.9427**
- Median per-pair score: 1.0
- Faithful: 412 (92.79%)
- Partial: 2 (0.45%)
- Unfaithful: 29 (6.53%)
- No_claims: 1 (0.23%)

## 1b. Faithfulness — Token-Overlap (Fast Cross-Check)

Method: token-overlap (stopwords removed, lightly stemmed); untestable pairs excluded
- Mean overlap score: **0.9035**
- Median overlap score: 0.9444
- Faithful (>= 0.70 overlap): **407** (92.29%)
- Partial (0.40-0.70 overlap): 27 (6.12%)
- Suspicious (< 0.40 overlap): 7 (1.59%)

_Both faithfulness methods are reported. NLI is the primary metric. Token-overlap is a fast sanity check — methods should broadly agree._

## 2. Question Quality

- Average question length: **12.4** words (median 12, range 5-23)
- Generic / meta-textual questions: **6** (1.35%)
- Type distribution:
   - what: 235 (52.93%)
   - how: 190 (42.79%)
   - other: 9 (2.03%)
   - when: 3 (0.68%)
   - where: 3 (0.68%)
   - which: 2 (0.45%)
   - why: 2 (0.45%)

## 3. Diversity and Q-A Relevance

Embedding model: `sentence-transformers/all-MiniLM-L6-v2`

**Q-A relevance** (does the answer address the question?):
- Mean cosine: **0.5913**
- % above 0.70 (highly relevant): 31.98%
- % below 0.30 (off-topic): 8.56%

**Question diversity** (are questions different from each other?):
- Mean nearest-neighbor cosine: 0.6665
- Near-duplicates (> 0.95): **0** (0.0%)
- Very-close pairs (> 0.90): 8

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

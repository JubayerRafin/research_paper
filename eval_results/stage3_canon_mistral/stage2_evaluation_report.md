# Stage 2 Q&A Dataset — Evaluation Report

**Source:** `augmented.jsonl`
**Pairs evaluated:** 1658
**Evaluation method:** independent of generation LLM (token-overlap + NLI + sentence-transformers)

---

## Headline Numbers

| Metric | Result | Target | Status |
|---|---:|---:|:---:|
| **Faithful pairs (NLI, gold standard)** | **86.22%** | >= 80% | PASS |
| Contradicted claims (NLI) | 4.32% | <= 1% | FAIL |
| Faithful pairs (token-overlap, fast check) | 83.96% | >= 80% | PASS |
| Suspicious pairs (token-overlap) | 2.35% | <= 5% | PASS |
| Generic questions | 0.0% | <= 5.0% | PASS |
| Short questions | 2.83% | <= 10% | PASS |
| Q-A mean cosine | 0.6325 | >= 0.5 | PASS |
| Near-duplicate Qs | 14.86% | <= 5.0% | FAIL |

## 1a. Faithfulness — NLI Gold Standard

Method: NLI (DeBERTa-v3-MNLI) on sentence-level claims
Model: `MoritzLaurer/DeBERTa-v3-large-mnli-fever-anli-ling-wanli` (independent of generation LLM, deterministic)

**Claim level** (1829 sentences across all answers):
- Entailed by chunk: **1590** (86.93%)
- Contradicted: 79 (4.32%)
- Neutral (chunk doesn't say): 160

**Pair level**:
- Mean per-pair score: **0.8734**
- Median per-pair score: 1.0
- Faithful: 1433 (86.22%)
- Partial: 18 (1.08%)
- Unfaithful: 211 (12.7%)

## 1b. Faithfulness — Token-Overlap (Fast Cross-Check)

Method: token-overlap (stopwords removed, lightly stemmed); untestable pairs excluded
- Mean overlap score: **0.874**
- Median overlap score: 1.0
- Faithful (>= 0.70 overlap): **1392** (83.96%)
- Partial (0.40-0.70 overlap): 227 (13.69%)
- Suspicious (< 0.40 overlap): 39 (2.35%)

_Both faithfulness methods are reported. NLI is the primary metric. Token-overlap is a fast sanity check — methods should broadly agree._

## 2. Question Quality

- Average question length: **12.4** words (median 12, range 6-24)
- Generic / meta-textual questions: **0** (0.0%)
- Type distribution:
   - how: 605 (36.4%)
   - what: 579 (34.84%)
   - other: 358 (21.54%)
   - which: 55 (3.31%)
   - when: 34 (2.05%)
   - where: 15 (0.9%)
   - yes/no: 13 (0.78%)
   - why: 3 (0.18%)

## 3. Diversity and Q-A Relevance

Embedding model: `sentence-transformers/all-MiniLM-L6-v2`

**Q-A relevance** (does the answer address the question?):
- Mean cosine: **0.6325**
- % above 0.70 (highly relevant): 39.71%
- % below 0.30 (off-topic): 4.63%

**Question diversity** (are questions different from each other?):
- Mean nearest-neighbor cosine: 0.8932
- Near-duplicates (> 0.95): **247** (14.86%)
- Very-close pairs (> 0.90): 911

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

# Stage 2 Q&A Dataset — Evaluation Report

**Source:** `augmented.jsonl`
**Pairs evaluated:** 1346
**Evaluation method:** independent of generation LLM (token-overlap + NLI + sentence-transformers)

---

## Headline Numbers

| Metric | Result | Target | Status |
|---|---:|---:|:---:|
| **Faithful pairs (NLI, gold standard)** | **93.63%** | >= 80% | PASS |
| Contradicted claims (NLI) | 2.35% | <= 1% | FAIL |
| Faithful pairs (token-overlap, fast check) | 94.5% | >= 80% | PASS |
| Suspicious pairs (token-overlap) | 0.0% | <= 5% | PASS |
| Generic questions | 1.78% | <= 5.0% | PASS |
| Short questions | 6.44% | <= 10% | PASS |
| Q-A mean cosine | 0.5499 | >= 0.5 | PASS |
| Near-duplicate Qs | 13.11% | <= 5.0% | FAIL |

## 1a. Faithfulness — NLI Gold Standard

Method: NLI (DeBERTa-v3-MNLI) on sentence-level claims
Model: `MoritzLaurer/DeBERTa-v3-large-mnli-fever-anli-ling-wanli` (independent of generation LLM, deterministic)

**Claim level** (1446 sentences across all answers):
- Entailed by chunk: **1360** (94.05%)
- Contradicted: 34 (2.35%)
- Neutral (chunk doesn't say): 52

**Pair level**:
- Mean per-pair score: **0.9448**
- Median per-pair score: 1.0
- Faithful: 1264 (93.63%)
- Partial: 15 (1.11%)
- Unfaithful: 71 (5.26%)

## 1b. Faithfulness — Token-Overlap (Fast Cross-Check)

Method: token-overlap (stopwords removed, lightly stemmed); untestable pairs excluded
- Mean overlap score: **0.9136**
- Median overlap score: 1.0
- Faithful (>= 0.70 overlap): **1272** (94.5%)
- Partial (0.40-0.70 overlap): 74 (5.5%)
- Suspicious (< 0.40 overlap): 0 (0.0%)

_Both faithfulness methods are reported. NLI is the primary metric. Token-overlap is a fast sanity check — methods should broadly agree._

## 2. Question Quality

- Average question length: **12.5** words (median 12, range 4-26)
- Generic / meta-textual questions: **24** (1.78%)
- Type distribution:
   - what: 503 (37.26%)
   - how: 429 (31.78%)
   - other: 299 (22.15%)
   - which: 58 (4.3%)
   - when: 26 (1.93%)
   - yes/no: 20 (1.48%)
   - why: 9 (0.67%)
   - where: 6 (0.44%)

## 3. Diversity and Q-A Relevance

Embedding model: `sentence-transformers/all-MiniLM-L6-v2`

**Q-A relevance** (does the answer address the question?):
- Mean cosine: **0.5499**
- % above 0.70 (highly relevant): 23.85%
- % below 0.30 (off-topic): 13.19%

**Question diversity** (are questions different from each other?):
- Mean nearest-neighbor cosine: 0.8859
- Near-duplicates (> 0.95): **177** (13.11%)
- Very-close pairs (> 0.90): 644

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

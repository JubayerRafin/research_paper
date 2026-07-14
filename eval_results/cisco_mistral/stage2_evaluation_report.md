# Stage 2 Q&A Dataset — Evaluation Report

**Source:** `cisco_mistral.jsonl`
**Pairs evaluated:** 92
**Evaluation method:** independent of generation LLM (token-overlap + NLI + sentence-transformers)

---

## Headline Numbers

| Metric | Result | Target | Status |
|---|---:|---:|:---:|
| **Faithful pairs (NLI, gold standard)** | **88.54%** | >= 80% | PASS |
| Contradicted claims (NLI) | 1.02% | <= 1% | FAIL |
| Faithful pairs (token-overlap, fast check) | 80.43% | >= 80% | PASS |
| Suspicious pairs (token-overlap) | 4.35% | <= 5% | PASS |
| Generic questions | 0.0% | <= 5.0% | PASS |
| Short questions | 1.04% | <= 10% | PASS |
| Q-A mean cosine | 0.6946 | >= 0.5 | PASS |
| Near-duplicate Qs | 0.0% | <= 5.0% | PASS |

## 1a. Faithfulness — NLI Gold Standard

Method: NLI (DeBERTa-v3-MNLI) on sentence-level claims
Model: `MoritzLaurer/DeBERTa-v3-large-mnli-fever-anli-ling-wanli` (independent of generation LLM, deterministic)

**Claim level** (98 sentences across all answers):
- Entailed by chunk: **88** (89.8%)
- Contradicted: 1 (1.02%)
- Neutral (chunk doesn't say): 9

**Pair level**:
- Mean per-pair score: **0.8947**
- Median per-pair score: 1.0
- Faithful: 85 (88.54%)
- Unfaithful: 10 (10.42%)
- No_claims: 1 (1.04%)

## 1b. Faithfulness — Token-Overlap (Fast Cross-Check)

Method: token-overlap (stopwords removed, lightly stemmed); untestable pairs excluded
- Mean overlap score: **0.8565**
- Median overlap score: 0.9333
- Faithful (>= 0.70 overlap): **74** (80.43%)
- Partial (0.40-0.70 overlap): 14 (15.22%)
- Suspicious (< 0.40 overlap): 4 (4.35%)

_Both faithfulness methods are reported. NLI is the primary metric. Token-overlap is a fast sanity check — methods should broadly agree._

## 2. Question Quality

- Average question length: **13.1** words (median 13, range 5-22)
- Generic / meta-textual questions: **0** (0.0%)
- Type distribution:
   - what: 57 (59.38%)
   - how: 39 (40.62%)

## 3. Diversity and Q-A Relevance

Embedding model: `sentence-transformers/all-MiniLM-L6-v2`

**Q-A relevance** (does the answer address the question?):
- Mean cosine: **0.6946**
- % above 0.70 (highly relevant): 57.29%
- % below 0.30 (off-topic): 8.33%

**Question diversity** (are questions different from each other?):
- Mean nearest-neighbor cosine: 0.6514
- Near-duplicates (> 0.95): **0** (0.0%)
- Very-close pairs (> 0.90): 0

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

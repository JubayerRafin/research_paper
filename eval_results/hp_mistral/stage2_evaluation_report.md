# Stage 2 Q&A Dataset — Evaluation Report

**Source:** `hp_mistral.jsonl`
**Pairs evaluated:** 611
**Evaluation method:** independent of generation LLM (token-overlap + NLI + sentence-transformers)

---

## Headline Numbers

| Metric | Result | Target | Status |
|---|---:|---:|:---:|
| **Faithful pairs (NLI, gold standard)** | **87.25%** | >= 80% | PASS |
| Contradicted claims (NLI) | 6.01% | <= 1% | FAIL |
| Faithful pairs (token-overlap, fast check) | 91.49% | >= 80% | PASS |
| Suspicious pairs (token-overlap) | 2.29% | <= 5% | PASS |
| Generic questions | 0.49% | <= 5.0% | PASS |
| Short questions | 2.61% | <= 10% | PASS |
| Q-A mean cosine | 0.6435 | >= 0.5 | PASS |
| Near-duplicate Qs | 0.0% | <= 5.0% | PASS |

## 1a. Faithfulness — NLI Gold Standard

Method: NLI (DeBERTa-v3-MNLI) on sentence-level claims
Model: `MoritzLaurer/DeBERTa-v3-large-mnli-fever-anli-ling-wanli` (independent of generation LLM, deterministic)

**Claim level** (716 sentences across all answers):
- Entailed by chunk: **629** (87.85%)
- Contradicted: 43 (6.01%)
- Neutral (chunk doesn't say): 44

**Pair level**:
- Mean per-pair score: **0.8889**
- Median per-pair score: 1.0
- Faithful: 534 (87.25%)
- Partial: 5 (0.82%)
- Unfaithful: 71 (11.6%)
- No_claims: 2 (0.33%)

## 1b. Faithfulness — Token-Overlap (Fast Cross-Check)

Method: token-overlap (stopwords removed, lightly stemmed); untestable pairs excluded
- Mean overlap score: **0.9075**
- Median overlap score: 1.0
- Faithful (>= 0.70 overlap): **559** (91.49%)
- Partial (0.40-0.70 overlap): 38 (6.22%)
- Suspicious (< 0.40 overlap): 14 (2.29%)

_Both faithfulness methods are reported. NLI is the primary metric. Token-overlap is a fast sanity check — methods should broadly agree._

## 2. Question Quality

- Average question length: **12.4** words (median 12, range 5-23)
- Generic / meta-textual questions: **3** (0.49%)
- Type distribution:
   - what: 324 (52.94%)
   - how: 286 (46.73%)
   - where: 1 (0.16%)
   - why: 1 (0.16%)

## 3. Diversity and Q-A Relevance

Embedding model: `sentence-transformers/all-MiniLM-L6-v2`

**Q-A relevance** (does the answer address the question?):
- Mean cosine: **0.6435**
- % above 0.70 (highly relevant): 45.1%
- % below 0.30 (off-topic): 7.19%

**Question diversity** (are questions different from each other?):
- Mean nearest-neighbor cosine: 0.7213
- Near-duplicates (> 0.95): **0** (0.0%)
- Very-close pairs (> 0.90): 14

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

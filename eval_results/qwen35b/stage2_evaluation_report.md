# Stage 2 Q&A Dataset — Evaluation Report

**Source:** `canon_qwen35b_qa.jsonl`
**Pairs evaluated:** 416
**Evaluation method:** independent of generation LLM (token-overlap + NLI + sentence-transformers)

---

## Headline Numbers

| Metric | Result | Target | Status |
|---|---:|---:|:---:|
| **Faithful pairs (NLI, gold standard)** | **94.47%** | >= 80% | PASS |
| Contradicted claims (NLI) | 1.41% | <= 1% | FAIL |
| Faithful pairs (token-overlap, fast check) | 94.95% | >= 80% | PASS |
| Suspicious pairs (token-overlap) | 0.72% | <= 5% | PASS |
| Generic questions | 2.64% | <= 5.0% | PASS |
| Short questions | 10.34% | <= 10% | FAIL |
| Q-A mean cosine | 0.6106 | >= 0.5 | PASS |
| Near-duplicate Qs | 0.0% | <= 5.0% | PASS |

## 1a. Faithfulness — NLI Gold Standard

Method: NLI (DeBERTa-v3-MNLI) on sentence-level claims
Model: `MoritzLaurer/DeBERTa-v3-large-mnli-fever-anli-ling-wanli` (independent of generation LLM, deterministic)

**Claim level** (426 sentences across all answers):
- Entailed by chunk: **403** (94.6%)
- Contradicted: 6 (1.41%)
- Neutral (chunk doesn't say): 17

**Pair level**:
- Mean per-pair score: **0.9459**
- Median per-pair score: 1.0
- Faithful: 393 (94.47%)
- Partial: 1 (0.24%)
- Unfaithful: 22 (5.29%)

## 1b. Faithfulness — Token-Overlap (Fast Cross-Check)

Method: token-overlap (stopwords removed, lightly stemmed); untestable pairs excluded
- Mean overlap score: **0.9291**
- Median overlap score: 1.0
- Faithful (>= 0.70 overlap): **395** (94.95%)
- Partial (0.40-0.70 overlap): 18 (4.33%)
- Suspicious (< 0.40 overlap): 3 (0.72%)

_Both faithfulness methods are reported. NLI is the primary metric. Token-overlap is a fast sanity check — methods should broadly agree._

## 2. Question Quality

- Average question length: **11.6** words (median 11, range 5-25)
- Generic / meta-textual questions: **11** (2.64%)
- Type distribution:
   - what: 209 (50.24%)
   - how: 203 (48.8%)
   - when: 4 (0.96%)

## 3. Diversity and Q-A Relevance

Embedding model: `sentence-transformers/all-MiniLM-L6-v2`

**Q-A relevance** (does the answer address the question?):
- Mean cosine: **0.6106**
- % above 0.70 (highly relevant): 37.5%
- % below 0.30 (off-topic): 8.65%

**Question diversity** (are questions different from each other?):
- Mean nearest-neighbor cosine: 0.6981
- Near-duplicates (> 0.95): **0** (0.0%)
- Very-close pairs (> 0.90): 13

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

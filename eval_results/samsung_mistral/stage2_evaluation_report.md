# Stage 2 Q&A Dataset — Evaluation Report

**Source:** `samsung_mistral.jsonl`
**Pairs evaluated:** 715
**Evaluation method:** independent of generation LLM (token-overlap + NLI + sentence-transformers)

---

## Headline Numbers

| Metric | Result | Target | Status |
|---|---:|---:|:---:|
| **Faithful pairs (NLI, gold standard)** | **82.4%** | >= 80% | PASS |
| Contradicted claims (NLI) | 5.76% | <= 1% | FAIL |
| Faithful pairs (token-overlap, fast check) | 90.21% | >= 80% | PASS |
| Suspicious pairs (token-overlap) | 2.24% | <= 5% | PASS |
| Generic questions | 0.0% | <= 5.0% | PASS |
| Short questions | 4.33% | <= 10% | PASS |
| Q-A mean cosine | 0.6541 | >= 0.5 | PASS |
| Near-duplicate Qs | 0.0% | <= 5.0% | PASS |

## 1a. Faithfulness — NLI Gold Standard

Method: NLI (DeBERTa-v3-MNLI) on sentence-level claims
Model: `MoritzLaurer/DeBERTa-v3-large-mnli-fever-anli-ling-wanli` (independent of generation LLM, deterministic)

**Claim level** (798 sentences across all answers):
- Entailed by chunk: **669** (83.83%)
- Contradicted: 46 (5.76%)
- Neutral (chunk doesn't say): 83

**Pair level**:
- Mean per-pair score: **0.8343**
- Median per-pair score: 1.0
- Faithful: 590 (82.4%)
- Partial: 7 (0.98%)
- Unfaithful: 118 (16.48%)
- No_claims: 1 (0.14%)

## 1b. Faithfulness — Token-Overlap (Fast Cross-Check)

Method: token-overlap (stopwords removed, lightly stemmed); untestable pairs excluded
- Mean overlap score: **0.9041**
- Median overlap score: 1.0
- Faithful (>= 0.70 overlap): **645** (90.21%)
- Partial (0.40-0.70 overlap): 54 (7.55%)
- Suspicious (< 0.40 overlap): 16 (2.24%)

_Both faithfulness methods are reported. NLI is the primary metric. Token-overlap is a fast sanity check — methods should broadly agree._

## 2. Question Quality

- Average question length: **12.1** words (median 12, range 6-27)
- Generic / meta-textual questions: **0** (0.0%)
- Type distribution:
   - how: 366 (51.12%)
   - what: 344 (48.04%)
   - which: 3 (0.42%)
   - when: 2 (0.28%)
   - why: 1 (0.14%)

## 3. Diversity and Q-A Relevance

Embedding model: `sentence-transformers/all-MiniLM-L6-v2`

**Q-A relevance** (does the answer address the question?):
- Mean cosine: **0.6541**
- % above 0.70 (highly relevant): 46.09%
- % below 0.30 (off-topic): 4.33%

**Question diversity** (are questions different from each other?):
- Mean nearest-neighbor cosine: 0.6977
- Near-duplicates (> 0.95): **0** (0.0%)
- Very-close pairs (> 0.90): 19

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

# Stage 2 Q&A Dataset — Evaluation Report

**Source:** `cisco_qwen.jsonl`
**Pairs evaluated:** 60
**Evaluation method:** independent of generation LLM (token-overlap + NLI + sentence-transformers)

---

## Headline Numbers

| Metric | Result | Target | Status |
|---|---:|---:|:---:|
| **Faithful pairs (NLI, gold standard)** | **81.25%** | >= 80% | PASS |
| Contradicted claims (NLI) | 8.06% | <= 1% | FAIL |
| Faithful pairs (token-overlap, fast check) | 86.67% | >= 80% | PASS |
| Suspicious pairs (token-overlap) | 5.0% | <= 5% | PASS |
| Generic questions | 3.12% | <= 5.0% | PASS |
| Short questions | 6.25% | <= 10% | PASS |
| Q-A mean cosine | 0.4782 | >= 0.5 | FAIL |
| Near-duplicate Qs | 0.0% | <= 5.0% | PASS |

## 1a. Faithfulness — NLI Gold Standard

Method: NLI (DeBERTa-v3-MNLI) on sentence-level claims
Model: `MoritzLaurer/DeBERTa-v3-large-mnli-fever-anli-ling-wanli` (independent of generation LLM, deterministic)

**Claim level** (62 sentences across all answers):
- Entailed by chunk: **53** (85.48%)
- Contradicted: 5 (8.06%)
- Neutral (chunk doesn't say): 4

**Pair level**:
- Mean per-pair score: **0.8607**
- Median per-pair score: 1.0
- Faithful: 52 (81.25%)
- Partial: 1 (1.56%)
- Unfaithful: 8 (12.5%)
- No_claims: 3 (4.69%)

## 1b. Faithfulness — Token-Overlap (Fast Cross-Check)

Method: token-overlap (stopwords removed, lightly stemmed); untestable pairs excluded
- Mean overlap score: **0.8974**
- Median overlap score: 1.0
- Faithful (>= 0.70 overlap): **52** (86.67%)
- Partial (0.40-0.70 overlap): 5 (8.33%)
- Suspicious (< 0.40 overlap): 3 (5.0%)

_Both faithfulness methods are reported. NLI is the primary metric. Token-overlap is a fast sanity check — methods should broadly agree._

## 2. Question Quality

- Average question length: **12.5** words (median 12, range 5-21)
- Generic / meta-textual questions: **2** (3.12%)
- Type distribution:
   - what: 52 (81.25%)
   - how: 11 (17.19%)
   - which: 1 (1.56%)

## 3. Diversity and Q-A Relevance

Embedding model: `sentence-transformers/all-MiniLM-L6-v2`

**Q-A relevance** (does the answer address the question?):
- Mean cosine: **0.4782**
- % above 0.70 (highly relevant): 17.19%
- % below 0.30 (off-topic): 20.31%

**Question diversity** (are questions different from each other?):
- Mean nearest-neighbor cosine: 0.6195
- Near-duplicates (> 0.95): **0** (0.0%)
- Very-close pairs (> 0.90): 2

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

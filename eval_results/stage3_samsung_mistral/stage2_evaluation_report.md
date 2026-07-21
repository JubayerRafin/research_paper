# Stage 2 Q&A Dataset — Evaluation Report

**Source:** `augmented.jsonl`
**Pairs evaluated:** 2640
**Evaluation method:** independent of generation LLM (token-overlap + NLI + sentence-transformers)

---

## Headline Numbers

| Metric | Result | Target | Status |
|---|---:|---:|:---:|
| **Faithful pairs (NLI, gold standard)** | **83.06%** | >= 80% | PASS |
| Contradicted claims (NLI) | 5.43% | <= 1% | FAIL |
| Faithful pairs (token-overlap, fast check) | 90.45% | >= 80% | PASS |
| Suspicious pairs (token-overlap) | 2.2% | <= 5% | PASS |
| Generic questions | 0.0% | <= 5.0% | PASS |
| Short questions | 3.06% | <= 10% | PASS |
| Q-A mean cosine | 0.6177 | >= 0.5 | PASS |
| Near-duplicate Qs | 17.06% | <= 5.0% | FAIL |

## 1a. Faithfulness — NLI Gold Standard

Method: NLI (DeBERTa-v3-MNLI) on sentence-level claims
Model: `MoritzLaurer/DeBERTa-v3-large-mnli-fever-anli-ling-wanli` (independent of generation LLM, deterministic)

**Claim level** (2948 sentences across all answers):
- Entailed by chunk: **2490** (84.46%)
- Contradicted: 160 (5.43%)
- Neutral (chunk doesn't say): 298

**Pair level**:
- Mean per-pair score: **0.8413**
- Median per-pair score: 1.0
- Faithful: 2196 (83.06%)
- Partial: 27 (1.02%)
- Unfaithful: 417 (15.77%)
- No_claims: 4 (0.15%)

## 1b. Faithfulness — Token-Overlap (Fast Cross-Check)

Method: token-overlap (stopwords removed, lightly stemmed); untestable pairs excluded
- Mean overlap score: **0.9059**
- Median overlap score: 1.0
- Faithful (>= 0.70 overlap): **2388** (90.45%)
- Partial (0.40-0.70 overlap): 194 (7.35%)
- Suspicious (< 0.40 overlap): 58 (2.2%)

_Both faithfulness methods are reported. NLI is the primary metric. Token-overlap is a fast sanity check — methods should broadly agree._

## 2. Question Quality

- Average question length: **12.8** words (median 12, range 5-30)
- Generic / meta-textual questions: **0** (0.0%)
- Type distribution:
   - what: 1000 (37.82%)
   - how: 822 (31.09%)
   - other: 613 (23.18%)
   - which: 133 (5.03%)
   - when: 30 (1.13%)
   - yes/no: 25 (0.95%)
   - why: 14 (0.53%)
   - where: 7 (0.26%)

## 3. Diversity and Q-A Relevance

Embedding model: `sentence-transformers/all-MiniLM-L6-v2`

**Q-A relevance** (does the answer address the question?):
- Mean cosine: **0.6177**
- % above 0.70 (highly relevant): 38.01%
- % below 0.30 (off-topic): 6.62%

**Question diversity** (are questions different from each other?):
- Mean nearest-neighbor cosine: 0.8989
- Near-duplicates (> 0.95): **451** (17.06%)
- Very-close pairs (> 0.90): 1558

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

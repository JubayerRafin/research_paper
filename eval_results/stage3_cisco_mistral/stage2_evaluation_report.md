# Stage 2 Q&A Dataset — Evaluation Report

**Source:** `augmented.jsonl`
**Pairs evaluated:** 321
**Evaluation method:** independent of generation LLM (token-overlap + NLI + sentence-transformers)

---

## Headline Numbers

| Metric | Result | Target | Status |
|---|---:|---:|:---:|
| **Faithful pairs (NLI, gold standard)** | **88.36%** | >= 80% | PASS |
| Contradicted claims (NLI) | 0.88% | <= 1% | PASS |
| Faithful pairs (token-overlap, fast check) | 81.0% | >= 80% | PASS |
| Suspicious pairs (token-overlap) | 4.36% | <= 5% | PASS |
| Generic questions | 0.0% | <= 5.0% | PASS |
| Short questions | 1.79% | <= 10% | PASS |
| Q-A mean cosine | 0.6693 | >= 0.5 | PASS |
| Near-duplicate Qs | 33.73% | <= 5.0% | FAIL |

## 1a. Faithfulness — NLI Gold Standard

Method: NLI (DeBERTa-v3-MNLI) on sentence-level claims
Model: `MoritzLaurer/DeBERTa-v3-large-mnli-fever-anli-ling-wanli` (independent of generation LLM, deterministic)

**Claim level** (342 sentences across all answers):
- Entailed by chunk: **307** (89.77%)
- Contradicted: 3 (0.88%)
- Neutral (chunk doesn't say): 32

**Pair level**:
- Mean per-pair score: **0.8943**
- Median per-pair score: 1.0
- Faithful: 296 (88.36%)
- Unfaithful: 35 (10.45%)
- No_claims: 4 (1.19%)

## 1b. Faithfulness — Token-Overlap (Fast Cross-Check)

Method: token-overlap (stopwords removed, lightly stemmed); untestable pairs excluded
- Mean overlap score: **0.8574**
- Median overlap score: 0.9333
- Faithful (>= 0.70 overlap): **260** (81.0%)
- Partial (0.40-0.70 overlap): 47 (14.64%)
- Suspicious (< 0.40 overlap): 14 (4.36%)

_Both faithfulness methods are reported. NLI is the primary metric. Token-overlap is a fast sanity check — methods should broadly agree._

## 2. Question Quality

- Average question length: **13.5** words (median 13, range 5-25)
- Generic / meta-textual questions: **0** (0.0%)
- Type distribution:
   - what: 136 (40.6%)
   - how: 87 (25.97%)
   - other: 64 (19.1%)
   - which: 32 (9.55%)
   - where: 9 (2.69%)
   - yes/no: 3 (0.9%)
   - why: 2 (0.6%)
   - when: 2 (0.6%)

## 3. Diversity and Q-A Relevance

Embedding model: `sentence-transformers/all-MiniLM-L6-v2`

**Q-A relevance** (does the answer address the question?):
- Mean cosine: **0.6693**
- % above 0.70 (highly relevant): 51.34%
- % below 0.30 (off-topic): 8.06%

**Question diversity** (are questions different from each other?):
- Mean nearest-neighbor cosine: 0.9179
- Near-duplicates (> 0.95): **113** (33.73%)
- Very-close pairs (> 0.90): 264

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

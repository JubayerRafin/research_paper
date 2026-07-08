# Stage 2 Q&A Dataset — Evaluation Report

**Source:** `canon_mistral_qa.jsonl`
**Pairs evaluated:** 537
**Evaluation method:** independent of generation LLM (token-overlap + NLI + sentence-transformers)

---

## Headline Numbers

| Metric | Result | Target | Status |
|---|---:|---:|:---:|
| **Faithful pairs (NLI, gold standard)** | **82.59%** | >= 80% | PASS |
| Contradicted claims (NLI) | 3.37% | <= 1% | FAIL |
| Faithful pairs (token-overlap, fast check) | 80.26% | >= 80% | PASS |
| Suspicious pairs (token-overlap) | 2.79% | <= 5% | PASS |
| Generic questions | 0.0% | <= 5.0% | PASS |
| Short questions | 4.63% | <= 10% | PASS |
| Q-A mean cosine | 0.6842 | >= 0.5 | PASS |
| Near-duplicate Qs | 0.0% | <= 5.0% | PASS |

## 1a. Faithfulness — NLI Gold Standard

Method: NLI (DeBERTa-v3-MNLI) on sentence-level claims
Model: `MoritzLaurer/DeBERTa-v3-large-mnli-fever-anli-ling-wanli` (independent of generation LLM, deterministic)

**Claim level** (593 sentences across all answers):
- Entailed by chunk: **494** (83.31%)
- Contradicted: 20 (3.37%)
- Neutral (chunk doesn't say): 79

**Pair level**:
- Mean per-pair score: **0.8324**
- Median per-pair score: 1.0
- Faithful: 446 (82.59%)
- Partial: 3 (0.56%)
- Unfaithful: 91 (16.85%)

## 1b. Faithfulness — Token-Overlap (Fast Cross-Check)

Method: token-overlap (stopwords removed, lightly stemmed); untestable pairs excluded
- Mean overlap score: **0.8659**
- Median overlap score: 1.0
- Faithful (>= 0.70 overlap): **431** (80.26%)
- Partial (0.40-0.70 overlap): 91 (16.95%)
- Suspicious (< 0.40 overlap): 15 (2.79%)

_Both faithfulness methods are reported. NLI is the primary metric. Token-overlap is a fast sanity check — methods should broadly agree._

## 2. Question Quality

- Average question length: **11.7** words (median 11, range 6-29)
- Generic / meta-textual questions: **0** (0.0%)
- Type distribution:
   - how: 349 (64.63%)
   - what: 187 (34.63%)
   - where: 2 (0.37%)
   - yes/no: 1 (0.19%)
   - why: 1 (0.19%)

## 3. Diversity and Q-A Relevance

Embedding model: `sentence-transformers/all-MiniLM-L6-v2`

**Q-A relevance** (does the answer address the question?):
- Mean cosine: **0.6842**
- % above 0.70 (highly relevant): 54.63%
- % below 0.30 (off-topic): 5.0%

**Question diversity** (are questions different from each other?):
- Mean nearest-neighbor cosine: 0.7423
- Near-duplicates (> 0.95): **0** (0.0%)
- Very-close pairs (> 0.90): 32

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

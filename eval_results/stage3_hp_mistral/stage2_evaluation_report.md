# Stage 2 Q&A Dataset — Evaluation Report

**Source:** `augmented.jsonl`
**Pairs evaluated:** 2261
**Evaluation method:** independent of generation LLM (token-overlap + NLI + sentence-transformers)

---

## Headline Numbers

| Metric | Result | Target | Status |
|---|---:|---:|:---:|
| **Faithful pairs (NLI, gold standard)** | **87.51%** | >= 80% | PASS |
| Contradicted claims (NLI) | 6.14% | <= 1% | FAIL |
| Faithful pairs (token-overlap, fast check) | 91.6% | >= 80% | PASS |
| Suspicious pairs (token-overlap) | 2.3% | <= 5% | PASS |
| Generic questions | 0.22% | <= 5.0% | PASS |
| Short questions | 2.91% | <= 10% | PASS |
| Q-A mean cosine | 0.6076 | >= 0.5 | PASS |
| Near-duplicate Qs | 22.91% | <= 5.0% | FAIL |

## 1a. Faithfulness — NLI Gold Standard

Method: NLI (DeBERTa-v3-MNLI) on sentence-level claims
Model: `MoritzLaurer/DeBERTa-v3-large-mnli-fever-anli-ling-wanli` (independent of generation LLM, deterministic)

**Claim level** (2640 sentences across all answers):
- Entailed by chunk: **2323** (87.99%)
- Contradicted: 162 (6.14%)
- Neutral (chunk doesn't say): 155

**Pair level**:
- Mean per-pair score: **0.8922**
- Median per-pair score: 1.0
- Faithful: 1982 (87.51%)
- Partial: 19 (0.84%)
- Unfaithful: 256 (11.3%)
- No_claims: 8 (0.35%)

## 1b. Faithfulness — Token-Overlap (Fast Cross-Check)

Method: token-overlap (stopwords removed, lightly stemmed); untestable pairs excluded
- Mean overlap score: **0.9079**
- Median overlap score: 1.0
- Faithful (>= 0.70 overlap): **2071** (91.6%)
- Partial (0.40-0.70 overlap): 138 (6.1%)
- Suspicious (< 0.40 overlap): 52 (2.3%)

_Both faithfulness methods are reported. NLI is the primary metric. Token-overlap is a fast sanity check — methods should broadly agree._

## 2. Question Quality

- Average question length: **13.0** words (median 13, range 4-31)
- Generic / meta-textual questions: **5** (0.22%)
- Type distribution:
   - what: 882 (38.94%)
   - how: 640 (28.26%)
   - other: 507 (22.38%)
   - which: 140 (6.18%)
   - where: 35 (1.55%)
   - yes/no: 25 (1.1%)
   - when: 21 (0.93%)
   - why: 14 (0.62%)
   - who: 1 (0.04%)

## 3. Diversity and Q-A Relevance

Embedding model: `sentence-transformers/all-MiniLM-L6-v2`

**Q-A relevance** (does the answer address the question?):
- Mean cosine: **0.6076**
- % above 0.70 (highly relevant): 36.47%
- % below 0.30 (off-topic): 8.34%

**Question diversity** (are questions different from each other?):
- Mean nearest-neighbor cosine: 0.905
- Near-duplicates (> 0.95): **519** (22.91%)
- Very-close pairs (> 0.90): 1428

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

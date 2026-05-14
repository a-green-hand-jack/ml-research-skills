# Contamination Checklist

Contamination means that information from the evaluation set influenced training, preprocessing, hyperparameter selection, or model selection in a way that inflates reported performance.

## Category 1 — Split-Level Contamination

| Check | Risk | Mitigation |
|---|---|---|
| Sample appears in both train and test | High — directly inflates performance | Deduplicate before splitting; report deduplication policy |
| Near-duplicate in train and test | Medium — depends on method sensitivity | Near-dedup using MinHash, embedding similarity, or n-gram overlap; report threshold |
| Entity spans multiple splits | High for entity-memorizing models | Group-aware split; report entity boundary definition |
| Preprocessing normalization fit on full dataset | High for leakage of test statistics into train | Fit scaler, vocab, mean/std only on train split |
| Augmentation applied to test set | Medium | Apply augmentation only to train; test uses original examples |

## Category 2 — LLM / Foundation Model Contamination

This is the most common unresolved reviewer concern for NLP/vision benchmarks evaluated with pre-trained models.

| Check | Risk | Mitigation |
|---|---|---|
| Benchmark test examples in pretraining corpus | High — model may have memorized answers | Check against known contamination audits (e.g., GPT-4 technical report, Llama contamination appendix); use n-gram overlap; use exact match hashing |
| Test prompts similar to pretraining instruction-tuning data | Medium | Compare to published instruction-tuning datasets; document as limitation if unknown |
| Eval harness exposes full answer choices in prompt | Medium | Use blind prompting when possible; report prompt format |
| Test set constructed by the same team as the pretraining data | High | Disclose explicitly; prefer third-party evaluation |

### Practical Contamination Audit Steps for LLMs

1. Download or access the benchmark's test split.
2. For each test example, compute 13-gram overlap against the target model's known pretraining sources.
3. Flag examples with >80% 13-gram overlap as contaminated.
4. Report: number flagged, percentage, performance on clean vs flagged subsets.
5. If source corpus is unavailable, state this explicitly and cite the model's contamination analysis if published.

Tools: `lm-contamination-checker`, `bigcode-evaluation-harness` contamination utils, or a simple MinHash LSH over n-grams.

## Category 3 — Hyperparameter and Model Selection Contamination

| Check | Risk | Mitigation |
|---|---|---|
| Best checkpoint selected by test performance | Very high | Use val set for selection; test only for final reporting |
| Hyperparameter search used test performance | Very high | NAS, HPO, or grid search must be run on val only |
| Architecture designed based on test-set ablations | High — test used for design, not evaluation | Report development history honestly; re-evaluate on a held-out reserve |
| Early stopping signal from test loss | High | Use val loss only for stopping |
| Multiple test evaluations without correction | Medium — positive selection bias | Report number of test evaluations and use Bonferroni or equivalent correction if many |

## Category 4 — Retrieval and RAG Contamination

| Check | Risk | Mitigation |
|---|---|---|
| Retrieved documents contain test answer | High | Filter retrieved context for test-adjacent content; or report retrieval-augmented and non-augmented scores separately |
| Retrieval corpus includes test-set questions | High | Exclude test questions from retrieval index |
| Retrieval score used to pick test examples | Medium | Report selection criteria and test on a random sample to check bias |

## Disclosure Policy

When contamination cannot be ruled out:

1. State explicitly in the paper's experimental settings: "We cannot confirm the absence of contamination because [reason]."
2. Report performance on any available clean subset.
3. Cite the model's own contamination analysis or note its absence.
4. Do not claim state-of-the-art performance on benchmarks where contamination is likely.

## Reviewer-Facing Risk Levels

| Level | Description | Required action |
|---|---|---|
| Clean | No known contamination vector | Report dedup and split policies |
| Possible | Known overlap vectors but no confirmed examples | Report audit steps, limits of audit |
| Likely | Overlap confirmed for ≥ 5% of test examples | Recompute on clean subset; report both |
| Unknown | Corpus unavailable for audit | Disclose explicitly; do not overstate claims |

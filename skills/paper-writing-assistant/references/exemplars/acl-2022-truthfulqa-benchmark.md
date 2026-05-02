# TruthfulQA: ACL 2022 Benchmark Exemplar

- Source: https://aclanthology.org/2022.acl-long.229/
- Venue/status: ACL 2022 Long Paper
- Topic: language model truthfulness evaluation
- Positioning: benchmark plus empirical finding
- Best for: benchmark motivation, evaluation validity, result interpretation that challenges scaling assumptions

## Reviewer Promise

Truthfulness requires measuring whether models avoid imitative falsehoods, and such a benchmark reveals failure modes not captured by standard scaling-oriented NLP evaluations.

## Section Patterns

### Abstract

- Defines the benchmark's target property.
- States dataset size and category coverage as protocol facts.
- Reports model and human comparisons.
- Ends with an implication about scaling and training objectives.

### Introduction

- Starts from practical deployment concerns and user-facing harm.
- Converts broad safety concern into a measurable question.
- Defines the failure mode motivating the benchmark.
- Explains why existing performance trends may not apply.

### Benchmark Design

- Defines the construct being measured before dataset details.
- Explains question construction as targeting a specific failure mode.
- Uses categories and human/model comparisons to support validity.

### Experiments and Results

- Compares models and humans to calibrate difficulty and risk.
- Interprets model size trends as a substantive finding.
- Connects false answers to the benchmark's motivating mechanism.

## Micro-Patterns

- Paragraph opening: start from the evaluation question, not the dataset artifact.
- Table caption: identify models, answer-scoring protocol, and metric interpretation.
- Result interpretation: explain why a result contradicts the expected scaling narrative.
- Limitation language: separate benchmark truthfulness from all factuality or safety claims.

## Reuse Cautions

- Benchmark papers need construct validity language; do not only report dataset size.
- Safety implications should be carefully scoped to the measured behavior.

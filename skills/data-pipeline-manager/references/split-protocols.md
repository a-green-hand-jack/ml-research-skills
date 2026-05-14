# Split Protocol Reference

## Core Split Types

### Random Split
- Best for: i.i.d. datasets without known structure
- Risk: silently breaks when examples are not independent (e.g., multiple crops from same image, utterances from same speaker)
- Requirement: fix seed; report seed in paper

### Stratified Split
- Best for: class-imbalanced or multi-label datasets
- Stratify by: class label, domain label, or any variable that must be balanced
- Risk: stratification by a variable correlated with the label can inflate test performance

### Group-Aware Split (No-Leakage Split)
- Use when: multiple examples share a source entity (patient ID, speaker ID, document ID, image sequence)
- Rule: all examples from one entity go to exactly one split
- Risk of not using: inflated test performance when a model memorizes entity-level patterns

### Temporal Split
- Use when: the dataset has a natural time ordering and the deployment scenario involves future data
- Rule: train on past, validate and test on future; never shuffle before splitting
- Risk: future test leakage when any time-based feature engineering looks forward

### Domain Split
- Use when: the paper claims generalization across domains
- Rule: at least one held-out domain must not appear in training
- Risk: if domains are used for hyperparameter search, the domain split is compromised

### Cross-Validation
- Use when: the dataset is too small for a reliable single split, or variance across splits matters
- Requirements: report mean and std across folds; use group-aware CV when entities must not span folds
- Risk: nested CV is expensive; ensure inner loop is not contaminated by outer loop data

## Split Size Guidelines

| Dataset size | Train | Val | Test |
|---|---|---|---|
| < 1k examples | 60% | 20% | 20% |
| 1k–10k | 70% | 15% | 15% |
| 10k–100k | 80% | 10% | 10% |
| > 100k | 90% | 5% | 5% |
| Published benchmark | use official splits |

Always prefer the official benchmark split over a custom split when comparing to published baselines.

## Validation Set Misuse Patterns

These patterns compromise the test set's integrity:

- Using val accuracy as a proxy for early stopping, then also reporting val accuracy as the test metric
- Tuning hyperparameters on the test set directly or by running many experiments and picking the best
- Running the test set more than once during development (report only the final run)
- Using the test set to decide between methods, then claiming the comparison is held out

## Forbidden-Use Policy Template

```markdown
Split: test
Forbidden use:
  - no hyperparameter tuning
  - no threshold selection
  - no method selection
  - no early stopping using test loss
  - only one final evaluation per submitted model
```

## Reviewer Checklist for Splits

- [ ] Are splits defined before method development begins, or at least before seeing their performance?
- [ ] Is the split seed fixed and reported?
- [ ] Are group boundaries respected (no entity spans multiple splits)?
- [ ] For temporal data, is the split causal?
- [ ] Is the val set clearly separated from the test set in all reported metrics?
- [ ] If official splits exist, are they used?
- [ ] Is class distribution reported for each split?

# Diagnosis Taxonomy

Use this taxonomy to classify symptoms and avoid jumping to conclusions.

## Symptom Types

### No Improvement

The method is statistically indistinguishable from baseline.

Common causes:

- effect is too small
- insufficient seeds
- baseline is strong
- method mechanism is irrelevant
- metric does not measure intended improvement
- implementation disabled or ineffective

### Regression

The method is worse than baseline.

Common causes:

- objective conflict
- over-regularization
- training instability
- bug
- unfair hyperparameters
- method assumption false

### Instability or High Variance

Results vary strongly across seeds, checkpoints, or data splits.

Common causes:

- underpowered experiment
- stochastic training instability
- sensitive hyperparameter
- noisy metric
- checkpoint selection bias
- small dataset or evaluation sample

### Metric Conflict

One metric improves while another worsens.

Common causes:

- true tradeoff
- metric mismatch with claim
- postprocessing issue
- evaluation split difference
- overfitting one objective

### Suspiciously Large Gain

The result looks too good.

Common causes:

- data leakage
- train/test contamination
- metric bug
- baseline misconfiguration
- wrong checkpoint
- accidental oracle information

### Baseline Unexpectedly Strong

Baseline closes the gap or beats the method.

Common causes:

- baseline tuning was previously weak
- method contribution is small
- target regime does not need the method
- method adds no useful inductive bias

### Diagnostic / Performance Mismatch

The mechanism diagnostic and final metric disagree.

Common causes:

- diagnostic does not measure the true mechanism
- mechanism changes but is irrelevant to task performance
- performance gain comes from a confound
- claim should be reframed

### Training Failure

Loss diverges, NaNs appear, gradients explode, or runs stop.

Common causes:

- numerical instability
- bad loss scaling
- invalid data batch
- optimizer/scheduler issue
- implementation bug

### Reproducibility Failure

The result cannot be repeated.

Common causes:

- missing seed control
- nondeterministic data pipeline
- environment drift
- untracked config
- checkpoint or artifact mismatch

### Paper Story Contradiction

The result undermines the planned narrative.

Common causes:

- claim too broad
- method works only in narrow regime
- mechanism claim unsupported
- experiment reveals a better paper framing

## Diagnosis Categories

Use these labels:

- `implementation-bug`
- `metric-bug`
- `data-issue`
- `baseline-fairness`
- `seed-variance`
- `optimization`
- `hyperparameter`
- `mechanism-failure`
- `scale-regime-mismatch`
- `claim-mismatch`
- `expected-negative-result`
- `unknown`

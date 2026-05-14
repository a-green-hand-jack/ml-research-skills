# Audit Criteria Reference

## Protocol Integrity Criteria

### Metric–Task Alignment
| Claimed property | Acceptable proxy metrics | Metrics that require caution |
|---|---|---|
| General reasoning | Multi-task benchmark (avg) | Single benchmark score |
| Robustness | OOD test set accuracy | In-distribution accuracy only |
| Efficiency | FLOP-matched comparison | Wall-clock without hardware disclosure |
| Sample efficiency | Learning curve (N vs perf) | Final accuracy only |
| Real-world utility | User study or deployment metrics | Automated benchmark |
| Calibration | ECE, reliability diagram | Accuracy only |

**Flag**: when the metric measures a proxy that correlates with the claimed property but does not directly measure it.

### Ablation Isolation Rules
A valid ablation changes exactly one factor:
- Same architecture, same data, same compute budget, same seed(s)
- The removed component is the *only* difference
- If multiple components are added together: require a full factorial or at minimum a partial ablation matrix

**Common violations**:
- Adding a component that also increases parameter count
- Removing a component that also changes training dynamics (e.g. removing a loss term changes the gradient scale)
- Comparing methods with different numbers of training steps

### Comparable Conditions
All compared methods must share:
- Same evaluation data split (or official benchmark split for all)
- Same tokenizer / preprocessing pipeline
- Equivalent hyperparameter tuning budget
- Same hardware tier (or normalize for FLOPs)

**Flag as `risk`**: if the proposed method received more tuning than baselines.
**Flag as `blocker`**: if the proposed method trained on data that overlaps with the test set of any baseline.

## Confound Classification

### Scale Confound
- **Definition**: the proposed method uses more parameters, more compute, or more data than the baseline
- **Ruling out**: FLOP-matched or parameter-matched ablation; or explicit analysis showing the gain holds at equal scale
- **Common disguises**: "we use a better architecture" without FLOP matching; "we pretrain longer" without separating the pretraining gain

### Data Confound
- **Definition**: the method was developed or tuned on data that overlaps with the test distribution
- **Ruling out**: contamination audit; separate held-out test set not used during development
- **Common disguises**: using val-set performance for model selection, then reporting val-set numbers

### Hyperparameter Confound
- **Definition**: the proposed method received more tuning effort than baselines
- **Ruling out**: equal hyperparameter search budget; or sensitivity analysis showing robustness
- **Common disguises**: tuning the proposed method with a large grid while using the baseline's default settings

### Metric Confound
- **Definition**: the metric rewards a superficial property that correlates with but is not the claimed property
- **Examples**: length bias in ROUGE/BLEU; confidence calibration rewarded by softmax temperature; leaderboard saturation making small gains meaningless
- **Ruling out**: secondary metric without the confound; human evaluation; diagnostic test

### Selection Confound
- **Definition**: the reported number comes from the best seed, checkpoint, or hyperparameter setting, not a principled selection
- **Ruling out**: mean ± std across all seeds; last checkpoint rather than best; pre-specified selection criterion

## Claim-Drift Taxonomy

| Drift type | Example | Max defensible rewording |
|---|---|---|
| Scope drift | "robust" from one benchmark | "performs better on [benchmark name]" |
| Generalization drift | "works for all users" from one demographic | "evaluated on [demographic]; generalization not yet studied" |
| Causation drift | "X causes Y" from correlation | "X is associated with Y"; requires controlled intervention for causation |
| Magnitude drift | "10× speedup" with cherry-picked baseline | "X% faster than [specific baseline] under [specific conditions]" |
| Transfer drift | "works in production" from lab results | "shows promise in controlled conditions; deployment not yet validated" |

## Minimum Statistical Support by Claim Type

| Claim type | Minimum required | Preferred |
|---|---|---|
| Method A outperforms B | mean ± std, N≥3 seeds | mean ± std, N≥5, p-value, effect size |
| Component X contributes Y% | mean ± std across runs | bootstrapped CI |
| Trend across scale | ≥3 data points on the scale axis | confidence band across seeds |
| Correlation between X and Y | scatter plot + r value | regression with CI |
| State-of-the-art claim | comparison to all recent public systems | + statistical test against closest competitor |

## Severity Classification Summary

| Finding type | Blocker | Risk | Note |
|---|---|---|---|
| No uncertainty interval for comparative claim | — | ✓ | — |
| Unaddressed high-likelihood confound | ✓ | — | — |
| Metric does not measure claimed property | ✓ | — | — |
| Scale or compute not matched | — | ✓ | — |
| Ablation changes more than one variable | — | ✓ | — |
| Scope drift to broader real-world claim | — | ✓ | — |
| Causation claimed from correlation | ✓ | — | — |
| Selection confound (best seed reported) | — | ✓ | — |
| Class imbalance unaddressed | — | ✓ | — |

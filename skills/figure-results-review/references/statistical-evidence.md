# Statistical Evidence

Use this to decide whether the displayed evidence is strong enough.

## Minimum Evidence Fields

Record:

- dataset and split
- metric definition
- number of seeds or repeated runs
- model size and training budget
- baseline tuning budget
- evaluation script or protocol
- whether raw logs and configs are available

## Uncertainty

Use an uncertainty display when:

- differences are small
- variance is expected across seeds or tasks
- the claim compares methods rather than presenting a single diagnostic
- reviewer confidence depends on stability

Options:

- mean plus standard deviation
- mean plus standard error
- confidence intervals
- paired differences
- bootstrap interval
- per-seed scatter or thin lines
- task-wise breakdown

State which one is used.

## Effect Size

Ask:

- Is the difference meaningful relative to variance?
- Is the effect large enough for the paper claim?
- Does the improvement hold across datasets, seeds, model sizes, or budgets?
- Does a single outlier drive the average?
- Would a reviewer interpret the result as noise?

## Efficiency Claims

If the claim involves speed or compute, include:

- wall-clock
- FLOPs or training compute proxy
- inference latency
- number of forward passes or function evaluations
- memory
- parameter count
- speed-quality or compute-quality curve

Do not present an efficiency claim using only quality metrics.

## When Evidence Is Insufficient

Route to:

- `rerun` if missing seeds or failed runs block the claim
- `baseline-audit` if comparison fairness is unclear
- `result-diagnosis` if the pattern is suspicious or contradictory
- `narrow-claim` if evidence supports only a smaller statement
- `move-to-appendix` if the result is useful but weak

## Reporting Language

Use cautious wording when evidence is partial:

- "suggests" for preliminary or single-seed results
- "is consistent with" for theory diagnostics that do not prove causality
- "improves in this setting" for one dataset or scale
- "matches" only when differences are within variance or clearly equivalent

Avoid "significant", "robust", "consistently", or "state of the art" unless the evidence supports those words.

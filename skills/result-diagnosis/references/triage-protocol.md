# Triage Protocol

Use this order to diagnose results cheaply and defensibly.

## 1. Provenance First

Ask:

- Did this run use the intended commit and config?
- Was the method enabled?
- Did baseline and method use comparable code paths?
- Is the output path correct?

If provenance is broken, decision is usually `debug`.

## 2. Metric and Evaluation

Ask:

- Is the metric direction correct?
- Is aggregation correct?
- Are splits correct?
- Is checkpoint selection fair?
- Does the metric answer the claim?
- Could data leakage explain the result?

If metric/evaluation is broken, fix before interpreting.

## 3. Baseline Fairness

Ask:

- Same architecture?
- Same data?
- Same sampler?
- Same training budget?
- Same tuning budget?
- Same checkpoint rule?
- Same preprocessing?

If not, the result is not a clean comparison. Decision is usually `rerun` or `ablate`.

## 4. Implementation Sanity

Ask:

- Does the new component affect the computation?
- Are tensor shapes and masks correct?
- Are gradients flowing as intended?
- Are loss scales reasonable?
- Does disabling the method reproduce baseline?
- Are train/eval modes correct?

Use tiny-data or one-batch tests before expensive reruns.

## 5. Statistical Stability

Ask:

- How many seeds?
- Is effect size larger than variance?
- Are there outliers?
- Are results checkpoint-sensitive?
- Is the evaluation sample large enough?

If underpowered, decision is usually `rerun` with more seeds or tighter controls.

## 6. Mechanism Diagnostic

Ask:

- Did the intended diagnostic move in the expected direction?
- Does the diagnostic correlate with final metric?
- Could a generic control match the diagnostic?
- Does the diagnostic expose a hidden failure?

Diagnostic mismatch should affect the claim, not just the experiment.

## 7. Claim Impact

Ask:

- Does the result support the main claim?
- Does it only support a narrower claim?
- Does it falsify the mechanism claim?
- Does it suggest a better paper framing?
- Is it enough to write, or only enough to plan the next experiment?

End with a concrete decision.

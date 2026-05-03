# Limitation Patterns

Use these patterns to classify and write limitations.

## Data or Benchmark Scope

Use when results depend on datasets, tasks, domains, annotation policies, language coverage, or benchmark construction.

Moves:

1. Name the dataset/task scope.
2. Explain what population or capability it may not cover.
3. State how this affects interpretation.
4. Preserve the supported claim.

## Method Assumption

Use when the method assumes access to labels, models, modalities, calibration, architecture properties, or training conditions.

Moves:

1. State the assumption.
2. Explain where it holds.
3. Explain where it may fail.
4. Link to future extension or scope-limited claim.

## Metric or Evaluation Scope

Use when metrics capture only part of the desired behavior.

Moves:

1. State what the metric measures.
2. State what it does not measure.
3. Explain why the paper still uses it.
4. Suggest complementary evaluation if appropriate.

## Compute or Scale Constraint

Use when experiments are limited by hardware, cost, model scale, data scale, or runtime.

Moves:

1. State the evaluated scale.
2. Avoid implying untested larger scale.
3. Explain whether the claim is expected to transfer or remains open.

## Generalization Boundary

Use when results are strong in tested settings but not all settings.

Moves:

1. Define tested settings.
2. Define untested or weaker settings.
3. State the resulting claim boundary.

## Failure Mode

Use when the paper identifies cases where the method or finding breaks.

Moves:

1. State the failure case.
2. Explain observed behavior.
3. Explain whether it is central or peripheral to the main claim.
4. Route to future work, diagnosis, or claim narrowing.

## Theory Assumption

Use when results depend on formal assumptions.

Moves:

1. State assumptions in interpretable language.
2. Explain why they are useful.
3. State what happens outside them.

## Artifact or Reproducibility Constraint

Use when code, data, model weights, runtime, or licensing limits affect reproducibility.

Moves:

1. State what will be released or not released.
2. Explain constraints.
3. Provide the best available reproducibility path.

## Limitation Tone

Good limitation tone:

- concrete
- scoped
- evidence-aware
- constructive

Bad limitation tone:

- apologetic
- vague
- hidden in future work
- broader than the actual issue

# Ablation Implications

Translate method design into ablations and diagnostics before implementation.

## Component Ablation

For every component, ask:

- What claim does it support?
- What should happen if removed?
- What baseline becomes equivalent when removed?
- Does removal change compute or parameter count?
- Is the ablation fair?

Minimum record:

```text
Component:
Purpose:
Remove/replace with:
Expected effect:
Metric:
Failure interpretation:
```

## Objective or Loss Ablation

For a new loss, regularizer, constraint, or reward:

- off/on
- coefficient sweep
- schedule sweep
- generic regularizer control
- gradient-flow variant if relevant
- normalized vs unnormalized form if scale matters
- interaction with base objective

Always define:

- tuning budget
- selected metric
- failure region
- stability metric

## Architecture Ablation

For a new module:

- remove module
- replace with parameter-matched simple module
- freeze or randomize module if useful
- size/depth/width sensitivity
- latency and memory overhead

Avoid claiming architectural benefit without parameter and compute accounting.

## Inference or Sampling Ablation

For a new inference method:

- same trained model, old inference
- same trained model, new inference
- new training, old inference
- number of steps or samples
- latency/quality tradeoff

This separates training effect from inference effect.

## Diagnostic

Each mechanism claim needs at least one diagnostic:

- diagnostic definition
- expected direction
- when measured
- how aggregated
- relation to final metric
- what result would refute the mechanism

Pre-register diagnostics before running major experiments.

## Experiment Handoff

The output to `experiment-design-planner` should include:

- primary claim
- independent variable
- baselines and controls
- ablation table
- diagnostics
- metrics
- expected directions
- falsification conditions
- compute/tuning fairness requirements

# Ablation Matrix

Use this reference when designing more than one run.

## One-Variable Discipline

Each ablation should isolate one conceptual change.

Bad:

```text
baseline vs our method with new loss, different model size, extra data, and longer training
```

Good:

```text
baseline
baseline + new loss
baseline + new loss + data selection
baseline + new loss + data selection + sampler
```

## Run Matrix Template

```markdown
| Run ID | Purpose | Change | Fixed controls | Dataset/split | Metric | Seeds | Expected result | Output |
|---|---|---|---|---|---|---|---|---|
```

## Common Ablation Types

- component ablation: remove/add one module
- data ablation: vary data size, selection, augmentation, or filtering
- hyperparameter sensitivity: vary one important hyperparameter
- model scale: vary parameter count or backbone
- compute budget: vary training steps, samples, or inference budget
- objective ablation: compare loss terms or weights
- evaluation ablation: compare metrics, prompts, or test distributions

## Factorial Designs

Use factorial designs only when interactions matter.

Example:

```markdown
| Loss | Data selection | Sampler | Purpose |
|---|---|---|---|
| off | off | off | baseline |
| on | off | off | loss effect |
| off | on | off | data effect |
| on | on | off | interaction |
```

If factorial design is too expensive, choose a staged design:

1. test primary component
2. test strongest secondary component
3. test interaction only if both help

## Reviewer-Facing Ablations

Reviewers usually ask:

- Which component is responsible?
- Is the gain from more compute?
- Is the baseline tuned fairly?
- Does the method work outside one dataset?
- Is the result robust to seeds?
- Does the claimed mechanism match observed behavior?

Design at least one ablation for the most likely reviewer attack.

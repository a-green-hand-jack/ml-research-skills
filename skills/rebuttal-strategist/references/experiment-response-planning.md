# Experiment Response Planning

Use this reference when reviewers request experiments, baselines, ablations, analyses, or proofs.

## Triage

Classify requested evidence:

- `already-done`: answer with existing table/figure/appendix/log
- `quick-analysis`: can compute from existing outputs
- `quick-run`: can run before rebuttal deadline
- `medium-run`: possible but may risk deadline
- `too-large`: cannot credibly complete during rebuttal
- `not-appropriate`: request is scientifically mismatched or outside scope

## Minimal Evidence Principle

Run the smallest experiment that directly answers the reviewer.

Good:

- one missing baseline on the main dataset
- one ablation isolating the disputed component
- one sensitivity analysis for the questioned hyperparameter
- proof sketch or counterexample addressing a theorem concern
- qualitative examples for a claimed failure mode

Bad:

- broad sweep unrelated to the exact concern
- adding many weak experiments instead of one decisive result
- promising a new benchmark with no time to validate it

## Experiment Plan Template

```markdown
| ID | Concern | Evidence type | Minimal setup | Time cost | Success criterion | Rebuttal sentence | Fallback |
|---|---|---|---|---|---|---|---|
```

## Outcome-Aware Wording

Positive result:

```text
We ran the requested baseline under the same protocol; Table R1 shows that our method remains ahead by X on Y.
```

Partial result:

```text
The new ablation confirms the trend on A, while B is within variance. We will add this nuance and report both cases.
```

Negative result:

```text
This experiment identifies a limitation in setting X. We will scope the claim accordingly; the main conclusion remains supported in settings Y/Z.
```

Too large:

```text
We agree this is an important direction, but it requires a separate benchmark because [...]. We will clarify that our current claim is limited to [...].
```

## Feasibility Checks

Before promising an experiment:

- data available?
- code runnable?
- compute available?
- metric defined?
- baseline implementation reliable?
- enough time for sanity checks?
- result can be explained in response length?

If no, do not promise it as completed. Scope the claim or propose final-version clarification.

## High-Leverage Rebuttal Experiments

Public OpenReview cases show that rebuttal experiments are most useful when they directly neutralize a reviewer objection rather than broaden the paper casually.

Common high-leverage patterns:

- `generalization check`: add one or two alternative backbones/models/providers when reviewer says results depend on a single model
- `component ablation`: compare full method against a version without the disputed component
- `initialization or sensitivity check`: vary initialization, seeds, prompts, timesteps, or hyperparameters when reviewer worries about dependence
- `efficiency table`: report runtime, query count, memory, or iteration count when reviewer worries about overhead
- `baseline fairness check`: explain or test whether baselines receive comparable supervision/data/access
- `closest-work comparison`: add a concise comparison table or experiment against the closest/concurrent method

For each experiment, prepare two response sentences:

- evidence sentence: the result and what it shows
- revision sentence: where it will be added in the final paper

# Failure Mode Map

A good method design should predict where it fails.

## Scientific Failure Modes

- Core assumption is false.
- Target property is not correlated with the desired metric.
- The proposed mechanism helps only under a narrow regime.
- The method improves a diagnostic but not task performance.
- The method improves performance but not the claimed mechanism.

Write what each failure means:

- revise mechanism
- narrow claim
- change metric
- run diagnostic
- park project
- kill claim

## Baseline and Confounder Failure Modes

Common confounds:

- baseline is under-tuned
- proposed method gets more compute
- checkpoint selection differs
- data preprocessing differs
- sampler or inference differs
- random seed variance explains the effect
- generic regularization explains the effect

Design response:

- tuning-matched baseline
- compute budget ledger
- fixed checkpoint rule
- same data/sampler/path
- seed sweep
- generic control

## Optimization Failure Modes

- gradients vanish or explode
- loss terms conflict
- new objective dominates the base objective
- training becomes unstable for some schedules
- added component increases sensitivity to initialization

Design response:

- pilot stability sweep
- gradient norm logging
- loss scale logging
- warmup or annealing plan
- fail-fast smoke test

## Implementation Failure Modes

- tensor shape ambiguity
- hidden detach/gradient-flow decision
- train/eval mismatch
- nondeterministic preprocessing
- config flag changes multiple variables
- diagnostic computed differently from loss

Design response:

- interface contract
- unit tests
- config diff
- minimal smoke run
- explicit gradient-flow statement
- shared diagnostic implementation

## Reviewer Failure Modes

- novelty looks like a small tweak
- mechanism claim lacks evidence
- assumptions are unrealistic
- ablations do not isolate components
- method has too many knobs
- cost is not reported

Design response:

- closest-work boundary
- mechanism diagnostic
- assumption discussion
- one-variable ablations
- hyperparameter budget table
- cost/quality table

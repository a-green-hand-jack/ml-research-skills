# Implementation Handoff

Use this to turn a method design into coding work without letting implementation silently decide the science.

## File and Interface Plan

Identify:

- files or modules likely to change
- new config fields
- new class/function names
- input/output shapes
- training loop hooks
- inference hooks
- logging hooks
- checkpoints or artifact changes

If the repo is unknown, describe the expected module boundaries rather than inventing paths.

## Config Contract

Every new behavior should be controlled by config:

- enable/disable flag
- coefficient or schedule
- diagnostic logging flag
- baseline-compatible defaults
- seed and reproducibility settings

Defaults should reproduce the baseline unless the user explicitly creates a new method config.

## Tests and Smoke Checks

Require:

- unit test for shape and basic numerical behavior
- smoke training run on tiny data
- loss/metric logging check
- gradient-flow check if a new objective is added
- config diff showing only intended changes

For stochastic methods, include a deterministic tiny setting if feasible.

## Logging

Log:

- method enabled/disabled
- hyperparameters and schedules
- loss components
- diagnostics
- seed
- commit
- dataset split
- runtime and memory if cost matters

Diagnostics should be computed consistently with the design document.

## Worktree Plan

For a research worktree, define:

- branch/worktree name
- purpose
- linked claim IDs
- linked experiment IDs
- difference from main branch
- first smoke test
- exit condition

Exit condition choices:

- `merge`: implementation works and evidence supports continuing
- `continue`: promising but needs more experiments
- `park`: blocked or lower priority
- `kill`: mechanism or implementation fails

## Handoff Output

Write:

```markdown
## Implementation Handoff
- Scope:
- Files/modules:
- Config:
- Tests:
- Logging:
- First smoke run:
- Worktree:
- Exit condition:
- Decisions coding must not make silently:
```

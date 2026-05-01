# Experiment Design Plan Template

Use this template for substantial experiment plans.

```markdown
# Experiment Design Plan

Date:
Project:
Owner:
Mode:
Target claim:

## 1. Research Question

## 2. Hypotheses
- Primary:
- Alternative explanations:
- Expected direction:
- Falsification condition:

## 3. Evidence Standard
- Intended use:
- Required baselines:
- Required datasets/tasks:
- Required repeats/seeds:
- Required ablations:
- Required figures/tables:

## 4. Experimental Unit
- Dataset/split:
- Preprocessing:
- Model/method:
- Baseline(s):
- Metrics:
- Compute:
- Environment:

## 5. Variables and Controls

| Type | Variable | Value(s) | Notes |
|---|---|---|---|
| Independent |  |  |  |
| Controlled |  |  |  |
| Nuisance |  |  |  |

## 6. Run Matrix

| Run ID | Purpose | Change | Fixed controls | Dataset/split | Metric | Seeds | Expected result | Output |
|---|---|---|---|---|---|---|---|---|

## 7. Logging Requirements

## 8. Stop Conditions and Decision Rule
- Support condition:
- Falsify condition:
- Continue condition:
- Stop condition:

## 9. Reviewer Risk Check

| Risk | Why it matters | Mitigation |
|---|---|---|

## 10. Next Execution Step
- Suggested `run-experiment` command or job plan:
```

## Status Labels

- `READY_TO_RUN`: plan is specific enough to execute
- `NEEDS_BASELINE`: baseline must be established first
- `NEEDS_METRIC`: metric does not yet answer the question
- `NEEDS_SCOPE`: claim is too broad for the proposed evidence
- `NEEDS_DATA`: data/split/preprocessing is unresolved

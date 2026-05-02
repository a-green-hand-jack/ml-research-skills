# Result Diagnosis Report Template

```markdown
# Result Diagnosis: <short name>

## Result Snapshot

- Linked claim:
- Linked experiment:
- Method:
- Baseline:
- Dataset/split:
- Metrics:
- Runs/seeds:
- Source paths:
- Certainty:

## Expected vs Observed

- Expected:
- Observed:
- Delta:
- Why this matters:

## Symptom Classification

- Primary symptom:
- Candidate diagnosis categories:
- Confidence:

## Evidence Checked

| Evidence | Status | Notes |
|---|---|---|
| Commit/config | checked/missing |  |
| Data/split | checked/missing |  |
| Baseline fairness | checked/missing |  |
| Metric computation | checked/missing |  |
| Logs | checked/missing |  |
| Seeds/variance | checked/missing |  |
| Diagnostic | checked/missing |  |

## Competing Explanations

| Explanation | Evidence For | Evidence Against | Cheapest Test | Decision If True |
|---|---|---|---|---|

## Most Likely Diagnosis

State the most likely diagnosis and uncertainty.

## Decision

- Decision: debug / rerun / ablate / revise-method / narrow-claim / write / park / kill
- Confidence:
- Why:

## Next Checks or Actions

1.
2.
3.

## Claim Impact

- Supported claims:
- Weakened claims:
- Claims to revise:
- Claims to cut:

## Project Memory Writeback

- Evidence:
- Risks:
- Actions:
- Decisions:
- Worktree status:
```

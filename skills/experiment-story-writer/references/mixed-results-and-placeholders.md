# Mixed Results and Placeholders

## Evidence Status Labels

Use consistent labels:

- `verified`: result checked in source table, figure, log, or report
- `user-stated`: user provided result, but source artifact was not checked
- `running`: experiment is still running
- `planned`: experiment is planned but not run
- `provisional`: temporary number or qualitative outcome used for draft scaffolding
- `missing`: needed evidence does not exist
- `contradicted`: evidence conflicts with the active claim

## Provisional Placeholder Format

Use searchable placeholders:

```text
[[PROVISIONAL_RESULT: short description; needed source; expected replacement]]
```

Rules:

- never make provisional numbers look final
- write only the minimum surrounding prose needed to preserve flow
- add every placeholder to `paper/.agent/provisional-results.md` or the experiment story plan
- mark what experiment, table, or figure will replace it

## Mixed Result Patterns

### Scope Narrowing

Use when the method works in some settings but not others.

Move:

- state the positive setting
- state the weaker setting
- explain the scope implication

### Mechanism Qualification

Use when an ablation supports part of the mechanism but not all of it.

Move:

- identify the supported component
- identify the unsupported or ambiguous component
- explain what claim remains valid

### Baseline-Specific Result

Use when gains depend on baseline strength.

Move:

- separate strong-baseline and weak-baseline comparisons
- avoid averaging away the important distinction
- route fairness questions to `baseline-selection-audit`

### Negative But Useful

Use when a result hurts the method claim but supports an analysis or limitation claim.

Move:

- state the negative result directly
- explain what it reveals
- decide whether the paper claim should narrow or reposition

## Red Flags

Route to `result-diagnosis` when:

- a main result contradicts the central claim
- variance changes the qualitative conclusion
- the best baseline was omitted from the narrative
- a table and figure disagree
- the result depends on a suspicious metric choice
- the draft is trying to hide a failure that reviewers will notice

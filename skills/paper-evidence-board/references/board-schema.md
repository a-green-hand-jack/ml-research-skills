# Board Schema

Use this schema for the paper-facing evidence board.

## Claim-Evidence Matrix

| Claim ID | Paper location | Claim strength | Evidence | Evidence status | Risk | Action |
|---|---|---|---|---|---|---|
| CLM-001 | Introduction P3 | strong / moderate / scoped | EVD-001, FIG-001 | observed / planned / stale | RSK-001 | ACT-001 |

## Claim Strength

Use:

- `strong`: broad or causal claim that needs direct evidence.
- `moderate`: empirical or technical claim with bounded scope.
- `scoped`: claim explicitly restricted to a dataset, setting, theorem assumption, or diagnostic.
- `background`: context claim supported mainly by citations.
- `limitation`: claim about what the work does not cover.

Strong claims without direct evidence are submission risks.

## Evidence Status

Use:

- `planned`: experiment/proof/analysis is planned but not run
- `running`: experiment is in progress
- `observed`: result exists in logs, tables, proof, or verified source
- `reported`: result is written in the paper
- `stale`: result or figure is superseded
- `contradicted`: evidence weakens the claim
- `cut`: evidence or claim has been removed

## Figure/Table Entry

| ID | Type | Paper location | Claim supported | Evidence source | Caption job | Status | Action |
|---|---|---|---|---|---|---|---|

Caption job examples:

- establish main result
- isolate mechanism
- show ablation
- show robustness
- show failure mode
- compare cost/quality
- support limitation

## Section Entry

| Section | Job | Claims | Evidence | Risks | Actions |
|---|---|---|---|---|---|

Section jobs:

- motivate problem
- state contribution
- define method
- support mechanism
- establish benchmark result
- analyze failure mode
- position related work
- delimit scope

## Risk Priority

Use:

- `blocking`: likely rejection or invalid claim
- `high`: reviewer likely complains
- `medium`: weakens paper but not fatal
- `low`: polish or clarity issue

Every blocking or high risk needs an action or accepted-risk decision.

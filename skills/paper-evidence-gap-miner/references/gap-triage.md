# Evidence Gap Triage

Use this taxonomy to decide what kind of "missing experiment" the paper actually has.

## Already Supported

Evidence exists, but the draft, evidence board, or section plan does not point to it.

Action:

- update `paper-evidence-board`
- revise prose
- add citation to existing table/figure

## Supportable From Existing CSV

CSV files contain the needed result, but no paper-facing asset or prose uses it.

Action:

- route to `paper-result-asset-builder`
- build table or figure
- record provenance

## Needs Reaggregation

Runs exist, but paper evidence needs a different aggregation:

- mean over seeds
- standard deviation or confidence interval
- dataset average
- per-task breakdown
- metric normalization
- best checkpoint rule
- fair baseline grouping

Action:

- derive from existing CSVs
- document aggregation rule
- review with `table-results-review` or `figure-results-review`

## Needs Slice

Runs exist, but the paper needs a slice:

- dataset family
- task type
- domain subset
- model scale
- difficulty group
- failure category
- method component
- baseline family

Action:

- verify the slice column exists or can be joined
- generate a slice asset
- narrow the claim if the slice is post hoc and exploratory

## Needs Asset

Evidence exists in reports, logs, or CSVs, but the paper lacks the table or figure.

Action:

- use `paper-result-asset-builder`
- record asset provenance
- review asset before prose writing

## Needs Diagnosis

Existing evidence is unstable, surprising, contradictory, or suspicious.

Action:

- use `result-diagnosis`
- do not write strong result prose until diagnosis is resolved

## Needs Claim Narrowing

Existing evidence supports a smaller claim than the draft states.

Action:

- update writing contract
- revise abstract/intro/results/limitations
- avoid new compute unless the broader claim is worth defending

## Needs New Compute

No existing result source can answer the claim under a fair protocol.

Action:

- define the minimum reviewer-relevant result
- route to `experiment-design-planner`
- route to `baseline-selection-audit` if comparisons are involved
- run only after the evidence standard is clear

## Cut or Defer

The claim is not central enough to justify asset building or compute.

Action:

- cut the claim
- move to future work or limitations
- remove stale promises from title, abstract, intro, and conclusion

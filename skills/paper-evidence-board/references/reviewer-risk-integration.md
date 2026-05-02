# Reviewer Risk Integration

Use this to connect reviewer-style concerns to paper evidence and actions.

## Risk Sources

Sources may include:

- `paper-reviewer-simulator` risk register
- `citation-coverage-audit` missing-citation risks
- `result-diagnosis` claim-impact decisions
- real OpenReview reviews and rebuttal issue boards
- advisor comments
- venue checklist or reviewer form

Separate observed real-review text from inferred simulated risks.

## Risk Mapping

For each risk, record:

- risk ID
- source
- affected claim
- paper location
- evidence gap
- reviewer concern
- fix type
- priority
- action

Fix types:

- experiment
- ablation
- proof
- analysis
- citation
- rewrite
- figure/table
- limitation
- rebuttal
- accept-risk

## Priority Rules

`blocking`:

- novelty claim may be false
- main result lacks fair baseline
- correctness issue in method or proof
- major unsupported claim in abstract/introduction

`high`:

- reviewer likely asks for missing ablation
- evidence exists but is not visible
- related work boundary is weak
- metric does not match claim

`medium`:

- clarity issue that could lower confidence
- missing secondary analysis
- figure/caption weak

`low`:

- polish
- minor wording
- optional appendix improvement

## Action Routing

Route:

- missing experiment -> `experiment-design-planner`
- ambiguous result -> `result-diagnosis`
- method flaw -> `algorithm-design-planner`
- writing confusion -> `conference-writing-adapter`
- missing related work -> `citation-coverage-audit`
- broken citation/ref -> `citation-audit`
- real review issue -> `rebuttal-strategist`

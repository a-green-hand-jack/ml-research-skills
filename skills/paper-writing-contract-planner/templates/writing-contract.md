# Paper Writing Contract

## Contract Metadata

- Status: draft
- Created:
- Last updated:
- Owner:
- Paper root:
- Target venue:
- Target year:
- Primary audience:
- Primary archetype:
- Secondary archetype:
- Dominant contribution type: insight | performance | capability | unresolved
- Contract mode: create

## Paper Thesis

- One-sentence thesis:
- Reviewer promise:
- Closest-work boundary:
- Claims to avoid:
- Forbidden tone:

## Quality Gates

- Logical-strength rule:
- Defensibility rule:
- Confusion-time rule:
- Information-density rule:
- Evidence-integrity rule:

## Claim Contract

| Claim ID | Claim wording | Strength | Paper locations | Evidence slots | Evidence status | Forbidden overclaim |
|---|---|---|---|---|---|---|
| CLM-001 |  | provisional |  |  | missing |  |

## Section Contract

| Section | Job | Required claims | Required evidence | Paragraph roles | Figures/tables | Notes |
|---|---|---|---|---|---|---|
| Abstract |  |  |  | move sequence |  |  |
| Introduction |  |  |  | P1/P2/P3/... |  |  |
| Method / Setup |  |  |  | overview/components |  |  |
| Experiments / Results |  |  |  | questions/results/analysis |  |  |
| Related Work |  |  |  | groups/boundaries |  |  |
| Limitations / Conclusion |  |  |  | scope/impact/close |  |  |

## Introduction Recipe

| Paragraph | Role | Opening move | Required claim | Required evidence | Closing move | Forbidden move |
|---|---|---|---|---|---|---|
| P1 | problem context |  |  |  |  | generic field opening |
| P2 | gap/failure mode |  |  |  |  | vague novelty |
| P3 | key insight |  |  |  |  | method details too early |
| P4 | approach preview |  |  |  |  | code walkthrough |
| P5 | evidence preview |  |  |  |  | unverified result |
| P6 | contributions |  |  |  |  | unsupported "first" claim |

## Evidence Contract

| Slot | Required for | Status | Source artifact | Paper location | Action |
|---|---|---|---|---|---|
| main_comparison | CLM-001 | missing |  |  |  |

Comparison-affecting evidence details to record when relevant: compute, data, training duration, tuning budget, model size, hardware, prompt, evaluation protocol, metric selection, seed/slice/dataset selection rule.

Status values: filled, user-stated, planned, running, provisional, missing, contradicted, not-needed.

## Figure and Table Contract

| ID | Type | Job | Claim supported | Evidence source | Caption pattern | Status |
|---|---|---|---|---|---|---|
| FIG-001 | figure | main-story |  |  | claim-first | planned |
| TAB-001 | table | main-comparison |  |  | comparison table | planned |

## Result Writing Rules

- Main result paragraph pattern:
- Ablation paragraph pattern:
- Mixed or negative result policy:
- Efficiency/result scope policy:
- Provisional result policy:

## Writing Layer Contract

| Layer | Allowed edits | Protected invariants | Memory writeback |
|---|---|---|---|
| layout | page fit, line breaks, local caption/callout compression | claim strength, notation, evidence interpretation | layout lesson if repeated |
| surface-fluency | grammar, rhythm, local transitions | paragraph job, claim scope, caveats | style lesson if repeated |
| argument | paragraph roles, claim/gap/insight/evidence order | evidence slots, forbidden claims | update contract and stale sections |
| technical-consistency | terms, notation, metrics, datasets, baselines, labels | paper meaning and canonical definitions | update terminology/notation map |
| style-consistency | tone, sentence density, claim-strength habits | technical meaning, evidence scope | update writing-style memory |
| venue-adaptation | venue emphasis, section expectations, limitation tone | positioning unless explicitly updated | update contract if positioning changes |
| final-polish | small visible defects after structure is stable | no new claims, terms, or evidence dependencies | usually none |

## Related Work Contract

- Closest work groups:
- Citation groups:
- Boundary statements:
- Claims not to make:
- Related work that belongs in introduction:
- Related work that belongs in related-work section:

## Limitation Contract

- Scope limitations:
- Evidence limitations:
- Method/system/data limitations:
- Claims to narrow:
- Claims to cut:

## Exemplar Contract

| Exemplar | Borrowed pattern | Use for | Do not borrow |
|---|---|---|---|
|  |  |  |  |

## Terminology Contract

- Method name:
- Dataset names:
- Baseline names:
- Metric names:
- Terms to use:
- Terms to avoid:

## Open Actions

| Action ID | Type | Description | Blocks | Owner | Status |
|---|---|---|---|---|---|
| ACT-001 | evidence |  | CLM-001 |  | open |

## Change Notes

- YYYY-MM-DD: Created initial writing contract.

## Writing Handoff

- Next section to write:
- Pattern references to use:
- Claims allowed:
- Evidence slots available:
- Placeholders required:
- Actions before final submission:

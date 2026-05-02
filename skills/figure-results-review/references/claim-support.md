# Claim Support

Use this to decide whether a figure or table actually supports the intended claim.

## Evidence Relation

Write:

```text
This figure/table supports [claim] by showing [comparison/trend/effect] under [setup].
```

If the sentence is weak or vague, the visual is not ready for paper use.

## Status Labels

`supports-claim`
: The displayed evidence directly supports the intended claim with appropriate comparisons and scope.

`supports-narrower-claim`
: The result is useful, but the claim must be restricted to a dataset, scale, metric, budget, model family, or regime.

`ambiguous`
: The result could support multiple interpretations or depends on missing setup details.

`contradicts-claim`
: The visual undermines the intended claim or conflicts with another result.

`diagnostic-only`
: Useful for debugging or method understanding, but not persuasive as a main paper result.

`not-ready`
: Missing key baselines, uncertainty, labels, setup, or data provenance.

## Required Questions

For each visual, answer:

- What exact claim is supported?
- What alternative explanation remains?
- Which baseline or ablation blocks that alternative explanation?
- Is the result main-paper, appendix, diagnostic, or cut?
- Does the visual support a performance claim, mechanism claim, efficiency claim, robustness claim, or qualitative claim?
- Does the result need a paired table, figure, or caption caveat?

## Claim Types

`performance`
: Requires strong baselines, fair protocol, metric clarity, and uncertainty when differences are close.

`mechanism`
: Requires ablations, diagnostics, or causal evidence that the proposed component causes the effect.

`efficiency`
: Requires compute, wall-clock, FLOPs, memory, NFE, or speed-quality reporting.

`robustness`
: Requires multiple datasets, conditions, perturbations, or seeds.

`qualitative`
: Requires representative examples, failure cases, and selection criteria.

`theory-diagnostic`
: Requires the measured quantity to match the theoretical prediction direction and regime.

## Reviewer Risk

Flag high risk when:

- the figure's best reading is weaker than the prose claim
- the main method is visually hard to compare
- baselines are missing or visually de-emphasized
- the result depends on one seed or one dataset
- a small effect is presented as decisive
- a diagnostic figure is used as a main performance result
- a negative or contradictory result is hidden without explanation

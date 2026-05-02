# Evidence Gap Triage

When a claim lacks support, decide what kind of work is actually needed.

## New Experiment

Choose `new-experiment` when:

- the claim needs missing baseline, ablation, robustness, or metric evidence
- reviewer risk cannot be fixed by prose
- a result is planned but not run

Route to `experiment-design-planner`. If the missing evidence is specifically a comparison-set or fairness issue, route to `baseline-selection-audit` first.

## Result Diagnosis

Choose `result-diagnosis` when:

- evidence exists but conflicts with the claim
- metrics disagree
- a diagnostic improves but final performance does not
- result reliability is unclear

Route to `result-diagnosis`.

## Rewrite

Choose `rewrite` when:

- evidence exists but prose overclaims
- contribution order hides the strongest evidence
- section structure causes reviewer confusion
- figure/table exists but interpretation is missing

Route to `paper-positioning-planner` when the paper is selling the wrong story or claim hierarchy. Route to `conference-writing-adapter` when the strategy is clear and the text needs venue-aware rewriting.

## Figure or Table Review

Choose `figure-results-review` when:

- evidence exists as a plot/table but the claim support is unclear
- axes, captions, uncertainty, table layout, or visual emphasis may mislead readers
- a figure/table should be main-paper, appendix, diagnostic, or cut

Route to `figure-results-review`.

## Narrow Claim

Choose `narrow-claim` when:

- evidence supports only one dataset, regime, metric, or assumption set
- mechanism evidence is weaker than performance evidence
- a broad claim can be made safe with scope.

Update claim wording and paper locations.

If narrowing changes the paper's primary contribution, route to `paper-positioning-planner`.

## Citation Work

Choose `citation-work` when:

- novelty boundary is unsupported
- related work is thin
- a method or dataset attribution is missing
- reviewer risk is primarily "missing prior work"

Route to `citation-coverage-audit` or `citation-audit`.

## Cut

Choose `cut` when:

- the claim is not essential
- supporting it would require too much work
- evidence contradicts it
- it distracts from the main story

Record the cut so the claim does not reappear later.

## Accept Risk

Choose `accept-risk` when:

- the issue is a limitation rather than a fatal gap
- fixing it is infeasible before the deadline
- the paper can state scope honestly

Accepted risks should appear in limitations or rebuttal prep.

After acceptance, route unresolved promised revisions, final claims, and residual risks to `camera-ready-finalizer`.

# Paper Asset Rules

## Experiment-Time vs Paper-Facing Visuals

Experiment-time visualizations:

- help debug, monitor, or explore
- may show many curves, noisy intermediate metrics, or temporary names
- can prioritize speed over style
- may live under `outputs/`, `logs/`, `wandb/`, or code-side result folders

Paper-facing visualizations:

- answer one paper claim or reviewer question
- use stable method names, metrics, colors, markers, and units
- include uncertainty when relevant
- have a caption, label, callout, and provenance record
- live under `paper/figures/` or `paper/tables/`

Do not directly paste experiment-time plots into the paper unless they pass paper-facing checks.

## Table Asset Rules

A paper table should have:

- standalone `tables/<name>.tex`
- caption and label
- row/column grouping aligned with the claim
- metric direction arrows or text
- bolding and tie rules
- missing-value rules
- source CSV and aggregation provenance
- paper callout sentence

Use tables when exact comparisons matter.

## Figure Asset Rules

A paper figure should have:

- rendered asset: `figures/<name>.pdf` and optionally `figures/<name>.png`
- wrapper: `figures/<name>.tex`
- stable caption and label
- visual style aligned with the paper
- readable labels and legends at final size
- source CSV and plotting provenance
- paper callout sentence

Use figures when trend, distribution, tradeoff, slice behavior, or qualitative comparison matters.

## Asset Type Selection

Choose:

- main result table: method/baseline comparison across datasets or metrics
- ablation table: component isolation
- line figure: training, scaling, data size, or threshold trends
- bar figure: few-category comparisons
- scatter/Pareto figure: tradeoff between quality and cost
- heatmap: two-dimensional sweep
- appendix table: full values that would distract in main text
- diagnostic figure: mechanism, failure, or stability evidence

## Naming Rules

Use stable names:

```text
tables/<claim-or-result-name>.tex
figures/<claim-or-result-name>.pdf
figures/<claim-or-result-name>.png
figures/<claim-or-result-name>.tex
```

Avoid names tied to temporary run IDs unless the asset is diagnostic.

## Handoff Rules

After building:

- `table-results-review` audits table integrity, caption, and provenance
- `figure-results-review` audits visual integrity, style, caption, and claim support
- `experiment-story-writer` writes the narrative around the asset
- `paper-evidence-board` records the claim/evidence link

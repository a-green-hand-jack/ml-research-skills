---
name: paper-result-asset-builder
description: Build paper-facing result assets from CSV experiment outputs. Use when the user has raw or aggregated CSV results and wants to inventory available evidence, select rows/slices, aggregate seeds, generate or update LaTeX tables, create publication figures, record provenance, or distinguish paper-facing figures from experiment-time visualizations.
argument-hint: "[project-dir] [--claim <claim-id-or-text>] [--asset table|figure|inventory|provenance]"
allowed-tools: Read, Write, Edit, Bash, Glob
---

# Paper Result Asset Builder

Turn CSV experiment outputs into paper-facing evidence assets: tables, figures, captions/callouts, and provenance records. This skill is the bridge from raw result files to paper artifacts.

Use this skill for:

- inventorying CSV result files and their columns, metrics, methods, datasets, seeds, and run identifiers
- deciding which CSV slices can support a paper claim
- generating or updating `tables/*.tex`, `figures/*.pdf`, `figures/*.png`, and `figures/*.tex`
- recording filtering, aggregation, rounding, bolding, plotting, and provenance rules
- separating paper-facing visualization from experiment-time debugging plots
- preparing assets for `table-results-review`, `figure-results-review`, and `experiment-story-writer`

Do not use this skill to decide whether a paper claim is worth making. Use `paper-evidence-board` or `paper-evidence-gap-miner` for claim/evidence triage. Do not use it to write the results narrative; use `experiment-story-writer` after assets exist. Do not use it for experiment-time debugging dashboards.

## Skill Directory Layout

```text
<installed-skill-dir>/
├── SKILL.md
├── scripts/
│   └── inventory_csv_results.py
├── references/
│   ├── csv-result-contract.md
│   └── paper-asset-rules.md
└── templates/
    ├── result-inventory.md
    └── result-asset-provenance.md
```

## Progressive Loading

- Always read `references/csv-result-contract.md` and `references/paper-asset-rules.md`.
- Use `scripts/inventory_csv_results.py` to inspect CSV files before reading large result files into context.
- Use `templates/result-inventory.md` when creating `paper/.agent/result-inventory.md`.
- Use `templates/result-asset-provenance.md` when creating `paper/.agent/result-asset-provenance.md`.
- Read local `paper/.agent/writing-contract.md`, `paper/.agent/paper-evidence-board.md`, `paper/.agent/writing-memory/`, `paper/.agent/evidence-completion-plan.md`, `paper/.agent/visual-style.md`, `figures/*.tex`, `tables/*.tex`, and current result sections when present.

## Core Principles

- Paper assets exist to support claims, not to dump all available results.
- CSV files are source evidence; paper tables and figures are curated views over those sources.
- Experiment-time visualizations and paper-facing visualizations are different artifacts.
- Every table or figure needs source CSV paths, filtering rules, aggregation rules, metric direction, rounding, styling, and claim mapping.
- Prefer reusing existing CSV results before asking for new compute.
- Never silently hand-enter numbers without provenance.
- If the asset requires a missing result, route to `paper-evidence-gap-miner` before inventing placeholders.
- After building assets, route to `table-results-review` or `figure-results-review`.

## Step 1 - Locate CSV Result Sources

Search likely locations:

```text
code/docs/results/**/*.csv
code/docs/runs/**/*.csv
code/docs/reports/**/*.csv
code/outputs/**/*.csv
code/results/**/*.csv
outputs/**/*.csv
results/**/*.csv
```

If the project uses different result paths, follow the user's paths.

Run the inventory script when useful:

```bash
python3 <installed-skill-dir>/scripts/inventory_csv_results.py <project-dir>
```

Save the curated inventory to:

```text
paper/.agent/result-inventory.md
```

If there is no `paper/` directory and the current directory is the paper repo, save to:

```text
.agent/result-inventory.md
```

## Step 2 - Define the Paper Asset Job

For each requested table or figure, write:

```markdown
- Asset ID:
- Asset type: table / figure
- Paper location:
- Claim supported:
- Reviewer question answered:
- Source CSV files:
- Required rows/slices:
- Metrics:
- Aggregation:
- Uncertainty:
- Styling:
- Output paths:
```

If this cannot be written, route to `paper-evidence-board` or `paper-evidence-gap-miner`.

## Step 3 - Build the Table or Figure View

Use structured CSV parsing, not ad hoc copy/paste.

For tables:

- choose row and column groups around the reader's comparison path
- aggregate seeds/repeats before rounding
- define bolding/underlining and missing-value rules
- include metric direction arrows when appropriate
- output standalone `tables/<name>.tex`

For figures:

- choose plot type based on the claim: bar, line, scatter, heatmap, Pareto frontier, calibration curve, slice plot, qualitative grid, or appendix diagnostic
- apply `paper/.agent/visual-style.md` when present
- export stable paper assets such as `figures/<name>.pdf` and optionally `figures/<name>.png`
- output a LaTeX wrapper `figures/<name>.tex` with caption and label scaffolding

## Step 4 - Record Provenance

Update:

```text
paper/.agent/result-asset-provenance.md
```

For every asset, record:

- source CSV path and file hash when practical
- run IDs, configs, seeds, datasets, splits, methods, and metrics
- filtering and aggregation code or exact rules
- rounding and bolding rules
- plotting parameters and visual style decisions
- manual edits, if any
- claim IDs and paper locations
- uncertainty or missing provenance

## Step 5 - Handoff to Review and Writing

After creating assets:

- use `table-results-review` for `tables/*.tex`
- use `figure-results-review` for `figures/*.pdf`, `figures/*.png`, and `figures/*.tex`
- use `experiment-story-writer` for result prose
- update `paper-evidence-board` with asset-to-claim mappings
- update `paper-writing-memory-manager` when new or changed assets affect captions, result prose, abstract, introduction, limitations, or conclusion
- update `memory/provenance-board.md` with CSV/report-to-asset traceability, aggregation rules, scripts, and paper locations when project memory exists
- update `memory/handoff-board.md` with ready handoffs to `figure-results-review`, `table-results-review`, `experiment-story-writer`, or `paper-evidence-board`
- update `memory/phase-dashboard.md` when the project moves from evidence production to paper asset building or drafting

## Final Sanity Check

Before finalizing:

- every number or plotted point traces back to a CSV source
- filtering and aggregation rules are explicit
- paper-facing visual style is separate from experiment-time visualization
- output files are paper-ready assets, not raw debug plots
- table/figure job maps to a claim or reviewer question
- missing results are routed to `paper-evidence-gap-miner`
- provenance is saved or returned

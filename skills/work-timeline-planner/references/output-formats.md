# Output Formats

Use this reference to choose the right output format and chart engine.

## 1. Markdown + Mermaid

Use when:

- the report should live in a repo
- the user wants something easy to diff, edit, and share
- the chart only needs light structure

Strengths:

- very portable
- easy to save in project docs
- works well for mentor updates and archived reports

Limitations:

- Mermaid Gantt is intentionally lightweight
- interactive behavior is limited
- complex dependencies and rich task UI are awkward

Choose this by default for:

- mentor-facing single-project reports
- repo-native progress notes
- first-pass retrospectives

## 2. HTML + Frappe Gantt

Use when:

- the user wants a richer local visualization
- the report is mainly for inspection rather than git diff review
- the user wants a standalone interactive page

Strengths:

- open source
- visually stronger than Mermaid
- good fit for one-file HTML outputs

Limitations:

- less natural for plain-text review
- better as a generated artifact than as hand-edited project documentation

Choose this by default for:

- local review dashboards
- multi-project personal reviews
- any case where the user explicitly says Mermaid feels too limiting

## 3. HTML + Plotly Timeline

Use when:

- task data is already structured
- the generation flow is Python-heavy
- the user wants interactive exploration more than gantt-specific styling

Strengths:

- good interactive behavior
- easy if data is already tabular

Limitations:

- less specialized for classic gantt presentation
- more useful once data shaping is already clean

Choose this only when:

- the task data is already normalized
- or the user explicitly asks for Plotly

## Default Policy

- `markdown` -> `mermaid`
- `html` -> `frappe-gantt`
- `both` -> Markdown with Mermaid plus HTML with Frappe Gantt

## Save Path Guidance

For Markdown:

- `docs/reports/work_timeline_YYYY_MM.md`
- `docs/reports/mentor_update_YYYY_MM.md`
- `docs/plans/next_phase_timeline.md`

For HTML:

- `docs/reports/work_timeline_YYYY_MM.html`
- `docs/reports/mentor_update_YYYY_MM.html`
- `docs/plans/next_phase_timeline.html`

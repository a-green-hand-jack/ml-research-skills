# Writing Memory Schema

The writing memory lives under `paper/.agent/writing-memory/`. It tracks dynamic paper-writing state, not full paper text.

## Files

### `writing-state.md`

Purpose: current paper-wide writing snapshot.

Records:

- venue and paper archetype
- current positioning
- active writing focus
- stable, draft, stale, blocked, and missing sections
- recent claim/evidence/result changes
- highest-risk writing dependencies
- recommended next writing action

### `section-ledger.md`

Purpose: per-section state.

For each section:

- status: `missing`, `draft`, `stable`, `stale`, `blocked`, `needs-review`
- paragraph jobs
- claims used
- evidence and result dependencies
- figures/tables/captions used
- style or terminology constraints
- open edits and next action

### `dependency-map.md`

Purpose: cross-paper dependency graph.

Map:

```text
claim/evidence/result/table/figure/caption/term
-> paper locations
-> dependent sections
-> stale status
```

This file answers: "If this changes, what else must be checked?"

### `edit-impact-log.md`

Purpose: semantic change log.

Record:

- date
- changed object
- old wording or status
- new wording or status
- reason
- affected locations
- completed updates
- remaining updates

### `style-and-terminology.md`

Purpose: durable writing conventions.

Record:

- method name and abbreviations
- dataset, benchmark, baseline, and metric names
- notation choices
- caption style
- contribution bullet style
- venue tone
- forbidden or downgraded wording
- claim-strength policy

### `open-writing-threads.md`

Purpose: unresolved writing tasks.

Record:

- thread ID
- source
- affected section
- issue
- blocker
- next skill/action
- priority

### `session-notes.md`

Purpose: nonlinear writing session continuity.

Record:

- session date
- focus
- files touched
- decisions made
- new dependencies
- stale areas
- next session entry point

## Status Labels

Use these consistently:

- `stable`: current and checked
- `draft`: written but not fully checked
- `stale`: likely outdated due to claim/evidence/style change
- `blocked`: cannot proceed without evidence, decision, or asset
- `missing`: not written or not created
- `needs-review`: written but needs specialist or consistency check
- `cut-candidate`: likely should be removed

## Dependency Types

Use:

- `claim`
- `evidence`
- `result`
- `table`
- `figure`
- `caption`
- `citation`
- `method-term`
- `notation`
- `style-rule`
- `limitation`
- `placeholder`

## Location Format

Prefer precise but lightweight locations:

```text
sections/intro.tex:P3
sections/results.tex:Table1-callout
figures/main.tex:caption
tables/main_results.tex:row=Ours
abstract:sentence2
contribution:bullet1
```

Use exact line numbers only when already known and stable enough to be useful.

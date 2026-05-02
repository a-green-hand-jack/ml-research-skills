# Memory Writeback

Use this when the project has `research-project-memory` files.

## What to Write

Write durable evidence state:

- which figures/tables support which claims
- whether evidence is main-paper ready, appendix-only, diagnostic, or not ready
- missing uncertainty, baselines, metrics, or captions
- reviewer risks caused by visual ambiguity or overclaiming
- rerun, plotting, caption, or writing actions

Do not store full raw logs. Link to reports, figure files, tables, or result artifacts.

## `memory/evidence-board.md`

Add or update figure/table evidence:

```markdown
## EVD-### - [Figure/Table]: [short name]

- Status: planned / observed / paper-ready / appendix / diagnostic / stale / blocked
- Evidence type: figure / table / plot / qualitative / diagnostic
- Linked claims:
- Linked risks:
- Source files:
- Setup:
- Supports:
- Caveats:
- Next action:
```

## `memory/claim-board.md`

Update claim status:

- `active`: figure/table supports paper use
- `narrowed`: result supports a smaller claim
- `revised`: result changes the story
- `blocked`: result cannot support the claim yet
- `cut`: claim should be removed

## `memory/risk-board.md`

Add reviewer risks:

```markdown
## RSK-### - Figure/result risk: [short name]

- Status: open
- Severity: high / medium / low
- Certainty: verified / inferred / unverified
- Linked evidence:
- Reviewer attack:
- Mitigation:
- Owner / next skill:
```

## `memory/action-board.md`

Add actions:

```markdown
## ACT-### - Fix [figure/table/result issue]

- Status: todo
- Type: plot / table / rerun / caption / writing / diagnosis / baseline / claim
- Priority: high / medium / low
- Linked evidence:
- Linked risks:
- Output expected:
- Exit condition:
```

## `paper/.agent/`

When a paper draft exists, update:

- figure/table map
- paper locations
- caption status
- stale figure warnings
- missing callouts
- main-vs-appendix placement decisions

## Worktree Memory

When code must change, update worktree `.agent/worktree-status.md` with:

- plotting or result-generation task
- source data/log path
- linked evidence/risk IDs
- expected output figure/table
- exit condition

## Certainty Labels

Use:

- `verified`: checked against raw data, logs, generated asset, or paper text
- `user-stated`: supplied by the user
- `inferred`: reviewer-risk or visual/narrative judgment
- `unverified`: image/data not inspected directly

Never mark a result paper-ready if raw data, setup, or uncertainty is unknown.

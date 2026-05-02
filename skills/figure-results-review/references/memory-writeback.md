# Memory Writeback

Use this when the project has `research-project-memory` files.

## What to Write

Write durable evidence state:

- which figures support which claims
- the rendered asset and LaTeX wrapper pairing for paper figures
- visual descriptions that distinguish what is visible from what is inferred
- plotting parameters and experiment parameters needed to interpret the figure
- whether evidence is main-paper ready, appendix-only, diagnostic, or not ready
- missing uncertainty, baselines, metrics, or captions
- reviewer risks caused by visual ambiguity or overclaiming
- rerun, plotting, caption, or writing actions
- visual style decisions such as palette, marker map, typography, figure sizing, and notation consistency

Do not store full raw logs. Link to reports, figure files, or result artifacts.

## `memory/evidence-board.md`

Add or update figure evidence:

```markdown
## EVD-### - [Figure]: [short name]

- Status: planned / observed / paper-ready / appendix / diagnostic / stale / blocked
- Evidence type: figure / plot / qualitative / diagnostic
- Linked claims:
- Linked risks:
- Source files:
- Rendered asset:
- LaTeX wrapper:
- Visual description:
- Plotting parameters:
- Experiment parameters:
- Provenance certainty:
- Setup:
- Supports:
- Caveats:
- Next action:
```

## `memory/claim-board.md`

Update claim status:

- `active`: figure supports paper use
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
## ACT-### - Fix [figure/result issue]

- Status: todo
- Type: plot / rerun / caption / writing / diagnosis / baseline / claim
- Priority: high / medium / low
- Linked evidence:
- Linked risks:
- Output expected:
- Exit condition:
```

## `paper/.agent/`

When a paper draft exists, update:

- figure map
- asset/wrapper pairings for `figures/*.pdf`, `figures/*.png`, and `figures/*.tex`
- paper locations
- visual descriptions
- caption status
- plotting and experiment parameter gaps
- visual style policy path, if one exists
- stale figure warnings
- missing callouts
- main-vs-appendix placement decisions

Recommended style policy paths:

- `paper/.agent/visual-style.md`
- `.agent/conference-writing/project-style.md` when venue adaptation is active

## Worktree Memory

When code must change, update worktree `.agent/worktree-status.md` with:

- plotting or result-generation task
- restyling task and expected visual policy
- source data/log path
- linked evidence/risk IDs
- expected output figure
- exit condition

## Certainty Labels

Use:

- `verified`: checked against raw data, logs, generated asset, or paper text
- `user-stated`: supplied by the user
- `inferred`: reviewer-risk or visual/narrative judgment
- `unverified`: image/data not inspected directly

Never mark a figure paper-ready if raw data, setup, or uncertainty is unknown.

# Memory Writeback

Use this when the project has `research-project-memory` files.

## What to Write

Write accepted-paper final state:

- acceptance and camera-ready status
- final claim status
- final evidence and paper-ready figures/tables
- fulfilled or missing rebuttal promises
- residual risks
- release and artifact obligations
- final paper paths and upload notes

## `memory/decision-log.md`

```markdown
## DEC-### - Camera-ready finalization for [paper]

- Date:
- Status: ready / blocked / uploaded
- Venue:
- Decision:
- Final PDF:
- Rationale:
- Revisit trigger:
```

## `memory/claim-board.md`

Update final statuses:

- `final`
- `narrowed-final`
- `moved-to-appendix`
- `limitation`
- `cut`

## `memory/evidence-board.md`

Mark final paper evidence:

```markdown
## EVD-### - Final [figure/table/experiment]

- Status: paper-ready / appendix / archived
- Linked claims:
- Final paper location:
- Source artifact:
- Caveats:
```

## `memory/risk-board.md`

Close or retain residual risks:

```markdown
## RSK-### - Camera-ready residual risk: [short name]

- Status: closed / accepted / open
- Severity:
- Linked claims/evidence:
- Resolution:
- Residual note:
```

## `memory/action-board.md`

Add final actions:

```markdown
## ACT-### - [final action]

- Status: todo / done
- Type: paper / release / artifact / citation / upload / tag
- Priority:
- Exit condition:
```

## Component Memory

Update:

- `paper/.agent/`: final PDF/source paths, upload state, final metadata, camera-ready notes
- `rebuttal/.agent/`: promise fulfillment and outcome
- `code/.agent/`: release handoff tasks
- `slides/.agent/`: accepted-paper presentation follow-up if relevant

## Certainty Labels

Use:

- `verified`: checked against final paper, logs, code, or official instructions
- `user-stated`: supplied by user
- `inferred`: agent judgment
- `unverified`: requires author or official venue confirmation

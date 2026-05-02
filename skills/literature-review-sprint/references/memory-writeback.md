# Memory Writeback

Use this when the project has `research-project-memory` files.

## What to Write

Write only durable project knowledge:

- closest-work risks
- novelty decisions
- baseline requirements
- evaluation protocol implications
- claims to revise, narrow, park, or cut
- literature-driven algorithm changes
- literature-driven writing or positioning changes
- follow-up reading and verification actions

Do not store every search hit in project memory. Keep exhaustive reading queues in the sprint report.

## Suggested Entries

### `memory/decision-log.md`

Add durable decisions such as:

```markdown
## DEC-### - Literature framing for [topic]

- Date:
- Status: active / revised / superseded
- Certainty: verified / inferred / provisional
- Decision:
- Rationale:
- Alternatives considered:
- Revisit trigger:
```

### `memory/risk-board.md`

Add risks such as:

```markdown
## RSK-### - Closest-work risk: [paper/family]

- Status: open
- Severity: high / medium / low
- Certainty: verified / inferred / unverified
- Linked claims:
- Description:
- Mitigation:
- Owner / next skill:
```

### `memory/action-board.md`

Add actions such as:

```markdown
## ACT-### - Read and compare [paper/family]

- Status: todo
- Type: literature / baseline / experiment / writing / design
- Priority: high / medium / low
- Linked risks:
- Output expected:
- Exit condition:
```

### `memory/claim-board.md`

Update claims when literature changes the paper story:

- `planned`: still plausible but not yet evidenced
- `revised`: claim changed because of closest work
- `narrowed`: claim remains but scope is smaller
- `parked`: claim may return later
- `cut`: no longer defensible

### `memory/evidence-board.md`

Add planned evidence when literature implies a required baseline or diagnostic:

```markdown
## EVD-### - Planned baseline comparison: [baseline]

- Status: planned
- Linked claims:
- Linked risks:
- Evidence type: baseline / ablation / diagnostic / theorem / dataset / metric
- Required because:
```

## Component Memory

If the sprint affects a draft, update `paper/.agent/` with:

- related-work framing
- target community
- accepted-paper exemplars
- claims to avoid
- missing citation families

If it affects code, update the relevant worktree `.agent/worktree-status.md` with:

- baseline implementation needed
- experiment protocol constraints
- exit condition tied to the literature risk

## Certainty Labels

Use:

- `verified`: checked against primary source
- `user-stated`: supplied by user
- `inferred`: agent judgment from available evidence
- `unverified`: search lead not checked

Never convert unverified search leads into strong project claims.

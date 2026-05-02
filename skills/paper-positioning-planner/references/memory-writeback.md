# Memory Writeback

Use this when the project has `research-project-memory` files.

## What to Write

Write durable paper strategy:

- selected archetype
- primary and secondary contribution hierarchy
- target audience and venue fit
- claims to keep, narrow, revise, cut, or block
- closest-work boundary
- title/abstract/main-figure direction
- routed actions

Do not store full prose drafts. Link to positioning reports, paper sections, or evidence boards.

## `memory/decision-log.md`

```markdown
## DEC-### - Paper positioning: [short name]

- Date:
- Status: active / revised / superseded
- Certainty: verified / inferred / provisional
- Decision:
- Archetype:
- Target audience:
- Primary contribution:
- Rationale:
- Revisit trigger:
```

## `memory/claim-board.md`

Update claim status:

- `active`: selected as part of the paper story
- `narrowed`: retained with smaller scope
- `revised`: changed due to evidence/literature
- `blocked`: needs evidence before use
- `cut`: removed from story

## `memory/evidence-board.md`

Add evidence needs required by the selected position:

```markdown
## EVD-### - Evidence needed for [claim]

- Status: planned / observed / blocked / paper-ready
- Linked claims:
- Linked risks:
- Evidence type: figure / table / experiment / theorem / baseline / analysis
- Required because:
```

## `memory/risk-board.md`

```markdown
## RSK-### - Positioning risk: [short name]

- Status: open
- Severity: high / medium / low
- Certainty: verified / inferred / unverified
- Linked claims:
- Reviewer attack:
- Mitigation:
- Owner / next skill:
```

## `memory/action-board.md`

```markdown
## ACT-### - Update paper positioning: [short action]

- Status: todo
- Type: writing / figure / experiment / literature / baseline / method / review
- Priority: high / medium / low
- Linked claims:
- Linked risks:
- Output expected:
- Exit condition:
```

## `paper/.agent/`

When a paper component exists, update:

- active paper thesis
- contribution hierarchy
- title/abstract direction
- main figure/table role
- related-work boundary
- claims-to-avoid list
- next writing adapter target

## Certainty Labels

Use:

- `verified`: checked against draft, evidence, results, or primary sources
- `user-stated`: supplied by user
- `inferred`: strategic judgment
- `unverified`: depends on missing literature, baseline, figure, or review data

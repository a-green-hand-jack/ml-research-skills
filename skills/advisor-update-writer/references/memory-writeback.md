# Memory Writeback

After an update, preserve only durable state.

## Recommended Updates

- `memory/current-status.md`: current milestone, next meeting entry point, top blockers.
- `memory/decision-log.md`: advisor decisions, rationale, superseded options.
- `memory/risk-board.md`: newly raised risks or risks downgraded after feedback.
- `memory/action-board.md`: owner, deadline, and next step for each action.
- `memory/evidence-board.md`: new evidence that changed the discussion.
- `slides/.agent/`: if the update created or changed a presentation.
- `paper/.agent/` or `code/.agent/`: if the update changes writing or implementation priorities.

## Style

Use short entries:

```markdown
### DEC-2026-05-02 - Narrow paper claim to mechanism analysis
- Decision: Target mechanism-analysis story instead of SOTA claim.
- Rationale: Current baselines are not enough for SOTA; evidence supports mechanism.
- Source: advisor update 2026-05-02
- Actions: ACT-014, ACT-015
```

Do not store the whole email or meeting transcript unless the user explicitly wants an archive.

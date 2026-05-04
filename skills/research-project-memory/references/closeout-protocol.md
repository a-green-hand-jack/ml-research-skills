# Closeout Protocol

Use closeout after any substantial session that changes project state, evidence, writing, risks, code direction, review status, or next steps.

## Closeout Questions

Answer:

- What changed?
- Which facts were observed, user-stated, inferred, stale, or needing verification?
- Which claims were added, supported, weakened, revised, or cut?
- Which evidence appeared or changed?
- Which provenance links were verified, made provisional, or became stale?
- Which risks appeared, changed severity, or closed?
- Which handoffs were produced, consumed, blocked, or invalidated?
- Which paper source surfaces became visible to coauthors, reviewers, arXiv, publisher, or the public?
- Did the project phase or active gate change?
- Which actions are next?
- Which component should the next session open first?

## Required Updates

Usually update:

- `memory/current-status.md`
- `memory/action-board.md`

Update as needed:

- `memory/phase-dashboard.md`
- `memory/claim-board.md`
- `memory/evidence-board.md`
- `memory/provenance-board.md`
- `memory/risk-board.md`
- `memory/handoff-board.md`
- `memory/source-visibility-board.md`
- `memory/decision-log.md`
- component `.agent/` status files
- worktree `.agent/worktree-status.md`

## Current Status Shape

Keep current status short:

```markdown
## Current Focus

## Latest Reliable State

## Top Open Risks

## Active Actions

## Needs Verification Next Session

## Next Step
```

## Durable Decisions

Add a decision-log entry only when a future session needs to know why a choice was made.

Examples:

- changing target venue
- cutting a claim
- choosing a baseline policy
- abandoning a worktree
- accepting a reviewer risk
- committing to a rebuttal promise

## Closeout Summary to User

When finishing, tell the user:

- memory files changed
- important state captured
- unresolved verification items
- next concrete action

Do not claim volatile facts are current unless verified during the session.

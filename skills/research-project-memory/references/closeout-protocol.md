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

Always update:

- `memory/BRIEFING.md` — regenerate the ≤30-line snapshot from current state; this is the first file every new session reads
- `memory/current-status.md`
- `memory/action-board.md`

Update `memory/hot-results.md` when:

- a new experiment result arrived that ranks among the top 5–7 project results
- a previously provisional result was confirmed or invalidated
- a result that was critical is no longer relevant

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

## BRIEFING.md Shape (≤30 lines)

Regenerate at every closeout. Every new agent session reads this first.

```markdown
## Identity
- Project: <name> | Phase: <phase> | Gate: <gate>
- Target: <venue> | Deadline: <date-or-TBD>

## Critical Must-Know
- <1–3 facts an agent must not forget or act against>

## Top Claims
- CLM-###: <claim> — confirmed|provisional|evidence-needed

## Hot Results  (→ full list in memory/hot-results.md)
- Best: <metric> = <value> — <run-id> (<date>)

## Open Actions (top 3)
- ACT-###: <action> — <component>

## Top Risks (top 2)
- RSK-###: <risk>
```

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

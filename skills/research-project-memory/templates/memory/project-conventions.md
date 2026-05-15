# Project Conventions

Active rules agents must follow in this project. Maintained by `research-project-memory`.
Last reviewed: {{REVIEW_DATE}}

> Read this file at every session start alongside `memory/BRIEFING.md`.
> When a convention no longer applies, move it to **Expired** with a reason — do not silently delete it.

## Active

| ID | Rule | Category | Since | Notes |
|----|------|----------|-------|-------|
| PC-001 | {{CONVENTION_RULE}} | {{CATEGORY}} | {{SINCE_DATE}} | {{NOTES_OR_EMPTY}} |

## Suspended

<!-- Temporarily inactive conventions — may be re-activated. -->

| ID | Rule | Category | Suspended | Resume condition |
|----|------|----------|-----------|-----------------|

## Expired

<!-- Dead conventions — kept for audit trail. -->

| ID | Rule | Category | Expired | Reason |
|----|------|----------|---------|--------|

---

## Categories

`git` · `ssh` · `python-env` · `memory` · `compute` · `paper` · `worktree` · `shell` · `other`

## Lifecycle

- **Active** → agent must follow now
- **Suspended** → skip until resume condition is met (e.g., GPU access not yet provisioned)
- **Expired** → convention no longer applies; keep row for audit trail, add reason

## Update Rule

- Add a row when a new project-specific convention is established by any skill
- Expire a row when infrastructure, scope, or project phase makes it obsolete
- Never delete rows — move to Expired so future sessions know the history
- Review at every major phase transition (method lock-in → experiments → writing → submission)

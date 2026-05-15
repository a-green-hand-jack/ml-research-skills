# Project Conventions

Active rules agents must follow in this project. Maintained by `research-project-memory`.
Last reviewed: 2026-05-16

> Read this file at every session start immediately after `memory/BRIEFING.md`.
> When a convention no longer applies, move it to **Expired** with a reason; do not silently delete it.

## Active

| ID | Rule | Category | Since | Notes |
|----|------|----------|-------|-------|
| PC-001 | Run scope detection before substantial memory work: `git rev-parse --show-toplevel` and `git rev-parse --git-common-dir`. | worktree | 2026-05-15 | Prevents worktree-local results from being written into root project memory. |
| PC-002 | Read `memory/BRIEFING.md`, then this file, then `memory/hot-results.md` before project-root maintenance decisions. | memory | 2026-05-16 | `hot-results.md` is intentionally present even though this skill repo has no experiment results. |
| PC-003 | Use `python3 scripts/validate_skills.py` before committing skill, template, helper, inventory, or memory protocol changes. | validation | 2026-05-05 | Current validator covers 68 skills and routing/template sanity checks. |
| PC-004 | Use `project-push /Users/jieke/Projects/project-skills origin main` for routine pushes after safe-git preflight. | git | 2026-05-12 | Do not replace preflight with the wrapper; pass explicit repo, remote, and branch. |
| PC-005 | Keep `skills/`, README.md, AGENTS.md, CLAUDE.md, `memory/`, and installed skill copies aligned after skill behavior changes. | maintenance | 2026-05-05 | Reinstall changed skills when runtime behavior or routing metadata changes. |

## Suspended

<!-- Temporarily inactive conventions - may be re-activated. -->

| ID | Rule | Category | Suspended | Resume condition |
|----|------|----------|-----------|-----------------|

## Expired

<!-- Dead conventions - kept for audit trail. -->

| ID | Rule | Category | Expired | Reason |
|----|------|----------|---------|--------|

---

## Categories

`git` · `ssh` · `python-env` · `memory` · `compute` · `paper` · `worktree` · `shell` · `validation` · `maintenance` · `other`

## Lifecycle

- **Active** -> agent must follow now
- **Suspended** -> skip until resume condition is met
- **Expired** -> convention no longer applies; keep row for audit trail, add reason

## Update Rule

- Add a row when a new project-specific convention is established by any skill.
- Expire a row when infrastructure, scope, or project phase makes it obsolete.
- Never delete rows; move to Expired so future sessions know the history.
- Review at every major phase transition or after repeated agent regressions.

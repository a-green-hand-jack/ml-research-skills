---
auto-generated: true
refresh: run research-project-memory --closeout or update manually after major work
volatile-fields: git-state, installed-skill-copies
---

# Project Briefing — ml-research-skills

> **Must-read at session start.** Re-verify volatile facts (git state, installed copies) before acting.

## Identity

- Project: ml-research-skills (skill collection for ML research lifecycle)
- Phase: maintenance | Gate: keep validation passing; update README/AGENTS/CLAUDE/memory on skill changes
- Repo: `a-green-hand-jack/ml-research-skills` | Install: `npx skills add a-green-hand-jack/ml-research-skills -g -a codex claude-code -y`

## Critical Must-Know

- **72 skills** as of 2026-05-18 (68 leaf/utility + 4 domain routers). All frontmatter, helper references, and doc-table entries must stay in sync.
- **4 domain routers**: `experiment-evidence-router`, `project-ops-router`, `paper-writing-router`, `discovery-router` — route-only, no business logic.
- Validation: `python3 scripts/validate_skills.py` — must pass before every commit.
- Template placeholders must use `{{UPPER_SNAKE_CASE}}` — lowercase triggers a validator error.
- Git closeout: use `project-push /Users/jieke/Projects/project-skills origin main` for routine pushes.
- Skill descriptions are routing rules, not titles — Codex hard-limits 500 chars per skill.
- Memory bootstrap: `uv run scripts/memory_bootstrap.py [--skill <name>]` — prints MUST READ / ACTIVE FACTS / DO NOT / WRITEBACK for any task.
- Memory reliability: `memory/fact-index.yaml` (P0 facts), `memory/memory-revision.json` (stale detection), `taxonomy/memory-contracts/` (per-skill contracts).
- Startup memory includes root `memory/project-conventions.md` and `memory/hot-results.md`; both paths must exist.

## Top Claims

- Collection covers the full ML research lifecycle from idea to release — `confirmed`
- All skills are ≤500 lines SKILL.md; larger reference material lives in linked files — `confirmed`

## Open Actions (top 3)

- ACT-038: Design and ship `memory/BRIEFING.md` + `hot-results.md` pattern to solve agent forgetting — `done` (this session)
- ACT-039: Reinstall updated skills after memory-reliability changes — `pending`
- ACT-040: Materialize root `project-conventions.md` and `hot-results.md` files — `done`

## Top Risks

- RSK-001: Skill inventory drift between `skills/`, README, AGENTS, CLAUDE, and installed runtime copies
- RSK-004: Memory could become stale if not updated after skill behavior changes

## Full Memory

`memory/project-conventions.md` · `memory/hot-results.md` · `memory/current-status.md` · `memory/decision-log.md` · `memory/action-board.md` · `memory/risk-board.md`

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

- **73 skills** as of 2026-05-18 (68 leaf/utility + 4 domain routers + 1 root router). All frontmatter, helper references, and doc-table entries must stay in sync.
- **5 routers**: `ml-research-router` (root) + `experiment-evidence-router`, `project-ops-router`, `paper-writing-router`, `discovery-router` (domain) — route-only, no business logic.
- Validation: `python3 scripts/validate_skills.py` — must pass before every commit.
- Template placeholders must use `{{UPPER_SNAKE_CASE}}` — lowercase triggers a validator error.
- Git closeout: use `project-push /Users/jieke/Projects/project-skills origin main` for routine pushes.
- Skill descriptions are routing rules, not titles — Codex hard-limits 500 chars per skill.
- Memory bootstrap: `uv run scripts/memory_bootstrap.py [--skill <name>]` — prints MUST READ / ACTIVE FACTS / DO NOT / WRITEBACK for any task.
- Taxonomy validator: `uv run scripts/validate_skill_taxonomy.py` — checks router/leaf consistency, expected_path chains, memory contracts, and skill-index.yaml.
- Memory reliability: `memory/fact-index.yaml` (P0 facts), `memory/memory-revision.json` (stale detection), `taxonomy/memory-contracts/` (per-skill contracts).
- Startup memory includes root `memory/project-conventions.md` and `memory/hot-results.md`; both paths must exist.
- Project-code worktrees share uv env by default: `UV_PROJECT_ENVIRONMENT=<ProjectRoot>/.uv-envs/code` plus `uv run` from the active worktree; use stage envs only for dependency/stack/sync-risk exceptions.

## Top Claims

- Collection covers the full ML research lifecycle from idea to release — `confirmed`
- All skills are ≤500 lines SKILL.md; larger reference material lives in linked files — `confirmed`

## Open Actions (top 3)

- ACT-038: Design and ship `memory/BRIEFING.md` + `hot-results.md` pattern to solve agent forgetting — `done` (this session)
- ACT-039: Reinstall updated skills after memory-reliability changes — `pending`
- ACT-041: Add shared project-code uv env policy for sibling worktrees — `done`

## Top Risks

- RSK-001: Skill inventory drift between `skills/`, README, AGENTS, CLAUDE, and installed runtime copies
- RSK-004: Memory could become stale if not updated after skill behavior changes
- RSK-021: Agents may still run bare `uv sync` in a worktree until updated skills/templates are reinstalled or reread

## Full Memory

`memory/project-conventions.md` · `memory/hot-results.md` · `memory/current-status.md` · `memory/decision-log.md` · `memory/action-board.md` · `memory/risk-board.md`

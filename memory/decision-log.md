# ml-research-skills Decision Log

Use this file for durable project decisions and rationale, not transient status.

## DEC-001 - Treat This Repository As A Project With Its Own Memory

- Date: 2026-05-05
- Decision: Add committed root `memory/` for the skill system itself.
- Why: The repo now contains durable architecture decisions, workflow policies, sidecar routing, reviewer isolation, token telemetry, and public/private boundaries that should survive across sessions.
- Alternatives considered: keep state only in README/AGENTS/CLAUDE and git history.
- Affects: `memory/`, README.md, AGENTS.md, CLAUDE.md.
- Revisit when: memory becomes stale or too heavy for the repo.
- Certainty: user-stated

## DEC-002 - Use Sidecar Agents As Bounded Helper Workers, Not Final Decision Makers

- Date: 2026-05-05
- Decision: Use `gpt-5.3-codex-spark` through `codex exec --ephemeral` for bounded scans, drafts, pre-reviews, and mechanical proposals.
- Why: Fast sidecars reduce main-agent context load and make low-risk helper work auditable through `.agent/sidecars/<task-id>/` artifacts.
- Alternatives considered: let every main agent do all helper work inline; use context-forked subagents.
- Affects: `sidecar-task-runner`, `code-reviewer`, `add-git-tag`, `token-usage-auditor`.
- Revisit when: sidecar output is repeatedly noisy, unavailable, or over-trusted.
- Certainty: observed

## DEC-003 - Keep Code Reviewer Context Isolated From Code Writer Context

- Date: 2026-05-05
- Decision: Fresh review should use artifact bundles and one-shot CLI sessions instead of inheriting writer chat context.
- Why: Shared context can bias review, hide shortcuts, and reduce independence.
- Alternatives considered: normal in-session self-review; GitHub issues as the default handoff.
- Affects: `skills/code-reviewer/`.
- Revisit when: an external review platform becomes more useful than local review artifacts.
- Certainty: observed

## DEC-004 - Token Burn Is Telemetry, Not Quality By Itself

- Date: 2026-05-05
- Decision: Track token usage as attention, friction, cost, and artifact-yield telemetry; do not equate high token burn with good work.
- Why: Token usage can reveal where effort went, but project quality still depends on artifacts, decisions, evidence, tests, and review outcomes.
- Alternatives considered: use token count as a direct productivity or quality metric.
- Affects: `skills/token-usage-auditor/`, `memory/action-board.md`, `memory/evidence-board.md`.
- Revisit when: exact cross-agent accounting improves enough to support better yield models.
- Certainty: user-stated

## DEC-005 - Keep Local Machine Facts Out Of Shared Project Policy

- Date: 2026-05-05
- Decision: Shared skills and project docs should record compile backends and policies, not one user's local installed paths or tools.
- Why: Local paths and installed components are private/runtime facts that drift by workstation.
- Alternatives considered: commit local TeX paths or PDF-reader aliases into public skill docs.
- Affects: `init-latex-project`, `submit-paper`, local private memory.
- Revisit when: a repo intentionally standardizes dev containers or CI images.
- Certainty: user-stated

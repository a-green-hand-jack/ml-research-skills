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

## DEC-006 - Treat LaTeX Layout Debugging As Local, Visual, Reversible Optimization

- Date: 2026-05-05
- Decision: Encode paper layout correction as a page/object-first workflow: localize the screenshot or affected object, make one small prose/float/page-break change, compile through the configured backend, inspect visually, and avoid broad global tuning unless the whole paper has a documented style issue.
- Why: User experience showed that short lines, floats, page breaks, and prose length interact; one-shot global `\sloppy`, `\emergencystretch`, paragraph, or float spacing changes can destabilize unrelated pages.
- Alternatives considered: treat layout as a global LaTeX parameter problem; treat it as pure writing rather than writing/float/page optimization.
- Affects: `skills/submit-paper/`, `skills/camera-ready-finalizer/`, `skills/figure-results-review/`, `skills/table-results-review/`.
- Revisit when: a project has a deliberate venue-wide layout policy or a class/style file issue that truly requires global tuning.
- Certainty: user-stated

## DEC-007 - Maintain Visual Assets As Indexed Documentation Artifacts

- Date: 2026-05-06
- Decision: Keep public diagrams under `asset/` with semantic filenames and a maintained `asset/README.md` index; update README links and memory figure inventory whenever a diagram is added, replaced, renamed, or materially repurposed.
- Why: The repo now uses several architecture diagrams with different scopes. Without an index, future agents can easily reuse the wrong image, create near-duplicates, or leave README and memory references stale.
- Alternatives considered: rely on file names only; keep visual roles implicit in README placement.
- Affects: `asset/`, README.md, AGENTS.md, CLAUDE.md, `skills/project-init/SKILL.md`, `memory/evidence-board.md`.
- Revisit when: source prompts, editable diagrams, or an automated image optimization pipeline is added.
- Certainty: observed

## DEC-008 - Use Risk-Tiered Commit Paths With Sidecar Precommit Classification

- Date: 2026-05-06
- Decision: Split commit/push closeout into Fast Path, Skill Path, Code Path, and Risk Path, and allow a read-only Spark sidecar to classify non-trivial diffs before the main agent commits.
- Why: Routine text or memory changes should not pay the latency cost of full smoke tests, full skill reinstall, or complete Git risk orientation. Sidecar classification can reduce main-agent decision time while keeping commit, push, reinstall, and final judgment with the main agent.
- Alternatives considered: always run the full validation and reinstall workflow; let sidecars perform commit/push directly.
- Affects: `skills/safe-git-ops/`, `skills/sidecar-task-runner/`, README.md, AGENTS.md, CLAUDE.md, `memory/project.yaml`.
- Revisit when: sidecar classification is slower than direct inspection or misses meaningful high-risk changes.
- Certainty: user-stated

## DEC-009 - Treat Paper Visual Style As Evolvable Memory

- Date: 2026-05-06
- Decision: Manage figure and table style through a promotion ladder: lesson -> preference -> project contract -> reusable skill rule.
- Why: Paper figure typography, line spacing, legend size, axis labels, colors, markers, exports, and wrapper behavior are too detailed and user/project-specific to fully specify upfront, but they still need durable memory so agents stop rediscovering the same fixes.
- Alternatives considered: hard-code one universal figure style; leave all style choices to ad hoc plotting scripts and visual inspection.
- Affects: `skills/figure-results-review/`, `skills/paper-result-asset-builder/`, README.md, AGENTS.md, CLAUDE.md.
- Revisit when: project-local style memories become noisy or are not actually read before figure generation.
- Certainty: user-stated

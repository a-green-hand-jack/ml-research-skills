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

## DEC-010 - Treat Paper Writing As Layered Engineering

- Date: 2026-05-07
- Decision: Manage writing edits through explicit layers: layout, surface fluency, argument, technical consistency, style consistency, venue adaptation, and final polish.
- Why: Paper edits often look local but can silently change claims, notation, evidence scope, venue positioning, or style. Naming the active layer and protected invariants makes later edits safer and easier to remember.
- Alternatives considered: treat all writing changes as generic polish; rely only on full-draft consistency checks after the fact.
- Affects: `skills/paper-writing-memory-manager/`, `skills/paper-writing-assistant/`, `skills/paper-writing-contract-planner/`, `skills/paper-draft-consistency-editor/`, README.md, AGENTS.md, CLAUDE.md.
- Revisit when: layer labels become overhead without improving edit safety.
- Certainty: user-stated

## DEC-011 - Use Low-Cost Trajectory Scans For Personalization Writeback

- Date: 2026-05-07
- Decision: Add a `personalization-memory` skill and a `sidecar-task-runner` `personalization-scanner` preset so low-cost sidecars can scan sanitized trajectories, logs, diffs, sidecar artifacts, and project memory for reusable preferences.
- Why: The user does not want main agents to interrupt the workflow with memory questions. Many durable preferences emerge from repeated corrections and interaction traces, so the system should propose scoped writeback automatically while keeping raw logs private.
- Alternatives considered: ask the user before every preference update; let the main agent manually inspect all trajectories; write raw transcripts into project memory.
- Affects: `skills/personalization-memory/`, `skills/sidecar-task-runner/`, README.md, AGENTS.md, CLAUDE.md, `memory/`.
- Revisit when: personalization scans are too noisy, too expensive, or create privacy risk.
- Certainty: user-stated

## DEC-012 - Split Project References Into Library, Reading, And Project-Synthesis Layers

- Date: 2026-05-08
- Decision: Add three reference skills: `reference-library-manager` for project-local PDF/index/status management, `reference-reading-summarizer` for paper cards, and `reference-project-synthesizer` for connecting cards to claims, risks, baselines, benchmarks, writing, citations, and project memory.
- Why: Project references serve different roles: writing exemplars, method/theory sources, benchmark sources, baselines, citation support, and reviewer-risk evidence. Splitting management, reading, and project interaction keeps context smaller and allows cheaper models for low-risk scans while preserving stronger reasoning for project-changing implications.
- Alternatives considered: keep reference work inside `literature-review-sprint`; create one monolithic PDF-reading skill.
- Affects: `skills/reference-library-manager/`, `skills/reference-reading-summarizer/`, `skills/reference-project-synthesizer/`, README.md, AGENTS.md, CLAUDE.md, `skills/project-init/`, `memory/`.
- Revisit when: paper cards become too heavy or agents fail to route from cards into project memory.
- Certainty: user-stated

## DEC-013 - Generalize References Into Source-Centric Project Intake

- Date: 2026-05-10
- Decision: Extend the reference skill trio from paper/PDF handling to source-centric project knowledge intake, covering papers, collaborator documents, Markdown notes, BibTeX files, scripts, specs, and manually constructed source bundles.
- Why: Project-relevant information often arrives as collaborator documents, initial idea folders, specs, scripts, notes, or mixed bundles rather than formal papers. Treating all of them as sources lets the system produce source cards and project-use notes before writing durable project memory.
- Alternatives considered: create a separate source-management skill family; keep non-paper artifacts in ad hoc notes; force all upstream material into paper-card templates.
- Affects: `skills/reference-library-manager/`, `skills/reference-reading-summarizer/`, `skills/reference-project-synthesizer/`, README.md, AGENTS.md, CLAUDE.md, `skills/project-init/`, `memory/`.
- Revisit when: generic source cards become too broad or paper-specific workflows lose useful precision.
- Certainty: user-stated

## DEC-014 - Add A Private-To-Public Memory Publication Audit Layer

- Date: 2026-05-10
- Decision: Add `memory-publication-auditor` to scan private skills, memories, notes, and logs before turning them into public skills, docs, templates, or reusable patterns.
- Why: Some personalized or private operational memory contains generalizable engineering methods, but raw memory also contains accounts, paths, hosts, IPs, collaborator context, unpublished project details, and trajectories that must not be copied into public artifacts.
- Alternatives considered: manually inspect private memories ad hoc; extend `personalization-memory`; create public skills directly from private notes without an audit stage.
- Affects: `skills/memory-publication-auditor/`, README.md, AGENTS.md, CLAUDE.md, `tests/test_memory_publication_auditor.py`, `memory/`.
- Revisit when: deterministic scanner findings are too noisy or miss common private patterns.
- Certainty: user-stated

## DEC-015 - Add Context-Safe Active Run Monitoring

- Date: 2026-05-11
- Decision: Add `run-status-monitor` to answer active experiment status questions through short status artifacts rather than raw logs or scheduler dumps.
- Why: During long local, SSH, SLURM, or RunAI experiments, the user often needs progress, intermediate metrics, and ETA without polluting the main coding context. A dedicated probe skill can compress operational state into `docs/ops/runs/<run-id>-status.md` and route failures or surprising metrics to diagnosis.
- Alternatives considered: let the main agent inspect raw logs directly; keep monitoring inside `run-experiment`; rely on manual server checks.
- Affects: `skills/run-status-monitor/`, README.md, AGENTS.md, CLAUDE.md, `tests/test_run_status_monitor.py`, `memory/`.
- Revisit when: run configs become too project-specific or ETA extraction is frequently misleading.
- Certainty: user-stated

## DEC-016 - Add User-Level SSH Command Wrappers

- Date: 2026-05-12
- Decision: Add `remote-cmd` and `remote-bash` helper scripts plus SSH quoting guidance to `remote-project-control`.
- Why: Agents were still composing complex SSH double-quoted one-liners where local shells could expand remote variables such as `$d` before the command reached the server. A stable user/project wrapper pattern makes simple commands argv-style and moves complex logic into project scripts.
- Alternatives considered: rely on agents remembering single-quote rules; keep writing ad hoc SSH one-liners; disable approval prompts broadly.
- Affects: `skills/remote-project-control/`, `skills/run-status-monitor/`, README.md, AGENTS.md, CLAUDE.md, `tests/test_remote_command_wrappers.py`, private local workstation memory.
- Revisit when: wrappers are too restrictive for common scheduler commands or agents misuse `remote-cmd` for shell pipelines.
- Certainty: user-stated

# ml-research-skills Current Status

> Cross-session working memory. Re-verify git state before acting.

## Current Focus

- Summary: The repository is in skill-system hardening mode, with sidecar execution, code-reviewer isolation, token telemetry, toolchain gates, repo-native project memory, automatic personalization writeback, project-local source/reference management, private-to-public knowledge audits, context-safe run monitoring, safer SSH wrapper protocols, and stable Git push wrappers.
- Active milestone: make the skill collection self-maintaining through memory, sidecar task artifacts, validation gates, personalization scans, source cards, publication audits, run-status artifacts, SSH wrapper guardrails, stable push wrappers, and clear public/private boundaries.
- Current phase: `maintenance`.
- Active gate: choose the smallest safe commit path; keep README/AGENTS/CLAUDE, skill inventory, tests, and memory aligned before push when affected.
- Last updated: 2026-05-12.

## Latest Reliable State

- 57 skills are present and installable after adding `run-status-monitor`.
- `run-status-monitor` probes local logs/processes, project wrapper commands, SLURM, and RunAI to produce short `docs/ops/runs/<run-id>-status.md` artifacts without copying raw logs or scheduler output into chat.
- `remote-project-control` now ships `remote-cmd` and `remote-bash` helper scripts plus SSH quoting guidance so agents avoid fragile double-quoted one-liners that expand remote variables locally.
- `safe-git-ops` now ships `project-push` so routine network pushes use one stable command shape instead of drifting among equivalent `git push` variants.
- `sidecar-task-runner` exists and was installed globally for Codex and Claude Code on 2026-05-05.
- `personalization-memory` defines a non-interrupting preference writeback protocol, and `sidecar-task-runner` provides a `personalization-scanner` preset for low-cost candidate extraction.
- `memory-publication-auditor` audits private skills, memories, notes, or logs before converting them into public skills, docs, templates, or reusable patterns.
- `reference-library-manager`, `reference-reading-summarizer`, and `reference-project-synthesizer` now treat papers, collaborator docs, Markdown notes, BibTeX files, scripts, specs, and source bundles as project sources that become source cards and project-use notes.
- `code-reviewer` supports Spark pre-review plus strong isolated review.
- `token-usage-auditor` supports Codex, Claude Code, and repo-local sidecar metadata.
- `add-git-tag` can use read-only sidecar proposal generation while preserving human gates for tag creation and push.
- `asset/` images are tracked with semantic file names; README embeds `current-system-overview-2026-05-12.png` as the current top-level overview, plus execution loop, project anatomy, memory bus, workspace architecture, infra/audit layer, and detailed workflow panels.
- `asset/README.md` indexes each public diagram's role, README placement, and maintenance rules.
- Local `.agent/sidecars/` artifacts are private/local and excluded from this repo's tracked files.
- `submit-paper` now includes a screenshot/page/object-first LaTeX layout debugging protocol, with short pointers from camera-ready, figure review, and table review skills.
- `submit-paper` and `table-results-review` now include a specific `wraptable` / `wrapfig` right-side object protocol: tune `[N]`, avoid nested floating `table`, use compact inline caption/label handling, and adjust width/font/spacing locally.
- `latex-layout-issue-bundler` now creates `.agent/layout-issues/` bundles so PDF layout problems can be handed to agents without manual screenshots.
- `safe-git-ops` now uses Fast / Skill / Code / Risk commit paths, and `sidecar-task-runner` has a read-only `precommit-classifier` preset to recommend minimal validation and reinstall scope.
- `figure-results-review` and `paper-result-asset-builder` now support evolvable style memory: lessons can become preferences, project contracts, and eventually reusable skill rules.
- Writing skills now treat paper editing as layered work: layout, fluency, argument, technical consistency, style consistency, venue adaptation, and final polish each have different permissions and protected invariants.

## Top Open Risks

- `RSK-001`: Skill inventory drift between `skills/`, README, AGENTS, CLAUDE, and installed runtime copies.
- `RSK-002`: Sidecar output could be over-trusted for high-risk design or final review decisions.
- `RSK-003`: Private local facts or agent session logs could leak into public shared memory.
- `RSK-004`: Memory could become stale if not updated after skill behavior changes.
- `RSK-006`: Automatic personalization scans could over-promote noisy or private trajectory details if scope and confidence gates are ignored.
- `RSK-007`: Raw sources or reading trajectories could leak copyrighted/private text into public project memory if source cards are not used as the compression layer.
- `RSK-008`: Private memory publication audits could accidentally reproduce sensitive evidence if reports are not redacted and local/private by default.
- `RSK-009`: Run-status monitors could leak raw logs or overstate ETA if probe artifacts are not kept short and uncertainty-aware.
- `RSK-010`: SSH wrappers can hide shell semantics if agents use `remote-cmd` for commands that actually require shell pipelines or variable expansion.
- `RSK-011`: Stable push wrappers could be used without ordinary preflight if agents treat them as replacing Git state checks.

## Active Actions

- `ACT-001`: Keep project memory current after meaningful workflow or skill-system decisions.
- `ACT-002`: Add sidecar execution contracts gradually to high-value mechanical skills.
- `ACT-003`: Periodically run `skill-system-auditor` against this repo.
- `ACT-004`: Keep token telemetry tied to artifacts and outcomes, not treated as quality by itself.
- `ACT-006`: Keep LaTeX layout debugging guidance aligned across paper submission, camera-ready, figure, and table review skills.
- `ACT-007`: Keep README visual panels aligned with renamed `asset/` files.
- `ACT-008`: Use `asset/README.md` as the entry point before changing public diagram assets.
- `ACT-009`: Use `latex-layout-issue-bundler` before screenshot-based LaTeX layout debugging when a rendered PDF is available.
- `ACT-010`: Reuse wraptable/wrapfig right-side object guidance during local paper layout tuning.
- `ACT-011`: Use sidecar-assisted risk-tiered commit closeout to avoid full validation/reinstall on low-risk changes.
- `ACT-012`: Use visual-style and plot-style contracts before generating or reviewing paper figures.
- `ACT-013`: Use active writing layer and protected invariants before nontrivial paper prose edits.
- `ACT-014`: Use personalization scans after substantial sessions to extract candidate preferences without interrupting the user.
- `ACT-015`: Use the reference skill trio to turn `reference/` sources into cards and project-use notes before project-memory writeback.
- `ACT-016`: Keep the generalized source-centric reference workflow compatible with old paper/PDF projects while supporting initial project seed bundles.
- `ACT-017`: Use `memory-publication-auditor` before extracting public skills or docs from private memories, private skills, notes, or operational logs.
- `ACT-018`: Use `run-status-monitor` for lightweight active-run questions before pulling raw logs into the main agent context.
- `ACT-019`: Use `remote-cmd` for simple server commands and `remote-bash` plus project `scripts/ops/` wrappers for complex SSH logic.
- `ACT-020`: Use `project-push <repo> <remote> <branch>` for routine post-commit network pushes after safe-git preflight.

## Needs Verification Next Session

- `git status --short --branch`
- `python3 scripts/validate_skills.py`
- Relevant unit tests for any changed helper scripts.
- Whether installed `~/.agents/skills/` and `~/.claude/skills/` copies need refresh after skill changes.

## Next Step

- Next substantial closeouts should preserve stable command shapes: `project-push` for Git pushes, `remote-cmd` for simple server commands, `remote-bash` for server shell logic, and `run-status-monitor` for active run summaries.

# ml-research-skills Current Status

> Cross-session working memory. Re-verify git state before acting.

## Current Focus

- Summary: The repository is at 65 skills after implementing all 8 planned new skills (ACT-030–ACT-037). The expansion phase is complete. The collection now covers: data pipeline management, experiment engineering debugging, compute budget planning, inbound feedback synthesis, appendix organization, mid-project pivot planning, model card writing, and statistical analysis reporting — closing all major lifecycle gaps.
- Active milestone: maintain 65-skill collection, keep validation passing, reinstall after skill changes.
- Current phase: `maintenance`.
- Active gate: choose the smallest safe commit path; keep README/AGENTS/CLAUDE, skill inventory, tests, and memory aligned before push when affected.
- Last updated: 2026-05-14.

## Latest Reliable State

- 57 skills are present and installable after adding `run-status-monitor`.
- Skill listing budgets are confirmed sufficient on both platforms (DEC-027, RSK-020 mitigated): Claude Code raised to 2% of context window via `skillListingBudgetFraction: 0.02` in `~/.claude/settings.json` (~16k chars for 200k context); Codex gpt-5.5 has a 265k-token context → 2% budget ≈ 21k chars; both exceed current 57-skill total of ~12,225 chars. All descriptions are ≤ 373 chars and front-loaded, satisfying Codex's 500-char per-skill hard limit. Re-audit when skill count exceeds ~80.
- `run-status-monitor` probes local logs/processes, project wrapper commands, SLURM, and RunAI to produce short `docs/ops/runs/<run-id>-status.md` artifacts without copying raw logs or scheduler output into chat.
- `remote-project-control` now ships `remote-cmd` and `remote-bash` helper scripts plus SSH quoting guidance so agents avoid fragile double-quoted one-liners that expand remote variables locally.
- `remote-project-control` routing metadata and generated project templates now explicitly mention raw SSH one-liners, SSH quoting issues, `remote-cmd`, and `remote-bash`, because wrapper scripts alone did not reliably stop stale sessions from composing fragile SSH commands.
- `safe-git-ops` now ships `project-push` so routine network pushes use one stable command shape instead of drifting among equivalent `git push` variants; root `AGENTS.md`/`CLAUDE.md`, README project-structure guidance, `project-init`, and `init-python-project` templates now surface the same rule outside the skill body.
- `run-experiment`, `remote-project-control`, and `run-status-monitor` now encode resource-aware launch: classify smoke/debug/formal work, inspect server resource and pending state when practical, use the fastest compatible allocation for smoke/debug, and preserve formal-job contracts.
- Server experiment skills now treat Python environment creation as a cost: reuse project/stage uv environments by default, avoid deriving `UV_PROJECT_ENVIRONMENT` from each job name, and require a concrete dependency/isolation/sync-race reason for job-specific envs.
- Server experiment skills now treat long image pulls, `ContainerCreating`, and GPU-generation/CUDA compatibility as scheduling inputs, so lower-wait pools are not chosen blindly for smoke/debug work.
- Server experiment skills now distinguish resource inventory from job occupancy: agents should understand available/allocated GPUs, workload parallelization shape, actual active GPU use, and write feedback when jobs underutilize requested resources.
- `run-status-monitor` and `remote-project-control` now stop repeated scheduler API probes after OAuth/session refresh failure, switch to filesystem/project-wrapper fallback when available, and record one login-refresh action.
- `run-status-monitor` now treats repeated progress tracking as artifact work: the main agent should not run long-lived `sleep`/poll/log-watch loops, and multi-check monitoring should be handled by a project wrapper, sidecar, or bounded background monitor that writes a short status artifact.
- `skill-system-auditor` now includes agent-regression hardening guidance: when a skill exists but agents keep regressing, promote the lesson into routing triggers, core contracts, references, templates, wrappers, memory, reinstall, and installed-copy checks.
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
- Writing skills now include public AI-paper writing heuristics distilled from hzwer/WritingAIPaper: core idea as insight/performance/capability, reader-facing story over research chronology, readability gates, evidence-integrity checks, and figure/table proximity rules.

## Top Open Risks

- `RSK-001`: Skill inventory drift between `skills/`, README, AGENTS, CLAUDE, and installed runtime copies.
- `RSK-002`: Sidecar output could be over-trusted for high-risk design or final review decisions.
- `RSK-003`: Private local facts or agent session logs could leak into public shared memory.
- `RSK-004`: Memory could become stale if not updated after skill behavior changes.
- `RSK-006`: Automatic personalization scans could over-promote noisy or private trajectory details if scope and confidence gates are ignored.
- `RSK-007`: Raw sources or reading trajectories could leak copyrighted/private text into public project memory if source cards are not used as the compression layer.
- `RSK-008`: Private memory publication audits could accidentally reproduce sensitive evidence if reports are not redacted and local/private by default.
- `RSK-009`: Run-status monitors could leak raw logs or overstate ETA if probe artifacts are not kept short and uncertainty-aware.
- `RSK-017`: Main agents could still become long-lived run observers, wasting tokens and crowding the context window, if polling is not pushed into artifacts, wrappers, or sidecars.
- `RSK-019`: Jobs can be running but underutilize allocated GPUs if agents do not model workload shape and actual resource occupancy.
- `RSK-010`: SSH wrappers can hide shell semantics if agents use `remote-cmd` for commands that actually require shell pipelines or variable expansion.
- `RSK-011`: Stable push wrappers could be used without ordinary preflight if agents treat them as replacing Git state checks.
- `RSK-012`: Already-open sessions and existing project guidance may keep stale SSH habits until skills are reinstalled or reread.

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
- `ACT-021`: Strengthen SSH wrapper routing and project templates, then reinstall changed skills.
- `ACT-022`: Use resource-aware launch for experiments: choose low-wait compatible resources for smoke/debug, preserve formal job resource contracts, and diagnose pending jobs by scheduler/resource cause.
- `ACT-023`: Reuse project/stage uv environments by default for server jobs; create job-specific uv envs only for dependency, isolation, or real sync-race reasons.
- `ACT-024`: Treat image pull / `ContainerCreating` and GPU-generation compatibility as smoke/debug routing inputs; avoid free-but-cold or incompatible pools.
- `ACT-025`: Use scheduler API auth circuit breakers: stop repeated API probes after OAuth/session refresh failure and use filesystem fallback plus one login-refresh action.
- `ACT-026`: Use artifact-bounded progress tracking: one bounded main-agent probe is acceptable, but repeated checks should update a short status artifact outside the main transcript.
- `ACT-027`: Use agent-regression hardening during skill maintenance: do not leave repeated mistakes as chat-only lessons or buried prose.
- `ACT-028`: Use utilization-aware resource feedback: track allocation vs active GPU use and update project status/memory when the next launch policy should change.
- `ACT-029`: Use public writing heuristics during paper skill work: classify the core sell, check logical strength/defensibility/confusion time/information density, and surface comparison-affecting protocol details before final prose.
- `ACT-030` (done): `data-pipeline-manager` — dataset acquisition, split design, quality audit, contamination check, versioning.
- `ACT-031` (done): `experiment-debugger` — NaN/gradient, OOM, slow training, metric errors, repro failures.
- `ACT-032` (done): `compute-budget-planner` — GPU-hour estimation, smoke test sizing, ablation costing.
- `ACT-033` (done): `feedback-synthesizer` — inbound advisor/collaborator feedback → triaged claim/risk/action items.
- `ACT-034` (done): `appendix-organizer` — appendix structure, claim boundaries, venue checklist filling.
- `ACT-035` (done): `project-pivot-planner` — narrow/angle/new-direction/kill framework for mid-project failures.
- `ACT-036` (done): `model-card-writer` — model cards, datasheets, reproducibility statements, artifact READMEs.
- `ACT-037` (done): `statistical-analysis-planner` — significance tests, effect sizes, CIs, seed variance, multiple-comparison corrections.

## Planned Skills Roadmap (ACT-030–ACT-037)

| Priority | Skill | Gap Filled |
|---|---|---|
| 1 | `data-pipeline-manager` | Dataset acquisition, preprocessing, split design, quality audit, contamination, versioning — zero current coverage |
| 2 | `experiment-debugger` | Engineering failures: NaN/gradient, GPU OOM, slow training, data loading, metric errors, reproducibility |
| 3 | `compute-budget-planner` | Pre-experiment GPU-hour estimation, smoke sizing, ablation cost, cheaper alternatives |
| 4 | `feedback-synthesizer` | Inbound advisor/collaborator/reviewer feedback → claim updates, risk entries, action items |
| 5 | `appendix-organizer` | Appendix planning, claim boundaries, cross-references, NeurIPS/ICLR checklist sections |
| 6 | `project-pivot-planner` | Mid-project narrowing, angle change, or kill decision on consistent negative results |
| 7 | `model-card-writer` | Model cards, reproducibility checklists, datasheets for venue-required materials |
| 8 | statistical rigor | Significance testing, effect sizes, CIs, seed variance — scope decision needed first |

## Needs Verification Next Session

- `git status --short --branch`
- `python3 scripts/validate_skills.py`
- Relevant unit tests for any changed helper scripts.
- Whether installed `~/.agents/skills/` and `~/.claude/skills/` copies need refresh after skill changes.

## Next Step

- Next substantial closeouts should preserve stable command shapes: `project-push` for Git pushes, `remote-cmd` for simple server commands, `remote-bash` for server shell logic, and `run-status-monitor` for active run summaries. Existing open sessions should reread `safe-git-ops/SKILL.md` plus `references/commit-paths.md` if they keep using raw Git push forms, reread `remote-project-control/SKILL.md` plus `references/ssh-command-wrappers.md` if they keep using raw SSH, and reread `run-status-monitor/SKILL.md` plus `references/backends.md` if they keep doing transcript-visible experiment polling.

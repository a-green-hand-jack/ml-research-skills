# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

**ml-research-skills** — a collection of Claude Code skills for the full lifecycle of ML research projects, installable via:

```bash
npx skills add a-green-hand-jack/ml-research-skills
```

For global installs targeting Codex and Claude Code together:

```bash
npx skills add a-green-hand-jack/ml-research-skills -g -a codex claude-code -y
```

For one specific skill:

```bash
npx skills add a-green-hand-jack/ml-research-skills -g -a codex claude-code -s remote-project-control -y
```

All files are instruction documents for AI agents — not executable code. Skills are deployed to the target agent's global skill home, typically `~/.agents/skills/` for Codex and `~/.claude/skills/` for Claude Code.

## Git Closeout Policy

For Git commits, pushes, branch operations, worktrees, merge/rebase/cherry-pick, lock-file errors, or sandbox/network Git failures, use `safe-git-ops`.

For routine branch pushes after preflight has identified the repo, remote, and branch, use:

```bash
project-push <repo> <remote> <branch>
```

Do not use raw `git push`, `git -C <repo> push`, `cd <repo> && git push`, or shell-wrapped push variants for routine closeout unless `project-push` is unavailable. `git -C <repo> ...` is still fine for inspection and non-push repo-local commands.

## Project Memory

This repo has shared project memory in `memory/`. Before substantial maintenance, read `memory/current-status.md`; after durable skill-system decisions, update the smallest relevant board such as `decision-log.md`, `action-board.md`, `risk-board.md`, `claim-board.md`, or `phase-dashboard.md`. Local sidecar artifacts belong under `.agent/sidecars/` and are ignored by git.

## Visual Assets

Public diagrams live under `asset/`, with roles and maintenance rules in `asset/README.md`. When adding, replacing, or renaming diagrams, keep filenames semantic, update README links, and refresh `memory/evidence-board.md` plus `memory/current-status.md` if the visual system changes materially.

## Testing Changes

No automated tests. To validate a change:

```bash
python3 scripts/validate_skills.py
```

This covers frontmatter, helper references, top-level skill inventory consistency, template placeholder format, and basic Python/shell syntax.

For the `init-python-project` scaffold smoke test:

```bash
python3 -m unittest -v tests.test_init_python_project_scaffold
```

1. Install the skill into the target agent runtime with `npx skills add`, such as `npx skills add a-green-hand-jack/ml-research-skills -g -a codex claude-code -s <skill-name> -y`
2. Invoke in the corresponding agent by describing the task
3. Verify the output and iterate

## Adding a New Skill

Skills live in `skills/<skill-name>/` and require a `SKILL.md` with YAML frontmatter:

```markdown
---
name: skill-name          # must match directory name exactly; lowercase/hyphens only
description: ...          # routing rule, not a title — determines auto-activation
allowed-tools: Read, Write, Edit, Bash, Glob
---
```

- Keep `SKILL.md` under 500 lines; move reference material to separate linked files
- Use `scripts/` for shell automation (only output consumes context, not the script itself)
- Use `templates/` for file templates the skill writes out
- Write descriptions as routing rules: "Use when the user mentions X, wants to do Y, or asks about Z"

## Skills Overview

| Skill | Purpose |
|---|---|
| `research-project-memory` | Initialize and maintain hierarchical memory across claim lifecycle, evidence provenance, source visibility, risks, actions, handoffs, phase dashboard, paper, code, worktrees, slides, reviewer simulation, and rebuttal |
| `research-idea-validator` | Turn a rough research idea into a pursue/revise/park/kill project decision using novelty, feasibility, evidence, and reviewer-risk analysis |
| `literature-review-sprint` | Turn a topic or project direction into a ranked literature map with closest-work, baseline, novelty, and positioning implications |
| `reference-library-manager` | Index and monitor project reference sources under `reference/`, including papers, PDFs, Word docs, Markdown notes, BibTeX files, scripts, specs, and source bundles |
| `reference-reading-summarizer` | Read project reference sources into structured source cards for writing, method, theory, benchmark, baseline, feedback, spec, implementation, risk, or citation-support extraction |
| `reference-project-synthesizer` | Connect source cards to project claims, risks, baselines, benchmarks, experiments, implementation plans, writing contracts, citation placement, collaborator actions, and memory writeback |
| `algorithm-design-planner` | Turn a promising research idea into a concrete method design with formulation, mechanism, assumptions, ablations, and implementation handoff |
| `init-latex-project` | Scaffold a LaTeX academic paper project with venue-specific templates and official style files |
| `latex-layout-issue-bundler` | Create reproducible `.agent/layout-issues/` bundles from PDF pages, crops, source snippets, and compile logs so agents can debug LaTeX layout without manual screenshots |
| `init-python-project` | Create a production-ready Python/ML code repo with uv, ruff, mypy, pytest, pre-commit, code-side evidence docs, and remote workflow memory |
| `project-init` | Initialize a research project control root with independent paper/code/slides repos, shared memory, optional GitHub Project board linkage, root project docs, root agent guidance, toolchain gates, and code/paper worktree policy |
| `project-sync` | Sync experiment results from the code repo into `paper/sections/daily_experiments.tex` |
| `new-workspace` | Create a git branch or project-aware component worktree for code experiments, paper venue versions, arXiv releases, and camera-ready paper versions |
| `run-status-monitor` | Probe local, server, SLURM, RunAI, or wrapper-backed experiment status, including pending-resource and GPU-occupancy diagnosis, and write short progress artifacts without copying raw logs into chat |
| `sidecar-task-runner` | Run bounded one-shot Codex sidecar tasks from repo-local prompt artifacts so fast scans, drafts, pre-reviews, and mechanical proposals can be delegated without giving away main-agent control |
| `personalization-memory` | Scan trajectories, sidecar artifacts, logs, and repeated corrections for reusable preferences, then write safe private or project memory without interrupting the user |
| `memory-publication-auditor` | Audit private skills, memories, notes, or logs before turning them into public skills, docs, templates, or reusable patterns |
| `code-reviewer` | Run fresh-context code reviews from `.agent/code-reviews/` bundles using one-shot Codex/Claude Code reviewer sessions so core implementations can be audited without sharing the writer's chat context |
| `data-pipeline-manager` | Manage ML dataset pipelines before training: acquire, preprocess, design train/val/test splits, audit data quality, check for contamination, and version datasets for reproducibility |
| `experiment-debugger` | Debug ML experiment engineering failures: NaN/gradient issues, GPU OOM, slow training, data loading bugs, metric errors, and reproducibility failures — distinct from scientific result diagnosis |
| `compute-budget-planner` | Estimate GPU compute costs before submitting ML experiments: size smoke tests, cost ablation matrices, find cheaper alternatives, and fit jobs to available resources |
| `experiment-design-planner` | Design hypothesis-driven experiments with baselines, ablations, metrics, controls, logging, and stop conditions before running |
| `baseline-selection-audit` | Audit whether experimental baselines are necessary, fair, current, and reviewer-proof before running or writing comparisons |
| `result-diagnosis` | Diagnose surprising, negative, unstable, or ambiguous experiment results and choose debug/rerun/ablate/revise/narrow/write/park/kill decisions |
| `experiment-report-writer` | Write structured experiment reports from notes, configs, logs, metrics, tables, and figures |
| `feedback-synthesizer` | Turn inbound advisor, collaborator, or reviewer feedback into structured claim updates, risk entries, action items, and experiment decisions |
| `advisor-update-writer` | Write decision-oriented advisor, mentor, lab meeting, or collaborator updates from evidence, risks, options, asks, and next actions |
| `research-slide-deck-builder` | Design and write research slide decks for advisor, lab, progress, reading, proposal, and conference talks using the external `progress-slides` template |
| `figure-results-review` | Review figure assets, LaTeX figure wrappers, plots, captions, visual descriptions, and paper visual style for claim support and reviewer risk |
| `table-results-review` | Review standalone `tables/*.tex` files, table captions, table descriptions, row/column semantics, numeric provenance, and experiment settings |
| `paper-evidence-board` | Maintain a paper-facing board aligning claims, evidence, figures, sections, reviewer risks, and next actions |
| `paper-evidence-gap-miner` | Mine existing CSV results, logs, reports, and assets to fill claim evidence gaps before planning new compute |
| `paper-result-asset-builder` | Build paper-facing tables, figures, wrappers, inventories, and provenance records from CSV experiment outputs |
| `paper-writing-memory-manager` | Maintain dynamic writing memory across nonlinear drafting sessions, section status, dependencies, style decisions, edit impact, stale prose, and open writing threads |
| `paper-positioning-planner` | Decide the paper's primary contribution, claim scope, archetype, target audience, novelty framing, and claims to avoid before venue-specific writing |
| `conference-writing-adapter` | Adapt a paper's structure, positioning, and paragraph-level writing to a target conference using venue exemplars and project-local writing memory |
| `abstract-title-contribution-writer` | Draft and revise titles, abstracts, and contribution lists so the paper's top-level promise matches venue, positioning, claims, and evidence |
| `experiment-story-writer` | Turn experiment tables, figures, ablations, mixed results, and provisional metrics into claim-aware results prose |
| `limitations-scope-writer` | Plan, draft, and revise limitations, scope, failure cases, ethics, broader impact, and conclusion caveats as claim-boundary control |
| `method-section-explainer` | Plan, draft, and revise method sections for notation flow, module ordering, overview figures, algorithm boxes, design rationales, and appendix boundaries |
| `paper-introduction-argument-writer` | Plan, draft, and revise introductions as venue-aware argument chains with hook, gap, insight, method, evidence, and contribution paragraph roles |
| `paper-draft-consistency-editor` | Audit and edit a paper draft for internal consistency across title, abstract, intro, method, results, figures, tables, captions, terminology, limitations, and conclusion |
| `paper-writing-contract-planner` | Create or update a writing contract that locks paper archetype, section order, paragraph roles, claim evidence slots, figure/table jobs, and forbidden claims before drafting |
| `paper-writing-assistant` | Draft and revise claim-aware paper prose, map archetypes to required evidence slots, use micro-patterns for captions and paragraph-level writing, and track provisional result placeholders until verified evidence arrives |
| `related-work-positioning-writer` | Plan, draft, and revise related work as novelty-boundary writing, grouping closest work and defining safe citation-backed boundary statements |
| `paper-reviewer-simulator` | Simulate target-conference reviewers, predicted scores, likely reject reasons, meta-review, rebuttal risks, and a ranked pre-submission risk register |
| `rebuttal-strategist` | Analyze real reviews, infer reviewer intent, plan rebuttal experiments, draft responses, and track promised revisions |
| `appendix-organizer` | Plan and write appendix or supplementary material: structure sections, enforce main-paper claim boundaries, fill NeurIPS/ICLR/ICML reproducibility checklists, and align cross-references |
| `camera-ready-finalizer` | Finalize an accepted paper by checking rebuttal promises, de-anonymization, final claims/evidence, supplement consistency, submission package, and release handoff |
| `artifact-evaluation-prep` | Prepare artifact evaluation packages, reviewer-facing reproduction instructions, smoke tests, manifests, and claim-to-artifact maps |
| `citation-coverage-audit` | Find missing classic, closest, benchmark, and recent concurrent citations before submission |
| `citation-audit` | Run a pre-submission audit of citation keys, BibTeX entries, metadata, citation claims, labels, and LaTeX references |
| `work-timeline-planner` | Build Markdown or HTML timeline reports from git history, docs, and notes for retrospective review or planning |
| `token-usage-auditor` | Audit project token usage from local Codex, Codex sidecar metadata, and Claude Code logs, separating total context, fresh token burn, cache reuse, sessions, and lifecycle interpretation |
| `safe-git-ops` | Perform common Git operations safely, especially around worktrees, sandboxed writes, failure diagnosis, and stable `project-push` closeout |
| `remote-project-control` | Recover project memory and coordinate safe local, Git remote, SSH/HPC/RunAI workflows, and SSH wrapper usage for a research repo |
| `add-git-tag` | Create an annotated git milestone tag with achievements and next-phase plans |
| `update-docs` | Detect code changes since the last docs commit and surgically update affected documentation |
| `submit-paper` | Pre-submission checklist for LaTeX papers: submission mode, mandatory sections, artifacts, anonymity, bibliography, source formatting, local layout debugging, and compile-backend handoff |
| `run-experiment` | Submit an ML experiment to local, SLURM, or RunAI environments with reproducible job scripts in `jobs/` and resource- and utilization-aware smoke/debug/formal planning |
| `release-code` | Prepare and publish a research code repository for public release: security audit, generate README/LICENSE/CITATION.cff, tag version, create GitHub release |
| `skill-system-auditor` | Audit the skill collection for inventory, lifecycle, routing, memory-writeback, documentation, and validation consistency |

## Key Design Patterns

- **`research-project-memory`**: Use as the project-level coordination layer. It maintains memory boards for claim lifecycle, evidence provenance, source visibility, risks, actions, handoffs, phase dashboard, decisions, components, and worktrees so experiment, writing, review, and rebuttal feedback loops stay aligned.
- **`research-idea-validator`**: Use at the start of a project or when a direction is uncertain. It applies the FIVE+C framework to decide pursue/revise/park/kill, then routes to literature review, algorithm design, experiment design, or project setup.
- **`literature-review-sprint`**: Use before method lock-in or after novelty doubts arise. It builds a ranked map of canonical, closest, recent, baseline, and positioning-relevant papers, then converts the map into project decisions and memory updates.
- **`reference-library-manager` / `reference-reading-summarizer` / `reference-project-synthesizer`**: Use for project-local `reference/` libraries. The manager answers "what sources do we have?", the summarizer answers "what does this source say?", and the synthesizer answers "what does it mean for this project?" Keep raw source text and reading trajectories local; commit source cards, project-use notes, and memory writeback only after summarization.
- **`algorithm-design-planner`**: Use after idea validation and before coding/experiment design. It turns a research idea into a method spec, failure-mode map, ablation implications, implementation handoff, and paper-method bridge.
- **`project-init` + `project-sync`**: Core paired workflow. `project-init` creates the project control root with independent component repos, shared memory, optional GitHub Project board linkage, root project docs, root `AGENTS.md`, toolchain gates, and code/paper worktree policies; `project-sync` promotes verified code-side evidence into the paper log.
- **`data-pipeline-manager`**: Use before experiment design when the dataset acquisition, split protocol, preprocessing, quality, or contamination status is unclear. It produces `code/.agent/data-pipeline-plan.md` and writes data decisions to project memory. Pair with `experiment-design-planner` to align split protocol and evaluation criteria.
- **`experiment-debugger`**: Use when training crashes, produces NaN/inf, OOM, or wrong metrics, or when a run cannot be reproduced. It classifies the failure mode (nan-gradient, OOM, slow, metric-error, repro-failure, crash, silent) and walks through targeted fixes. Do not use it for surprising but valid scientific results — use `result-diagnosis` for those.
- **`compute-budget-planner`**: Use between experiment design and job submission to estimate GPU-hours, size smoke tests under 30 minutes, cost the ablation matrix with priorities, and identify cheaper alternatives. Writes `code/.agent/compute-budget.md`.
- **`experiment-design-planner`**: Use before `run-experiment` to turn a paper claim into hypotheses, baselines, ablations, metrics, controls, logging, and stop conditions.
- **`baseline-selection-audit`**: Use between literature review and experiment execution, or whenever a comparison table may be vulnerable. It classifies baselines as must-have/should-have/optional/not-comparable/citation-only and produces a fairness ledger plus reviewer-risk forecast.
- **`result-diagnosis`**: Use after results are surprising, negative, unstable, or hard to interpret. It separates bugs, metric issues, baseline fairness, variance, mechanism failure, and claim mismatch before deciding the next action.
- **`experiment-report-writer`**: Use after experiments have enough evidence to explain motivation, setup, metrics, figures, interpretation, limitations, and next steps in a shareable report.
- **`feedback-synthesizer`**: Use after an advisor meeting, collaborator review, or informal pre-submission feedback arrives. It triages feedback into must-address/should-address/noted/disagree, links each item to claims/risks/actions/evidence in project memory, and saves a dated record in `memory/feedback/`. Use `rebuttal-strategist` instead when formal review decisions arrive.
- **`advisor-update-writer`**: Use when project state needs to become a decision-oriented advisor email, weekly update, lab note, or collaborator status memo with explicit asks and actions.
- **`research-slide-deck-builder`**: Use when project state, experiment reports, figures, or advisor/lab updates need to become slides. It should use `https://github.com/a-green-hand-jack/progress-slides.git` as the external template repo for progress/advisor/lab decks rather than duplicating slide templates in this repository. For Slidev decks, validate the active root, deck-local assets, global CSS import, figure sizing, code readability, and representative browser screenshots; build success alone is not visual validation.
- **`figure-results-review`**: Use before figures, plots, figure captions, or figure result prose enter a paper, slide deck, rebuttal, or advisor update. It checks rendered assets, `figures/*.tex` wrappers, visual descriptions, claim support, visual style, uncertainty, caption wording, and routes fixes to reruns, diagnosis, baseline audit, restyling, or paper evidence updates.
- **`table-results-review`**: Use before standalone `tables/*.tex` files, table captions, or table result prose enter a paper, slide deck, rebuttal, or advisor update. It checks table descriptions, row/column semantics, numeric provenance, experiment settings, bolding rules, footnotes, caption wording, and routes fixes to reruns, diagnosis, baseline audit, table edits, or paper evidence updates.
- **`paper-evidence-board`**: Use while writing or reviewing a draft to keep claims, evidence, figures, sections, reviewer risks, and next actions aligned.
- **`paper-evidence-gap-miner`**: Use when writing exposes a missing result or evidence gap; it checks existing CSVs, logs, reports, and assets before recommending new compute.
- **`paper-result-asset-builder`**: Use when CSV experiment outputs need to become paper-facing tables, figures, LaTeX wrappers, result inventories, and provenance records.
- **`paper-writing-memory-manager`**: Use as the global writing-state layer for nonlinear drafting: section status, dependencies, stale prose, writing-layer decisions, style/terminology decisions, edit impact, and open writing threads. Writing layers are `layout`, `surface-fluency`, `argument`, `technical-consistency`, `style-consistency`, `venue-adaptation`, and `final-polish`; nontrivial edits should name the active layer and protected invariants.
- **`paper-positioning-planner`**: Use when deciding what the paper should strategically sell before venue-specific rewriting. It chooses paper archetype, primary/secondary contribution hierarchy, claim scope, target audience, related-work boundary, narrative architecture, and claims to avoid.
- **`conference-writing-adapter`**: Use when a paper needs to be reshaped for a target venue's reviewer expectations. It learns from accepted/oral/spotlight exemplars, diagnoses the paper archetype, and produces section-level or paragraph-level rewrite plans.
- **`abstract-title-contribution-writer`**: Use when title, abstract, or contribution bullets need to match the paper's highest-level claim, venue positioning, and verified evidence.
- **`experiment-story-writer`**: Use when tables, figures, ablations, mixed results, or provisional metrics need to become claim-aware results prose.
- **`limitations-scope-writer`**: Use when limitations, scope statements, failure cases, ethics, broader impact, or conclusion caveats need to control claim boundaries without weakening supported claims.
- **`method-section-explainer`**: Use when an existing method needs clearer notation flow, module order, overview figure placement, algorithm-box framing, design rationale, or appendix boundaries.
- **`paper-introduction-argument-writer`**: Use when the introduction needs a clear argument chain, paragraph roles, gap/insight/method/evidence flow, or contribution bullets aligned with the writing contract.
- **`paper-draft-consistency-editor`**: Use after draft sections exist to align title, abstract, intro, results, figures, tables, captions, terminology, writing-layer permissions, limitations, and conclusion without changing the selected paper story.
- **`paper-writing-contract-planner`**: Use before detailed drafting to create `paper/.agent/writing-contract.md`, locking section order, paragraph roles, claim/evidence slots, writing-layer permissions, figure/table jobs, related-work boundaries, limitation policy, and forbidden claims.
- **`paper-writing-assistant`**: Use when the paper needs actual prose, not review. It maps the selected paper archetype to required evidence slots, writes and revises sections against the active claims, declares the active writing layer for nontrivial edits, uses reference-backed micro-patterns for captions, paragraph starts, transitions, and result interpretation, and records any temporary result placeholders in `paper/.agent/provisional-results.md` until verified evidence replaces them.
- **`related-work-positioning-writer`**: Use when related work needs closest-work grouping, novelty-boundary paragraphs, safe citation-backed wording, or an intro-vs-related-work split aligned with the paper's positioning.
- **`paper-reviewer-simulator`**: Use before submission to simulate venue-specific reviewers, predict likely reject reasons, produce an area-chair style meta-review, and rank fixes by acceptance impact.
- **`rebuttal-strategist`**: Use after real reviews arrive to parse OpenReview/reviewer comments, infer reviewer intent, decide which experiments or clarifications matter, draft rebuttals, and track promised revisions.
- **`appendix-organizer`**: Use when main paper sections are mostly drafted and appendix structure needs to be decided. It assigns a job to each appendix section, enforces main-paper claim boundaries, fills venue checklists (NeurIPS/ICLR/ICML/ACL/CVPR), and audits cross-references. Use before `submit-paper` to ensure checklist items are answered.
- **`camera-ready-finalizer`**: Use after acceptance to close rebuttal promises, de-anonymize, lock final claims against evidence, check supplement consistency, run final submission handoff, and route code/artifact/release tasks.
- **`artifact-evaluation-prep`**: Use when an accepted or submitted paper needs an artifact evaluation package, reviewer quickstart, smoke tests, runtime envelope, data/checkpoint manifest, or claim-to-artifact map.
- **`citation-coverage-audit`**: Use before submission to find missing foundational, closest, benchmark, and recent concurrent citations, then map each missing paper to an insertion point and novelty risk.
- **`citation-audit`**: Use before paper submission to verify the LaTeX citation graph, BibTeX correctness, metadata accuracy, and whether high-risk citation claims are actually supported by the cited works.
- **`new-workspace`**: In a project-init layout, code worktrees go to `<ProjectName>/code-worktrees/<branch-type>-<branch-name>/` when the target repo is `<ProjectName>/code/`, and paper version worktrees go to `<ProjectName>/paper-worktrees/<version-type>-<venue-or-name>/` when the target repo is `<ProjectName>/paper/`. Code worktrees get evidence dirs and optional UV sync; paper worktrees record target venue/release, template differences, source visibility, cleanup requirements, compile workflow, purpose, and exit condition in `.agent/worktree-status.md`.
- **`run-status-monitor`**: Use for lightweight progress checks while experiments are running. It probes local logs/processes, SLURM, RunAI, SSH/server wrappers, or project-specific status commands, writes a short `docs/ops/runs/<run-id>-status.md` artifact, and keeps raw logs/scheduler output out of the main context.
- **`sidecar-task-runner`**: Use for bounded scans, drafts, pre-reviews, milestone proposals, precommit path classification, and other low/medium-risk helper work. The main agent writes prompt artifacts under `.agent/sidecars/<task-id>/`, runs one-shot Codex sidecars such as `codex exec --ephemeral -m gpt-5.3-codex-spark`, then verifies or rejects the output before acting. For commit closeout, the `precommit-classifier` preset should only inspect read-only Git state and recommend Fast / Skill / Code / Risk path, minimal validation, and reinstall scope.
- **`personalization-memory`**: Use when repeated corrections, trajectory logs, sidecar artifacts, or project memory reveal reusable user/project preferences. Prefer a low-cost `personalization-scanner` sidecar to produce candidates, then write derived privacy-safe rules to private or project memory without asking the user during the main workflow.
- **`memory-publication-auditor`**: Use before turning private memory, private skills, operational notes, or logs into public skills/docs/templates. It scans for private facts, classifies private-only/redactable/publishable/reusable-pattern material, and keeps raw audit artifacts local by default.
- **`code-reviewer`**: Use after core algorithm or production-code implementation to create `.agent/code-reviews/<change-id>/` bundles and review them from a fresh context. Prefer one-shot `codex exec --ephemeral` or `claude -p --no-session-persistence` reviewer sessions over writer-context subagents; findings should be written to `review.md`.
- **`safe-git-ops`**: Use this for general Git work, especially when an agent might confuse sandbox failures with merge conflicts or when shared worktree metadata makes write paths non-obvious. For routine commit/push closeout, choose the fastest safe path and use `project-push <repo> <remote> <branch>` for the final network push instead of drifting among equivalent `git push` command shapes.
- **`remote-project-control`**: Use this before server-heavy work when a repo is edited locally, synced through a Git remote, and run on SSH/HPC/RunAI servers. It establishes repo-native project memory and keeps local / Git remote / server state explicit across sessions. For complex SSH commands, prefer `remote-cmd` / `remote-bash` or project wrappers over double-quoted one-liners so remote variables are not expanded by the local shell. For GitHub Projects, treat `gh project ...` as GitHub API work requiring the `project` token scope, separate from normal Git SSH push.
- **`init-latex-project`**: Invoked by `project-init` via `scripts/init.sh`. Always expand `~` to the actual home path when calling the script. For paper repos, record the project/worktree compile backend (`local`, `Overleaf-GitHub`, `CI`, or `unknown`) separately from runtime local TeX availability; do not commit machine-specific compiler paths or run local LaTeX/package-install commands as a reflex after paper edits.
- **`latex-layout-issue-bundler`**: Use before layout debugging when the user would otherwise provide manual PDF screenshots. It creates `.agent/layout-issues/<issue-id>/` bundles with prompt, manifest, page/crop images when tools are available, page text, source snippets, and compile-log excerpts; fixing remains the job of `submit-paper` or paper-writing skills.
- **`figure-results-review` / `paper-result-asset-builder`**: Treat paper figure style as evolving memory. Use `paper/.agent/visual-style.md` for the paper-facing contract, optional `paper/.agent/style-lessons.md` for append-only lessons, and `code/config/plot_style.yaml` for machine-readable plotting settings. New style issues should start as lessons and only become project contracts after reuse.
- **`init-python-project`**: Treat `experiments/` as runnable logic. Code-side evidence belongs in `docs/results/`, `docs/reports/`, and `docs/runs/`; raw outputs, logs, checkpoints, tensorboard caches, and wandb runs stay ignored or external. Default Python gates are `uv sync`, `ruff format --check`, `ruff check`, `mypy`, `pytest`, and `pre-commit`, with optional gates for secrets, shell scripts, notebooks, GitHub Actions, configs, and docs links. Mutating format/fix commands run only when requested or documented by policy.
- **`token-usage-auditor`**: Use when measuring Codex, Codex sidecar, and Claude Code token burn as project attention and cost telemetry. It scans local logs and `.agent/sidecars/*/model.json` without copying raw prompts into project memory.
- **`skill-system-auditor`**: Use when maintaining this repository as a collection: inventory drift, lifecycle gaps, routing quality, memory writeback coverage, stale future-skill references, validation readiness, and repeated live-session agent regressions that need stronger triggers/contracts/templates.

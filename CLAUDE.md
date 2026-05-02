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
| `research-project-memory` | Initialize and maintain hierarchical memory across claims, evidence, risks, actions, paper, code, worktrees, slides, reviewer simulation, and rebuttal |
| `research-idea-validator` | Turn a rough research idea into a pursue/revise/park/kill project decision using novelty, feasibility, evidence, and reviewer-risk analysis |
| `literature-review-sprint` | Turn a topic or project direction into a ranked literature map with closest-work, baseline, novelty, and positioning implications |
| `algorithm-design-planner` | Turn a promising research idea into a concrete method design with formulation, mechanism, assumptions, ablations, and implementation handoff |
| `init-latex-project` | Scaffold a LaTeX academic paper project with venue-specific templates and official style files |
| `init-python-project` | Create a production-ready Python/ML code repo with uv, pytest, black, ruff, mypy, code-side evidence docs, and remote workflow memory |
| `project-init` | Initialize a research project control root with independent paper/code/slides repos, shared memory, optional GitHub Project board linkage, root project docs, root agent guidance, and code/paper worktree policy |
| `project-sync` | Sync experiment results from the code repo into `paper/sections/daily_experiments.tex` |
| `new-workspace` | Create a git branch or project-aware component worktree for code experiments, paper venue versions, arXiv releases, and camera-ready paper versions |
| `experiment-design-planner` | Design hypothesis-driven experiments with baselines, ablations, metrics, controls, logging, and stop conditions before running |
| `baseline-selection-audit` | Audit whether experimental baselines are necessary, fair, current, and reviewer-proof before running or writing comparisons |
| `result-diagnosis` | Diagnose surprising, negative, unstable, or ambiguous experiment results and choose debug/rerun/ablate/revise/narrow/write/park/kill decisions |
| `experiment-report-writer` | Write structured experiment reports from notes, configs, logs, metrics, tables, and figures |
| `advisor-update-writer` | Write decision-oriented advisor, mentor, lab meeting, or collaborator updates from evidence, risks, options, asks, and next actions |
| `research-slide-deck-builder` | Design and write research slide decks for advisor, lab, progress, reading, proposal, and conference talks using the external `progress-slides` template |
| `figure-results-review` | Review figure assets, LaTeX figure wrappers, plots, captions, visual descriptions, and paper visual style for claim support and reviewer risk |
| `table-results-review` | Review standalone `tables/*.tex` files, table captions, table descriptions, row/column semantics, numeric provenance, and experiment settings |
| `paper-evidence-board` | Maintain a paper-facing board aligning claims, evidence, figures, sections, reviewer risks, and next actions |
| `paper-positioning-planner` | Decide the paper's primary contribution, claim scope, archetype, target audience, novelty framing, and claims to avoid before venue-specific writing |
| `conference-writing-adapter` | Adapt a paper's structure, positioning, and paragraph-level writing to a target conference using venue exemplars and project-local writing memory |
| `paper-writing-assistant` | Draft and revise claim-aware paper prose, map archetypes to required evidence slots, use micro-patterns for captions and paragraph-level writing, and track provisional result placeholders until verified evidence arrives |
| `paper-reviewer-simulator` | Simulate target-conference reviewers, predicted scores, likely reject reasons, meta-review, rebuttal risks, and a ranked pre-submission risk register |
| `rebuttal-strategist` | Analyze real reviews, infer reviewer intent, plan rebuttal experiments, draft responses, and track promised revisions |
| `camera-ready-finalizer` | Finalize an accepted paper by checking rebuttal promises, de-anonymization, final claims/evidence, supplement consistency, submission package, and release handoff |
| `artifact-evaluation-prep` | Prepare artifact evaluation packages, reviewer-facing reproduction instructions, smoke tests, manifests, and claim-to-artifact maps |
| `citation-coverage-audit` | Find missing classic, closest, benchmark, and recent concurrent citations before submission |
| `citation-audit` | Run a pre-submission audit of citation keys, BibTeX entries, metadata, citation claims, labels, and LaTeX references |
| `work-timeline-planner` | Build Markdown or HTML timeline reports from git history, docs, and notes for retrospective review or planning |
| `safe-git-ops` | Perform common Git operations safely, especially around worktrees, sandboxed writes, and failure diagnosis |
| `remote-project-control` | Recover project memory and coordinate safe local, Git remote, and SSH/HPC/RunAI server workflows for a research repo |
| `add-git-tag` | Create an annotated git milestone tag with achievements and next-phase plans |
| `update-docs` | Detect code changes since the last docs commit and surgically update affected documentation |
| `submit-paper` | Pre-submission checklist for LaTeX papers: submission mode, mandatory sections, artifacts, anonymity, bibliography, optional compilation |
| `run-experiment` | Submit an ML experiment to local, SLURM, or RunAI environments with reproducible job scripts in `jobs/` |
| `release-code` | Prepare and publish a research code repository for public release: security audit, generate README/LICENSE/CITATION.cff, tag version, create GitHub release |
| `skill-system-auditor` | Audit the skill collection for inventory, lifecycle, routing, memory-writeback, documentation, and validation consistency |

## Key Design Patterns

- **`research-project-memory`**: Use as the project-level coordination layer. It maintains memory boards for claims, evidence, risks, actions, decisions, components, and worktrees so experiment, writing, review, and rebuttal feedback loops stay aligned.
- **`research-idea-validator`**: Use at the start of a project or when a direction is uncertain. It applies the FIVE+C framework to decide pursue/revise/park/kill, then routes to literature review, algorithm design, experiment design, or project setup.
- **`literature-review-sprint`**: Use before method lock-in or after novelty doubts arise. It builds a ranked map of canonical, closest, recent, baseline, and positioning-relevant papers, then converts the map into project decisions and memory updates.
- **`algorithm-design-planner`**: Use after idea validation and before coding/experiment design. It turns a research idea into a method spec, failure-mode map, ablation implications, implementation handoff, and paper-method bridge.
- **`project-init` + `project-sync`**: Core paired workflow. `project-init` creates the project control root with independent component repos, shared memory, optional GitHub Project board linkage, root project docs, root `AGENTS.md`, and code/paper worktree policies; `project-sync` promotes verified code-side evidence into the paper log.
- **`experiment-design-planner`**: Use before `run-experiment` to turn a paper claim into hypotheses, baselines, ablations, metrics, controls, logging, and stop conditions.
- **`baseline-selection-audit`**: Use between literature review and experiment execution, or whenever a comparison table may be vulnerable. It classifies baselines as must-have/should-have/optional/not-comparable/citation-only and produces a fairness ledger plus reviewer-risk forecast.
- **`result-diagnosis`**: Use after results are surprising, negative, unstable, or hard to interpret. It separates bugs, metric issues, baseline fairness, variance, mechanism failure, and claim mismatch before deciding the next action.
- **`experiment-report-writer`**: Use after experiments have enough evidence to explain motivation, setup, metrics, figures, interpretation, limitations, and next steps in a shareable report.
- **`advisor-update-writer`**: Use when project state needs to become a decision-oriented advisor email, weekly update, lab note, or collaborator status memo with explicit asks and actions.
- **`research-slide-deck-builder`**: Use when project state, experiment reports, figures, or advisor/lab updates need to become slides. It should use `https://github.com/a-green-hand-jack/progress-slides.git` as the external template repo for progress/advisor/lab decks rather than duplicating slide templates in this repository.
- **`figure-results-review`**: Use before figures, plots, figure captions, or figure result prose enter a paper, slide deck, rebuttal, or advisor update. It checks rendered assets, `figures/*.tex` wrappers, visual descriptions, claim support, visual style, uncertainty, caption wording, and routes fixes to reruns, diagnosis, baseline audit, restyling, or paper evidence updates.
- **`table-results-review`**: Use before standalone `tables/*.tex` files, table captions, or table result prose enter a paper, slide deck, rebuttal, or advisor update. It checks table descriptions, row/column semantics, numeric provenance, experiment settings, bolding rules, footnotes, caption wording, and routes fixes to reruns, diagnosis, baseline audit, table edits, or paper evidence updates.
- **`paper-evidence-board`**: Use while writing or reviewing a draft to keep claims, evidence, figures, sections, reviewer risks, and next actions aligned.
- **`paper-positioning-planner`**: Use when deciding what the paper should strategically sell before venue-specific rewriting. It chooses paper archetype, primary/secondary contribution hierarchy, claim scope, target audience, related-work boundary, narrative architecture, and claims to avoid.
- **`conference-writing-adapter`**: Use when a paper needs to be reshaped for a target venue's reviewer expectations. It learns from accepted/oral/spotlight exemplars, diagnoses the paper archetype, and produces section-level or paragraph-level rewrite plans.
- **`paper-writing-assistant`**: Use when the paper needs actual prose, not review. It maps the selected paper archetype to required evidence slots, writes and revises sections against the active claims, uses reference-backed micro-patterns for captions, paragraph starts, transitions, and result interpretation, and records any temporary result placeholders in `paper/.agent/provisional-results.md` until verified evidence replaces them.
- **`paper-reviewer-simulator`**: Use before submission to simulate venue-specific reviewers, predict likely reject reasons, produce an area-chair style meta-review, and rank fixes by acceptance impact.
- **`rebuttal-strategist`**: Use after real reviews arrive to parse OpenReview/reviewer comments, infer reviewer intent, decide which experiments or clarifications matter, draft rebuttals, and track promised revisions.
- **`camera-ready-finalizer`**: Use after acceptance to close rebuttal promises, de-anonymize, lock final claims against evidence, check supplement consistency, run final submission handoff, and route code/artifact/release tasks.
- **`artifact-evaluation-prep`**: Use when an accepted or submitted paper needs an artifact evaluation package, reviewer quickstart, smoke tests, runtime envelope, data/checkpoint manifest, or claim-to-artifact map.
- **`citation-coverage-audit`**: Use before submission to find missing foundational, closest, benchmark, and recent concurrent citations, then map each missing paper to an insertion point and novelty risk.
- **`citation-audit`**: Use before paper submission to verify the LaTeX citation graph, BibTeX correctness, metadata accuracy, and whether high-risk citation claims are actually supported by the cited works.
- **`new-workspace`**: In a project-init layout, code worktrees go to `<ProjectName>/code-worktrees/<branch-type>-<branch-name>/` when the target repo is `<ProjectName>/code/`, and paper version worktrees go to `<ProjectName>/paper-worktrees/<version-type>-<venue-or-name>/` when the target repo is `<ProjectName>/paper/`. Code worktrees get evidence dirs and optional UV sync; paper worktrees record target venue/release, template differences, source visibility, cleanup requirements, compile workflow, purpose, and exit condition in `.agent/worktree-status.md`.
- **`safe-git-ops`**: Use this for general Git work, especially when an agent might confuse sandbox failures with merge conflicts or when shared worktree metadata makes write paths non-obvious.
- **`remote-project-control`**: Use this before server-heavy work when a repo is edited locally, synced through a Git remote, and run on SSH/HPC/RunAI servers. It establishes repo-native project memory and keeps local / Git remote / server state explicit across sessions. For GitHub Projects, treat `gh project ...` as GitHub API work requiring the `project` token scope, separate from normal Git SSH push.
- **`init-latex-project`**: Invoked by `project-init` via `scripts/init.sh`. Always expand `~` to the actual home path when calling the script.
- **`init-python-project`**: Treat `experiments/` as runnable logic. Code-side evidence belongs in `docs/results/`, `docs/reports/`, and `docs/runs/`; raw outputs, logs, checkpoints, tensorboard caches, and wandb runs stay ignored or external.
- **`skill-system-auditor`**: Use when maintaining this repository as a collection: inventory drift, lifecycle gaps, routing quality, memory writeback coverage, stale future-skill references, and validation readiness.

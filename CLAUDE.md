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
| `init-latex-project` | Scaffold a LaTeX academic paper project with venue-specific templates and official style files |
| `init-python-project` | Create a production-ready Python/ML project with uv, pytest, black, ruff, mypy |
| `project-init` | Initialize a full research project: parent folder with `paper/` (LaTeX) + `code/` (Python) + `PROJECT.md` |
| `project-sync` | Sync experiment results from the code repo into `paper/sections/daily_experiments.tex` |
| `new-workspace` | Create a git branch or worktree with UV sync and IDE config copying |
| `experiment-report-writer` | Write structured experiment reports from notes, configs, logs, metrics, tables, and figures |
| `conference-writing-adapter` | Adapt a paper's structure, positioning, and paragraph-level writing to a target conference using venue exemplars and project-local writing memory |
| `paper-reviewer-simulator` | Simulate target-conference reviewers, predicted scores, likely reject reasons, meta-review, rebuttal risks, and a ranked pre-submission risk register |
| `citation-audit` | Run a pre-submission audit of citation keys, BibTeX entries, metadata, citation claims, labels, and LaTeX references |
| `work-timeline-planner` | Build Markdown or HTML timeline reports from git history, docs, and notes for retrospective review or planning |
| `safe-git-ops` | Perform common Git operations safely, especially around worktrees, sandboxed writes, and failure diagnosis |
| `remote-project-control` | Recover project memory and coordinate safe local/remote SSH workflows for a research repo |
| `add-git-tag` | Create an annotated git milestone tag with achievements and next-phase plans |
| `update-docs` | Detect code changes since the last docs commit and surgically update affected documentation |
| `submit-paper` | Pre-submission checklist for LaTeX papers: submission mode, mandatory sections, artifacts, anonymity, bibliography, optional compilation |
| `run-experiment` | Submit an ML experiment to local, SLURM, or RunAI environments with reproducible job scripts in `jobs/` |
| `release-code` | Prepare and publish a research code repository for public release: security audit, generate README/LICENSE/CITATION.cff, tag version, create GitHub release |

## Key Design Patterns

- **`project-init` + `project-sync`**: Core paired workflow. `project-init` creates `paper/` and `code/` sibling repos under a shared parent; `project-sync` keeps `daily_experiments.tex` updated with new results.
- **`experiment-report-writer`**: Use after experiments have enough evidence to explain motivation, setup, metrics, figures, interpretation, limitations, and next steps in a shareable report.
- **`conference-writing-adapter`**: Use when a paper needs to be reshaped for a target venue's reviewer expectations. It learns from accepted/oral/spotlight exemplars, diagnoses the paper archetype, and produces section-level or paragraph-level rewrite plans.
- **`paper-reviewer-simulator`**: Use before submission to simulate venue-specific reviewers, predict likely reject reasons, produce an area-chair style meta-review, and rank fixes by acceptance impact.
- **`citation-audit`**: Use before paper submission to verify the LaTeX citation graph, BibTeX correctness, metadata accuracy, and whether high-risk citation claims are actually supported by the cited works.
- **`new-workspace`**: Worktrees go to `<project-root>/../worktrees/<branch-type>-<branch-name>/`. IDE config dirs (`.vscode`, `.cursor`, `.claude`) are copied (not symlinked). Large shared assets declared in `.worktree-links` are symlinked.
- **`safe-git-ops`**: Use this for general Git work, especially when an agent might confuse sandbox failures with merge conflicts or when shared worktree metadata makes write paths non-obvious.
- **`remote-project-control`**: Use this before remote-heavy work when a repo is edited locally but run on SSH servers. It establishes repo-native project memory and keeps local/remote state explicit across sessions.
- **`init-latex-project`**: Invoked by `project-init` via `scripts/init.sh`. Always expand `~` to the actual home path when calling the script.

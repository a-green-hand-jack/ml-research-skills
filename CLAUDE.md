# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

**ml-research-skills** — a collection of Claude Code skills for the full lifecycle of ML research projects, installable via:

```bash
npx skills add a-green-hand-jack/ml-research-skills
```

All files are instruction documents for AI agents — not executable code. Skills are deployed by copying to `~/.claude/skills/`.

## Testing Changes

No automated tests. To validate a change:
1. Copy the skill directory to `~/.claude/skills/<skill-name>/`
2. Invoke in Claude Code by describing the task
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
| `add-git-tag` | Create an annotated git milestone tag with achievements and next-phase plans |
| `update-docs` | Detect code changes since the last docs commit and surgically update affected documentation |
| `submit-paper` | Pre-submission checklist for LaTeX papers: submission mode, mandatory sections, artifacts, anonymity, bibliography, optional compilation |
| `run-experiment` | Submit an ML experiment to local, SLURM, or RunAI environments with reproducible job scripts in `jobs/` |

## Key Design Patterns

- **`project-init` + `project-sync`**: Core paired workflow. `project-init` creates `paper/` and `code/` sibling repos under a shared parent; `project-sync` keeps `daily_experiments.tex` updated with new results.
- **`new-workspace`**: Worktrees go to `<project-root>/../worktrees/<branch-type>-<branch-name>/`. IDE config dirs (`.vscode`, `.cursor`, `.claude`) are copied (not symlinked). Large shared assets declared in `.worktree-links` are symlinked.
- **`init-latex-project`**: Invoked by `project-init` via `scripts/init.sh`. Always expand `~` to the actual home path when calling the script.

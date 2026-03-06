# Project Skills

A collection of Claude Code skills, slash commands, and agent workflows for research and ML engineering.

## Overview

| Type | What it does | Installs to |
|------|-------------|-------------|
| **Skills** | Extend Claude Code with new capabilities | `~/.claude/skills/` |
| **Commands** | Slash commands (`/cmd`) for common tasks | `~/.claude/commands/` |
| **Workflows** | Multi-step agent procedures | `~/.agent/workflows/` |

---

## Skills

Skills are loaded on-demand by Claude Code. Install them once, use them forever.

### `init-latex-project`

Initialize a LaTeX academic paper project with standard structure, macros, and writing guide.

**Supports:** ICLR, CVPR, ICML, ACM SIGCONF, ACL/*ACL

**Trigger:**
```
/init-latex-project my-paper --venue iclr --git
/init-latex-project my-cvpr-paper . --venue cvpr
```

**What you get:**
- Venue-specific `main.tex` with correct document class and bibliography style
- Full math macro library (`macros.tex`): calligraphic, bold, blackboard bold, operators, theorem environments
- Standard section files: abstract, intro, related, method, exp, conclusion, appendix
- Empty `bib/refs.bib`

---

### `init-python-project`

Initialize a production-ready Python/ML project, or enhance an existing fork.

**Trigger:**
```
/init-python-project
```

**What you get:**
- `src/` layout with editable install via `uv`
- Isolated `tests/` structure mirroring `src/`
- `docs/` with three layers: `outlines/` (planning), `dev/` (features), `src/` (modules)
- Dev tooling: pytest, black, ruff, mypy
- `.env` / `.env.example`, VSCode/Cursor/Claude settings
- Project CLAUDE.md with development principles

**Supports both:**
- **New project**: full scaffold from scratch
- **Fork/Enhancement**: analyze existing repo and add missing components

---

### `prompt-manager`

Set up and manage LLM prompts using a production-grade prompt management system.

**Trigger:** When the user wants to create, organize, version, or manage prompts for LLM applications.

**What you get:**
- YAML config + Jinja2 template separation
- Version management (v1, v2, v3 coexist)
- Multi-level caching (50–90% speedup)
- Pydantic parameter validation
- Hot-reload dev mode

**Directory layout:**
```
prompts/
├── configs/          # YAML: metadata, parameters, LLM config
└── templates/
    ├── common/       # Reusable Jinja2 components
    ├── system/       # System prompts (v1.jinja2, v2.jinja2, ...)
    └── user/         # User prompts
```

---

## Commands

Slash commands available directly in Claude Code as `/command-name`.

### `/init-python-project`
Alias command that triggers the `init-python-project` skill interactively.

### `/new-workspace`
Create a new Git branch or worktree for experiments or features.

- Supports `feature/<name>` and `exp/<name>` branch types
- For worktrees: auto-copies `.vscode`, `.cursor`, `.claude` configs; creates symlinks from `.worktree-links`; runs `uv sync`

### `/setup-git-github`
Configure Git global settings and set up GitHub SSH authentication on a new device.

- Generates ed25519 SSH key
- Configures `~/.ssh/config`
- Guides through adding key to GitHub
- Tests the connection

> **Personalization required**: edit this file to pre-fill your name and email, or leave it interactive.

### `/sync-config`
Sync your `~/.claude/` configuration to remote SSH servers via rsync.

- Smart sync: compares timestamps before pushing/pulling
- Safe excludes: skips session data, credentials, history

> **Personalization required**: edit this file to configure your target server aliases.

---

## Workflows

Multi-step agent procedures for the full research lifecycle. These live in `~/.agent/workflows/` and are invoked by telling the agent which workflow to run.

### `add-git-tag`

Mark a project milestone with an annotated Git tag.

**Use when:** completing a phase and wanting to checkpoint progress.

**Flow:** ask for version + achievements + next plans → preview tag message → create annotated tag → optionally push to remote.

**Example tag format:**
```
Tag: v0.2.0
Date: 2026-03-06

## ✅ This Phase — What Was Achieved
- Implemented baseline model
- Added CIFAR-10 data pipeline

## 🚀 Next Phase — What's Planned
- Ablation studies
- Add attention module
```

---

### `update-docs`

Analyse code changes since the last docs update and refresh documentation files.

**Use when:** code has changed and docs are out of date.

**Flow:** detect project + docs location → find baseline commit (last docs commit) → diff code changes → map changes to affected docs → surgical edits → optionally commit.

**Key behavior:** preserves existing writing style and language; only edits sections affected by the diff.

---

### `project-init`

Initialize a new research project with aligned paper and code repositories.

**Use when:** starting a new research project that needs both a LaTeX paper and Python implementation.

**Output:**
```
~/Projects/<ProjectName>/
├── paper/    ← LaTeX repo (uses init-latex-project)
├── code/     ← Python ML repo (uses init-python-project)
└── PROJECT.md
```

`PROJECT.md` links both repos, documents the research overview (method, datasets, metrics), and defines the workflow between paper and code.

The paper repo gets a `sections/daily_experiments.tex` — a running log of experiment results in reverse chronological order.

---

### `project-sync`

Sync new experiment results from the code repo into the paper's experiment log.

**Use when:** you have new results and want to record them in the paper.

**Flow:** auto-detect `code/` and `paper/` sibling dirs → ask for experiment details (or auto-read from `outputs/logs/`) → preview LaTeX entry → insert at top of `daily_experiments.tex` → optionally commit.

---

## Installation

### Skills

```bash
# Clone this repo
git clone <repo-url> ~/Projects/project-skills

# Install a specific skill
cp -r ~/Projects/project-skills/skills/init-latex-project ~/.claude/skills/

# Install all skills
cp -r ~/Projects/project-skills/skills/* ~/.claude/skills/
```

### Commands

```bash
# Install a specific command
cp ~/Projects/project-skills/commands/new-workspace.md ~/.claude/commands/

# Install all commands
cp ~/Projects/project-skills/commands/* ~/.claude/commands/
```

### Workflows

```bash
# Create the workflows directory if it doesn't exist
mkdir -p ~/.agent/workflows/

# Install all workflows
cp ~/Projects/project-skills/workflows/* ~/.agent/workflows/
```

### Install everything at once

```bash
cp -r ~/Projects/project-skills/skills/* ~/.claude/skills/
cp ~/Projects/project-skills/commands/* ~/.claude/commands/
mkdir -p ~/.agent/workflows/ && cp ~/Projects/project-skills/workflows/* ~/.agent/workflows/
```

---

## How Skills, Commands, and Workflows Fit Together

```
project-init  (workflow)
  ├── init-latex-project  (skill → /init-latex-project)
  └── init-python-project (skill → /init-python-project)
        └── /new-workspace  (command — create experiment branches)

During development:
  ├── prompt-manager      (skill — LLM prompt management)
  ├── update-docs         (workflow — keep docs in sync with code)
  └── project-sync        (workflow — log experiment results to paper)

At milestones:
  ├── add-git-tag         (workflow — annotated version tags)
  └── /sync-config        (command — sync config to remote servers)
```

---

## Contributing

Each skill/command/workflow is a single Markdown file (or a directory with `SKILL.md` + supporting files). To add or improve one:

1. Edit the relevant file
2. Test it by invoking it in Claude Code
3. Submit a PR with a clear description of what changed and why

For skills with scripts, keep `SKILL.md` under 500 lines — move reference material to separate files linked from `SKILL.md`.

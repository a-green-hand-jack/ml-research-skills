# AGENTS.md

Guidance for AI coding agents working in this repository.

## Repository Overview

This repo is **ml-research-skills** — a collection of Claude Code skills for ML researchers, installable via `npx skills add`. Each file is an instruction document for an AI agent, not executable code.

## Directory Structure

```
ml-research-skills/
└── skills/    # → ~/.claude/skills/   (one subdirectory per skill)
    ├── init-latex-project/
    ├── init-python-project/
    ├── project-init/
    ├── project-sync/
    ├── new-workspace/
    ├── add-git-tag/
    └── update-docs/
```

## Adding a New Skill

Skills live in `skills/<skill-name>/` and require a `SKILL.md` with YAML frontmatter:

```markdown
---
name: skill-name
description: One sentence describing when to use this skill. Include trigger phrases.
allowed-tools: Read, Write, Edit, Bash, Glob
---

# Skill Title

Brief description.

## When to Use This Skill
...

## Steps
...
```

**Guidelines:**
- The directory name must exactly match the `name` field
- `name` must be lowercase letters, numbers, and hyphens only
- Keep `SKILL.md` under 500 lines; move reference material to separate linked files
- Use `scripts/` for shell automation (scripts don't consume context, only their output does)
- Use `templates/` for file templates the skill writes out
- Write the `description` as a routing rule, not a title — agents use it to decide when to activate the skill

## Testing

1. Copy the skill directory to `~/.claude/skills/`
2. Invoke in Claude Code by describing the task
3. Verify output and iterate

No automated tests — correctness is validated by running the skill.

## Installation (for users)

```bash
npx skills add <owner>/ml-research-skills
```

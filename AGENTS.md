# AGENTS.md

Guidance for AI coding agents working in this repository.

## Repository Overview

This repo contains Claude Code skills, slash commands, and agent workflows for research and ML engineering. Each file is an instruction document for an AI agent — not executable code.

## Directory Structure

```
project-skills/
├── skills/       # → ~/.claude/skills/   (Claude Code skills, each in its own dir)
├── commands/     # → ~/.claude/commands/ (slash commands, one .md file each)
└── workflows/    # → ~/.agent/workflows/ (multi-step agent workflows, one .md file each)
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
- Keep `SKILL.md` under 500 lines; move reference material to separate linked files
- Use `scripts/` for shell automation (scripts don't consume context, only their output does)
- Use `templates/` for file templates the skill writes out
- Write specific `description` fields — this is what determines when the skill activates

## Adding a New Command

Commands live in `commands/<command-name>.md`. They are plain Markdown instructions for the agent — no frontmatter required, but a clear `#` title and structured steps help.

Commands should:
- Be self-contained (complete one task end-to-end)
- Ask the user for any required personal configuration rather than hardcoding it
- Confirm before taking destructive or irreversible actions

## Adding a New Workflow

Workflows live in `workflows/<workflow-name>.md` with optional YAML frontmatter:

```markdown
---
description: One sentence describing what this workflow does.
---

# Workflow Title
...
```

Workflows should:
- Use `// turbo` comments before steps that should run without user confirmation
- Ask the user for information in a **single message** (not one question at a time)
- Show a preview of any destructive action before executing
- End with a summary of what was done

## Personal Configuration

Two commands require personal configuration before sharing:

- `commands/setup-git-github.md` — asks the user for name/email interactively (do not hardcode)
- `commands/sync-config.md` — asks the user for server aliases interactively (do not hardcode)

When editing these files, keep them generic. Users can maintain a local override in `~/.claude/commands/` if they want pre-filled versions.

## Testing

To test a skill or command locally:
1. Copy it to the appropriate `~/.claude/` or `~/.agent/` directory
2. Invoke it in Claude Code
3. Verify the output and iterate

There are no automated tests — correctness is validated by running the skill.

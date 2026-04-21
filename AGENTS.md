# AGENTS.md

Guidance for AI coding agents working in this repository.

## Repository Overview

This repo is **ml-research-skills** — a collection of agent skills for ML researchers. Each skill lives under `skills/<skill-name>/` as an instruction bundle centered on `SKILL.md`, with optional `scripts/` and `templates/` directories.

Skills in this repo are installed with:

```bash
npx skills add a-green-hand-jack/ml-research-skills
```

These files are primarily agent instructions and templates, not an application with automated runtime tests.

## Current Repository Structure

```text
ml-research-skills/
├── README.md
├── CLAUDE.md
├── AGENTS.md
└── skills/
    ├── add-git-tag/
    │   └── SKILL.md
    ├── init-latex-project/
    │   ├── SKILL.md
    │   ├── scripts/
    │   └── templates/
    ├── init-python-project/
    │   └── SKILL.md
    ├── new-workspace/
    │   └── SKILL.md
    ├── project-init/
    │   └── SKILL.md
    ├── project-sync/
    │   └── SKILL.md
    ├── release-code/
    │   ├── SKILL.md
    │   ├── checklist.md
    │   └── templates/
    ├── run-experiment/
    │   ├── SKILL.md
    │   ├── environments.yaml
    │   └── templates/
    ├── submit-paper/
    │   ├── SKILL.md
    │   └── scripts/
    └── update-docs/
        └── SKILL.md
```

## Current Skill Set

| Skill | Purpose |
|---|---|
| `init-latex-project` | Initialize a LaTeX paper project with venue-specific templates, macros, and downloaded style files |
| `init-python-project` | Create or enhance a production-ready Python/ML project using `uv` |
| `project-init` | Create a parent research workspace with aligned `paper/` and `code/` repos |
| `project-sync` | Sync experiment results from the code repo into the paper's `daily_experiments.tex` |
| `new-workspace` | Create a Git branch or worktree for features and experiments |
| `run-experiment` | Generate reproducible local / SLURM / RunAI job scripts and submission commands |
| `submit-paper` | Run a pre-submission readiness check for a LaTeX paper project |
| `release-code` | Prepare and publish a research code repository for public release |
| `add-git-tag` | Create an annotated milestone tag with achievements and next-phase plans |
| `update-docs` | Detect code changes since the last docs update and refresh affected documentation |

## Adding or Updating a Skill

Skills live in `skills/<skill-name>/` and must include a `SKILL.md` with YAML frontmatter:

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

Guidelines:
- The directory name must exactly match the `name` field.
- `name` must use lowercase letters, numbers, and hyphens only.
- Keep `SKILL.md` under 500 lines; move large references into linked files.
- Use `scripts/` for shell automation so the agent can run commands without embedding large shell blocks inline.
- Use `templates/` for files the skill writes into user projects.
- Write the `description` as a routing rule, not a title. Agents use it to decide when to activate the skill.
- Keep examples and venue/tooling references aligned with the actual templates and scripts shipped in the same skill directory.

## Validation

There are no automated tests in this repository. Before manual validation, run the local repository sanity check:

```bash
python3 scripts/validate_skills.py
```

Then validate changes by exercising the skill in the target agent runtime:

1. Copy the skill directory to the target agent's skill home, such as `~/.claude/skills/` or `~/.agents/skills/`
2. Invoke it by describing a matching task
3. Check that the generated instructions, scripts, and templates behave as intended

## Notes for Agents

- Prefer updating the minimum set of files needed when a skill changes.
- If you change a skill's behavior, also check whether `README.md` and `CLAUDE.md` now need corresponding updates.
- Treat `SKILL.md`, helper scripts, and templates as a single unit; avoid documenting behavior that the shipped assets do not actually support.

# AGENTS.md

Guidance for AI coding agents working in this repository.

## Repository Overview

This repo is **ml-research-skills** — a collection of agent skills for ML researchers. Each skill lives under `skills/<skill-name>/` as an instruction bundle centered on `SKILL.md`, with optional `scripts/` and `templates/` directories.

Skills in this repo are installed with:

```bash
npx skills add a-green-hand-jack/ml-research-skills
```

To install globally for both Codex and Claude Code:

```bash
npx skills add a-green-hand-jack/ml-research-skills -g -a codex claude-code -y
```

To install one specific skill globally for both agents:

```bash
npx skills add a-green-hand-jack/ml-research-skills -g -a codex claude-code -s remote-project-control -y
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
    ├── research-idea-validator/
    │   ├── SKILL.md
    │   └── references/
    ├── init-latex-project/
    │   ├── SKILL.md
    │   ├── scripts/
    │   └── templates/
    ├── init-python-project/
    │   └── SKILL.md
    ├── new-workspace/
    │   └── SKILL.md
    ├── experiment-design-planner/
    │   ├── SKILL.md
    │   └── references/
    ├── experiment-report-writer/
    │   ├── SKILL.md
    │   └── templates/
    ├── conference-writing-adapter/
    │   ├── SKILL.md
    │   └── references/
    ├── paper-reviewer-simulator/
    │   ├── SKILL.md
    │   └── references/
    ├── rebuttal-strategist/
    │   ├── SKILL.md
    │   └── references/
    ├── citation-coverage-audit/
    │   ├── SKILL.md
    │   └── references/
    ├── citation-audit/
    │   ├── SKILL.md
    │   ├── references/
    │   └── scripts/
    ├── work-timeline-planner/
    │   ├── SKILL.md
    │   ├── references/
    │   └── templates/
    ├── project-init/
    │   └── SKILL.md
    ├── project-sync/
    │   └── SKILL.md
    ├── safe-git-ops/
    │   ├── SKILL.md
    │   └── references/
    ├── remote-project-control/
    │   ├── SKILL.md
    │   ├── references/
    │   ├── template_manifest.json
    │   └── templates/
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
| `research-idea-validator` | Turn a rough research idea into a pursue/revise/park/kill decision using novelty, feasibility, evidence, and reviewer-risk analysis |
| `init-latex-project` | Initialize a LaTeX paper project with venue-specific templates, macros, and downloaded style files |
| `init-python-project` | Create or enhance a production-ready Python/ML project using `uv` |
| `project-init` | Create a parent research workspace with aligned `paper/` and `code/` repos |
| `project-sync` | Sync experiment results from the code repo into the paper's `daily_experiments.tex` |
| `new-workspace` | Create a Git branch or worktree for features and experiments |
| `experiment-design-planner` | Design hypothesis-driven experiments with baselines, ablations, metrics, controls, logging, and stop conditions before running |
| `experiment-report-writer` | Write structured experiment reports from notes, configs, logs, metrics, tables, and figures |
| `conference-writing-adapter` | Adapt an ML paper's structure, positioning, and paragraph-level writing to a target conference using venue exemplars and reusable writing memory |
| `paper-reviewer-simulator` | Simulate target-conference reviewers, predicted scores, likely reject reasons, meta-review, rebuttal risks, and a ranked pre-submission risk register |
| `rebuttal-strategist` | Analyze real reviews, infer reviewer intent, plan rebuttal experiments, draft responses, and track promised revisions |
| `citation-coverage-audit` | Find missing classic, closest, benchmark, and recent concurrent citations before submission |
| `citation-audit` | Run a pre-submission audit of LaTeX citation keys, BibTeX entries, metadata, citation claims, labels, and references |
| `work-timeline-planner` | Build Markdown or HTML timeline reports with Gantt-style visualizations from git history, docs, notes, and user context |
| `safe-git-ops` | Perform common Git operations safely with better worktree and sandbox failure diagnosis |
| `remote-project-control` | Recover project memory and safely coordinate local-to-remote SSH workflows |
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

This covers frontmatter, helper references, top-level skill inventory consistency, template placeholder format, and basic Python/shell syntax.

For the `init-python-project` scaffold smoke test, run:

```bash
python3 -m unittest -v tests.test_init_python_project_scaffold
```

Then validate changes by exercising the skill in the target agent runtime:

1. Install the skill with `npx skills add`, such as `npx skills add a-green-hand-jack/ml-research-skills -g -a codex claude-code -s <skill-name> -y`
2. Invoke it by describing a matching task
3. Check that the generated instructions, scripts, and templates behave as intended

## Notes for Agents

- Prefer updating the minimum set of files needed when a skill changes.
- If you change a skill's behavior, also check whether `README.md` and `CLAUDE.md` now need corresponding updates.
- Treat `SKILL.md`, helper scripts, and templates as a single unit; avoid documenting behavior that the shipped assets do not actually support.

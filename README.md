# ml-research-skills

Claude Code skills for the full ML research workflow: initializing paper and code repos, running experiments, syncing results, updating docs, checking paper readiness, and tagging milestones.

## Install

Install the full collection:

```bash
npx skills add a-green-hand-jack/ml-research-skills
```

Or install a specific skill:

```bash
npx skills add a-green-hand-jack/ml-research-skills --skill init-latex-project
npx skills add a-green-hand-jack/ml-research-skills --skill run-experiment
npx skills add a-green-hand-jack/ml-research-skills --skill submit-paper
```

Installed skills are copied into `~/.claude/skills/`.

## Skills

| Skill | What it does |
|---|---|
| `init-latex-project` | Scaffold a LaTeX academic paper project with venue-specific templates, macros, and official style files |
| `init-python-project` | Create or enhance a production-ready Python/ML project using `uv`, pytest, black, ruff, and mypy |
| `project-init` | Set up a parent research workspace with aligned `paper/` and `code/` repositories plus `PROJECT.md` |
| `project-sync` | Sync experiment results from the code repo into the paper's `sections/daily_experiments.tex` log |
| `new-workspace` | Create a Git branch or worktree for a new feature or experiment |
| `run-experiment` | Generate reproducible local, SLURM, or RunAI job scripts and submission commands |
| `submit-paper` | Run a pre-submission checklist for a LaTeX paper, including anonymity, mandatory sections, and optional compile checks |
| `add-git-tag` | Create an annotated milestone tag with achievements and next-phase plans |
| `update-docs` | Detect changes since the last docs update and refresh only the affected documentation |

## Typical Workflow

```text
1. project-init       -> create a parent workspace with paper/ and code/
2. new-workspace      -> isolate a feature or experiment branch
3. run-experiment     -> launch locally or on SLURM / RunAI
4. project-sync       -> record results in paper/sections/daily_experiments.tex
5. update-docs        -> refresh docs after meaningful code changes
6. submit-paper       -> run a readiness check before a deadline
7. add-git-tag        -> mark a milestone
```

## What `init-latex-project` Provides

- A complete LaTeX paper scaffold with `main.tex`, `macros.tex`, and a writing guide for agents
- Venue-specific templates for `icml`, `acl`, `emnlp`, `naacl`, `iccv`, `eccv`, `neurips`, `iclr`, `cvpr`, and `acm`
- Support for generic non-venue projects by using the default template without `--venue`
- A helper script that downloads official style files where needed and writes `venue_preamble.tex`

## What `init-python-project` Provides

- A four-layer ML project structure: `src/`, `experiments/`, `eval/`, and `infra/`
- `uv`-based Python project setup with editable installs
- Development tooling: pytest, black, ruff, and mypy
- Project docs scaffolding under `docs/`
- Editor configuration for Claude Code / Cursor / VS Code

## What `run-experiment` Provides

- Reproducible job templates under `jobs/` for local runs, SLURM clusters, and RunAI/Kubernetes
- A shared `environments.yaml` registry for cluster-specific defaults
- Built-in support for:
  - `local`
  - `ibex` (KAUST SLURM)
  - `uw` (placeholder SLURM profile to customize)
  - `runai` (EPFL RunAI / Kubernetes)

## What `submit-paper` Checks

- Submission mode in `venue_preamble.tex`
- Drafting artifacts such as TODOs and comment macros
- Venue-specific required sections and bibliography presence
- Basic anonymity issues for blind review
- Optional compile checks and page-count sanity checks

## Validation

There are no automated tests in this repository. To validate a skill:

1. Copy the skill directory to `~/.claude/skills/<skill-name>/`
2. Invoke it in Claude Code with a matching request
3. Inspect the generated files, commands, or instructions and iterate

## Requirements

- [Claude Code](https://claude.ai/code)
- [npx skills](https://github.com/vercel-labs/skills)
- For Python-related skills: [uv](https://docs.astral.sh/uv/)
- For LaTeX-related skills: a TeX distribution such as TeX Live or MiKTeX

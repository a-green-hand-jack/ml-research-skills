# ml-research-skills

Agent skills for the full ML research workflow: initializing paper and code repos, running experiments, syncing results, updating docs, checking paper readiness, preparing releases, and tagging milestones.

## Install

Install the full collection:

```bash
npx skills add a-green-hand-jack/ml-research-skills
```

Or install a specific skill:

```bash
npx skills add a-green-hand-jack/ml-research-skills --skill init-latex-project
npx skills add a-green-hand-jack/ml-research-skills --skill run-experiment
npx skills add a-green-hand-jack/ml-research-skills --skill remote-project-control
npx skills add a-green-hand-jack/ml-research-skills --skill submit-paper
```

Installed skills are copied into the target agent's global skill home, for example `~/.claude/skills/` for Claude Code or `~/.agents/skills/` for Codex.

## Skills

| Skill | What it does |
|---|---|
| `init-latex-project` | Scaffold a LaTeX academic paper project with venue-specific templates, macros, and official style files |
| `init-python-project` | Create or enhance a production-ready Python/ML project using `uv`, pytest, black, ruff, and mypy |
| `project-init` | Set up a parent research workspace with aligned `paper/` and `code/` repositories plus `PROJECT.md` |
| `project-sync` | Sync experiment results from the code repo into the paper's `sections/daily_experiments.tex` log |
| `new-workspace` | Create a Git branch or worktree for a new feature or experiment |
| `remote-project-control` | Recover project memory and safely coordinate local-to-remote SSH workflows for research repos |
| `run-experiment` | Generate reproducible local, SLURM, or RunAI job scripts and submission commands |
| `submit-paper` | Run a pre-submission checklist for a LaTeX paper, including anonymity, mandatory sections, and optional compile checks |
| `release-code` | Prepare a research code repository for public release with audit, README/LICENSE/CITATION, tagging, and optional GitHub release |
| `add-git-tag` | Create an annotated milestone tag with achievements and next-phase plans |
| `update-docs` | Detect changes since the last docs update and refresh only the affected documentation |

## Typical Workflow

```text
1. project-init       -> create a parent workspace with paper/ and code/
2. new-workspace      -> isolate a feature or experiment branch
3. remote-project-control -> recover project memory and align local vs remote state
4. run-experiment     -> launch locally or on SLURM / RunAI
5. project-sync       -> record results in paper/sections/daily_experiments.tex
6. update-docs        -> refresh docs after meaningful code changes
7. submit-paper       -> run a readiness check before a deadline
8. release-code       -> prepare the public code release when needed
9. add-git-tag        -> mark a milestone
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

## What `remote-project-control` Provides

- A repo-native memory model for projects developed locally but executed remotely over SSH
- Shared and private memory files for server mappings, working status, and local overrides
- Safe orchestration for inspect, sync, remote job submission, monitoring, and artifact lookup
- A clean handoff layer between project memory and `run-experiment`

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

## What `release-code` Provides

- A release audit for secrets, large files, and missing repo hygiene
- Templates for `README.md` and `CITATION.cff`
- License generation guidance
- A structured tagging and publishing flow for public code releases

## Validation

There are no automated tests in this repository. For a quick repository sanity check, run:

```bash
python3 scripts/validate_skills.py
```

This validator checks frontmatter parsing, skill-directory name alignment, helper-file references, hardcoded Claude-only skill paths, text-template placeholder format, skill inventory consistency in the top-level docs, and basic Python/shell syntax for helper scripts.

For the `init-python-project` scaffold smoke test, run:

```bash
python3 -m unittest -v tests.test_init_python_project_scaffold
```

To validate a skill end-to-end:

1. Copy the skill directory to the target agent's skill home (for example `~/.claude/skills/<skill-name>/` or `~/.agents/skills/<skill-name>/`)
2. Invoke it in the corresponding agent with a matching request
3. Inspect the generated files, commands, or instructions and iterate

## Requirements

- [Claude Code](https://claude.ai/code) or another compatible agent runtime
- [npx skills](https://github.com/vercel-labs/skills)
- For Python-related skills: [uv](https://docs.astral.sh/uv/)
- For LaTeX-related skills: a TeX distribution such as TeX Live or MiKTeX

# Python Project Architecture

The ML project layout follows a four-layer architecture with strict one-way dependencies:

`infra` -> `experiments/eval` -> `src`

Lower layers never import from higher layers.

## Standard ML Layout

```text
<project-name>/
├── src/
│   └── <package_name>/          # Layer 1: Algorithm core (pure, portable)
│       ├── __init__.py
│       ├── models/
│       ├── data/
│       └── utils/
├── experiments/                 # Layer 2: Experiment logic ("what to run")
│   ├── configs/
│   │   └── base.yaml
│   ├── config.py                # Loads infra/envs/<ENV>.yaml + configs/
│   ├── train.py
│   ├── evaluate.py
│   └── README.md
├── eval/                        # Layer 3: Evaluation & baselines
│   ├── benchmarks/
│   ├── baselines/
│   │   └── reproduced/
│   └── metrics.py
├── infra/                       # Layer 4: Platform configs ("how to run")
│   ├── envs/
│   │   ├── local.yaml
│   │   └── <cluster>.yaml
│   ├── remote-projects.yaml     # Shared local/remote execution memory
│   ├── submit/
│   │   └── slurm/
│   └── README.md
├── tests/                       # Unit tests for src/ only
│   ├── __init__.py
│   ├── data/
│   ├── outputs/
│   ├── conftest.py
│   └── ...
├── docs/
│   ├── outlines/
│   │   ├── project_plan.md
│   │   └── progress.md
│   ├── results/                 # Stable result summaries and paper-facing table/figure notes
│   ├── reports/                 # Experiment reports and technical result writeups
│   ├── runs/                    # Run registry, job pointers, config/commit pointers
│   ├── ops/
│   │   ├── current-status.md
│   │   └── decision-log.md
│   └── dev/
│       ├── feature_template.md
│       └── features/
├── .agent/
│   └── local-overrides.yaml
├── .gitmodules
├── .vscode/
│   └── settings.json
├── .cursor/
│   └── settings.json
├── .claude/
│   └── commands/
├── .env
├── .env.example
├── .gitignore
├── pyproject.toml
├── README.md
├── AGENTS.md
└── CLAUDE.md
```

## Layer Rules

| Layer | What lives here | May import from |
|---|---|---|
| `src/<pkg>/` | Core algorithm, pure Python | nothing in this repo |
| `experiments/` | Training / eval entry points | `src/<pkg>/` |
| `eval/` | Benchmarks, baselines | `src/<pkg>/` |
| `infra/` | Cluster configs, submit scripts | nothing |

Migrating to a new HPC should only require adding one YAML file to `infra/envs/`. Science code should not change.

For projects that are developed locally but run remotely, store stable mapping and policy in `infra/remote-projects.yaml`, keep cross-session working memory in `docs/ops/`, and keep private machine-specific overrides in `.agent/local-overrides.yaml`.

## Experiment Evidence Policy

`experiments/` is runnable logic, not a result archive.

Use:

- `docs/results/` for stable result summaries, table notes, and figure notes that are small enough to review and commit.
- `docs/reports/` for `experiment-report-writer` outputs and technical result narratives.
- `docs/runs/` for run registries, job IDs, config pointers, commit hashes, remote output paths, and short metric summaries.

Do not commit raw training outputs, checkpoints, large logs, tensorboard caches, or wandb directories. Keep those in ignored paths such as `outputs/`, `logs/`, `checkpoints/`, or external storage, then link to them from `docs/runs/`.

## Worktree Policy

Do not place linked worktrees inside the main code repo by default.

When this code repo is part of a project control root, prefer:

```text
<ProjectName>/
├── code/
└── code-worktrees/
    ├── exp-<name>/
    └── rebuttal-<name>/
```

Each code worktree should keep its own `.agent/worktree-status.md` and may use the same `docs/results/`, `docs/reports/`, and `docs/runs/` convention for branch-local evidence.

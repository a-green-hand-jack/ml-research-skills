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
│   └── dev/
│       ├── feature_template.md
│       └── features/
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

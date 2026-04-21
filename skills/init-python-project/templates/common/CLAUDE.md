# Claude Code Instructions for {{PROJECT_NAME}}

## Project Overview

{{DESCRIPTION}}

## Four-Layer Architecture

This project uses a strict layered structure. Dependencies flow one way only.

| Layer | Directory | Role |
|---|---|---|
| 1 | `src/{{PACKAGE_NAME}}/` | Algorithm core |
| 2 | `experiments/` | Entry points |
| 3 | `eval/` | Benchmarks and baselines |
| 4 | `infra/` | Platform configs |

## Rules You Must Follow

- Never hardcode file paths in `src/` or `experiments/`.
- Run experiments with `ENV=<name> uv run python experiments/train.py`.
- Add published baselines as submodules under `eval/baselines/`.
- Add new cluster configs in `infra/envs/`; do not fork science code per cluster.

## Development Principles

1. Keep tests close to the modules they cover.
2. Format with `black`, lint with `ruff`, type-check with `mypy`.
3. Prefer editable installs and absolute imports.
4. Update docs when structure or behavior changes.

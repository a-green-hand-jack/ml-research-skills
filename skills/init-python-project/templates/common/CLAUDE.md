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
- Treat `experiments/` as runnable logic, not a result archive.
- Put stable result summaries in `docs/results/`, experiment reports in `docs/reports/`, and run/job/config/commit pointers in `docs/runs/`.
- Keep raw outputs, logs, checkpoints, tensorboard caches, and wandb runs out of Git.
- Add published baselines as submodules under `eval/baselines/`.
- Add new cluster configs in `infra/envs/`; do not fork science code per cluster.
- Keep `infra/remote-projects.yaml` updated if this project is controlled locally but executed remotely.
- Treat `docs/ops/current-status.md` as working memory, not execution truth; re-check volatile remote state before acting.
- Put private SSH aliases or machine-specific overrides in `.agent/local-overrides.yaml`, not in shared repo files.

## Development Principles

1. Keep tests close to the modules they cover.
2. Use the toolchain gates below before commit, push, experiment submission, release, or artifact handoff.
3. Prefer editable installs and absolute imports.
4. Update docs when structure or behavior changes.
5. Use the `remote-project-control` skill before sync, remote submission, monitoring, or artifact inspection workflows.
6. If this repo is part of a project control root, prefer sibling code worktrees under `../code-worktrees/` rather than nested worktrees inside this repo.

## Toolchain Gates

Default to check-before-mutate. Run non-mutating gates first:

```bash
uv sync
uv run ruff format --check src tests experiments scripts
uv run ruff check src tests experiments scripts
uv run mypy src
uv run pytest tests -v
```

Run mutating commands only when requested or required by project policy, then review the diff:

```bash
uv run ruff format src tests experiments scripts
uv run ruff check --fix src tests experiments scripts
```

If this repo documents different tools such as `black`, `isort`, `pyright`, `pre-commit`, or CI-specific commands, follow the documented repo-local toolchain and update this section.

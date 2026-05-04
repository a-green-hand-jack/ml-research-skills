# AGENTS.md - AI Agent Guide for {{PROJECT_NAME}}

This file is the universal/Codex entrypoint for agents working in this code repo. `CLAUDE.md` is the Claude Code entrypoint. Keep both files semantically aligned.

## Project Overview

{{DESCRIPTION}}

## Architecture

This project uses a strict four-layer structure. Dependencies flow one way only.

| Layer | Directory | Role |
|---|---|---|
| 1 | `src/{{PACKAGE_NAME}}/` | Algorithm core |
| 2 | `experiments/` | Entry points |
| 3 | `eval/` | Benchmarks and baselines |
| 4 | `infra/` | Platform configs |

## Rules

- Never hardcode file paths in `src/` or `experiments/`.
- Run experiments with `ENV=<name> uv run python experiments/train.py`.
- Treat `experiments/` as runnable logic, not a result archive.
- Put stable result summaries in `docs/results/`, experiment reports in `docs/reports/`, and run/job/config/commit pointers in `docs/runs/`.
- Keep raw outputs, logs, checkpoints, tensorboard caches, and wandb runs out of Git.
- Add published baselines as submodules under `eval/baselines/`.
- Add new cluster configs in `infra/envs/`; do not fork science code per cluster.
- Keep `infra/remote-projects.yaml` updated if this project is controlled locally but executed remotely.
- Treat `docs/ops/current-status.md` as operational memory, not execution truth; re-check volatile remote state before acting.
- Put private SSH aliases or machine-specific overrides in `.agent/local-overrides.yaml`, not in shared repo files.
- If this repo is part of a project control root, prefer sibling code worktrees under `../code-worktrees/` rather than nested worktrees inside this repo.
- Keep cross-worktree rollups in `.agent/worktree-index.md` when this repo uses sibling worktrees.

## Toolchain Gates

Default to check-before-mutate. Run non-mutating gates before commit, push, experiment submission, release, or artifact handoff:

```bash
uv sync
uv run ruff format --check src tests experiments scripts
uv run ruff check src tests experiments scripts
uv run mypy src
uv run pytest tests -v
uv run pre-commit run --all-files
```

Run mutating commands only when requested or required by project policy, then review the diff:

```bash
uv run ruff format src tests experiments scripts
uv run ruff check --fix src tests experiments scripts
```

The bundled `.pre-commit-config.yaml` is a local gate runner. It uses project/system tools when available for secrets (`gitleaks`), shell (`shellcheck`, `shfmt`), notebooks (`nbstripout`), GitHub Actions (`actionlint`), TOML/YAML (`taplo`, `yamllint`), and docs links (`lychee`). Missing optional tools are reported as skipped unless project policy makes them required.

If this repo documents different tools such as `black`, `isort`, `pyright`, `pre-commit`, or CI-specific commands, follow the documented repo-local toolchain and update this section.

## Compatibility

Also keep `CLAUDE.md` aligned with this file. If the two files disagree, stop and ask which policy should be canonical before editing.

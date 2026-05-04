# New Project Flow

Use this flow when the user wants a new Python project from scratch.

## Questions to Gather

Ask for:

1. Project name
2. Package name
3. Short description
4. Python version
5. Project type: `ml`, `web`, `lib`, or `general`
6. GitHub repository URL, if available
7. Author name and email

## Recommended Scaffolding Strategy

For `ml` projects, create the full four-layer layout from `references/architecture.md`.

For the standard `new + ml` path, prefer `scripts/scaffold_new_project.py` so directory creation, template copying, and placeholder replacement stay deterministic.

For `web`, `lib`, and `general`, keep the common project files but trim ML-specific directories if they are not justified. Do not force `experiments/`, `eval/`, or `infra/` into projects that clearly do not need them.

## Template Sources of Truth

Use `template_manifest.json` as the source of truth for which templates belong to the scaffold. The files still live under `templates/`, but the manifest defines the groups and placeholder set.

- Common templates:
  - `templates/common/.gitignore`
  - `templates/common/.env.example`
  - `templates/common/README.md`
  - `templates/common/AGENTS.md`
  - `templates/common/CLAUDE.md`
  - `templates/common/.pre-commit-config.yaml`
  - `templates/common/pyproject.toml.tmpl`
  - `templates/common/tests/conftest.py`
  - `templates/common/docs/outlines/project_plan.md`
  - `templates/common/docs/outlines/progress.md`
  - `templates/common/docs/results/.gitkeep`
  - `templates/common/docs/reports/.gitkeep`
  - `templates/common/docs/runs/.gitkeep`
  - `templates/common/docs/dev/feature_template.md`
  - `templates/common/docs/src/dependencies.md`
  - `templates/common/.vscode/settings.json`
- ML-specific templates:
  - `templates/ml/experiments/config.py`
  - `templates/ml/experiments/configs/base.yaml`
  - `templates/ml/infra/envs/local.yaml`
  - `templates/ml/infra/envs/cluster.yaml.example`
  - `templates/ml/infra/remote-projects.yaml`
  - `templates/ml/infra/README.md`
  - `templates/ml/docs/ops/current-status.md`
  - `templates/ml/docs/ops/decision-log.md`
  - `templates/ml/.agent/local-overrides.yaml`
  - `templates/ml/eval/baselines/README.md`
  - `templates/ml/scripts/train.py`
  - `templates/ml/scripts/download_data.py`

## Placeholder Variables

Replace these placeholders when materializing templates:

- `{{PROJECT_NAME}}`
- `{{PACKAGE_NAME}}`
- `{{DESCRIPTION}}`
- `{{PYTHON_VERSION}}`
- `{{AUTHOR_NAME}}`
- `{{AUTHOR_EMAIL}}`
- `{{REPO_URL}}`
- `{{LOCAL_REPO_ROOT}}`
- `{{DEFAULT_BRANCH}}`
- `{{DEFAULT_SERVER_NAME}}`
- `{{DEFAULT_SSH_ALIAS}}`
- `{{DEFAULT_REMOTE_REPO_ROOT}}`
- `{{DEFAULT_SCHEDULER}}`
- `{{DEFAULT_LAUNCH_MODE}}`
- `{{DEFAULT_ENV_ACTIVATION}}`
- `{{DATE}}`

If the user did not provide a value such as `REPO_URL`, leave a clear `TBD` marker instead of fabricating one.

## Code-Side Evidence Layout

For ML projects, make the distinction explicit:

- `experiments/` contains runnable training/evaluation logic and configs.
- `docs/results/` contains small stable result summaries and table/figure notes.
- `docs/reports/` contains experiment reports and result narratives.
- `docs/runs/` contains run pointers, job IDs, commit/config references, and short metric summaries.

Raw outputs, checkpoints, logs, tensorboard caches, and wandb runs should be ignored or stored externally, with pointers from `docs/runs/`.

## Default Toolchain Gates

For new projects, make the gate commands explicit in `README.md`, `AGENTS.md`, and `CLAUDE.md`.

Default ML code gates:

```bash
uv sync
uv run ruff format --check src tests experiments scripts
uv run ruff check src tests experiments scripts
uv run mypy src
uv run pytest tests -v
uv run pre-commit run --all-files
```

For non-ML projects, omit paths that do not exist. Use mutating commands only when requested or required:

```bash
uv run ruff format src tests experiments scripts
uv run ruff check --fix src tests experiments scripts
```

If the user asks for `black`, `isort`, `pyright`, `pre-commit`, or another tool, document that policy instead of mixing competing formatters without a reason.

The default `.pre-commit-config.yaml` uses local hooks so the commands stay aligned with the repo's installed tools. It checks Python formatting/lint/type/test gates, shell scripts with `shellcheck` and `shfmt` when installed, secrets with `gitleaks` when installed, notebooks with `nbstripout` when installed, GitHub Actions with `actionlint` when installed, TOML/YAML config with `taplo`/`yamllint` when installed, and docs links with `lychee` when installed.

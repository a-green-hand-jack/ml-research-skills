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

For `web`, `lib`, and `general`, keep the common project files but trim ML-specific directories if they are not justified. Do not force `experiments/`, `eval/`, or `infra/` into projects that clearly do not need them.

## Template Sources of Truth

Use the files under `templates/` instead of copying long blocks from `SKILL.md`.

- Common templates:
  - `templates/common/.gitignore`
  - `templates/common/.env.example`
  - `templates/common/README.md`
  - `templates/common/CLAUDE.md`
  - `templates/common/pyproject.toml.tmpl`
  - `templates/common/tests/conftest.py`
  - `templates/common/docs/outlines/project_plan.md`
  - `templates/common/docs/outlines/progress.md`
  - `templates/common/docs/dev/feature_template.md`
  - `templates/common/docs/src/dependencies.md`
  - `templates/common/.vscode/settings.json`
- ML-specific templates:
  - `templates/ml/experiments/config.py`
  - `templates/ml/experiments/configs/base.yaml`
  - `templates/ml/infra/envs/local.yaml`
  - `templates/ml/infra/envs/cluster.yaml.example`
  - `templates/ml/infra/README.md`
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

If the user did not provide a value such as `REPO_URL`, leave a clear `TBD` marker instead of fabricating one.

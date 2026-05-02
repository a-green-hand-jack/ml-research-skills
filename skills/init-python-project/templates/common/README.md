# {{PROJECT_NAME}}

{{DESCRIPTION}}

## Installation

### Prerequisites

- Python {{PYTHON_VERSION}}
- `uv` (recommended) or `pip`

### Setup

1. Clone the repository:

```bash
git clone {{REPO_URL}}
cd {{PROJECT_NAME}}
```

2. Install dependencies:

```bash
uv sync
uv pip install -e ".[dev]"
uv pip install -e ".[dev,ml]"
```

3. Set up environment variables:

```bash
cp .env.example .env
```

## Project Structure

- `src/{{PACKAGE_NAME}}/` - main source code
- `tests/` - unit tests
- `docs/` - documentation and planning
- `docs/results/` - stable result summaries and paper-facing table/figure notes
- `docs/reports/` - experiment reports and technical result writeups
- `docs/runs/` - run registry, job pointers, config and commit pointers
- `scripts/` - executable scripts
- `experiments/` - runnable experiment logic and configs
- `infra/remote-projects.yaml` - shared local/remote project mapping and execution policy
- `docs/ops/current-status.md` - cross-session working memory for ongoing remote work

## Remote Workflow Bootstrap

If this project is developed locally but runs on a remote server, fill in these files early:

- `infra/remote-projects.yaml`
- `docs/ops/current-status.md`
- `docs/ops/decision-log.md`
- `.agent/local-overrides.yaml` for private machine-specific values

Recommended workflow:

1. Update `infra/remote-projects.yaml` with the real SSH alias, remote repo path, and scheduler.
2. Keep `docs/ops/current-status.md` current so new coding-agent sessions can recover context quickly.
3. Use the `remote-project-control` skill before remote-heavy work such as sync, submit, monitor, or artifact lookup.

## Usage

### Training

```bash
python scripts/train.py
```

### Testing

```bash
pytest tests/
```

## Experiment Evidence

Use `experiments/` for runnable logic. Keep code-side evidence in:

- `docs/results/` for small stable result summaries
- `docs/reports/` for experiment reports
- `docs/runs/` for run IDs, config paths, commit hashes, remote output paths, and short metric summaries

Raw outputs, checkpoints, logs, tensorboard caches, and wandb runs should stay in ignored paths or external storage.

## Development

### Code Quality

```bash
black src/ tests/
ruff check src/ tests/
mypy src/
```

## Authors

- {{AUTHOR_NAME}} <{{AUTHOR_EMAIL}}>

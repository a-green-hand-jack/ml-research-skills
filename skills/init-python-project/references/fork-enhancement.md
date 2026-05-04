# Fork / Enhancement Flow

Use this flow when the user wants to clone an existing Python repository and bring it up to the repo standard.

## Baseline Analysis

Check what already exists before writing anything:

- `pyproject.toml`, `setup.py`, `requirements.txt`
- `src/`, `tests/`, `docs/`, `scripts/`
- `.env.example`, `AGENTS.md`, `CLAUDE.md`, `.vscode/settings.json`
- pytest configuration and editable-install support

## Enhancement Checklist

1. Directory structure
   - Does `tests/` mirror `src/`?
   - Are `tests/data/` and `tests/outputs/` isolated?
   - Are `docs/outlines/`, `docs/dev/`, and `docs/src/` present if the repo is large enough to justify them?
2. Configuration
   - Is there a `pyproject.toml`, or only `requirements.txt`?
   - Is the package installable?
   - Is there an `.env.example`?
3. Documentation
   - Are paired project instruction files such as `AGENTS.md` and `CLAUDE.md` present?
   - Are module docs or dependency notes present?
4. Testing
   - Is pytest configured?
   - Is there a `conftest.py`?
   - Is coverage obviously too low?
5. Toolchain gates
   - Is formatting checked with `ruff format --check`, `black --check`, or another formatter?
   - Is linting checked with `ruff check`, `flake8`, or another linter?
   - Is type checking configured with `mypy`, `pyright`, or another checker?
   - Are tests and CI/PR checks documented?
   - Is `pre-commit` configured as a local gate runner?
   - Are secret, shell, notebook, config, workflow, and link checks present when the repo has those file types?

## Enhancement Rules

- Add only missing components; do not rewrite a healthy repo into the full ML scaffold unless the user explicitly wants that.
- Reuse the common templates under `templates/common/` to fill gaps.
- If migrating from `requirements.txt`, offer to create a `pyproject.toml` using `templates/common/pyproject.toml.tmpl`.
- Show the user a concise analysis report before bulk edits when the repo already has substantial structure.
- Preserve an existing healthy toolchain. Do not replace `black`, `isort`, `pyright`, `pre-commit`, `gitleaks`, `shellcheck`, `shfmt`, `actionlint`, `nbstripout`, or CI commands just because the new scaffold defaults to `ruff`, `mypy`, `pytest`, and local `pre-commit` hooks.

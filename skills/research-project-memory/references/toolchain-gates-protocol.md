# Toolchain Gates Protocol

Toolchain gates make project tools explicit. They answer which commands should run before commit, push, experiment submission, paper submission, camera-ready cleanup, artifact release, or public release.

## Core Policy

Default to check-before-mutate:

- Run non-mutating checks automatically when they are cheap and available.
- Run mutating format or fix commands only when the user asks, a documented project policy requires them, or the task cannot finish without them.
- Review diffs after any formatter or auto-fixer runs.
- Treat missing optional tools as a reported skip unless the gate is explicitly required.
- Do not confuse source hygiene checks with execution truth. A formatter, linter, or static checker does not replace tests, compile logs, remote job status, or artifact smoke tests.

## Default Gate Families

Code repos:

```text
uv sync
uv run ruff format --check src tests experiments scripts
uv run ruff check src tests experiments scripts
uv run mypy src
uv run pytest tests -v
```

Use `ruff format` / `ruff check --fix` only after the user requests formatting/fixes or project policy requires them. If an existing repo already uses `black`, `isort`, `pyright`, `pre-commit`, or another checker, preserve the existing toolchain and record the actual commands instead of forcing the default scaffold policy.

Paper repos:

```text
tex-fmt --check --nowrap --recursive .
bash <submit-paper-skill-dir>/scripts/check.sh "$PAPER_DIR"
```

Use `tex-fmt --nowrap --recursive .` only after formatting is requested or required, then review the diff. Treat Overleaf/GitHub or local LaTeX compile output as the PDF truth.

Git and GitHub:

```text
git status --short --branch
git diff --check
git remote -v
gh auth status
gh pr checks
```

Use `safe-git-ops` for commits, pushes, branch operations, worktrees, merges, rebases, tags, and sandbox-sensitive failures. Use `gh` only for collaborator-facing issues, PRs, releases, and GitHub Project fields that should be visible outside private research memory.

Remote execution:

```text
ssh <host> ...
squeue / sacct / runai list / runai logs
```

Use `remote-project-control` before sync, submission, monitoring, or artifact inspection when a project spans local, Git remote, and SSH/HPC/RunAI state.

Release and artifact gates:

```text
pytest / smoke tests
license / README / CITATION checks
secret and large-file audit
artifact install or reproduction smoke test
```

Route detailed release work to `release-code` and artifact packaging to `artifact-evaluation-prep`.

## Memory Location

Record stable defaults in `memory/project.yaml` under `toolchain_gates`.

Record component-specific overrides in:

- code repo: `code/AGENTS.md`, `code/CLAUDE.md`, `code/docs/ops/current-status.md`, or code worktree `.agent/worktree-status.md`
- paper repo: `paper/AGENTS.md`, `paper/CLAUDE.md`, `memory/source-visibility-board.md`, or paper worktree `.agent/worktree-status.md`
- root project: `memory/decision-log.md` for durable policy changes and `memory/action-board.md` for failed or missing gates

## Gate Status

When reporting a gate, include:

- command
- scope
- status: `passed`, `failed`, `skipped`, `blocked`, or `needs-verification`
- whether it mutated files
- evidence source, such as command output, Overleaf log, CI check, PR check, or remote scheduler state
- next action for failures

Do not store full command transcripts in memory. Store concise status, paths, and pointers.

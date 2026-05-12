# {{PROJECT_NAME}} Current Status

> Working memory for cross-session server execution control. Re-verify volatile facts before acting.

Terminology: local = local development machine; Git remote = GitHub/GitLab remote such as `origin`; server = SSH/HPC/RunAI execution environment.

## Stable Pointers

- Default server: `{{DEFAULT_SERVER_NAME}}`
- Git remote: `origin`
- Default branch: `{{DEFAULT_BRANCH}}`
- Local repo root: `{{LOCAL_REPO_ROOT}}`
- GitHub/GitLab CLI auth: unknown until checked
- GitHub/GitLab API network access: unknown until checked
- General network-sensitive commands: `gh`, `git fetch/push/ls-remote`, `ssh`, `curl`, package managers, and scheduler/API CLIs may require network permission in sandboxed agent runtimes
- SSH wrapper policy: use `remote-cmd <ssh-alias> <remote-repo-root> -- <command> [args...]` for simple server commands; use `remote-bash <ssh-alias> <remote-repo-root> scripts/ops/<wrapper>.sh` for loops, `$variables`, command substitution, pipes, globs, `find`, `awk`, or multi-line logic
- Python environment policy: reuse the configured project or stage env by default; do not create a job-specific uv env unless dependencies changed, isolation is required, or a real concurrent sync/race risk exists

## Current Focus

- Summary: Fill in the main task for the current phase.
- Active branch: `{{DEFAULT_BRANCH}}`
- Current experiment or issue: Fill in the current experiment, bug, or refactor target.

## Latest Known Server State

- Server: `{{DEFAULT_SERVER_NAME}}`
- Server repo root: `{{DEFAULT_REMOTE_REPO_ROOT}}`
- Last verified: `{{DATE}}`
- Last known commit: Fill in after a real check.
- Latest known job: Fill in the most relevant recent job name or id.
- Important logs: Fill in paths worth checking next.

## Open Issues

- Record blockers, mismatches, or things the next session should re-check.
- Re-check `gh auth status` with network access before using GitHub API commands such as repo creation, repo view, or fork.
- If `gh` reports `api.github.com` connection failure, treat it as network/sandbox access until rechecked with network permission.
- If `git`, `ssh`, `curl`, package managers, or scheduler/API CLIs report DNS, timeout, or connection failures, recheck with network permission before diagnosing credentials, Git remotes, SSH keys, or server configuration.
- Do not compose complex SSH double-quoted one-liners. If a command would contain shell control flow or remote variables, create or reuse a project wrapper under `scripts/ops/` and call it with `remote-bash`.

## Next Step

- State one concrete next action for the next session.

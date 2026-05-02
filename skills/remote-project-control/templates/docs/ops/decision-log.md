# {{PROJECT_NAME}} Decision Log

Use this file for durable workflow decisions, not ephemeral runtime status.

## {{DATE}} - Initial Server Workflow Setup

- Default server: `{{DEFAULT_SERVER_NAME}}`
- Server repo root: `{{DEFAULT_REMOTE_REPO_ROOT}}`
- Why this exists: Capture why this server, scheduler, and workflow are the project defaults.
- Revisit when: Record the trigger that would make this decision stale.

## Terminology Convention

- `local`: local development machine.
- `Git remote`: GitHub/GitLab remote such as `origin`.
- `server`: SSH/HPC/RunAI execution environment.

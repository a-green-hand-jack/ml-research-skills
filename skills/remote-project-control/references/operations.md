# Operations Reference

Use this reference after the project memory has been loaded and summarized.

## Inspect

Goal: understand the current local and remote situation without changing code or scheduler state.

Check:

- local git root, branch, short commit, dirty state
- chosen server's remote repo root, branch, short commit, dirty state
- presence of the configured data, checkpoint, scratch, and logs roots
- scheduler type and whether the expected command exists

Report mismatches clearly:

- local and remote branches differ
- local commit is ahead of remote
- remote repo is dirty
- configured path does not exist
- scheduler or environment activation command looks stale

## Sync Code

Goal: safely align local code and the remote repo through git.

Default flow:

1. Inspect local git state
2. If local work is uncommitted, ask whether to commit first
3. Push local commits through the configured git remote
4. On the remote repo, fetch and pull with a non-destructive fast-forward strategy

Preferred remote update pattern:

```bash
ssh <ssh-alias> "cd <remote-repo-root> && git fetch --all --prune && git pull --ff-only <remote-name> <branch>"
```

Stop and ask the user instead of forcing through if:

- the remote repo is dirty
- the remote branch differs unexpectedly
- the pull is not fast-forward
- the user seems to want a branch switch or rewrite

Do not use `git reset --hard` on the remote repo unless the user explicitly asks.

## Run Job

Goal: submit reproducible work on the remote server.

Workflow:

1. Verify the remote repo and scheduler state
2. Ensure the remote repo is at the intended branch or commit
3. Reuse an existing job script if one already fits
4. If a new job script is needed, invoke `run-experiment` after the remote context is known
5. Submit from the remote repo root with the configured environment activation

When wrapping a command, prefer this structure:

```bash
ssh <ssh-alias> "cd <remote-repo-root> && <env-activation> && <submit-command>"
```

If the project policy says remote runs require git sync first, enforce that order.

## Interactive Session

Goal: prepare a correct interactive remote workflow.

Typical patterns:

- `salloc` to obtain resources
- `srun --pty bash` to enter an interactive compute shell
- direct remote shell only for lightweight inspection, not heavy training

Keep the environment and repo root explicit in the command sequence. Do not assume the remote shell starts in the right directory or activates the right environment.

## Monitor

Goal: inspect the state of running or recent jobs and follow logs.

For SLURM-like setups, common commands are:

- `squeue -u $USER`
- `sacct -j <jobid> --format=JobID,State,Elapsed,AllocGRES`
- `tail -f <logs-root>/<job-name>/slurm-<jobid>.out`

For RunAI-like setups, common commands are:

- `runai list`
- `runai logs <job-name> -f`

Use the configured `logs_root` when available instead of inventing paths.

## Artifacts

Goal: find checkpoints, result files, or logs associated with the project.

Preferred order:

1. Search the configured `checkpoint_root` or project output directory
2. Search the configured `logs_root`
3. Search the remote repo tree only if the previous locations do not apply

Default to listing or inspecting artifacts first. Do not copy large files unless the user clearly asks for transfer.

## Closeout

Goal: leave useful context for the next session.

Update `docs/ops/current-status.md` with:

- the branch or commit to resume from
- what changed in this session
- latest known job and where to monitor it
- blockers or follow-up questions
- the next concrete action

If the session established a stable policy or convention, append a short entry to `docs/ops/decision-log.md`.

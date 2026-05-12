# Operations Reference

Use this reference after the project memory has been loaded and summarized.

## Inspect

Goal: understand the current local, Git remote, and server situation without changing code or scheduler state.

Check:

- local git root, branch, short commit, dirty state
- chosen server's repo root, branch, short commit, dirty state
- presence of the configured data, checkpoint, scratch, and logs roots
- scheduler type and whether the expected command exists

Report mismatches clearly:

- local and server branches differ
- local commit is ahead of the server repo
- server repo is dirty
- configured path does not exist
- scheduler or environment activation command looks stale

Network preflight rule:

- For commands that contact GitHub/GitLab, SSH servers, package registries, or scheduler APIs, DNS failure, timeout, or connection failure is `network/sandbox access` until rerun with network permission.
- Do not classify network-restricted `git`, `gh`, `ssh`, `curl`, or API commands as bad credentials, missing repos, bad SSH keys, or broken server configuration before a network-enabled rerun.

## Sync Code

Goal: safely align local code, the Git remote, and the server repo through git.

Default flow:

1. Inspect local git state
2. If local work is uncommitted, ask whether to commit first
3. Push local commits through the configured Git remote
4. On the server repo, fetch and pull from the Git remote with a non-destructive fast-forward strategy

Preferred server update pattern:

```bash
ssh <ssh-alias> "cd <remote-repo-root> && git fetch --all --prune && git pull --ff-only <remote-name> <branch>"
```

If user-level wrappers are available, prefer the argv-safe equivalent:

```bash
remote-cmd <ssh-alias> <remote-repo-root> -- git fetch --all --prune
remote-cmd <ssh-alias> <remote-repo-root> -- git pull --ff-only <remote-name> <branch>
```

Stop and ask the user instead of forcing through if:

- the server repo is dirty
- the server branch differs unexpectedly
- the pull is not fast-forward
- the user seems to want a branch switch or rewrite

Do not use `git reset --hard` on the server repo unless the user explicitly asks.

## Git Remote Setup

Goal: create or repair the GitHub/GitLab side of the workflow without confusing Git hosting, local repos, and execution servers.

Preflight:

1. Inspect each repo independently:

```bash
git -C <repo> remote -v
git -C <repo> branch --show-current
git -C <repo> status --short
```

2. If the project uses a control root with component repos, check the root repo and component repos separately:

```bash
git -C <project-root> remote -v
git -C <project-root>/code remote -v
git -C <project-root>/paper remote -v
```

3. Before using `gh repo view`, `gh repo create`, `gh repo fork`, `gh project ...`, or any other GitHub API command, run:

```bash
gh auth status
```

If `gh auth status` fails with a network/API reachability message such as `error connecting to api.github.com`, `check your internet connection`, DNS failure, timeout, or TLS connection failure:

- classify the first problem as `GitHub API network/sandbox access`
- rerun `gh auth status` with network permission before asking the user to log in again
- do not conclude the token is invalid from a network-restricted run

If `gh auth status` has network access and still fails:

- classify the problem as `GitHub CLI authentication`, not a Git repo or server problem
- tell the user to run `gh auth login -h github.com`
- do not continue to `gh repo create`, `gh repo fork`, or `git push`

If `gh auth login` succeeds but the next `gh repo ...` command fails with `api.github.com` reachability, classify that as `GitHub API network/sandbox access`, not as a failed login. Rerun the repo command with network permission.

The same pattern applies to `git fetch`, `git push`, `git pull`, `git ls-remote`, and `ssh`: if the first failure is DNS, timeout, host unreachable, or API reachability, rerun with network permission before diagnosing Git credentials, SSH keys, repository existence, or server state.

Repository setup rules:

- A project control root and `code/` component repo often need separate GitHub repositories.
- A GitHub Project can coordinate several repos, but it is not itself a Git repo and should not collapse root/code/paper/slides repository boundaries.
- `gh project ...` requires the `project` token scope. If missing, use `gh auth refresh -s project` before creating, viewing, linking, or editing the project board.
- A cloned upstream repo may have `origin` pointing to an upstream project where the user has no write permission.
- For an upstream-based code repo, prefer adding a writable fork remote or changing `origin` only after the user confirms the desired policy.
- Do not create a GitHub repo for a nested component unless it is clear which local repo it should own.

Report separately:

- root repo Git remote and GitHub repo status
- code repo Git remote and GitHub repo status
- whether `gh` is authenticated
- whether `gh` has the `project` scope when GitHub Projects are involved
- whether the latest `gh` checks had network permission
- whether normal `git` SSH push is expected to work

## Run Job

Goal: submit reproducible work on the server.

Workflow:

1. Verify the server repo and scheduler state
2. Ensure the server repo is at the intended branch or commit
3. Classify the task as smoke, debug, or formal, then match the allocation to the task's real compute requirements
4. Inspect current resource availability, queue/pending state, or scheduler events when practical before choosing a partition, node-pool, GPU class, or interactive allocation
5. Reuse an existing job script if one already fits
6. If a new job script is needed, invoke `run-experiment` after the remote context is known
7. Submit from the server repo root with the configured environment activation

Resource-aware rule:

- Experiment momentum is usually more important than waiting for an ideal but unnecessary resource. For smoke/debug jobs, prefer the fastest-starting compatible allocation that validates the codepath.
- Formal jobs must preserve the intended experimental contract. If queue pressure suggests changing GPU class, memory, precision, batch size, seed plan, or distributed shape, surface the tradeoff and record the rationale instead of silently downgrading.
- When a job is pending, inspect scheduler events to distinguish resource-pool capacity, quota/fair-share, CPU/memory request, image/env startup, and code failures before launching duplicates.
- Do not store volatile queue snapshots as durable facts; record only the decision rationale and the monitor command or artifact.

Environment reuse rule:

- Treat virtualenv/uv environment creation as an operational cost, not a harmless default.
- Reuse the configured project or stage environment when dependencies are unchanged.
- Do not generate a new `UV_PROJECT_ENVIRONMENT` from each job name or smoke target.
- Create a job-specific env only for dependency changes, incompatible stacks, destructive package tests, or real concurrent sync/race risk.
- If the server repo has many env directories or slow uv startup, inspect the existing environment policy before submitting more jobs.

When wrapping a command, prefer this structure:

```bash
ssh <ssh-alias> "cd <remote-repo-root> && <env-activation> && <submit-command>"
```

When the command contains loops, `$variables`, command substitution, pipes, globs, `find`, `awk`, or more than one short shell clause, do not expand the one-liner. Create or reuse a project wrapper under `scripts/ops/` and run:

```bash
remote-bash <ssh-alias> <remote-repo-root> scripts/ops/<job-or-status-wrapper>.sh
```

If the project policy says server runs require git sync first, enforce that order.

## Interactive Session

Goal: prepare a correct interactive server workflow.

Typical patterns:

- `salloc` to obtain resources
- `srun --pty bash` to enter an interactive compute shell
- direct server shell only for lightweight inspection, not heavy training

Keep the environment and repo root explicit in the command sequence. Do not assume the server shell starts in the right directory or activates the right environment.

## Monitor

Goal: inspect the state of running or recent jobs and follow logs.

Before composing ad hoc SSH status commands, check whether `run-status-monitor` or a project wrapper can answer the question with a short artifact. Prefer:

```bash
remote-bash <ssh-alias> <remote-repo-root> scripts/ops/status_run.sh
```

over fragile long SSH one-liners.

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
3. Search the server repo tree only if the previous locations do not apply

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

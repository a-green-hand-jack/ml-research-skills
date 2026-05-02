# Git Failure Modes

Use this reference to avoid telling the user the wrong thing after a Git command fails.

## 1. Real Content Conflict

Typical signals:

- `CONFLICT (content):`
- `CONFLICT (modify/delete):`
- `Automatic merge failed`
- Git tells you to resolve files and continue
- files contain conflict markers like `<<<<<<<`

Interpretation:

- Git successfully started the write operation
- the failure is about incompatible content changes

What to tell the user:

- which files conflicted
- whether Git is in cherry-pick, merge, or rebase state
- what the next action is: resolve, add, continue, abort

## 2. Sandbox or Permission Restriction

Typical signals:

- `operation not permitted`
- `permission denied`
- cannot create `index.lock`
- cannot update `ORIG_HEAD`, `CHERRY_PICK_HEAD`, or refs
- cannot write under `.git/worktrees/...`
- cannot write under the common git dir

Interpretation:

- the problem is environmental
- Git may not have reached the content-merge phase at all

What to tell the user:

- this is not evidence of a code conflict
- the command likely needs permission escalation
- if known, name the blocked path or class of path

## 3. Repository State Problem

Typical signals:

- working tree not clean
- local changes would be overwritten
- commit or branch does not exist
- detached HEAD when the user expected a branch
- rebase or cherry-pick already in progress
- branch is checked out in another worktree

Interpretation:

- the repo needs cleanup or a user decision before the command can proceed

What to tell the user:

- the exact blocking state
- the safe options, such as commit, stash, abort, continue, or switch branches

## 4. User-Requested Destructive Action

Typical signals:

- the requested command itself is destructive

Interpretation:

- this is not an error condition, but it requires a confirmation boundary

What to do:

- explain the risk plainly
- ask for explicit approval before executing

## 5. Network or Sandbox Network Restriction

Typical signals:

- `Could not resolve host`
- `Could not read from remote repository`
- `Connection timed out`
- `Network is unreachable`
- DNS failure, TLS connection failure, or API reachability failure
- `ssh: Could not resolve hostname`
- `gh` reports `error connecting to api.github.com`

Interpretation:

- the command may not have reached the Git remote, GitHub/GitLab API, or SSH server
- this is not yet evidence of a bad token, bad SSH key, missing repository, branch mismatch, or GitHub/server outage
- sandboxed agent runtimes may require network permission even when the same command works in the user's normal terminal

What to tell the user:

- classify the first failure as network/sandbox access
- rerun with network permission if the command is required
- only diagnose authentication, missing repo, or server-side failures after a network-enabled rerun reaches the host

## Reporting Rule

Do not collapse these categories into a generic phrase like "Git conflict", "merge issue", "auth failed", or "remote is broken." Say which category it is.

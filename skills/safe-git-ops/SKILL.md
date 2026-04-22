---
name: safe-git-ops
description: Perform common Git operations safely with sandbox-aware failure handling. Use whenever the user wants to inspect or modify git state, especially for cherry-pick, merge, rebase, commit, branch, stash, or worktree workflows. Always use this skill when git errors might be confused with code conflicts, when the repo uses worktrees, or when a sandboxed agent needs to decide whether to request permission escalation.
allowed-tools: Read, Write, Edit, Bash, Glob
---

# Safe Git Ops

Help the user perform common Git operations without confusing sandbox failures, repository state issues, and real content conflicts.

## Skill Directory Layout

```text
<installed-skill-dir>/
├── SKILL.md
└── references/
    ├── failure-modes.md
    └── worktrees.md
```

## Progressive Loading

- Always read `references/failure-modes.md`
- Read `references/worktrees.md` when the repo uses `git worktree`, when `.git` points to another directory, or when the user mentions multiple worktrees

## Core Behavior

- Separate preflight inspection from state-changing Git commands
- Distinguish sandbox or permission failures from merge conflicts
- Treat worktrees as a special case because they may write shared Git metadata outside the visible working directory
- Ask before destructive operations such as `reset --hard`, `checkout --`, deleting branches, or dropping stashes
- Prefer non-interactive Git commands
- When a write operation is blocked by the sandbox, explain that clearly and request escalation instead of guessing about conflicts

## Step 1 — Orient the Repository

Before any meaningful Git action, inspect the repository shape:

```bash
git rev-parse --show-toplevel
git rev-parse --git-dir
git branch --show-current
git status --short
```

If the user mentions worktrees or `.git` is a file rather than a directory, also inspect:

```bash
git worktree list
git rev-parse --git-common-dir
```

Summarize:

- repo root
- current branch
- whether the tree is dirty
- whether this is a worktree
- whether shared Git metadata lives outside the current directory

## Step 2 — Classify the Requested Operation

Handle the request as one of these categories:

- `inspect`: status, log, diff, branch list, remotes, worktree layout
- `safe_write`: add, commit, cherry-pick, merge, rebase, stash, branch creation, worktree creation
- `destructive_write`: reset, checkout over local changes, clean, branch deletion, stash drop, force push

For `inspect`, run the command directly if sandbox rules allow it.

For `safe_write`, do a preflight check first.

For `destructive_write`, require explicit user confirmation before executing.

## Step 3 — Preflight Before Any State-Changing Git Command

Before `safe_write` or `destructive_write`, gather enough context to avoid sloppy failure handling:

```bash
git status --short
git branch --show-current
git rev-parse --short HEAD
```

For `cherry-pick`, `merge`, or `rebase`, also inspect the target commit or branch first:

```bash
git log --oneline --decorate -n 5
git show --stat --summary <target>
```

For worktrees, inspect the shared metadata location:

```bash
git rev-parse --git-common-dir
```

If the command will likely write to shared Git metadata outside the sandboxed writable root, tell the user this before running it and be ready to request escalation.

## Step 4 — Execute and Interpret Failures Correctly

When a Git write fails, classify the failure before telling the user what happened.

Use the guidance in `references/failure-modes.md`. The high-level rule is:

- If Git reports `CONFLICT`, conflict markers, or asks to resolve files, this is a code conflict
- If Git reports `operation not permitted`, `permission denied`, failure to create lock files, or inability to update refs or worktree metadata, this is a sandbox or permission problem
- If Git reports dirty state, untracked-file overwrite, detached HEAD mismatch, or missing commit, this is a repository state problem

Do not tell the user "there is a conflict" unless Git actually reported one.

## Step 5 — Escalate Cleanly When Sandbox Restrictions Are the Real Problem

If a write command is important and fails because of sandbox restrictions:

1. State that the failure is environmental, not a code conflict
2. Name the blocked operation
3. Mention the likely write target if known, such as:
   - `.git/index.lock`
   - `.git/worktrees/...`
   - shared refs under the common git dir
4. Request permission escalation and rerun the same command

Use wording like:

> This `git cherry-pick` failure looks like a sandbox write restriction, not a merge conflict. Git needs to update shared worktree metadata, so I should rerun it with elevated permissions.

## Step 6 — Worktree-Specific Rules

When the repo uses worktrees:

- Assume `commit`, `cherry-pick`, `merge`, `rebase`, and similar commands may write outside the current worktree directory
- Check `git worktree list` and `git rev-parse --git-common-dir` early
- Avoid claiming that a failure is "local to this worktree" until you confirm where Git is trying to write
- Be extra careful with branch deletion or reset because another worktree may be using the same branch

Read `references/worktrees.md` for the detailed handling rules.

## Step 7 — Report Outcomes Precisely

When you finish, report one of these outcomes clearly:

- success
- conflict requiring manual resolution
- sandbox or permission restriction
- repository state problem that needs a user choice

For each case, give the user the next action, not a vague Git dump.

Good example:

> `git cherry-pick <commit>` did not reach merge resolution. Git was blocked from writing shared worktree metadata under the common git dir, so this is a sandbox issue. The next step is to rerun the same command with elevated permissions.

Bad example:

> cherry-pick failed, probably a conflict

## Commands This Skill Should Handle Well

- `git status`, `log`, `diff`, `show`, `branch`, `remote`
- `git add`, `commit`, `stash`
- `git cherry-pick`
- `git merge`
- `git rebase`
- `git switch`, `checkout`, `checkout -b`
- `git worktree list`, `git worktree add`

## Commands Requiring Extra Caution

- `git reset --hard`
- `git checkout -- <path>`
- `git clean -fd`
- `git branch -D`
- `git stash drop` or `clear`
- `git push --force`

Do not run these without explicit user approval.

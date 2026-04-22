# Git Worktrees

Git worktrees deserve special handling because the visible working directory is not the full write surface.

## Why Agents Misdiagnose Worktree Failures

In a worktree, Git metadata may be shared across directories:

- the current worktree has its own working files
- the common git dir may live elsewhere
- Git writes may touch `.git/worktrees/...`, refs, lock files, and shared state

As a result, a sandbox that allows writes in the worktree directory may still block Git from updating shared metadata.

## Commands Commonly Affected

- `git commit`
- `git cherry-pick`
- `git merge`
- `git rebase`
- `git branch -d` or `-D`
- `git worktree add`

These commands should trigger an early check of:

```bash
git rev-parse --git-dir
git rev-parse --git-common-dir
git worktree list
```

## Special State Problems in Worktrees

Watch for:

- the target branch is already checked out in another worktree
- the shared Git metadata is outside the current writable root
- another operation is already in progress in the current worktree

Do not describe these as merge conflicts.

## Good Worktree Reporting

Good:

> This repo is using a linked worktree. `git cherry-pick` needs to update shared metadata under the common git dir, and the sandbox blocked that write. This is a permission issue, not a code conflict.

Bad:

> cherry-pick hit a conflict in the worktree

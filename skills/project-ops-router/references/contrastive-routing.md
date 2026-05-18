# Contrastive Routing Rules — Project Ops

---

## `safe-git-ops` vs `remote-project-control`

**Use `safe-git-ops`** when the task is about the local Git repository:
- commit, push, merge, rebase, stash, cherry-pick
- resolving conflicts, diagnosing lock files, worktree state
- choosing between commit paths (fast/validation/reinstall)

**Use `remote-project-control`** when the task requires coordinating with an SSH/HPC/RunAI server:
- checking server state, syncing code to a remote machine
- submitting or monitoring jobs on a server (when `run-status-monitor` is not the right fit)
- recovering project memory from a server, SSH wrapper usage, remote shell commands

**Decision rule**: Is the primary blocker a Git state problem (use `safe-git-ops`) or a remote server coordination problem (use `remote-project-control`)?

---

## `new-workspace` vs `project-init`

**Use `new-workspace`** when the project already exists and you need to create a new branch or worktree within it:
- experiment branch, baseline branch, paper venue branch, arXiv release
- code worktrees under `<ProjectName>/code-worktrees/`
- paper version worktrees under `<ProjectName>/paper-worktrees/`

**Use `project-init`** when initializing a brand new research project from scratch:
- creating the root project structure with paper/, code/, slides/ repos
- setting up GitHub Project board linkage, root AGENTS.md, toolchain gates
- first-time project memory setup

**Decision rule**: Does the project already exist? Yes → `new-workspace`. No → `project-init`.

---

## `research-project-memory` vs `personalization-memory`

**Use `research-project-memory`** for project-level state that all agents on this project need to share:
- claims, evidence, risks, actions, worktree status, phase dashboard
- conventions that apply to this specific research project

**Use `personalization-memory`** for user-level preferences that apply across projects:
- reusable style preferences, repeated corrections, workflow patterns
- preferences that should persist beyond this project

**Decision rule**: Is the information specific to this research project (project memory) or portable to all future projects (personalization)?

---

## `sidecar-task-runner` vs `code-reviewer`

**Use `sidecar-task-runner`** for bounded one-shot delegated tasks:
- pre-commit classification, draft proposals, mechanical scans
- any task where you want to run an ephemeral Codex without sharing main context

**Use `code-reviewer`** specifically for code review with writer/reviewer separation:
- auditing a core algorithm implementation from a fresh context
- creating `.agent/code-reviews/` bundles for independent review

**Decision rule**: Is the task a code review requiring writer/reviewer independence (use `code-reviewer`) or a general bounded delegation task (use `sidecar-task-runner`)?

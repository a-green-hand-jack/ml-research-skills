---
name: project-ops-router
description: Route project operations tasks — git, memory, remote, workspace, code review, timeline, ops — to the correct skill. Use when the task involves commits, pushes, worktrees, project memory, SSH/server coordination, sidecar runners, or audits. Do not solve the ops task directly.
allowed-tools: Read, Bash
---

# Project Ops Router

You are a **router**. Do not perform the operation directly.

Your job: classify the task → select one child skill → hand off.

## Before Routing — Mandatory

1. Detect scope: `git rev-parse --git-common-dir` vs `--show-toplevel`.
2. If `memory/BRIEFING.md` exists, read it for current phase and active worktrees.

## Classification Buckets

| Bucket | Key signals | Route to |
|---|---|---|
| **git-ops** | commit, push, merge, rebase, stash, conflict, lock file, worktree state, Git failure | `safe-git-ops` |
| **new-branch/worktree** | create branch, new worktree, experiment branch, paper venue branch, arXiv branch | `new-workspace` |
| **project-memory** | claim board, evidence, risk, action, handoff, phase dashboard, memory bootstrap, closeout | `research-project-memory` |
| **project-init** | initialize project, create paper/code/slides repos, GitHub Project, root AGENTS.md | `project-init` |
| **remote-server** | SSH, server state, sync safety, SLURM/RunAI coordination, remote logs, artifacts, HPC | `remote-project-control` |
| **code-review** | review implementation, fresh-context audit, writer/reviewer separation, review bundle | `code-reviewer` |
| **sidecar** | one-shot Codex task, bounded scan, precommit classifier, draft proposal, ephemeral run | `sidecar-task-runner` |
| **sync-paper** | promote experiment results to paper memory, sync evidence, project-sync | `project-sync` |
| **timeline** | retrospective, progress summary, git history timeline, mentor report, phase planning | `work-timeline-planner` |
| **token-audit** | token usage, Codex burn, cache reuse, session cost, attention telemetry | `token-usage-auditor` |
| **skill-audit** | skill inventory, routing quality, stale references, validation readiness, skill system | `skill-system-auditor` |
| **personalization** | user preferences, repeated corrections, private memory, reusable rules from trajectory | `personalization-memory` |
| **memory-publish** | audit private memory/skills before publishing, redaction, privacy risk | `memory-publication-auditor` |

## Routing Steps

1. Identify the single most blocking bucket.
2. If uncertain between `safe-git-ops` and `remote-project-control`, read `references/contrastive-routing.md`.
3. Select exactly one child skill.
4. Hand off — state which skill and why.

## Hard Constraints

- Do not run git commands yourself before handing off to `safe-git-ops`.
- Do not connect to servers yourself before handing off to `remote-project-control`.
- Do not write to memory boards yourself; route to `research-project-memory`.
- If a task spans ops and experiment/paper domains, ops work (commit/push/sync) goes to this router first; scientific work goes to the appropriate domain router after.

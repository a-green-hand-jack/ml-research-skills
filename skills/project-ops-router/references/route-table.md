# Project Ops Route Table

| Task type | Concrete signals | Correct skill | Avoid |
|---|---|---|---|
| Commit / push / merge | "commit my changes", "push to main", "merge conflict", "rebase", "cherry-pick", "index.lock", "CONFLICT" | `safe-git-ops` | `remote-project-control` (that's for server coordination) |
| New branch or worktree | "create experiment branch", "new worktree for paper", "arXiv release", "NeurIPS branch" | `new-workspace` | `project-init` (that creates a whole new project) |
| Project memory | "update claims", "log this result", "risk board", "action board", "phase dashboard", "memory closeout", "session bootstrap" | `research-project-memory` | `personalization-memory` (that's user-level, not project-level) |
| Initialize new project | "start a new research project", "create paper/ and code/ repos", "set up GitHub Project board" | `project-init` | `new-workspace` (that works within an existing project) |
| Server / HPC / RunAI coordination | "sync code to server", "check server state", "SSH command", "remote logs", "RunAI project recovery" | `remote-project-control` | `safe-git-ops` (that's local Git, not server) |
| Code review | "review my implementation", "fresh-context audit", "review bundle", "writer/reviewer separation" | `code-reviewer` | `sidecar-task-runner` (that's general delegation, not code review) |
| One-shot Codex delegation | "run a quick Codex scan", "precommit classifier", "bounded draft", "ephemeral sidecar" | `sidecar-task-runner` | `code-reviewer` (that's specifically for code review) |
| Sync results to paper | "promote experiment results to paper memory", "project-sync", "graduate results from code to paper" | `project-sync` | `research-project-memory` (that's for broader project state) |
| Progress timeline | "retrospective", "git history timeline", "mentor report", "phase summary", "what did we do last month" | `work-timeline-planner` | `research-project-memory` (that maintains live state, not retrospective timelines) |
| Token / cost audit | "how many tokens did I use", "Codex burn rate", "session cost", "cache reuse" | `token-usage-auditor` | `skill-system-auditor` |
| Skill system audit | "skill inventory", "stale skill references", "routing quality", "validation readiness" | `skill-system-auditor` | `token-usage-auditor` |
| User preferences | "save my style preference", "remember my workflow", "scan for reusable rules from this session" | `personalization-memory` | `research-project-memory` |
| Pre-publish audit | "audit my private notes before sharing", "redact private skill", "privacy check" | `memory-publication-auditor` | `memory-publication-auditor` is the only skill for this |

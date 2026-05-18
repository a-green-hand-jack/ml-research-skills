# ML Research Root Route Table

Use this table when the domain classification bucket is not immediately obvious.

| Task type | Concrete signals | Correct route | Wrong choice to avoid |
|---|---|---|---|
| Experiment work | run, submit, debug, NaN, OOM, results, baselines, ablations, metrics, statistics, claim-audit, pivot | `experiment-evidence-router` | `paper-writing-router` (writing about experiments ≠ doing experiments) |
| Paper writing | draft, revise prose, write section, submission checklist, citation audit, LaTeX, consistency edit | `paper-writing-router` | `experiment-evidence-router` (writing about results ≠ diagnosing them) |
| Research discovery | new idea, literature survey, related work map, reference papers, corpus comparison | `discovery-router` | `experiment-evidence-router` (surveying literature ≠ running experiments) |
| Project operations | git, push, commit, worktree, memory boards, server, HPC, code review, timeline | `project-ops-router` | `remote-project-control` directly (ops-router selects the right ops skill) |
| Method design | design algorithm, formulate method, mechanism spec, ablation implications, implementation handoff | `algorithm-design-planner` | `experiment-design-planner` (method design is pre-experiment, not experiment hypothesis) |
| Inbound feedback | advisor gave feedback, lab meeting comments, collaborator review, process/triage inbound notes | `feedback-synthesizer` | `advisor-update-writer` (writing TO advisor ≠ processing feedback FROM advisor) |
| Outbound advisor update | write update, weekly memo, lab note, decision-oriented email to advisor | `advisor-update-writer` | `feedback-synthesizer` (processing feedback ≠ writing an update) |
| Real reviews | reviews arrived, OpenReview decision, respond to reviewer, plan rebuttal experiments | `rebuttal-strategist` | `paper-writing-router` → `paper-reviewer-simulator` (simulated ≠ real reviews) |
| Slide deck | presentation, progress talk, advisor slides, reading group slides | `research-slide-deck-builder` | `paper-writing-router` (slides ≠ paper writing) |
| Model card / datasheet | model card, dataset datasheet, HuggingFace documentation, reproducibility statement | `model-card-writer` | `release-code` (model card writing ≠ code release prep) |
| Public code release | GitHub release, LICENSE, CITATION.cff, public repo README, security audit | `release-code` | `model-card-writer` (code release ≠ model card writing) |
| Artifact evaluation | AE package, reviewer quickstart, smoke tests, claim-to-artifact map | `artifact-evaluation-prep` | `release-code` (artifact eval is a separate submission deliverable) |

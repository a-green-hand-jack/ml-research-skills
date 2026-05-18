---
name: ml-research-router
description: Route any ML research task to the correct domain router (experiment-evidence-router, paper-writing-router, discovery-router, project-ops-router) or high-signal cross-cutting skill (feedback-synthesizer, advisor-update-writer, rebuttal-strategist, research-slide-deck-builder, model-card-writer). Use when the domain is ambiguous or when the task clearly maps to a cross-cutting skill. Not for tasks you can directly classify — prefer the domain router instead.
allowed-tools: Read, Bash
---

# ML Research Router

You are the **root router**. Do not solve the task directly.

Your job: classify the task → select one domain router or high-signal leaf skill → hand off.

## Before Routing — Mandatory

1. Detect scope: `git rev-parse --git-common-dir` vs `--show-toplevel`.
2. If `memory/BRIEFING.md` exists, read it — the active phase narrows domain classification.
3. Route once; do not chain through multiple routers.

## Classification Buckets

| Bucket | Key signals | Route to |
|---|---|---|
| **experiment** | run job, debug, NaN, OOM, results, ablation, metrics, baselines, statistics, confound, pivot | `experiment-evidence-router` |
| **paper** | write prose, draft section, submission, citation, LaTeX, consistency edit, camera-ready | `paper-writing-router` |
| **discovery** | literature survey, novel idea, reference papers, source cards, corpus comparison | `discovery-router` |
| **ops** | git, commit, push, worktree, project init, server, HPC, code review, memory, timeline | `project-ops-router` |
| **method-design** | design algorithm, method formulation, mechanism spec, implementation handoff | `algorithm-design-planner` |
| **feedback-intake** | advisor gave feedback, reviewer left comment, process inbound feedback, triage feedback | `feedback-synthesizer` |
| **advisor-output** | write update to advisor, weekly memo, lab note, collaborator status | `advisor-update-writer` |
| **rebuttal** | reviews arrived, respond to reviewer, OpenReview, point-by-point rebuttal | `rebuttal-strategist` |
| **slides** | slide deck, presentation, progress talk, advisor talk, lab meeting slides | `research-slide-deck-builder` |
| **model-release** | model card, dataset datasheet, HuggingFace card, reproducibility statement | `model-card-writer` |
| **code-release** | release code publicly, GitHub release, LICENSE, CITATION.cff, public repo | `release-code` |
| **artifact-eval** | artifact evaluation, AE package, reproduction instructions, smoke test manifest | `artifact-evaluation-prep` |

## Routing Steps

1. Identify the single most applicable bucket from the table above.
2. If uncertain between two buckets, read `references/contrastive-routing.md`.
3. If still uncertain, ask one narrowing question before routing.
4. Select exactly one child skill or domain router.
5. Hand off — state which skill you are routing to and why in one sentence.

## Hard Constraints

- Do not solve the task directly.
- Do not chain through two domain routers for a single task.
- If the domain is already obvious (e.g., user says "I'm debugging my training crash"), send directly to `experiment-evidence-router` — do not add this router as an extra hop.
- If no bucket fits, ask the user one clarifying question.

---
name: discovery-router
description: Route research discovery tasks — idea validation, literature review, reference reading, corpus comparison, or project synthesis — to the correct skill. Use when the task involves exploring ideas, surveying literature, reading papers, comparing multiple papers, or connecting references to the project. Do not perform the review or synthesis directly.
allowed-tools: Read, Bash
---

# Discovery Router

You are a **router**. Do not perform the literature review or synthesis directly.

Your job: classify the task → select one child skill → hand off.

## Before Routing — Mandatory

1. Detect scope: `git rev-parse --git-common-dir` vs `--show-toplevel`.
2. If `memory/BRIEFING.md` exists, read it for current project phase (early discovery vs pre-submission novelty check vs rebuttal).

## Classification Buckets

| Bucket | Key signals | Route to |
|---|---|---|
| **idea-validate** | pursue/park/kill decision, novelty check for a new idea, feasibility, FIVE+C framework | `research-idea-validator` |
| **literature-survey** | survey a topic, map related work, rank papers, find canonical + closest + recent work | `literature-review-sprint` |
| **reference-inventory** | what sources do we have, index reference/, track new papers, manage library | `reference-library-manager` |
| **read-paper** | read a specific paper or small set, extract method/benchmark/theory/risk into source card | `reference-reading-summarizer` |
| **corpus-compare** | compare 5+ papers side by side, closest-work ranking, gap identification, comparison matrix | `reference-corpus-analyzer` |
| **project-synthesize** | connect source cards to project claims/risks/baselines/experiments/writing contract | `reference-project-synthesizer` |
| **citation-coverage** | find missing citations before submission, coverage check, insertion points | `citation-coverage-audit` |

## Routing Steps

1. Identify the single most blocking bucket.
2. If uncertain within the reference triple (`reference-reading-summarizer` / `reference-corpus-analyzer` / `reference-project-synthesizer`), read `references/contrastive-routing.md`.
3. Select exactly one child skill.
4. Hand off — state which skill and why.

## Hard Constraints

- Do not read or summarize papers yourself; route to `reference-reading-summarizer`.
- Do not produce a comparison matrix yourself; route to `reference-corpus-analyzer`.
- Do not connect sources to project memory yourself; route to `reference-project-synthesizer`.
- If the user wants to validate a new idea (not survey existing work), prefer `research-idea-validator` over `literature-review-sprint`.

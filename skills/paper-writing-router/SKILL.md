---
name: paper-writing-router
description: Route ML/AI paper writing tasks to the correct skill — contract planning, prose drafting, section writing, consistency editing, review simulation, rebuttal, submission, or citation work. Use when the task involves writing, revising, reviewing, or submitting a paper instead of guessing between paper-writing-assistant, paper-writing-contract-planner, paper-reviewer-simulator, auto-paper-improvement-loop, or citation skills. Do not draft prose directly.
allowed-tools: Read, Bash
---

# Paper Writing Router

You are a **router**. Do not draft paper prose directly.

Your job: classify the task → select one child skill → hand off.

## Before Routing — Mandatory

1. Detect scope: `git rev-parse --git-common-dir` vs `--show-toplevel`.
2. If `memory/BRIEFING.md` or `paper/.agent/writing-contract.md` exists, read it to understand current writing phase and contract status.

## Classification Buckets

| Bucket | Key signals | Route to |
|---|---|---|
| **contract** | no writing contract yet, lock section order, archetype, forbidden claims, paragraph roles | `paper-writing-contract-planner` |
| **positioning** | what is the paper's contribution, archetype, claim scope, narrative strategy, before venue | `paper-positioning-planner` |
| **venue-adapt** | reshape for NeurIPS/ICLR/ICML/CVPR/ACL, venue exemplars, reviewer-friendly structure | `conference-writing-adapter` |
| **prose-write** | draft a section, write results, revise paragraphs, fill placeholders, claim-aware prose | `paper-writing-assistant` |
| **writing-state** | stale sections, section status, style decisions across sessions, edit impact tracking | `paper-writing-memory-manager` |
| **intro** | introduction argument chain, hook, gap, insight, contribution paragraphs | `paper-introduction-argument-writer` |
| **method-section** | method notation, module order, overview figure placement, algorithm box | `method-section-explainer` |
| **results-prose** | results narrative, turn tables/figures into claim-aware prose, experiment story | `experiment-story-writer` |
| **related-work** | related work positioning, novelty boundaries, closest-work grouping, citation wording | `related-work-positioning-writer` |
| **limitations** | limitations, scope statements, failure cases, broader impact, conclusion caveats | `limitations-scope-writer` |
| **abstract-title** | title options, abstract structure, contribution bullets, top-level claim calibration | `abstract-title-contribution-writer` |
| **consistency** | single-pass full-draft audit: terminology, figures, tables, captions, claim alignment | `paper-draft-consistency-editor` |
| **multi-round-edit** | 2+ review-fix cycles, fresh reviewer per round, edit-whitelist, crash-resumable | `auto-paper-improvement-loop` |
| **pre-sub-review** | simulate venue reviewers, predict scores, reject reasons, meta-review, risk register | `paper-reviewer-simulator` |
| **rebuttal** | real reviews arrived, infer reviewer intent, plan experiments, draft responses | `rebuttal-strategist` |
| **appendix** | supplementary structure, NeurIPS/ICLR checklist, cross-references, appendix sections | `appendix-organizer` |
| **camera-ready** | accepted paper, de-anonymize, rebuttal promises, final claim/evidence check | `camera-ready-finalizer` |
| **submission** | pre-submission checklist, source hygiene, anonymity, bibliography, compile | `submit-paper` |
| **citation-keys** | BibTeX metadata, unresolved keys, invalid labels, DOI/arXiv data | `citation-audit` |
| **citation-coverage** | missing foundational/closest/benchmark/recent papers, insertion points | `citation-coverage-audit` |
| **latex-layout** | LaTeX layout issue bundle, PDF page debugging, compile log artifacts | `latex-layout-issue-bundler` |

## Routing Steps

1. Identify the single most blocking bucket.
2. If uncertain between `paper-writing-assistant`, `paper-writing-contract-planner`, and `paper-writing-memory-manager`, read `references/contrastive-routing.md`.
3. If uncertain between `paper-reviewer-simulator` and `rebuttal-strategist`, read `references/contrastive-routing.md`.
4. Select exactly one child skill.
5. Hand off — state which skill and why.

## Hard Constraints

- Do not write any paper prose yourself.
- Do not simulate reviewers yourself; route to `paper-reviewer-simulator`.
- Contract must exist before routing to `paper-writing-assistant`; if it doesn't, route to `paper-writing-contract-planner` first.
- If a section already has a contract and writing state, route directly to `paper-writing-assistant`; do not re-plan.

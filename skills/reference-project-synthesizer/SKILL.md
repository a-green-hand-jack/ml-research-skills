---
name: reference-project-synthesizer
description: Connect structured reference paper cards to the active ML project. Use when references should inform claims, risks, baselines, benchmarks, experiments, algorithm design, writing contracts, citations, or reviewer strategy.
argument-hint: "[project-root] [paper-card-or-paper-id] [--link-claims] [--benchmark] [--baseline] [--writing] [--risk]"
allowed-tools: Read, Write, Edit, Bash, Glob
---

# Reference Project Synthesizer

Convert paper cards into project decisions. This skill answers: **What does this reference mean for our project?**

Use after `reference-reading-summarizer` has produced a paper card. Do not repeatedly re-read the PDF unless the card is insufficient or low confidence.

## Skill Directory Layout

```text
<installed-skill-dir>/
├── SKILL.md
├── references/
│   └── project-link-routing.md
└── templates/
    └── project-use-note.md
```

## Core Contract

- Read project memory before linking a reference to claims, experiments, risks, or writing.
- Use paper cards as compressed inputs. Raw PDFs and raw reading trajectories stay out of project memory.
- Stronger reasoning is required when the reference changes a claim, baseline, benchmark, novelty boundary, or rebuttal strategy.
- Every project implication should link to a paper card, confidence level, and target memory object.
- Do not promote a cheap skim into a project decision without marking uncertainty or requesting deeper reading.

## Inputs

Prefer:

- `reference/cards/<paper-id>.md`
- `reference/.agent/reference-index.md`
- `reference/.agent/reading-status.md`
- `memory/current-status.md`
- `memory/claim-board.md`
- `memory/evidence-board.md`
- `memory/risk-board.md`
- `memory/action-board.md`
- `paper/.agent/writing-contract.md`
- `code/.agent/benchmark-plan.md` or equivalent, when present

## Model Routing

Read `references/project-link-routing.md`.

- Tier 2 normal main model: routine project-use notes, citation placement, writing-pattern routing.
- Tier 3 strong/deep model: closest-work risk, must-have baseline, benchmark protocol, core algorithm/theory impact, final positioning.
- Do not use cheap sidecar output as the final authority for project decisions.

## Workflow

1. Locate the project root and existing memory.
2. Read the relevant paper card and its confidence/provenance.
3. Identify requested synthesis mode:
   - claim support or challenge
   - baseline implication
   - benchmark/task/protocol implication
   - method/theory implication
   - writing pattern
   - citation placement
   - reviewer-risk or novelty boundary
4. Create or update `reference/project-use/<paper-id>.md` from `templates/project-use-note.md`.
5. Write only durable conclusions into project memory:
   - claim/evidence/risk/action/provenance boards
   - paper writing contract or style memory
   - code benchmark/baseline plan
6. If the card is too weak, route back to `reference-reading-summarizer` with the required reading mode.

## Output Rules

Each project-use note should include:

- one-line project relevance
- supported claims
- challenged claims
- baseline or benchmark implications
- algorithm/theory implications
- writing/citation implications
- risks and actions
- confidence and required follow-up

End with the closure audit:

```text
Goal: What project question did this reference help answer?
Answer: What did we learn?
Path: Which card, sections, and memory objects support this?
Correctness: Why should we trust it, and what needs deeper reading?
Next: What changes in the project?
```

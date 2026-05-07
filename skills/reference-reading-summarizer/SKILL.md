---
name: reference-reading-summarizer
description: Read and summarize project reference papers into structured paper cards. Use for skimming PDFs, extracting writing patterns, methods, theory, benchmarks, baselines, limitations, and citation support without yet deciding project implications.
argument-hint: "[project-root] [paper-id-or-pdf] [--mode skim|extract-writing|extract-method|extract-theory|extract-benchmark|extract-baseline|extract-risk|deep-read]"
allowed-tools: Read, Write, Edit, Bash, Glob, WebSearch, WebFetch
---

# Reference Reading Summarizer

Turn a reference paper into a structured, copyright-safe paper card. This skill answers: **What does this paper say?**

Do not force every paper into project decisions. Use `reference-project-synthesizer` after a card exists and the project implication matters.

## Skill Directory Layout

```text
<installed-skill-dir>/
├── SKILL.md
├── references/
│   ├── model-routing.md
│   └── reading-modes.md
└── templates/
    ├── paper-card.md
    └── reading-run.md
```

## Core Contract

- Read to the requested purpose, not exhaustively by default.
- Use cheaper models for skim and routine extraction; escalate for central method, theory, benchmark, closest-work, or final-paper claims.
- Preserve provenance: source PDF, pages/sections inspected, reading mode, model tier, confidence, and reviewer status.
- Do not paste long PDF text into cards. Summarize and point to pages/sections.
- Separate paper content from project implications.

## Reading Modes

- `skim`: relevance, role labels, whether deeper reading is needed
- `extract-writing`: intro framing, paragraph moves, contribution wording, captions, figure/table narration
- `extract-method`: algorithm, objective, architecture, inference, implementation details
- `extract-theory`: assumptions, theorem statements, proof ideas, formal definitions
- `extract-benchmark`: task, dataset, split, metric, protocol, compute, evaluation caveats
- `extract-baseline`: baseline method role, fairness conditions, comparison requirements
- `extract-risk`: closest-work threat, novelty boundary, reviewer attack surface
- `deep-read`: high-value paper where misunderstanding would change project direction

## Model Routing

Read `references/model-routing.md`.

Default:

- Tier 0 deterministic tools: PDF text extraction, metadata, page rendering when available
- Tier 1 cheap sidecar: `skim`, simple card skeleton, writing-pattern extraction
- Tier 2 normal main model: benchmark/protocol extraction, method extraction, citation support
- Tier 3 strong/deep model: core theory, closest work, must-have baseline, final paper claims

Escalate when the paper is closest work, a core algorithm source, a theory source, a benchmark source, or when the card will support a claim, experiment, baseline, or rebuttal.

## Workflow

1. Locate `reference/.agent/reference-index.md` if available.
2. Identify the paper path and requested reading mode.
3. Create a run artifact under `reference/.agent/runs/<run-id>/` when extraction is nontrivial:
   - `input-manifest.md`
   - `extraction-notes.md`
   - `model.json`
   - `decision.md`
4. Extract only the needed text/pages. Prefer local PDF tools; if unavailable, ask for text snippets or proceed from available metadata and mark limitations.
5. Fill `templates/paper-card.md` into `reference/cards/<paper-id>.md`.
6. Update `reference/.agent/reading-status.md` from `unread` or `skimmed` to `carded` when appropriate.
7. Route:
   - project implications needed -> `reference-project-synthesizer`
   - broad field map needed -> `literature-review-sprint`
   - citation coverage needed -> `citation-coverage-audit`

## Paper Card Rules

Every card should include:

- metadata
- reading mode
- role labels
- problem and contribution
- method/theory/benchmark/writing extraction only as relevant
- limitations and uncertainty
- reusable assets
- provenance and confidence

Do not turn cheap skim cards into strong conclusions. Mark `confidence: skim` or `needs-deep-read` when appropriate.

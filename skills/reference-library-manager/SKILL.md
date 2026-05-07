---
name: reference-library-manager
description: Manage a project reference PDF library under reference/. Use when scanning, ingesting, indexing, deduplicating, monitoring, or tracking reading status for project papers without deeply reading them.
argument-hint: "[project-root] [--scan] [--ingest] [--monitor] [--status]"
allowed-tools: Read, Write, Edit, Bash, Glob
---

# Reference Library Manager

Manage the project reference library as durable research infrastructure. This skill answers: **What references do we have, and what is their processing state?**

Do not use this skill for deep paper understanding or project implications. Use `reference-reading-summarizer` for "what does this paper say?" and `reference-project-synthesizer` for "what does this paper mean for our project?"

## Skill Directory Layout

```text
<installed-skill-dir>/
├── SKILL.md
├── scripts/
│   └── scan_reference_library.py
├── references/
│   └── library-policy.md
└── templates/
    ├── reference-index.md
    └── reading-status.md
```

## Core Contract

- Default project reference root is `<project-root>/reference/`.
- PDF files may be private, licensed, or large. Do not assume PDFs should be committed to a public repo.
- Commit derived indexes, cards, and project-use notes only when they are sanitized and useful.
- Prefer deterministic scanning for filenames, hashes, size, and modification time.
- Use cheap sidecars only for fuzzy title matching or metadata cleanup, not for raw PDF storage.

## Expected Project Layout

```text
reference/
├── papers/                  # PDFs and source documents, often ignored/private
├── cards/                   # stable paper cards from reference-reading-summarizer
├── project-use/             # project implications from reference-project-synthesizer
├── summaries/               # optional reading summaries
├── notes/                   # human notes
└── .agent/
    ├── reference-index.md
    ├── reading-status.md
    ├── metadata-gaps.md
    ├── duplicate-check.md
    └── runs/                # raw scan/read trajectories, usually ignored
```

## Model Routing

- Tier 0 script: scan files, hashes, size, mtime, missing cards, reading-status skeletons.
- Tier 1 cheap sidecar: fuzzy duplicate titles, filename-to-title cleanup, coarse role tags.
- Tier 2/3 models: not needed here; route to the reading or project synthesis skills.

## Workflow

1. Locate project root and `reference/`. If only `reference/` exists without `papers/`, scan PDFs recursively under `reference/`.
2. Read `references/library-policy.md`.
3. Run the scanner when indexing is needed:

```bash
python3 <installed-skill-dir>/scripts/scan_reference_library.py --project-root .
```

4. Review generated or updated files:
   - `reference/.agent/reference-index.md`
   - `reference/.agent/reading-status.md`
   - `reference/.agent/metadata-gaps.md`
   - `reference/.agent/duplicate-check.md`
5. Mark each paper's intended role when known:
   - `writing-exemplar`
   - `method-source`
   - `theory-source`
   - `benchmark-source`
   - `baseline`
   - `citation-support`
   - `closest-work`
   - `reviewer-risk`
6. Route next action:
   - unread but important -> `reference-reading-summarizer`
   - card exists and project decisions are needed -> `reference-project-synthesizer`
   - missing citation coverage in a draft -> `citation-coverage-audit`
   - broad field search -> `literature-review-sprint`

## Output Rules

- Store raw scanner trajectories under `reference/.agent/runs/` only when useful.
- Store durable index state under `reference/.agent/`.
- Store stable summaries as paper cards under `reference/cards/`.
- Never paste long PDF text into memory or public docs.
- Report only counts, major gaps, duplicates, and recommended next reads unless the user asks for detail.

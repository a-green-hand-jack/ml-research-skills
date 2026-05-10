---
name: reference-library-manager
description: Manage project reference sources under reference/. Use when scanning, ingesting, indexing, deduplicating, monitoring, or tracking processing status for papers, PDFs, Word docs, Markdown notes, BibTeX files, scripts, specs, or source bundles without deeply reading them.
argument-hint: "[project-root] [--scan] [--ingest] [--monitor] [--status]"
allowed-tools: Read, Write, Edit, Bash, Glob
---

# Reference Library Manager

Manage the project reference/source library as durable research infrastructure. This skill answers: **What sources do we have, and what is their processing state?**

Do not use this skill for deep source understanding or project implications. Use `reference-reading-summarizer` for "what does this source say?" and `reference-project-synthesizer` for "what does this source mean for our project?"

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
- A source can be a paper PDF, collaborator PDF/Word doc, Markdown note, BibTeX file, script, spec/config, notebook, webpage snapshot, or hand-built folder bundle.
- Raw source files may be private, licensed, large, or collaborator-provided. Do not assume they should be committed to a public repo.
- Commit derived indexes, source cards, and project-use notes only when they are sanitized and useful.
- Prefer deterministic scanning for filenames, hashes, size, and modification time.
- Use cheap sidecars only for fuzzy title matching or metadata cleanup, not for raw source storage.

## Expected Project Layout

```text
reference/
├── sources/                 # non-paper sources and bundles, often ignored/private
│   ├── collaborator-docs/
│   ├── markdown/
│   ├── bundles/
│   └── misc/
├── papers/                  # backward-compatible paper/PDF location
├── cards/                   # stable source cards from reference-reading-summarizer
├── project-use/             # project implications from reference-project-synthesizer
├── summaries/               # optional summaries
├── notes/                   # human notes
└── .agent/
    ├── source-index.md
    ├── reference-index.md   # compatibility alias
    ├── processing-status.md
    ├── reading-status.md    # compatibility alias
    ├── metadata-gaps.md
    ├── duplicate-check.md
    └── runs/                # raw scan/read trajectories, usually ignored
```

## Model Routing

- Tier 0 script: scan files/folders, hashes, size, mtime, missing cards, processing-status skeletons.
- Tier 1 cheap sidecar: fuzzy duplicate titles, filename-to-title cleanup, coarse source type and role tags.
- Tier 2/3 models: not needed here; route to the reading or project synthesis skills.

## Workflow

1. Locate project root and `reference/`. Prefer `reference/sources/` plus backward-compatible `reference/papers/`; if neither exists, scan supported source files recursively under `reference/`.
2. Read `references/library-policy.md`.
3. Run the scanner when indexing is needed:

```bash
python3 <installed-skill-dir>/scripts/scan_reference_library.py --project-root .
```

4. Review generated or updated files:
   - `reference/.agent/source-index.md`
   - `reference/.agent/reference-index.md`
   - `reference/.agent/processing-status.md`
   - `reference/.agent/reading-status.md`
   - `reference/.agent/metadata-gaps.md`
   - `reference/.agent/duplicate-check.md`
5. Mark each source's intended role when known:
   - `idea-seed`
   - `writing-exemplar`
   - `method-source`
   - `theory-source`
   - `benchmark-source`
   - `implementation-source`
   - `collaborator-feedback`
   - `project-spec`
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
- Store stable summaries as source cards under `reference/cards/`.
- Never paste long raw source text into memory or public docs.
- Report only counts, major gaps, duplicates, and recommended next sources unless the user asks for detail.

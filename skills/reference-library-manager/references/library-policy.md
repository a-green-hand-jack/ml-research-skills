# Reference Library Policy

## What Counts As A Source

A project source is any upstream object that can inform project direction, implementation, writing, evidence, or review risk:

- research paper PDF
- collaborator PDF, Word document, slide export, or feedback note
- Markdown, text, LaTeX, or spec document
- BibTeX collection
- script, notebook, config, or protocol snippet
- webpage snapshot or URL note
- manually constructed folder bundle containing documents, scripts, bib files, or data notes

## What Belongs Where

| Artifact | Default path | Commit policy |
|---|---|---|
| Paper/source file | `reference/papers/` or `reference/sources/` | Often private or ignored; do not assume public commit is OK |
| Folder bundle | `reference/sources/bundles/<bundle-id>/` | Often private or ignored; commit only when intentionally shared |
| Source index | `reference/.agent/source-index.md` | Can be committed if paths are project-relative and safe |
| Compatibility index | `reference/.agent/reference-index.md` | Same content as source index for old prompts/tools |
| Processing status | `reference/.agent/processing-status.md` | Can be committed |
| Raw extraction text | `reference/.agent/runs/<run-id>/` | Default local/ignored |
| Source card | `reference/cards/<source-id>.md` | Can be committed after copyright-safe summarization |
| Project-use note | `reference/project-use/<source-id>.md` | Can be committed |
| Memory writeback | `memory/` and component `.agent/` | Commit when it changes durable project state |

## Privacy And Copyright

- Do not copy long raw source text into public repo memory.
- Do not quote long passages from papers, books, reports, or collaborator documents.
- Prefer paraphrased summaries, structured cards, and source page/section/file pointers.
- If a source includes private collaborator feedback, reviewer comments, licensed material, private paths, or unpublished project ideas, keep raw artifacts local.
- A source card may be public only after it has been sanitized for copyright, attribution, and privacy.

## Processing State Labels

Use these states:

- `unread`: known file or bundle, not inspected
- `skimmed`: coarse relevance established
- `carded`: structured source card exists
- `project-linked`: project-use note exists
- `used`: linked to claim/evidence/risk/action, citation, experiment, implementation, or writing contract
- `deferred`: not useful now
- `superseded`: replaced by a newer or cleaner source

## Role Labels

- `idea-seed`: source that starts or reframes the project
- `writing-exemplar`: prose, framing, figure captions, intro/related-work/method style
- `method-source`: algorithm, architecture, objective, inference, implementation idea
- `theory-source`: assumptions, theorem, proof sketch, formalization
- `benchmark-source`: task, dataset, metric, protocol, split, evaluation setup
- `implementation-source`: script, notebook, config, or engineering pattern worth adapting
- `collaborator-feedback`: collaborator review, TODO, constraint, concern, or decision input
- `project-spec`: requirements, design note, task definition, or operating constraint
- `baseline`: method likely needed in experiments
- `citation-support`: supports a paper sentence or claim boundary
- `closest-work`: threatens novelty or positioning
- `reviewer-risk`: likely reviewer comparison or attack

## Identity And Duplicates

Use stable `source_id` values derived from metadata when possible:

```text
firstauthor-year-shorttitle
collaborator-topic-date
bundle-topic-date
```

If metadata is unknown, use a filename or folder slug and mark `metadata_status: missing`.

Detect duplicates by SHA-256 first. Folder bundles use a deterministic digest over contained file paths and hashes. Fuzzy title matching is advisory and should not delete files automatically.

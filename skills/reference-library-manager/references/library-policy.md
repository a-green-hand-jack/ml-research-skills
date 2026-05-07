# Reference Library Policy

## What Belongs Where

| Artifact | Default path | Commit policy |
|---|---|---|
| PDF/source file | `reference/papers/` or `reference/` | Often private or ignored; do not assume public commit is OK |
| file index | `reference/.agent/reference-index.md` | Can be committed if paths are project-relative and safe |
| reading status | `reference/.agent/reading-status.md` | Can be committed |
| raw extraction text | `reference/.agent/runs/<run-id>/` | Default local/ignored |
| paper card | `reference/cards/<paper-id>.md` | Can be committed after copyright-safe summarization |
| project-use note | `reference/project-use/<paper-id>.md` | Can be committed |
| memory writeback | `memory/` and component `.agent/` | Commit when it changes durable project state |

## PDF Privacy And Copyright

- Do not copy PDF text into public repo memory.
- Do not quote long passages from papers. Use short, necessary excerpts only when the user explicitly asks and keep within copyright limits.
- Prefer paraphrased summaries, structured cards, and source page pointers.
- If a PDF includes private reviewer comments, collaborator notes, or licensed material, keep raw artifacts local.

## Reading State Labels

Use these states:

- `unread`: known file, not inspected
- `skimmed`: coarse relevance established
- `carded`: structured card exists
- `project-linked`: project-use note exists
- `used`: linked to claim/evidence/risk/action, citation, experiment, or writing contract
- `deferred`: not useful now
- `superseded`: replaced by a newer or cleaner source

## Role Labels

- `writing-exemplar`: prose, framing, figure captions, intro/related-work/method style
- `method-source`: algorithm, architecture, objective, inference, implementation idea
- `theory-source`: assumptions, theorem, proof sketch, formalization
- `benchmark-source`: task, dataset, metric, protocol, split, evaluation setup
- `baseline`: method likely needed in experiments
- `citation-support`: supports a paper sentence or claim boundary
- `closest-work`: threatens novelty or positioning
- `reviewer-risk`: likely reviewer comparison or attack

## Identity And Duplicates

Use stable `paper_id` values derived from metadata when possible:

```text
firstauthor-year-shorttitle
```

If metadata is unknown, use a filename slug and mark `metadata_status: missing`.

Detect duplicates by SHA-256 first. Fuzzy title matching is advisory and should not delete files automatically.

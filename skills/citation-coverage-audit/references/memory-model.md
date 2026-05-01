# Memory Model

Store citation coverage knowledge project-locally so future scans do not restart from scratch.

## Default Location

```text
.agent/
└── citation-coverage/
    ├── README.md
    ├── project-coverage.md
    └── topics/
        └── <topic-slug>.md
```

## README.md

```markdown
# Citation Coverage Memory

Project-local notes about canonical, close, recent, and intentionally excluded citations for this paper. Search dates matter because recent and concurrent work changes over time.
```

## project-coverage.md

```markdown
# Project Citation Coverage

## Current Target
- Venue:
- Deadline:
- Topic:
- Last coverage audit:

## Must-Cite Added

## Should-Cite Candidates

## Intentionally Not Cited

## Novelty Claims To Watch

## Open Author Decisions
```

## topics/<topic-slug>.md

```markdown
# [Topic] Citation Map

## Search Metadata
- Last searched:
- Search horizon:
- Sources:

## Foundational Classics

## Closest Prior Work

## Direct Competitors / Baselines

## Recent and Concurrent Work

## Surveys / Taxonomies

## Papers Considered But Not Relevant

## Search Queries

## Updates
- YYYY-MM-DD:
```

## Memory Rules

- Include search dates and source URLs.
- Mark recent/concurrent entries as time-sensitive.
- Separate "must cite" from "maybe cite".
- Record papers intentionally not cited and why.
- Do not store long abstracts or copied paper text.
- Re-run web search before relying on old recent-work notes.

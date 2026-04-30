# Memory Model

This skill should accumulate reusable writing knowledge in the user's project, not only in the conversation. Use project-local memory so future writing passes can reuse what was learned from target conference exemplars and from decisions about the current paper.

## Default Memory Location

Create this structure in the active paper or project repository:

```text
.agent/
└── conference-writing/
    ├── README.md
    ├── project-style.md
    ├── venues/
    │   └── <venue>.md
    └── exemplars/
        └── <venue>-<year>.md
```

If the project already has another agent memory directory, follow the local convention and keep the same information model.

## README.md

Explain what the memory is for:

```markdown
# Conference Writing Memory

Reusable notes for adapting this paper to target conference writing conventions.

These notes distinguish observed exemplar patterns, inferred venue taste, project-specific writing decisions, and unresolved questions. They should not contain copied paper text.
```

## project-style.md

Use this file for decisions specific to the current paper:

```markdown
# Project Writing Style

## Current Target
- Venue:
- Year:
- Track:
- Page budget:

## Paper Archetype
- Primary:
- Secondary:
- Rationale:

## Reviewer Promise

## Narrative Decisions

## Claims We Can Support

## Claims To Avoid Or Qualify

## Appendix Strategy

## Open Writing Questions
```

## venues/<venue>.md

Use one file per venue:

```markdown
# [Venue] Writing Patterns

## Official Constraints
- Source:
- Page limit:
- Anonymity:
- Mandatory sections:
- Supplementary rules:
- Checklist / ethics / impact:

## Observed Taste

## Successful Archetypes

## Introduction Patterns

## Experiment / Evidence Patterns

## Limitation Patterns

## Reviewer Risk Patterns

## Updates
- YYYY-MM-DD:
```

## exemplars/<venue>-<year>.md

Use this file to record paraphrased notes from accepted/oral/spotlight/best-paper examples:

```markdown
# [Venue Year] Exemplar Notes

## Source Lists
- URL:
- Access date:
- Selection rule:

## Papers Studied

### [Title]
- Status:
- Authors:
- URL:
- Archetype:
- Main claim:
- Introduction sequence:
- Evidence strategy:
- Notable writing pattern:
- Relevance to our paper:

## Cross-Paper Patterns

## Patterns Not Suitable For Our Paper
```

## Memory Rules

- Record titles, URLs, venue status, and paraphrased observations.
- Do not store long copied text from papers.
- Mark inference explicitly. Example: "Inference: NeurIPS oral papers in this sample foreground broad ML relevance within the first page."
- Separate venue-level patterns from current-paper decisions.
- Include access dates for web sources.
- Update memory after learning from exemplars or after the user accepts a narrative decision.

## Reuse Procedure

At the start of a new writing pass:

1. read `.agent/conference-writing/project-style.md` if it exists
2. read `.agent/conference-writing/venues/<venue>.md` if it exists
3. read recent exemplar notes for the target venue/year
4. state which memory entries are being reused
5. update stale official constraints only after verifying current venue instructions

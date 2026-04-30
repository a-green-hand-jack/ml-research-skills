# Memory Model

Store reviewer-style knowledge project-locally so future pre-reviews become sharper.

## Default Memory Location

```text
.agent/
└── reviewer-simulator/
    ├── README.md
    ├── project-risk-register.md
    ├── venues/
    │   └── <venue>.md
    └── examples/
        └── <venue>-<year>-reviews.md
```

If the project already has an agent memory convention, follow it.

## README.md

```markdown
# Reviewer Simulator Memory

Project-local memory for shadow reviews, venue-specific reviewer patterns, example review notes, and risk registers. Notes should be paraphrased and source-linked.
```

## venues/<venue>.md

```markdown
# [Venue] Reviewer Patterns

## Official Criteria
- Source:
- Access date:
- Score scale:
- Confidence scale:
- Required review fields:

## Observed Reviewer Style

## Common Acceptance Patterns

## Common Rejection Triggers

## Topic-Specific Notes

## Updates
- YYYY-MM-DD:
```

## examples/<venue>-<year>-reviews.md

```markdown
# [Venue Year] Example Review Notes

## Sources
- URL:
- Access date:
- Selection rule:

## Review Pattern Matrix

## Lessons For This Paper

## Patterns Not Applicable
```

## project-risk-register.md

```markdown
# Project Reviewer Risk Register

## Current Target
- Venue:
- Year:
- Submission stage:

## Current Predicted Decision

## Active Risks

## Resolved Risks

## Rebuttal Preparation Notes

## Open Questions
```

## Memory Rules

- Store paraphrased review patterns, not long copied review text.
- Include source URLs and access dates.
- Separate observed review behavior from inference.
- Keep current-paper risks separate from venue-wide patterns.
- Update memory after a full review, after studying examples, or after real reviews arrive.

## Reuse Procedure

At the start of a new shadow review:

1. read `.agent/reviewer-simulator/project-risk-register.md` if it exists
2. read `.agent/reviewer-simulator/venues/<venue>.md` if it exists
3. read recent example notes for the target venue/year
4. state what memory is being reused
5. refresh official criteria if stale or if exact scoring matters

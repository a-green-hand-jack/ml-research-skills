# Memory Model

Store rebuttal state project-locally so discussion rounds and final revisions remain coordinated.

## Default Location

```text
.agent/
└── rebuttal-strategy/
    ├── README.md
    ├── reviews.md
    ├── issue-board.md
    ├── experiment-plan.md
    ├── response-drafts.md
    ├── decision-analysis.md
    └── promised-revisions.md
```

## reviews.md

Store paraphrased or user-approved copied review content:

```markdown
# Reviews

## Source Log

## Review R1
- Score:
- Confidence:
- Summary:
- Strengths:
- Weaknesses:
- Questions:
```

## issue-board.md

Use the table from `issue-board.md`.

## experiment-plan.md

Track evidence tasks:

```markdown
# Rebuttal Experiment Plan

| ID | Owner | Command/log | Status | Result | Response use |
|---|---|---|---|---|---|
```

## response-drafts.md

Save response drafts with timestamps:

```markdown
# Response Drafts

## Draft 1 - YYYY-MM-DD

## Follow-up Replies
```

## decision-analysis.md

Track stance and strategy:

```markdown
# Decision Analysis

## Reviewer Intent Map

## Accept Path

## Reject Path

## Pivotal Issues
```

## promised-revisions.md

Track promises:

```markdown
# Promised Revisions

| Promise | Section | Source issue | Final version status |
|---|---|---|---|
```

## Memory Rules

- Keep private review content in the project, not global memory.
- Separate reviewer text from author inference.
- Update status after each discussion round.
- Track every promised paper revision so it is not forgotten after acceptance.
- Record final decision and what mattered, if known.

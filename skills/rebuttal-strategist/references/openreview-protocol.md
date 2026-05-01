# OpenReview Protocol

Use this reference when reviews or discussion live on OpenReview.

## What To Collect

From the submission forum or exported data, collect:

- paper title and forum URL
- review IDs and reviewer labels
- ratings, confidence, and recommendation fields
- summary, strengths, weaknesses, questions, limitations, ethics, reproducibility fields
- official comments and author responses
- follow-up questions after rebuttal opens
- meta-review or AC note, if available
- response deadline and character/word limits

## Access Strategy

OpenReview pages may be client-rendered or require login. Prefer:

1. user-provided pasted reviews or exported JSON
2. OpenReview API or direct forum/note URLs when accessible
3. screenshots transcribed by the user
4. static web content only when it contains full review text

If login or permissions block access, do not guess. Ask the user for the review text or JSON export.

## Review Extraction Template

```markdown
## Review [R?]
- Rating:
- Confidence:
- Summary:
- Strengths:
- Weaknesses:
- Questions:
- Requested experiments:
- Ethics / reproducibility:
- Official comments:
- Follow-up status:
```

## Thread State

Track the discussion state:

- `not-started`: reviews received, no response yet
- `drafting`: preparing author response
- `submitted`: author response posted
- `discussion`: reviewers are asking follow-up questions
- `meta-review`: AC/meta-review visible
- `decision`: final decision known

## Source Log

Record source and access date:

```markdown
| Source | URL or file | Access date | Notes |
|---|---|---|---|
```

Do not store private review text in global memory. If saving locally, keep it in the project repo and respect the user's privacy expectations.

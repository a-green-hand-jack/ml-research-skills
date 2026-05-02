# Paper Taxonomy

Classify papers by the role they play in the project decision.

## Roles

`foundational`
: Established work that defines the problem, model family, objective, or theoretical lens.

`closest-prior`
: The paper most likely to make the user's idea look incremental.

`direct-competitor`
: A recent method or claim that targets the same problem with a comparable contribution.

`baseline-method`
: A method reviewers will expect in experiments, even if it is not conceptually closest.

`benchmark-source`
: Dataset, metric, protocol, or task definition that fixes the evaluation standard.

`adjacent-family`
: Related method family that informs framing or ablations but does not directly compete.

`theory-source`
: Formal result, assumption, bound, proof technique, or conceptual principle relevant to the claim.

`survey-or-taxonomy`
: Paper useful for orienting terminology and coverage.

`recent-or-concurrent`
: Work close enough in time that it may affect novelty, reviewer expectations, or citation coverage.

`negative-or-limitation`
: Evidence that a popular approach fails, is expensive, has known weaknesses, or cannot support a claim.

`writing-exemplar`
: Accepted or high-quality paper whose structure or positioning is useful for the user's venue.

## Paper Card

Use compact cards:

```markdown
### [Paper]

- Role:
- Core idea:
- Main evidence:
- What it assumes:
- What it does not show:
- Relation to our project:
- Decision impact:
- Read priority:
- Source/verification:
```

## Closest-Work Comparison

For each closest paper, compare:

```markdown
| Paper | Problem | Method move | Claim | Evidence | Our distinction | Risk |
|---|---|---|---|---|---|---|
```

Risk labels:

- `fatal-if-same`
- `must-distinguish`
- `baseline-required`
- `citation-required`
- `positioning-only`
- `low`

## Literature Family Map

Group papers into method families:

```markdown
| Family | Core mechanism | Representative papers | Standard evidence | Open gap | Relevance |
|---|---|---|---|---|---|
```

Avoid making the family map a bibliography. Each family should explain how it changes the project.

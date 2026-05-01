# Issue Board

Use the issue board to convert reviews into manageable tasks.

## Issue Fields

Each issue should include:

- ID
- reviewer
- quote or paraphrased concern
- category
- severity: critical, high, medium, low
- reviewer correctness: correct, partial, misunderstanding, unclear
- response posture
- evidence available
- evidence needed
- action
- owner
- deadline
- status

## Categories

- novelty
- significance
- correctness
- theory
- experiments
- baseline
- ablation
- data/benchmark
- related work
- clarity
- reproducibility
- ethics/limitations
- formatting
- direct question
- praise

## Priority Buckets

- `must-win`: likely determines acceptance
- `must-answer`: direct or serious question
- `quick-win`: easy clarification or citation
- `experiment-needed`: requires new evidence
- `paper-revision`: can be addressed by promised manuscript change
- `do-not-overinvest`: low impact or not realistically persuadable

## Template

```markdown
| ID | Priority | Reviewer | Concern | Category | Correctness | Posture | Evidence | Action | Status |
|---|---|---|---|---|---|---|---|---|---|
| I-001 | must-win | R2 | Missing baseline X | baseline | correct | provide-new-result | pending run | run X on datasets A/B | open |
```

## Status Values

- `open`
- `needs-data`
- `running`
- `evidence-ready`
- `drafted`
- `resolved`
- `deferred`

## Good Actions

Good actions are concrete:

- "Run baseline X on dataset A with same tokenizer and report metric M."
- "Add one sentence distinguishing from Smith et al. in the introduction and related work."
- "Point R3 to Appendix C and move proof sketch into main text in final version."

Bad actions are vague:

- "Improve experiments."
- "Clarify."
- "Address reviewer."

# Consistency Edit Protocol

Use this protocol before editing paper source. The goal is to fix coherence without accidentally changing the science.

## Safe Direct Edits

Usually safe:

- standardize method, dataset, baseline, and metric names
- align a local sentence with a verified result already present nearby
- weaken overstrong verbs when evidence is narrower
- remove repeated or contradictory adjectives
- fix figure/table references or local caption wording
- replace "all" with the actual tested scope when scope is clear

## Requires Caution

Do not directly edit without clear evidence:

- changing primary contribution
- moving claims across sections
- replacing provisional result placeholders
- altering numbers, metrics, or statistical statements
- adding new baselines, experiments, or claims
- deleting limitations
- changing related-work novelty boundary

Route these to the appropriate skill or mark as an unresolved issue.

## Edit Classes

### Name Alignment

Use when the same object has inconsistent names.

Action:

- choose the spelling from the writing contract, method section, or first definition
- update later occurrences only where they refer to the same object
- preserve citation titles and quoted names

### Claim Weakening

Use when one section overstates compared with evidence.

Examples:

- "demonstrates" -> "suggests" when evidence is diagnostic but not causal
- "generalizes across domains" -> "generalizes across the evaluated domains"
- "outperforms all baselines" -> "outperforms the evaluated baselines on [metric/setting]"

### Result Alignment

Use when prose and table/caption disagree.

Action:

- prefer verified table/source artifact over prose
- if source is unclear, report issue instead of editing numbers
- do not infer missing statistics

### Figure/Table Callout Alignment

Use when main text and caption differ.

Action:

- make the callout state the same takeaway as the caption
- ensure figure/table job matches the writing contract
- keep visual-style corrections for `figure-results-review` or `table-results-review`

## Editing Report

For every edit, record:

```markdown
- File:
- Location:
- Issue:
- Edit class:
- Before:
- After:
- Reason:
```

Keep before/after snippets short. Do not include long paper passages.

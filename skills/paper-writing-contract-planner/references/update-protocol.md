# Writing Contract Update Protocol

Use this reference when a writing contract already exists or when new evidence changes the paper's story.

## When to Update

Update `paper/.agent/writing-contract.md` when:

- target venue changes
- primary archetype changes
- title/abstract/intro thesis changes
- a main claim is added, narrowed, contradicted, or cut
- an evidence slot changes status
- new figures or tables change the story
- provisional results are resolved
- reviewer simulation or real reviews expose a structural issue
- related-work boundary changes after literature review

## Update Rules

- Preserve stable decisions unless evidence invalidates them.
- Add a short change note with date and reason.
- Do not silently strengthen claims after new results.
- If evidence contradicts a claim, mark the claim `blocked`, `narrowed`, or `cut`.
- If new evidence fills a slot, update all paper locations that depend on it.
- Keep old provisional placeholders visible until replaced or removed.

## Contract Audit Checklist

Check:

- Is one primary archetype still correct?
- Does the section order match the current paper?
- Do intro contribution bullets map to evidence slots?
- Does each main claim have allowed wording strength?
- Are there claims in abstract/title not supported by the evidence map?
- Do figures/tables still have the jobs assigned in the contract?
- Are provisional results still open?
- Are related-work boundaries still accurate?
- Are limitations consistent with evidence gaps?

## Change Note Format

Use:

```markdown
## Change Notes

- YYYY-MM-DD: [create/update/audit] [short reason]. Changed [claims/sections/evidence/figures/actions].
```

## Handoff Format

At the end of an update, report:

```markdown
## Writing Handoff
- Next section to write:
- Pattern references to use:
- Claims allowed:
- Evidence slots available:
- Placeholders required:
- Actions before final submission:
```

# Writing Memory Update Protocol

Use this protocol whenever a writing-related skill changes prose, plans, claims, result assets, captions, or style rules.

## Before Editing

Read:

- `writing-state.md`
- relevant rows in `section-ledger.md`
- relevant entries in `dependency-map.md`
- relevant style rules in `style-and-terminology.md`
- active threads in `open-writing-threads.md`

If these files do not exist, initialize them.

## During Editing

Track:

- changed paper location
- claim or evidence involved
- whether wording strength changed
- whether a dependency was added or removed
- whether the edit creates a new thread
- whether any other section may now be stale

## After Editing

Update concise entries:

1. `section-ledger.md`
   - status
   - paragraph/caption/table job
   - claim/evidence dependencies
   - next action

2. `dependency-map.md`
   - new or changed links
   - stale locations

3. `edit-impact-log.md`
   - semantic change and reason
   - affected locations
   - completed and remaining updates

4. `open-writing-threads.md`
   - close resolved threads
   - add new blockers

5. `writing-state.md`
   - active focus
   - stale/stable sections
   - next recommended action

6. `session-notes.md`
   - session summary

## Writeback Granularity

Record a memory update for:

- new or revised title/abstract/contribution claim
- new or narrowed claim
- new result or changed result interpretation
- new table/figure/caption
- section status change
- terminology or notation decision
- limitation/scope change
- evidence gap discovery or closure
- placeholder added or resolved

Do not record every typo fix unless it changes style rules or claim meaning.

## Conflict Rules

If writing memory conflicts with `paper-evidence-board`, trust verified evidence and update writing memory.

If writing memory conflicts with `writing-contract.md`, decide whether:

- the draft should follow the contract
- the contract is stale and needs `paper-writing-contract-planner`
- the claim should be narrowed or cut

If writing memory conflicts with current draft text, mark the relevant section `needs-review` and inspect before editing.

## Output Shape

When reporting to the user, include:

- memory files touched
- state changes
- stale locations
- next writing action

Keep the report short. The durable detail belongs in the memory files.

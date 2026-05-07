# Writing Layers

Use this when a paper edit could affect more than one kind of writing quality.

Writing is layered work. Before editing, name the active layer so the edit does not accidentally change claims, notation, evidence, or style.

## Layer Map

| Layer | Goal | Typical edits | Do not accidentally change |
|---|---|---|---|
| `layout` | Fit the page and avoid bad line/float behavior | shorten sentence, split phrase, move local callout, reduce caption length | claim strength, terminology, evidence interpretation |
| `surface-fluency` | Make prose grammatical and smooth | remove redundancy, improve transitions, fix local rhythm | argument structure, notation, measured claims |
| `argument` | Clarify the core point and persuasion path | reorder paragraph jobs, sharpen gap/insight/evidence, change contribution framing | evidence scope without checking the evidence board |
| `technical-consistency` | Keep names, symbols, metrics, datasets, baselines, and notation stable | update glossary, notation, method names, metric arrows, caption labels | author voice or paragraph flow unless needed |
| `style-consistency` | Keep tone, rhythm, claim-strength habits, and venue voice stable | unify "we show" vs "we find", active/passive preference, sentence density | technical meaning or venue-required content |
| `venue-adaptation` | Match target reviewer expectations | adjust section emphasis, related-work granularity, limitation tone, result framing | project positioning unless the contract is updated |
| `final-polish` | Remove small visible defects after structure is stable | repeated words, local concision, citation/caption/callout polish | paragraph order, claims, new evidence dependencies |

If more than one layer is active, edit in this order:

1. argument
2. technical-consistency
3. style-consistency
4. surface-fluency
5. layout
6. final-polish

Venue adaptation can wrap the whole pass, but record whether it changes the paper contract.

## Promotion Ladder

Writing preferences should evolve like visual-style memory:

1. `lesson`: one observed writing issue and fix.
2. `preference`: repeated user/project habit.
3. `project contract`: rule future paper edits must follow.
4. `reusable skill rule candidate`: rule worth moving into public skills after repeated success.

Do not turn a one-off edit into a broad rule unless the user explicitly asks.

## Recommended Memory Files

Use:

```text
paper/.agent/writing-memory/style-and-terminology.md
paper/.agent/writing-style.md                  # optional paper-wide style contract
paper/.agent/writing-style-lessons.md          # optional append-only noisy lesson log
paper/.agent/notation-contract.md              # optional when notation is complex
```

If the current directory is the paper repo, use `.agent/...` equivalents.

## Edit Contract

Before a nontrivial prose edit, record or infer:

```markdown
- Active layer:
- Intended effect:
- Protected invariants:
- Evidence dependency:
- Style/notation dependency:
- Memory writeback needed:
```

Protected invariants usually include:

- no claim strengthening without evidence
- no terminology or notation change without updating the map
- no broad venue repositioning without the writing contract
- no layout-only edit that changes scientific meaning
- no polish edit that removes required caveats

## Lesson Entry

When a reusable lesson appears, append:

```markdown
## YYYY-MM-DD - <short issue>

- Level: lesson | preference | project contract | reusable skill rule candidate
- Layer: layout | surface-fluency | argument | technical-consistency | style-consistency | venue-adaptation | final-polish
- Context:
- Problem:
- Fix:
- Applies to:
- Exceptions:
- Promote when:
- Certainty: user-stated | observed | inferred | unverified
```

Keep entries short. The point is to guide the next edit, not to preserve every sentence draft.

## Layer-Specific Checks

### Layout

- Did the edit only solve page, line, or float pressure?
- Did it preserve claim strength and notation?
- Is the local layout lesson worth recording for future camera-ready edits?

### Surface Fluency

- Is the sentence smoother without changing the argument role?
- Did the edit remove a caveat or experimental condition?

### Argument

- Does the paragraph still map to a claim and evidence slot?
- Did the edit require updating the writing contract or evidence board?

### Technical Consistency

- Are method names, acronyms, symbols, metrics, units, datasets, and baselines canonical?
- Did changing one term make another section stale?

### Style Consistency

- Does the edit match the paper's tone, claim-strength policy, and venue voice?
- Is this a user preference or a project contract?

### Venue Adaptation

- Is the change based on target venue expectations?
- Does it alter positioning, section order, limitation scope, or related-work boundary?

### Final Polish

- Is the paper structurally stable enough for polish?
- Did the edit avoid new claims, new terminology, and new evidence dependencies?

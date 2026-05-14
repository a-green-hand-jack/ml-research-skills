# Edit-Whitelist Contract

An edit-whitelist declares which operation types are **frozen** and which are **allowed** before any controlled rewrite pass begins. It prevents scope creep during writing-quality passes and makes audit trails interpretable.

## When to Use

Declare an edit-whitelist whenever:

- running a multi-round improvement loop (`auto-paper-improvement-loop`)
- doing a surface-fluency or style pass that should not touch claims
- making argument or technical-consistency edits that should not touch prose style
- running camera-ready cleanup that should not reopen scientific decisions

## Standard Whitelist Presets

### Writing-Quality Pass (prose, captions, transitions)
```
FROZEN:
  - Theorem, lemma, proof, and corollary bodies
  - All numerical result values (accuracy, BLEU, F1, etc.)
  - Citation keys and reference list entries
  - Section titles and ordering
  - Algorithm pseudocode bodies

ALLOWED:
  - Prose rewording for clarity and flow
  - Paragraph restructuring within a section
  - Caption rewording (not caption claims)
  - Transition sentences between paragraphs
  - Notation consistency fixes (rename a symbol consistently)
  - Fixing typos, grammar, and punctuation
```

### Argument Pass (logic, claim flow, evidence links)
```
FROZEN:
  - Numerical result values
  - Citation keys (may add citations, not change existing)
  - Style and formatting choices from prior passes

ALLOWED:
  - Restructuring argument order within a section
  - Strengthening or narrowing claim wording based on evidence
  - Adding/removing hedges ("we show" → "we demonstrate" or vice versa)
  - Fixing claim-evidence mismatches
  - Adding forward/backward references to figures, tables, and sections
```

### Technical-Consistency Pass (notation, definitions, terms)
```
FROZEN:
  - Prose style and sentence structure from prior passes
  - Numerical values
  - Argument structure

ALLOWED:
  - Renaming a symbol or variable consistently throughout
  - Adding missing variable definitions
  - Aligning method names and acronyms
  - Fixing equation/theorem numbering inconsistencies
```

### Camera-Ready Cleanup Pass
```
FROZEN:
  - All scientific claims and results
  - Proof bodies and theorem statements
  - Any section that was peer-reviewed

ALLOWED:
  - De-anonymization (author names, institution, acknowledgments)
  - Page-limit formatting adjustments
  - Fixing venue-specific formatting requirements
  - Correcting broken references, labels, and cross-refs
  - Updating URLs or DOIs
```

## How to Declare a Whitelist

At the start of a rewrite pass, write:

```markdown
## Rewrite Pass: <pass name>
Active layer: <writing layer from writing contract>
Edit whitelist: <preset name> | custom
Frozen: <list>
Allowed: <list>
Protected invariants from writing contract: <list any additional>
```

## Rejection Logging

When a proposed edit touches a frozen category, log it:

```
WHITELIST REJECTION
Pass: <pass name>
Proposed edit: <brief description>
Frozen category: <category>
Alternative: <what can be done instead, or "defer to argument/claim pass">
```

Do not silently drop frozen-category edits. Log them so they can be addressed in the correct pass.

## Relation to Writing Layers

The edit-whitelist is a per-pass constraint. The writing contract's layer permissions are the permanent policy. Both must be respected:

- If the writing contract forbids a change at the `style-consistency` layer, the whitelist cannot override it.
- If the whitelist freezes numerics, but the writing contract has a `technical-consistency` layer open, the whitelist still wins for this pass.

# Contrastive Routing Rules — Paper Writing

---

## `paper-writing-contract-planner` vs `paper-writing-assistant` vs `paper-writing-memory-manager`

**Use `paper-writing-contract-planner`** when:
- No writing contract exists yet (`paper/.agent/writing-contract.md` is missing)
- The user wants to lock section order, archetype, paragraph roles, or forbidden claims
- This is the first drafting session and structure is still undecided

**Use `paper-writing-assistant`** when:
- A writing contract already exists
- The user wants to write or revise actual prose: drafting a section, filling placeholders, revising paragraphs
- The question is "write X" not "plan X" or "track X"

**Use `paper-writing-memory-manager`** when:
- The paper has been drafted across multiple sessions
- The user wants to know which sections are stale, what style decisions were made, or what editing threads are open
- The task is state tracking, not writing

**Decision rule**:
- No contract → `paper-writing-contract-planner`
- Has contract, wants prose → `paper-writing-assistant`
- Has prose, wants state → `paper-writing-memory-manager`

---

## `paper-reviewer-simulator` vs `rebuttal-strategist`

**Use `paper-reviewer-simulator`** when:
- Reviews have NOT arrived yet
- The user wants to anticipate reviewer objections before submission
- The goal is a pre-submission risk register, predicted scores, or simulated reject reasons

**Use `rebuttal-strategist`** when:
- Real reviews HAVE arrived (from OpenReview, email, or conference system)
- The user needs to parse review intent, plan follow-up experiments, or draft point-by-point responses
- The question is about responding to actual feedback, not simulating it

**Decision rule**: Have real reviews arrived yet?
- No → `paper-reviewer-simulator`
- Yes → `rebuttal-strategist`

---

## `paper-draft-consistency-editor` vs `auto-paper-improvement-loop`

**Use `paper-draft-consistency-editor`** when:
- A single-pass audit of the full draft is needed
- The task is checking consistency: terminology, claim alignment, figure/table references
- One session, one editor, one sweep

**Use `auto-paper-improvement-loop`** when:
- Multiple review-fix cycles are needed (2+ rounds)
- Each round needs a fresh reviewer context (no carry-over)
- An edit-whitelist is needed to freeze theorems, numerics, or citations during prose passes

**Decision rule**: Is this one sweep (consistency editor) or multiple rounds with fresh reviewers (improvement loop)?

---

## `submit-paper` vs `camera-ready-finalizer`

**Use `submit-paper`** before acceptance:
- pre-submission checklist, source hygiene, anonymity check, bibliography, compile

**Use `camera-ready-finalizer`** after acceptance:
- de-anonymization, rebuttal promise tracking, final claim/evidence lock, supplement update

**Decision rule**: Has the paper been accepted yet?
- No → `submit-paper`
- Yes → `camera-ready-finalizer`

---

## `citation-audit` vs `citation-coverage-audit`

**Use `citation-audit`** for BibTeX correctness:
- unresolved citation keys, metadata errors, DOI/arXiv data, invalid labels

**Use `citation-coverage-audit`** for missing citations:
- foundational works not cited, closest-work papers missing, recent concurrent work

**Decision rule**: Is the problem bad metadata on existing citations (audit) or missing papers that should be cited (coverage)?

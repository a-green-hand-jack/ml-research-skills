# Introduction Paragraph Moves

Use these as paragraph jobs, not as fixed wording.

## Opening Paragraph

Job: establish the problem's importance and audience.

Strong openings:

- name the capability, bottleneck, or question the paper addresses
- connect it to an active research or deployment pressure
- avoid starting with generic history

Weak openings:

- broad claims about AI transforming everything
- field summaries that could introduce any paper
- ungrounded claims of importance

## Gap Paragraph

Job: make the missing piece specific.

Required moves:

- identify the closest current approach, benchmark, assumption, or practice
- state the concrete limitation
- explain why the limitation matters for the target claim

Avoid:

- listing many unrelated shortcomings
- saying "little work has explored" without explaining the consequence
- relying on unsupported "first" language

## Insight Paragraph

Job: explain why the paper's solution should work.

Required moves:

- state the organizing observation or hypothesis
- connect it to the gap
- preview the mechanism without implementation detail

The insight paragraph is often the difference between "we tried X" and "X is the right thing to try."

## Method Overview Paragraph

Job: introduce the proposed object at the right abstraction level.

Required moves:

- name the method/resource/study/system
- describe the core components or design principles
- connect each component to the gap or insight

Avoid:

- equations before the reader knows the paper's job
- implementation details that belong in the method section
- unsupported adjectives such as simple, general, or robust

## Evidence Paragraph

Job: show that the introduction's claims are supported.

Required moves:

- state the evaluation setting
- summarize the main evidence in claim order
- distinguish verified, user-stated, and provisional results

If numbers are provisional, mark them with searchable placeholders and route to `paper-writing-assistant` or `paper-evidence-board`.

## Contribution Paragraph

Job: make the paper's promises explicit.

Good bullets:

- start with a concrete deliverable or finding
- include the evidence type or evaluation scope
- use consistent claim strength

Bad bullets:

- repeat "we propose" three times without saying what is delivered
- mix method, result, and implication in one long bullet
- claim broad generality not supported by experiments

## Handoff Sentences

Every paragraph ending should answer "why should the next paragraph exist?"

Common handoffs:

- problem -> gap: "However, this progress relies on..."
- gap -> insight: "This limitation suggests that..."
- insight -> method: "Motivated by this observation, we..."
- method -> evidence: "We evaluate whether these design choices..."
- evidence -> contributions: "Together, these results support..."

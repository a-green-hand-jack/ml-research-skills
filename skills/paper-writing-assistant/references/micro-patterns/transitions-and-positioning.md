# Transitions and Positioning

Use this file for local transitions, contribution bullets, related-work positioning, and limitation language.

## Section Transitions

Problem to method:

- "This failure mode suggests that [needed property]. We therefore design [method] around [mechanism]."

Method to experiments:

- "The method predicts [testable behavior]. The experiments test this prediction through [main comparison] and [ablation]."

Main result to analysis:

- "The aggregate result supports [claim], but does not explain why. We next isolate [mechanism/factor]."

Result to limitation:

- "The same evidence also reveals a boundary: [condition]."

## Contribution Bullets

Pattern:

- Claim: what is asserted.
- Artifact or method: what the paper provides.
- Evidence: what supports the claim.
- Scope: where the claim applies.

Good forms:

- "We identify [gap] in [setting] and show through [evidence] that [finding]."
- "We introduce [method/artifact], which [mechanism/design principle], and evaluate it on [setting]."
- "We provide [analysis/benchmark/resource] that enables [specific comparison or diagnosis]."

Avoid:

- "We propose a novel framework..."
- "We conduct extensive experiments..."
- "To the best of our knowledge..." unless novelty has been checked.

## Related-Work Positioning

Good:

- "[Prior family] addresses [related problem], but assumes [condition] that does not hold in our setting."
- "Our work is complementary to [family]: it studies [axis] rather than [axis]."
- "We compare against [method] because it represents [closest alternative]."

Avoid:

- dismissive language
- claiming prior work cannot do something without citation support
- positioning based only on keyword differences

## Limitation Language

Good:

- "Our evidence supports [claim] for [scope], but does not establish [broader claim]."
- "This limitation is important because [reviewer-relevant consequence]."
- "We treat [assumption] as part of the problem setting rather than a universal condition."

Avoid:

- "We leave all limitations to future work."
- limitations that introduce a new untested claim

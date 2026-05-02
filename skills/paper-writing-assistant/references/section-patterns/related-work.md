# Related Work Patterns

Use this file when drafting or revising related work. Related work should define the paper's boundary and novelty without turning into a citation list.

## Grouping Strategy

Group papers by the reader question they answer:

- What problem family does this paper belong to?
- What are the closest methods or artifacts?
- What evaluations or datasets define the comparison space?
- What theoretical or empirical findings motivate the claim?
- What adjacent work is related but not directly comparable?

## Paragraph Pattern

1. Topic sentence: name the group and its relevance.
2. Synthesis: state what the group established.
3. Boundary: state what remains unresolved for this paper's claim.
4. Positioning: explain how the current paper differs.

Avoid:

- one sentence per citation
- novelty claims based only on missing keywords
- hostile framing of prior work
- "Unlike all prior work..." unless carefully verified

## Closest Work Paragraph

Use when reviewers are likely to compare against a specific paper or method family.

Pattern:

- "The closest line of work is [family], which [what it does well]."
- "Our setting differs in [task/protocol/assumption/mechanism], which matters because [claim-specific reason]."
- "We compare to [baseline/citation] in [experiment/table] to isolate this difference."

## Benchmark or Dataset Related Work

Use:

- "Existing benchmarks measure [capability], but do not isolate [failure/capability] because [protocol issue]."
- "Our benchmark complements rather than replaces [benchmark family]: it targets [new axis] while retaining [shared evaluation property]."

Avoid:

- claiming a benchmark is obsolete
- treating all prior datasets as directly comparable

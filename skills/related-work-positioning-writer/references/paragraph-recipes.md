# Related Work Paragraph Recipes

Use this reference to draft or revise related-work paragraphs. Each paragraph should synthesize a group and define a boundary.

## Standard Paragraph Shape

1. Topic sentence: name the work family and why it matters.
2. Synthesis: state what the group has established.
3. Closest-work detail: mention closest papers explicitly when needed.
4. Boundary sentence: state how the current paper differs.
5. Handoff: connect to the paper's claim, method, benchmark, or evidence.

Avoid:

- one sentence per paper
- chronological summaries without synthesis
- vague "related but different" endings
- novelty claims without an axis

## Closest Work Paragraph

Use early when reviewer novelty risk is high.

Pattern:

- "The closest line of work is [family], which [achievement]."
- "[Paper A] and [Paper B] are especially relevant because [reason]."
- "Our work differs in [specific axis], and this difference is central to [claim/evidence]."

## Method Family Paragraph

Pattern:

- "[Method family] has been used for [settings]."
- "These methods typically rely on [assumption/design]."
- "Our method uses/changes [component] to address [different constraint]."

## Benchmark / Evaluation Paragraph

Pattern:

- "Evaluation for [capability] commonly uses [benchmarks/metrics]."
- "These resources measure [properties], but leave [gap]."
- "Our benchmark/evaluation focuses on [axis], which is necessary for [claim]."

## Empirical Study Paragraph

Pattern:

- "Empirical studies of [phenomenon] have found [known pattern]."
- "However, existing evidence often varies [confounder]."
- "We isolate [factor] through [study design], allowing us to support [finding]."

## Theory Paragraph

Pattern:

- "Theoretical work on [topic] establishes [result/assumption]."
- "Our paper uses this perspective to [derive/interpret] [specific mechanism]."
- "Unlike results that assume [condition], our claim concerns [scope]."

## Systems Paragraph

Pattern:

- "Systems for [workload] optimize [metric] under [setting]."
- "Prior systems address [bottleneck], but [remaining constraint]."
- "Our design targets [constraint], evaluated through [metric/workload]."

## Application Paragraph

Pattern:

- "In [domain], prior work has focused on [task/metric]."
- "These approaches are limited by [domain constraint]."
- "Our paper adapts [technical element] and evaluates with [domain-relevant criterion]."

## Intro vs Related Work

Put in introduction:

- one or two closest-work contrasts needed to understand the gap
- citation that defines the main problem
- benchmark or baseline that makes the contribution legible

Put in related work:

- broader method families
- secondary adjacent lines
- detailed benchmark or dataset taxonomy
- concurrent work discussion
- surveys and historical context

## Ending Sentences

Good:

- "This distinction matters because our main claim concerns [axis], which prior work does not isolate."
- "We therefore compare to [family] in [section/table] while evaluating [new axis]."
- "These works motivate our setup, but our contribution is [specific claim]."

Weak:

- "Our work is different from all these methods."
- "These methods are orthogonal to ours."
- "To the best of our knowledge, no work has studied this."

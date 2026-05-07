# Reading Modes

## `skim`

Answer:

- Is this paper relevant?
- What role could it play?
- Should it be read deeper?

## `extract-writing`

Extract:

- intro structure
- problem/gap/insight moves
- contribution wording
- caption and result narration patterns
- related-work positioning style

## `extract-method`

Extract:

- objective/function/module
- algorithm steps
- assumptions
- implementation-relevant details
- ablations that validate mechanism

## `extract-theory`

Extract:

- definitions
- assumptions
- theorem statements
- proof strategy
- what the theorem does and does not imply

## `extract-benchmark`

Extract:

- dataset/task
- split/preprocessing
- metrics
- evaluation protocol
- compute/hardware if relevant
- fairness caveats

## `extract-baseline`

Extract:

- baseline identity and citation role
- required implementation details
- what comparison would be fair or unfair
- whether it is must-have, should-have, optional, or citation-only

## `extract-risk`

Extract:

- closest-work overlap
- saturated claims
- reviewer attack surface
- novelty boundary language
- claims to avoid

## `deep-read`

Use when the paper changes the project. Combine method, theory, benchmark, risk, and citation-support extraction, then mark remaining uncertainties explicitly.

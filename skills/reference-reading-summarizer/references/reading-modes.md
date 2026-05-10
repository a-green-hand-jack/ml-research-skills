# Reading Modes

## `skim`

Answer:

- Is this source relevant?
- What role could it play?
- Should it be read deeper?

## `extract-writing`

Extract:

- intro or explanation structure
- problem/gap/insight moves
- contribution wording
- caption and result narration patterns
- related-work or positioning style

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

## `extract-feedback`

Use for collaborator documents, review notes, voice-transcript notes, annotated drafts, and meeting feedback. Extract:

- requested changes
- objections and constraints
- contradictions or later corrections
- decision points
- priority and owner when clear
- places that need project memory or action-board writeback

## `extract-spec`

Use for project specs, task definitions, benchmark instructions, acceptance criteria, and API/interface documents. Extract:

- requirements
- assumptions
- input/output contracts
- constraints
- acceptance criteria
- open questions

## `extract-bundle`

Use for a manually constructed folder. Extract:

- bundle purpose
- file inventory by role
- which files are important vs incidental
- missing context
- recommended next reading order
- whether the bundle should seed project memory

## `extract-implementation-hints`

Use for scripts, notebooks, configs, command logs, and old project folders. Extract:

- reusable commands
- APIs or functions worth adapting
- preprocessing or evaluation details
- environment assumptions
- failure modes and portability risks

## `extract-project-seed`

Use when a project starts from a document or bundle. Extract:

- initial problem
- intended contribution or deliverable
- available resources
- assumptions
- risks
- first project actions
- which skills should run next

## `deep-read`

Use when the source changes the project. Combine relevant modes, then mark remaining uncertainties explicitly.

# Boundary Patterns

Use this reference to position related work safely. The goal is to state what prior work establishes and exactly how the current paper differs.

## Work Buckets

### Closest Direct Work

Role: papers most likely to make reviewers question novelty.

Boundary pattern:

- "The closest work to ours is [family/paper], which [what it establishes]. Our work differs in [axis], which matters because [claim-specific reason]."

Required:

- cite directly
- compare on the axis that supports the paper's contribution
- avoid dismissive language

### Same Problem, Different Method

Role: prior attempts at the same task or question.

Boundary pattern:

- "Prior work on [problem] primarily addresses it through [approach family]. We instead focus on [method/assumption/evaluation axis], enabling [claim]."

### Same Method Family, Different Problem

Role: method ancestors or adjacent mechanisms.

Boundary pattern:

- "[Method family] has been used for [settings]. We use/adapt it for [new setting] where [constraint] changes the design or evidence requirements."

### Benchmark / Dataset / Evaluation Work

Role: evaluation protocols, datasets, metrics, and benchmark comparisons.

Boundary pattern:

- "Existing benchmarks measure [capability], but do not isolate [capability/failure] because [protocol limitation]. Our evaluation targets [axis] while retaining [shared property]."

### Theory / Analysis Foundations

Role: assumptions, proof techniques, analytical concepts, diagnostic tools.

Boundary pattern:

- "These results provide [foundation], while our paper uses this lens to [derive/analyze/evaluate] [specific claim]."

### Systems / Tooling Foundations

Role: infrastructure, scaling, serving, compilers, data pipelines, measurement methods.

Boundary pattern:

- "Systems work on [family] optimizes [metric/workload]. Our paper differs in [workload/design constraint], so the relevant comparison is [metric or setting]."

### Application / Domain Work

Role: domain-specific baselines, non-ML practice, evaluation criteria, deployment constraints.

Boundary pattern:

- "Domain work emphasizes [constraint/metric]. Our contribution is not simply applying [method], but adapting [component/evaluation] to satisfy [domain constraint]."

### Concurrent Work

Role: recent papers that may not define ancestry but affect novelty.

Boundary pattern:

- "Concurrent work also studies [topic]. It is complementary in [axis], while our paper focuses on [axis]."

Use cautious language unless the papers have been carefully compared.

## Unsafe Wording

Avoid unless verified:

- "first"
- "novel" as a standalone claim
- "unlike all prior work"
- "orthogonal"
- "no prior work"
- "the only"
- "entirely different"
- "solves"

Safer alternatives:

- "to our knowledge, under [scope]"
- "differs from the closest work in [specific axis]"
- "complements"
- "focuses on"
- "extends"
- "adapts"
- "evaluates under [setting]"
- "isolates [factor]"

## Boundary Axes

Use one or more:

- problem/task
- assumption
- mechanism
- objective
- architecture
- data/protocol
- metric
- theoretical guarantee
- system workload
- domain constraint
- evaluation scope
- artifact/release
- scale or resource regime

The boundary axis must match the paper's actual claim.

# Method Patterns

Use this file when drafting or revising method, approach, theory setup, benchmark design, or system design sections.

## Method Section Sequence

1. Section promise: state what the method must accomplish and which claim it supports.
2. Setup and notation: define only what the method needs immediately.
3. Core mechanism: present the central idea before secondary components.
4. Component details: explain each component by its job in the mechanism.
5. Training/inference/protocol: give operational details needed for reproducibility.
6. Complexity or implementation notes: include only if they affect claims or evaluation.
7. Bridge to experiments: state what the next section must test.

## Method Overview Paragraph

Job: make the method inspectable before details.

Pattern:

- "Our approach addresses [failure mode] by [central mechanism]."
- "At a high level, it consists of [small number of components], where [component A] handles [role] and [component B] handles [role]."
- "This design predicts [testable behavior], which we evaluate in [experiment/analysis]."

Avoid:

- enumerating modules without saying why they exist
- burying the central mechanism after implementation detail
- using notation before the conceptual objects are clear

## Component Paragraph

Job: explain one component as a claim-supporting design choice.

Pattern:

1. State the component's problem.
2. Explain the design choice.
3. Explain the expected effect.
4. Point to the ablation or analysis that tests it, if available.

## Benchmark or Dataset Design Paragraph

Job: justify why the benchmark measures the claimed capability.

Pattern:

1. State the capability or failure mode.
2. Explain the data/task construction rule.
3. Explain what confound the design controls.
4. State the baseline or diagnostic that validates the protocol.

## Theory Setup Paragraph

Job: make assumptions and consequence legible.

Pattern:

1. State the informal setting.
2. Introduce assumptions in the order they are needed.
3. State why the assumptions are appropriate or limiting.
4. Preview the theorem consequence before formal detail.

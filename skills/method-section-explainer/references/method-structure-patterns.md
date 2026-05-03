# Method Structure Patterns

Choose one primary structure and adapt subsection names to the paper.

## Algorithmic Method

Order:

1. Problem setup and notation.
2. Method overview.
3. Core algorithm or update rule.
4. Training or optimization objective.
5. Inference procedure.
6. Complexity or implementation notes.

Writing pressure:

- The overview should explain the algorithm's idea before equations.
- The algorithm box should be readable after the overview, not before.

## Model Architecture

Order:

1. Input/output definition.
2. Architecture overview.
3. Component modules in data-flow order.
4. Training objective.
5. Inference or deployment.
6. Implementation details.

Writing pressure:

- Tie each module to the paper's design insight.
- Avoid cataloging layers without explaining why they matter.

## Training Objective or Loss Method

Order:

1. Setup and baseline objective.
2. Limitation of the baseline objective.
3. New objective or regularizer.
4. Optimization procedure.
5. Practical details and inference.

Writing pressure:

- Explain what behavior the objective is intended to induce.
- Avoid relying on intuition alone when a derivation is central.

## Benchmark or Dataset Construction

Order:

1. Evaluation desiderata.
2. Data/task source.
3. Filtering, annotation, or generation pipeline.
4. Quality control.
5. Metrics and protocols.
6. Release or usage details.

Writing pressure:

- Method prose should justify design choices, not only list dataset statistics.

## System or Tool

Order:

1. Requirements and constraints.
2. System overview.
3. Components in request/data-flow order.
4. Scheduling, caching, parallelism, or storage design.
5. User/deployment interface.
6. Failure handling and limitations.

Writing pressure:

- Connect system components to measured properties such as speed, scale, cost, or reliability.

## Theory or Formal Setup

Order:

1. Problem setting.
2. Assumptions.
3. Main objects and definitions.
4. Main theorem or proposition.
5. Proof intuition.
6. Consequences or algorithmic implication.

Writing pressure:

- Make assumptions interpretable, not only formal.
- Keep proof details out of the main text unless they are the contribution.

## Hybrid Method

Use when two structures are necessary, such as architecture plus benchmark or system plus algorithm.

Rule:

- First explain the object that readers need to understand all later components.
- Use explicit subsection handoffs to prevent the method section from feeling like two unrelated papers.

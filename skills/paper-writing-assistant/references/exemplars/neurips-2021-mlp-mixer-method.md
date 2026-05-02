# MLP-Mixer: NeurIPS 2021 Method Exemplar

- Source: https://proceedings.neurips.cc/paper/2021/hash/cba0a4ee5ccd02fda0fe3f9a3e7b89fe-Abstract.html
- Venue/status: NeurIPS 2021
- Topic: vision architectures
- Positioning: method with counterintuitive empirical claim
- Best for: simple architecture explanation, counterfactual framing, architecture figure captions

## Reviewer Promise

Competitive image classification does not require convolution or attention when an architecture has the right token- and channel-mixing structure and enough data/regularization.

## Section Patterns

### Abstract

- Opens from the dominant architectural assumptions in the field.
- States the counterintuitive claim plainly.
- Introduces the architecture by its two core operations.
- Scopes evidence to training regimes and benchmark conditions.

### Introduction

- Builds from historical inductive biases to the question of necessity.
- Presents the method as conceptually simple and technically minimal.
- Makes the paper's claim about architectural sufficiency rather than universal superiority.

### Method

- Uses a compact architecture description with a central diagram.
- Defines two recurring operations and their roles.
- Keeps notation light because the mechanism is structural.

### Experiments and Results

- Compares against established architecture families.
- Uses data scale and regularization conditions to scope conclusions.
- Interprets results as challenging assumptions, not replacing all prior models.

## Micro-Patterns

- Paragraph opening: phrase the paper around "is X necessary?" or "what is sufficient?"
- Figure caption: walk through the architecture in the same order as computation.
- Table caption: state model families and training regime before the comparison.
- Limitation language: keep the claim tied to dataset scale and regularization.

## Reuse Cautions

- Counterintuitive claims need careful scope; do not turn "sufficient under conditions" into "always better."
- Architecture simplicity should not be used as a substitute for evidence.

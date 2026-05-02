# Rethinking Generalization: ICLR 2017 Analysis Exemplar

- Source: https://openreview.net/forum?id=Sy8gdB9xx
- Venue/status: ICLR 2017 Oral
- Topic: deep learning generalization
- Positioning: empirical study with theoretical support
- Best for: question-led analysis papers, falsification experiments, mixed empirical/theory narrative

## Reviewer Promise

Common explanations for neural-network generalization are insufficient, as systematic experiments and a theoretical construction show that large networks can fit random labels and noise.

## Section Patterns

### Abstract

- Starts from a field-level puzzle.
- States the conventional explanation being challenged.
- Uses systematic experiments as the main evidence type.
- Adds theory as corroboration rather than replacing empirical evidence.

### Introduction

- Frames the paper as a conceptual challenge, not a new method.
- Makes the reader's prior belief explicit.
- Converts that belief into testable claims.
- Stages experiments to eliminate simple explanations.

### Method / Experimental Design

- Designs experiments as falsification tests.
- Uses synthetic controls and label randomization to isolate explanation gaps.
- Keeps the experimental intervention easy to understand.

### Results

- Results are interpreted as ruling out explanations, not optimizing performance.
- Theory is used to show plausibility or generality of the empirical phenomenon.

## Micro-Patterns

- Paragraph opening: "If [conventional explanation] were sufficient, then [expected result]."
- Result bridge: "Instead, [observed behavior] shows that [explanation] is incomplete."
- Table/figure caption: state the intervention and what hypothesis it tests.
- Limitation language: avoid replacing one incomplete explanation with an unsupported universal theory.

## Reuse Cautions

- This style fits analysis papers with strong controls; it is risky for ordinary ablations.
- A surprising empirical result needs careful alternative-explanation handling.

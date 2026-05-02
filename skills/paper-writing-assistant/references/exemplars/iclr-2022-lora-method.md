# LoRA: ICLR 2022 Method Exemplar

- Source: https://openreview.net/forum?id=nZeVKeeFYf9
- Venue/status: ICLR 2022 Poster
- Topic: language model adaptation and fine-tuning
- Positioning: method with efficiency and quality claims
- Best for: method sections, efficiency tables, introduction framing around deployment cost

## Reviewer Promise

Large pretrained models are expensive to adapt with full fine-tuning; a low-rank adaptation mechanism can preserve task quality while sharply reducing trainable parameters, memory, and inference overhead.

## Section Patterns

### Abstract

- Opens from a concrete scaling pain point: full fine-tuning becomes infeasible for large pretrained models.
- Introduces the mechanism after the cost problem is clear.
- Places efficiency and quality evidence together, so the claim is not only "smaller" but "smaller without quality loss."
- Ends with artifact/release and analysis value.

### Introduction

- Starts from a widely adopted workflow and its bottleneck.
- Converts bottleneck into a method requirement: adapt without changing all model weights.
- Positions against adjacent adaptation methods by practical constraints: parameters, memory, throughput, and latency.
- Contributions are readable as method, evidence, analysis, and artifact.

### Method

- Defines the insertion point in existing architectures before algebraic detail.
- Explains low-rank matrices as the central mechanism.
- Separates what is frozen from what is trainable.
- Keeps deployment implications close to the design choice.

### Experiments and Results

- Combines quality tables with efficiency metrics.
- Uses multiple model families to support broad adaptation claims.
- Includes analysis of rank choices to support the mechanism rather than only the benchmark result.

## Micro-Patterns

- Paragraph opening: begin from the user cost or deployment constraint, then introduce the technical mechanism.
- Table caption: state both comparison axes: task quality and resource footprint.
- Result interpretation: phrase as "matching or improving quality while reducing adaptation cost," not just "outperforming."
- Limitation language: scope the claim to adaptation regimes and tested model families.

## Reuse Cautions

- Do not borrow the efficiency framing unless the user's evidence includes real memory, parameter, speed, or latency measurements.
- If the user's method has extra inference cost, do not use a "no inference overhead" style claim.

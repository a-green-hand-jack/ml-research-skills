# ZeRO: SC20 Systems Exemplar

- Source: https://sc20.supercomputing.org/proceedings/tech_paper/tech_paper_pages/pap379.html
- Venue/status: SC20 Technical Paper
- Topic: distributed training systems
- Positioning: systems method with scalability and throughput evidence
- Best for: systems sections, operational constraints, scalability tables, workload captions

## Reviewer Promise

Memory redundancy, not only computation, limits large-model training; partitioning optimizer/model states can scale model size while preserving efficient distributed training.

## Section Patterns

### Abstract

- Opens from operational bottleneck: training very large models exceeds device memory.
- States why existing parallel strategies are insufficient.
- Introduces the system idea as a resource-optimization mechanism.
- Reports scale, throughput, and usability evidence.

### Introduction

- Makes hardware/resource constraints concrete.
- Describes user pain: model size, memory footprint, communication, and usability.
- Converts system design into measurable goals.
- Previews end-to-end and component-level evaluation.

### System Design

- Starts with memory accounting and bottleneck decomposition.
- Presents design stages or components as responses to specific memory redundancies.
- Explains communication/computation tradeoffs near the design choice.

### Experiments and Results

- Uses workload, hardware, and scale as part of every result claim.
- Reports throughput, speedup, model-size ceiling, and usability.
- Separates analytical claims from measured system results.

## Micro-Patterns

- Paragraph opening: start with a resource bottleneck or workload requirement.
- Table caption: include hardware, model size, number of devices, and metric units.
- Result interpretation: state what system constraint was removed or shifted.
- Limitation language: scope claims to cluster scale, workload, framework, and hardware.

## Reuse Cautions

- Systems claims require workload and hardware details in captions and result prose.
- Avoid "scales to" language without specifying what scales and under which efficiency measure.

# Segment Anything: ICCV 2023 Benchmark/Artifact Exemplar

- Source: https://openaccess.thecvf.com/content/ICCV2023/html/Kirillov_Segment_Anything_ICCV_2023_paper.html
- Venue/status: ICCV 2023
- Topic: image segmentation foundation models
- Positioning: new task + model + dataset + artifact release
- Best for: artifact papers, dataset/model/task triangulation, visual captions

## Reviewer Promise

A promptable segmentation task, trained through a large-scale data engine, can support zero-shot transfer across segmentation settings and provide a reusable foundation artifact.

## Section Patterns

### Abstract

- Introduces the project as a task, model, and dataset together.
- States scale as evidence only after the task/model purpose is clear.
- Emphasizes transfer and release value.

### Introduction

- Frames segmentation as fragmented by task-specific setups.
- Introduces promptability as the organizing idea.
- Connects data collection, model design, and dataset scale into one system.
- Uses release language to clarify community contribution.

### Method / System

- Separates task definition, model design, and data engine.
- Explains each component by its role in enabling promptable zero-shot use.
- Keeps dataset construction tied to model capability.

### Experiments and Results

- Uses many tasks to support transfer claims.
- Compares zero-shot behavior against supervised or task-specific baselines with careful wording.
- Visual examples help readers inspect generality.

## Micro-Patterns

- Figure caption: define prompts, masks, and task variants explicitly.
- Table caption: state whether comparisons are zero-shot, supervised, or otherwise not equivalent.
- Paragraph opening: introduce task/model/dataset as mutually reinforcing, not three unrelated contributions.
- Contribution bullet: artifact release plus capability plus evaluation scope.

## Reuse Cautions

- Do not claim foundation-model generality without broad transfer evidence.
- Dataset scale should not replace data quality, licensing, or evaluation validity discussion.

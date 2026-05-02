# BERT: NAACL 2019 Method Exemplar

- Source: https://aclanthology.org/N19-1423/
- Venue/status: NAACL 2019 Best Long Paper
- Topic: NLP pretraining
- Positioning: method with broad benchmark evidence
- Best for: simple method exposition, broad NLP benchmark result paragraphs, contribution bullets

## Reviewer Promise

Bidirectional pretraining can produce a general language representation that transfers across many NLP tasks with minimal task-specific architecture.

## Section Patterns

### Abstract

- Names the method and immediately contrasts it with prior representation directionality.
- States the mechanism in plain terms before benchmark evidence.
- Uses broad task coverage as the key evidence style.

### Introduction

- Starts from transfer learning and representation learning context.
- Makes a single architectural/pretraining distinction do much of the explanatory work.
- Uses result breadth to justify general-purpose claims.
- Keeps the contribution story simple: pretraining method, fine-tuning recipe, broad results.

### Method

- Explains model input, pretraining tasks, and fine-tuning workflow in operational order.
- Makes "simple to fine-tune" part of the method story.
- Avoids overcomplicating the architecture beyond what supports the claim.

### Experiments and Results

- Organizes experiments by task families.
- Uses benchmark breadth to support general representation claims.
- Result prose emphasizes consistent transfer rather than a single isolated win.

## Micro-Patterns

- Paragraph opening: introduce the central contrast with prior methods before naming every benchmark.
- Contribution bullet: method plus usability plus broad empirical support.
- Table caption: state task family and metric direction, then the transfer takeaway.
- Result interpretation: link breadth of improvements to generality, but avoid claiming universal language understanding.

## Reuse Cautions

- Broad benchmark evidence only supports broad claims when tasks are diverse and comparable.
- Avoid copying the "simple and powerful" style if the user's method has complex task-specific machinery.

# DDPM: NeurIPS 2020 Method Exemplar

- Source: https://proceedings.neurips.cc/paper/2020/hash/4c5bcfec8584af0d967f1ab10179ca4b-Abstract.html
- Venue/status: NeurIPS 2020 Poster
- Topic: generative modeling and diffusion
- Positioning: theory-inspired method with visual and quantitative evidence
- Best for: method intuition, figure-first generative model exposition, result interpretation with sample quality metrics

## Reviewer Promise

A diffusion probabilistic model can be trained through a denoising objective that connects likelihood-based modeling with score-based sampling, yielding high-quality image generation.

## Section Patterns

### Abstract

- Opens with result category and method family.
- Connects the objective to a theoretical or conceptual bridge.
- Includes visual/generation quality evidence and benchmark metrics.

### Introduction

- Places the method among generative model families.
- Identifies weaknesses or tradeoffs in existing families.
- Introduces diffusion as a route to combine desirable properties.
- Lets early visual evidence establish reader interest.

### Method

- Builds from process definition to training objective to sampling interpretation.
- Uses equations for precision but keeps the generative story visible.
- Connects mathematical terms to sampling behavior.

### Experiments and Results

- Pairs visual samples with quantitative generation metrics.
- Uses comparisons to established generative baselines.
- Interprets results as image quality and modeling behavior, not only metric wins.

## Micro-Patterns

- Figure caption: state what the samples demonstrate and under which dataset/resolution.
- Result paragraph opening: name the benchmark and metric before interpreting generation quality.
- Claim-evidence bridge: connect objective choice to observed sample quality or sampling behavior.
- Limitation language: separate image quality evidence from claims about likelihood, diversity, or downstream utility.

## Reuse Cautions

- Do not use sample visuals as sufficient evidence if the user's claim is about calibration, controllability, or robustness.
- Metrics such as FID or Inception Score need context and baseline comparison.

# Latent Diffusion: CVPR 2022 Method Exemplar

- Source: https://openaccess.thecvf.com/content/CVPR2022/html/Rombach_High-Resolution_Image_Synthesis_With_Latent_Diffusion_Models_CVPR_2022_paper.html
- Venue/status: CVPR 2022
- Topic: high-resolution image synthesis
- Positioning: method with compute-efficiency and quality claims
- Best for: CVPR-style visual narrative, figure captions, compute bottleneck framing

## Reviewer Promise

Moving diffusion modeling into a perceptually meaningful latent space can preserve generation quality while reducing the computational burden of pixel-space diffusion.

## Section Patterns

### Abstract

- Opens from an established method's strength and its compute bottleneck.
- States the representation shift as the core mechanism.
- Uses quality, flexibility, and compute reduction as linked evidence axes.
- Mentions multiple tasks to support versatility.

### Introduction

- Frames image synthesis as visually successful but computationally demanding.
- Explains why pixel-space modeling creates unnecessary cost.
- Introduces latent modeling as a quality/efficiency compromise.
- Uses figure evidence early to make visual quality inspectable.

### Method

- Separates autoencoding representation from diffusion process.
- Explains conditioning mechanisms as extensions of the main idea.
- Makes spatial compression and detail preservation central design concerns.

### Experiments and Results

- Organizes around task variety and quality/efficiency tradeoffs.
- Captions and figures carry much of the visual claim.
- Tables support claims with metrics, while figures support perceptual plausibility.

## Micro-Patterns

- Figure caption: first sentence should state the visual or reconstruction takeaway.
- Table caption: include metric direction and task setting because multiple tasks are compared.
- Result interpretation: present quality and compute as a tradeoff, not separate claims.
- Transition: move from bottleneck to latent representation as a necessity, not only an implementation detail.

## Reuse Cautions

- Do not claim compute reduction unless the paper reports comparable training or inference cost.
- Visual quality claims should be paired with benchmark or human/metric evaluation when possible.

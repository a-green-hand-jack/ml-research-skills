# Compute Estimation Guide

## Throughput Reference Values (approximate, single GPU)

These are rough order-of-magnitude estimates for planning. Actual throughput depends on batch size, sequence length, mixed precision, and GPU generation. Always prefer measured throughput from a smoke test.

### Language Models (tokens/second, BF16/FP16)

| Model size | A100 80GB | H100 80GB | V100 32GB | RTX 3090 |
|---|---|---|---|---|
| 125M | ~80k tok/s | ~130k tok/s | ~35k tok/s | ~25k tok/s |
| 350M | ~35k tok/s | ~55k tok/s | ~15k tok/s | ~10k tok/s |
| 1B | ~12k tok/s | ~20k tok/s | ~5k tok/s | ~3k tok/s |
| 7B | ~1.5k tok/s | ~3k tok/s | OOM | OOM |
| 70B (4× A100) | ~0.5k tok/s | ~1k tok/s | — | — |

Divide by sequence length to get samples/second for fixed-length data.

### Vision Models (samples/second, BF16)

| Model | A100 80GB | V100 32GB | RTX 3090 |
|---|---|---|---|
| ResNet-50 (224×224, BS=256) | ~1800/s | ~700/s | ~500/s |
| ViT-B/16 (224×224, BS=128) | ~800/s | ~300/s | ~200/s |
| ViT-L/16 (224×224, BS=64) | ~250/s | ~80/s | ~50/s |
| CLIP ViT-B (BS=256) | ~700/s | ~250/s | ~180/s |

### Multi-Modal / Diffusion (approximate)

These are highly variable; measure from a smoke test.

| Model class | A100 throughput (rough) |
|---|---|
| Stable Diffusion XL inference | ~3 images/s |
| SDXL training (512×512, BS=4) | ~0.5 iter/s |
| LLaVA 7B inference | ~8 tok/s |

## GPU Memory Estimation

Rule of thumb for model parameters in BF16/FP16:

```
Model memory (GB) ≈ parameters (billions) × 2
```

Training with optimizer states (AdamW):

```
Training memory (GB) ≈ parameters (billions) × 16
```

This is a rough estimate. Add activation memory (~10–30% of model memory for typical batch sizes) and gradient checkpointing reduces activations at ~30% throughput cost.

LoRA fine-tuning: model memory + ~0.1–0.5GB for adapter weights + optimizer on adapters only (~2 × adapter parameters GB).

## GPU-Hour Estimation Formula

```
gpu_hours = (total_steps × batch_size) / (throughput_samples_per_sec × 3600) × num_gpus
```

Or equivalently:

```
gpu_hours = total_samples_seen / (throughput_samples_per_sec × 3600) × num_gpus
```

For token-based training:

```
gpu_hours = (total_steps × batch_size × seq_len) / (throughput_tokens_per_sec × 3600) × num_gpus
```

## Common Benchmark Costs (approximate)

| Experiment | Model | Hardware | Cost |
|---|---|---|---|
| ImageNet classification (90 epochs) | ResNet-50 | 1× A100 | ~12 GPU-hours |
| GLUE fine-tuning (3 epochs) | BERT-base | 1× A100 | ~1 GPU-hour |
| C4 pre-training (1B tokens) | GPT-125M | 1× A100 | ~2 GPU-hours |
| C4 pre-training (1B tokens) | GPT-1B | 1× A100 | ~15 GPU-hours |
| CIFAR-10 (200 epochs) | ResNet-18 | 1× RTX 3090 | ~2 GPU-hours |

## Smoke Test Sizing Rules

| Full run cost | Smoke test target | Recommended steps |
|---|---|---|
| < 1 GPU-hour | 5–10 min, 1 GPU | 50–200 steps |
| 1–10 GPU-hours | 10–20 min, 1 GPU | 200–500 steps |
| 10–100 GPU-hours | 15–30 min, 1 GPU | 500–2000 steps |
| > 100 GPU-hours | 20–30 min, 1 GPU | 1000–5000 steps |

Smoke tests should show:
1. Loss decreases by at least 10% from the first step
2. No NaN, OOM, or crash
3. One checkpoint saves and loads correctly
4. Metrics are computed without error

## Disclosure Language for Papers

When reporting compute in a paper:

```
"We trained on N× [GPU model] for approximately X GPU-hours. 
The full ablation matrix required Y GPU-hours total. 
[Model/checkpoint size] is Z GB."
```

For reproducibility sections (NeurIPS, ICLR checklists):

- Report GPU type and count
- Report total training GPU-hours for the primary result
- Report wall-clock time for the primary result
- State whether the result can be reproduced on consumer hardware and at what cost reduction

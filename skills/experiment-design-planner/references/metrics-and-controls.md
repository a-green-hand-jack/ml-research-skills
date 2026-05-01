# Metrics and Controls

Use this reference to choose metrics, controls, and logging fields.

## Metric Selection

For each metric, define:

- name
- exact formula or library implementation
- direction: higher/lower is better
- unit
- split
- aggregation: mean, median, final, best checkpoint, area under curve
- variance: std, stderr, confidence interval, bootstrap, or per-seed values
- failure meaning

Prefer metrics that directly answer the research question.

## Metric Types

- task performance: accuracy, F1, BLEU, ROUGE, perplexity, win rate
- calibration: ECE, Brier score, reliability curve
- efficiency: runtime, throughput, latency, memory, FLOPs, query count, cost
- robustness: performance under perturbation, shift, corruption, adversarial examples
- sample efficiency: performance vs data size or labels
- stability: variance across seeds, checkpoints, prompts, or data samples
- qualitative: representative examples, failure taxonomy, human inspection

## Controls

Common controlled variables:

- dataset and split
- preprocessing
- model architecture
- parameter count
- training budget
- optimizer and schedule
- batch size
- random seed
- evaluation protocol
- prompt/template
- hardware
- inference budget

## Nuisance Variables

List confounders that could explain results:

- different compute budget
- different hyperparameter tuning effort
- data leakage
- baseline under-tuning
- metric implementation mismatch
- checkpoint selection bias
- prompt sensitivity
- seed variance
- preprocessing differences
- train/test contamination

## Logging Checklist

Required fields:

- git commit hash
- command
- config file
- dataset version
- split name
- seed
- hyperparameters
- environment or container
- hardware
- start/end time
- metric outputs
- artifact paths
- failure notes

If a result may go into a paper, log enough to reproduce the table row.

# Title and Contribution Rules

## Title Styles

Use title options to expose strategic choices.

### Direct Method Name

Good when the method name is distinctive and the paper's audience can infer the area.

Risk: may hide the problem or evidence.

### Problem Plus Method

Good when the problem is important and the method is the main contribution.

Risk: can become long or generic.

### Finding-Led

Good for empirical, analysis, or negative-result papers.

Risk: needs strong evidence and careful scope.

### Resource-Led

Good for benchmark, dataset, or tool papers.

Risk: should not sound like a software announcement unless artifact value is central.

### Mechanism-Led

Good when the insight is the contribution.

Risk: may overpromise generality if the mechanism is narrowly tested.

### Scoped Conservative

Good for early drafts, narrow studies, or papers with mixed evidence.

Risk: may undersell if the evidence is strong.

## Title Checks

Ask:

- Does the title name the right object: problem, method, finding, resource, or system?
- Does the title imply a broader scope than experiments support?
- Would the target venue's reviewers know what area this belongs to?
- Does the title conflict with the contribution bullets?

## Contribution Bullet Recipe

Each bullet should contain:

```text
deliverable/finding + scope + evidence/value
```

Examples of bullet jobs:

- method contribution: what mechanism or algorithm is new
- evidence contribution: what experiments show
- analysis contribution: what finding changes understanding
- resource contribution: what dataset/benchmark/tool is released
- practical contribution: what speed, scale, or workflow benefit is demonstrated

## Contribution Bullet Checks

Avoid:

- multiple bullets that all start with "We propose"
- bullets that claim novelty without specifying the novelty boundary
- bullets that mention a result without saying the setting
- bullets that promise a release not planned for submission
- bullets that duplicate the abstract without adding auditability

## Overclaim Downgrades

Use these downgrades when evidence is limited:

- "solves" -> "addresses" or "improves"
- "general" -> "effective across the evaluated settings"
- "state-of-the-art" -> "outperforms the evaluated baselines"
- "demonstrates robustness" -> "is stable across the tested seeds/settings"
- "explains" -> "provides evidence that" or "is consistent with"

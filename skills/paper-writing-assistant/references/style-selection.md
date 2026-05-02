# Style Selection

Use this file to choose the writing style before drafting. The goal is to select a small set of section and micro-pattern references that match the paper's venue, topic, positioning, evidence type, and active writing task.

Do not copy wording from exemplar papers. Use exemplars to infer structure, pacing, evidence placement, and rhetorical moves.

## Selection Inputs

Collect these before writing:

- Target venue and year
- Topic area: vision, language, representation learning, agents, theory, systems, robustness, evaluation, data, science application, or domain-specific
- Paper positioning: method, benchmark/dataset, empirical study, theory, systems, analysis, application, or hybrid
- Active section: abstract, introduction, method, experiments, results, related work, limitations, conclusion, figure caption, or table caption
- Evidence type: table, figure, theorem, ablation, qualitative result, benchmark protocol, user study, system measurement, or citation synthesis
- Claim strength: main claim, secondary claim, scope claim, limitation, or rebuttal-preempting clarification

## Venue Style Heuristics

### NeurIPS / ICML

Good default for method, empirical, theory, benchmark, and dataset papers.

- Make the contribution and evidence chain easy to audit.
- State the claim early, then show why the experiment design tests it.
- Prefer precise claim/evidence language over promotional novelty language.
- For empirical papers, emphasize controls, baselines, ablations, and alternative explanations.
- For theory papers, make assumptions and implications legible before proof detail.

### ICLR

Good default for method, representation, generative modeling, agents, and analysis papers.

- Make the central intuition unusually clear.
- Use experiments to test the mechanism or hypothesis, not only leaderboard wins.
- Let ablations carry conceptual evidence when they isolate the proposed mechanism.
- Avoid hiding key design choices behind implementation details.

### CVPR / ICCV / ECCV

Good default for vision method, benchmark, dataset, and application papers.

- Make visual evidence and task setup visible early.
- Use figures and tables as primary story carriers.
- Captions should be more self-contained because readers skim visuals heavily.
- Explain protocol, metrics, and data splits close to the first result that depends on them.

### ACL / EMNLP / NAACL

Good default for NLP, LLM evaluation, data, empirical analysis, and application papers.

- Be explicit about task framing, data provenance, annotation/evaluation validity, and linguistic or usage scope.
- Result interpretation should separate model capability claims from dataset/protocol artifacts.
- Related work often needs tighter grouping by task, evaluation setting, and method family.
- Avoid overgeneralizing from one benchmark family to language understanding broadly.

### Systems Venues

Good default for training, serving, infrastructure, compilers, data systems, and deployment papers.

- Start from the operational constraint and workload.
- Tie design choices to measured latency, throughput, cost, reliability, scalability, or usability.
- Captions should state workload, hardware, metric, and operational takeaway.
- Avoid method-paper framing unless the system contribution is an algorithmic design.

## Positioning to Structure

### Method

- Opening: existing approaches fail under a specific condition.
- Core move: introduce the mechanism that addresses the failure.
- Evidence: main result shows benefit; ablations isolate the mechanism; analysis explains when it works.
- Style risk: claiming generality without sufficient task or dataset coverage.

### Empirical Study

- Opening: a field-level question remains unresolved or mismeasured.
- Core move: define controlled comparisons and what each can falsify.
- Evidence: systematic results, sensitivity analyses, and alternative explanations.
- Style risk: sounding like a benchmark paper without a clear finding.

### Benchmark / Dataset

- Opening: current evaluation cannot measure an important capability or failure mode.
- Core move: define task, protocol, data quality, and validity checks.
- Evidence: baseline suite, diagnostic slices, and examples of newly visible behavior.
- Style risk: treating dataset construction as sufficient without showing what it enables.

### Theory

- Opening: existing understanding lacks a guarantee, condition, or impossibility result.
- Core move: state assumptions, theorem shape, and proof intuition.
- Evidence: theorem, proof, tightness, examples, or empirical sanity check.
- Style risk: burying the consequence of the theorem behind notation.

### Systems

- Opening: real workloads expose a constraint that existing systems do not meet.
- Core move: present design choices as responses to measurable bottlenecks.
- Evidence: end-to-end performance, component breakdowns, scaling, and stress tests.
- Style risk: reporting many metrics without saying which design claim each supports.

### Analysis

- Opening: a phenomenon is observed but not explained.
- Core move: isolate factors through diagnostics or controlled interventions.
- Evidence: linked analyses that rule out simpler explanations.
- Style risk: overclaiming causality from correlational diagnostics.

## Reference Loading Rules

Load section patterns by active section:

- Abstract: `section-patterns/abstract.md`
- Introduction: `section-patterns/introduction.md`
- Method: `section-patterns/method.md`
- Experiments/results: `section-patterns/experiments-results.md`
- Related work: `section-patterns/related-work.md`
- Limitations/conclusion: `section-patterns/limitations-conclusion.md`

Load micro-patterns by writing action:

- Paragraph starts and closes: `micro-patterns/paragraph-openings-closings.md`
- Figure captions: `micro-patterns/figure-captions.md`
- Table captions: `micro-patterns/table-captions.md`
- Result interpretation and claim bridges: `micro-patterns/result-interpretation.md`
- Transitions, contribution bullets, and related-work positioning: `micro-patterns/transitions-and-positioning.md`

If the task is broad, load at most one section-pattern file and one or two micro-pattern files first. Load more only when the requested edit needs them.

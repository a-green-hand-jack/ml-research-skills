# Paragraph Protocol

Use this protocol when producing paragraph-level plans or rewrites. Conference papers are dense persuasive documents: every paragraph should do one job for a reviewer.

## Paragraph Functions

Choose one primary function per paragraph:

- `context`: establish the field, task, or practical stakes
- `problem`: make a limitation, gap, or failure mode concrete
- `tension`: explain why the problem is nontrivial
- `insight`: state the paper's key idea
- `approach`: summarize how the paper operationalizes the insight
- `contribution`: enumerate claims and evidence
- `setup`: define notation, task, assumptions, or benchmark protocol
- `mechanism`: explain how a method component works
- `evidence`: describe an experiment, theorem, analysis, or qualitative result
- `interpretation`: explain what evidence means and what it does not mean
- `preemption`: address an obvious reviewer concern before it becomes a weakness
- `positioning`: distinguish the work from related work
- `limitation`: bound the claim honestly
- `transition`: justify why the next section exists

## Abstract Pattern

Most ML abstracts should be one paragraph with this sequence:

1. problem or context
2. gap in current approaches or understanding
3. proposed idea in one sentence
4. method/evaluation scope
5. headline evidence
6. implication or availability, if relevant

Do not use the abstract to list every component. Use it to make the reviewer believe the paper has a focused promise and credible evidence.

## Introduction Pattern

Default 5-paragraph introduction:

1. `context`: why the problem matters now
2. `problem`: what current methods, benchmarks, or theories fail to address
3. `tension`: why the gap is hard or has been missed
4. `insight + approach`: the paper's core idea and how it becomes a method/study/benchmark
5. `contribution`: 3-4 contributions, each tied to evidence

For very strong empirical-study papers, replace paragraph 4 with a findings preview. For theory papers, paragraph 4 should state the formal question and main result in interpretable terms.

## Method Section Pattern

Open with a method overview paragraph:

- inputs and outputs
- high-level components
- what is new
- how the section is organized

Then use one paragraph per component or conceptual step:

- state the component's job
- give intuition
- define the operation or objective
- explain interaction with previous components
- mention implementation details only when they affect the claim

End with complexity, assumptions, or practical details if reviewers will care.

## Experiment Section Pattern

Order experiments by reviewer questions:

1. Does the method/study/benchmark address the main claim?
2. Is the comparison fair and strong?
3. Which component matters?
4. When does it fail or stop helping?
5. Is the result robust across settings?
6. What qualitative or diagnostic evidence explains the result?

Each result paragraph should follow:

```text
Question -> setup -> result -> interpretation -> limitation or next question
```

Avoid table narration that repeats every number. Name the comparison that changes the reader's belief.

## Related Work Pattern

Related work should position the paper, not merely cite papers.

Use paragraphs by conceptual boundary:

- closest methods and why they are insufficient
- adjacent benchmark/data/theory work
- tools or domains that inform but do not solve the problem

For venues where related work is often after experiments, keep introduction citations focused on the closest motivation and move broad taxonomy later.

## Limitation Pattern

A good limitation paragraph:

- names the boundary
- explains why it exists
- states whether it threatens the main claim
- suggests what evidence would resolve it

Do not bury limitations in vague statements. Reviewers trust limitations that are specific and scoped.

## Paragraph Blueprint Template

Use this exact template for important paragraphs:

```markdown
### [Section] P[N]
- Function:
- Reader question answered:
- Claim:
- Evidence or support:
- Opening move:
- Closing move:
- Keep:
- Cut or move:
- Risk if weak:
```

## Rewrite Checks

For each rewritten paragraph, check:

- can the reviewer name the paragraph's job?
- is the first sentence a useful orientation?
- does the paragraph end by advancing the argument?
- is there exactly one main claim?
- is the claim supported by evidence, citation, definition, or explicit scope?
- can any sentence move to appendix without weakening the argument?

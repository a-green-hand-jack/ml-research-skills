# Contrastive Routing Rules — Root Router

Use this file when two or more root-level buckets seem equally plausible.

---

## `feedback-synthesizer` vs `advisor-update-writer`

**Use `feedback-synthesizer`** when:
- Feedback is arriving **inbound** from an advisor, collaborator, or reviewer
- The task is to triage, interpret, and connect feedback to project claims/risks/actions
- The user says: "my advisor said...", "we got comments from...", "how do I process this feedback?"

**Use `advisor-update-writer`** when:
- The user is **writing outbound** to an advisor or collaborator
- The task is to produce a decision-oriented memo, email, or lab note
- The user says: "I need to write an update to my advisor", "write my weekly memo"

**Decision rule**: Is information flowing IN (synthesize) or OUT (write)?
- Information flowing in → `feedback-synthesizer`
- Information flowing out → `advisor-update-writer`

---

## `rebuttal-strategist` vs `paper-writing-router` → `paper-reviewer-simulator`

**Use `rebuttal-strategist`** when:
- Real reviewer comments have arrived from a conference or journal
- The user needs to parse actual review text, plan experiments, draft point-by-point responses
- The user says: "reviews are in", "reviewer 2 says...", "OpenReview posted decisions"

**Use `paper-writing-router` → `paper-reviewer-simulator`** when:
- No real reviews exist yet
- The user wants to simulate what reviewers might say before submission
- The user says: "what will reviewers think?", "predict my scores", "simulate a meta-review"

**Decision rule**: Have real reviews arrived yet?
- Yes → `rebuttal-strategist`
- No (simulating) → `paper-writing-router` → `paper-reviewer-simulator`

---

## `discovery-router` vs `experiment-evidence-router`

**Use `discovery-router`** when:
- The task is about exploring the research landscape, validating an idea, or reading literature
- The user hasn't started experiments yet or is questioning the research direction
- The user says: "is this idea novel?", "survey related work", "read these papers", "what's been done?"

**Use `experiment-evidence-router`** when:
- The project direction is decided and the task is about executing, debugging, or interpreting experiments
- The user says: "run this ablation", "my results show...", "I got NaN training loss"

**Decision rule**: Is the task exploratory/directional (discovery) or execution/evidence-driven (experiment)?
- Exploratory, idea-level → `discovery-router`
- Execution or result-level → `experiment-evidence-router`

---

## `algorithm-design-planner` vs `experiment-evidence-router` → `experiment-design-planner`

**Use `algorithm-design-planner`** when:
- The user needs to design the method itself: formulation, mechanism, assumptions, ablation implications
- The method does not yet exist and the task is to specify it
- The user says: "design the algorithm", "how should the mechanism work?", "method spec"

**Use `experiment-evidence-router` → `experiment-design-planner`** when:
- The method is already designed and the task is to plan how to test it
- The task is about ablation hypothesis, metrics, controls, stop conditions
- The user says: "design the ablation experiments", "what metrics should I log?", "experiment plan"

**Decision rule**: Is the method itself being designed (algorithm-design-planner) or is the experiment to test it being planned (experiment-design-planner)?
- Designing the method → `algorithm-design-planner`
- Planning experiments to test the method → `experiment-evidence-router` → `experiment-design-planner`

---

## Paper-adjacent tasks: `paper-writing-router` vs `experiment-evidence-router`

**Use `paper-writing-router`** when:
- The primary output is prose, LaTeX, or a document artifact
- The task is writing or editing, not running or interpreting experiments
- "Build a table from my CSV" is borderline — it produces a paper asset, so route to `paper-writing-router` → `paper-result-asset-builder`

**Use `experiment-evidence-router`** when:
- The primary output is an experiment decision, job submission, or scientific interpretation
- The user is acting on results, not writing about them yet
- "My results are ready, what do I do?" → `experiment-evidence-router` → `result-diagnosis` or `research-results-auditor`

**Decision rule**: Is the deliverable a written/LaTeX artifact (paper-writing-router) or an experiment decision/action (experiment-evidence-router)?

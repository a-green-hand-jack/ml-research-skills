# ml-research-skills

Agent skills for the full ML research workflow: initializing paper and code repos, running experiments, syncing results, updating docs, checking paper readiness, preparing releases, and tagging milestones.

## Install

Install the full collection:

```bash
npx skills add a-green-hand-jack/ml-research-skills
```

Or install a specific skill:

```bash
npx skills add a-green-hand-jack/ml-research-skills --skill init-latex-project
npx skills add a-green-hand-jack/ml-research-skills --skill run-experiment
npx skills add a-green-hand-jack/ml-research-skills --skill remote-project-control
npx skills add a-green-hand-jack/ml-research-skills --skill submit-paper
```

Install globally for both Codex and Claude Code:

```bash
npx skills add a-green-hand-jack/ml-research-skills -g -a codex claude-code -y
```

Install one specific skill globally for both agents:

```bash
npx skills add a-green-hand-jack/ml-research-skills -g -a codex claude-code -s remote-project-control -y
```

With the default local setup used in this repo, Codex installs under `~/.agents/skills/` and Claude Code reads from `~/.claude/skills/`, often via symlinks created by `npx skills`.

## Skills

| Skill | What it does |
|---|---|
| `research-project-memory` | Initialize and maintain hierarchical project memory across claims, evidence, risks, actions, paper, code, worktrees, slides, reviews, and rebuttal |
| `research-idea-validator` | Turn a rough research idea into a pursue/revise/park/kill decision with novelty, feasibility, evidence, and reviewer-risk analysis |
| `init-latex-project` | Scaffold a LaTeX academic paper project with venue-specific templates, macros, and official style files |
| `init-python-project` | Create or enhance a production-ready Python/ML project using `uv`, pytest, black, ruff, and mypy, with remote-workflow memory scaffolding |
| `project-init` | Set up a parent research workspace with aligned `paper/` and `code/` repositories plus `PROJECT.md` |
| `project-sync` | Sync experiment results from the code repo into the paper's `sections/daily_experiments.tex` log |
| `new-workspace` | Create a Git branch or worktree for a new feature or experiment |
| `experiment-design-planner` | Design hypothesis-driven experiments with baselines, ablations, metrics, controls, logging, and stop conditions before running |
| `experiment-report-writer` | Write structured experiment reports from notes, configs, logs, metrics, tables, and figures, with setup, results, interpretation, limitations, and next steps |
| `conference-writing-adapter` | Adapt an ML paper's structure, positioning, and paragraph-level writing to a target conference using venue exemplars and reusable writing memory |
| `paper-reviewer-simulator` | Simulate target-conference reviewers, predicted scores, likely reject reasons, meta-review, and a ranked pre-submission risk register |
| `rebuttal-strategist` | Analyze real reviews, infer reviewer intent, plan rebuttal experiments, draft responses, and track promised revisions |
| `citation-coverage-audit` | Find missing classic, closest, benchmark, and recent concurrent citations before submission |
| `citation-audit` | Run a pre-submission audit of LaTeX citation keys, BibTeX entries, metadata, citation claims, labels, and references |
| `work-timeline-planner` | Build Markdown and/or HTML work timelines from git history, docs, and notes, with Mermaid or richer Gantt visualizations for review and planning |
| `safe-git-ops` | Perform common Git operations with sandbox-aware failure handling and worktree-safe diagnostics |
| `remote-project-control` | Recover project memory and safely coordinate local-to-remote SSH workflows for research repos |
| `run-experiment` | Generate reproducible local, SLURM, or RunAI job scripts and submission commands |
| `submit-paper` | Run a pre-submission checklist for a LaTeX paper, including anonymity, mandatory sections, and optional compile checks |
| `release-code` | Prepare a research code repository for public release with audit, README/LICENSE/CITATION, tagging, and optional GitHub release |
| `add-git-tag` | Create an annotated milestone tag with achievements and next-phase plans |
| `update-docs` | Detect changes since the last docs update and refresh only the affected documentation |

## Lifecycle Categories

These skills are organized around the lifecycle of an ML research project: set up the workspace, run and summarize experiments, shape the paper for submission, handle review and rebuttal, then maintain or release the project.

### 0. Project Memory and Coordination

Use this skill to keep feedback loops between idea, algorithm, experiments, writing, review, and rebuttal coherent across sessions:

| Skill | Lifecycle role |
|---|---|
| **research-project-memory** | Maintain hierarchical memory and claim-evidence-risk-action links across project components |

### 1. Idea Validation and Project Shaping

Use these skills when deciding whether an idea is worth pursuing and how it should become a research project:

| Skill | Lifecycle role |
|---|---|
| **research-idea-validator** | Judge a rough idea with the FIVE+C framework and choose pursue, revise, park, or kill |

### 2. Project and Workspace Setup

Use these skills when starting a project, creating paper/code repositories, or isolating a new line of work:

| Skill | Lifecycle role |
|---|---|
| **project-init** | Create the parent research workspace with aligned `paper/` and `code/` repositories |
| **init-latex-project** | Scaffold the paper repo with venue-aware LaTeX structure |
| **init-python-project** | Scaffold or enhance the code repo with ML project structure and tooling |
| **new-workspace** | Create a branch or worktree for a new feature, experiment, or revision |
| **remote-project-control** | Coordinate local editing with remote execution on SSH/HPC environments |

### 3. Experiment Execution and Evidence Capture

Use these skills while producing the evidence that will support the paper:

| Skill | Lifecycle role |
|---|---|
| **experiment-design-planner** | Design hypotheses, baselines, ablations, controls, metrics, and stop conditions before running |
| **run-experiment** | Launch reproducible local, SLURM, or RunAI experiment jobs |
| **experiment-report-writer** | Turn logs, metrics, configs, tables, and figures into an interpretable report |
| **project-sync** | Record experiment results from the code repo into the paper repo |

### 4. Paper Writing and Pre-Submission Review

Use these skills while turning results into a submission and reducing reviewer risk before the deadline:

| Skill | Lifecycle role |
|---|---|
| **conference-writing-adapter** | Adapt structure, narrative, and paragraph-level writing to a target venue |
| **paper-reviewer-simulator** | Simulate target-conference reviewers and rank likely rejection risks |
| **citation-coverage-audit** | Find missing classic, closest, benchmark, and recent concurrent citations |
| **citation-audit** | Verify existing citation keys, BibTeX metadata, references, and citation claims |
| **submit-paper** | Run final submission readiness checks for format, anonymity, required sections, and compilation |

### 5. Review, Rebuttal, and Revision

Use this stage after real reviews arrive:

| Skill | Lifecycle role |
|---|---|
| **rebuttal-strategist** | Analyze reviews, infer reviewer intent, plan rebuttal experiments, draft responses, and track promised revisions |

### 6. Maintenance, Release, and Retrospective

Use these skills to keep the project understandable, publishable, and easy to hand off:

| Skill | Lifecycle role |
|---|---|
| **update-docs** | Refresh documentation after meaningful code or workflow changes |
| **release-code** | Prepare a public research code release with repo hygiene, README, license, citation, and tagging |
| **work-timeline-planner** | Summarize past work or plan future work from git history, docs, and notes |
| **add-git-tag** | Mark a milestone with an annotated git tag |

### 7. Git Safety

Use this whenever a workflow touches non-trivial Git state:

| Skill | Lifecycle role |
|---|---|
| **safe-git-ops** | Diagnose and perform Git operations safely, especially around worktrees, conflicts, and sandboxed metadata writes |

## Role-Based Categories

The same skills can also be viewed by research role. A single researcher may switch between these roles during a project, but the classification helps choose the right skill for the job at hand.

### Experiment Runner

For the person running experiments, collecting evidence, and making results reproducible:

| Skill | Role support |
|---|---|
| **research-project-memory** | Track evidence, risks, actions, and worktree state across experiment feedback loops |
| **experiment-design-planner** | Convert a claim into a runnable experiment matrix with controls and decision rules |
| **run-experiment** | Launch local, SLURM, or RunAI experiments with reproducible job scripts |
| **experiment-report-writer** | Turn raw logs, metrics, tables, and figures into readable experiment reports |
| **project-sync** | Move experiment findings into the paper repo's experiment log |
| **remote-project-control** | Keep local code and remote execution state aligned |

### Paper Writer

For the person turning research evidence into a submission:

| Skill | Role support |
|---|---|
| **research-project-memory** | Keep paper claims, evidence, figures, sections, and risks aligned |
| **conference-writing-adapter** | Shape the paper around target-conference writing expectations |
| **citation-coverage-audit** | Find missing classic, close, benchmark, and concurrent citations |
| **citation-audit** | Verify citation correctness, BibTeX metadata, and LaTeX references |
| **submit-paper** | Check final submission readiness |

### Reviewer / Internal Critic

For the person stress-testing the paper before reviewers see it:

| Skill | Role support |
|---|---|
| **research-project-memory** | Link simulated reviewer risks to claims, evidence gaps, and concrete actions |
| **paper-reviewer-simulator** | Simulate venue-specific reviewers, predicted scores, likely reject reasons, and meta-review dynamics |
| **citation-coverage-audit** | Detect missing related work that reviewers are likely to complain about |
| **citation-audit** | Check whether cited papers actually support the text's claims |

### Rebuttal Lead

For the person coordinating author response after real reviews arrive:

| Skill | Role support |
|---|---|
| **research-project-memory** | Link real review issues to rebuttal actions, promised revisions, and updated evidence |
| **rebuttal-strategist** | Parse reviews, infer reviewer intent, prioritize issues, plan rebuttal experiments, draft responses, and track promised revisions |
| **run-experiment** | Execute targeted rebuttal experiments or analyses |
| **conference-writing-adapter** | Turn accepted reviewer criticism into paper revisions |

### Project Maintainer / Release Owner

For the person keeping the repo usable, documented, and publishable:

| Skill | Role support |
|---|---|
| **research-project-memory** | Maintain project-level status, decisions, actions, component memory, and closeout summaries |
| **update-docs** | Refresh docs after code or workflow changes |
| **release-code** | Prepare the public research code release |
| **add-git-tag** | Mark milestones with annotated tags |
| **work-timeline-planner** | Summarize work history or plan the next phase |
| **safe-git-ops** | Handle Git operations safely |

### Project Designer

For the person designing the overall research project, repo structure, and collaboration workflow:

| Skill | Role support |
|---|---|
| **research-project-memory** | Define memory layout and component ownership for the full project |
| **research-idea-validator** | Decide whether a rough idea should become a project and what must change before investing |
| **project-init** | Create the initial paper/code workspace |
| **init-latex-project** | Define the paper scaffold and venue template |
| **init-python-project** | Define the code repo structure and tooling |
| **new-workspace** | Isolate new directions, experiments, or revisions |
| **remote-project-control** | Establish local/remote execution conventions |

### Algorithm / Research Idea Designer

This role is partially covered in this repository today. Existing skills help validate ideas and design evidence once a rough claim exists, but there is not yet a dedicated skill for:

- turning a rough algorithmic idea into a precise method
- designing ablations and baselines from first principles
- mapping assumptions, failure modes, and theory/experiment claims

Current partial support:

| Skill | Role support |
|---|---|
| **research-project-memory** | Preserve idea, claim, evidence, risk, and action state across project pivots |
| **research-idea-validator** | Turn a rough idea into a pursue/revise/park/kill decision with novelty, feasibility, and paper-shape analysis |
| **experiment-design-planner** | Designs evidence for a claim once the rough idea exists |

Potential future skills could include **algorithm-design-planner**, **result-diagnosis**, **paper-evidence-board**, or **paper-positioning-planner**.

## Typical Workflow

```text
1. research-project-memory -> initialize or recover hierarchical project memory and feedback-loop state
2. research-idea-validator -> decide whether a rough idea should be pursued, revised, parked, or killed
3. project-init       -> create a parent workspace with paper/ and code/
4. new-workspace      -> isolate a feature or experiment branch
5. remote-project-control -> recover project memory and align local vs remote state
6. experiment-design-planner -> design baselines, ablations, metrics, and stop conditions
7. run-experiment     -> launch locally or on SLURM / RunAI
8. project-sync       -> record results in paper/sections/daily_experiments.tex
9. experiment-report-writer -> turn experiment evidence into a structured report
10. conference-writing-adapter -> reshape the paper for a target venue's reviewer expectations
11. paper-reviewer-simulator -> simulate venue reviewers and rank likely rejection risks
12. citation-coverage-audit -> find missing classic, close, and concurrent citations
13. citation-audit  -> verify citations, BibTeX metadata, and LaTeX references before submission
14. submit-paper    -> run a readiness check before a deadline
15. rebuttal-strategist -> analyze real reviews and draft strategic rebuttals
16. work-timeline-planner -> summarize recent work or draft the next-phase timeline
17. update-docs     -> refresh docs after meaningful code changes
18. release-code    -> prepare the public code release when needed
19. add-git-tag     -> mark a milestone
```

## What `research-project-memory` Provides

- Hierarchical project memory across `memory/`, component `.agent/` folders, and worktree status files
- Claim-evidence-risk-action tracking with stable IDs such as `CLM-001`, `EVD-001`, `RSK-001`, and `ACT-001`
- Templates for project boards: claims, evidence, risks, actions, decisions, current status, and component index
- Consistency checks for unsupported claims, stale evidence, reviewer risks without actions, rebuttal promises, and worktrees without exit conditions
- A shared writeback protocol for other skills after idea validation, experiment design, runs, writing, review simulation, and rebuttal
- Integration guidance in core research-loop skills so results, reviews, citations, rebuttals, and remote runs can update the same project memory graph

## What `research-idea-validator` Provides

- Early-stage idea validation using the FIVE+C framework: framing, importance, validity, evidence, execution, and competition
- A clear decision label: pursue, revise, park, or kill
- Paper-shape analysis for method, theory, benchmark, empirical analysis, systems, application, negative-result, and position-style ideas
- Minimum viable project, killer experiment or analysis, reviewer attack forecast, kill criteria, and next actions
- Memory guidance for preserving promising, parked, revised, or killed ideas across sessions

## What `init-latex-project` Provides

- A complete LaTeX paper scaffold with `main.tex`, `macros.tex`, and a writing guide for agents
- Venue-specific templates for `icml`, `acl`, `emnlp`, `naacl`, `iccv`, `eccv`, `neurips`, `iclr`, `cvpr`, and `acm`
- Support for generic non-venue projects by using the default template without `--venue`
- A helper script that downloads official style files where needed and writes `venue_preamble.tex`

## What `init-python-project` Provides

- A four-layer ML project structure: `src/`, `experiments/`, `eval/`, and `infra/`
- `uv`-based Python project setup with editable installs
- Development tooling: pytest, black, ruff, and mypy
- Project docs scaffolding under `docs/`
- Remote workflow bootstrap files under `infra/remote-projects.yaml`, `docs/ops/`, and `.agent/`
- Editor configuration for Claude Code / Cursor / VS Code

## What `remote-project-control` Provides

- A repo-native memory model for projects developed locally but executed remotely over SSH
- Shared and private memory files for server mappings, working status, and local overrides
- Safe orchestration for inspect, sync, remote job submission, monitoring, and artifact lookup
- A clean handoff layer between project memory and `run-experiment`

## What `work-timeline-planner` Provides

- Evidence-based timeline synthesis from git commits, docs, notes, and user-provided chat excerpts
- Markdown and/or standalone HTML reports that can be kept privately or shared upward
- Mermaid Gantt charts for lightweight repo-native reports and richer HTML timelines when needed
- A clean split between observed work blocks and inferred or planned work

## What `experiment-report-writer` Provides

- A structured report format for experiment motivation, setup, methods, metrics, results, interpretation, conclusions, limitations, and next steps
- Guidance for explaining figures and tables, including axes, legends, units, scales, and error bars
- Evidence-first writing that distinguishes measured results from interpretation and marks missing reproducibility details
- Audience-aware output for lab notes, mentor updates, paper sections, or presentation-ready summaries

## What `experiment-design-planner` Provides

- Claim-first experiment planning before using compute
- Hypothesis, alternative explanation, falsification, and decision-rule templates
- Baseline, control, nuisance-variable, metric, seed, repeat, and logging requirements
- Ablation matrix guidance for isolating components and avoiding multi-variable confounds
- Reviewer-risk checks that ask whether the planned evidence will satisfy paper or rebuttal expectations

## What `conference-writing-adapter` Provides

- Conference-aware paper restructuring for venues such as NeurIPS, ICML, ICLR, CVPR, ACL, and EMNLP
- A workflow for learning from accepted, oral, spotlight, or best-paper exemplars without copying their text
- Paper archetype diagnosis for method, empirical study, benchmark, theory, systems, analysis, and application papers
- Section-level and paragraph-level rewrite blueprints that assign each paragraph a reviewer-facing function
- Project-local writing memory under `.agent/conference-writing/` for venue patterns, exemplar notes, and current-paper style decisions

## What `paper-reviewer-simulator` Provides

- Venue-specific shadow reviews for ML/AI conferences such as NeurIPS, ICML, ICLR, CVPR, ACL, and EMNLP
- Dynamic learning from official reviewer guidelines, OpenReview discussions, example reviews, and accepted-paper patterns
- Multi-reviewer panels with technical, skeptical generalist, empirical/reproducibility, related-work, and area-chair perspectives
- Predicted decision, score/confidence estimates, likely reviewer questions, rebuttal readiness, and an actionable risk register
- Project-local memory under `.agent/reviewer-simulator/` for venue review patterns, example notes, and current-paper risks

## What `rebuttal-strategist` Provides

- OpenReview-aware review extraction, thread state tracking, and source logging for real reviews and discussion rounds
- Reviewer intent analysis that distinguishes champions, persuadable reviewers, skeptical reviewers, and likely rejects
- Issue boards that turn review comments into ranked must-win, must-answer, experiment-needed, and paper-revision tasks
- Targeted rebuttal experiment planning with success, partial-success, failure, and out-of-scope response wording
- Evidence-first rebuttal drafting, follow-up reply preparation, decision-path analysis, and promised-revision tracking
- Project-local memory under `.agent/rebuttal-strategy/` for reviews, issue boards, experiments, drafts, and final outcomes

## What `citation-coverage-audit` Provides

- A pre-submission scan for missing foundational classics, closest prior work, direct competitors, benchmark/data/metric sources, and recent concurrent papers
- Search protocols for arXiv, OpenReview, proceedings, ACL Anthology, PMLR, CVF, Semantic Scholar, DBLP, and venue-specific sources
- Risk classification for missing citations that could undermine novelty, baselines, theory claims, or related work coverage
- Suggested insertion points and novelty-framing changes for must-cite and should-cite papers
- Project-local memory under `.agent/citation-coverage/` for topic citation maps, search dates, and intentionally excluded papers

## What `citation-audit` Provides

- Local deterministic checks for LaTeX `\cite{}` keys, BibTeX entries, duplicate keys, labels, and cross-references
- Metadata verification guidance for DOI, arXiv, OpenReview, proceedings, publisher, and venue information
- Citation-claim auditing to check whether cited papers actually support nearby prose
- A pre-submission report format that separates blocking issues, important issues, warnings, and unresolved author decisions

## What `run-experiment` Provides

- Reproducible job templates under `jobs/` for local runs, SLURM clusters, and RunAI/Kubernetes
- A shared `environments.yaml` registry for cluster-specific defaults
- Built-in support for:
  - `local`
  - `ibex` (KAUST SLURM)
  - `uw` (placeholder SLURM profile to customize)
  - `runai` (EPFL RunAI / Kubernetes)

## What `submit-paper` Checks

- Submission mode in `venue_preamble.tex`
- Drafting artifacts such as TODOs and comment macros
- Venue-specific required sections and bibliography presence
- Basic anonymity issues for blind review
- Optional compile checks and page-count sanity checks

## What `release-code` Provides

- A release audit for secrets, large files, and missing repo hygiene
- Templates for `README.md` and `CITATION.cff`
- License generation guidance
- A structured tagging and publishing flow for public code releases

## Contributors

- Jieke
- Claude Code
- Codex

## Validation

There are no automated tests in this repository. For a quick repository sanity check, run:

```bash
python3 scripts/validate_skills.py
```

This validator checks frontmatter parsing, skill-directory name alignment, helper-file references, hardcoded Claude-only skill paths, text-template placeholder format, skill inventory consistency in the top-level docs, and basic Python/shell syntax for helper scripts.

For the `init-python-project` scaffold smoke test, run:

```bash
python3 -m unittest -v tests.test_init_python_project_scaffold
```

To validate a skill end-to-end:

1. Install the skill into the target agent runtime with `npx skills add`, for example `npx skills add a-green-hand-jack/ml-research-skills -g -a codex claude-code -s <skill-name> -y`
2. Invoke it in the corresponding agent with a matching request
3. Inspect the generated files, commands, or instructions and iterate

## Requirements

- [Claude Code](https://claude.ai/code) or another compatible agent runtime
- [npx skills](https://github.com/vercel-labs/skills)
- For Python-related skills: [uv](https://docs.astral.sh/uv/)
- For LaTeX-related skills: a TeX distribution such as TeX Live or MiKTeX

# AGENTS.md

Guidance for AI coding agents working in this repository.

## Repository Overview

This repo is **ml-research-skills** — a collection of agent skills for ML researchers. Each skill lives under `skills/<skill-name>/` as an instruction bundle centered on `SKILL.md`, with optional `scripts/` and `templates/` directories.

Skills in this repo are installed with:

```bash
npx skills add a-green-hand-jack/ml-research-skills
```

To install globally for both Codex and Claude Code:

```bash
npx skills add a-green-hand-jack/ml-research-skills -g -a codex claude-code -y
```

To install one specific skill globally for both agents:

```bash
npx skills add a-green-hand-jack/ml-research-skills -g -a codex claude-code -s remote-project-control -y
```

These files are primarily agent instructions and templates, not an application with automated runtime tests.

## Current Repository Structure

```text
ml-research-skills/
├── README.md
├── CLAUDE.md
├── AGENTS.md
└── skills/
    ├── add-git-tag/
    │   └── SKILL.md
    ├── research-project-memory/
    │   ├── SKILL.md
    │   ├── references/
    │   └── templates/
    ├── research-idea-validator/
    │   ├── SKILL.md
    │   └── references/
    ├── literature-review-sprint/
    │   ├── SKILL.md
    │   └── references/
    ├── algorithm-design-planner/
    │   ├── SKILL.md
    │   └── references/
    ├── init-latex-project/
    │   ├── SKILL.md
    │   ├── scripts/
    │   └── templates/
    ├── init-python-project/
    │   └── SKILL.md
    ├── new-workspace/
    │   └── SKILL.md
    ├── experiment-design-planner/
    │   ├── SKILL.md
    │   └── references/
    ├── baseline-selection-audit/
    │   ├── SKILL.md
    │   └── references/
    ├── result-diagnosis/
    │   ├── SKILL.md
    │   └── references/
    ├── experiment-report-writer/
    │   ├── SKILL.md
    │   └── templates/
    ├── advisor-update-writer/
    │   ├── SKILL.md
    │   └── references/
    ├── research-slide-deck-builder/
    │   └── SKILL.md
    ├── figure-results-review/
    │   ├── SKILL.md
    │   └── references/
    ├── table-results-review/
    │   └── SKILL.md
    ├── paper-evidence-board/
    │   ├── SKILL.md
    │   └── references/
    ├── paper-positioning-planner/
    │   ├── SKILL.md
    │   └── references/
    ├── conference-writing-adapter/
    │   ├── SKILL.md
    │   └── references/
    ├── abstract-title-contribution-writer/
    │   ├── SKILL.md
    │   ├── references/
    │   └── templates/
    ├── experiment-story-writer/
    │   ├── SKILL.md
    │   ├── references/
    │   └── templates/
    ├── limitations-scope-writer/
    │   ├── SKILL.md
    │   ├── references/
    │   └── templates/
    ├── method-section-explainer/
    │   ├── SKILL.md
    │   ├── references/
    │   └── templates/
    ├── paper-introduction-argument-writer/
    │   ├── SKILL.md
    │   ├── references/
    │   └── templates/
    ├── paper-draft-consistency-editor/
    │   ├── SKILL.md
    │   ├── references/
    │   └── templates/
    ├── paper-writing-contract-planner/
    │   ├── SKILL.md
    │   ├── references/
    │   └── templates/
    ├── paper-writing-assistant/
    │   ├── SKILL.md
    │   └── references/
    ├── related-work-positioning-writer/
    │   ├── SKILL.md
    │   ├── references/
    │   └── templates/
    ├── paper-reviewer-simulator/
    │   ├── SKILL.md
    │   └── references/
    ├── rebuttal-strategist/
    │   ├── SKILL.md
    │   └── references/
    ├── camera-ready-finalizer/
    │   ├── SKILL.md
    │   └── references/
    ├── artifact-evaluation-prep/
    │   ├── SKILL.md
    │   └── references/
    ├── citation-coverage-audit/
    │   ├── SKILL.md
    │   └── references/
    ├── citation-audit/
    │   ├── SKILL.md
    │   ├── references/
    │   └── scripts/
    ├── work-timeline-planner/
    │   ├── SKILL.md
    │   ├── references/
    │   └── templates/
    ├── project-init/
    │   └── SKILL.md
    ├── project-sync/
    │   └── SKILL.md
    ├── safe-git-ops/
    │   ├── SKILL.md
    │   └── references/
    ├── remote-project-control/
    │   ├── SKILL.md
    │   ├── references/
    │   ├── template_manifest.json
    │   └── templates/
    ├── release-code/
    │   ├── SKILL.md
    │   ├── checklist.md
    │   └── templates/
    ├── skill-system-auditor/
    │   ├── SKILL.md
    │   └── references/
    ├── run-experiment/
    │   ├── SKILL.md
    │   ├── environments.yaml
    │   └── templates/
    ├── submit-paper/
    │   ├── SKILL.md
    │   └── scripts/
    └── update-docs/
        └── SKILL.md
```

## Current Skill Set

| Skill | Purpose |
|---|---|
| `research-project-memory` | Initialize and maintain hierarchical memory across claims, evidence, risks, actions, paper, code, worktrees, slides, reviewer simulation, and rebuttal |
| `research-idea-validator` | Turn a rough research idea into a pursue/revise/park/kill decision using novelty, feasibility, evidence, and reviewer-risk analysis |
| `literature-review-sprint` | Build a ranked literature map with canonical, closest, recent, baseline, and positioning implications for a topic or project direction |
| `algorithm-design-planner` | Turn a promising research idea into a concrete method design with formulation, mechanism, assumptions, ablations, and implementation handoff |
| `init-latex-project` | Initialize a LaTeX paper project with venue-specific templates, macros, and downloaded style files |
| `init-python-project` | Create or enhance a production-ready Python/ML code repo using `uv`, with code-side evidence docs and remote workflow memory |
| `project-init` | Create a research project control root with independent paper/code/slides repos, shared memory, optional GitHub Project board linkage, root project docs, root agent guidance, and code/paper worktree policy |
| `project-sync` | Sync experiment results from the code repo into the paper's `daily_experiments.tex` |
| `new-workspace` | Create a Git branch or project-aware component worktree for code experiments, baselines, rebuttal fixes, paper venue versions, arXiv releases, and camera-ready paper versions |
| `experiment-design-planner` | Design hypothesis-driven experiments with baselines, ablations, metrics, controls, logging, and stop conditions before running |
| `baseline-selection-audit` | Audit whether experimental baselines are necessary, fair, current, and reviewer-proof before running or writing comparisons |
| `result-diagnosis` | Diagnose surprising, negative, unstable, or ambiguous experiment results and choose the next project action |
| `experiment-report-writer` | Write structured experiment reports from notes, configs, logs, metrics, tables, and figures |
| `advisor-update-writer` | Write decision-oriented advisor, mentor, lab meeting, or collaborator updates from evidence, risks, options, asks, and next actions |
| `research-slide-deck-builder` | Design and write research slide decks for advisor, lab, progress, reading, proposal, and conference talks using the external `progress-slides` template |
| `figure-results-review` | Review figure assets, LaTeX figure wrappers, plots, captions, visual descriptions, and paper visual style for claim support and reviewer risk |
| `table-results-review` | Review standalone `tables/*.tex` files, table captions, table descriptions, row/column semantics, numeric provenance, and experiment settings |
| `paper-evidence-board` | Maintain a paper-facing board aligning claims, evidence, figures, sections, reviewer risks, and next actions |
| `paper-positioning-planner` | Decide the paper's primary contribution, claim scope, archetype, target audience, novelty framing, and claims to avoid before venue-specific writing |
| `conference-writing-adapter` | Adapt an ML paper's structure, positioning, and paragraph-level writing to a target conference using venue exemplars and reusable writing memory |
| `abstract-title-contribution-writer` | Draft and revise titles, abstracts, and contribution lists so the paper's top-level promise matches venue, positioning, claims, and evidence |
| `experiment-story-writer` | Turn experiment tables, figures, ablations, mixed results, and provisional metrics into claim-aware results prose |
| `limitations-scope-writer` | Plan, draft, and revise limitations, scope, failure cases, ethics, broader impact, and conclusion caveats as claim-boundary control |
| `method-section-explainer` | Plan, draft, and revise method sections for notation flow, module ordering, overview figures, algorithm boxes, design rationales, and appendix boundaries |
| `paper-introduction-argument-writer` | Plan, draft, and revise introductions as venue-aware argument chains with hook, gap, insight, method, evidence, and contribution paragraph roles |
| `paper-draft-consistency-editor` | Audit and edit a paper draft for internal consistency across title, abstract, intro, method, results, figures, tables, captions, terminology, limitations, and conclusion |
| `paper-writing-contract-planner` | Create or update a writing contract that locks paper archetype, section order, paragraph roles, claim evidence slots, figure/table jobs, and forbidden claims before drafting |
| `paper-writing-assistant` | Draft and revise claim-aware paper prose, map archetypes to required evidence slots, use micro-patterns for captions and paragraph-level writing, and track provisional result placeholders until verified evidence arrives |
| `related-work-positioning-writer` | Plan, draft, and revise related work as novelty-boundary writing, grouping closest work and defining safe citation-backed boundary statements |
| `paper-reviewer-simulator` | Simulate target-conference reviewers, predicted scores, likely reject reasons, meta-review, rebuttal risks, and a ranked pre-submission risk register |
| `rebuttal-strategist` | Analyze real reviews, infer reviewer intent, plan rebuttal experiments, draft responses, and track promised revisions |
| `camera-ready-finalizer` | Finalize an accepted paper by checking rebuttal promises, de-anonymization, final claims/evidence, supplement consistency, submission package, and release handoff |
| `artifact-evaluation-prep` | Prepare artifact evaluation packages, reviewer-facing reproduction instructions, smoke tests, manifests, and claim-to-artifact maps |
| `citation-coverage-audit` | Find missing classic, closest, benchmark, and recent concurrent citations before submission |
| `citation-audit` | Run a pre-submission audit of LaTeX citation keys, BibTeX entries, metadata, citation claims, labels, and references |
| `work-timeline-planner` | Build Markdown or HTML timeline reports with Gantt-style visualizations from git history, docs, notes, and user context |
| `safe-git-ops` | Perform common Git operations safely with better worktree and sandbox failure diagnosis |
| `remote-project-control` | Recover project memory and safely coordinate local, Git remote, and SSH/HPC/RunAI server workflows |
| `run-experiment` | Generate reproducible local / SLURM / RunAI job scripts and submission commands |
| `submit-paper` | Run a pre-submission readiness check for a LaTeX paper project |
| `release-code` | Prepare and publish a research code repository for public release |
| `add-git-tag` | Create an annotated milestone tag with achievements and next-phase plans |
| `update-docs` | Detect code changes since the last docs update and refresh affected documentation |
| `skill-system-auditor` | Audit the skill collection for inventory, lifecycle, routing, memory-writeback, documentation, and validation consistency |

## Adding or Updating a Skill

Skills live in `skills/<skill-name>/` and must include a `SKILL.md` with YAML frontmatter:

```markdown
---
name: skill-name
description: One sentence describing when to use this skill. Include trigger phrases.
allowed-tools: Read, Write, Edit, Bash, Glob
---

# Skill Title

Brief description.

## When to Use This Skill
...

## Steps
...
```

Guidelines:
- The directory name must exactly match the `name` field.
- `name` must use lowercase letters, numbers, and hyphens only.
- Keep `SKILL.md` under 500 lines; move large references into linked files.
- Use `scripts/` for shell automation so the agent can run commands without embedding large shell blocks inline.
- Use `templates/` for files the skill writes into user projects.
- Write the `description` as a routing rule, not a title. Agents use it to decide when to activate the skill.
- Keep examples and venue/tooling references aligned with the actual templates and scripts shipped in the same skill directory.

## Validation

There are no automated tests in this repository. Before manual validation, run the local repository sanity check:

```bash
python3 scripts/validate_skills.py
```

This covers frontmatter, helper references, top-level skill inventory consistency, template placeholder format, and basic Python/shell syntax.

For the `init-python-project` scaffold smoke test, run:

```bash
python3 -m unittest -v tests.test_init_python_project_scaffold
```

Then validate changes by exercising the skill in the target agent runtime:

1. Install the skill with `npx skills add`, such as `npx skills add a-green-hand-jack/ml-research-skills -g -a codex claude-code -s <skill-name> -y`
2. Invoke it by describing a matching task
3. Check that the generated instructions, scripts, and templates behave as intended

## Notes for Agents

- Prefer updating the minimum set of files needed when a skill changes.
- If you change a skill's behavior, also check whether `README.md` and `CLAUDE.md` now need corresponding updates.
- Treat `SKILL.md`, helper scripts, and templates as a single unit; avoid documenting behavior that the shipped assets do not actually support.

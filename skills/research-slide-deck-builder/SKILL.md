---
name: research-slide-deck-builder
description: Help a researcher design and write reusable research slide decks for advisor updates, lab meetings, paper reading reports, progress reports, proposal talks, conference talks, or thesis-style presentations. Use this skill when the user asks to make slides, write a slide deck, structure PPT/Slidev content, use the progress-slides template, or decide what each slide should contain.
allowed-tools: Read, Write, Edit, Bash, Glob
---

# Research Slide Deck Builder

## Purpose

Turn research content into a clear slide deck: story, slide order, page-level layout, figure placement, speaker notes, and the actual deck source.

This skill should use the external `progress-slides` template repo as the preferred implementation scaffold for progress, advisor, lab, and research-update decks:

```text
https://github.com/a-green-hand-jack/progress-slides.git
```

Do not duplicate that template inside this skill. Treat it as an external slides component or project template that should be cloned, inspected, installed, and edited in the user's project.

Use `presentation-dry-run` later when the user already has slides and wants timing, spoken transitions, rehearsal, or Q&A practice.

## When to Use

- The user needs slides for an advisor meeting, lab meeting, group update, paper reading report, conference talk, proposal, or defense segment.
- The user asks what the deck should look like, how many slides to make, what title page to use, or how to structure each page.
- The user asks to use `progress-slides` or a reusable slides template.
- A `project-init` project has a `slides/` component that needs content, setup, or maintenance.
- Research notes, figures, experiment reports, or project memory need to become a presentation.

## Template Policy

- Prefer `progress-slides` for research progress, advisor, lab, and project-update decks unless the user explicitly asks for another format.
- Keep template code upstream. Do not reimplement its CSS, components, theme, package config, or build pipeline in this skill.
- Before editing, inspect the cloned template's `README.md`, `package.json`, and existing slide source files because the external repo is the source of truth.
- If the repository is private or temporarily unavailable, record that blocker and still produce a deck outline or Markdown source that can be moved into the template later.
- If the user is inside a project-control-root layout, put or connect the template at `<ProjectName>/slides/` as an independent component repo.

## Installing or Connecting `progress-slides`

For a new slides component:

```bash
git clone https://github.com/a-green-hand-jack/progress-slides.git slides
cd slides
```

Then inspect the template:

```bash
ls
cat README.md
cat package.json
```

Install dependencies using the package manager indicated by the template lockfile or README. If there is no stronger local instruction, use:

```bash
npm install
```

Run the local preview command from `package.json`. Common Slidev-style commands are:

```bash
npm run dev
npx slidev
```

For an existing project:

- If `slides/` already exists and is the template repo, edit it in place.
- If `slides/` exists but is not the template, ask whether to migrate, add `progress-slides` as a new independent repo, or only write a compatible outline.
- If the template uses Git, preserve its history and use normal Git operations from inside `slides/`.

## Deck Design Principles

- One slide, one job. Every slide needs a sentence-level takeaway.
- Make the audience path explicit: context -> question -> evidence -> decision.
- For advisor updates, prioritize decisions, blockers, and evidence over polished storytelling.
- For research talks, prioritize motivation, problem framing, method intuition, and result interpretation.
- Figures are evidence, not decoration. Explain axes, setup, and takeaway.
- Keep slide titles specific. Avoid generic titles like "Results", "Method", or "Experiments".
- Put dense details in backup slides instead of shrinking text.

## Workflow

### 1. Identify Presentation Type

Determine:

- audience: advisor, lab, committee, conference, interview, or class
- time limit
- goal: feedback, progress report, teaching, persuasion, or defense
- single most important takeaway
- available material: memory, notes, figures, reports, paper draft, code results, or existing slides

### 2. Choose the Deck Archetype

Use the closest archetype.

Advisor update deck:

1. Title / meeting goal
2. Last commitments
3. Progress summary
4. Key result or evidence
5. What is solved
6. What is stuck
7. Options / decision needed
8. Next-week plan

Lab meeting research update:

1. Title
2. Problem and motivation
3. Current research question
4. Method or setup
5. Experimental setup
6. Main result
7. Ablation / analysis
8. Limitation or failure case
9. Next steps and questions

Paper reading report:

1. Title: paper and why it matters
2. One-sentence contribution
3. Problem setting
4. Method overview
5. Key technical idea
6. Main experiments
7. Strengths
8. Weaknesses / assumptions
9. Relevance to the user's project
10. Discussion questions

Conference-style talk:

1. Title
2. Motivation
3. Problem
4. Gap in prior work
5. Method intuition
6. Method details
7. Experimental setup
8. Main result
9. Analysis / ablation
10. Limitations
11. Takeaway

### 3. Write Template-Compatible Source

After inspecting `progress-slides`, write in the format the template already uses. For Slidev-style Markdown, prefer this pattern:

```markdown
---
theme: default
title: Project Progress Update
---

# Specific Takeaway Title

- Evidence or status point
- Decision or implication

<!--
Speaker note: what to say in 20-40 seconds.
-->

---

# Main Result Supports the Current Claim

<figure-or-table-placeholder>

- Setup:
- Metric:
- Interpretation:
```

Keep speaker notes close to the slide source when the template supports notes. Keep image paths relative to the slide deck so the deck can be moved or shared.

### 4. Use Project Evidence Correctly

- Pull stable figures from `code/docs/results/`, `code/docs/reports/`, paper figures, or user-provided assets.
- Do not copy raw logs, huge outputs, checkpoints, or wandb/tensorboard caches into the slides repo.
- If a figure is stale, unclear, or too dense, use `figure-results-review` before finalizing the deck.
- If slide claims diverge from the paper or project status, update `memory/` or `slides/.agent/` with the risk.

### 5. Produce a Slide Plan Before Heavy Editing

For each slide, write:

- slide number
- slide type
- takeaway title
- visual/evidence needed
- bullets or diagram content
- speaker note
- risk: what may confuse the audience

If a slide has no takeaway, merge it, cut it, or move it to backup.

### 6. Validate the Deck

Before finishing:

- run the template's preview/build command when dependencies are available
- confirm the deck opens locally
- check that all image paths resolve
- check that text is readable in 16:9 presentation view
- check that each result slide explains setup, metric, and interpretation
- update `slides/.agent/` with deck purpose, audience, source evidence, stale evidence risks, and follow-up actions when using a project-control-root layout

## Output Shape

For a planning-only request, produce:

```markdown
# Research Slide Deck Plan - [Deck Name]

## Context
- Audience:
- Time limit:
- Goal:
- One takeaway:
- Template: progress-slides

## Slide Plan
| # | Type | Takeaway title | Visual/evidence | Speaker note | Risk |
|---:|---|---|---|---|---|

## Required Assets
- [ ] [figure/table/diagram]

## Decision Points
1. [Decision/question]

## Backup Slides
- [Backup topic]
```

For an implementation request, edit the actual `slides/` source files in the cloned `progress-slides` repo and report the changed paths plus the preview/build command used.

## Do Not

- Do not create a separate in-skill slide template.
- Do not redesign the external template unless the user asks to modify the template itself.
- Do not make a deck of status bullets without evidence or decisions.
- Do not force a conference-talk narrative onto an advisor update.
- Do not overpack slides because the user is afraid to leave things out.

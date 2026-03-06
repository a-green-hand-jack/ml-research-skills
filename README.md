# ml-research-skills

Claude Code skills for the full lifecycle of ML research projects — from initializing a paper+code workspace to syncing experiment results and tagging milestones.

## Install

```bash
npx skills add a-green-hand-jack/ml-research-skills
```

Or install specific skills:

```bash
npx skills add a-green-hand-jack/ml-research-skills --skill init-latex-project
npx skills add a-green-hand-jack/ml-research-skills --skill project-init
```

## Skills

| Skill | What it does |
|---|---|
| `init-latex-project` | Scaffold a LaTeX paper project for ICLR, CVPR, ICML, ACM, ACL, or arXiv |
| `init-python-project` | Create a production-ready Python/ML project with uv, pytest, ruff, mypy |
| `project-init` | Set up a full research project: `paper/` (LaTeX) + `code/` (Python) + `PROJECT.md` |
| `project-sync` | Log experiment results from the code repo into the paper's daily experiments section |
| `new-workspace` | Create a git branch or worktree with UV env sync and IDE config copying |
| `add-git-tag` | Create an annotated milestone tag with achievements and next-phase plans |
| `update-docs` | Detect code changes since the last docs commit and update only the affected docs |

## Typical Workflow

```
1. project-init       → create paper/ + code/ repos under a shared parent
2. new-workspace      → isolate each experiment in its own worktree
3. (run experiments)
4. project-sync       → log results into paper/sections/daily_experiments.tex
5. update-docs        → refresh code documentation
6. add-git-tag        → mark the milestone
```

## What `init-latex-project` Creates

- Venue-specific `main.tex` (correct document class and bibliography style)
- Full math macro library (`macros.tex`): calligraphic, bold, blackboard bold, operators, theorem environments
- Standard section files: abstract, intro, related, method, exp, conclusion, appendix
- Empty `bib/refs.bib`

Supported venues: `iclr`, `cvpr`, `icml`, `acm`, `acl`, or generic arXiv.

## What `init-python-project` Creates

- `src/` layout with editable install via `uv`
- Isolated `tests/` structure mirroring `src/`
- `docs/` with three layers: `outlines/` (planning), `dev/` (features), `src/` (modules)
- Dev tooling: pytest, black, ruff, mypy
- `.env` / `.env.example`, VSCode/Cursor/Claude settings

## Requirements

- [Claude Code](https://claude.ai/code)
- [npx skills](https://github.com/vercel-labs/skills)
- For Python skills: [uv](https://docs.astral.sh/uv/)
- For LaTeX skills: a TeX distribution (TeX Live or MiKTeX)

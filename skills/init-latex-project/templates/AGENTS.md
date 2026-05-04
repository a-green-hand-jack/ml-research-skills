# AGENTS.md - AI Agent Writing Guide for This LaTeX Project

This file is the universal/Codex entrypoint for agents working on this paper. `CLAUDE.md` is the Claude Code entrypoint. Keep both files semantically aligned.

This file is agent-private by default. If this branch is linked to Overleaf, visible to coauthors, uploaded to a submission system, or prepared for arXiv/camera-ready source, keep `AGENTS.md`, `CLAUDE.md`, `.agent/`, raw CSVs, internal result docs, plotting scripts, and reviewer notes out of the visible source. Use a private worktree or root project memory for agent state.

## Compile Workflow

Do not assume local TeX Live, MacTeX, `pdflatex`, `xelatex`, or `lualatex` is installed. The default workflow is local edit -> Git diff review -> GitHub push when requested -> Overleaf compile through GitHub sync.

Use Overleaf logs and PDF preview as the compile source of truth unless the user explicitly asks for local compilation.

## Source Formatting

If `tex-fmt` is installed, use it as the default LaTeX source-format check:

```bash
tex-fmt --check --nowrap --recursive .
```

Do not run formatting silently during submission or release checks. When formatting is requested, run:

```bash
tex-fmt --nowrap --recursive .
```

Then review the diff before committing or pushing. Use a project-local `tex-fmt` config if one exists; otherwise keep `--nowrap` so routine formatting does not reflow long prose lines.

## Paper Version Worktrees

If this paper belongs to a project control root, paper versions may live in sibling worktrees under `../paper-worktrees/`.

Use paper worktrees for different conference templates, arXiv/preprint releases, camera-ready versions, and paper-only rebuttal edits. Public-source versions such as arXiv must not contain internal notes, TODOs, reviewer notes, author comments, private paths, or internal figure/table descriptions in released `.tex` source.

If `main` syncs to Overleaf through GitHub, treat it as `author-visible`, not private. Only keep collaborator-safe paper source and paper-facing assets there.

## Writing Rules

- Check `macros.tex` before writing math symbols, operators, or theorem environments.
- Use `\cref{...}` for figures, tables, sections, theorems, and algorithms.
- Use `\eqref{...}` for equations.
- Keep figure captions, table captions, internal visual/table descriptions, provenance, and main-text callouts conceptually separate.
- Store internal figure/table descriptions and provenance in `.agent/` or project memory, not in public LaTeX comments.
- Store raw CSVs, result inventories, provenance ledgers, and plotting scripts outside author-visible/public paper source unless explicitly cleaned for release.
- Keep venue mode, anonymity, acknowledgement, checklist, limitations, and source hygiene requirements consistent with the active submission target.

## Detailed Local Policy

Also follow `CLAUDE.md` in this directory for the full paper-local writing guide. If `AGENTS.md` and `CLAUDE.md` disagree, stop and ask which policy should be canonical before editing.

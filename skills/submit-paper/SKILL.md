---
name: submit-paper
description: Pre-submission checklist for LaTeX academic papers. Use when the user wants to submit a paper, check submission readiness, prepare camera-ready, switch to final mode, or verify a paper is ready for a conference deadline.
argument-hint: "[project-dir] [--venue <venue>] [--mode <anonymous|camera-ready|arxiv>] [--compile]"
allowed-tools: Read, Edit, Bash, Glob, Grep
---

# Submit Paper — Pre-Submission Checklist

Run a systematic readiness check on a LaTeX paper project before submitting to a conference. Covers submission mode, mandatory sections, drafting artifacts, bibliography, anonymity, and optional compilation.

Do not assume the local machine has TeX Live, MacTeX, or another LaTeX distribution installed. Many macOS research workflows edit locally, sync through GitHub, and compile on Overleaf. If `pdflatex`, `xelatex`, or `lualatex` is missing, do not ask the user to install TeX unless they explicitly want local compilation. Use static checks locally and route compile/page-count verification through the GitHub-linked Overleaf project.

Paper versions may live in separate worktrees. If the project has `paper-worktrees/`, prefer checking the specific version worktree for the target venue, arXiv release, or camera-ready submission rather than mutating the main `paper/` branch.

---

## Step 1 — Locate the LaTeX project

// turbo
Find the paper directory:

```bash
# If we're inside a project-init project, look for paper/ sibling
git rev-parse --show-toplevel 2>/dev/null
ls "$(git rev-parse --show-toplevel 2>/dev/null)/../" 2>/dev/null || true

# Find main.tex
find . -maxdepth 3 -name "main.tex" 2>/dev/null | head -5
```

Determine `$PAPER_DIR` — the directory containing `main.tex`.

If `$ARGUMENTS` provides a path, use it directly.
If in a `project-init` project structure, check for `paper/` sibling.
If the requested target is a venue retarget, arXiv release, or camera-ready version, also check for a matching `paper-worktrees/` sibling.

---

## Step 2 — Ask for submission context

Ask the user **in a single message**:

1. **Submission type**: Initial submission (anonymous) / Camera-ready / arXiv preprint?
2. **Deadline**: When is the deadline? (helps prioritize what to fix)
3. **Compile workflow**: Is this paper compiled locally or in Overleaf through GitHub? If unknown, assume Overleaf/GitHub for macOS users.
4. **Version workspace**: Is this the main `paper/` repo or a `paper-worktrees/` version for a specific venue/arXiv/camera-ready target?
5. **Source visibility**: Is this source `agent-private`, `author-visible` through Overleaf/coauthors, `anonymous-submission`, `public-preprint`, `camera-ready-public`, or `publisher-artifact`?

If venue can be inferred from `venue_preamble.tex` (Step 3 will read it), skip asking.

Wait for the answer before proceeding.

---

## Step 3 — Run the check script

// turbo

```bash
bash <submit-paper-skill-dir>/scripts/check.sh "$PAPER_DIR" [--compile]
```

**Important**: Resolve `<submit-paper-skill-dir>` as the installed directory for this skill and use the absolute path to `check.sh`.

Only pass `--compile` when a local LaTeX compiler exists or the user explicitly asked for a local compile attempt. If no compiler exists, run the script without `--compile`; it still performs the useful static checks.

The script performs:
| Check | What it looks for |
|---|---|
| Project detection | `main.tex` present, venue from `venue_preamble.tex` |
| Drafting artifacts | `\todo`, `\fixme`, `\red{}`, author comment macros, TODO/FIXME text |
| Anonymity | Acknowledgements, funding disclosures, personal URLs/emails |
| Bibliography | `.bib` file non-empty, `\bibliography{}` call present |
| Mandatory sections | Venue-specific required sections (see below) |
| Abstract length | ~30–350 words (warns outside range) |
| Figures & tables | All `\label{fig:*}` and `\label{tab:*}` are `\ref`'d |
| Compilation | optional local LaTeX compile when a compiler exists; otherwise verify PDF/page count in Overleaf |

---

## Step 4 — Handle Overleaf/GitHub compilation

Use this workflow when the user says they compile in Overleaf, when the paper repo is linked to Overleaf through GitHub, or when local LaTeX commands are missing.

1. Confirm the local paper repo has a GitHub remote:

```bash
git -C "$PAPER_DIR" remote -v
git -C "$PAPER_DIR" status --short --branch
```

2. If the user asks to publish the changes for Overleaf, commit and push through normal Git flow. Do not commit unrelated user changes without checking the diff.

3. Tell the user to compile the synced branch in Overleaf. Treat Overleaf as the source of PDF truth for:
   - clean compile status
   - page count
   - overfull boxes and layout warnings
   - bibliography rendering
   - final PDF inspection

4. If Overleaf reports errors, use the Overleaf log text or screenshots as the compile evidence. Fix the LaTeX source locally, then push again.

Do not block submission readiness solely because local `pdflatex` is unavailable.

If project memory exists and the paper source is visible to coauthors, reviewers, arXiv, publisher, or artifact readers, update `memory/source-visibility-board.md` with the tier, sync target, cleanup gate, audit status, and cleanup actions.

---

## Step 5 — Fix submission mode in venue_preamble.tex

After reading the script output, check `venue_preamble.tex` and verify the `\usepackage` option matches what the user said in Step 2.

**If the mode is wrong**, show the user what to change and offer to fix it:

| Submission type | venue_preamble.tex should contain |
|---|---|
| Initial / anonymous | e.g. `\usepackage{neurips_<year>}`, `\usepackage[review]{cvpr}`, or `\usepackage[review]{iccv}` |
| arXiv / preprint | e.g. `\usepackage[preprint]{neurips_<year>}` |
| Camera-ready | e.g. `\usepackage[final]{neurips_<year>}`, `\usepackage{cvpr}`, or `\usepackage{iccv}` |

Ask "Should I update `venue_preamble.tex` to `[mode]` mode?" — then edit if confirmed.

---

## Step 6 — Check source visibility and cleanup

Different paper versions have different source hygiene requirements. Source visibility is independent of venue. If the branch is linked to Overleaf/GitHub or visible to coauthors, treat it as `author-visible`, not private.

| Visibility tier | Typical source surface | Required cleanup |
|---|---|---|
| `agent-private` | local/private draft worktree | May contain agent state, internal notes, plotting scripts, CSVs, and provenance; should not be pushed to Overleaf/public remotes |
| `author-visible` | main branch linked to Overleaf/GitHub | Exclude `.agent/`, `AGENTS.md`, `CLAUDE.md`, raw CSVs, internal result docs, plotting scripts, reviewer strategy, private paths, and agent-only notes |
| `anonymous-submission` | venue submission source/PDF | Enforce anonymization, remove identity leaks, avoid internal comments because source may be uploaded |
| `public-preprint` | arXiv/public source | Remove TODOs, author comments, reviewer notes, hidden comments, internal figure/table descriptions, anonymization leftovers, agent files, provenance docs, scripts, CSVs, and non-public paths |
| `camera-ready-public` | publisher/final source package | De-anonymize, add acknowledgements/funding, remove draft-only notes, close rebuttal promises, exclude agent/private files |

For author-visible, anonymous, arXiv, camera-ready, or publisher-visible source, do not leave internal audit artifacts in the source tree. This includes `.agent/`, `AGENTS.md`, `CLAUDE.md`, figure descriptions, table descriptions, provenance notes, reviewer-response notes, TODOs, raw CSVs, internal result docs, plotting scripts, notebooks, private paths, and author comment macros. Keep those in root `memory/`, code-side docs, or an `agent-private` paper worktree, not in visible source.

Check for forbidden files in visible source:

```bash
find "$PAPER_DIR" -maxdepth 3 \( \
  -path "$PAPER_DIR/.agent" -o \
  -name "AGENTS.md" -o -name "CLAUDE.md" -o \
  -name "*.csv" -o -name "*.ipynb" -o \
  -path "*/docs/results/*" -o -path "*/docs/reports/*" -o -path "*/docs/runs/*" -o \
  -path "*/scripts/*" -o -path "*/plot_scripts/*" -o \
  -iname "*provenance*" -o -iname "*result-inventory*" -o -iname "*writing-memory*" \
\) -print
```

Check for risky source text:

```bash
grep -RIn "\\\\todo\\|\\\\fixme\\|TODO\\|FIXME\\|\\\\jieke\\|\\\\jerry\\|\\\\wwm\\|Reviewer\\|internal\\|description\\|provenance" "$PAPER_DIR" --include="*.tex" || true
```

Use judgment before deleting. Some words such as "description" may be legitimate paper prose. Remove or rewrite only draft/internal material.

---

## Step 7 — Report findings and action plan

Present results in a structured format:

Mention the local/Overleaf compile state explicitly:

- local static-check result
- Overleaf/GitHub compile status if known, or "pending Overleaf compile" if the user must verify it there
- whether local LaTeX was skipped because no compiler exists
- version workspace status: main paper repo or specific paper worktree
- source visibility tier and source hygiene status for author-visible, anonymous, arXiv, camera-ready, or publisher-visible mode

```
## Submission Readiness: <venue> — <mode>

### ✅ Passed (N)
- ...

### ⚠️ Warnings (N) — review before submitting
- ...

### ❌ Must Fix (N) — blocking submission
- ...

### Action Plan
1. <highest-priority fix>
2. ...
```

For each failure or warning, provide the **specific file and line** and the **exact fix**.

---

## Step 8 — Offer targeted fixes

For common failures, offer to fix them immediately:

- **Drafting artifacts**: Show the list; ask if you should remove them.
- **Missing mandatory sections**: Offer to create a placeholder that the user can fill in.
- **Wrong submission mode**: Offer to edit `venue_preamble.tex`.
- **Source hygiene issues**: For author-visible/public/submission source, offer to remove or relocate `.agent/`, AGENTS/CLAUDE guidance, internal comments, figure/table descriptions, reviewer notes, TODOs, raw CSVs, plotting scripts, provenance docs, and author comment macros after showing the diff scope.
- **Empty bib file**: Remind user to add references to `bib/refs.bib`.

Do **not** auto-fix without confirmation.

---

## Venue Reference: Mandatory Sections & Page Limits

| Venue | Deadline | Pages (main) | Mandatory extras |
|---|---|---|---|
| ICML | Jan | 9 | `sections/impact.tex` (Broader Impact) |
| ACL | Feb | 8 | `sections/limitations.tex` |
| ICCV | Mar (odd) | 8 | — |
| ECCV | Mar (even) | 14 total incl. figs | — |
| NeurIPS | May | 9 | `sections/impact.tex` + `sections/checklist.tex` |
| EMNLP | May | 8 | `sections/limitations.tex` |
| ICLR | Sep | ~9 (soft) | — |
| CVPR | Nov | 8 | — |
| NAACL | Dec | 8 | `sections/limitations.tex` |
| ACM | varies | varies | CCS concepts, `\acmConference` (camera-ready) |

**References and mandatory extras do not count toward page limits** (all venues listed above).

---

## Submission Mode Quick Reference

### NeurIPS
```latex
% Anonymous submission (default):
\usepackage{neurips_<year>}
% arXiv preprint:
\usepackage[preprint]{neurips_<year>}
% Camera-ready:
\usepackage[final]{neurips_<year>}
```

### ICML
```latex
\usepackage{icml<year>}           % anonymous
\usepackage[accepted]{icml<year>} % camera-ready
```

### ICLR
```latex
\usepackage[submitted]{iclr<year>_conference}  % anonymous
\usepackage[accepted]{iclr<year>_conference}   % camera-ready
```

### CVPR
```latex
\usepackage[review]{cvpr}   % anonymous
\usepackage{cvpr}           % camera-ready
\usepackage[pagenumbers]{cvpr}  % arXiv (shows page numbers)
```

### ICCV
```latex
\usepackage[review]{iccv}   % anonymous
\usepackage{iccv}           % camera-ready
\usepackage[pagenumbers]{iccv}  % arXiv (shows page numbers)
```

### ACL / EMNLP / NAACL
```latex
\usepackage[review]{acl}   % anonymous
\usepackage{acl}           % camera-ready
```

### ECCV
```latex
\usepackage{eccv}            % anonymous (blind review)
\usepackage[final]{eccv}     % camera-ready
```

---

## Camera-Ready Checklist (additional items)

When `--mode camera-ready` or submission type is camera-ready, additionally verify:

- [ ] `venue_preamble.tex` set to `[final]` / `[accepted]` mode
- [ ] Author names and affiliations filled in `main.tex`
- [ ] Acknowledgements added (funding, compute credits, etc.)
- [ ] All author comment macros removed (`\jieke{}`, `\jerry{}`, etc.)
- [ ] `sections/acknowledgement.tex` is non-empty
- [ ] Copyright / license statement added if required (ACM)
- [ ] Final bibliography formatted correctly (no "Anonymous" entries)
- [ ] Supplementary material packaged separately if required
- [ ] Source `.tex` files zipped and ready for upload (many venues require source)

---

## arXiv Submission Notes

arXiv has different packaging requirements from venue submission:

- Must submit `.tex` source (not just PDF)
- Flatten `\input{...}` if using many files (some arXiv setups require a single `.tex`)
- Switch to `[preprint]` mode (removes venue branding / anonymization)
- Include all `.sty`, `.bst`, `.cls` files in the zip
- Remove internal comments, TODOs, author comment macros, reviewer notes, private paths, and figure/table descriptions from public source
- Remove any `\usepackage{times}` if it causes font issues on arXiv
- arXiv compiles with an older TeX Live — check for package compatibility

---

## Example Invocations

```
/submit-paper                                   # check current directory
/submit-paper ~/Papers/my-neurips-paper         # check specific project
/submit-paper . --compile                       # include local LaTeX check only if a compiler exists
/submit-paper . --mode camera-ready             # camera-ready checklist
```

# Paper Source Visibility Protocol

Paper source visibility is orthogonal to venue. A NeurIPS, ICML, arXiv, or camera-ready paper version can still differ in who may see the source tree and which files may exist there.

Use this protocol whenever a paper repo or paper worktree is linked to Overleaf, shared with collaborators, uploaded to a submission system, prepared for arXiv, or packaged for camera-ready/public release.

## Visibility Tiers

Use these tiers in `memory/source-visibility-board.md` and paper worktree status files:

| Tier | Typical surface | Audience | Policy |
|---|---|---|---|
| `agent-private` | local/private draft worktree or private branch | researcher and agents | May contain `.agent/`, `AGENTS.md`, `CLAUDE.md`, writing memory, provenance notes, internal result docs, plotting scripts, CSVs, TODOs, and reviewer strategy. Should not sync to Overleaf or public remotes unless intentionally private. |
| `author-visible` | main paper branch linked to Overleaf/GitHub | coauthors and collaborators | Contains collaborator-safe paper source. Must not contain `.agent/`, `AGENTS.md`, `CLAUDE.md`, internal memory, private result CSVs, internal plotting scripts, reviewer strategy, private paths, or agent-only docs. |
| `anonymous-submission` | conference submission source/PDF | reviewers, submission system, organizers | Must enforce anonymity and venue mode. Avoid internal comments because some venues request source upload. Must not contain identity leaks, `.agent/`, agent guidance, private paths, or internal result/provenance files. |
| `public-preprint` | arXiv source or public preprint repo | public, permanent archive | Public-clean LaTeX source and assets only. No TODOs, hidden notes, reviewer notes, agent memory, private paths, internal scripts, CSVs, provenance docs, or non-public comments. |
| `camera-ready-public` | final accepted paper source/package | publisher, public, artifact readers | De-anonymized, final, and public-clean. No draft-only notes, rebuttal scratch, agent state, private paths, internal scripts, or unverified provisional assets. |
| `publisher-artifact` | final paper source plus artifact links/package | publisher/artifact reviewers/public | Only final public paper, supplement, artifact links, release metadata, and reproducibility-facing files. Private project memory remains outside the bundle. |

## Allowed and Forbidden Surfaces

Default policy:

| Path or file class | `agent-private` | `author-visible` | `anonymous-submission` | `public-preprint` / `camera-ready-public` |
|---|---|---|---|---|
| `main.tex`, `sections/*.tex`, `macros.tex`, `venue_preamble.tex`, `bib/*.bib` | allowed | allowed | allowed after mode/anonymity checks | allowed after public cleanup |
| `figures/*.pdf`, `figures/*.png`, `figures/*.tex`, `tables/*.tex` | allowed | allowed if paper-facing | allowed if anonymized/public-safe | allowed if final/public-safe |
| `.agent/` | allowed | forbidden | forbidden | forbidden |
| `AGENTS.md`, `CLAUDE.md` | allowed as local agent guidance | forbidden by default | forbidden | forbidden |
| `memory/`, `paper/.agent/`, reviewer/rebuttal notes | allowed outside visible source | forbidden | forbidden | forbidden |
| `paper/.agent/result-inventory.md`, `result-asset-provenance.md`, writing memory | allowed | forbidden | forbidden | forbidden |
| raw CSVs, run logs, code-side reports, `docs/results/`, `docs/reports/`, `docs/runs/` inside paper repo | allowed only in private worktrees | forbidden | forbidden | forbidden |
| plotting scripts, notebooks, exploratory images, debug plots | allowed only in private worktrees | forbidden unless explicitly public-clean | forbidden | forbidden unless packaged intentionally |
| TODOs, author-comment macros, hidden comments, private paths | allowed during private drafting | discouraged; must not leak sensitive content | forbidden | forbidden |

## Default Branch Interpretation

- If `paper/main` is linked to Overleaf through GitHub, treat it as `author-visible`, not private.
- If collaborators can see a GitHub branch, treat it as at least `author-visible`.
- If a source archive may be uploaded to a venue or arXiv, treat it as `anonymous-submission`, `public-preprint`, or `camera-ready-public` depending on target.
- Store agent/private state in root `memory/`, private component `.agent/`, or an `agent-private` paper worktree. Do not rely on a visible paper branch for agent memory.

## Source Visibility Board

Track source surfaces in:

```text
memory/source-visibility-board.md
```

Use IDs:

- `VIS-###`: source visibility surface or policy

Each entry should record:

- surface path and branch
- visibility tier
- audience
- remote/sync target, such as Overleaf/GitHub, submission system, arXiv, publisher, or none
- allowed paths
- forbidden paths
- cleanup gate
- linked worktree ID
- latest audit status

## Visibility Audit

Before pushing, uploading, or packaging a visible paper source, check for forbidden files:

```text
.agent/
AGENTS.md
CLAUDE.md
memory/
docs/results/
docs/reports/
docs/runs/
*.csv
*.ipynb
scripts/
plot_scripts/
plots/debug/
*provenance*
*result-inventory*
*writing-memory*
*reviewer*
*rebuttal*
```

Also scan `.tex`, `.bib`, `.sty`, and `.cls` for:

```text
TODO, FIXME, internal, private path, reviewer note, response note, author comment macros, hidden figure/table descriptions, provenance notes
```

Use judgment for legitimate prose. The audit is a gate, not a blind deletion script.

## Relationship To Code Release

Code repositories may remain private until `release-code` creates a cleaned public release. Paper repositories often become collaborator-visible early through Overleaf. Therefore paper source visibility must be managed during writing, not only at the final release stage.

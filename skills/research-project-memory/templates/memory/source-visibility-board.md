# {{PROJECT_NAME}} Source Visibility Board

Track which paper source surfaces are private, collaborator-visible, submission-visible, or public.

| ID | Surface | Branch / worktree | Tier | Audience | Sync target | Allowed paths | Forbidden paths | Cleanup gate | Linked worktree | Audit status | Updated |
|---|---|---|---|---|---|---|---|---|---|---|---|
| VIS-000 | paper | main | author-visible | coauthors / Overleaf collaborators | Overleaf-GitHub | `main.tex`, `sections/`, `figures/`, `tables/`, `bib/`, `macros.tex`, `venue_preamble.tex` | `.agent/`, `AGENTS.md`, `CLAUDE.md`, raw CSVs, internal docs, plotting scripts, private paths | before push to visible remote | WTR-000 | needs-verification | {{DATE}} |

## Visibility Tiers

- `agent-private`: researcher/agent-only local or private branch.
- `author-visible`: coauthor-visible source, often GitHub-linked Overleaf.
- `anonymous-submission`: venue submission source/PDF, anonymous and source-clean.
- `public-preprint`: arXiv/public source, public-clean.
- `camera-ready-public`: final accepted paper source/package, public-clean.
- `publisher-artifact`: final public paper plus artifact/release-facing files.

## Open Visibility Actions

- Record any source surface that needs a cleanup audit before push, upload, arXiv, camera-ready, or public release.

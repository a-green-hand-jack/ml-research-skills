# Visual Asset Index

This directory stores public visual panels used to explain the `ml-research-skills` system. Images are documentation artifacts: keep names semantic, keep README links current, and update project memory when a figure changes meaningfully.

## Primary Panels

| File | Role | README placement | Notes |
|---|---|---|---|
| `system-overview.png` | Main system overview for the full skill collection. | Top of `README.md` | Use as the first visual entry point. |
| `project-anatomy.png` | Managed ML project structure, component repos, memory bus, and skill maintenance map. | `Project Anatomy` | Best panel for explaining the control-root layout. |
| `tool-calling-loop.png` | Core execution loop: read memory, plan, call skill/tool, write memory, evaluate. | `Core Execution Loop` | Use when explaining how a single skill invocation works. |
| `memory-project-bus.png` | Memory boards and object graph: claims, evidence, provenance, risks, actions, handoffs, phase, visibility. | `Memory System` | Use when explaining cross-session coordination. |
| `workspace-component-architecture.png` | Component boundaries, isolated repos, worktrees, and synchronization through memory. | `Project Anatomy` / control-root discussion | Use when explaining why `paper/`, `code/`, and worktrees stay isolated. |
| `infra-ops-audit-layer.png` | Infrastructure, ops, toolchain gates, sidecar, token audit, and governance. | `Project Toolchain Gates` | Use when explaining check-before-mutate and audit workflows. |
| `tool-memory-workflow.png` | Dense detailed workflow map of lifecycle, tool-calling loop, memory, workspace, infra, and audit. | `Lifecycle Categories` | Use as the detailed map after readers understand the simpler panels. |

## Secondary Variants

| File | Role | Policy |
|---|---|---|
| `lifecycle-skills-overview.png` | Earlier multi-panel lifecycle and skill-category overview. | Keep linked as a variant unless superseded by a clearer generated panel. |
| `lifecycle-system-collage.png` | Earlier high-resolution lifecycle collage. | Keep linked as a variant; avoid using as the main README image. |

## Maintenance Rules

- Use lowercase kebab-case filenames.
- Prefer one stable image per architectural concept instead of accumulating near-duplicates.
- When replacing or adding a primary panel, update:
  - `README.md`
  - this file
  - `memory/evidence-board.md` figure inventory
  - `memory/current-status.md` if the visual system changed materially
- If a generated image has a durable prompt, design brief, or source file, store it in a future `asset/prompts/` or `docs/visuals/` folder and link it here.
- Compress images only if all text remains readable at normal GitHub README zoom.

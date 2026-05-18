# ML Research Skills 分级架构与 Memory Reliability 改造设计文档

> 目标：把现有 `ml-research-skills` 从“flat skill registry + shared memory bus”升级为一个可路由、可验证、可 profile-gate、可回归测试的 **ML research lifecycle OS**。

---

## 0. 一句话版本

当前系统已经有很好的基础：

```text
skills/        # flat skill registry
memory/        # durable project coordination layer
scripts/       # validation / maintenance helpers
tests/         # routing evals
AGENTS.md      # repo-level agent policy
README.md      # human-facing inventory
```

下一步不要先把 `skills/` 物理搬成多层目录，而是增加一套机器可读的中间层：

```text
flat source tree
+ canonical taxonomy
+ router skills
+ activation profiles
+ memory contracts
+ routing path evals
+ closeout / stale-session / installed-copy checks
```

最终原则：

```text
leaf skills do work
router skills choose work
profiles control visibility
memory contracts control recall
evals control regressions
taxonomy controls truth
```

---

## 1. 当前问题

你现在遇到的问题可以拆成两个相关但不同的 failure modes。

### 1.1 Skill routing failure

当 skill 数量变多以后，agent 面对的是一个很大的 flat list：

```text
LLM
├── skill A
├── skill B
├── skill C
├── ...
└── skill N
```

这会导致：

- 相似 skill 之间误触发，例如 `experiment-debugger` vs `result-diagnosis` vs `research-results-auditor`；
- agent 只看到 compressed description，漏掉关键边界；
- 新增 skill 后旧 routing behavior 回归；
- README / AGENTS / SKILL.md / tests 里的 skill inventory 容易 drift。

### 1.2 Memory recall failure

现有 `memory/` 已经能保存很多项目事实、约定和状态，但 agent 经常“记不住”重要事实，根因通常不是没有写入 memory，而是没有 **recall guarantee**。

典型失败：

```text
重要事实写在 memory 里
但当前 task 没有强制读取对应 memory
agent 继续按旧上下文、旧约定、旧 skill 行动
```

所以需要把：

```text
“请记得读 memory”
```

升级成：

```text
“这个 skill 在这个 task tag 下必须读取这些 fact IDs / memory files，否则不得行动。”
```

---

## 2. 设计目标

### 2.1 Primary goals

1. **降低初始 skill 上下文污染**
   通过 router + profile，只向 agent 暴露当前阶段最相关的 skill 子集。

2. **稳定 skill selection**
   用 taxonomy、route table、contrastive routing rule 和 routing eval 固化选择边界。

3. **提高重要事实召回率**
   用 fact registry、memory bootstrap 和 per-skill memory contract 强制加载关键约定。

4. **让架构可验证**
   validator 不只检查 SKILL.md frontmatter，还检查 taxonomy、profiles、routes、evals、memory contracts。

5. **避免 source-of-truth drift**
   把 skill 分组、profile、route path、memory contract 从 Markdown inventory 中抽出来，放进机器可读的 canonical files。

### 2.2 Non-goals

第一版不要做这些：

- 不要物理重排 `skills/` 目录；
- 不要一次性重写所有 skill；
- 不要让 router skill 直接做业务；
- 不要把所有 memory 文件塞进 bootstrap；
- 不要把 `BRIEFING.md` 变成新的上下文垃圾桶。

---

## 3. 总体架构

推荐目标结构：

```text
ml-research-skills/
├── skills/
│   ├── ml-research-router/
│   ├── project-ops-router/
│   ├── discovery-router/
│   ├── method-code-router/
│   ├── experiment-evidence-router/
│   ├── paper-writing-router/
│   ├── feedback-review-router/
│   ├── release-artifact-router/
│   └── ... existing leaf/coordinator/utility skills ...
│
├── taxonomy/
│   ├── skill-index.yaml
│   ├── routes/
│   │   ├── root.yaml
│   │   ├── project-ops.yaml
│   │   ├── discovery.yaml
│   │   ├── method-code.yaml
│   │   ├── experiment-evidence.yaml
│   │   ├── paper-writing.yaml
│   │   ├── feedback-review.yaml
│   │   └── release-artifact.yaml
│   ├── profiles/
│   │   ├── kernel.yaml
│   │   ├── discovery.yaml
│   │   ├── method-code.yaml
│   │   ├── experiment.yaml
│   │   ├── paper.yaml
│   │   ├── rebuttal.yaml
│   │   ├── release.yaml
│   │   └── maintenance.yaml
│   └── memory-contracts/
│       ├── kernel.yaml
│       ├── experiment-run.yaml
│       ├── experiment-monitor.yaml
│       ├── result-interpretation.yaml
│       ├── paper-writing.yaml
│       ├── paper-evidence.yaml
│       └── release.yaml
│
├── memory/
│   ├── BRIEFING.md
│   ├── current-status.md
│   ├── project-conventions.md
│   ├── hot-results.md
│   ├── fact-index.yaml
│   ├── memory-revision.json
│   └── ... existing boards ...
│
├── scripts/
│   ├── memory_bootstrap.py
│   ├── memory_closeout.py
│   ├── activate_skill_profile.py
│   ├── check_installed_skill_sync.py
│   ├── generate_router_tables.py
│   ├── validate_skill_taxonomy.py
│   ├── validate_memory_contracts.py
│   └── routing_eval_harness.py
│
└── tests/
    ├── routing-evals.json
    ├── memory-routing-evals.json
    └── profile-evals.json
```

---

## 4. Skill 类型定义

不要让所有 skill 都承担同一种角色。建议把 skill 分为四类。

| 类型 | 职责 | 是否直接完成业务 | 示例 |
|---|---|---:|---|
| `router` | classify task, select child skill/profile, load memory pack | 否 | `ml-research-router`, `experiment-evidence-router` |
| `coordinator` | 编排多个 leaf skill，推进生命周期状态 | 有时 | `research-project-memory`, `auto-paper-improvement-loop` |
| `leaf` | 执行一个具体任务，产出具体 artifact | 是 | `run-experiment`, `result-diagnosis`, `paper-writing-assistant` |
| `utility` | 跨阶段工具能力 | 是 | `safe-git-ops`, `remote-project-control`, `run-status-monitor` |

关键规则：

```text
router skill 不直接解决任务。
router skill 只负责分类、选择、加载最小 memory context、记录 route decision。
```

否则 router 会变成新的 giant skill。

---

## 5. 分级原则：主树 + alias graph

ML research lifecycle 不是纯树，而是 DAG。一个 skill 可能服务多个阶段。

例如：

```text
run-status-monitor
```

既属于：

```text
experiment.execution
```

也属于：

```text
project_ops.remote
```

因此建议采用：

```yaml
primary_parent: experiment.execution
aliases:
  - project_ops.remote
  - project_ops.monitoring
```

也就是：

```text
主路由用树
辅助召回用 alias graph
```

好处：

- `expected_route_path` 清晰；
- cross-cutting skill 不会丢；
- profile 可以包含 alias skill；
- validator 可以检查主树是否有环、alias 是否存在。

---

## 6. 顶层 taxonomy

推荐顶层分成 7 个 domain routers，再加一个 root router。

```text
ml-research-router
├── project-ops-router
├── discovery-router
├── method-code-router
├── experiment-evidence-router
├── paper-writing-router
├── feedback-review-router
└── release-artifact-router
```

### 6.1 `project-ops-router`

职责：项目控制、memory、git、remote、sidecar、系统维护。

```text
project-ops-router
├── research-project-memory
├── project-init
├── new-workspace
├── project-sync
├── safe-git-ops
├── remote-project-control
├── run-status-monitor
├── sidecar-task-runner
├── code-reviewer
├── personalization-memory
├── memory-publication-auditor
├── token-usage-auditor
├── skill-system-auditor
└── work-timeline-planner
```

边界：

```text
project-ops 不改变科学内容，只保证项目系统可靠运行。
```

### 6.2 `discovery-router`

职责：idea、literature、reference、positioning 前期探索。

```text
discovery-router
├── research-idea-validator
├── literature-review-sprint
├── reference-library-manager
├── reference-reading-summarizer
├── reference-project-synthesizer
├── reference-corpus-analyzer
├── citation-coverage-audit
└── feedback-synthesizer
```

reference skills 的边界要写清楚：

```text
reference-library-manager
  管 inventory，不做深读。

reference-reading-summarizer
  读单篇或少量 source，生成 source card。

reference-project-synthesizer
  把 source card 连接到 claims / risks / baselines / experiments / writing contracts。

reference-corpus-analyzer
  对多篇文献做 comparison matrix、closest-work ranking、gap analysis。
```

### 6.3 `method-code-router`

职责：method design、code scaffold、data pipeline、implementation readiness。

```text
method-code-router
├── algorithm-design-planner
├── init-python-project
├── data-pipeline-manager
├── compute-budget-planner
├── code-reviewer
└── update-docs
```

边界：

```text
method-code router 负责把 idea 变成可实现系统。
experiment-evidence router 负责验证系统是否支持 claim。
```

### 6.4 `experiment-evidence-router`

这是最需要分级的一块，因为 experiment skill 之间很容易混。

```text
experiment-evidence-router
├── experiment-planning-router
├── experiment-execution-router
├── experiment-interpretation-router
└── experiment-packaging-router
```

展开：

```text
experiment-planning-router
├── experiment-design-planner
├── baseline-selection-audit
├── statistical-analysis-planner
├── compute-budget-planner
└── data-pipeline-manager

experiment-execution-router
├── run-experiment
├── run-status-monitor
├── experiment-debugger
└── remote-project-control

experiment-interpretation-router
├── result-diagnosis
├── research-results-auditor
├── statistical-analysis-planner
└── project-pivot-planner

experiment-packaging-router
├── experiment-report-writer
├── paper-evidence-board
├── paper-evidence-gap-miner
├── paper-result-asset-builder
├── figure-results-review
└── table-results-review
```

关键 routing rules：

```text
NaN / OOM / dataloader bug / metric bug
  -> experiment-debugger

existing job queued / stuck / ContainerCreating / scheduler state
  -> run-status-monitor

need to create or submit a new job
  -> run-experiment

result is valid but surprising / negative / ambiguous
  -> result-diagnosis

result seems to support a claim but protocol/confound risk exists
  -> research-results-auditor

effect size / confidence interval / seed variance / significance
  -> statistical-analysis-planner

core claim failed across multiple cycles
  -> project-pivot-planner

paper-facing tables/figures/provenance from result CSV/logs
  -> paper-result-asset-builder
```

### 6.5 `paper-writing-router`

```text
paper-writing-router
├── paper-contract-router
├── paper-drafting-router
├── paper-evidence-asset-router
├── paper-editing-router
└── paper-submission-router
```

展开：

```text
paper-contract-router
├── paper-positioning-planner
├── conference-writing-adapter
├── paper-writing-contract-planner
└── paper-writing-memory-manager

paper-drafting-router
├── paper-writing-assistant
├── paper-introduction-argument-writer
├── method-section-explainer
├── experiment-story-writer
├── related-work-positioning-writer
├── limitations-scope-writer
└── abstract-title-contribution-writer

paper-evidence-asset-router
├── paper-evidence-board
├── paper-evidence-gap-miner
├── paper-result-asset-builder
├── figure-results-review
└── table-results-review

paper-editing-router
├── paper-draft-consistency-editor
├── auto-paper-improvement-loop
├── citation-audit
├── citation-coverage-audit
└── latex-layout-issue-bundler

paper-submission-router
├── appendix-organizer
├── submit-paper
├── camera-ready-finalizer
└── artifact-evaluation-prep
```

关键边界：

```text
paper-writing-contract-planner
  决定能写什么、不能写什么。

paper-writing-assistant
  真正写 claim-aware prose。

paper-writing-memory-manager
  维护 nonlinear drafting state，不是主写手。

paper-draft-consistency-editor
  检查全稿一致性，不负责创造主 claim。

auto-paper-improvement-loop
  多轮 review/edit 编排，不是单次编辑。

experiment-story-writer
  只写 results narrative，不负责 method 或 intro 主论证。
```

### 6.6 `feedback-review-router`

```text
feedback-review-router
├── feedback-synthesizer
├── advisor-update-writer
├── research-slide-deck-builder
├── paper-reviewer-simulator
├── rebuttal-strategist
├── appendix-organizer
└── camera-ready-finalizer
```

边界：

```text
advisor / collaborator feedback
  -> feedback-synthesizer

need to write update / email / lab meeting summary
  -> advisor-update-writer

pre-submission simulated review
  -> paper-reviewer-simulator

real reviews received
  -> rebuttal-strategist

accepted paper finalization
  -> camera-ready-finalizer
```

### 6.7 `release-artifact-router`

```text
release-artifact-router
├── artifact-evaluation-prep
├── model-card-writer
├── release-code
├── add-git-tag
├── update-docs
└── work-timeline-planner
```

边界：

```text
artifact-evaluation-prep
  reviewer-facing reproducibility package。

release-code
  public repo release。

model-card-writer
  model / dataset documentation。

add-git-tag
  milestone tagging。

update-docs
  affected docs refresh。
```

---

## 7. Canonical taxonomy: `taxonomy/skill-index.yaml`

`skill-index.yaml` 应该是 skill 分级、profile、routing、docs generation 的唯一 source of truth。

### 7.1 示例 schema

```yaml
version: 1

default_root: ml-research-router

skills:
  run-experiment:
    kind: leaf
    primary_parent: experiment.execution
    aliases:
      - project_ops.remote
    profiles:
      - experiment
      - kernel-remote
    short_description: >
      Create reproducible local, SLURM, or RunAI experiment jobs.
    use_when:
      - Need to launch or prepare a new experiment run.
      - Need smoke/debug/formal job script generation.
      - Need resource-aware submission command.
    not_when:
      - Existing job status is needed; use run-status-monitor.
      - Training has NaN/OOM/metric bug; use experiment-debugger.
      - Scientific interpretation is needed; use result-diagnosis.
    memory_contract: experiment-run
    input_artifacts:
      - config
      - training script
      - compute target
    output_artifacts:
      - job script
      - submission command
      - provenance pointer
    confusable_with:
      - run-status-monitor
      - experiment-debugger
      - compute-budget-planner

  run-status-monitor:
    kind: utility
    primary_parent: experiment.execution
    aliases:
      - project_ops.remote
      - project_ops.monitoring
    profiles:
      - kernel
      - experiment
    short_description: >
      Probe status for existing local, server, SLURM, RunAI, or wrapper-backed jobs.
    use_when:
      - Need current status of an existing job.
      - Need pending-resource or scheduler diagnosis.
      - Need short progress artifact without raw log dumping.
    not_when:
      - Need to launch a new job; use run-experiment.
      - Need to debug NaN/OOM/training failure; use experiment-debugger.
    memory_contract: experiment-monitor
    confusable_with:
      - run-experiment
      - experiment-debugger
      - remote-project-control

  result-diagnosis:
    kind: leaf
    primary_parent: experiment.interpretation
    profiles:
      - experiment
      - evidence
    short_description: >
      Diagnose valid but surprising, negative, unstable, or ambiguous ML results.
    use_when:
      - Result is scientifically surprising but not an engineering failure.
      - Need decide rerun/ablate/revise/narrow/write/park/kill.
    not_when:
      - NaN/OOM/dataloader bug exists; use experiment-debugger.
      - Need significance/effect size/seed variance; use statistical-analysis-planner.
      - Need confound/protocol audit before locking claim; use research-results-auditor.
    memory_contract: result-interpretation
    confusable_with:
      - experiment-debugger
      - research-results-auditor
      - statistical-analysis-planner
```

### 7.2 Validator requirements

`validate_skill_taxonomy.py` 应该检查：

```text
- every skill in taxonomy exists under skills/<name>/SKILL.md
- every skills/<name> exists in taxonomy, unless explicitly ignored
- kind is one of router/coordinator/leaf/utility
- primary_parent exists in taxonomy/routes/*.yaml
- aliases point to existing route nodes
- profiles point to existing taxonomy/profiles/*.yaml
- memory_contract points to existing taxonomy/memory-contracts/*.yaml
- confusable_with names exist
- router skills have children
- leaf skills do not have children
- no cycles in primary_parent graph
- short_description is short enough for generated route tables
```

---

## 8. Route tables: `taxonomy/routes/*.yaml`

Route files define the hierarchy. They should be compact and machine-readable.

Example: `taxonomy/routes/experiment-evidence.yaml`

```yaml
route: experiment-evidence-router
children:
  experiment.planning:
    router_skill: experiment-planning-router
    description: Plan experiments, baselines, metrics, controls, budgets, and data readiness.
    children:
      - experiment-design-planner
      - baseline-selection-audit
      - statistical-analysis-planner
      - compute-budget-planner
      - data-pipeline-manager

  experiment.execution:
    router_skill: experiment-execution-router
    description: Launch, monitor, and debug experiment jobs.
    children:
      - run-experiment
      - run-status-monitor
      - experiment-debugger
      - remote-project-control

  experiment.interpretation:
    router_skill: experiment-interpretation-router
    description: Interpret valid results, audit claims, and decide pivots.
    children:
      - result-diagnosis
      - research-results-auditor
      - statistical-analysis-planner
      - project-pivot-planner

  experiment.packaging:
    router_skill: experiment-packaging-router
    description: Convert results into evidence, reports, tables, and figures.
    children:
      - experiment-report-writer
      - paper-evidence-board
      - paper-evidence-gap-miner
      - paper-result-asset-builder
      - figure-results-review
      - table-results-review
```

---

## 9. Router skill design

Router skill 要短、强约束、只路由。

目录结构：

```text
skills/experiment-evidence-router/
├── SKILL.md
└── references/
    ├── route-table.md
    ├── contrastive-routing.md
    └── memory-contract.md
```

### 9.1 `SKILL.md` 模板

```markdown
---
name: experiment-evidence-router
description: Route ML experiment, compute, result, evidence, and claim-support tasks to the right planning, execution, debugging, diagnosis, audit, or packaging skill. Do not solve the experiment task directly.
---

# Experiment Evidence Router

## Contract

You are a router. Do not solve the experiment task directly.

Your job is to:

1. classify the user task;
2. select the most appropriate child route or leaf skill;
3. load the minimal relevant memory contract;
4. record a routing trace if repo-local memory is available.

## Routing steps

1. Classify the task into exactly one primary bucket:
   - planning
   - execution
   - monitoring
   - engineering-debugging
   - interpretation
   - claim-audit
   - paper-packaging

2. Read `references/route-table.md`.

3. Read `references/contrastive-routing.md` if the task matches a confusable pair.

4. Run or request memory bootstrap:

   ```bash
   python3 scripts/memory_bootstrap.py \
     --task "<user task>" \
     --route experiment-evidence-router
   ```

5. Select one child skill.

6. If confidence is low, ask one narrowing question. Otherwise hand off directly.

7. If repo-local `.agent/` exists, append a JSONL route decision to `.agent/routing-trace.jsonl`.
```

### 9.2 `references/route-table.md` 示例

```markdown
# Experiment Evidence Route Table

| Bucket | Use when | Skill |
|---|---|---|
| Planning | Need baselines, ablations, metrics, controls, logging, or stop conditions | experiment-design-planner |
| Baseline fairness | Need to decide whether baselines are necessary/current/fair | baseline-selection-audit |
| Compute sizing | Need GPU hours, budget, smoke/debug/formal sizing | compute-budget-planner |
| Launch | Need to create or submit a new local/SLURM/RunAI job | run-experiment |
| Status | Existing job is queued/stuck/running/finished | run-status-monitor |
| Engineering failure | NaN, OOM, dataloader, metric bug, reproducibility failure | experiment-debugger |
| Scientific surprise | Result is valid but negative/surprising/ambiguous | result-diagnosis |
| Claim audit | Need confound, protocol, or claim-drift audit | research-results-auditor |
| Statistical rigor | Need significance, confidence interval, effect size, seed variance | statistical-analysis-planner |
| Paper evidence | Need tables/figures/evidence board from results | paper-result-asset-builder |
```

### 9.3 `references/contrastive-routing.md` 示例

```markdown
# Contrastive Routing Rules

## `run-experiment` vs `run-status-monitor`

Use `run-experiment` when the user needs to create, configure, or submit a new job.

Use `run-status-monitor` when the job already exists and the user asks whether it is queued, stuck, running, completed, or failed.

## `experiment-debugger` vs `result-diagnosis`

Use `experiment-debugger` for engineering failures: NaN loss, OOM, dataloader bugs, metric bugs, broken reproducibility, slow training caused by implementation issues.

Use `result-diagnosis` for scientifically valid but surprising, negative, unstable, or ambiguous outcomes.

## `result-diagnosis` vs `research-results-auditor`

Use `result-diagnosis` to decide what to do next after a surprising result.

Use `research-results-auditor` to check whether completed results legitimately support a claim, especially for confounds, protocol drift, attribution, or reviewer risk.
```

---

## 10. Leaf skill description reform

Leaf skill 的 frontmatter `description` 应该更 routing-oriented：短、触发词明确、边界明确。

### 10.1 Before

```yaml
description: Generate reproducible local, SLURM, or RunAI job scripts and submission commands with resource-aware smoke/debug/formal planning
```

### 10.2 After

```yaml
description: Use when launching or preparing a new ML experiment job: local, SLURM, RunAI, smoke/debug/formal scripts. Not for existing job status; use run-status-monitor. Not for NaN/OOM bugs; use experiment-debugger.
```

建议规则：

```text
- description 第一分句写 positive trigger。
- 第二分句写最常见 negative boundary。
- 最多提 2-3 个 confusable alternatives。
- 不在 description 里塞完整 workflow。
- 完整 workflow 放 SKILL.md body 或 references/。
```

---

## 11. Activation profiles

只靠 router metadata 是软分级；真正降低上下文污染，需要 profile-gated visibility。

### 11.1 Profile 目标

不同 project phase / worktree 只激活一小组 skill：

```text
root project: kernel + current phase profile
code worktree: kernel + experiment profile
paper worktree: kernel + paper profile
rebuttal branch: kernel + rebuttal profile
release branch: kernel + release profile
```

### 11.2 Example: `taxonomy/profiles/kernel.yaml`

```yaml
name: kernel
description: Always-visible minimal skill layer for project control, memory, safe git, remote status, and routing.
skills:
  - ml-research-router
  - project-ops-router
  - research-project-memory
  - safe-git-ops
  - remote-project-control
  - run-status-monitor
  - skill-system-auditor
```

### 11.3 Example: `taxonomy/profiles/experiment.yaml`

```yaml
name: experiment
include:
  - kernel
skills:
  - experiment-evidence-router
  - experiment-design-planner
  - baseline-selection-audit
  - statistical-analysis-planner
  - compute-budget-planner
  - data-pipeline-manager
  - run-experiment
  - experiment-debugger
  - result-diagnosis
  - research-results-auditor
  - project-pivot-planner
  - experiment-report-writer
  - paper-evidence-board
  - paper-evidence-gap-miner
  - paper-result-asset-builder
  - figure-results-review
  - table-results-review
```

### 11.4 Example: `taxonomy/profiles/paper.yaml`

```yaml
name: paper
include:
  - kernel
skills:
  - paper-writing-router
  - paper-positioning-planner
  - conference-writing-adapter
  - paper-writing-contract-planner
  - paper-writing-memory-manager
  - paper-writing-assistant
  - paper-introduction-argument-writer
  - method-section-explainer
  - experiment-story-writer
  - related-work-positioning-writer
  - limitations-scope-writer
  - abstract-title-contribution-writer
  - paper-draft-consistency-editor
  - auto-paper-improvement-loop
  - citation-audit
  - citation-coverage-audit
  - latex-layout-issue-bundler
  - appendix-organizer
  - submit-paper
```

### 11.5 Activation script interface

```bash
python3 scripts/activate_skill_profile.py experiment
```

Expected behavior:

```text
1. Resolve profile includes.
2. Verify all referenced skills exist.
3. Create/update repo-local .agents/skills/ symlinks or copies.
4. Remove skills that are not in active profile, unless pinned.
5. Write active profile to .agent/worktree-status.md or memory/current-status.md.
6. Print visible routers and visible leaf skills.
```

Example output:

```text
ACTIVE PROFILE: experiment
VISIBLE ROUTERS:
- ml-research-router
- project-ops-router
- experiment-evidence-router

VISIBLE LEAF/UTILITY SKILLS:
- run-experiment
- run-status-monitor
- experiment-debugger
- result-diagnosis
- research-results-auditor
...
```

---

## 12. Connect phase-dashboard to profile activation

`memory/phase-dashboard.md` 应该能映射到 recommended profile。

Example mapping:

```yaml
phase_to_profile:
  idea_triage: discovery
  literature_review: discovery
  method_design: method-code
  implementation: method-code
  experiment_planning: experiment
  experiment_running: experiment
  result_analysis: experiment
  paper_drafting: paper
  submission: paper
  rebuttal: rebuttal
  camera_ready: release
  public_release: release
```

`memory_bootstrap.py` 可以输出：

```text
ACTIVE PHASE
- experiment_running

RECOMMENDED PROFILE
- experiment

VISIBLE ROUTERS
- ml-research-router
- project-ops-router
- experiment-evidence-router

CANDIDATE LEAF SKILLS
- run-experiment
- run-status-monitor
- experiment-debugger
- result-diagnosis
- research-results-auditor
```

---

## 13. Memory Reliability Layer

分级 skill 解决“选哪个 skill”。Memory Reliability Layer 解决“选中之后必须记住什么”。

目标：

```text
task -> route -> skill -> memory contract -> required fact IDs / files -> bounded action -> writeback gate
```

### 13.1 Canonical fact registry: `memory/fact-index.yaml`

```yaml
schema: 1

facts:
  - id: PC-004
    type: convention
    priority: P0
    status: active
    scope: project
    certainty: user-stated
    owner_skill: safe-git-ops
    source_of_truth: memory/project-conventions.md#PC-004

    text: >
      Routine pushes must use the project-push wrapper after safe-git preflight.
      Do not replace preflight with the wrapper.

    applies_to:
      - git
      - push
      - commit-closeout
      - project-maintenance

    read_triggers:
      - push
      - commit
      - closeout
      - sync branch
      - publish changes

    enforcement:
      allowed_command_patterns:
        - "^project-push "
      forbidden_command_patterns:
        - "\\bgit\\s+push\\b"
        - "git -C .* push"
        - "cd .* && git push"

    freshness:
      mode: stable-until-expired
      last_reviewed: 2026-05-16
```

Recommended source-of-truth split:

```text
memory/fact-index.yaml        = machine-readable source of truth
memory/project-conventions.md = generated or curated human view
memory/BRIEFING.md            = compact task-independent startup snapshot
memory/hot-results.md         = compact result view
```

### 13.2 Recall tiers

| Tier | Meaning | Examples | Recall mechanism |
|---|---|---|---|
| P0 | 绝对不能忘 | active conventions, forbidden commands, source visibility, scope rules | every bootstrap |
| P1 | 当前任务必须知道 | active experiment protocol, writing contract, current worktree purpose | task-specific bootstrap |
| P2 | 相关时检索 | older decisions, archived risks, failed runs | skill-specific route |
| P3 | 历史记录 | logs, superseded drafts, expired conventions | audit/timeline only |

### 13.3 `memory_bootstrap.py`

Interface:

```bash
python3 scripts/memory_bootstrap.py \
  --task "run a smoke experiment on the remote server" \
  --skill run-experiment \
  --scope auto
```

Expected output:

```text
SCOPE
- Detected: code worktree
- Project root: /path/to/project
- Local write target: .agent/worktree-status.md
- Project write target: memory/ only for confirmed cross-component results

MUST READ
- memory/BRIEFING.md
- memory/project-conventions.md
- memory/hot-results.md
- .agent/worktree-status.md

ACTIVE FACTS
- PC-001: Run scope detection before memory work.
- PC-002: Read BRIEFING -> project-conventions -> hot-results before decisions.
- PC-023: Reuse project/stage uv environments by default.
- PC-026: Do not do repeated transcript-visible polling.

NEEDS VERIFY
- git state
- scheduler / job state
- installed skill copy freshness

DO NOT
- Do not write provisional worktree results into root memory.
- Do not create job-specific uv envs without a concrete reason.
- Do not run long-lived polling loops in the main transcript.

WRITEBACK
- In-progress result: worktree .agent/worktree-status.md
- Confirmed result: memory/hot-results.md + evidence/provenance
- New convention: memory/fact-index.yaml, then regenerate project-conventions.md
```

### 13.4 Memory contracts

Every high-risk skill should point to a memory contract.

Example: `taxonomy/memory-contracts/experiment-run.yaml`

```yaml
name: experiment-run
applies_to:
  - run-experiment
  - experiment-execution-router

task_tags:
  - experiment
  - remote
  - compute
  - code-worktree

always_read:
  - memory/BRIEFING.md
  - memory/project-conventions.md
  - memory/hot-results.md

conditional_read:
  - when: inside_worktree
    files:
      - .agent/worktree-status.md
  - when: paper_facing_result_or_claim_changes
    files:
      - memory/claim-board.md
      - memory/evidence-board.md
      - memory/provenance-board.md

verify_before_acting:
  - git-state
  - worktree-scope
  - scheduler-state
  - environment-state

writeback:
  in_progress:
    - .agent/worktree-status.md
  confirmed_cross_component:
    - memory/hot-results.md
    - memory/evidence-board.md
    - memory/provenance-board.md
    - memory/action-board.md

forbidden:
  - write provisional worktree-only results into root memory
  - treat queue state as durable memory
  - create job-specific environments without explicit isolation reason
```

---

## 14. Memory closeout gate

Add:

```bash
python3 scripts/memory_closeout.py --changed-from HEAD~1
```

Expected checks:

```text
If skills/*/SKILL.md changed:
  - Does taxonomy/skill-index.yaml need update?
  - Do route tables need update?
  - Do README / AGENTS / CLAUDE inventories need regeneration?
  - Do routing evals need update?
  - Do installed skill copies need refresh?

If experiment/report/table/figure changed:
  - Does hot-results need update?
  - Does evidence-board/provenance-board need update?
  - If no, is there a no-memory-update reason?

If paper source changed:
  - Does claim-board or paper-evidence-board need update?
  - Does writing-contract need update?
  - Did source visibility change?

If wrappers / remote scripts changed:
  - Does project-conventions need update?
  - Does fact-index need update?
  - Is there a regression eval for the new rule?
```

Principle:

```text
重要事实不能只停留在 chat history 里。
```

---

## 15. Stale-session detection

Add `memory/memory-revision.json`:

```json
{
  "revision": 42,
  "updated_at": "2026-05-16T20:00:00+08:00",
  "briefing_hash": "sha256:...",
  "fact_index_hash": "sha256:...",
  "project_conventions_hash": "sha256:...",
  "hot_results_hash": "sha256:..."
}
```

`memory_bootstrap.py` should print:

```text
MEMORY REVISION: 42
If your last seen revision is lower, reread BRIEFING and project-conventions before acting.
```

For high-risk actions:

```bash
python3 scripts/memory_bootstrap.py --check-stale --seen-revision 41
```

Expected failure:

```text
ERROR: memory revision changed from 41 to 42.
Reread task context before acting.
```

---

## 16. Installed-copy sync auditor

Skill repo 修改后，installed skill copies 可能还是旧副本。需要显式检查。

Add:

```bash
python3 scripts/check_installed_skill_sync.py
```

Expected output:

```text
LOCAL REPO
- skills/run-experiment/SKILL.md hash: abc123

INSTALLED CODEX
- ~/.agents/skills/run-experiment/SKILL.md hash: old999
- status: STALE

INSTALLED CLAUDE
- ~/.claude/skills/run-experiment/SKILL.md hash: abc123
- status: OK

ACTION
- run: npx skills add a-green-hand-jack/ml-research-skills -g -a codex claude-code -y
```

`memory_closeout.py` should require this check when these files change:

```text
skills/**/SKILL.md
taxonomy/**
scripts/memory_bootstrap.py
scripts/activate_skill_profile.py
scripts/validate_skill_taxonomy.py
AGENTS.md
CLAUDE.md
README.md
```

---

## 17. Routing evals: from flat trigger to path eval

Current routing evals should evolve from:

```json
{
  "id": "RTE-001",
  "prompt": "My training loss became NaN after 500 steps. How do I fix it?",
  "should_trigger": "experiment-debugger",
  "should_not_trigger": ["result-diagnosis", "research-results-auditor"],
  "rationale": "NaN loss is an engineering failure, not a scientific result issue."
}
```

to:

```json
{
  "id": "RTE-001",
  "prompt": "My training loss became NaN after 500 steps. How do I fix it?",
  "expected_path": [
    "ml-research-router",
    "experiment-evidence-router",
    "experiment-execution-router",
    "experiment-debugger"
  ],
  "expected_profile": "experiment",
  "should_trigger": "experiment-debugger",
  "should_not_trigger": [
    "result-diagnosis",
    "research-results-auditor"
  ],
  "must_read_memory_contract": [
    "kernel",
    "experiment-debugging"
  ],
  "rationale": "NaN loss is an engineering failure, not a scientific result issue."
}
```

### 17.1 Memory regression eval example

```json
{
  "id": "MEM-ROUTE-001",
  "prompt": "Commit and push these skill changes.",
  "expected_path": [
    "ml-research-router",
    "project-ops-router",
    "safe-git-ops"
  ],
  "must_read_facts": [
    "PC-004"
  ],
  "allowed_patterns": [
    "project-push "
  ],
  "forbidden_patterns": [
    "git push",
    "git -C .* push",
    "cd .* && git push"
  ]
}
```

### 17.2 Validator rules

`validate_skill_taxonomy.py` and/or `validate_skills.py` should check:

```text
- every expected_path node exists
- expected_path starts with ml-research-router
- expected_path ends in should_trigger
- should_trigger exists
- should_not_trigger skills exist
- expected_profile exists
- expected_profile includes should_trigger directly or through include
- every must_read_memory_contract exists
- every must_read_fact exists in memory/fact-index.yaml
- every confusable_with pair has at least one routing eval
```

---

## 18. Generated docs

Once `taxonomy/skill-index.yaml` is source of truth, generate human-facing docs instead of manually editing all inventories.

Add:

```bash
python3 scripts/generate_router_tables.py
```

Generated outputs:

```text
skills/*-router/references/route-table.md
skills/*-router/references/contrastive-routing.md
docs/skill-taxonomy.md
docs/skill-profiles.md
README skill inventory section
AGENTS.md skill inventory section
CLAUDE.md skill inventory section
```

Recommended policy:

```text
Manual edits should happen in taxonomy/ and memory-contracts/.
Generated docs should be overwritten by script.
Validator should fail if generated docs are stale.
```

---

## 19. Minimal viable implementation plan

### Phase 0 — Baseline snapshot

Do this before changing architecture:

```bash
python3 scripts/validate_skills.py
python3 scripts/check_installed_skill_sync.py || true
```

Record in `memory/current-status.md`:

```text
- current number of skills
- current validator status
- current installed-copy freshness if known
- current active pain points
```

### Phase 1 — Canonical taxonomy MVP

Add:

```text
taxonomy/skill-index.yaml
taxonomy/routes/root.yaml
taxonomy/routes/experiment-evidence.yaml
taxonomy/routes/paper-writing.yaml
taxonomy/routes/project-ops.yaml
taxonomy/profiles/kernel.yaml
taxonomy/profiles/experiment.yaml
taxonomy/profiles/paper.yaml
```

Only include high-risk first batch:

```text
experiment side:
- run-experiment
- run-status-monitor
- experiment-debugger
- result-diagnosis
- research-results-auditor
- statistical-analysis-planner
- experiment-design-planner
- baseline-selection-audit
- compute-budget-planner

paper side:
- paper-writing-contract-planner
- paper-writing-memory-manager
- paper-writing-assistant
- experiment-story-writer
- paper-draft-consistency-editor
- paper-evidence-board
- submit-paper

ops side:
- research-project-memory
- safe-git-ops
- remote-project-control
- new-workspace
- sidecar-task-runner
```

### Phase 2 — Router skills MVP

Add four router skills:

```text
skills/ml-research-router/
skills/experiment-evidence-router/
skills/paper-writing-router/
skills/project-ops-router/
```

Each router gets:

```text
SKILL.md
references/route-table.md
references/contrastive-routing.md
references/memory-contract.md
```

### Phase 3 — Memory reliability MVP

Add:

```text
memory/fact-index.yaml
memory/memory-revision.json
taxonomy/memory-contracts/kernel.yaml
taxonomy/memory-contracts/experiment-run.yaml
taxonomy/memory-contracts/experiment-monitor.yaml
taxonomy/memory-contracts/result-interpretation.yaml
taxonomy/memory-contracts/paper-writing.yaml
scripts/memory_bootstrap.py
```

Patch first high-risk skills to reference memory contracts:

```text
research-project-memory
safe-git-ops
remote-project-control
run-experiment
run-status-monitor
experiment-debugger
result-diagnosis
research-results-auditor
paper-writing-contract-planner
paper-writing-assistant
paper-evidence-board
```

### Phase 4 — Profile activation

Add:

```text
scripts/activate_skill_profile.py
scripts/check_installed_skill_sync.py
```

Start with three profiles:

```text
kernel
experiment
paper
```

Do not over-optimize profile count at first.

### Phase 5 — Validation and evals

Extend or add:

```text
scripts/validate_skill_taxonomy.py
scripts/validate_memory_contracts.py
scripts/routing_eval_harness.py
tests/routing-evals.json
tests/memory-routing-evals.json
```

First acceptance target:

```text
- taxonomy validates
- profiles validate
- every high-risk skill has memory_contract
- every confusable pair has at least one eval
- expected_path is checked for all migrated evals
```

### Phase 6 — Generated docs

Add:

```text
scripts/generate_router_tables.py
docs/skill-taxonomy.md
docs/skill-profiles.md
```

Then decide whether README / AGENTS / CLAUDE skill inventories should be generated or manually maintained with validator checks.

---

## 20. Acceptance criteria

First stable version is acceptable when these are true:

```text
[ ] Existing skills/ directory remains compatible with current install flow.
[ ] taxonomy/skill-index.yaml covers at least the high-risk first batch.
[ ] kernel, experiment, and paper profiles validate.
[ ] ml-research-router, experiment-evidence-router, paper-writing-router, project-ops-router exist.
[ ] Router skills do not directly perform leaf work.
[ ] High-risk skills have memory contracts.
[ ] memory_bootstrap.py produces task-specific MUST READ / ACTIVE FACTS / DO NOT / WRITEBACK sections.
[ ] routing-evals.json supports expected_path.
[ ] Validator checks path, profile, and memory contract references.
[ ] installed-copy sync check exists.
[ ] memory_closeout.py blocks or warns on skill changes without taxonomy/eval/memory consideration.
[ ] Docs explain how to activate profile and how to add a new skill.
```

---

## 21. How to add a new skill after this refactor

New skill workflow:

```text
1. Create skills/<new-skill>/SKILL.md.
2. Add entry to taxonomy/skill-index.yaml.
3. Assign kind: router/coordinator/leaf/utility.
4. Assign primary_parent.
5. Add aliases if cross-cutting.
6. Add profiles.
7. Add memory_contract.
8. Add confusable_with if needed.
9. Add or update routing eval.
10. Run validator.
11. Generate router tables/docs.
12. Run installed-copy sync check if skill should be active.
```

Command sketch:

```bash
python3 scripts/validate_skill_taxonomy.py
python3 scripts/validate_memory_contracts.py
python3 scripts/generate_router_tables.py
python3 scripts/validate_skills.py
python3 scripts/routing_eval_harness.py --offline
python3 scripts/check_installed_skill_sync.py
```

---

## 22. Practical first patch

The smallest useful PR should include:

```text
A. taxonomy/
   - skill-index.yaml
   - profiles/kernel.yaml
   - profiles/experiment.yaml
   - profiles/paper.yaml
   - routes/root.yaml
   - routes/experiment-evidence.yaml
   - routes/paper-writing.yaml
   - routes/project-ops.yaml

B. skills/
   - ml-research-router/SKILL.md
   - experiment-evidence-router/SKILL.md
   - paper-writing-router/SKILL.md
   - project-ops-router/SKILL.md

C. tests/
   - routing-evals.json upgraded for expected_path on existing examples

D. scripts/
   - validate_skill_taxonomy.py

E. memory/
   - fact-index.yaml with only P0 conventions
   - memory-revision.json
```

Do **not** try to migrate every skill in the first patch. The goal of patch one is to prove the architecture.

---

## 23. Risk register

| Risk | Failure mode | Mitigation |
|---|---|---|
| Router bloat | Router starts doing leaf work | Router contract: classify/select/load/trace only |
| Taxonomy drift | README/AGENTS/SKILL.md disagree | Generate docs from taxonomy and validate stale output |
| Profile hides needed skill | Agent cannot access relevant leaf | Kernel profile contains root routers and emergency ops utilities; aliases help recall |
| Memory bootstrap too large | Context pollution returns | P0/P1/P2/P3 recall tiers and task-specific selection |
| Too much initial refactor | Migration stalls | First patch covers only high-risk skills |
| Eval false confidence | Tests only check names, not behavior | Move from should_trigger to expected_path + memory_contract + forbidden pattern checks |
| Installed skills stale | Runtime uses old SKILL.md | check_installed_skill_sync.py + closeout gate |
| Alias graph becomes messy | Everything links to everything | Require primary_parent; aliases must be justified and validated |

---

## 24. Final design rule

不要让 agent 在 60+ flat skills 里猜。

让它按下面路径行动：

```text
task
  -> active phase/profile
    -> root router
      -> domain router
        -> sub-router or leaf skill
          -> memory contract
            -> bounded action
              -> writeback gate
                -> regression eval if failure was discovered
```

这个设计把“skill 很多导致上下文爆炸”和“agent 忘记重要事实”合并成同一个工程问题：

```text
每一层都只暴露下一步必须知道的信息。
```

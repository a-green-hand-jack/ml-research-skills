# Reading Priority

Prioritize papers by project decision value.

## Priority Labels

`read-now`
: The paper can change novelty, claim scope, method design, baseline selection, evaluation protocol, or whether to pursue the project.

`skim`
: The paper is useful for terminology, framing, related-work coverage, or secondary comparisons, but unlikely to change the core decision.

`defer`
: Relevant but not needed for the current sprint question.

`ignore-for-now`
: Out of scope, superseded, too weakly related, or not useful for the user's current decision.

## Ranking Factors

Increase priority when a paper:

- targets the same problem, model family, or benchmark
- makes the same conceptual move
- is recent or accepted at the target venue
- is heavily cited or defines community terminology
- provides a baseline reviewers expect
- has public code or standard configs
- contradicts the user's expected claim
- reveals a cheaper decisive experiment

Decrease priority when a paper:

- only shares surface terminology
- focuses on a different regime or task
- is superseded by a clearer later paper
- is a weak workshop variant with no distinct claim
- is only useful for final citation polishing

## Decision-First Reading Plan

For each `read-now` paper, specify:

```markdown
| Paper | Why read now | Question to answer | Decision affected |
|---|---|---|---|
```

Example decision effects:

- pursue or revise idea
- change closest baseline
- narrow claim
- add ablation
- change target venue or paper type
- route to `algorithm-design-planner`
- route to `experiment-design-planner`

## Sprint Modes

`quick`
: 5 to 12 candidate papers, 3 to 5 read-now papers, explicit uncertainty.

`full`
: 20 to 50 candidate papers, family map, closest-work table, and reading queue.

`novelty`
: emphasize closest prior work, concurrent work, and claim boundaries.

`baseline`
: emphasize standard baselines, benchmark protocols, code availability, and fairness risks.

`positioning`
: emphasize communities, venues, contribution type, accepted-paper styles, and claims to avoid.

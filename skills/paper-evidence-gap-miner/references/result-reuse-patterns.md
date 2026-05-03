# Result Reuse Patterns

Try these before proposing new compute.

## Reuse Existing Main Results

Use when the paper claim needs a headline comparison.

Check:

- methods and baselines already present
- datasets and splits match the paper claim
- metrics have known directions
- seeds or repeats are available
- failed runs are marked

Output:

- main result table
- result prose update

## Reaggregate Existing Runs

Use when raw per-run data exists but the paper needs reviewer-facing statistics.

Possible transformations:

- mean and standard deviation over seeds
- confidence interval
- per-dataset average
- macro/micro average
- best/checkpoint selection under a documented rule
- compute-normalized metric

Risk:

- changing aggregation can change the claim. Record the rule and update wording.

## Slice Existing Results

Use when a claim needs evidence under a condition.

Common slices:

- dataset/task family
- model scale
- data size
- difficulty group
- domain
- method component
- baseline family
- inference budget

Risk:

- exploratory slices should be written as analysis or limitation unless preplanned.

## Build Appendix Evidence

Use when evidence is useful but not central enough for the main paper.

Examples:

- full per-dataset table
- additional seed table
- extended baseline table
- sensitivity sweep
- failure-case gallery

Action:

- build appendix asset
- cite it from main text only if needed

## Convert Existing Result to Limitation

Use when a result does not support the intended strong claim but reveals a boundary.

Action:

- route to `limitations-scope-writer`
- downgrade the claim
- use `experiment-story-writer` for mixed-result prose

## Reuse Existing Diagnostics

Use when a mechanism claim needs support.

Examples:

- ablation already logged
- sensitivity sweep exists
- component comparison exists
- training curve suggests mechanism

Action:

- build a compact figure/table
- avoid causal language if diagnostic evidence is weak

## Minimal New Compute Criteria

Only propose new compute when:

- no existing CSV/log/report can answer the claim
- claim is central enough to defend
- the required comparison is fair and specific
- the experiment matrix is minimal
- compute budget and deadline make it feasible

If these criteria fail, narrow or cut the claim.

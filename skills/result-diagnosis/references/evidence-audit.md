# Evidence Audit

Inspect primary artifacts before interpreting results.

## Provenance

Check:

- git commit
- branch or worktree
- dirty state at run time, if known
- command or job script
- config file and overrides
- environment or package version
- hardware type
- run ID and output directory

Missing provenance usually means the result is not paper-grade.

## Data

Check:

- dataset name and version
- train/validation/test split
- preprocessing
- sample count
- filtering
- seed for split or data order
- leakage risk
- whether baseline and method used identical data

## Method and Baseline

Check:

- method flag enabled
- baseline flag disabled
- config diff
- architecture and parameter count
- training budget
- checkpoint selection rule
- sampler or inference procedure
- hyperparameter search space and trial count

## Metrics

Check:

- metric definition
- direction
- split
- aggregation
- confidence interval or std
- missing values
- postprocessing
- whether metrics match paper claim

Common metric bugs:

- higher/lower direction inverted
- validation and test mixed
- best checkpoint selected on test
- averaging incompatible units
- filtering failures silently

## Logs

Check:

- loss curves
- learning rate
- gradient norms if relevant
- NaNs or infs
- warnings and stderr
- runtime
- memory usage
- checkpoint save/load events
- diagnostic logs

## Figures and Tables

Check:

- axis labels and units
- legend mapping
- whether plotted values match raw metrics
- smoothing
- clipping
- log scale
- missing seeds
- cherry-picked points

## Minimal Artifact Set

A diagnosis should ideally cite:

- command or job script
- config diff
- metric table
- log path
- figure/table path
- baseline run pointer
- method run pointer

If these are absent, mark the diagnosis low confidence.

# Paper Section Map

Use this when mapping a draft into claims, evidence, and actions.

## Abstract

Check:

- Does every major abstract claim appear in the board?
- Are result numbers final or placeholders?
- Does the abstract overstate evidence?

## Introduction

Check:

- problem motivation
- gap claim
- contribution bullets
- headline result
- limitation or scope signal

Common risks:

- contribution bullet unsupported
- novelty boundary not cited
- main result appears too late
- problem importance not evidenced

## Background / Setup

Check:

- definitions needed for method
- assumptions
- baseline description
- notation consistency

Common risks:

- setup introduces claims not later used
- assumptions hidden until appendix

## Method

Check:

- method components
- objective or algorithm
- assumptions
- implementation details
- claimed mechanism

Common risks:

- method claim lacks diagnostic
- too many knobs without ablation
- baseline difference unclear

## Experiments

Check:

- each experiment maps to a claim
- baselines and metrics are aligned
- figures/tables are discussed
- ablations isolate mechanisms
- negative or weak results are scoped

Common risks:

- table exists but does not support main claim
- missing baseline
- metric mismatch
- no seed/variance reporting

## Analysis / Discussion

Check:

- explains why results happen
- handles failure modes
- connects diagnostics to mechanism
- narrows claims where needed

Common risks:

- post-hoc story unsupported
- diagnostic/performance mismatch ignored

## Related Work

Check:

- closest work
- direct competitors
- novelty boundary
- concurrent work
- benchmark/data/metric sources

Common risks:

- related work does not protect novelty claims
- missing paper implies missing baseline

## Limitations

Check:

- accepted risks
- scope limits
- compute/data limitations
- failure cases

Common risks:

- limitations contradict abstract
- serious reviewer risk hidden instead of addressed

## Appendix

Check:

- promised details actually exist
- appendix supports main text
- no main claim depends only on hidden appendix material unless acceptable for venue

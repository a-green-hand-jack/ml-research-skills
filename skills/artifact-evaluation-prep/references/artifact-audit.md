# Artifact Audit

Use this checklist before declaring an artifact ready.

## Readiness Levels

| Level | Meaning |
|---|---|
| `ready` | Reviewer can run quickstart and core reproduction commands with documented resources. |
| `ready-with-caveats` | Main claims are covered, but some optional runs, scale, or restricted assets have clear caveats. |
| `blocked` | A reviewer is likely to fail because setup, data, checkpoints, scripts, or instructions are incomplete. |
| `not-applicable` | Artifact evaluation is not required or the paper has no runnable artifact obligation. |

## Blocking Issues

- Missing install path or environment file.
- Missing data, checkpoint, or documented substitute.
- Commands require private paths, credentials, or undocumented services.
- Expected outputs are not stated.
- Runtime or hardware exceeds reviewer budget without a smaller path.
- Paper claims cannot be mapped to commands or cached outputs.
- License or redistribution status is unclear.

## Claim Coverage Labels

- `full-run`: reviewer can reproduce the result from raw or documented inputs.
- `reduced-run`: reviewer can run a smaller version that exercises the same mechanism.
- `cached-output`: reviewer can inspect generated outputs but not regenerate them within budget.
- `manual-inspection`: reviewer can inspect code, configs, proofs, or logs.
- `out-of-scope`: not reproducible in the artifact; requires explicit justification.

## Minimum Evidence

For each core result, require:

- command or script path
- config path or parameter list
- required inputs
- expected outputs
- runtime and hardware
- comparison target in paper
- known variance or tolerance

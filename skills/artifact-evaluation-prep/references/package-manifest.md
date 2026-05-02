# Package Manifest

Create a compact manifest that lets a reviewer understand exactly what is being evaluated.

## Suggested Fields

```markdown
# Artifact Manifest

## Identity
- Paper:
- Venue:
- Artifact version:
- Code commit/tag:
- Archive/checksum:

## Directory Layout

## Environment
- OS assumptions:
- Python/CUDA/framework versions:
- Environment file:
- Docker image:

## Data and Checkpoints
| Asset | Location | Size | License | Required for | Checksum |
|---|---|---:|---|---|---|

## Reproduction Commands
| Claim/result | Command | Expected output | Runtime | Hardware | Priority |
|---|---|---|---|---|---|

## Known Limitations

## Contact or Support Policy
```

## Rules

- Include exact version identifiers rather than "latest".
- Include checksums for downloaded archives when practical.
- Separate required assets from optional extended assets.
- Do not include secrets, private hostnames, or local absolute paths unless they are intentionally user-specific and clearly marked.

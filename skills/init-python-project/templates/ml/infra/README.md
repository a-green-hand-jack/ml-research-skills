# Infrastructure

## Adding a new compute environment

1. Copy `envs/cluster.yaml.example` to `envs/<cluster-name>.yaml`
2. Fill in the actual paths for that cluster
3. Run experiments with `ENV=<cluster-name> uv run python experiments/train.py`

Never hardcode cluster paths in `src/` or `experiments/`.

## Remote Project Memory

If the project is edited locally but executed remotely, keep these files current:

- `infra/remote-projects.yaml` for stable shared mapping and policy
- `docs/ops/current-status.md` for cross-session working memory
- `docs/ops/decision-log.md` for durable workflow decisions
- `.agent/local-overrides.yaml` for private machine-specific values

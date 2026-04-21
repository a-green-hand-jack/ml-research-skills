# Infrastructure

## Adding a new compute environment

1. Copy `envs/cluster.yaml.example` to `envs/<cluster-name>.yaml`
2. Fill in the actual paths for that cluster
3. Run experiments with `ENV=<cluster-name> uv run python experiments/train.py`

Never hardcode cluster paths in `src/` or `experiments/`.

import os
from pathlib import Path

import yaml


def load_config(experiment_config: str = "base") -> dict:
    """Load merged config: infra env + experiment yaml."""
    root = Path(__file__).parent.parent
    env = os.getenv("ENV", "local")

    env_cfg_path = root / "infra" / "envs" / f"{env}.yaml"
    if not env_cfg_path.exists():
        raise FileNotFoundError(
            f"No infra config for ENV={env!r}. Create {env_cfg_path} from cluster.yaml.example."
        )

    with open(env_cfg_path, encoding="utf-8") as f:
        cfg = yaml.safe_load(f)

    exp_cfg_path = root / "experiments" / "configs" / f"{experiment_config}.yaml"
    if exp_cfg_path.exists():
        with open(exp_cfg_path, encoding="utf-8") as f:
            cfg.update(yaml.safe_load(f) or {})

    return cfg

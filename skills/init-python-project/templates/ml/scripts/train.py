#!/usr/bin/env python3
"""Training script."""

import os
from pathlib import Path

from dotenv import load_dotenv

from {{PACKAGE_NAME}}.data import load_data
from {{PACKAGE_NAME}}.models import create_model
from {{PACKAGE_NAME}}.utils import setup_logging


load_dotenv()


def main():
    """Main training function."""
    logger = setup_logging("train")

    data_dir = Path(os.getenv("DATA_DIR", "data"))
    outputs_dir = Path(os.getenv("OUTPUTS_DIR", "outputs"))

    logger.info("Starting training...")

    train_data = load_data(data_dir / "processed" / "train.csv")
    model = create_model()

    model_path = outputs_dir / "models" / "model.pth"
    model_path.parent.mkdir(parents=True, exist_ok=True)

    logger.info("Loaded %s training records", len(train_data))
    logger.info("Model initialized: %s", type(model).__name__)
    logger.info("Model path: %s", model_path)


if __name__ == "__main__":
    main()

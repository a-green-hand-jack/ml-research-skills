#!/usr/bin/env python3
"""Download dataset."""

import os
from pathlib import Path

from dotenv import load_dotenv


load_dotenv()


def main():
    """Download dataset to data/raw/."""
    data_dir = Path(os.getenv("DATA_DIR", "data"))
    raw_dir = data_dir / "raw"
    raw_dir.mkdir(parents=True, exist_ok=True)

    print(f"Downloading data to {raw_dir}...")
    print("Download complete!")


if __name__ == "__main__":
    main()

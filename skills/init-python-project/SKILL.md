---
name: init-python-project
description: Initialize Python Project (New or Fork). Use when the user wants to create a new production-ready Python/ML project structure, or fork and enhance an existing one. Uses uv for environment management.
argument-hint: (interactive — no arguments needed, the skill asks questions)
allowed-tools: Read, Write, Edit, Bash, Glob
---

# Initialize Python Project (New or Fork)

You are helping the user create a production-ready Python project structure or enhance an existing project with best practices.

## Project Types

This command supports two scenarios:
1. **New Project**: Create a new Python project from scratch
2. **Fork/Enhancement**: Clone an existing project and enhance it with missing components

## Standard Project Structure (ML Research)

The ML project layout follows a **four-layer architecture** with strict one-way dependencies:
`infra` → `experiments/eval` → `src`. Lower layers never import from higher layers.

```
<project-name>/
├── src/
│   └── <package_name>/          # Layer 1: Algorithm core (pure, portable)
│       ├── __init__.py
│       ├── models/              # Core model/algorithm definitions
│       ├── data/                # Core data abstractions (no hardcoded paths)
│       └── utils/               # Shared utilities
├── experiments/                 # Layer 2: Experiment logic ("what to run")
│   ├── configs/                 # Experiment configs (yaml)
│   │   └── base.yaml
│   ├── config.py                # Loads infra/envs/<ENV>.yaml + configs/
│   ├── train.py                 # Training entry point
│   ├── evaluate.py              # Evaluation entry point
│   └── README.md
├── eval/                        # Layer 3: Evaluation & baselines
│   ├── benchmarks/              # Benchmark datasets & scoring scripts
│   ├── baselines/               # Baseline implementations
│   │   └── reproduced/          # Self-reproduced baselines (your code)
│   └── metrics.py               # Shared evaluation metrics
├── infra/                       # Layer 4: Platform configs ("how to run")
│   ├── envs/                    # One yaml per compute environment
│   │   ├── local.yaml           # Local dev machine
│   │   └── <cluster>.yaml       # HPC cluster (add one per new cluster)
│   ├── submit/                  # Job submission scripts
│   │   └── slurm/
│   └── README.md
├── tests/                       # Unit tests for src/ only
│   ├── __init__.py
│   ├── data/                    # Test-specific data (isolated)
│   ├── outputs/                 # Test outputs (isolated)
│   ├── conftest.py
│   └── ...                      # Mirror src/ structure
├── docs/
│   ├── outlines/
│   │   ├── project_plan.md
│   │   └── progress.md
│   └── dev/
│       ├── feature_template.md
│       └── features/
├── .gitmodules                  # Baseline git submodules (if any)
├── .vscode/
│   └── settings.json
├── .cursor/
│   └── settings.json
├── .claude/
│   └── commands/
├── .env                         # Not committed — fill from .env.example
├── .env.example
├── .gitignore
├── pyproject.toml
├── README.md
└── CLAUDE.md
```

### Layer rules

| Layer | What lives here | May import from |
|---|---|---|
| `src/<pkg>/` | Core algorithm, pure Python | nothing in this repo |
| `experiments/` | Training / eval entry points | `src/<pkg>/` |
| `eval/` | Benchmarks, baselines | `src/<pkg>/` |
| `infra/` | Cluster configs, submit scripts | nothing |

Migrating to a new HPC = add one yaml to `infra/envs/`. Zero science code changes.

## Workflow

### Step 1: Ask User for Project Information

Ask the user:

1. **Project type**:
   - `new` - Create new project from scratch
   - `fork` - Clone and enhance existing project

2. **If new project**:
   - Project name (e.g., `my-ml-project`)
   - Package name (e.g., `my_ml_project`, defaults to snake_case of project name)
   - Short description
   - Python version (default: 3.11)
   - Project type: `ml` (machine learning), `web` (web app), `lib` (library), `general`

3. **If fork project**:
   - GitHub repository URL (SSH format)
   - Do you want to create a fork on GitHub or just clone?

4. **For both**:
   - GitHub repository URL for this project (can skip and add later)
   - Author name and email

### Step 2A: Create New Project

#### 2A.1: Initialize UV Project

```bash
# Create project directory
mkdir <project-name>
cd <project-name>

# Initialize uv project
uv init --name <package_name> --python <version>

# Create src structure
mkdir -p src/<package_name>/{models,data,utils}
touch src/<package_name>/__init__.py
touch src/<package_name>/models/__init__.py
touch src/<package_name>/data/__init__.py
touch src/<package_name>/utils/__init__.py
```

#### 2A.2: Create Directory Structure

```bash
# Layer 2 — experiments
mkdir -p experiments/configs
touch experiments/README.md

# Layer 3 — eval & baselines
mkdir -p eval/{benchmarks,baselines/reproduced}
touch eval/metrics.py

# Layer 4 — infra
mkdir -p infra/envs infra/submit/slurm
touch infra/README.md

# Tests (src/ only)
mkdir -p tests/{data,outputs,models,data_tests,utils}
touch tests/__init__.py
touch tests/conftest.py

# Docs
mkdir -p docs/{outlines,dev/features}

# IDE configurations
mkdir -p .vscode .cursor .claude/commands

# Environment file
touch .env .env.example
```

#### 2A.3: Configure pyproject.toml for Editable Install

Edit `pyproject.toml` to add:

```toml
[project]
name = "<package_name>"
version = "0.1.0"
description = "<description>"
authors = [
    {name = "<author_name>", email = "<author_email>"}
]
readme = "README.md"
requires-python = ">= <version>"
dependencies = [
    # Add based on project type
]

[project.optional-dependencies]
dev = [
    "pytest>=7.4.0",
    "pytest-cov>=4.1.0",
    "black>=23.0.0",
    "ruff>=0.1.0",
    "mypy>=1.5.0",
]

# For ML projects, add:
ml = [
    "torch>=2.0.0",
    "numpy>=1.24.0",
    "pandas>=2.0.0",
    "scikit-learn>=1.3.0",
    "matplotlib>=3.7.0",
    "seaborn>=0.12.0",
    "tqdm>=4.65.0",
]

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = "test_*.py"
python_functions = "test_*"
addopts = "-v --cov=src/<package_name> --cov-report=html --cov-report=term"

[tool.black]
line-length = 100
target-version = ['py311']

[tool.ruff]
line-length = 100
select = ["E", "F", "I", "N", "W"]

[tool.mypy]
python_version = "<version>"
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true
```

#### 2A.4: Create Infra Environment Configs

Create `infra/envs/local.yaml` (template — user fills actual paths):

```yaml
# Platform: local development machine
data_root: ~/data
checkpoint_root: ~/checkpoints
output_root: ~/outputs
n_gpus: 1
```

Create `infra/envs/cluster.yaml.example` (rename and fill per HPC):

```yaml
# Platform: <cluster name>
# Usage: ENV=<cluster> uv run python experiments/train.py
data_root: /path/to/shared/datasets
checkpoint_root: /path/to/user/checkpoints
output_root: /path/to/user/outputs
n_gpus: 8
partition: gpu
```

Create `experiments/config.py`:

```python
import os, yaml
from pathlib import Path

def load_config(experiment_config: str = "base") -> dict:
    """Load merged config: infra env + experiment yaml.

    Usage: ENV=kaust uv run python experiments/train.py
    """
    root = Path(__file__).parent.parent
    env = os.getenv("ENV", "local")

    env_cfg_path = root / "infra" / "envs" / f"{env}.yaml"
    if not env_cfg_path.exists():
        raise FileNotFoundError(
            f"No infra config for ENV={env!r}. "
            f"Create {env_cfg_path} from cluster.yaml.example."
        )
    with open(env_cfg_path) as f:
        cfg = yaml.safe_load(f)

    exp_cfg_path = root / "experiments" / "configs" / f"{experiment_config}.yaml"
    if exp_cfg_path.exists():
        with open(exp_cfg_path) as f:
            cfg.update(yaml.safe_load(f) or {})

    return cfg
```

Create `experiments/configs/base.yaml`:

```yaml
# Base experiment config (platform-agnostic)
seed: 42
batch_size: 32
max_epochs: 100
learning_rate: 1.0e-4
```

Create `infra/README.md`:

```markdown
# Infrastructure

## Adding a new compute environment

1. Copy `envs/cluster.yaml.example` → `envs/<cluster-name>.yaml`
2. Fill in the actual paths for that cluster
3. Run experiments with: `ENV=<cluster-name> uv run python experiments/train.py`

Never hardcode paths in `src/` or `experiments/`. All paths come from `infra/envs/`.
```

#### 2A.5: Create Baseline Submodule Placeholders

Create `eval/baselines/README.md`:

```markdown
# Baselines

## External baselines (git submodules)
Add published baselines as submodules:
```bash
git submodule add https://github.com/<author>/<repo> eval/baselines/<name>
git submodule update --init --recursive
```

## Reproduced baselines
Self-reproduced code goes in `eval/baselines/reproduced/<name>/`.
```

#### 2A.6: Install Package in Editable Mode

```bash
# Add pyyaml for config loading
uv add pyyaml

# Install package in editable mode with dev dependencies
uv pip install -e ".[dev]"

# For ML projects:
uv pip install -e ".[dev,ml]"
```

### Step 2B: Fork and Enhance Existing Project

#### 2B.1: Clone Repository

```bash
# Clone the repository
git clone <github-ssh-url> <project-name>
cd <project-name>

# If forking, set up upstream
git remote add upstream <original-repo-url>
```

#### 2B.2: Analyze Existing Structure

Check what already exists:

```bash
# List current structure
ls -la

# Check for pyproject.toml, setup.py, requirements.txt
# Check existing directories
```

#### 2B.3: Identify Missing Components

Compare existing structure with standard structure and identify missing:
- Documentation directories (docs/outlines, docs/dev, docs/src)
- Test structure (tests/data, tests/outputs)
- Scripts directory
- Configuration files (.env.example, CLAUDE.md)
- IDE configurations

#### 2B.4: Add Missing Components

Create only the missing directories and files:

```bash
# Example: If docs/outlines is missing
mkdir -p docs/outlines

# If tests/data is missing
mkdir -p tests/{data,outputs}

# If .env.example is missing
touch .env.example
```

#### 2B.5: Enhance pyproject.toml

If project uses `requirements.txt`, offer to migrate to `pyproject.toml`:

```bash
# Install uv if not present
# Create pyproject.toml from requirements.txt
uv init

# Install existing requirements
uv pip install -r requirements.txt

# Add to pyproject.toml
```

If `pyproject.toml` exists but lacks editable install config, add it.

### Step 3: Create Template Files

#### 3.1: .gitignore

```gitignore
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# Virtual Environment
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/
.uv/

# IDE
.vscode/
.idea/
*.swp
*.swo
*~
.cursor/

# Testing
.pytest_cache/
.coverage
htmlcov/
.tox/
.hypothesis/

# Experiment outputs (large, machine-specific)
experiments/outputs/
experiments/runs/
experiments/wandb/

# Infra secrets (actual env yamls with real paths)
# Track only *.yaml.example; actual yamls are local
infra/envs/*.yaml
!infra/envs/local.yaml       # keep local.yaml as reference
!infra/envs/*.yaml.example

# Logs
*.log
logs/

# OS
.DS_Store
Thumbs.db

# Environment variables
.env

# Model checkpoints
*.pth
*.ckpt
*.pt
```

#### 3.2: .env.example

```bash
# --- Compute environment selector ---
# Set to the filename (without .yaml) in infra/envs/ for your current machine.
# Example: ENV=local  or  ENV=kaust  or  ENV=lambda
ENV=local

# --- API keys (never hardcode these in source) ---
HF_TOKEN=your_hf_token_here
WANDB_API_KEY=your_wandb_key_here
OPENAI_API_KEY=your_openai_key_here   # if needed
```

#### 3.3: .env (create empty, user will fill)

```bash
# Copy from .env.example and fill in actual values
# This file is not committed to git
```

#### 3.4: README.md

```markdown
# <Project Name>

<Short description>

## Installation

### Prerequisites
- Python <version>
- uv (recommended) or pip

### Setup

1. Clone the repository:
```bash
git clone <repo-url>
cd <project-name>
```

2. Install dependencies:
```bash
# Using uv (recommended)
uv sync

# Install in editable mode
uv pip install -e ".[dev]"

# For ML projects
uv pip install -e ".[dev,ml]"
```

3. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your actual values
```

## Project Structure

- `src/<package_name>/` - Main source code
  - `models/` - Model definitions
  - `data/` - Data loading and processing
  - `utils/` - Utility functions
- `tests/` - Unit tests (mirrors src/ structure)
- `docs/` - Documentation
  - `outlines/` - Project roadmap and progress
  - `dev/` - Feature development tracking
  - `src/` - Module documentation
- `data/` - Project data
- `outputs/` - Model outputs and results
- `scripts/` - Executable scripts
- `experiments/` - Experiment tracking

## Usage

### Training
```bash
python scripts/train.py
```

### Testing
```bash
pytest tests/
```

## Development

### Running Tests
```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src/<package_name>

# Run specific test file
pytest tests/models/test_layers.py
```

### Code Quality
```bash
# Format code
black src/ tests/

# Lint code
ruff check src/ tests/

# Type checking
mypy src/
```

## Documentation

See `docs/` for detailed documentation:
- `docs/outlines/` - Project planning and milestones
- `docs/dev/` - Feature development tracking
- `docs/src/` - Module documentation and dependencies

## Contributing

1. Create a new branch for your feature
2. Write tests for your changes
3. Update documentation in `docs/`
4. Submit a pull request

## License

[Specify license]

## Authors

- <Author Name> <<email>>
```

#### 3.5: CLAUDE.md

```markdown
# Claude Code Instructions for <Project Name>

## Project Overview

<Brief description of the project>

## Four-Layer Architecture

This project uses a strict layered structure. **Dependencies flow one way only** — lower layers never import from higher layers.

| Layer | Directory | Role |
|---|---|---|
| 1 | `src/<pkg>/` | Algorithm core — pure, portable, no paths |
| 2 | `experiments/` | Entry points — what to run |
| 3 | `eval/` | Benchmarks and baselines |
| 4 | `infra/` | Platform configs — how to run |

### Rules you must follow

- **NEVER hardcode file paths** in `src/` or `experiments/`. All paths come from `infra/envs/<ENV>.yaml` via `experiments/config.py`.
- **Run experiments** with `ENV=<name> uv run python experiments/train.py`. The `ENV` var selects the cluster config.
- **Adding a new baseline**: if it's a published repo, add it as a git submodule under `eval/baselines/`; if self-reproduced, put it in `eval/baselines/reproduced/`.
- **Adding a new cluster**: copy `infra/envs/cluster.yaml.example` → `infra/envs/<cluster>.yaml`, fill in paths. No other files change.

## Development Principles

1. **Test-Driven Development**
   - Unit tests cover `src/` only — use isolated `tests/data/` and `tests/outputs/`
   - Run tests before committing: `pytest`

2. **Code Quality**
   - Format with `black`, lint with `ruff`, type-check with `mypy`
   - All dependencies via `pyproject.toml`; editable install via `uv pip install -e .`

## Project Structure Rules

### `src/<pkg>/` — Algorithm core
- Pure Python, minimal dependencies, no hardcoded paths
- Every module has corresponding tests in `tests/` (mirror structure)

### `experiments/` — What to run
- Entry points load config via `experiments/config.py`
- Platform-agnostic: runs identically on any machine given the right `ENV=`

### `eval/` — Evaluation
- Benchmark scripts and metrics in `eval/benchmarks/` and `eval/metrics.py`
- External baselines as git submodules; reproduced baselines in `eval/baselines/reproduced/`

### `infra/` — How to run
- One yaml per compute environment in `infra/envs/`
- Slurm/LSF submit scripts in `infra/submit/`
- Actual cluster yamls with real paths are gitignored (sensitive); share `.yaml.example` instead

## When Adding New Features

1. **Create feature doc**: `docs/dev/features/<feature_name>.md`
2. **Implement in src**: `src/<package_name>/<module>/<feature>.py`
3. **Write tests**: `tests/<module>/test_<feature>.py`
4. **Update module doc**: `docs/src/<module>.md`
5. **Update dependencies**: Document in `docs/src/dependencies.md`

## Common Tasks

### Adding a New Model

1. Create: `src/<package_name>/models/<model_name>.py`
2. Test: `tests/models/test_<model_name>.py`
3. Document: `docs/src/models.md`
4. Feature track: `docs/dev/features/<model_name>.md`

### Adding a New Data Loader

1. Create: `src/<package_name>/data/<loader_name>.py`
2. Test: `tests/data_tests/test_<loader_name>.py`
   - Use `tests/data/` for test datasets
3. Document: `docs/src/data.md`

### Adding a New Script

1. Create: `scripts/<script_name>.py`
2. Use environment variables from `.env`
3. Import from installed package: `from <package_name> import ...`
4. Document usage in `README.md`

## Environment Variables

Always use `python-dotenv`:

```python
from dotenv import load_dotenv
import os

load_dotenv()

HF_HOME = os.getenv('HF_HOME')
HF_TOKEN = os.getenv('HF_TOKEN')
```

## Testing Guidelines

- Use `pytest` fixtures in `tests/conftest.py`
- Isolated test data in `tests/data/`
- Test outputs go to `tests/outputs/`
- Aim for >80% code coverage
- Run before committing: `pytest --cov=src/<package_name>`

## Important Reminders

- ✓ Always create tests for new code
- ✓ Always update documentation
- ✓ Use editable install (no relative imports)
- ✓ Keep tests isolated from main data/outputs
- ✓ Track feature development in docs/dev/
- ✓ Document module dependencies
```

#### 3.6: tests/conftest.py

```python
"""Pytest configuration and fixtures."""
import pytest
from pathlib import Path
import shutil

# Test directories
TEST_DATA_DIR = Path(__file__).parent / "data"
TEST_OUTPUTS_DIR = Path(__file__).parent / "outputs"


@pytest.fixture(scope="session", autouse=True)
def setup_test_dirs():
    """Create test directories if they don't exist."""
    TEST_DATA_DIR.mkdir(exist_ok=True)
    TEST_OUTPUTS_DIR.mkdir(exist_ok=True)
    yield
    # Optional: Clean up test outputs after all tests
    # shutil.rmtree(TEST_OUTPUTS_DIR, ignore_errors=True)
    # TEST_OUTPUTS_DIR.mkdir(exist_ok=True)


@pytest.fixture
def test_data_dir():
    """Provide path to test data directory."""
    return TEST_DATA_DIR


@pytest.fixture
def test_outputs_dir():
    """Provide path to test outputs directory."""
    return TEST_OUTPUTS_DIR


@pytest.fixture(autouse=True)
def reset_test_outputs():
    """Clean test outputs before each test."""
    if TEST_OUTPUTS_DIR.exists():
        for item in TEST_OUTPUTS_DIR.iterdir():
            if item.is_file():
                item.unlink()
            elif item.is_dir():
                shutil.rmtree(item)
    yield
```

#### 3.7: docs/outlines/project_plan.md

```markdown
# Project Plan: <Project Name>

## Overview
<Brief project description and goals>

## Objectives
1. [Objective 1]
2. [Objective 2]
3. [Objective 3]

## Timeline

### Phase 1: Foundation (Weeks 1-2)
- [ ] Set up project structure
- [ ] Implement core data loading
- [ ] Set up testing framework

### Phase 2: Core Development (Weeks 3-6)
- [ ] Implement main models
- [ ] Add training pipeline
- [ ] Create evaluation metrics

### Phase 3: Refinement (Weeks 7-8)
- [ ] Optimize performance
- [ ] Add documentation
- [ ] Write examples

### Phase 4: Release (Week 9+)
- [ ] Final testing
- [ ] Prepare release
- [ ] Write publication/blog

## Architecture

### Core Components
1. **Data Module**: Data loading and preprocessing
2. **Models Module**: Model definitions and architectures
3. **Training Module**: Training loops and optimization
4. **Evaluation Module**: Metrics and evaluation

### Dependencies
See `docs/src/dependencies.md` for detailed module dependencies.

## Success Criteria
- [ ] All tests passing
- [ ] Code coverage > 80%
- [ ] Documentation complete
- [ ] Performance benchmarks met
```

#### 3.8: docs/outlines/progress.md

```markdown
# Project Progress

Last updated: [Date]

## Current Status
**Phase**: [Current phase]
**Progress**: [X]%

## Completed Milestones
- ✓ [Milestone 1] - [Date]
- ✓ [Milestone 2] - [Date]

## In Progress
- [ ] [Current task 1]
- [ ] [Current task 2]

## Upcoming
- [ ] [Next task 1]
- [ ] [Next task 2]

## Blockers
- [None / List blockers]

## Notes
[Any important notes or decisions]
```

#### 3.9: docs/dev/feature_template.md

```markdown
# Feature: [Feature Name]

**Status**: [Planning / In Progress / Testing / Complete]
**Started**: [Date]
**Completed**: [Date]

## Overview
Brief description of the feature and its purpose.

## Design
### Architecture
[How this feature fits into the overall architecture]

### Dependencies
- Depends on: [List modules this depends on]
- Used by: [List modules that will use this]

### API Design
```python
# Example usage
from <package_name>.module import FeatureName

feature = FeatureName(param1, param2)
result = feature.process(data)
```

## Implementation

### Files Created/Modified
- `src/<package_name>/module/feature.py` - Main implementation
- `tests/module/test_feature.py` - Unit tests
- `docs/src/module.md` - Documentation updated

### Key Components
1. [Component 1]: Description
2. [Component 2]: Description

## Testing

### Test Cases
- [ ] Test basic functionality
- [ ] Test edge cases
- [ ] Test error handling
- [ ] Test integration with other modules

### Test Results
```bash
pytest tests/module/test_feature.py -v
# Results:
```

### Coverage
```bash
pytest tests/module/test_feature.py --cov
# Coverage: XX%
```

## Documentation
- [ ] API documentation in docstrings
- [ ] Module documentation updated (`docs/src/module.md`)
- [ ] Dependencies documented (`docs/src/dependencies.md`)
- [ ] Usage examples added

## Performance
[Any performance considerations or benchmarks]

## Future Improvements
- [Improvement 1]
- [Improvement 2]

## Notes
[Any additional notes, decisions, or learnings]
```

#### 3.10: docs/src/dependencies.md

```markdown
# Module Dependencies

Visual representation of how modules depend on each other.

## Dependency Graph

```
utils (no dependencies)
  ↑
data (depends on: utils)
  ↑
models (depends on: utils)
  ↑
training (depends on: models, data, utils)
  ↑
evaluation (depends on: models, data, utils)
```

## Detailed Dependencies

### utils
- **Purpose**: Utility functions and helpers
- **Dependencies**: None (base module)
- **Used by**: data, models, training, evaluation
- **Documentation**: `docs/src/utils.md`

### data
- **Purpose**: Data loading and preprocessing
- **Dependencies**: utils
- **Used by**: models, training, evaluation
- **Documentation**: `docs/src/data.md`

### models
- **Purpose**: Model definitions and architectures
- **Dependencies**: utils
- **Used by**: training, evaluation
- **Documentation**: `docs/src/models.md`

### training
- **Purpose**: Training loops and optimization
- **Dependencies**: models, data, utils
- **Used by**: scripts
- **Documentation**: `docs/src/training.md`

### evaluation
- **Purpose**: Evaluation metrics and validation
- **Dependencies**: models, data, utils
- **Used by**: training, scripts
- **Documentation**: `docs/src/evaluation.md`

## Circular Dependencies

**IMPORTANT**: Avoid circular dependencies!

Current circular dependencies: [None / List if any]

## External Dependencies

See `pyproject.toml` for third-party package dependencies.
```

#### 3.11: scripts/train.py

```python
#!/usr/bin/env python3
"""Training script."""
from dotenv import load_dotenv
import os
from pathlib import Path

# Load environment variables
load_dotenv()

# Import from installed package (editable mode)
from <package_name>.data import load_data
from <package_name>.models import create_model
from <package_name>.utils import setup_logging

def main():
    """Main training function."""
    # Setup
    logger = setup_logging("train")

    # Get paths from environment
    data_dir = Path(os.getenv("DATA_DIR", "data"))
    outputs_dir = Path(os.getenv("OUTPUTS_DIR", "outputs"))

    logger.info("Starting training...")

    # Load data
    train_data = load_data(data_dir / "processed" / "train.csv")

    # Create model
    model = create_model()

    # Train
    # ... training code ...

    # Save model
    model_path = outputs_dir / "models" / "model.pth"
    model_path.parent.mkdir(parents=True, exist_ok=True)
    # torch.save(model.state_dict(), model_path)

    logger.info(f"Model saved to {model_path}")

if __name__ == "__main__":
    main()
```

#### 3.12: scripts/download_data.py

```python
#!/usr/bin/env python3
"""Download dataset."""
from dotenv import load_dotenv
import os
from pathlib import Path

load_dotenv()

def main():
    """Download dataset to data/raw/."""
    data_dir = Path(os.getenv("DATA_DIR", "data"))
    raw_dir = data_dir / "raw"
    raw_dir.mkdir(parents=True, exist_ok=True)

    print(f"Downloading data to {raw_dir}...")

    # Download logic here
    # Example: use huggingface datasets, kaggle API, etc.

    print("Download complete!")

if __name__ == "__main__":
    main()
```

#### 3.13: .vscode/settings.json

```json
{
  "python.defaultInterpreterPath": "${workspaceFolder}/.venv/bin/python",
  "python.testing.pytestEnabled": true,
  "python.testing.pytestArgs": ["tests"],
  "python.formatting.provider": "black",
  "python.linting.enabled": true,
  "python.linting.ruffEnabled": true,
  "editor.formatOnSave": true,
  "editor.codeActionsOnSave": {
    "source.organizeImports": true
  },
  "[python]": {
    "editor.defaultFormatter": "ms-python.black-formatter",
    "editor.formatOnSave": true,
    "editor.rulers": [100]
  },
  "files.exclude": {
    "**/__pycache__": true,
    "**/*.pyc": true,
    "**/.pytest_cache": true,
    "**/.mypy_cache": true,
    "**/.ruff_cache": true
  },
  "python.analysis.typeCheckingMode": "basic"
}
```

### Step 4: Initialize Git Repository

```bash
# Initialize git
git init

# Placeholder files so empty dirs are tracked
touch experiments/configs/.gitkeep
touch eval/benchmarks/.gitkeep
touch eval/baselines/reproduced/.gitkeep
touch infra/submit/slurm/.gitkeep
touch tests/data/.gitkeep
touch tests/outputs/.gitkeep

# Add all files
git add .

# Create initial commit
git commit -m "Initial ML research project structure

- Four-layer architecture: src / experiments / eval / infra
- Platform-portable: cluster switching via ENV= + infra/envs/*.yaml
- src/<pkg> installable as editable package (uv)
- Development tooling: pytest, black, ruff, mypy"
```

### Step 5: Link to GitHub Repository

If user provided GitHub URL:

```bash
# Add remote
git remote add origin <github-ssh-url>

# Verify remote
git remote -v

# Ask user if they want to push
# If yes:
git branch -M main
git push -u origin main
```

If forked project:

```bash
# Already has remote 'origin' pointing to fork
# Add upstream if provided
git remote add upstream <original-repo-url>

# Fetch upstream
git fetch upstream

# Create development branch
git checkout -b dev
```

### Step 6: Final Setup

```bash
# Install package in editable mode
uv pip install -e ".[dev]"

# Run initial test to verify setup
pytest tests/ -v

# If no tests yet, create a placeholder
echo "def test_placeholder():\n    assert True" > tests/test_placeholder.py
pytest tests/
```

### Step 7: Display Summary

Show a complete summary:

```
✓ ML research project initialized: <project-name>
✓ Four-layer structure created:
  - src/<package_name>/  (algorithm core, editable install)
  - experiments/         (entry points + configs)
  - eval/                (benchmarks + baselines)
  - infra/envs/          (cluster configs)
✓ UV environment configured; package installed in editable mode
✓ Development tools: pytest, black, ruff, mypy
✓ Git repository initialized
✓ GitHub remote configured: <url>

Project location: <full-path>

Next steps:
1. cd <project-name>
2. cp .env.example .env  — set ENV=local (or your cluster name)
3. Fill in infra/envs/local.yaml with your actual data paths
4. Start implementing in src/<package_name>/
5. Write tests in tests/ (mirror src/ structure)
6. Run experiments: ENV=local uv run python experiments/train.py

Adding a new cluster:
  cp infra/envs/cluster.yaml.example infra/envs/<cluster>.yaml
  # fill in paths, then: ENV=<cluster> uv run python experiments/train.py

Adding a baseline:
  git submodule add https://github.com/<author>/<repo> eval/baselines/<name>
```

## Enhancement Mode (Fork/Existing Project)

When enhancing existing project:

### Analysis Checklist

1. **Directory Structure**:
   - [ ] Check if tests/ mirrors src/
   - [ ] Check for tests/data and tests/outputs isolation
   - [ ] Check for docs/outlines, docs/dev, docs/src

2. **Configuration**:
   - [ ] Check for pyproject.toml vs requirements.txt
   - [ ] Check if package is installable
   - [ ] Check for .env.example

3. **Documentation**:
   - [ ] Check for CLAUDE.md
   - [ ] Check for module documentation
   - [ ] Check for feature tracking

4. **Testing**:
   - [ ] Check for pytest configuration
   - [ ] Check for conftest.py
   - [ ] Check test coverage

### Enhancement Actions

Based on analysis, offer to:

1. **Add missing directories** (docs/outlines, docs/dev/features, docs/src, tests/data, tests/outputs)
2. **Create missing config files** (.env.example, CLAUDE.md, .vscode/settings.json)
3. **Migrate to pyproject.toml** (if using requirements.txt)
4. **Add development tools** (pytest, black, ruff, mypy)
5. **Create documentation templates** (feature_template, dependencies)
6. **Set up editable install**
7. **Create missing tests** (identify untested modules)

Show user a report:

```
Analysis of <project-name>:

Existing structure:
✓ src/ directory
✓ Basic tests/
✗ docs/outlines/ - MISSING
✗ docs/dev/ - MISSING
✗ docs/src/ - MISSING
✗ tests/data/ - MISSING (tests may share main data/)
✗ tests/outputs/ - MISSING
✓ README.md
✗ CLAUDE.md - MISSING

Configuration:
✓ pyproject.toml exists
✓ Package installable
✗ .env.example - MISSING
✗ Development dependencies incomplete

Testing:
✓ pytest configured
✗ conftest.py - MISSING
⚠ Test coverage: XX% (low)

Recommendations:
1. Add isolated test directories (tests/data, tests/outputs)
2. Create documentation structure (docs/outlines, docs/dev, docs/src)
3. Add CLAUDE.md with project instructions
4. Create .env.example for environment variables
5. Add missing tests for untested modules
6. Document module dependencies

Would you like me to:
1. Add all missing components
2. Select specific components to add
3. Generate a checklist for manual addition
```

## Error Handling

- **Directory already exists**:
  - For new project: Ask to choose different name or cancel
  - For fork: Confirm before cloning into existing directory

- **Git already initialized**:
  - Skip git init
  - Check for existing remote
  - Offer to add new remote with different name

- **Package name conflict**:
  - Check if package name is already taken on PyPI
  - Suggest alternative names

- **UV not installed**:
  - Provide installation instructions
  - Offer to use pip as fallback

- **GitHub SSH authentication fails**:
  - Check SSH key setup
  - Suggest `/setup-git-github` command
  - Offer to continue without remote

- **Existing remote with same name**:
  - Offer to use different remote name
  - Or update existing remote

## Best Practices

1. **Always use editable install**: `uv pip install -e .`
2. **Isolate test data**: Never share data/outputs between tests and main project
3. **Mirror structure**: tests/ should mirror src/ exactly
4. **Document everything**:
   - Modules in docs/src/
   - Features in docs/dev/
   - Dependencies in docs/src/dependencies.md
5. **Track progress**: Update docs/outlines/progress.md regularly
6. **Use environment variables**: Never hardcode paths or keys
7. **Type hints**: Use type hints for better IDE support and type checking
8. **Code quality**: Format, lint, type-check before committing

## Important Notes

- **Editable install**: Enables absolute imports from anywhere
- **Test isolation**: Critical for reproducible tests
- **Documentation structure**: Mirrors code structure for easy navigation
- **Feature tracking**: Essential for larger projects
- **Environment variables**: Keep secrets out of code
- **Development tools**: Enforce code quality automatically

## Security Considerations

- Never commit `.env` file
- Always provide `.env.example` as template
- Validate all file paths before creation
- Don't automatically push without confirmation
- Check for existing sensitive files before initializing git

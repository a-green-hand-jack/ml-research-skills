# {{PROJECT_NAME}}

{{DESCRIPTION}}

## Installation

### Prerequisites

- Python {{PYTHON_VERSION}}
- `uv` (recommended) or `pip`

### Setup

1. Clone the repository:

```bash
git clone {{REPO_URL}}
cd {{PROJECT_NAME}}
```

2. Install dependencies:

```bash
uv sync
uv pip install -e ".[dev]"
uv pip install -e ".[dev,ml]"
```

3. Set up environment variables:

```bash
cp .env.example .env
```

## Project Structure

- `src/{{PACKAGE_NAME}}/` - main source code
- `tests/` - unit tests
- `docs/` - documentation and planning
- `scripts/` - executable scripts
- `experiments/` - experiment tracking

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

### Code Quality

```bash
black src/ tests/
ruff check src/ tests/
mypy src/
```

## Authors

- {{AUTHOR_NAME}} <{{AUTHOR_EMAIL}}>

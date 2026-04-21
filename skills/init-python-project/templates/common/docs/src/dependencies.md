# Module Dependencies

## Dependency Graph

```text
utils (no dependencies)
  ^
data (depends on: utils)
  ^
models (depends on: utils)
  ^
training (depends on: models, data, utils)
  ^
evaluation (depends on: models, data, utils)
```

## Detailed Dependencies

- `utils`: base helpers used by the rest of the package
- `data`: data loading and preprocessing
- `models`: model definitions and architectures
- `training`: training loops and optimization
- `evaluation`: evaluation metrics and validation

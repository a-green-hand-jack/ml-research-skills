# Baselines

## External baselines (git submodules)

Add published baselines as submodules:

```bash
git submodule add https://github.com/<author>/<repo> eval/baselines/<name>
git submodule update --init --recursive
```

## Reproduced baselines

Self-reproduced code goes in `eval/baselines/reproduced/<name>/`.

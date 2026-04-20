# Release Code Checklist

Reference checklist for the `release-code` skill. Each item is checked automatically where possible; some require human confirmation.

---

## 🔐 Security

- [ ] No passwords, API keys, tokens, or credentials in any tracked file
- [ ] No credentials in git history (not just the current HEAD)
- [ ] No `.env` files committed
- [ ] No PEM/key files committed
- [ ] No internal URLs, IP addresses, or hostnames that shouldn't be public
- [ ] No personal file paths hardcoded (e.g. `/home/myname/data/`)
- [ ] No wandb API keys in config files
- [ ] No HuggingFace tokens hardcoded

**How to check history for secrets:**
```bash
git log --all --oneline --diff-filter=D -- "*.env" "*.pem" "*.key" secrets.yaml
# Or use git-secrets / truffleHog for a deep scan:
# pip install trufflehog && trufflehog git file://$(git rev-parse --show-toplevel)
```

If a secret was ever committed (even if deleted), consider the key compromised and rotate it. Use `git filter-repo` to purge from history before making the repo public.

---

## 📁 Repository Hygiene

- [ ] `.gitignore` covers: `__pycache__/`, `*.pyc`, `outputs/`, `wandb/`, `*.ckpt`, `*.pt`, `*.pth`, `*.pkl`, `.env`, `data/`
- [ ] No large binary files (>50MB) tracked in git
- [ ] No dataset files committed (link to download instead)
- [ ] No pre-trained weights committed (host on HuggingFace Hub or Google Drive)
- [ ] `outputs/` directory not committed (or explicitly excluded)
- [ ] No Jupyter notebook outputs with sensitive data (strip outputs: `nbstripout`)
- [ ] No temporary or editor files (`.DS_Store`, `*.swp`, `Thumbs.db`)

---

## 📄 Documentation

### README.md
- [ ] Paper title and authors
- [ ] Teaser figure or result image
- [ ] One-paragraph abstract or description
- [ ] Badges (arXiv, license, stars, paper-with-code)
- [ ] Installation instructions (tested from scratch)
- [ ] Quick start / minimal working example
- [ ] Full training command(s) with important flags explained
- [ ] Evaluation command(s) with expected metrics
- [ ] Pre-trained model download links (with expected performance)
- [ ] Dataset preparation instructions (or links to official datasets)
- [ ] BibTeX citation block
- [ ] License section
- [ ] Acknowledgements (funding, compute, borrowed code)

### Other docs
- [ ] `CITATION.cff` present (GitHub shows "Cite this repository" button)
- [ ] `LICENSE` file present (not just mentioned in README)
- [ ] `CHANGELOG.md` or release notes (optional but helpful)
- [ ] Any paper-specific supplementary docs linked

---

## 📦 Reproducibility

### Environment
- [ ] `requirements.txt` OR `pyproject.toml` / `uv.lock` present
- [ ] Python version specified (in `pyproject.toml`, `.python-version`, or README)
- [ ] CUDA version documented (in README or Dockerfile)
- [ ] No pinned versions that conflict with each other (test a fresh install)
- [ ] `conda` environment export available if conda-dependent (e.g. `environment.yml`)

### Code quality
- [ ] Main entry points clearly documented (which script to run for training/eval)
- [ ] Hardcoded paths replaced with config args or relative paths
- [ ] Random seed setting is exposed / documented
- [ ] Results are deterministic or variance is documented
- [ ] Config files for the main experiments are included (e.g. `configs/`)

### Pre-trained models
- [ ] Weights hosted on HuggingFace Hub, Google Drive, or project page
- [ ] Download script or instructions provided
- [ ] Model card provided (HuggingFace) or performance table in README
- [ ] Checkpoint format documented (epoch, training loss, etc.)

---

## ⚖️ Legal

- [ ] License file present and appropriate:
  - **MIT / Apache-2.0**: permissive, good for most ML code
  - **GPL-3.0**: copyleft, use if the project is based on GPL code
  - **CC-BY-4.0**: for data, models, or non-code artifacts
- [ ] Third-party code attributed (check README acknowledgements)
- [ ] Licenses of dependencies are compatible with chosen license
- [ ] Dataset licenses permit your use and redistribution
- [ ] Pre-trained model licenses checked (e.g. LLaMA has restricted license)
- [ ] Institutional IP / export control check if required

---

## 🏷️ Git & Versioning

- [ ] Release commit on `main` (or release branch)
- [ ] Annotated git tag created (e.g. `v1.0.0`)
- [ ] Tag message includes paper title and venue
- [ ] Tag pushed to `origin`
- [ ] No uncommitted changes at release point

---

## 🚀 Publication

- [ ] GitHub repository set to **public** (if it was private)
- [ ] GitHub repository description and topics set
- [ ] GitHub release created with release notes
- [ ] arXiv abstract updated with code link (add `[Code: https://github.com/...]`)
- [ ] Project page updated with code link
- [ ] PapersWithCode submission: https://paperswithcode.com/add-paper
- [ ] Social media post / announcement (optional)

---

## 🧪 Sanity Test (Recommended)

Before making public, clone the repo into a fresh directory and verify:

```bash
# In a clean environment:
git clone https://github.com/username/repo /tmp/repo-test
cd /tmp/repo-test
pip install -r requirements.txt       # or: uv sync
python train.py --config configs/default.yaml --dry-run
python eval.py --checkpoint <downloaded-weights>
```

The installation and minimal run should work from the README alone.

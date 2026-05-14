# Venue Checklists for Appendix/Supplementary Material

## NeurIPS (Reproducibility Checklist)

NeurIPS requires authors to answer the reproducibility checklist. All items must be answered yes/no/na with a brief justification.

**Claims and Evidence**
- [ ] All claims in the abstract and main text are supported in the paper
- [ ] Experimental results are reproducible with the provided code/data/instructions
- [ ] Assumptions and limitations are stated

**Experiments**
- [ ] All statistics are computed over multiple independent runs with the number reported
- [ ] Error bars are included or an explanation is given for why they are omitted
- [ ] The compute used for the main result is reported (GPU type, hours)
- [ ] The code is released or a statement is given about why it is not
- [ ] Data is released or access instructions are provided

**Theory**
- [ ] All theorems and proofs are correct (or marked as claims)
- [ ] Proof sketch vs complete proof is clearly distinguished

**Dataset**
- [ ] Dataset license and usage terms are stated
- [ ] Personal or sensitive data is handled per applicable standards
- [ ] IRB or ethics approval is mentioned if applicable

**Model**
- [ ] Model card is included or linked (if applicable)
- [ ] Known biases, failure modes, and out-of-distribution behavior are discussed

**Broader Impact**
- [ ] A broader impact statement is included

## ICLR (Reproducibility Statement)

ICLR does not use a checkbox form but expects:

- A **reproducibility statement** section in the main paper or appendix stating:
  - where the code is available (URL or "will be released")
  - what hardware and compute was used
  - which hyperparameters are reported
  - whether all reported results are averaged over multiple seeds

- If a new dataset is introduced: license, statistics, collection methodology

**Appendix expectations for ICLR**:
- Full hyperparameter tables for all models compared
- Compute budget per experiment
- Proofs for any theoretical claims

## ICML

ICML has an **ethics review checklist** and a **reproducibility statement**.

**Ethics checklist** (mark yes/no/na):
- [ ] New assets (data, models, code): license stated
- [ ] Crowdsourced data: worker compensation stated
- [ ] Potentially harmful uses identified and addressed
- [ ] Personal data: anonymization, consent, and data protection compliance

**Reproducibility statement** should include:
- Compute resources and environment
- Hyperparameter sensitivity analysis
- Code and data availability

## ACL / EMNLP / NAACL

**Limitations section**: required in main paper (short section or paragraph)

**Ethics statement**: required for papers involving human subjects, crowdsourcing, or data privacy

**Appendix**: not strictly required but strongly recommended for:
- Full model cards for new models
- Annotation protocols and inter-annotator agreement
- Full prompts used in LLM experiments
- Detailed hyperparameter tables

## CVPR / ICCV / ECCV

**Supplementary material** (usually up to 100MB):
- Extended ablations
- More qualitative results
- Implementation and training details
- Video demos (for video/animation papers)
- Proof details

No formal checklist, but reviewers commonly ask for:
- Training curves and convergence analysis
- Failure cases
- Comparison with more baselines
- Per-class or per-scene breakdown

## General Appendix Best Practices

### What belongs in the appendix (not the main paper):
- Full proof details when the main paper gives a proof sketch
- Hyperparameter tables for all experiments
- Per-seed variance or ablation tables too long for the main paper
- Dataset statistics and preprocessing details
- Training curves and convergence plots
- Additional qualitative examples or visualizations
- IRB approval statements

### What does NOT belong in the appendix:
- The main contribution (if it is only in the appendix, reviewers may not see it)
- Claims that are stronger than what the main paper states
- New methods or techniques not introduced in the main paper
- Responses to imagined reviewer questions (rebuttals go in the rebuttal period)

### Cross-reference conventions:
- Always reference appendix sections from the relevant main-paper paragraph: "(see Appendix B)"
- Use `\appendix` in LaTeX to separate supplementary from main content
- Label appendix figures as "Figure A.1", "Figure B.1" etc. (venue-dependent)
- Appendix tables: "Table A.1", "Table B.1" etc.

# Exemplar Index

Use this index when the writing task would benefit from concrete paper examples. The exemplar cards are paraphrased writing-pattern notes, not paper summaries and not source text. They are meant to help choose section and micro-patterns for the user's paper.

## Copyright and Scope Rules

- Do not copy paper prose into the user's draft.
- Do not store long quotes from exemplar papers.
- Use official source URLs when possible: OpenReview, conference proceedings, CVF Open Access, ACL Anthology, or official conference pages.
- Treat these cards as seed examples. For a real target venue/year, inspect additional recent close exemplars when available.

## Quick Selection Matrix

| Need | Good Starting Exemplars | Load |
|---|---|---|
| LLM adaptation method with efficiency claim | LoRA | `exemplars/iclr-2022-lora-method.md` |
| NLP pretraining method with broad benchmark evidence | BERT | `exemplars/naacl-2019-bert-method.md` |
| Generative model method with theory-mechanism bridge | DDPM, Latent Diffusion | `exemplars/neurips-2020-ddpm-method.md`, `exemplars/cvpr-2022-latent-diffusion-method.md` |
| Vision architecture paper with counterintuitive claim | MLP-Mixer | `exemplars/neurips-2021-mlp-mixer-method.md` |
| Benchmark or evaluation paper | TruthfulQA, Segment Anything | `exemplars/acl-2022-truthfulqa-benchmark.md`, `exemplars/iccv-2023-segment-anything-benchmark.md` |
| Empirical study / analysis paper | Rethinking Generalization | `exemplars/iclr-2017-rethinking-generalization-analysis.md` |
| Systems paper with operational metrics | ZeRO | `exemplars/sc20-zero-systems.md` |

## Exemplar Coverage

| Exemplar | Venue | Topic | Positioning | Most useful for |
|---|---|---|---|---|
| LoRA | ICLR 2022 Poster | LLM adaptation | Method + efficiency | problem framing around full fine-tuning cost; tables that combine quality and efficiency |
| BERT | NAACL 2019 Best Long Paper | NLP pretraining | Method | simple mechanism explanation; broad benchmark result narrative |
| DDPM | NeurIPS 2020 Poster | Diffusion models | Method | theory-inspired mechanism; visual evidence and quantitative generation metrics |
| Latent Diffusion | CVPR 2022 | Vision generation | Method + efficiency | compute bottleneck framing; figure-first visual narrative |
| MLP-Mixer | NeurIPS 2021 | Vision architecture | Method / empirical challenge | counterintuitive claim; architecture diagram and benchmark tables |
| TruthfulQA | ACL 2022 Long | LLM evaluation | Benchmark + empirical finding | benchmark motivation; result interpretation that challenges scaling assumptions |
| Segment Anything | ICCV 2023 | Vision foundation model | Task + model + dataset | artifact release narrative; dataset/model/task triangulation |
| Rethinking Generalization | ICLR 2017 Oral | Generalization | Empirical study + theory | question-led empirical study; experiments that falsify conventional explanations |
| ZeRO | SC20 | Distributed training systems | Systems | workload-first framing; scalability and throughput result prose |

## How to Use an Exemplar Card

1. Match by venue and positioning first, topic second.
2. Read only one to three exemplar cards for the current writing task.
3. Extract the relevant section or micro-pattern row.
4. Apply the pattern to the user's claim and evidence.
5. If the exemplar's evidence type differs from the user's evidence type, use it only for tone or structure, not result language.

## Source URLs

- LoRA: https://openreview.net/forum?id=nZeVKeeFYf9
- BERT: https://aclanthology.org/N19-1423/
- DDPM: https://proceedings.neurips.cc/paper/2020/hash/4c5bcfec8584af0d967f1ab10179ca4b-Abstract.html
- Latent Diffusion: https://openaccess.thecvf.com/content/CVPR2022/html/Rombach_High-Resolution_Image_Synthesis_With_Latent_Diffusion_Models_CVPR_2022_paper.html
- MLP-Mixer: https://proceedings.neurips.cc/paper/2021/hash/cba0a4ee5ccd02fda0fe3f9a3e7b89fe-Abstract.html
- TruthfulQA: https://aclanthology.org/2022.acl-long.229/
- Segment Anything: https://openaccess.thecvf.com/content/ICCV2023/html/Kirillov_Segment_Anything_ICCV_2023_paper.html
- Rethinking Generalization: https://openreview.net/forum?id=Sy8gdB9xx
- ZeRO: https://sc20.supercomputing.org/proceedings/tech_paper/tech_paper_pages/pap379.html

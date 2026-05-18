# Contrastive Routing Rules — Discovery

---

## The Reference Triple: `reference-reading-summarizer` vs `reference-corpus-analyzer` vs `reference-project-synthesizer`

These three skills are the most commonly confused in the discovery domain.

**Use `reference-reading-summarizer`** when:
- Reading one paper or a small set (1–4 papers) in depth
- Extracting method details, theory, benchmarks, baselines, risks into a source card
- The goal is "what does this paper say?"

**Use `reference-corpus-analyzer`** when:
- Comparing 5+ papers side by side
- Producing a comparison matrix across method/task/benchmark dimensions
- Ranking closest work with differentiators, identifying open gaps
- The goal is "how do these papers relate to each other?"

**Use `reference-project-synthesizer`** when:
- Source cards already exist and need to be connected to the project
- The goal is "what does this literature mean for my claims, baselines, or experiments?"
- Linking sources to claims/risks/baselines/writing contract/memory

**Decision rule**:
- Reading 1–4 specific papers → `reference-reading-summarizer`
- Comparing 5+ papers for a matrix/ranking → `reference-corpus-analyzer`
- Connecting existing source cards to project memory → `reference-project-synthesizer`

---

## `research-idea-validator` vs `literature-review-sprint`

**Use `research-idea-validator`** when:
- The user has a specific idea and wants a pursue/revise/park/kill decision
- Novelty, feasibility, and reviewer risk for a particular direction need evaluation
- This is about deciding whether to start a project or change direction

**Use `literature-review-sprint`** when:
- The user wants to survey a topic area broadly
- The goal is a ranked map of canonical, closest, recent, and baseline papers
- There is no specific idea to validate — just a field or problem area to understand

**Decision rule**: Is there a specific idea to evaluate (validator) or a field to map (sprint)?

---

## `literature-review-sprint` vs `reference-corpus-analyzer`

**Use `literature-review-sprint`** when:
- Starting a broad survey from scratch
- The user doesn't have papers yet and needs help finding/ranking them
- The output is a ranked literature map with positioning implications

**Use `reference-corpus-analyzer`** when:
- Papers already exist (source cards or a corpus in `reference/`)
- The task is comparison and gap analysis, not discovery
- The output is a comparison matrix, not a reading list

**Decision rule**: Are papers already identified and in hand (corpus analyzer) or does the user need help finding and ranking them first (literature sprint)?

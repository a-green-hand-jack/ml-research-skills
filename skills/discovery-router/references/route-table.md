# Discovery Route Table

| Task type | Concrete signals | Correct skill | Avoid |
|---|---|---|---|
| Validate new idea | "should I pursue this idea", "is this novel enough", "pursue/park/kill", "FIVE+C analysis" | `research-idea-validator` | `literature-review-sprint` (that surveys a field, not an idea) |
| Survey a topic | "survey this area", "map related work", "find canonical papers", "novelty map", "what's the landscape" | `literature-review-sprint` | `reference-corpus-analyzer` (that compares, needs papers already in hand) |
| Manage reference library | "what papers do we have", "index reference/", "track new papers added", "inventory sources" | `reference-library-manager` | `reference-reading-summarizer` (that reads papers, not manages the library) |
| Read 1–4 specific papers | "read this paper", "summarize this PDF", "extract method from source", "source card for X" | `reference-reading-summarizer` | `reference-corpus-analyzer` (that's for 5+ papers as a corpus) |
| Compare 5+ papers | "compare these 10 papers", "comparison matrix", "closest-work ranking", "gap analysis across corpus" | `reference-corpus-analyzer` | `reference-reading-summarizer` (that's per-paper, not corpus-level) |
| Connect sources to project | "what does this literature mean for my claims", "link source cards to baselines", "project-level synthesis" | `reference-project-synthesizer` | `reference-corpus-analyzer` (that compares papers, not connects them to project) |
| Missing citations before submission | "did I miss any important papers", "citation coverage", "closest-work gap" | `citation-coverage-audit` | `citation-audit` (that's about metadata, not missing papers) |

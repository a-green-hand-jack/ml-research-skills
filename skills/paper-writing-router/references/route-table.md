# Paper Writing Route Table

| Task type | Concrete signals | Correct skill | Avoid |
|---|---|---|---|
| Writing contract | "no contract yet", "lock section order", "what sections do I need", "forbidden claims", "paragraph roles" | `paper-writing-contract-planner` | `paper-writing-assistant` (don't write before planning) |
| Strategic positioning | "what's my paper's contribution", "choose archetype", "claim scope", "narrative strategy" | `paper-positioning-planner` | `paper-writing-contract-planner` (positioning is before contract) |
| Venue adaptation | "reshape for NeurIPS", "ICLR style", "CVPR structure", "venue exemplars", "reviewer expectations" | `conference-writing-adapter` | `paper-writing-assistant` (adapt structure before writing) |
| Write / revise prose | "draft the method section", "revise introduction", "fill placeholder results", "claim-aware prose" | `paper-writing-assistant` | `paper-writing-contract-planner` (that plans, this writes) |
| Track writing state | "which sections are stale", "what style decisions did I make", "open writing threads", "edit impact" | `paper-writing-memory-manager` | `paper-writing-assistant` (that writes, this tracks) |
| Introduction argument | "introduction argument chain", "hook sentence", "gap paragraph", "contribution bullets" | `paper-introduction-argument-writer` | `paper-writing-assistant` (use intro specialist first) |
| Method section | "method notation", "overview figure placement", "algorithm box", "module ordering" | `method-section-explainer` | `paper-writing-assistant` (use method specialist first) |
| Results prose | "turn my table into a paragraph", "results narrative", "claim-aware experiment story" | `experiment-story-writer` | `paper-writing-assistant` (results story has a specialist) |
| Related work | "related work section", "novelty boundaries", "closest-work grouping", "citation boundary statements" | `related-work-positioning-writer` | `paper-writing-assistant` (related work has a specialist) |
| Limitations | "limitations section", "scope statement", "failure cases", "broader impact", "conclusion caveats" | `limitations-scope-writer` | `paper-writing-assistant` |
| Abstract and title | "title options", "abstract structure", "contribution list", "top-level claim" | `abstract-title-contribution-writer` | `paper-writing-assistant` |
| Single-pass consistency | "check consistency across draft", "terminology drift", "figure cross-refs", "align title/abstract/conclusion" | `paper-draft-consistency-editor` | `auto-paper-improvement-loop` (that's multi-round) |
| Multi-round improvement | "2+ review cycles", "fresh reviewer each round", "edit-whitelist", "crash-resumable improvement" | `auto-paper-improvement-loop` | `paper-draft-consistency-editor` (that's single-pass) |
| Pre-submission simulation | "what will reviewers say", "predicted scores", "reject risks", "meta-review simulation" | `paper-reviewer-simulator` | `rebuttal-strategist` (that's for real reviews) |
| Real rebuttal | "reviews arrived", "respond to reviewer 2", "plan follow-up experiments", "point-by-point" | `rebuttal-strategist` | `paper-reviewer-simulator` (that's simulated, not real) |
| Appendix / checklist | "appendix structure", "NeurIPS reproducibility checklist", "supplementary sections" | `appendix-organizer` | `submit-paper` |
| Pre-submission final | "final checklist before submission", "source hygiene", "anonymity", "bibliography check" | `submit-paper` | `camera-ready-finalizer` (that's post-acceptance) |
| Camera-ready | "accepted paper", "de-anonymize", "rebuttal promises done", "final version" | `camera-ready-finalizer` | `submit-paper` (that's pre-acceptance) |
| Fix BibTeX / citation keys | "unresolved keys", "bad DOI", "invalid label", "BibTeX metadata" | `citation-audit` | `citation-coverage-audit` (that's about missing papers) |
| Find missing citations | "missing foundational paper", "should I cite X", "closest work not cited" | `citation-coverage-audit` | `citation-audit` (that's about metadata, not coverage) |
| LaTeX layout bug | "layout issue", "overfull hbox", "figure placement", "compile log", "PDF page debug" | `latex-layout-issue-bundler` | `submit-paper` |

# CLAUDE.md — AI Agent Writing Guide for This LaTeX Project

> This document defines writing requirements and LaTeX conventions for **all AI agents** (Claude, Gemini, GPT, etc.) working on this academic paper.

---

## 0. Local vs Overleaf Compile Workflow

Do not assume the local machine has TeX Live, MacTeX, `pdflatex`, `xelatex`, or `lualatex` installed. The default workflow is:

1. Edit LaTeX source locally.
2. Review `git diff`.
3. Commit and push to GitHub when the user asks.
4. Compile in Overleaf through the GitHub-linked project.
5. Use Overleaf logs and PDF preview as the compile source of truth.

If a local LaTeX compiler is missing, do not ask the user to install TeX unless they explicitly want local compilation. Continue with static source checks and push the changes for Overleaf validation.

---

## 0.1 Paper Version Worktrees and Source Hygiene

If this paper belongs to a project control root, paper versions may live in sibling worktrees under `../paper-worktrees/`.

Use paper worktrees for:

- different conference targets with different templates or style files
- arXiv or preprint releases
- camera-ready versions
- paper-only rebuttal edits

For public-source versions such as arXiv, do not leave internal notes in `.tex` files. Remove TODOs, reviewer notes, author comments, hidden comments, private paths, and internal figure/table descriptions before source release. Keep figure/table descriptions and provenance in `.agent/` or project memory, not in public LaTeX comments.

For anonymous conference versions, enforce anonymity and venue format. Do not assume source comments are safe if the submission system asks for source upload.

---

## 1. Top Priority: Use Macros from `macros.tex`

> [!CAUTION]
> **Always prioritize macros defined in `macros.tex`.** Do NOT write raw LaTeX when a macro already exists. Before writing any math symbol, operator, or environment, check `macros.tex` first.

Examples of **required** macro usage:

| ❌ Do NOT write     | ✅ Use the macro instead |
| ------------------ | ----------------------- |
| `\mathbb{R}`       | `\R`                    |
| `\mathbb{E}`       | `\E`                    |
| `\mathbb{P}`       | `\bbP`                  |
| `\mathcal{L}`      | `\calL`                 |
| `\mathbf{x}`       | `\bx`                   |
| `\mathbf{A}`       | `\bA`                   |
| `\mathrm{argmin}`  | `\argmin`               |
| `\mathrm{Softmax}` | `\Softmax`              |
| `\partial`         | `\pa`                   |
| `\frac{1}{2}`      | `\half`                 |
| `\sum_{i=1}^N`     | `\sumN`                 |
| `\lambda`          | `\lG`                   |
| `\theta`           | `\tG`                   |
| `\sigma`           | `\sG`                   |

This rule applies to **all** LaTeX content: equations, captions, inline math, theorem statements, etc.

---

## 2. Five Mandatory Writing Rules

Every sentence you write **must** follow all five rules simultaneously:

| #   | Rule                                            | ✅ Good                                                           | ❌ Bad                                                            |
| --- | ----------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| 1   | **Use simple words**                            | "We use a transformer."                                          | "We utilize a transformer."                                      |
| 2   | **Use short sentences. No compound sentences.** | "The model learns representations. It maps genes to embeddings." | "The model learns representations and maps genes to embeddings." |
| 3   | **No passive voice**                            | "We train the model on PBMC data."                               | "The model is trained on PBMC data."                             |
| 4   | **Only present tense**                          | "We show that..." / "The model achieves..."                      | "We showed that..." / "The model achieved..."                    |
| 5   | **No adverbs**                                  | "The model converges in 10 epochs."                              | "The model converges quickly in 10 epochs."                      |

> [!CAUTION]
> These five rules are **non-negotiable**. Violating any of them requires a rewrite.

---

## 3. Section Structure Rules

- **Every section begins with a summary paragraph.** This paragraph gives the reader a high-level overview before any subsections or details.
- **The Introduction ends with an organization summary.** The last paragraph lists the structure of the rest of the paper (e.g., "In Section 2, we review... In Section 3, we describe...").

---

## 4. Cross-Reference and Citation Commands

| What you reference                           | Command         | Example                          |
| -------------------------------------------- | --------------- | -------------------------------- |
| Figure, Table, Section, Theorem, Lemma, etc. | `\cref{label}`  | `\cref{fig:overview}`            |
| Equation                                     | `\eqref{label}` | `\eqref{eq:loss}`                |
| Other paper                                  | `\cite{key}`    | `\cite{author2024}`              |

> [!IMPORTANT]
> - Do **not** use `\ref{}` — always use `\cref{}`.
> - In natbib-based templates, `\cite` is remapped to `\citep` in `macros.tex`.
> - In ACM templates, `\cite` keeps the class-native behavior.

---

## 5. Math Environments

| Environment | Command               | Label convention     |
| ----------- | --------------------- | -------------------- |
| Theorem     | `\begin{theorem}`     | `\label{thm:name}`   |
| Lemma       | `\begin{lemma}`       | `\label{lemma:name}` |
| Corollary   | `\begin{corollary}`   | `\label{coro:name}`  |
| Definition  | `\begin{definition}`  | `\label{def:name}`   |
| Assumption  | `\begin{assumption}`  | `\label{assmption:name}` |
| Remark      | `\begin{remark}`      | `\label{remark:name}` |
| Problem     | `\begin{problem}`     | `\label{prob:name}`  |
| Proposition | `\begin{proposition}` | `\label{prop:name}`  |

---

## 6. Available Math Shorthand Macros

| Category                        | Examples                                              |
| ------------------------------- | ----------------------------------------------------- |
| **Calligraphic** `\calA`–`\calZ` | `\calL` → ℒ, `\calX` → 𝒳                             |
| **Bold** `\bA`–`\bZ`, `\ba`–`\bz` | `\bA` → **A**, `\bx` → **x**                       |
| **Blackboard bold**             | `\R` → ℝ, `\E` → 𝔼, `\bbP` → ℙ                     |
| **Operators**                   | `\argmin`, `\argmax`, `\Var`, `\Softmax`, `\Sigmoid` |
| **Sums**                        | `\sumN`, `\sumK`, `\sumM`, `\sumT`, `\sumd`          |
| **Greek shortcuts**             | `\g` → γ, `\sG` → σ, `\lG` → λ, `\tG` → θ           |
| **Other**                       | `\pa` → ∂, `\half` → ½                               |

---

## 7. Comment / Annotation Macros

Use these for inline comments during drafting:

| Macro             | Color     | Who   |
| ----------------- | --------- | ----- |
| `\jerry{text}`    | Firebrick | JH    |
| `\wwm{text}`      | Blue      | WM    |
| `\jennifer{text}` | Magenta   | Jen   |
| `\ali{text}`      | Red       | Ali   |
| `\ray{text}`      | Purple    | Ray   |
| `\yibo{text}`     | Orange    | Yibo  |
| `\jieke{text}`    | Teal      | Jieke |

> Add or modify these macros in `macros.tex` to match your team.

---

## 8. Figure and Table Conventions

### Figures
```latex
\begin{figure}[t]
    \centering
    \includegraphics[width=\columnwidth]{figures/name.pdf}
    \caption{
        \textbf{Short bold title.}
        Description in present tense, active voice, simple words.
    }
    \label{fig:name}
\end{figure}
```

### Tables
```latex
\begin{table}[htbp]
    \centering
    \caption{
        \textbf{Short bold title.}
        Description follows the five writing rules.
    }
    \label{tab:name}
    \begin{tabular}{l|cccc}
        \toprule
        ...
        \midrule
        ...
        \bottomrule
    \end{tabular}
\end{table}
```

> [!NOTE]
> - Use `\toprule`, `\midrule`, `\bottomrule` — never `\hline`.
> - Bold the best result with `\textbf{}`.
> - Caption goes **above** the table.

---

## 9. Project File Structure

```
├── main.tex                 # Main document entry point
├── macros.tex               # All packages, macros, theorem environments
├── sections/
│   ├── title.tex
│   ├── abstract.tex
│   ├── intro.tex
│   ├── related.tex
│   ├── method.tex
│   ├── exp.tex
│   ├── conclusion.tex
│   ├── appendix.tex
│   └── acknowledgement.tex
├── figures/
├── tables/
└── bib/
    └── refs.bib
```

> For venue-specific requirements (e.g., NeurIPS broader impact, ICML author checklist), add the required section files and include them in `main.tex`.

---

## 10. Quick Checklist Before Submitting Any LaTeX Text

- [ ] Every sentence uses **present tense**?
- [ ] Every sentence uses **active voice**?
- [ ] No **compound sentences**?
- [ ] No **adverbs**?
- [ ] All words are **simple**?
- [ ] Section starts with a **summary paragraph**?
- [ ] Figures/tables/sections use `\cref{}`? Equations use `\eqref{}`?
- [ ] Citations use `\cite{}`?
- [ ] Tables use `\toprule`/`\midrule`/`\bottomrule`?
- [ ] Macro shortcuts used where available?

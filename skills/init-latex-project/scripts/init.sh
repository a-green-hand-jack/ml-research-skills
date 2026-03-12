#!/usr/bin/env bash
# init.sh — Initialize a LaTeX academic paper project
# Usage: init.sh <project-name> [target-dir] [--venue <iclr|cvpr|icml|acm|acl>] [--git]

set -euo pipefail

# ── Defaults ─────────────────────────────────────────────────────────────────
PROJECT_NAME=""
TARGET_DIR="."
VENUE=""
INIT_GIT=false

# ── Argument Parsing ──────────────────────────────────────────────────────────
while [[ $# -gt 0 ]]; do
  case "$1" in
    --git)
      INIT_GIT=true
      shift ;;
    --venue)
      VENUE="${2:?--venue requires an argument: iclr|cvpr|icml|acm|acl|neurips}"
      shift 2 ;;
    --venue=*)
      VENUE="${1#*=}"
      shift ;;
    -*)
      echo "ERROR: Unknown flag: $1" >&2
      echo "Usage: init.sh <project-name> [target-dir] [--venue <iclr|cvpr|icml|acm|acl|neurips>] [--git]" >&2
      exit 1 ;;
    *)
      if [[ -z "$PROJECT_NAME" ]]; then
        PROJECT_NAME="$1"
      elif [[ "$TARGET_DIR" == "." ]]; then
        TARGET_DIR="$1"
      fi
      shift ;;
  esac
done

# ── Validate ──────────────────────────────────────────────────────────────────
if [[ -z "$PROJECT_NAME" ]]; then
  echo "Usage: init.sh <project-name> [target-dir] [--venue <iclr|cvpr|icml|acm|acl|neurips>] [--git]" >&2
  exit 1
fi

# Normalize venue to lowercase
VENUE="${VENUE,,}"

SUPPORTED_VENUES="iclr cvpr icml acm acl neurips"
if [[ -n "$VENUE" && ! " $SUPPORTED_VENUES " =~ " $VENUE " ]]; then
  echo "ERROR: Unsupported venue '$VENUE'. Choose from: $SUPPORTED_VENUES" >&2
  exit 1
fi

DEST="$TARGET_DIR/$PROJECT_NAME"
SKILL_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TEMPLATES="$SKILL_DIR/templates"

if [[ -d "$DEST" ]]; then
  echo "ERROR: Directory '$DEST' already exists. Choose a different name or path." >&2
  exit 1
fi

# ── Create Directory Structure ────────────────────────────────────────────────
echo "Creating project: $PROJECT_NAME${VENUE:+ (venue: $VENUE)}"
mkdir -p "$DEST"/{sections,figures,tables,bib}

# ── Copy Base Template Files ──────────────────────────────────────────────────
cp "$TEMPLATES/macros.tex" "$DEST/macros.tex"
cp "$TEMPLATES/CLAUDE.md"  "$DEST/CLAUDE.md"

# Choose main.tex: venue-specific or generic
if [[ -n "$VENUE" && -f "$TEMPLATES/venues/$VENUE/main.tex" ]]; then
  cp "$TEMPLATES/venues/$VENUE/main.tex" "$DEST/main.tex"
else
  cp "$TEMPLATES/main.tex" "$DEST/main.tex"
fi

# ── Create Placeholder Section Files ─────────────────────────────────────────
cat > "$DEST/sections/title.tex"          <<'EOF'
Title of the Paper
EOF

cat > "$DEST/sections/abstract.tex"       <<'EOF'
TODO: Write abstract here.
EOF

cat > "$DEST/sections/intro.tex"          <<'EOF'
TODO: Write introduction here.

% Structure hint:
% 1. Opening paragraph: what is the problem?
% 2. Why is it hard?
% 3. What do we do?
% 4. Contributions list
% 5. Organization (last paragraph):
%    "In \cref{sec:related}, we review...
%     In \cref{sec:method}, we describe...
%     In \cref{sec:exp}, we evaluate..."
EOF

cat > "$DEST/sections/related.tex"        <<'EOF'
TODO: Write related work here.
EOF

cat > "$DEST/sections/method.tex"         <<'EOF'
TODO: Write method here.
EOF

cat > "$DEST/sections/exp.tex"            <<'EOF'
TODO: Write experiments here.
EOF

cat > "$DEST/sections/conclusion.tex"     <<'EOF'
TODO: Write conclusion here.
EOF

cat > "$DEST/sections/acknowledgement.tex" <<'EOF'
TODO: Add funding acknowledgments here.
EOF

cat > "$DEST/sections/appendix.tex" <<'EOF'
\section{Proofs}
\label{sec:proofs}

TODO

\section{Additional Experiments}
\label{sec:add-exp}

TODO
EOF

# ── Venue-Specific Section Files ──────────────────────────────────────────────
case "$VENUE" in
  neurips)
    cat > "$DEST/sections/impact.tex" <<'EOF'
% NeurIPS REQUIREMENT: MANDATORY, does NOT count toward the page limit.
% Discuss both positive and negative potential societal impacts.
% If impacts are minimal, you may use the minimal boilerplate below instead.

% --- Minimal boilerplate (use only if truly applicable) ---
% This paper presents work whose goal is to advance the field of machine learning.
% There are many potential societal consequences of our work, none of which we feel
% must be specifically highlighted here.

% --- Full template (recommended) ---
\textbf{Positive impacts.}
TODO: Describe the positive societal impacts of this work.

\textbf{Potential risks.}
TODO: Describe any potential negative societal impacts and how they can be mitigated.
EOF
    cat > "$DEST/sections/checklist.tex" <<'EOF'
% ── NeurIPS 2025 Paper Checklist ──────────────────────────────────────────────
% MANDATORY — does NOT count toward the page limit.
% Instructions: https://neurips.cc/public/guides/PaperChecklist
% Answer macros: \answerYes{} \answerNo{} \answerNA{} \answerTODO{}
% (Defined in neurips_2025.sty)

\section*{NeurIPS Paper Checklist}

\begin{enumerate}

\item {\bf Claims}
\item[] Question: Do the main claims made in the abstract and introduction accurately reflect the paper's contributions and scope?
\item[] Answer: \answerTODO{}
\item[] Justification: TODO
\item[] Guidelines:
\begin{itemize}
    \item The answer NA means that the abstract and introduction do not include the claims made in the paper.
    \item The abstract and/or introduction should clearly state the claims made, including the contributions made in the paper and important assumptions and limitations. A No or NA answer to this question will not be perceived well by the reviewers.
    \item The claims made should match theoretical and experimental results, and reflect how much the results can be expected to generalize to other settings.
    \item It is fine to include aspirational goals as motivation as long as it is clear that these goals are not attained by the paper.
\end{itemize}

\item {\bf Limitations}
\item[] Question: Does the paper discuss the limitations of the work performed by the authors?
\item[] Answer: \answerTODO{}
\item[] Justification: TODO
\item[] Guidelines:
\begin{itemize}
    \item The answer NA means that the paper has no limitation while the answer No means that the paper has limitations, but those are not discussed in the paper.
    \item The authors are encouraged to create a separate "Limitations" section in their paper.
    \item The paper should point out any strong assumptions and how robust the results are to violations of these assumptions (e.g., independence assumptions, noiseless settings, model well-specification, asymptotic approximations only holding locally). The authors should reflect on how these assumptions might be violated in practice and what the implications would be.
    \item The authors should reflect on the scope of the claims made, e.g., if the method has been evaluated on a few datasets or with a few runs, it is possible that the claims will not generalize to other settings.
    \item Authors should be careful not to exaggerate the claims reached from the experimental evidence.
\end{itemize}

\item {\bf Theory Assumptions and Proofs}
\item[] Question: For each theoretical result, does the paper provide the full set of assumptions and a complete proof?
\item[] Answer: \answerTODO{}
\item[] Justification: TODO
\item[] Guidelines:
\begin{itemize}
    \item The answer NA means that the paper does not include theoretical results.
    \item All the theorems, formulas, and proofs in the paper should be numbered and cross-referenced.
    \item All assumptions should be clearly stated or referenced in the statement of any theorems.
    \item The proofs can either appear in the main paper or the supplemental material, but if they appear in the supplemental material, the authors are encouraged to provide a short proof sketch to provide intuition.
    \item Inversely, any informal proof provided in the core of the paper should be complemented by formal proofs provided in appendix or supplemental material.
    \item Theorems and Lemmas that the proof relies upon should be properly referenced.
\end{itemize}

\item {\bf Experimental Result Reproducibility}
\item[] Question: Does the paper fully disclose all the information needed to reproduce the main experimental results of the paper to the extent that it affects the main claims and/or conclusions of the paper (regardless of whether the code and data are provided or not)?
\item[] Answer: \answerTODO{}
\item[] Justification: TODO
\item[] Guidelines:
\begin{itemize}
    \item The answer NA means that the paper does not include experiments.
    \item If the paper includes experiments, a No answer to this question will not be perceived well by the reviewers and may result in rejection.
    \item Experimental settings should be presented in the paper or, if not, should be reproducible from the code.
    \item The paper should indicate if "internal data" is used in experiments.
    \item All the data that is needed to reproduce the main results should be included.
    \item All the hyperparameters that are needed to reproduce the main results should be included.
    \item Ideally, the code should be submitted with the paper.
\end{itemize}

\item {\bf Open access to data and code}
\item[] Question: Does the paper provide open access to the data and code, with sufficient instructions to faithfully reproduce the main experimental results, as described in supplemental material?
\item[] Answer: \answerTODO{}
\item[] Justification: TODO
\item[] Guidelines:
\begin{itemize}
    \item The answer NA means that paper does not include experiments requiring code.
    \item Please see the NeurIPS code and data submission guidelines (\url{https://nips.cc/public/guides/CodeSubmissionPolicy}) for more details.
    \item While we encourage the release of code and data, we understand that this might not be possible, so No is an acceptable answer. Authors of accepted papers that are asked to provide code, but fail to do so in time, will be required to continue their release after the conference and will be publicly tagged with a 'No Country for Old Men' tag that will be displayed on the location of the paper.
    \item 5% of the NeurIPS 2025 submissions will be selected for a reproducibility study and submitting authors will be required to provide code and data for this purpose.
    \item All datasets used should have a license that allows usage for research purposes.
    \item For the datasets used, authors should check whether the license allows to make derivatives and publish them.
    \item Datasets that have been scraped from the web could pose richer ethical challenges and should be evaluated carefully.
    \item The authors are encouraged to release the data.
\end{itemize}

\item {\bf Experimental Setting/Details}
\item[] Question: Does the paper specify all the training and test details (e.g., data splits, hyperparameters, how they were selected) necessary to understand the results?
\item[] Answer: \answerTODO{}
\item[] Justification: TODO
\item[] Guidelines:
\begin{itemize}
    \item The answer NA means that the paper does not include experiments.
    \item The experimental setting should be presented in the core of the paper to a level of detail that is necessary to appreciate the results and make sense of them.
    \item The full details can be provided either with the code, in appendix, or as supplemental material.
\end{itemize}

\item {\bf Experiment Statistical Significance}
\item[] Question: Does the paper report error bars suitably and correctly defined or other appropriate information about the statistical significance of the experiments?
\item[] Answer: \answerTODO{}
\item[] Justification: TODO
\item[] Guidelines:
\begin{itemize}
    \item The answer NA means that the paper does not include experiments.
    \item The authors should answer "Yes" if the results are accompanied by error bars, confidence intervals, or statistical significance tests, at least for the experiments that support the main claims of the paper.
    \item The factors of uncertainty include: the random seed, the train/test split, the initialization, the choice of the training configuration.
    \item The method for calculating the error bars should be explained (closed form formula, call to a library function, bootstrap, etc.)
    \item The assumptions made should be given (e.g., Gaussian errors).
    \item It should be clear whether the error bar is the standard deviation or the standard error of the mean.
    \item It is OK to report 1-sigma error bars, but one should state it. The authors should preferably report a 2-sigma error bar than state that they have a 96\% CI, if the hypothesis of Gaussianity of errors is not verified.
    \item For asymmetric distributions, the authors should be careful not to show in tables or figures symmetric error bars that would yield results that are out of range (e.g. negative error rates).
    \item If error bars are reported in tables or figures, The authors should explain in the text how they were calculated and reference the relevant figures or tables in the text.
\end{itemize}

\item {\bf Compute Resources}
\item[] Question: For each experiment, does the paper provide sufficient information on the computer resources (type of compute, memory, time of execution) needed to reproduce the experiments?
\item[] Answer: \answerTODO{}
\item[] Justification: TODO
\item[] Guidelines:
\begin{itemize}
    \item The answer NA means that the paper does not include experiments.
    \item The paper should indicate the type of compute workers CPU or GPU, internal cluster, or cloud provider, including relevant memory and storage.
    \item The paper should provide the amount of compute required for each of the individual experimental runs as well as estimate the total compute.
    \item The paper should disclose whether the full research project required more compute than the experiments reported in the paper (e.g., preliminary or failed experiments that didn't make it into the paper).
\end{itemize}

\item {\bf Code Of Ethics}
\item[] Question: Does the research conducted in the paper conform, in every respect, with the NeurIPS Code of Ethics \url{https://neurips.cc/public/EthicsGuidelines}?
\item[] Answer: \answerYes{}
\item[] Justification: We have reviewed and comply with the NeurIPS Code of Ethics.
\item[] Guidelines:
\begin{itemize}
    \item The answer NA means that the authors have not reviewed the NeurIPS Code of Ethics.
    \item If the authors answer No, they should explain the special circumstances that require a deviation from the Code of Ethics.
    \item The authors should make sure to preserve anonymity (e.g., if there is a venue-specific anonymity period).
\end{itemize}

\item {\bf Broader Impacts}
\item[] Question: Does the paper discuss both potential positive societal impacts and negative societal impacts of the work performed?
\item[] Answer: \answerYes{}
\item[] Justification: See the Broader Impact section above.
\item[] Guidelines:
\begin{itemize}
    \item The answer NA means that there are no societal impacts of the work performed.
    \item If the authors answer NA or No, they should explain why their work has no societal impact or why the paper does not address societal impact.
    \item Examples of negative societal impacts include potential malicious or unintended uses (e.g., disinformation, generating fake profiles, surveillance), fairness considerations (e.g., deployment of technologies that could make decisions that unfairly impact specific groups), privacy considerations, and security considerations.
    \item The conference expects that many papers will be foundational research and not tied to particular applications, let alone deployments. However, if there is a direct path to any negative applications, the authors should point it out.
    \item If there is no potential negative impact, the authors should argue why that is the case.
    \item At the conference, the authors will be asked to provide a 1-paragraph statement of Broader Impacts in their submission.
    \item Papers submitted to NeurIPS are not allowed to include papers where the only contribution is making a negative baseline available.
    \item As a rule of thumb, the more likely it is that someone could use your work for harm, the more responsible you are to discuss it.
\end{itemize}

\item {\bf Safeguards}
\item[] Question: Does the paper describe safeguards that have been put in place for responsible release of data or models that have potential for misuse (e.g., pretrained language models, image generators, or scrapers)?
\item[] Answer: \answerNA{}
\item[] Justification: TODO: update if you release pretrained models or scraped datasets.
\item[] Guidelines:
\begin{itemize}
    \item The answer NA means that the paper poses no such risks.
    \item Released models that have potential for misuse or harm (e.g., pretrained language models, image generators, or scrapers) should be released with necessary safeguards to allow for controlled use of the model, e.g., in the form of an access-controlled API.
    \item Datasets that have been scraped from the web could pose richer ethical challenges and should be evaluated carefully.
    \item The authors are encouraged to provide a 1-paragraph statement of Broader Impacts in their submission.
\end{itemize}

\item {\bf Licenses for existing assets}
\item[] Question: Are the creators or original owners of assets (e.g., code, data, models), used in this paper, properly credited and are the license terms respected?
\item[] Answer: \answerTODO{}
\item[] Justification: TODO
\item[] Guidelines:
\begin{itemize}
    \item The answer NA means that the paper does not use existing assets.
    \item The authors should cite the original paper that produced the code package or dataset.
    \item The authors should state which version of the asset is used and, if possible, include a URL.
    \item The name of the license (e.g., CC-BY 4.0) should be included for each asset.
    \item Indicate if the asset is used for research purposes only.
    \item If the code is taken from GitHub repos, the authors should make sure that the GitHub repo has a license and the license is compatible with the use case.
    \item If the asset is a dataset, the authors should provide the datasheet for the dataset.
\end{itemize}

\item {\bf New Assets}
\item[] Question: Are new assets introduced in the paper well documented and is the license of the new assets described?
\item[] Answer: \answerTODO{}
\item[] Justification: TODO
\item[] Guidelines:
\begin{itemize}
    \item The answer NA means that the paper does not release new assets.
    \item Newly introduced datasets should include a license, structured metadata, and a detailed description of the collection process such that it can be used by others.
    \item Newly introduced models should include a model card, training recipe, inference and evaluation scripts, along with a license.
\end{itemize}

\item {\bf Crowdsourcing and Research with Human Subjects}
\item[] Question: For crowdsourcing experiments and research with human subjects, does the paper include the necessary information consistent with the IRB approval, and terms of consent received from participants?
\item[] Answer: \answerNA{}
\item[] Justification: The paper does not involve crowdsourcing or research with human subjects.
\item[] Guidelines:
\begin{itemize}
    \item The answer NA means that the paper does not involve crowdsourcing nor research with human subjects.
    \item Including this information in the supplemental material is fine, but if the present, it should be on the first page of the supplemental material.
\end{itemize}

\item {\bf Institutional Review Board (IRB) Approvals or Equivalent for Research with Human Subjects}
\item[] Question: Does the paper describe potential risks incurred by study participants, whether such risks were disclosed to the subjects, and whether Institutional Review Board (IRB) approvals (or an equivalent approval/review based on the requirements of your country or institution) were obtained?
\item[] Answer: \answerNA{}
\item[] Justification: The paper does not involve research with human subjects.
\item[] Guidelines:
\begin{itemize}
    \item The answer NA means that the paper does not involve crowdsourcing nor research with human subjects.
    \item Confirming that an appropriate IRB approval (or equivalent) is in place for the proposed research is essential in maintaining the integrity of the research and protecting the rights of the participants.
    \item The authors are encouraged to maintain high ethical standards and protect the privacy of participants.
\end{itemize}

\end{enumerate}
EOF
    echo "  + sections/impact.tex    (MANDATORY for NeurIPS — does not count toward page limit)"
    echo "  + sections/checklist.tex (MANDATORY for NeurIPS — does not count toward page limit)"
    ;;

  icml)
    cat > "$DEST/sections/impact.tex" <<'EOF'
% ICML REQUIREMENT: MANDATORY, does NOT count toward the page limit.
% Discuss both positive and negative potential societal impacts.
% If impacts are minimal, you may use the minimal boilerplate below instead.

% --- Minimal boilerplate (use only if truly applicable) ---
% This paper presents work whose goal is to advance the field of machine learning.
% There are many potential societal consequences of our work, none of which we feel
% must be specifically highlighted here.

% --- Full template (recommended) ---
\textbf{Positive impacts.}
TODO: Describe the positive societal impacts of this work.

\textbf{Potential risks.}
TODO: Describe any potential negative societal impacts and how they can be mitigated.
EOF
    echo "  + sections/impact.tex  (MANDATORY for ICML — does not count toward page limit)"
    ;;

  iclr)
    cat > "$DEST/sections/impact.tex" <<'EOF'
TODO: Optionally describe the broader societal impact of this work.

% ICLR: Ethics statement is optional. Include only if your paper raises specific concerns.
EOF
    echo "  + sections/impact.tex  (optional Ethics Statement for ICLR)"
    ;;

  acl)
    cat > "$DEST/sections/limitations.tex" <<'EOF'
TODO: Describe the limitations of this work.

% ACL/EMNLP/NAACL: Limitations section is strongly encouraged.
% It does NOT count toward the page limit in most *ACL venues.
EOF
    cat > "$DEST/sections/ethics.tex" <<'EOF'
TODO: Describe any ethical considerations relevant to this work.

% ACL/EMNLP/NAACL: Ethics statement is required if the paper involves
% human subjects, personal data, or potentially harmful applications.
EOF
    echo "  + sections/limitations.tex  (required/encouraged for *ACL)"
    echo "  + sections/ethics.tex       (required if applicable for *ACL)"
    ;;
esac

# ── Empty Bibliography ────────────────────────────────────────────────────────
cat > "$DEST/bib/refs.bib" <<'EOF'
% Add your references here.
% Example:
% @article{author2024,
%   title   = {Title},
%   author  = {Author, First and Author, Second},
%   journal = {Journal Name},
%   year    = {2024},
% }
EOF

# ── Git Init ──────────────────────────────────────────────────────────────────
if [[ "$INIT_GIT" == true ]]; then
  git -C "$DEST" init -q
  git -C "$DEST" add .
  git -C "$DEST" commit -q -m "init: Initialize LaTeX paper project${VENUE:+ (venue: $VENUE)}"
  echo "  Git repository initialized and initial commit created."
fi

# ── Venue Setup Notes ─────────────────────────────────────────────────────────
print_venue_notes() {
  case "$VENUE" in
    iclr)
      echo ""
      echo "ICLR setup:"
      echo "  1. Download: https://github.com/ICLR/Master-Template"
      echo "  2. Place iclr2026_conference.sty and iclr2026.bst in project root"
      echo "  3. Camera-ready: change [submitted] to [accepted] in main.tex"
      ;;
    cvpr)
      echo ""
      echo "CVPR setup:"
      echo "  1. Download: https://github.com/cvpr-org/author-kit"
      echo "  2. Place cvpr.sty and ieeenat_fullname.bst in project root"
      echo "  3. Camera-ready: remove [review] from \\usepackage[review]{cvpr}"
      echo "  Layout: TWO-COLUMN — use figure* / table* for full-width floats"
      ;;
    icml)
      echo ""
      echo "ICML setup:"
      echo "  1. Download: https://icml.cc/Downloads/2026"
      echo "  2. Place icml2026.sty and icml2026.bst in project root"
      echo "  3. Camera-ready: \\usepackage[accepted]{icml2026}"
      echo "  REQUIRED: sections/impact.tex (Broader Impact, does not count toward page limit)"
      ;;
    acm)
      echo ""
      echo "ACM setup:"
      echo "  1. acmart.cls is included in TeX Live / MiKTeX — no download needed"
      echo "     (If missing: https://www.acm.org/publications/proceedings-template)"
      echo "  2. Camera-ready: remove [review,anonymous] from documentclass options"
      echo "  3. Add \\acmConference, \\acmDOI, \\setcopyright for camera-ready"
      echo "  WARNING: acmart redefines \\P — may conflict with macros.tex"
      ;;
    acl)
      echo ""
      echo "ACL setup:"
      echo "  1. Download: https://github.com/acl-org/acl-style-files"
      echo "  2. Place acl.sty and acl_natbib.bst in project root"
      echo "  3. Camera-ready: change \\usepackage[review]{acl} to \\usepackage{acl}"
      echo "  NOTE: Use \\citet{} for in-text citations, \\cite{} for parenthetical"
      ;;
    neurips)
      echo ""
      echo "NeurIPS setup:"
      echo "  1. Download: https://neurips.cc/Conferences/2025/PaperInformation/StyleFiles"
      echo "  2. Place neurips_2025.sty in project root"
      echo "  3. Submission (anonymous): \\usepackage{neurips_2025}"
      echo "     Preprint / arXiv:       \\usepackage[preprint]{neurips_2025}"
      echo "     Camera-ready:           \\usepackage[final]{neurips_2025}"
      echo "  REQUIRED: sections/impact.tex   (Broader Impact, does not count toward page limit)"
      echo "  REQUIRED: sections/checklist.tex (Author Checklist, does not count toward page limit)"
      ;;
  esac
}

# ── Summary ───────────────────────────────────────────────────────────────────
echo ""
echo "Project '$PROJECT_NAME' created at: $(cd "$DEST" && pwd)"
echo ""
echo "Files:"
find "$DEST" -not -path '*/.git/*' | sort | sed "s|$DEST/||" | grep -v "^$" | \
  awk 'NF{print "  " $0}'
print_venue_notes
echo ""
echo "Next steps:"
echo "  1. Edit sections/title.tex with your paper title"
echo "  2. Edit main.tex — fill in authors and affiliations"
if [[ -n "$VENUE" ]]; then
  echo "  3. Download and add venue style files (see above)"
fi

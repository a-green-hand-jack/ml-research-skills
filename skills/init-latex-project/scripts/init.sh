#!/usr/bin/env bash
# init.sh — Initialize a LaTeX academic paper project
# Usage: init.sh <project-name> [target-dir] [--venue <venue>] [--git] [--offline]
#
# Supported venues: icml acl emnlp naacl iccv eccv neurips iclr cvpr acm
#
# For year-specific venues (icml, neurips, iclr), this script downloads the
# current year's official style files from the venue website and generates
# venue_preamble.tex automatically.  Use --offline to skip the download.

set -euo pipefail

# ── Argument Parsing ──────────────────────────────────────────────────────────
PROJECT_NAME=""
TARGET_DIR="."
VENUE=""
INIT_GIT=false
OFFLINE=false

while [[ $# -gt 0 ]]; do
  case "$1" in
    --git)     INIT_GIT=true; shift ;;
    --offline) OFFLINE=true;  shift ;;
    --venue)
      VENUE="${2:?--venue requires an argument}"
      shift 2 ;;
    --venue=*)
      VENUE="${1#*=}"; shift ;;
    -*)
      echo "ERROR: Unknown flag: $1" >&2
      echo "Usage: init.sh <project-name> [target-dir] [--venue <venue>] [--git] [--offline]" >&2
      exit 1 ;;
    *)
      if   [[ -z "$PROJECT_NAME" ]]; then PROJECT_NAME="$1"
      elif [[ "$TARGET_DIR" == "." ]];  then TARGET_DIR="$1"
      fi
      shift ;;
  esac
done

# ── Validate ──────────────────────────────────────────────────────────────────
if [[ -z "$PROJECT_NAME" ]]; then
  echo "Usage: init.sh <project-name> [target-dir] [--venue <venue>] [--git] [--offline]" >&2
  exit 1
fi

VENUE="${VENUE,,}"   # normalize to lowercase

SUPPORTED="icml acl emnlp naacl iccv eccv neurips iclr cvpr acm"
if [[ -n "$VENUE" && ! " $SUPPORTED " =~ " $VENUE " ]]; then
  echo "ERROR: Unsupported venue '$VENUE'." >&2
  echo "  Supported: $SUPPORTED" >&2
  exit 1
fi

DEST="$TARGET_DIR/$PROJECT_NAME"
SKILL_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TEMPLATES="$SKILL_DIR/templates"

if [[ -d "$DEST" ]]; then
  echo "ERROR: '$DEST' already exists." >&2
  exit 1
fi

# ── Style-File Download Helpers ───────────────────────────────────────────────
YEAR=$(date +%Y)
TODAY=$(date +%Y-%m-%d)

# Download a zip from $1, extract all .sty/.bst/.cls files flat into $2.
fetch_zip() {
  local url="$1" dest="$2" tmpdir
  tmpdir=$(mktemp -d)
  if curl -fsSL --connect-timeout 15 --max-time 90 "$url" -o "$tmpdir/pkg.zip" 2>/dev/null; then
    if unzip -q "$tmpdir/pkg.zip" -d "$tmpdir/x/" 2>/dev/null; then
      find "$tmpdir/x" \( -name "*.sty" -o -name "*.bst" -o -name "*.cls" \) \
        -exec cp {} "$dest/" \;
      rm -rf "$tmpdir"
      return 0
    fi
  fi
  rm -rf "$tmpdir"
  return 1
}

# Write a placeholder venue_preamble.tex when download fails.
write_placeholder_preamble() {
  local venue="$1" dest="$2"
  cat > "$dest/venue_preamble.tex" <<EOF
% PLACEHOLDER — style files could not be downloaded automatically.
% 1. Download the official package (see sources.yaml in the skill for the URL).
% 2. Place the .sty/.bst files in this directory.
% 3. Replace the lines below with the correct \usepackage command.
%
% Venue: ${venue}
% Official instructions: see sources.yaml or the venue website.
EOF
  echo "  WARN: Could not auto-download style files for $venue."
  echo "        Edit venue_preamble.tex manually after placing .sty files here."
}

# ── Per-Venue Download Logic ──────────────────────────────────────────────────
download_styles() {
  local venue="$1" dest="$2"
  [[ "$OFFLINE" == true ]] && { write_placeholder_preamble "$venue" "$dest"; return; }

  local ok=false sty pkg y url

  case "$venue" in
    # ── icml ────────────────────────────────────────────────────────────────
    icml)
      for y in "$YEAR" "$((YEAR-1))"; do
        url="https://media.icml.cc/Conferences/ICML${y}/Styles/icml${y,,}.zip"
        if fetch_zip "$url" "$dest"; then
          sty=$(find "$dest" -maxdepth 1 -name "icml*.sty" -printf "%f\n" 2>/dev/null | head -1)
          if [[ -n "$sty" ]]; then
            pkg="${sty%.sty}"
            cat > "$dest/venue_preamble.tex" <<EOF
% ICML ${y} — fetched from icml.cc on ${TODAY}
% Camera-ready: \usepackage[accepted]{${pkg}}
\usepackage{${pkg}}
EOF
            ok=true; break
          fi
        fi
      done ;;

    # ── neurips ─────────────────────────────────────────────────────────────
    neurips)
      for y in "$YEAR" "$((YEAR-1))"; do
        url="https://media.nips.cc/Conferences/${y}/Styles/neurips_${y}.zip"
        if fetch_zip "$url" "$dest"; then
          sty=$(find "$dest" -maxdepth 1 -name "neurips_*.sty" -printf "%f\n" 2>/dev/null | head -1)
          if [[ -n "$sty" ]]; then
            pkg="${sty%.sty}"
            cat > "$dest/venue_preamble.tex" <<EOF
% NeurIPS ${y} — fetched from neurips.cc on ${TODAY}
% Preprint/arXiv: \usepackage[preprint]{${pkg}}
% Camera-ready:   \usepackage[final]{${pkg}}
\PassOptionsToPackage{numbers,compress}{natbib}
\usepackage{${pkg}}
EOF
            ok=true; break
          fi
        fi
      done ;;

    # ── iclr ────────────────────────────────────────────────────────────────
    iclr)
      for y in "$YEAR" "$((YEAR-1))"; do
        url="https://github.com/ICLR/Master-Template/raw/master/iclr${y}.zip"
        if fetch_zip "$url" "$dest"; then
          sty=$(find "$dest" -maxdepth 1 -name "iclr*_conference.sty" -printf "%f\n" 2>/dev/null | head -1)
          if [[ -n "$sty" ]]; then
            pkg="${sty%.sty}"
            cat > "$dest/venue_preamble.tex" <<EOF
% ICLR ${y} — fetched from github.com/ICLR/Master-Template on ${TODAY}
% Camera-ready: \usepackage[accepted]{${pkg}}
\usepackage[submitted]{${pkg}}
EOF
            ok=true; break
          fi
        fi
      done ;;

    # ── cvpr ────────────────────────────────────────────────────────────────
    cvpr)
      for url in \
        "https://github.com/cvpr-org/author-kit/archive/refs/tags/CVPR${YEAR}-v1(latex).zip" \
        "https://github.com/cvpr-org/author-kit/archive/refs/heads/main.zip"; do
        if fetch_zip "$url" "$dest" && [[ -f "$dest/cvpr.sty" ]]; then
          cat > "$dest/venue_preamble.tex" <<EOF
% CVPR — fetched from github.com/cvpr-org/author-kit on ${TODAY}
% Camera-ready: \usepackage{cvpr}
% arXiv:        \usepackage[pagenumbers]{cvpr}
\usepackage[review]{cvpr}
EOF
          ok=true; break
        fi
      done ;;

    # ── iccv (biennial: odd years) ───────────────────────────────────────────
    iccv)
      # Try current year and adjacent odd years
      for y in "$YEAR" "$((YEAR-1))" "$((YEAR+1))"; do
        url="https://media.eventhosts.cc/Conferences/ICCV${y}/ICCV${y}-Author-Kit-Feb.zip"
        if fetch_zip "$url" "$dest"; then
          sty=$(find "$dest" -maxdepth 1 \( -name "iccv*.sty" -o -name "cvpr.sty" \) \
                  -printf "%f\n" 2>/dev/null | head -1)
          if [[ -n "$sty" ]]; then
            pkg="${sty%.sty}"
            cat > "$dest/venue_preamble.tex" <<EOF
% ICCV ${y} — fetched from CVF on ${TODAY}
% Camera-ready: \usepackage{${pkg}}
\usepackage[review]{${pkg}}
EOF
            ok=true; break
          fi
        fi
      done ;;

    # ── eccv (biennial: even years) ──────────────────────────────────────────
    eccv)
      url="https://github.com/paolo-favaro/paper-template/archive/refs/tags/Latest.zip"
      if fetch_zip "$url" "$dest" && [[ -f "$dest/eccv.sty" ]]; then
        cat > "$dest/venue_preamble.tex" <<EOF
% ECCV — fetched from github.com/paolo-favaro/paper-template on ${TODAY}
% Uses Springer LNCS (\documentclass{llncs} in main.tex — NOT article)
\usepackage{eccv}
\usepackage{eccvabbrv}
EOF
        ok=true
      fi ;;

    # ── acl / emnlp / naacl (all share the same acl.sty) ─────────────────────
    acl|emnlp|naacl)
      url="https://github.com/acl-org/acl-style-files/archive/refs/heads/master.zip"
      if fetch_zip "$url" "$dest" && [[ -f "$dest/acl.sty" ]]; then
        local vname="${venue^^}"
        cat > "$dest/venue_preamble.tex" <<EOF
% ${vname} (*ACL family) — fetched from github.com/acl-org/acl-style-files on ${TODAY}
% Camera-ready: \usepackage{acl}
\usepackage[review]{acl}
EOF
        ok=true
      fi ;;

    # ── acm (pre-installed via CTAN; no download needed) ─────────────────────
    acm)
      # Just write the preamble comment; acmart is already in TeX Live / MiKTeX
      cat > "$dest/venue_preamble.tex" <<EOF
% ACM — acmart class (pre-installed in TeX Live / MiKTeX via CTAN)
% If missing: tlmgr install acmart
% Document class options are in main.tex (\documentclass[sigconf,review,anonymous]{acmart})
EOF
      ok=true ;;
  esac

  [[ "$ok" == false ]] && write_placeholder_preamble "$venue" "$dest"
}

# ── Create Directory Structure ────────────────────────────────────────────────
echo "Creating project: $PROJECT_NAME${VENUE:+ (venue: $VENUE)}"
mkdir -p "$DEST"/{sections,figures,tables,bib}

# ── Copy Base Template Files ──────────────────────────────────────────────────
cp "$TEMPLATES/macros.tex" "$DEST/macros.tex"
cp "$TEMPLATES/CLAUDE.md"  "$DEST/CLAUDE.md"

# Copy venue-specific main.tex (all use \input{venue_preamble})
if [[ -n "$VENUE" && -f "$TEMPLATES/venues/$VENUE/main.tex" ]]; then
  cp "$TEMPLATES/venues/$VENUE/main.tex" "$DEST/main.tex"
else
  cp "$TEMPLATES/main.tex" "$DEST/main.tex"
fi

# ── Download Official Style Files ─────────────────────────────────────────────
if [[ -n "$VENUE" ]]; then
  echo "Fetching official style files for $VENUE..."
  download_styles "$VENUE" "$DEST"
fi

# ── Create Placeholder Section Files ─────────────────────────────────────────
cat > "$DEST/sections/title.tex" <<'EOF'
Title of the Paper
EOF

cat > "$DEST/sections/abstract.tex" <<'EOF'
TODO: Write abstract here.
EOF

cat > "$DEST/sections/intro.tex" <<'EOF'
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

cat > "$DEST/sections/related.tex"    <<'EOF'
TODO: Write related work here.
EOF

cat > "$DEST/sections/method.tex"     <<'EOF'
TODO: Write method here.
EOF

cat > "$DEST/sections/exp.tex"        <<'EOF'
TODO: Write experiments here.
EOF

cat > "$DEST/sections/conclusion.tex" <<'EOF'
TODO: Write conclusion here.
EOF

cat > "$DEST/sections/acknowledgement.tex" <<'EOF'
TODO: Add funding acknowledgments here.
EOF

cat > "$DEST/sections/appendix.tex"   <<'EOF'
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

\textbf{Positive impacts.}
TODO: Describe the positive societal impacts of this work.

\textbf{Potential risks.}
TODO: Describe any potential negative societal impacts and how they can be mitigated.
EOF
    cat > "$DEST/sections/checklist.tex" <<'EOF'
% ── NeurIPS Paper Checklist ────────────────────────────────────────────────────
% MANDATORY — does NOT count toward the page limit.
% Answer macros: \answerYes{} \answerNo{} \answerNA{} \answerTODO{}

\section*{NeurIPS Paper Checklist}

\begin{enumerate}

\item {\bf Claims}
\item[] Question: Do the main claims made in the abstract and introduction accurately reflect the paper's contributions and scope?
\item[] Answer: \answerTODO{}
\item[] Justification: TODO

\item {\bf Limitations}
\item[] Question: Does the paper discuss the limitations of the work performed by the authors?
\item[] Answer: \answerTODO{}
\item[] Justification: TODO

\item {\bf Theory Assumptions and Proofs}
\item[] Question: For each theoretical result, does the paper provide the full set of assumptions and a complete proof?
\item[] Answer: \answerTODO{}
\item[] Justification: TODO

\item {\bf Experimental Result Reproducibility}
\item[] Question: Does the paper fully disclose all the information needed to reproduce the main experimental results?
\item[] Answer: \answerTODO{}
\item[] Justification: TODO

\item {\bf Open access to data and code}
\item[] Question: Does the paper provide open access to the data and code?
\item[] Answer: \answerTODO{}
\item[] Justification: TODO

\item {\bf Experimental Setting/Details}
\item[] Question: Does the paper specify all the training and test details necessary to understand the results?
\item[] Answer: \answerTODO{}
\item[] Justification: TODO

\item {\bf Experiment Statistical Significance}
\item[] Question: Does the paper report error bars suitably and correctly defined?
\item[] Answer: \answerTODO{}
\item[] Justification: TODO

\item {\bf Compute Resources}
\item[] Question: Does the paper provide sufficient information on the computer resources needed to reproduce the experiments?
\item[] Answer: \answerTODO{}
\item[] Justification: TODO

\item {\bf Code Of Ethics}
\item[] Question: Does the research conform with the NeurIPS Code of Ethics?
\item[] Answer: \answerYes{}
\item[] Justification: We have reviewed and comply with the NeurIPS Code of Ethics.

\item {\bf Broader Impacts}
\item[] Question: Does the paper discuss both potential positive and negative societal impacts?
\item[] Answer: \answerYes{}
\item[] Justification: See the Broader Impact section above.

\item {\bf Safeguards}
\item[] Question: Does the paper describe safeguards for responsible release of data or models?
\item[] Answer: \answerNA{}
\item[] Justification: TODO: update if you release pretrained models or scraped datasets.

\item {\bf Licenses for existing assets}
\item[] Question: Are creators of assets used in this paper properly credited?
\item[] Answer: \answerTODO{}
\item[] Justification: TODO

\item {\bf New Assets}
\item[] Question: Are new assets introduced in the paper well documented?
\item[] Answer: \answerTODO{}
\item[] Justification: TODO

\item {\bf Crowdsourcing and Research with Human Subjects}
\item[] Question: Does the paper include the necessary information consistent with IRB approval?
\item[] Answer: \answerNA{}
\item[] Justification: The paper does not involve crowdsourcing or research with human subjects.

\item {\bf Institutional Review Board (IRB) Approvals}
\item[] Question: Does the paper describe potential risks incurred by study participants?
\item[] Answer: \answerNA{}
\item[] Justification: The paper does not involve research with human subjects.

\end{enumerate}
EOF
    echo "  + sections/impact.tex    (MANDATORY for NeurIPS — does not count toward page limit)"
    echo "  + sections/checklist.tex (MANDATORY for NeurIPS — does not count toward page limit)"
    ;;

  icml)
    cat > "$DEST/sections/impact.tex" <<'EOF'
% ICML REQUIREMENT: MANDATORY, does NOT count toward the page limit.

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

  acl|emnlp|naacl)
    cat > "$DEST/sections/limitations.tex" <<'EOF'
TODO: Describe the limitations of this work.

% MANDATORY for *ACL venues. Does NOT count toward the page limit.
EOF
    cat > "$DEST/sections/ethics.tex" <<'EOF'
TODO: Describe any ethical considerations relevant to this work.

% Required if the paper involves human subjects, personal data, or potentially
% harmful applications. Encouraged for all *ACL submissions.
EOF
    echo "  + sections/limitations.tex  (MANDATORY for *ACL — does not count toward page limit)"
    echo "  + sections/ethics.tex       (required if applicable for *ACL)"
    ;;
esac

# ── Empty Bibliography ────────────────────────────────────────────────────────
cat > "$DEST/bib/refs.bib" <<'EOF'
% Add your references here.
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
  echo "  Git repository initialized."
fi

# ── Summary ───────────────────────────────────────────────────────────────────
echo ""
echo "Project '$PROJECT_NAME' created at: $(cd "$DEST" && pwd)"
echo ""
echo "Files:"
find "$DEST" -not -path '*/.git/*' | sort | sed "s|$DEST/||" | grep -v "^$" | \
  awk 'NF{print "  " $0}'

if [[ -n "$VENUE" ]]; then
  echo ""
  echo "venue_preamble.tex: contains the \usepackage command for $VENUE."
  echo "  To switch submission mode (e.g. anonymous → preprint), edit that file."
fi

echo ""
echo "Next steps:"
echo "  1. Edit sections/title.tex with your paper title"
echo "  2. Edit main.tex — fill in authors and affiliations"
if [[ -n "$VENUE" ]]; then
  echo "  3. Check venue_preamble.tex — verify style files are present"
fi

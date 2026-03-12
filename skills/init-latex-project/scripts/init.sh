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
TODO: Describe the broader societal impact of this work.

% NeurIPS REQUIREMENT: This section is MANDATORY and does NOT count toward the page limit.
% Minimal text (if impacts are well-established):
% "This paper presents work whose goal is to advance the field of machine learning.
%  There are many potential societal consequences of our work, none of which we feel
%  must be specifically highlighted here."
EOF
    cat > "$DEST/sections/checklist.tex" <<'EOF'
% NeurIPS Paper Checklist
% This checklist is MANDATORY and does NOT count toward the page limit.
% See: https://neurips.cc/public/guides/PaperChecklist

\begin{enumerate}

\item {\bf Claims}
\item[] Question: Do the main claims made in the abstract and introduction accurately reflect the paper's contributions and scope?
\item[] Answer: \answerYes{}
\item[] Justification: TODO
\item[] Guidelines: ...

\item {\bf Limitations}
\item[] Question: Does the paper discuss the limitations of the work performed by the authors?
\item[] Answer: \answerYes{}
\item[] Justification: TODO
\item[] Guidelines: ...

% Add remaining checklist items from the official NeurIPS checklist template.

\end{enumerate}
EOF
    echo "  + sections/impact.tex    (MANDATORY for NeurIPS — does not count toward page limit)"
    echo "  + sections/checklist.tex (MANDATORY for NeurIPS — does not count toward page limit)"
    ;;

  icml)
    cat > "$DEST/sections/impact.tex" <<'EOF'
TODO: Describe the broader societal impact of this work.

% ICML REQUIREMENT: This section is MANDATORY and does NOT count toward the page limit.
% Minimal text (if impacts are well-established):
% "This paper presents work whose goal is to advance the field of machine learning.
%  There are many potential societal consequences of our work, none of which we feel
%  must be specifically highlighted here."
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

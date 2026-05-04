#!/usr/bin/env bash
# submit-paper: mechanical pre-submission checks for LaTeX papers
#
# Usage:
#   bash check.sh [project-dir] [--compile]
#
# Flags:
#   --compile   Run local LaTeX + bibtex to check compilation, page count,
#               overfull boxes, and undefined refs. If no compiler is installed,
#               skip local compilation and use Overleaf/GitHub workflow.
#               Skipped by default (static analysis only).

set -euo pipefail

# ── Args ──────────────────────────────────────────────────────────────────────
PROJECT="."
DO_COMPILE=false
for arg in "$@"; do
  case "$arg" in
    --compile) DO_COMPILE=true ;;
    *) PROJECT="$arg" ;;
  esac
done

cd "$PROJECT"

# ── Counters ──────────────────────────────────────────────────────────────────
PASS=0; WARN=0; FAIL=0

pass() { printf "  ✅ %s\n" "$1"; ((PASS++)) || true; }
warn() { printf "  ⚠️  %s\n" "$1"; ((WARN++)) || true; }
fail() { printf "  ❌ %s\n" "$1"; ((FAIL++)) || true; }
info() { printf "  ℹ️  %s\n" "$1"; }
section() { printf "\n── %s ──────────────────────────────────────────\n" "$1"; }

# ── 1. Project detection ───────────────────────────────────────────────────────
section "Project Detection"

if [[ ! -f "main.tex" ]]; then
  printf "ERROR: No main.tex found in %s\n" "$PROJECT"
  exit 2
fi
pass "main.tex found"

VENUE=""
PREAMBLE_MODE="unknown"

if [[ -f "venue_preamble.tex" ]]; then
  pass "venue_preamble.tex found"
  PREAMBLE=$(cat venue_preamble.tex)

  # Detect venue from preamble content
  if   echo "$PREAMBLE" | grep -qi "neurips";  then VENUE="neurips"
  elif echo "$PREAMBLE" | grep -qi "\\bicml";  then VENUE="icml"
  elif echo "$PREAMBLE" | grep -qi "\\biclr";  then VENUE="iclr"
  elif echo "$PREAMBLE" | grep -qi "\\bcvpr";  then VENUE="cvpr"
  elif echo "$PREAMBLE" | grep -qi "\\biccv";  then VENUE="iccv"
  elif echo "$PREAMBLE" | grep -qi "\\beccv";  then VENUE="eccv"
  elif echo "$PREAMBLE" | grep -qi "\\bacl";   then VENUE="acl"
  elif echo "$PREAMBLE" | grep -qi "acmart";   then VENUE="acm"
  fi

  [[ -n "$VENUE" ]] && info "Venue: $VENUE" || warn "Could not detect venue from venue_preamble.tex"

  # Detect submission mode
  if   echo "$PREAMBLE" | grep -qiE '\[(final|accepted|camera.?ready)\]'; then
    PREAMBLE_MODE="camera-ready"
  elif echo "$PREAMBLE" | grep -qiE '\[(preprint|arxiv)\]';               then
    PREAMBLE_MODE="preprint"
  elif echo "$PREAMBLE" | grep -qiE '\[(review|submitted|blind)\]';       then
    PREAMBLE_MODE="anonymous"
  elif echo "$PREAMBLE" | grep -qE '\\usepackage\{(neurips_|icml)';       then
    PREAMBLE_MODE="anonymous"   # bare \usepackage{neurips_YEAR} = anonymous
  fi
  info "Submission mode: $PREAMBLE_MODE"
else
  warn "venue_preamble.tex not found — is this an init-latex-project project?"
  # Try to detect venue from main.tex directly
  MAIN=$(cat main.tex 2>/dev/null || echo "")
  if   echo "$MAIN" | grep -qi "neurips";  then VENUE="neurips"
  elif echo "$MAIN" | grep -qi "icml";     then VENUE="icml"
  elif echo "$MAIN" | grep -qi "iclr";     then VENUE="iclr"
  elif echo "$MAIN" | grep -qi "cvpr";     then VENUE="cvpr"
  fi
  [[ -n "$VENUE" ]] && info "Venue (from main.tex): $VENUE"
fi

# ── 2. Drafting artifacts ──────────────────────────────────────────────────────
section "Drafting Artifacts"

# Patterns: \todo, \fixme, \red{, \hl{, author comment macros, inline TODOs
ARTIFACT_PATTERN='\\todo|\\fixme|\\red\{|\\hl\{|\\note\{|\\jieke\{|\\jerry\{|\\wwm\{|\\ethan\{|\bTODO\b|\bFIXME\b|\bXXX\b'

ARTIFACTS=$(grep -rn "$ARTIFACT_PATTERN" --include="*.tex" . 2>/dev/null \
  | grep -v "venue_preamble\|macros\.tex\|\.git" || true)

if [[ -z "$ARTIFACTS" ]]; then
  pass "No TODO/FIXME/author-comment artifacts found"
else
  N=$(echo "$ARTIFACTS" | wc -l | tr -d ' ')
  fail "$N unresolved drafting artifact(s):"
  echo "$ARTIFACTS" | head -15 | sed 's/^/      /'
  [[ $N -gt 15 ]] && printf "      ... (%d more)\n" $((N-15))
fi

# ── 3. Anonymity ──────────────────────────────────────────────────────────────
section "Anonymity"

if [[ "$PREAMBLE_MODE" == "anonymous" ]]; then
  # Acknowledgements must be hidden in anonymous mode
  ACK=$(grep -rn "\\\\section.*[Aa]cknowledg\|\\\\paragraph.*[Aa]cknowledg" \
    --include="*.tex" . 2>/dev/null \
    | grep -v "^Binary\|%.*\\\\section\|\.git" || true)
  if [[ -z "$ACK" ]]; then
    pass "No visible acknowledgements section (good)"
  else
    warn "Acknowledgements section found — wrap in venue's anonymous guard (e.g., NeurIPS {ack} env)"
  fi

  # Funding / grant numbers leak identity
  GRANTS=$(grep -rn "NSF\|NIH\|EPSRC\|grant\|supported by\|funded by" \
    --include="*.tex" . 2>/dev/null | grep -iv "^Binary\|\.git" || true)
  if [[ -n "$GRANTS" ]]; then
    N=$(echo "$GRANTS" | wc -l | tr -d ' ')
    warn "$N potential funding disclosure(s) — remove for blind review:"
    echo "$GRANTS" | head -5 | sed 's/^/      /'
  else
    pass "No funding disclosures detected"
  fi

  # Personal URLs / emails
  URLS=$(grep -rn "github\.com/\|arxiv\.org/\|@.*\.\(com\|edu\|org\)" \
    --include="*.tex" . 2>/dev/null | grep -v "^Binary\|%\|\.git" || true)
  if [[ -n "$URLS" ]]; then
    N=$(echo "$URLS" | wc -l | tr -d ' ')
    warn "$N personal URL/email reference(s) — may reveal identity:"
    echo "$URLS" | head -5 | sed 's/^/      /'
  else
    pass "No personal URLs or emails found"
  fi

elif [[ "$PREAMBLE_MODE" == "camera-ready" ]]; then
  HAS_AUTHOR=$(grep -n "\\\\author{" main.tex 2>/dev/null || true)
  if [[ -n "$HAS_AUTHOR" ]]; then
    pass "Author information present (camera-ready)"
  else
    warn "Camera-ready mode but \\author{} not found in main.tex"
  fi
fi

# ── 4. Bibliography ────────────────────────────────────────────────────────────
section "Bibliography"

BIB_FILE=$(find . -name "*.bib" -not -path "./.git/*" 2>/dev/null | head -1)
if [[ -n "$BIB_FILE" ]]; then
  BIB_ENTRIES=$(grep -c "^@" "$BIB_FILE" 2>/dev/null || echo 0)
  if [[ $BIB_ENTRIES -gt 0 ]]; then
    pass "$BIB_ENTRIES bib entries ($BIB_FILE)"
  else
    fail ".bib file is empty ($BIB_FILE)"
  fi
else
  fail "No .bib file found"
fi

if grep -rq "\\\\bibliography{" --include="*.tex" . 2>/dev/null; then
  pass "\\bibliography{} call found"
else
  fail "No \\bibliography{} call — missing bibliography"
fi

# ── 5. Mandatory venue sections ────────────────────────────────────────────────
section "Mandatory Sections"

check_section() {
  local file="$1"
  local desc="$2"
  if [[ -f "$file" ]]; then
    # Count non-blank, non-comment lines
    LINES=$(grep -v "^[[:space:]]*%\|^[[:space:]]*$" "$file" 2>/dev/null | wc -l | tr -d ' ')
    if [[ $LINES -gt 3 ]]; then
      pass "$desc ($file, ~$LINES content lines)"
    else
      warn "$desc exists but looks like a placeholder ($file)"
    fi
  else
    fail "$desc required but not found: $file"
  fi
}

case "$VENUE" in
  neurips)
    check_section "sections/impact.tex"    "Broader Impact (NeurIPS mandatory)"
    check_section "sections/checklist.tex" "Author Checklist (NeurIPS mandatory)"
    ;;
  icml)
    check_section "sections/impact.tex"    "Broader Impact (ICML mandatory)"
    ;;
  acl|emnlp|naacl)
    check_section "sections/limitations.tex" "Limitations (ACL-family mandatory)"
    ;;
esac

# ── 6. Abstract ────────────────────────────────────────────────────────────────
section "Abstract"

ABS_FILE="sections/abstract.tex"
ABS_SRC=""
if [[ -f "$ABS_FILE" ]]; then
  ABS_SRC=$(cat "$ABS_FILE")
elif grep -q "\\\\begin{abstract}" main.tex 2>/dev/null; then
  ABS_SRC=$(sed -n '/\\begin{abstract}/,/\\end{abstract}/p' main.tex)
fi

if [[ -n "$ABS_SRC" ]]; then
  # Strip LaTeX commands and count words roughly
  WORDS=$(echo "$ABS_SRC" \
    | sed 's/\\[a-zA-Z]*{[^}]*}//g; s/[\\{}%]//g; s/[^a-zA-Z ]/ /g' \
    | wc -w | tr -d ' ')
  if   [[ $WORDS -lt 30  ]]; then warn "Abstract is very short (~$WORDS words)"
  elif [[ $WORDS -gt 350 ]]; then warn "Abstract may be too long (~$WORDS words) — most venues cap at 200-250"
  else                              pass "Abstract: ~$WORDS words"
  fi
else
  fail "No abstract found (sections/abstract.tex or \\begin{abstract} in main.tex)"
fi

# ── 7. Figure and table integrity ──────────────────────────────────────────────
section "Figures & Tables"

# Find all \label{fig:*} / \label{tab:*} and check they are \ref'd
FIG_LABELS=$(grep -rh "\\\\label{fig:" --include="*.tex" . 2>/dev/null \
  | sed 's/.*\\label{\([^}]*\)}.*/\1/' || true)
TAB_LABELS=$(grep -rh "\\\\label{tab:" --include="*.tex" . 2>/dev/null \
  | sed 's/.*\\label{\([^}]*\)}.*/\1/' || true)

UNREFFED=0
while IFS= read -r lbl; do
  [[ -z "$lbl" ]] && continue
  if ! grep -rq "\\\\ref{$lbl}\|\\\\autoref{$lbl}\|\\\\cref{$lbl}" \
      --include="*.tex" . 2>/dev/null; then
    warn "Unreferenced label: \\label{$lbl}"
    ((UNREFFED++)) || true
  fi
done <<< "$FIG_LABELS"
while IFS= read -r lbl; do
  [[ -z "$lbl" ]] && continue
  if ! grep -rq "\\\\ref{$lbl}\|\\\\autoref{$lbl}\|\\\\cref{$lbl}" \
      --include="*.tex" . 2>/dev/null; then
    warn "Unreferenced label: \\label{$lbl}"
    ((UNREFFED++)) || true
  fi
done <<< "$TAB_LABELS"

FIG_COUNT=$(echo "$FIG_LABELS" | grep -c "." || true)
TAB_COUNT=$(echo "$TAB_LABELS" | grep -c "." || true)
[[ $UNREFFED -eq 0 ]] \
  && pass "All figure/table labels referenced ($FIG_COUNT fig, $TAB_COUNT tab)" \
  || true  # individual warns already printed

# ── 8. Source formatting ─────────────────────────────────────────────────────
section "Source Formatting"

if command -v tex-fmt &>/dev/null; then
  TEX_FMT_LOG=$(mktemp)
  if tex-fmt --check --nowrap --recursive . > "$TEX_FMT_LOG" 2>&1; then
    pass "tex-fmt check passed"
  else
    warn "tex-fmt found source formatting changes; run: tex-fmt --nowrap --recursive ."
    head -20 "$TEX_FMT_LOG" | sed 's/^/      /'
  fi
  rm -f "$TEX_FMT_LOG"
else
  info "tex-fmt not installed; skipping optional source formatting check"
fi

# ── 9. PDF compilation (optional) ─────────────────────────────────────────────
if $DO_COMPILE; then
  section "Compilation"

  LATEX_CMD=""
  command -v pdflatex &>/dev/null && LATEX_CMD="pdflatex"
  command -v xelatex  &>/dev/null && LATEX_CMD="xelatex"
  command -v lualatex &>/dev/null && LATEX_CMD="lualatex"

  if [[ -z "$LATEX_CMD" ]]; then
    warn "No LaTeX compiler found (pdflatex/xelatex/lualatex) — skipping local compile; use Overleaf/GitHub workflow"
  else
    COMPILE_LOG=$(mktemp)
    info "Running: $LATEX_CMD -interaction=nonstopmode main.tex"

    if $LATEX_CMD -interaction=nonstopmode -halt-on-error main.tex > "$COMPILE_LOG" 2>&1; then
      pass "Compilation succeeded"

      # Run bibtex if .aux exists
      if [[ -f "main.aux" ]] && grep -q "\\\\bibdata" main.aux 2>/dev/null; then
        bibtex main >> "$COMPILE_LOG" 2>&1 || true
        $LATEX_CMD -interaction=nonstopmode main.tex >> "$COMPILE_LOG" 2>&1 || true
        $LATEX_CMD -interaction=nonstopmode main.tex >> "$COMPILE_LOG" 2>&1 || true
      fi

      # Page count
      if command -v pdfinfo &>/dev/null && [[ -f "main.pdf" ]]; then
        PAGES=$(pdfinfo main.pdf 2>/dev/null | grep "^Pages:" | awk '{print $2}')
        info "PDF total pages: $PAGES (includes refs/appendix — check main-content pages manually)"
      fi

      # Overfull hboxes
      OVF=$(grep -c "Overfull .hbox" "$COMPILE_LOG" 2>/dev/null || echo 0)
      if   [[ $OVF -eq 0 ]]; then pass "No overfull hbox warnings"
      elif [[ $OVF -le 5  ]]; then warn "$OVF overfull hbox warning(s) — minor layout issue"
      else                         fail "$OVF overfull hbox warnings — fix before submission"
      fi

      # Undefined references / citations
      UNDEF_REF=$(grep -c "LaTeX Warning: Reference.*undefined"  "$COMPILE_LOG" 2>/dev/null || echo 0)
      UNDEF_CIT=$(grep -c "LaTeX Warning: Citation.*undefined"   "$COMPILE_LOG" 2>/dev/null || echo 0)
      [[ $UNDEF_REF -eq 0 ]] && pass "No undefined references" \
        || fail "$UNDEF_REF undefined reference(s) — run LaTeX twice"
      [[ $UNDEF_CIT -eq 0 ]] && pass "No undefined citations"  \
        || fail "$UNDEF_CIT undefined citation(s) — check .bib file"

    else
      ERRORS=$(grep "^!" "$COMPILE_LOG" | head -5)
      fail "Compilation failed:"
      echo "$ERRORS" | sed 's/^/      /'
    fi

    rm -f "$COMPILE_LOG"
  fi
else
  section "Compilation"
  info "Skipped local compile (pass --compile only when a local LaTeX compiler is available)"
fi

# ── Summary ────────────────────────────────────────────────────────────────────
printf "\n══════════════════════════════════════════════════\n"
printf "  SUMMARY  ✅ %d passed   ⚠️  %d warnings   ❌ %d failed\n" \
  "$PASS" "$WARN" "$FAIL"
printf "══════════════════════════════════════════════════\n"

if   [[ $FAIL -gt 0 ]]; then
  printf "  ⛔  Fix all failures before submitting.\n"
  exit 1
elif [[ $WARN -gt 0 ]]; then
  printf "  🟡  Review warnings before submitting.\n"
  exit 0
else
  printf "  🟢  All checks passed — good to go!\n"
  exit 0
fi

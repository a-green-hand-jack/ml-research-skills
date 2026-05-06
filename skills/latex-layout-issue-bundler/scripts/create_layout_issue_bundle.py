#!/usr/bin/env python3
"""Create a reproducible LaTeX layout issue bundle from a PDF page."""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path


WARNING_RE = re.compile(
    r"(overfull|underfull|warning|error|float|rerun|undefined|missing|emergency)",
    re.IGNORECASE,
)


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", value.strip().lower()).strip("-")
    return slug or "layout-issue"


def parse_source(value: str | None) -> tuple[Path, int | None, int | None] | None:
    if not value:
        return None
    match = re.match(r"^(.*?)(?::(\d+)(?:-(\d+))?)?$", value)
    if not match:
        raise ValueError(f"invalid --source value: {value}")
    path = Path(match.group(1)).expanduser()
    start = int(match.group(2)) if match.group(2) else None
    end = int(match.group(3)) if match.group(3) else start
    return path, start, end


def run_command(args: list[str], cwd: Path | None = None) -> tuple[bool, str]:
    proc = subprocess.run(args, cwd=cwd, capture_output=True, text=True, check=False)
    output = (proc.stdout + proc.stderr).strip()
    return proc.returncode == 0, output


def render_page(pdf: Path, page: int, out_prefix: Path, manifest: dict[str, object]) -> Path | None:
    pdftoppm = shutil.which("pdftoppm")
    if pdftoppm:
        ok, output = run_command(
            [pdftoppm, "-f", str(page), "-l", str(page), "-r", "180", "-png", str(pdf), str(out_prefix)]
        )
        if ok:
            candidates = sorted(out_prefix.parent.glob(f"{out_prefix.name}-*.png"))
            if candidates:
                target = out_prefix.parent / f"page-{page:02d}.png"
                candidates[0].replace(target)
                manifest["page_png"] = str(target)
                return target
        manifest.setdefault("warnings", []).append(f"pdftoppm failed: {output}")

    magick = shutil.which("magick") or shutil.which("convert")
    if magick:
        target = out_prefix.parent / f"page-{page:02d}.png"
        page_selector = f"{pdf}[{page - 1}]"
        ok, output = run_command([magick, "-density", "180", page_selector, str(target)])
        if ok and target.exists():
            manifest["page_png"] = str(target)
            return target
        manifest.setdefault("warnings", []).append(f"ImageMagick render failed: {output}")

    manifest.setdefault("missing_tools", []).append("pdftoppm or ImageMagick renderer")
    return None


def extract_page_text(pdf: Path, page: int, output_path: Path, manifest: dict[str, object]) -> None:
    pdftotext = shutil.which("pdftotext")
    if not pdftotext:
        manifest.setdefault("missing_tools", []).append("pdftotext")
        return
    ok, output = run_command(
        [pdftotext, "-layout", "-f", str(page), "-l", str(page), str(pdf), str(output_path)]
    )
    if ok and output_path.exists():
        manifest["page_text"] = str(output_path)
    else:
        manifest.setdefault("warnings", []).append(f"pdftotext failed: {output}")


def crop_image(page_png: Path, crop: str | None, output_path: Path, manifest: dict[str, object]) -> None:
    if not crop:
        return
    magick = shutil.which("magick") or shutil.which("convert")
    if not magick:
        manifest.setdefault("missing_tools", []).append("ImageMagick crop")
        return

    identify = shutil.which("identify")
    if identify:
        ok, dims = run_command([identify, "-format", "%w %h", str(page_png)])
    elif Path(magick).name == "magick":
        ok, dims = run_command([magick, "identify", "-format", "%w %h", str(page_png)])
    else:
        manifest.setdefault("missing_tools", []).append("identify")
        return
    if not ok:
        manifest.setdefault("warnings", []).append(f"could not inspect page image size: {dims}")
        return

    width, height = [int(part) for part in dims.split()[:2]]
    geometry = crop_geometry(crop, width, height)
    ok, output = run_command([magick, str(page_png), "-crop", geometry, "+repage", str(output_path)])
    if ok and output_path.exists():
        manifest["crop_png"] = str(output_path)
        manifest["crop_geometry"] = geometry
    else:
        manifest.setdefault("warnings", []).append(f"crop failed: {output}")


def crop_geometry(crop: str, width: int, height: int) -> str:
    crop = crop.strip().lower()
    rect_match = re.fullmatch(r"(\d+),(\d+),(\d+),(\d+)", crop)
    if rect_match:
        x, y, w, h = [int(item) for item in rect_match.groups()]
        return f"{w}x{h}+{x}+{y}"

    if crop == "top":
        return f"{width}x{height // 2}+0+0"
    if crop == "bottom":
        return f"{width}x{height // 2}+0+{height // 2}"
    if crop == "left":
        return f"{width // 2}x{height}+0+0"
    if crop == "right":
        return f"{width // 2}x{height}+{width // 2}+0"
    if crop == "center":
        w = int(width * 0.7)
        h = int(height * 0.7)
        x = (width - w) // 2
        y = (height - h) // 2
        return f"{w}x{h}+{x}+{y}"
    raise ValueError("--crop must be top, bottom, left, right, center, or x,y,w,h")


def write_source_snippet(
    source: tuple[Path, int | None, int | None] | None,
    paper_dir: Path,
    output_path: Path,
    manifest: dict[str, object],
) -> None:
    if source is None:
        return
    path, start, end = source
    if not path.is_absolute():
        path = paper_dir / path
    if not path.exists():
        manifest.setdefault("warnings", []).append(f"source file not found: {path}")
        return

    lines = path.read_text(encoding="utf-8").splitlines()
    start = start or 1
    end = end or len(lines)
    start = max(1, start)
    end = min(len(lines), end)
    snippet = []
    for index in range(start, end + 1):
        snippet.append(f"{index:>5}  {lines[index - 1]}")
    output_path.write_text("\n".join(snippet) + "\n", encoding="utf-8")
    manifest["source_snippet"] = str(output_path)
    manifest["source"] = {"path": str(path), "start": start, "end": end}


def write_log_excerpt(log_path: Path | None, output_path: Path, manifest: dict[str, object]) -> None:
    if log_path is None:
        return
    if not log_path.exists():
        manifest.setdefault("warnings", []).append(f"log file not found: {log_path}")
        return

    selected = []
    for line in log_path.read_text(encoding="utf-8", errors="replace").splitlines():
        if WARNING_RE.search(line):
            selected.append(line)
    if not selected:
        selected.append("No matching warning/error lines found in log excerpt scan.")
    output_path.write_text("\n".join(selected[:250]) + "\n", encoding="utf-8")
    manifest["compile_log_excerpt"] = str(output_path)
    manifest["compile_log"] = str(log_path)


def write_prompt(args: argparse.Namespace, bundle_dir: Path, manifest: dict[str, object]) -> None:
    files = [
        path.name
        for path in sorted(bundle_dir.iterdir())
        if path.name not in {"prompt.md", "manifest.json"}
    ]
    body = [
        f"# LaTeX Layout Issue: {args.title}",
        "",
        "## Problem",
        "",
        args.problem.strip(),
        "",
        "## Location",
        "",
        f"- PDF: `{Path(args.pdf).name}`",
        f"- Page: {args.page}",
        f"- Object: {args.object or 'not specified'}",
        f"- Crop request: {args.crop or 'none'}",
        "",
        "## Bundle Files",
        "",
    ]
    body.extend(f"- `{name}`" for name in files)
    body.extend(
        [
            "",
            "## Instructions For The Fixing Agent",
            "",
            "- Use this bundle as the visual and source context for one local layout issue.",
            "- Identify whether the issue is prose length, float placement, algorithm/table/figure spacing, page break behavior, or a local interaction.",
            "- Prefer local, reversible fixes. Do not start with global `\\sloppy`, `\\emergencystretch`, paragraph, or global float-spacing changes.",
            "- Change one object at a time, then verify the same page through the configured compile backend.",
            "- Report the exact source change, compile backend, visual inspection result, and whether neighboring pages need rechecking.",
            "",
            "## Manifest Summary",
            "",
            "```json",
            json.dumps(manifest, indent=2, sort_keys=True),
            "```",
            "",
        ]
    )
    (bundle_dir / "prompt.md").write_text("\n".join(body), encoding="utf-8")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--paper-dir", required=True, help="Paper repo or worktree root.")
    parser.add_argument("--pdf", required=True, help="Rendered PDF path.")
    parser.add_argument("--page", required=True, type=int, help="1-indexed page number.")
    parser.add_argument("--title", required=True, help="Short issue title.")
    parser.add_argument("--problem", required=True, help="Visual problem description.")
    parser.add_argument("--object", default="", help="Affected object or paragraph.")
    parser.add_argument("--source", help="Optional source pointer: path:start-end.")
    parser.add_argument("--crop", help="Crop preset top/bottom/left/right/center or x,y,w,h.")
    parser.add_argument("--log", help="Optional compile log path.")
    parser.add_argument("--issue-id", help="Stable issue id. Defaults to date-page-title slug.")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    paper_dir = Path(args.paper_dir).expanduser().resolve()
    pdf = Path(args.pdf).expanduser()
    if not pdf.is_absolute():
        pdf = paper_dir / pdf
    pdf = pdf.resolve()
    if not paper_dir.exists():
        parser.error(f"--paper-dir does not exist: {paper_dir}")
    if not pdf.exists():
        parser.error(f"--pdf does not exist: {pdf}")
    if args.page < 1:
        parser.error("--page must be >= 1")

    issue_id = args.issue_id or f"{datetime.now().strftime('%Y-%m-%d')}-page-{args.page:02d}-{slugify(args.title)}"
    issue_id = slugify(issue_id)
    bundle_dir = paper_dir / ".agent" / "layout-issues" / issue_id
    bundle_dir.mkdir(parents=True, exist_ok=True)

    manifest: dict[str, object] = {
        "issue_id": issue_id,
        "created_at": datetime.now().isoformat(timespec="seconds"),
        "paper_dir": str(paper_dir),
        "pdf": str(pdf),
        "page": args.page,
        "title": args.title,
        "problem": args.problem,
        "object": args.object,
        "missing_tools": [],
        "warnings": [],
    }

    page_png = render_page(pdf, args.page, bundle_dir / "page", manifest)
    extract_page_text(pdf, args.page, bundle_dir / f"page-{args.page:02d}.txt", manifest)
    if page_png is not None:
        crop_image(page_png, args.crop, bundle_dir / "crop.png", manifest)
    elif args.crop:
        manifest.setdefault("warnings", []).append("crop requested but no page image was rendered")

    source = parse_source(args.source)
    write_source_snippet(source, paper_dir, bundle_dir / "source-snippet.tex", manifest)

    log_path: Path | None
    if args.log:
        log_path = Path(args.log).expanduser()
        if not log_path.is_absolute():
            log_path = paper_dir / log_path
    else:
        candidate = pdf.with_suffix(".log")
        log_path = candidate if candidate.exists() else None
    write_log_excerpt(log_path, bundle_dir / "compile-log-excerpt.txt", manifest)

    manifest_path = bundle_dir / "manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    write_prompt(args, bundle_dir, manifest)

    print(bundle_dir.relative_to(paper_dir))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

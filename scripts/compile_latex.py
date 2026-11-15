#!/usr/bin/env python3
"""Compile Bunthen Lesson Plan Projects Khmer/Math XeLaTeX documents into verified PDFs."""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_SMOKE_REL = (
    "01_កិច្ចតែងការបង្រៀន/ថ្នាក់ទី៨/"
    "ធរណីមាត្រ_មេរៀនទី១២_ការប្រៀបធៀបត្រីកោណ/"
    "៣.១_វិសមភាពចំពោះជ្រុងនិងមុំនៃត្រីកោណមួយ"
)


def is_excluded(path: Path) -> bool:
    """Return True if a path belongs to agent skills/hidden metadata that should not be built."""
    return ".agents" in path.parts or "dist_pdfs" in path.parts


def collect_tex_from_target(target_spec: str) -> list[Path]:
    """Collect sorted .tex files from a target file, directory, or 'latest'/'smoke' alias."""
    spec = target_spec.strip()
    if spec.lower() in {"latest", "smoke"}:
        spec = DEFAULT_SMOKE_REL

    candidate = Path(spec)
    if not candidate.is_absolute():
        candidate = REPO_ROOT / candidate
    candidate = candidate.resolve()

    if candidate.is_file():
        if candidate.suffix.lower() != ".tex":
            raise ValueError(f"Target file is not a .tex file: {candidate}")
        return [candidate]

    if candidate.is_dir():
        tex_files = sorted(p for p in candidate.rglob("*.tex") if p.is_file() and not is_excluded(p))
        if not tex_files:
            raise FileNotFoundError(f"No .tex files found under directory: {candidate}")
        return tex_files

    raise FileNotFoundError(f"Target path does not exist: {candidate}")


def collect_changed_tex(before_sha: str, after_sha: str) -> tuple[list[Path], bool]:
    """Collect changed .tex files between two commits, falling back to smoke slice if needed."""
    before = (before_sha or "").strip()
    after = (after_sha or "").strip()
    if not before or set(before) == {"0"} or not after:
        return collect_tex_from_target(DEFAULT_SMOKE_REL), True

    cmd = [
        "git",
        "-c",
        "core.quotePath=false",
        "diff",
        "--name-only",
        "--diff-filter=ACMR",
        before,
        after,
        "--",
        "*.tex",
    ]
    proc = subprocess.run(
        cmd,
        cwd=str(REPO_ROOT),
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=False,
    )
    if proc.returncode != 0:
        print(
            f"WARN: git diff failed ({proc.stderr.strip()}); falling back to smoke target.",
            file=sys.stderr,
        )
        return collect_tex_from_target(DEFAULT_SMOKE_REL), True

    changed: list[Path] = []
    for raw_line in proc.stdout.splitlines():
        rel = raw_line.strip()
        if not rel:
            continue
        p = (REPO_ROOT / rel).resolve()
        if p.is_file() and not is_excluded(p):
            changed.append(p)

    changed = sorted(set(changed))
    if not changed:
        return collect_tex_from_target(DEFAULT_SMOKE_REL), True
    return changed, False


def get_pdf_page_count(pdf_path: Path) -> str:
    """Return page count string using PyMuPDF when installed."""
    try:
        import fitz  # type: ignore
    except ImportError:
        return "?"

    with fitz.open(pdf_path) as doc:
        return str(len(doc))


def compile_single_tex(
    tex_path: Path,
    in_place: bool,
    compiled_manifest: list[str],
) -> bool:
    """Compile one .tex file with two xelatex passes and verify 0 errors / 0 missing glyphs."""
    try:
        rel_tex = tex_path.resolve().relative_to(REPO_ROOT.resolve())
    except ValueError:
        rel_tex = Path(tex_path.name)

    with tempfile.TemporaryDirectory() as tmp:
        tmp_dir = Path(tmp)
        cmd = [
            "xelatex",
            "-interaction=nonstopmode",
            "-halt-on-error",
            f"-output-directory={tmp_dir}",
            tex_path.name,
        ]
        pass_rcs: list[int] = []
        last_stdout = ""
        last_stderr = ""
        for _ in range(2):
            proc = subprocess.run(
                cmd,
                cwd=str(tex_path.parent),
                capture_output=True,
                text=True,
                encoding="utf-8",
                errors="replace",
                check=False,
            )
            pass_rcs.append(proc.returncode)
            last_stdout = proc.stdout
            last_stderr = proc.stderr
            if proc.returncode != 0:
                break

        log_path = tmp_dir / f"{tex_path.stem}.log"
        pdf_tmp_path = tmp_dir / f"{tex_path.stem}.pdf"
        log_lines: list[str] = []
        if log_path.is_file():
            log_lines = log_path.read_text(encoding="utf-8", errors="replace").splitlines()

        error_lines = [line for line in log_lines if line.startswith("! ")]
        if any(rc != 0 for rc in pass_rcs) or error_lines:
            print(f"FAIL: {rel_tex.as_posix()} (xelatex rcs={pass_rcs})", file=sys.stderr)
            if log_lines:
                print("--- Last 40 lines of .log ---", file=sys.stderr)
                for line in log_lines[-40:]:
                    print(line, file=sys.stderr)
            elif last_stdout or last_stderr:
                print(last_stdout[-2000:], file=sys.stderr)
                print(last_stderr[-1000:], file=sys.stderr)
            return False

        missing_lines = [
            line for line in log_lines if "Missing character: There is no" in line
        ]
        if missing_lines:
            print(
                f"FAIL: {rel_tex.as_posix()} has {len(missing_lines)} missing character(s):",
                file=sys.stderr,
            )
            for line in missing_lines[:20]:
                print(f"  {line}", file=sys.stderr)
            return False

        if not pdf_tmp_path.is_file() or pdf_tmp_path.stat().st_size == 0:
            print(
                f"FAIL: {rel_tex.as_posix()} produced missing or empty PDF.",
                file=sys.stderr,
            )
            return False

        dist_pdf_path = REPO_ROOT / "dist_pdfs" / rel_tex.parent / f"{tex_path.stem}.pdf"
        dist_pdf_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(pdf_tmp_path, dist_pdf_path)

        if in_place:
            target_pdf = tex_path.with_suffix(".pdf")
            shutil.copy2(pdf_tmp_path, target_pdf)
            rel_pdf_posix = (rel_tex.parent / f"{tex_path.stem}.pdf").as_posix()
            compiled_manifest.append(rel_pdf_posix)

        pages = get_pdf_page_count(dist_pdf_path)
        pdf_size = dist_pdf_path.stat().st_size
        print(f"OK: {rel_tex.as_posix()} -> {pages} pp., {pdf_size} B, missing=0")
        return True


def main() -> int:
    """Parse CLI arguments, compile requested .tex targets, and write dist_pdfs manifest."""
    parser = argparse.ArgumentParser(
        description="Compile Bunthen Lesson Plan Projects Khmer/Math XeLaTeX documents with 0-error verification."
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "--target",
        help="Relative or absolute path to a .tex file or folder, or 'latest' / 'smoke'.",
    )
    group.add_argument(
        "--changed",
        nargs=2,
        metavar=("BEFORE_SHA", "AFTER_SHA"),
        help="Compile .tex files changed between two commits (falls back to smoke if none).",
    )
    parser.add_argument(
        "--in-place",
        action="store_true",
        help="Also copy compiled PDFs alongside their .tex source and write compiled_paths.txt.",
    )
    args = parser.parse_args()

    used_smoke_fallback = False
    if args.target is not None:
        tex_files = collect_tex_from_target(args.target)
    else:
        tex_files, used_smoke_fallback = collect_changed_tex(
            args.changed[0], args.changed[1]
        )

    effective_in_place = bool(args.in_place and not used_smoke_fallback)
    print(
        f"Compiling {len(tex_files)} .tex file(s) "
        f"(effective_in_place={effective_in_place}, smoke_fallback={used_smoke_fallback})..."
    )

    compiled_manifest: list[str] = []
    all_ok = True
    for tex_path in tex_files:
        ok = compile_single_tex(tex_path, effective_in_place, compiled_manifest)
        if not ok:
            all_ok = False

    manifest_path = REPO_ROOT / "dist_pdfs" / "compiled_paths.txt"
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_body = "\n".join(compiled_manifest) + ("\n" if compiled_manifest else "")
    manifest_path.write_bytes(manifest_body.encode("utf-8"))

    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())

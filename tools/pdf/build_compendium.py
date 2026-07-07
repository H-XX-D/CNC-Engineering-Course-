#!/usr/bin/env python3
"""Build one combined course PDF from the canonical PDF exports."""

from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
PDF_DIR = BASE_DIR / "PDFs"
OUTPUT_PDF = PDF_DIR / "CNC-Engineering-Course-Compendium.pdf"

sys.path.insert(0, str(BASE_DIR / "tools"))

from course_manifest import MODULES  # noqa: E402


FRONT_MATTER = (
    "00-Table-of-Contents.pdf",
    "01-Foreword.pdf",
    "02-Acknowledgments.pdf",
    "03-Thank-You-to-AI.pdf",
    "04-License.pdf",
)


def canonical_pdf_paths() -> list[Path]:
    front_matter = [PDF_DIR / name for name in FRONT_MATTER]
    modules = [PDF_DIR / f"{module.export_stem}.pdf" for module in MODULES]
    appendices = sorted(PDF_DIR.glob("Appendix-*.pdf"))
    return front_matter + modules + appendices


def main() -> int:
    pdfunite = shutil.which("pdfunite")
    if not pdfunite:
        print("pdfunite is required to build the compendium PDF.")
        return 1

    inputs = canonical_pdf_paths()
    missing = [path for path in inputs if not path.exists()]
    if missing:
        print("Missing PDF inputs:")
        for path in missing:
            print(f"  {path.relative_to(BASE_DIR)}")
        return 1

    if OUTPUT_PDF.exists():
        OUTPUT_PDF.unlink()

    cmd = [pdfunite, *map(str, inputs), str(OUTPUT_PDF)]
    subprocess.run(cmd, check=True)
    print(f"Created {OUTPUT_PDF.relative_to(BASE_DIR)} from {len(inputs)} PDFs")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

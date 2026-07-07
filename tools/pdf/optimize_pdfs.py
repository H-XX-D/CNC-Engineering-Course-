#!/usr/bin/env python3
"""Optimize (compress) existing PDFs into an optimized folder."""

import subprocess
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
PDF_DIR = BASE_DIR / "PDFs"
OPTIMIZED_DIR = PDF_DIR / "optimized"

GS_CMD = [
    "gs",
    "-sDEVICE=pdfwrite",
    "-dCompatibilityLevel=1.4",
    "-dPDFSETTINGS=/ebook",
    "-dNOPAUSE",
    "-dQUIET",
    "-dBATCH",
]


def optimize_pdf(source: Path, target: Path) -> bool:
    cmd = GS_CMD + ["-sOutputFile=" + str(target), str(source)]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode == 0:
        print(f"✓ Optimized: {source.name} -> {target.name}")
        return True
    print(f"✗ Failed: {source.name}\n  {result.stderr.strip()}")
    return False


def main() -> None:
    if not PDF_DIR.exists():
        print(f"PDF directory not found: {PDF_DIR}")
        return

    OPTIMIZED_DIR.mkdir(parents=True, exist_ok=True)

    pdf_files = sorted([p for p in PDF_DIR.glob("*.pdf") if p.is_file()])

    if not pdf_files:
        print("No PDFs found to optimize.")
        return

    for pdf in pdf_files:
        target = OPTIMIZED_DIR / pdf.name
        optimize_pdf(pdf, target)

    print("\nOptimization complete. Optimized files stored in 'PDFs/optimized'.")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Generate PDFs for CNC Engineering Course
Creates individual PDFs for each module and a comprehensive table of contents
"""

import re
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Optional, List

# Repository and tool directories
BASE_DIR = Path(__file__).resolve().parents[2]
TOOL_DIR = Path(__file__).resolve().parent
BUILD_DIR = BASE_DIR / "build"
MODULES_DIR = BASE_DIR
APPENDICES_DIR = BASE_DIR / "Appendices"
PRINT_DIR = BASE_DIR / "Print"
PDF_DIR = BASE_DIR / "PDFs"
OPTIMIZED_PDF_DIR = PDF_DIR / "optimized"
TEMP_DIR = BUILD_DIR / "tmp_pdf"
PANDOC_HEADER = TOOL_DIR / "pandoc-header.tex"

PANDOC = shutil.which("pandoc")
TECTONIC = shutil.which("tectonic")
sys.path.insert(0, str(BASE_DIR / "tools"))

from course_manifest import get_module, find_module_dir, module_groups  # noqa: E402

# Ensure PDF directory exists
PDF_DIR.mkdir(exist_ok=True)
OPTIMIZED_PDF_DIR.mkdir(exist_ok=True)
TEMP_DIR.mkdir(parents=True, exist_ok=True)

# Map problematic Unicode characters to ASCII-safe equivalents for LaTeX
REPLACEMENTS = {
    "\u2260": "!=",
    "\u2264": "<=",
    "\u2265": ">=",
    "\u2070": "^0",
    "\xb9": "^1",
    "\u00b2": "^2",
    "\u00b3": "^3",
    "\u2074": "^4",
    "\u2075": "^5",
    "\u2076": "^6",
    "\u2077": "^7",
    "\u2078": "^8",
    "\u2079": "^9",
    "\u207b": "^-",
    "\u2080": "_0",
    "\u2081": "_1",
    "\u2082": "_2",
    "\u2083": "_3",
    "\u2084": "_4",
    "\u2085": "_5",
    "\u2086": "_6",
    "\u2087": "_7",
    "\u2088": "_8",
    "\u2089": "_9",
    "\u03bc": "mu",
    "\u03bd": "nu",
    "\u03b1": "alpha",
    "\u03b2": "beta",
    "\u03b3": "gamma",
    "\u03b4": "delta",
    "\u03b5": "epsilon",
    "\u03b6": "zeta",
    "\u03b7": "eta",
    "\u03b8": "theta",
    "\u03bb": "lambda",
    "\u03c0": "pi",
    "\u03c1": "rho",
    "\u03c3": "sigma",
    "\u03c4": "tau",
    "\u03c6": "phi",
    "\u03c8": "psi",
    "\u03c9": "omega",
    "\u0394": "Delta",
    "\u03a9": "Ohms",
    "\u03a6": "Phi",
    "\u03a3": "Sigma",
    "\u03c7": "chi",
    "\xb0": " deg",
    "\xe6": "ae",
    "\xe9": "e",
    "\xe8": "e",
    "\xf6": "o",
    "\xfc": "u",
    "\xd6": "O",
    "\xdc": "U",
    "\u0304": "",
    "\u00b5": "mu",
    "𝛥": "Delta",
    "𝛼": "alpha",
    "𝛽": "beta",
    "𝛾": "gamma",
    "𝛿": "delta",
    "𝜀": "epsilon",
    "𝜁": "zeta",
    "𝜂": "eta",
    "𝜃": "theta",
    "𝜆": "lambda",
    "𝜇": "mu",
    "𝜈": "nu",
    "𝜋": "pi",
    "𝜌": "rho",
    "𝜎": "sigma",
    "𝜏": "tau",
    "𝜙": "phi",
    "𝜓": "psi",
    "𝜔": "omega",
    "𝜖": "epsilon",
    "𝜛": "upsilon",
    "𝝅": "pi",
    "𝝍": "psi",
    "\u2202": "partial",
    "\u2207": "nabla",
    "\u2211": "sum",
    "\u221a": "sqrt",
    "\u221e": "infinity",
    "\u222b": "integral",
    "\u221d": "proportional to",
    "\u2243": "asymptotically equal",
    "\u207a": "^+",
    "\u2099": "_n",
    "\u209b": "_s",
    "\u1d40": "^T",
    "\u1d62": "_i",
    "\u1d63": "_r",
    "\u209a": "_p",
    "\u209c": "_t",
    "\u2191": "up",
    "\u2193": "down",
    "\u2194": "<->",
    "\u2195": "up/down",
    "\u2197": "up-right",
    "\u21a7": "down",
    "\u21b3": "return",
    "\u2220": "angle",
    "\u2225": "parallel",
    "\u2261": "equivalent",
    "\u2295": "plus",
    "\u22a5": "perpendicular",
    "\u2300": "diameter",
    "\u2312": "arc",
    "\u2313": "profile",
    "\u2316": "position",
    "\u232d": "cylindricity",
    "\u2334": "flatness",
    "\u24c1": "(L)",
    "\u24c2": "(M)",
    "\u2022": "-",
    "\u2113": "l",
    "\u203e": "-",
    "\u22c5": "*",
    "\u2605": "*",
    "\u26a0": "Warning",
    "\u2705": "[check]",
    "\u274c": "[x]",
    "\ufe0f": "",
    "\u25cb": "o",
    "\u25b2": "^",
    "\u25ba": ">",
    "\u25c4": "<",
    "\u2591": " ",
    "\u2593": "#",
    "\u2584": "_",
    "\u2588": "#",
    "\u258c": "|",
    "\u2590": "|",
    "\u2550": "=",
    "\u256e": "+",
    "\u256f": "+",
    "\u2717": "x",
    "\u2b1c": "[ ]",
    "\u2460": "(1)",
    "\u2461": "(2)",
    "\u2462": "(3)",
    "\u2463": "(4)",
    "\u2464": "(5)",
    "\u2465": "(6)",
    "\u2466": "(7)",
    "\u2713": "[check]",
    "\u2610": "[ ]",
    "\u25a1": "[ ]",
    "\u2500": "-",
    "\u2502": "|",
    "\u250c": "+",
    "\u2510": "+",
    "\u2514": "+",
    "\u2518": "+",
    "\u252c": "+",
    "\u2534": "+",
    "\u251c": "|",
    "\u2524": "|",
    "\u253c": "+",
    "\u2014": "--",
    "\u2013": "-",
    "\u2248": "approx",
    "\u2192": "->",
    "\u2190": "<-",
    "\u00d7": "x",
    "\u00f7": "/",
    "\u00b7": "*",
    "\u00b1": "+/-",
    "\u2212": "-",
    "\u2122": "TM",
    "\u2120": "SM",
    "\xae": "(R)",
    "\xa2": "cents",
    "\xbc": "1/4",
    "\xbd": "1/2",
    "\xa7": "section",
    "\xc5": "A",
    "\xd8": "O",
    "\xf8": "o",
    "\xe4": "a",
    "\u0393": "Gamma",
    "\u039b": "Lambda",
    "\u03be": "xi",
    "\u1e8b": "x-dot",
    "\u1e8d": "x-ddot",
    "\u0307": "",
    "\u0308": "",
    "\u2011": "-",
    "\u2019": "'",
    "\u201c": "\"",
    "\u201d": "\"",
    "\u202f": " ",
    "\u21d2": "=>",
    "\u2196": "up-left",
    "\u2198": "down-right",
    "\u2199": "down-left",
    "\u2b06": "up",
    "\u25bc": "down",
    "\u25c1": "<",
    "\u25cb": "o",
    "\u25d0": "half",
    "\u25b3": "triangle",
    "\u25b7": ">",
    "\u25c6": "diamond",
    "\u2b25": "diamond",
    "\u25cf": "o",
    "\u25ce": "target",
    "\u232f": "runout",
    "\u23e5": "symmetry",
    "\u23f1": "timer",
    "\u2504": "-",
    "\u254c": "-",
    "\u2551": "|",
    "\u2554": "+",
    "\u2557": "+",
    "\u255a": "+",
    "\u255d": "+",
    "\u2560": "+",
    "\u2563": "+",
    "\u2571": "/",
    "\u2572": "\\",
    "\u2611": "[x]",
    "\u263c": "sun",
    "\u26a1": "power",
    "\U0001f534": "[red]",
    "\U0001f7e1": "[yellow]",
    "\U0001f7e2": "[green]",
    "\U0001f4f7": "[camera]",
    "\U0001f389": "[celebration]",
    "\U0001f53a": "[alert]",
    "串": "",
    "联": "",
    "え": "",
    "る": "",
    "カ": "",
    "ケ": "",
    "ポ": "",
    "ヨ": "",
    "化": "",
    "善": "",
    "場": "",
    "改": "",
    "板": "",
    "燈": "",
    "現": "",
    "看": "",
    "行": "",
    "見": "",
    "\uff0c": ",",
    "\uff1a": ":"
}

def sanitize_text(text: str) -> str:
    """Replace problematic characters with LaTeX-safe alternatives and handle math delimiters"""
    # Apply Unicode replacements before math handling so replacement text cannot
    # introduce new math delimiters.
    for old, new in REPLACEMENTS.items():
        text = text.replace(old, new)

    # Normalize plain Windows paths before Pandoc turns backslashes into TeX.
    lines = text.split('\n')
    processed_lines = []
    for line in lines:
        if re.search(r'[A-Za-z]:\\', line):
            processed_line = line.replace('\\', '/')
        else:
            processed_line = line
        processed_lines.append(processed_line)
    text = '\n'.join(processed_lines)

    text = text.replace(r'\r\n', 'CRLF')
    text = text.replace(r'\n', 'LF')
    text = text.replace(r'\0.', '0.')
    text = text.replace('($$$)', '(high)')
    text = text.replace('($$)', '(medium)')
    text = text.replace('($)', '(small)')
    text = re.sub(r'(?<!\S)\$\$\$[ \t]+(?=[A-Za-z])', 'High cost ', text)
    text = re.sub(r'(?<!\S)\$\$[ \t]+(?=[A-Za-z])', 'Medium cost ', text)
    text = re.sub(r'(?<!\S)\$[ \t]+(?=[A-Za-z])', 'Low cost ', text)
    text = text.replace('in^3/min', 'in3/min')
    text = text.replace('cm^3/min', 'cm3/min')
    text = text.replace('mm^3/s', 'mm3/s')

    # Currency and cost notation are common in business/process modules. Escape
    # those dollars before treating remaining dollar pairs as inline math.
    text = re.sub(r'(?<![\\$])\$(?!\$)(?=[\d/])', r'\\$', text)
    text = re.sub(r'\\\$(\d+(?:\.\d+)?\\)', r'$\1', text)
    text = re.sub(r'\\\$(\d+(?:\.\d+)?)(?=\s+(?:\\(?!text\b)|[A-Z_]))', r'$\1', text)

    def restore_numeric_math(match: re.Match[str]) -> str:
        expression = match.group(1)
        if expression.endswith('\\') or r'\$' in expression or r'\text' in expression:
            return match.group(0)
        return f'${expression}$'

    text = re.sub(r'\\\$(\d+(?:\.\d+)?(?:\s*[/=+\-]\s*[^$\n]+)?)\$(?!\$)', restore_numeric_math, text)

    return text

def sanitize_title(title: str) -> str:
    """Sanitize title strings for LaTeX metadata"""
    return title.replace("&", "and").strip()

def ensure_pandoc_header() -> None:
    """Ensure the Pandoc header file exists with layout tuning commands."""
    if PANDOC_HEADER.exists():
        return
    PANDOC_HEADER.write_text(
        r"""% Pandoc header tweaks to help LaTeX line breaking
\setlength{\emergencystretch}{3em}
\sloppy
""",
        encoding="utf-8",
    )

def prepare_temp_file(source_path: Path, temp_name: Optional[str] = None) -> Path:
    """Create a sanitized copy of the markdown file for PDF conversion"""
    target_name = temp_name or source_path.name
    temp_path = TEMP_DIR / target_name
    with open(source_path, 'r', encoding='utf-8') as src:
        sanitized = sanitize_text(src.read())
    with open(temp_path, 'w', encoding='utf-8') as dst:
        dst.write(sanitized)
    return temp_path

def get_module_name(module_num):
    """Get module name from module master outline file"""
    return get_module(module_num).title

def convert_to_pdf(markdown_file, output_pdf, title: str = "", include_toc: bool = True):
    """Convert markdown file to PDF using pandoc with the Tectonic engine"""
    if PANDOC is None:
        print("✗ pandoc not found. Please install pandoc to generate PDFs.")
        return False

    if TECTONIC is None:
        print("✗ tectonic not found. Install it for LaTeX-based PDF output.")
        return False

    try:
        clean_title = sanitize_title(title) if title else ""
        ensure_pandoc_header()
        cmd = [
            PANDOC,
            str(markdown_file),
            '-o', str(output_pdf),
            '--standalone',
            '--pdf-engine', 'tectonic',
            '--from', 'markdown+smart+pipe_tables+grid_tables+multiline_tables',
            '--variable', 'geometry:margin=1in',
            '--include-in-header', str(PANDOC_HEADER)
        ]

        if include_toc:
            cmd.append('--toc')

        if clean_title:
            cmd.extend(['--metadata', f'title={clean_title}'])

        cmd.extend([
            '--metadata', r'header-includes=\setlength{\emergencystretch}{3em}',
            '--metadata', r'header-includes=\sloppy'
        ])
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            print(f"✓ Created: {output_pdf.name}")
            return True
        else:
            print(f"✗ Failed: {output_pdf.name}")
            print(f"  Error: {result.stderr[:200]}")
            return False
    except Exception as e:
        print(f"✗ Error creating {output_pdf.name}: {e}")
        return False

def combine_markdown_files(parts: List[Path], output_file: Path) -> None:
    """Concatenate multiple markdown files into a single file with page breaks"""
    with open(output_file, 'w', encoding='utf-8') as combined:
        for idx, part in enumerate(parts):
            with open(part, 'r', encoding='utf-8') as src:
                combined.write(src.read().strip())
            if idx != len(parts) - 1:
                combined.write("\n\n\\newpage\n\n")

def optimize_pdf(input_pdf: Path, output_pdf: Path) -> bool:
    """Compress PDF size using Ghostscript"""
    cmd = [
        'gs',
        '-sDEVICE=pdfwrite',
        '-dCompatibilityLevel=1.4',
        '-dPDFSETTINGS=/ebook',
        '-dNOPAUSE',
        '-dQUIET',
        '-dBATCH',
        '-sOutputFile=' + str(output_pdf),
        str(input_pdf)
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode == 0:
        print(f"✓ Optimized: {output_pdf.name}")
        return True
    else:
        print(f"✗ Optimization failed for {input_pdf.name}: {result.stderr[:200]}")
        return False

def merge_module_files(module_dir, output_file):
    """Merge all section files in a module into one file for PDF generation"""
    sections: List[str] = []
    section_files = [
        file
        for file in sorted(module_dir.glob("*.md"))
        if not file.name.startswith("module-") and file.name != output_file.name
    ]

    for idx, file in enumerate(section_files):
        with open(file, 'r', encoding='utf-8') as f:
            content = sanitize_text(f.read())
            sections.append(content.strip())
        if idx != len(section_files) - 1:
            sections.append("\n\n\\newpage\n\n")  # Force page break between sections

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("\n".join(sections))

def generate_toc():
    """Generate comprehensive table of contents"""
    toc_content = """# CNC Engineering Course
## Table of Contents

**Author**: Todd  
**Company**: Hendrixx Design  
**Contact**: todd@hendrixxdesign.com

---

## Front Matter

1. **Foreword** - A Word from the Author
2. **Acknowledgments** - Recognition of Contributors
3. **Thank You to AI** - Collaboration with AI Tools
4. **License** - Course Terms and Conditions

---

## Course Modules

"""

    for group_name, modules in module_groups():
        toc_content += f"### {group_name}\n\n"
        for module in modules:
            toc_content += f"**Module {module.number_text}**: {module.title}\n\n"
        toc_content += "\n"
    
    toc_content += "\n---\n\n## Appendices\n\n"
    
    # Add appendices
    appendix_names = {
        'A': 'Material Properties',
        'B': 'Hardware Specifications',
        'C': 'Motor Drive Sizing',
        'D': 'Linear Motion',
        'E': 'Electrical Standards',
        'F': 'G-code Reference',
        'G': 'Safety Standards',
        'H': 'Lubrication',
        'I': 'Conversions',
        'J': 'Troubleshooting',
        'K': 'Vendors',
        'L': 'Resources',
        'M': 'Glossary',
        'N': 'Contact',
        'O': 'Updates',
        'P': 'Mathematics',
        'Q': 'QMS Templates',
        'R': 'Organization Templates',
        'S': 'LEAN Manufacturing Templates (2,910 lines)',
        'T': 'Business Ownership Templates (6,612 lines)'
    }
    
    for letter, name in appendix_names.items():
        toc_content += f"**Appendix {letter}**: {name}\n\n"
    
    toc_content += "\n---\n\n## Course Information\n\n"
    toc_content += "**Total Modules**: 26 comprehensive modules\n\n"
    toc_content += "**Total Appendices**: 20 reference appendices (including 9,500+ lines of templates)\n\n"
    toc_content += "**Course Scope**: Foundation through advanced topics and business ownership\n\n"
    toc_content += "**Target Audience**: Entry-level through experienced professionals and entrepreneurs\n\n"
    toc_content += "\n---\n\n"
    toc_content += "*Course Version 1.0 | Last Updated: November 2025*\n"
    
    # Write TOC
    toc_file = BASE_DIR / "table-of-contents.md"
    with open(toc_file, 'w', encoding='utf-8') as f:
        f.write(toc_content)
    
    print(f"\n✓ Created: table-of-contents.md")

    sanitized_toc = prepare_temp_file(toc_file, "table-of-contents-sanitized.md")

    # Convert TOC to PDF
    toc_pdf = PDF_DIR / "00-Table-of-Contents.pdf"
    convert_to_pdf(sanitized_toc, toc_pdf, "CNC Engineering Course - Table of Contents", include_toc=False)
    
    return sanitized_toc

def main():
    print("=" * 60)
    print("CNC Engineering Course - PDF Generation")
    print("=" * 60)
    
    foreword_md: Optional[Path] = None
    acknowledgments_md: Optional[Path] = None
    thank_you_md: Optional[Path] = None
    module_markdowns: List[Path] = []
    appendix_markdowns: List[Path] = []

    # Generate Table of Contents
    print("\n📄 Generating Table of Contents...")
    sanitized_toc = generate_toc()
    
    # Generate Front Matter PDFs
    print("\n📄 Generating Front Matter PDFs...")
    
    front_matter = [
        (PRINT_DIR / "course-foreword.md", "01-Foreword.pdf", "Foreword"),
        (PRINT_DIR / "course-acknowledgments.md", "02-Acknowledgments.pdf", "Acknowledgments"),
        (PRINT_DIR / "thank-you-to-ai.md", "03-Thank-You-to-AI.pdf", "Thank You to AI"),
        (PRINT_DIR / "course-license.md", "04-License.pdf", "License")
    ]
    
    for source, pdf_name, title in front_matter:
        if source.exists():
            output_pdf = PDF_DIR / pdf_name
            temp_md = prepare_temp_file(source, f"{source.stem}-sanitized.md")
            convert_to_pdf(temp_md, output_pdf, title, include_toc=False)
            stem_lower = source.stem.lower()
            if "foreword" in stem_lower:
                foreword_md = temp_md
            elif "acknowledgments" in stem_lower:
                acknowledgments_md = temp_md
            elif "thank-you" in stem_lower:
                thank_you_md = temp_md
        else:
            print(f"⚠ Warning: {source} not found")
    
    # Generate Module PDFs
    print("\n📄 Generating Module PDFs...")
    
    for group_name, modules in module_groups():
        print(f"\n  {group_name}")
        for module in modules:
            module_num = module.number
            module_dir = find_module_dir(MODULES_DIR, module_num)
        
            if module_dir is None:
                print(f"⚠ Warning: Module-{module_num:02d} not found")
                continue
        
            module_name = module.title
        
            # Create merged module file
            merged_file = TEMP_DIR / f"module-{module_num:02d}-complete.md"
            merge_module_files(module_dir, merged_file)
            module_markdowns.append(merged_file)
        
            # Convert to PDF
            output_pdf = PDF_DIR / f"{module.export_stem}.pdf"
            convert_to_pdf(merged_file, output_pdf, f"Module {module_num}: {module_name}", include_toc=False)
    
    # Generate Appendix PDFs
    print("\n📄 Generating Appendix PDFs...")
    
    for appendix_file in sorted(APPENDICES_DIR.glob("appendix-*.md")):
        letter = appendix_file.stem.split('-')[1].upper()
        name = ' '.join(appendix_file.stem.split('-')[2:]).title()
        
        temp_md = prepare_temp_file(appendix_file, f"{appendix_file.stem}-sanitized.md")
        appendix_markdowns.append(temp_md)
        output_pdf = PDF_DIR / f"Appendix-{letter}-{appendix_file.stem.split('-', 2)[2]}.pdf"
        convert_to_pdf(temp_md, output_pdf, f"Appendix {letter}: {name}", include_toc=False)

    # Build combined course PDF
    print("\n📄 Building compiled course PDF...")

    combined_sections: List[Path] = []
    if sanitized_toc:
        combined_sections.append(sanitized_toc)
    if foreword_md:
        combined_sections.append(foreword_md)
    else:
        print("⚠ Warning: Foreword not found; compiled PDF will omit it")

    combined_sections.extend(module_markdowns)
    combined_sections.extend(appendix_markdowns)

    if acknowledgments_md:
        combined_sections.append(acknowledgments_md)
    else:
        print("⚠ Warning: Acknowledgments not found; compiled PDF will omit it")

    if thank_you_md:
        combined_sections.append(thank_you_md)
    else:
        print("⚠ Warning: Thank You to AI not found; compiled PDF will omit it")

    combined_md = TEMP_DIR / "cnc-engineering-course-combined.md"
    combine_markdown_files(combined_sections, combined_md)

    combined_pdf = PDF_DIR / "CNC-Engineering-Course-Complete.pdf"
    convert_to_pdf(combined_md, combined_pdf, "CNC Engineering Course", include_toc=False)

    # Optimize PDFs
    print("\n📦 Optimizing PDFs for upload...")
    if shutil.which('gs'):
        for pdf_file in PDF_DIR.glob("*.pdf"):
            optimized_path = OPTIMIZED_PDF_DIR / pdf_file.name
            optimize_pdf(pdf_file, optimized_path)
    else:
        print("⚠ Ghostscript not found; skipping PDF optimization step.")
    
    print("\n" + "=" * 60)
    print("✅ PDF Generation Complete!")
    print(f"📁 PDFs saved to: {PDF_DIR}")
    print(f"📁 Optimized PDFs saved to: {OPTIMIZED_PDF_DIR}")
    # Clean up temporary markdown files
    for temp_file in list(TEMP_DIR.iterdir()):
        if temp_file.is_file():
            temp_file.unlink()
    print("=" * 60)

if __name__ == "__main__":
    main()

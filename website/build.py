#!/usr/bin/env python3
"""
Build the CNC Engineering Course website content from root-level module folders.
"""

import os
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
MODULES_DIR = BASE_DIR
OUTPUT_DIR = BASE_DIR / 'website' / 'content'

# Ensure output directory exists
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
sys.path.insert(0, str(BASE_DIR / "tools"))

from course_manifest import all_module_numbers, find_module_dir  # noqa: E402

# Module numbers to process
MODULE_NUMS = all_module_numbers()

def get_section_files(module_dir):
    """Get all content files from a module directory, sorted."""
    files = []
    for f in os.listdir(module_dir):
        if f.endswith('.md') and 'master-outline' not in f.lower():
            files.append(f)
    
    # Sort by numeric prefix if present
    def sort_key(filename):
        # Handle patterns like "1_1.name.md" or "section-1.1.md"
        name = filename.lower()
        if name.startswith('section-'):
            parts = name.replace('section-', '').replace('.md', '').split('.')
        elif '_' in name[:4]:
            parts = name.split('_')[0:2]
            if '.' in parts[1]:
                parts = [parts[0]] + parts[1].split('.')[0:1]
        else:
            parts = ['999', '999']
        
        try:
            return (int(parts[0]), int(parts[1]) if len(parts) > 1 else 0)
        except:
            return (999, 999)
    
    return sorted(files, key=sort_key)

def build_module(module_num):
    """Build a single module's content file."""
    module_dir = find_module_dir(MODULES_DIR, module_num)
    
    if module_dir is None:
        print(f"  Module-{module_num:02d}: Directory not found, skipping")
        return False
    
    section_files = get_section_files(module_dir)
    
    if not section_files:
        print(f"  Module-{module_num}: No content files found")
        return False
    
    # Combine all section content
    combined = []
    for filename in section_files:
        filepath = module_dir / filename
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read().strip()
                if content:
                    combined.append(content)
        except Exception as e:
            print(f"    Warning: Could not read {filename}: {e}")
    
    if not combined:
        return False
    
    # Write combined content
    output_file = OUTPUT_DIR / f'module-{module_num:02d}.md'
    full_content = '\n\n---\n\n'.join(combined)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(full_content)
    
    print(f"  Module-{module_num:02d}: {len(section_files)} sections -> {output_file.name}")
    return True

def main():
    print("=" * 60)
    print("Building CNC Engineering Course Website Content")
    print("=" * 60)
    print(f"\nSource: {MODULES_DIR}")
    print(f"Output: {OUTPUT_DIR}\n")
    
    success = 0
    for num in MODULE_NUMS:
        if build_module(num):
            success += 1
    
    print(f"\n{'=' * 60}")
    print(f"Complete! {success}/{len(MODULE_NUMS)} modules built.")
    print("=" * 60)

if __name__ == '__main__':
    main()

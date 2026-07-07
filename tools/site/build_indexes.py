#!/usr/bin/env python3
"""Build glossary, resource, and link-graph data for the static website."""

from __future__ import annotations

import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
WEBSITE_DATA_DIR = BASE_DIR / "website" / "data"

sys.path.insert(0, str(BASE_DIR / "tools"))

from course_manifest import MODULES, find_module_dir  # noqa: E402


def slugify(value: str) -> str:
    value = value.lower()
    value = re.sub(r"[^a-z0-9]+", "-", value).strip("-")
    return re.sub(r"-+", "-", value)


def strip_markdown(value: str) -> str:
    value = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", value)
    value = re.sub(r"[`*_~]", "", value)
    return re.sub(r"\s+", " ", value).strip()


def parse_glossary() -> list[dict[str, str]]:
    glossary = BASE_DIR / "Appendices" / "appendix-M-glossary.md"
    current_category = ""
    entries: list[dict[str, str]] = []
    active: dict[str, str] | None = None

    for raw_line in glossary.read_text(encoding="utf-8").splitlines():
        line = raw_line.rstrip()
        heading = re.match(r"^##\s+M\.\d+\s+(.+)$", line)
        if heading:
            current_category = strip_markdown(heading.group(1))
            active = None
            continue

        term_match = re.match(r"^-\s+\*\*(.+?):\*\*\s*(.*)$", line)
        if term_match:
            term = strip_markdown(term_match.group(1))
            definition = strip_markdown(term_match.group(2))
            active = {
                "id": f"term-{slugify(term)}",
                "term": term,
                "category": current_category,
                "definition": definition,
            }
            entries.append(active)
            continue

        if active and line.startswith("  - "):
            active["definition"] = f"{active['definition']} {strip_markdown(line[4:])}".strip()

    return entries


def parse_markdown_tables(text: str) -> list[tuple[str, list[str], list[list[str]]]]:
    tables: list[tuple[str, list[str], list[list[str]]]] = []
    current_heading = ""
    lines = text.splitlines()
    i = 0
    while i < len(lines):
        heading = re.match(r"^#{2,3}\s+(.+)$", lines[i])
        if heading:
            current_heading = strip_markdown(re.sub(r"^[A-Z]\.\d+(?:\.\d+)?\s+", "", heading.group(1)))
            i += 1
            continue

        if lines[i].startswith("|") and i + 1 < len(lines) and re.match(r"^\|[-:\s|]+\|$", lines[i + 1]):
            headers = [strip_markdown(cell) for cell in lines[i].strip("|").split("|")]
            rows: list[list[str]] = []
            i += 2
            while i < len(lines) and lines[i].startswith("|"):
                rows.append([strip_markdown(cell) for cell in lines[i].strip("|").split("|")])
                i += 1
            tables.append((current_heading, headers, rows))
            continue

        i += 1
    return tables


def normalize_url(value: str) -> str:
    value = value.strip()
    if not value or value.lower() in {"n/a", "none"}:
        return ""
    if re.match(r"https?://", value):
        return value
    if "." in value and " " not in value:
        return f"https://{value}"
    return ""


def parse_resources() -> list[dict[str, str]]:
    resources_md = (BASE_DIR / "Appendices" / "appendix-L-resources.md").read_text(encoding="utf-8")
    resources: list[dict[str, str]] = []

    for category, headers, rows in parse_markdown_tables(resources_md):
        for row in rows:
            if not row or len(row) != len(headers):
                continue
            data = dict(zip(headers, row))
            title = row[0]
            url = ""
            for cell in row:
                url = normalize_url(cell)
                if url:
                    break
            description_parts = [cell for cell in row[1:] if cell and normalize_url(cell) != cell]
            resources.append(
                {
                    "id": f"resource-{slugify(category)}-{slugify(title)}",
                    "title": title,
                    "category": category,
                    "url": url,
                    "description": " | ".join(description_parts),
                    "fields": data,
                }
            )

    return resources


def module_text(module_number: int) -> str:
    module_dir = find_module_dir(BASE_DIR, module_number)
    if module_dir is None:
        return ""
    parts = []
    for path in sorted(module_dir.glob("*.md")):
        if not path.name.startswith("module-"):
            parts.append(path.read_text(encoding="utf-8", errors="ignore"))
    return "\n".join(parts).lower()


def build_graph(glossary: list[dict[str, str]], resources: list[dict[str, str]]) -> dict[str, list[dict[str, str]]]:
    nodes: dict[str, dict[str, str]] = {}
    edges: list[dict[str, str | int]] = []

    def add_node(node_id: str, label: str, kind: str, group: str = "") -> None:
        nodes[node_id] = {"id": node_id, "label": label, "kind": kind, "group": group}

    add_node("appendix-glossary", "Glossary", "appendix", "Appendices")
    add_node("appendix-resources", "Recommended Resources", "appendix", "Appendices")

    for module in MODULES:
        module_id = f"module-{module.number_text}"
        add_node(module_id, f"Module {module.number_text}: {module.title}", "module", module.group)

    for entry in glossary:
        add_node(entry["id"], entry["term"], "term", entry["category"])
        edges.append({"source": "appendix-glossary", "target": entry["id"], "relation": "defines", "weight": 1})

    for resource in resources:
        add_node(resource["id"], resource["title"], "resource", resource["category"])
        edges.append({"source": "appendix-resources", "target": resource["id"], "relation": "lists", "weight": 1})

    term_patterns = [
        (entry, re.compile(rf"\b{re.escape(entry['term'].lower())}\b"))
        for entry in glossary
        if len(entry["term"]) >= 4 and not re.search(r"[/(),]", entry["term"])
    ]

    for module in MODULES:
        text = module_text(module.number)
        module_id = f"module-{module.number_text}"
        counts: Counter[str] = Counter()
        for entry, pattern in term_patterns:
            matches = len(pattern.findall(text))
            if matches:
                counts[entry["id"]] = matches

        for term_id, count in counts.most_common(18):
            edges.append({"source": module_id, "target": term_id, "relation": "mentions", "weight": count})

    resource_keywords = {
        "linuxcnc": "module-14",
        "fusion 360": "module-16",
        "freecad": "module-16",
        "g-code": "module-15",
        "machinery": "module-20",
        "metrology": "module-21",
        "quality": "module-22",
        "lean": "module-24",
        "plasma": "module-05",
        "laser": "module-07",
        "waterjet": "module-08",
    }
    for resource in resources:
        haystack = f"{resource['title']} {resource['description']}".lower()
        for keyword, module_id in resource_keywords.items():
            if keyword in haystack:
                edges.append({"source": module_id, "target": resource["id"], "relation": "resource", "weight": 1})

    return {"nodes": list(nodes.values()), "edges": edges}


def main() -> int:
    WEBSITE_DATA_DIR.mkdir(parents=True, exist_ok=True)

    glossary = parse_glossary()
    resources = parse_resources()
    graph = build_graph(glossary, resources)

    outputs = {
        "glossary.json": glossary,
        "resources.json": resources,
        "link-graph.json": graph,
    }
    for filename, data in outputs.items():
        (WEBSITE_DATA_DIR / filename).write_text(json.dumps(data, indent=2), encoding="utf-8")
        print(f"Wrote website/data/{filename}")

    print(f"Glossary terms: {len(glossary)}")
    print(f"Resources: {len(resources)}")
    print(f"Graph nodes: {len(graph['nodes'])}")
    print(f"Graph edges: {len(graph['edges'])}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

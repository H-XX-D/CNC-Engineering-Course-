"""Authoritative course module metadata."""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class ModuleInfo:
    number: int
    title: str
    group: str

    @property
    def number_text(self) -> str:
        return f"{self.number:02d}"

    @property
    def slug(self) -> str:
        replacements = {
            "&": "and",
            "/": "-",
            ":": "",
            "(": "",
            ")": "",
        }
        slug = self.title.replace("4.0", "4-0")
        for old, new in replacements.items():
            slug = slug.replace(old, new)
        slug = re.sub(r"(?<=[A-Za-z])\.(?=[A-Za-z])", "", slug)
        slug = slug.replace(".", "-")
        slug = re.sub(r"[^A-Za-z0-9]+", "-", slug).strip("-")
        return re.sub(r"-+", "-", slug)

    @property
    def directory_name(self) -> str:
        return f"Module-{self.number_text}-{self.slug}"

    @property
    def export_stem(self) -> str:
        return f"Module-{self.number_text}-{self.slug}"


MODULES = (
    ModuleInfo(1, "Mechanical Frame and Structure", "Foundation Modules"),
    ModuleInfo(2, "Vertical Axis and Z-Stage", "Foundation Modules"),
    ModuleInfo(3, "Linear Motion Systems", "Foundation Modules"),
    ModuleInfo(4, "Control Electronics", "Foundation Modules"),
    ModuleInfo(5, "Plasma Cutting", "Tool-Specific Modules"),
    ModuleInfo(6, "Spindle and Rotary Tools", "Tool-Specific Modules"),
    ModuleInfo(7, "Fiber Laser", "Tool-Specific Modules"),
    ModuleInfo(8, "Waterjet Cutting", "Tool-Specific Modules"),
    ModuleInfo(9, "Pick and Place Robot", "Advanced and Hybrid Systems"),
    ModuleInfo(10, "Robotic Arm", "Advanced and Hybrid Systems"),
    ModuleInfo(11, "Large-Format FDM 3D Printing", "Advanced and Hybrid Systems"),
    ModuleInfo(12, "Water-Jet Guided Laser Cutting", "Advanced and Hybrid Systems"),
    ModuleInfo(13, "EMI/EMC for Motion Control", "Control, Software, and Process Engineering"),
    ModuleInfo(14, "LinuxCNC HAL and Real-Time Control", "Control, Software, and Process Engineering"),
    ModuleInfo(15, "G-Code Standards and Post-Processing", "Control, Software, and Process Engineering"),
    ModuleInfo(16, "CAD Design for Manufacturable Parts", "Control, Software, and Process Engineering"),
    ModuleInfo(17, "Advanced Materials: Composites and Ceramics", "Control, Software, and Process Engineering"),
    ModuleInfo(18, "Industry 4.0 for CNC Manufacturing", "Control, Software, and Process Engineering"),
    ModuleInfo(19, "Advanced Control Systems", "Control, Software, and Process Engineering"),
    ModuleInfo(20, "Feeds and Speeds", "Control, Software, and Process Engineering"),
    ModuleInfo(21, "Metrology and Precision Measurement", "Professional and Business Modules"),
    ModuleInfo(22, "Quality Management Systems (QMS)", "Professional and Business Modules"),
    ModuleInfo(23, "Shop Organization and Management", "Professional and Business Modules"),
    ModuleInfo(24, "L.E.A.N. Strategies for CNC Manufacturing", "Professional and Business Modules"),
    ModuleInfo(25, "Work-Life Balance in CNC Manufacturing", "Professional and Business Modules"),
    ModuleInfo(26, "CNC Business Ownership and Management", "Professional and Business Modules"),
)


def all_module_numbers() -> list[int]:
    return [module.number for module in MODULES]


def module_groups() -> list[tuple[str, tuple[ModuleInfo, ...]]]:
    groups: list[tuple[str, list[ModuleInfo]]] = []
    for module in MODULES:
        if not groups or groups[-1][0] != module.group:
            groups.append((module.group, []))
        groups[-1][1].append(module)
    return [(name, tuple(modules)) for name, modules in groups]


def get_module(number: int) -> ModuleInfo:
    for module in MODULES:
        if module.number == number:
            return module
    raise KeyError(f"Unknown module number: {number}")


def find_module_dir(modules_dir: Path, number: int) -> Path | None:
    prefix = f"Module-{number:02d}"
    matches = sorted(path for path in modules_dir.glob(f"{prefix}*") if path.is_dir())
    return matches[0] if matches else None

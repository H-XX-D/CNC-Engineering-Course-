#!/usr/bin/env python3
"""Focused tests for audit_intake.py."""

from __future__ import annotations

import copy
import json
import unittest
from pathlib import Path

from audit_intake import (
    AXIS_REQUIRED_BY_STAGE,
    PROCESS_REQUIRED,
    REQUIRED_BY_STAGE,
    STAGES,
    audit,
    get_path,
    is_filled,
    selected_processes,
)


SKILL_ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = SKILL_ROOT / "assets" / "machine-design-input.json"


def set_path(data: dict, path: str, value) -> None:
    target = data
    keys = path.split(".")
    for key in keys[:-1]:
        target = target.setdefault(key, {})
    target[keys[-1]] = value


def sample_for(existing):
    if isinstance(existing, list):
        return ["sample"]
    if isinstance(existing, dict):
        return {"sample": "value"}
    if isinstance(existing, bool):
        return True
    if isinstance(existing, (int, float)):
        return 1
    return "sample"


def filled_through(stage: str, process: str = "plasma") -> dict:
    data = json.loads(TEMPLATE.read_text(encoding="utf-8"))
    target_index = STAGES.index(stage)
    for candidate in STAGES[: target_index + 1]:
        for path in REQUIRED_BY_STAGE.get(candidate, ()):
            existing = get_path(data, path)
            set_path(data, path, sample_for(existing))

    data["design_stage"] = stage
    data["process"]["machine_types"] = [process]
    data["scope"]["authority_having_jurisdiction"] = "sample authority"
    data["compliance"]["primary_source_evidence"] = ["official source"]

    if target_index >= STAGES.index("concept"):
        data["requirements"] = [
            {"id": "REQ-001", "statement": "sample requirement", "verification": "sample test"}
        ]
        axis = data["axes"][0]
        for candidate in STAGES[1 : target_index + 1]:
            for path in AXIS_REQUIRED_BY_STAGE.get(candidate, ()):
                existing = get_path(axis, path)
                set_path(axis, path, sample_for(existing))

    branch = data["process_specific"][process]
    branch["applicable"] = True
    for candidate in STAGES[1 : target_index + 1]:
        for field in PROCESS_REQUIRED[process].get(candidate, ()):
            branch[field] = "sample"
    return data


class AuditIntakeTests(unittest.TestCase):
    def test_placeholder_semantics(self) -> None:
        self.assertFalse(is_filled(None))
        self.assertFalse(is_filled("TBD"))
        self.assertFalse(is_filled("N/A"))
        self.assertTrue(is_filled("N/A - no fluid system"))
        self.assertTrue(is_filled(0))
        self.assertTrue(is_filled(False))

    def test_blank_template_reports_discovery_gaps(self) -> None:
        data = json.loads(TEMPLATE.read_text(encoding="utf-8"))
        errors, _ = audit(data, "discovery")
        self.assertGreater(len(errors), 20)
        self.assertTrue(any("project.name" in error for error in errors))

    def test_complete_discovery_has_no_gaps(self) -> None:
        errors, warnings = audit(filled_through("discovery"), "discovery")
        self.assertEqual(errors, [])
        self.assertEqual(warnings, [])

    def test_selected_process_requires_matching_branch(self) -> None:
        data = filled_through("concept", "plasma")
        data["process_specific"]["plasma"]["applicable"] = False
        errors, _ = audit(data, "concept")
        self.assertTrue(any("process_specific.plasma.applicable" in error for error in errors))

    def test_vertical_axis_requires_retention_at_preliminary(self) -> None:
        data = filled_through("preliminary", "plasma")
        data["axes"][0]["orientation"] = "vertical Z"
        data["axes"][0]["brake_or_counterbalance"] = None
        errors, _ = audit(data, "preliminary")
        self.assertTrue(any("brake_or_counterbalance" in error for error in errors))

    def test_duplicate_requirement_ids_are_rejected(self) -> None:
        data = filled_through("concept", "plasma")
        duplicate = copy.deepcopy(data["requirements"][0])
        data["requirements"].append(duplicate)
        errors, _ = audit(data, "concept")
        self.assertTrue(any("duplicate 'REQ-001'" in error for error in errors))

    def test_every_supported_process_can_close_release_coverage(self) -> None:
        for process in (
            "spindle",
            "plasma",
            "laser",
            "waterjet",
            "water_jet_guided_laser",
            "additive",
            "robot",
            "metrology",
            "hybrid",
        ):
            with self.subTest(process=process):
                errors, warnings = audit(filled_through("release", process), "release")
                self.assertEqual(errors, [])
                self.assertEqual(warnings, [])

    def test_every_questionnaire_machine_family_routes_to_a_branch(self) -> None:
        expected = {
            "router": "spindle",
            "mill": "spindle",
            "plasma": "plasma",
            "fiber laser": "laser",
            "abrasive waterjet": "waterjet",
            "water-jet-guided laser": "water_jet_guided_laser",
            "additive": "additive",
            "pick and place": "robot",
            "robotic arm": "robot",
            "inspection": "metrology",
            "hybrid": "hybrid",
        }
        for machine_type, branch in expected.items():
            with self.subTest(machine_type=machine_type):
                data = {"process": {"machine_types": [machine_type]}}
                self.assertEqual(selected_processes(data), {branch})

    def test_template_contains_every_audited_process_branch(self) -> None:
        data = json.loads(TEMPLATE.read_text(encoding="utf-8"))
        self.assertTrue(set(PROCESS_REQUIRED).issubset(data["process_specific"]))


if __name__ == "__main__":
    unittest.main()

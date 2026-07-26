#!/usr/bin/env python3
"""Audit a CNC machine design intake for stage and process coverage.

This is a coverage checker, not an engineering approval or safety validator.
It intentionally uses only the Python standard library.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


STAGES = ("discovery", "concept", "preliminary", "detailed", "release")

REQUIRED_BY_STAGE: dict[str, tuple[str, ...]] = {
    "discovery": (
        "questionnaire_version",
        "design_stage",
        "project.name",
        "project.owner",
        "project.technical_authority",
        "project.safety_authority",
        "scope.problem_statement",
        "scope.intended_use",
        "scope.exclusions",
        "scope.users",
        "scope.success_measures",
        "scope.jurisdictions",
        "scope.installation_location",
        "process.machine_types",
        "process.primary_process",
        "process.materials",
        "parts.maximum_dimensions.x",
        "parts.maximum_dimensions.y",
        "parts.maximum_dimensions.z",
        "parts.maximum_dimensions.unit",
        "parts.maximum_mass.value",
        "parts.maximum_mass.unit",
        "envelope.description",
        "throughput.target_parts_per_hour",
        "duty.operating_schedule",
        "performance.positioning_accuracy",
        "performance.bidirectional_repeatability",
        "performance.tool_to_work_deflection_limit",
        "performance.maximum_velocity_by_axis",
        "electrical.available_power.voltage",
        "electrical.available_power.phase",
        "facility.ambient_and_environment",
        "commercial.capital_ceiling",
        "commercial.milestones",
    ),
    "concept": (
        "requirements",
        "architecture.alternatives",
        "architecture.selected",
        "architecture.selection_rationale",
        "architecture.kinematics",
        "architecture.force_loop",
        "structure.materials",
        "structure.datum_hierarchy",
        "process_head.type",
        "controls.controller_class",
        "controls.feedback_architecture",
        "safety.hazard_analysis_method",
        "safety.hazard_log_reference",
        "safety.risk_acceptance_authority",
        "compliance.applicability_matrix_reference",
        "facility.floor_foundation_and_anchors",
        "manufacturing.make_buy_strategy",
        "verification.verification_matrix_reference",
    ),
    "preliminary": (
        "load_cases",
        "structure.error_budget_reference",
        "structure.stress_calculation_reference",
        "structure.deflection_calculation_reference",
        "structure.modal_analysis_reference",
        "structure.thermal_analysis_reference",
        "process_head.process_window_reference",
        "electrical.load_list_reference",
        "electrical.single_line_reference",
        "electrical.protection_and_sccr_reference",
        "electrical.power_supply_and_regeneration_reference",
        "electrical.enclosure_thermal_reference",
        "electrical.grounding_shielding_emc_reference",
        "controls.real_time_requirements",
        "controls.trajectory_and_interpolation",
        "controls.state_machine_reference",
        "controls.fault_response_reference",
        "safety.guarding_reference",
        "safety.safety_functions_reference",
        "safety.stop_time_and_distance_reference",
        "safety.energy_isolation_reference",
        "facility.utility_failure_safe_states",
        "manufacturing.datum_and_tolerance_stack_reference",
        "verification.metrology_and_uncertainty_reference",
        "reliability_and_maintenance.reliability_target",
        "reliability_and_maintenance.component_life_reference",
        "commercial.target_cost",
        "documentation.calculation_ledger_reference",
    ),
    "detailed": (
        "structure.fabrication_and_alignment_plan",
        "process_head.model",
        "process_head.qualification_plan",
        "electrical.schematics_reference",
        "electrical.io_schedule_reference",
        "controls.controller_model",
        "controls.software_repository",
        "controls.software_test_reference",
        "controls.configuration_and_release_method",
        "controls.backup_and_restore_method",
        "safety.fire_and_emergency_reference",
        "safety.safety_validation_reference",
        "compliance.edition_and_date_verified",
        "compliance.primary_source_evidence",
        "manufacturing.assembly_plan_reference",
        "manufacturing.alignment_plan_reference",
        "manufacturing.lifting_shipping_installation_reference",
        "commercial.bom_reference",
        "documentation.drawings_reference",
        "documentation.electrical_documentation_reference",
        "documentation.software_configuration_reference",
        "documentation.manufacturing_and_assembly_reference",
        "reliability_and_maintenance.lubrication_plan_reference",
        "reliability_and_maintenance.preventive_maintenance_reference",
        "reliability_and_maintenance.spares_and_obsolescence_reference",
    ),
    "release": (
        "verification.requirements_traceability_reference",
        "verification.factory_acceptance_reference",
        "verification.site_acceptance_reference",
        "verification.commissioning_reference",
        "verification.process_capability_reference",
        "verification.test_evidence",
        "verification.release_approval",
        "documentation.operation_manual_reference",
        "documentation.maintenance_manual_reference",
        "documentation.training_reference",
        "documentation.as_built_dossier_reference",
        "manufacturing.as_built_capture_method",
        "approvals.safety_validation",
        "approvals.release",
    ),
}

AXIS_REQUIRED_BY_STAGE: dict[str, tuple[str, ...]] = {
    "concept": ("name", "type", "orientation", "travel.value", "travel.unit"),
    "preliminary": (
        "moving_mass.value",
        "moving_mass.unit",
        "maximum_process_force.value",
        "maximum_process_force.unit",
        "maximum_velocity.value",
        "maximum_acceleration.value",
        "maximum_jerk.value",
        "guide.type",
        "transmission.type",
        "motor.type",
        "calculations_reference",
    ),
    "detailed": (
        "guide.model",
        "guide.rating_and_life_reference",
        "transmission.model",
        "transmission.sizing_reference",
        "motor.model",
        "motor.sizing_reference",
        "drive.model",
        "drive.control_mode",
        "feedback.type",
        "home_limits_stops_and_recovery",
        "verification_reference",
    ),
}

PROCESS_ALIASES = {
    "spindle": "spindle",
    "router": "spindle",
    "mill": "spindle",
    "milling": "spindle",
    "plasma": "plasma",
    "laser": "laser",
    "fiber_laser": "laser",
    "fiber laser": "laser",
    "waterjet": "waterjet",
    "water jet": "waterjet",
    "abrasive_waterjet": "waterjet",
    "abrasive waterjet": "waterjet",
    "water_jet_guided_laser": "water_jet_guided_laser",
    "water jet guided laser": "water_jet_guided_laser",
    "wjgl": "water_jet_guided_laser",
    "additive": "additive",
    "fdm": "additive",
    "3d_printing": "additive",
    "3d printing": "additive",
    "robot": "robot",
    "robotic_arm": "robot",
    "robotic arm": "robot",
    "pick_and_place": "robot",
    "pick and place": "robot",
    "inspection": "metrology",
    "metrology": "metrology",
    "measurement": "metrology",
    "cmm": "metrology",
    "hybrid": "hybrid",
}

PROCESS_REQUIRED: dict[str, dict[str, tuple[str, ...]]] = {
    "spindle": {
        "concept": ("material_and_tool_range",),
        "preliminary": ("power_torque_speed_envelope", "tool_interface_and_runout"),
        "detailed": ("spindle_model", "vfd_braking_and_cooling", "chip_dust_coolant_and_fire_controls"),
        "release": ("cutting_force_chatter_and_qualification_reference",),
    },
    "plasma": {
        "concept": ("material_thickness_window",),
        "preliminary": ("source_torch_current_and_duty", "gas_pressure_flow_and_purity", "height_control_and_arc_voltage"),
        "detailed": ("work_lead_hf_start_and_emc_controls", "table_fume_dross_and_fire_controls"),
        "release": ("qualification_reference",),
    },
    "laser": {
        "concept": ("material_thickness_reflectivity_window",),
        "preliminary": ("source_wavelength_power_and_beam_quality", "optics_focus_head_and_height_control", "assist_gas_pressure_flow_and_purity"),
        "detailed": ("cooling_fume_and_fire_controls", "laser_class_enclosure_interlocks_and_validation"),
        "release": ("qualification_reference",),
    },
    "waterjet": {
        "concept": ("material_thickness_window",),
        "preliminary": ("pressure_flow_pump_and_power", "orifice_mixing_tube_and_abrasive"),
        "detailed": ("high_pressure_plumbing_restraint_and_release", "water_chiller_catcher_sludge_and_wastewater", "noise_kerf_taper_and_maintenance"),
        "release": ("qualification_reference",),
    },
    "water_jet_guided_laser": {
        "concept": ("material_thickness_reflectivity_window",),
        "preliminary": (
            "laser_source_wavelength_power_and_beam_quality",
            "water_pressure_flow_quality_and_temperature",
            "optical_coupling_nozzle_orifice_and_jet_stability",
            "focus_standoff_and_height_control",
        ),
        "detailed": (
            "high_pressure_plumbing_restraint_and_release",
            "cooling_enclosure_interlocks_fume_and_wastewater",
            "combined_laser_pressure_hazard_validation",
        ),
        "release": ("qualification_reference",),
    },
    "additive": {
        "concept": ("feedstock_and_handling",),
        "preliminary": ("extruder_nozzle_flow_and_force", "heater_bed_chamber_and_runaway_protection", "layer_bead_shrinkage_and_cooling"),
        "detailed": ("slicing_and_motion_flow_synchronization",),
        "release": ("ventilation_fire_and_qualification_reference",),
    },
    "robot": {
        "concept": ("payload_inertia_reach_dof_and_singularities",),
        "preliminary": ("cycle_repeatability_joints_and_drives", "end_effector_grip_vacuum_and_retention", "vision_lighting_and_calibration"),
        "detailed": ("conveyors_fixtures_tracking_and_collision", "safeguarded_space_collaboration_and_recovery"),
        "release": ("qualification_reference",),
    },
    "metrology": {
        "concept": ("measurands_feature_material_and_volume", "accuracy_uncertainty_and_ratio_policy"),
        "preliminary": (
            "sensor_probe_scanner_and_probing_force",
            "kinematics_fixture_datums_and_sampling_path",
            "environment_vibration_and_thermal_control",
        ),
        "detailed": (
            "calibration_artifacts_and_traceability_chain",
            "data_processing_and_uncertainty_budget_reference",
        ),
        "release": ("verification_and_requalification_reference",),
    },
    "hybrid": {
        "concept": (
            "constituent_processes_and_branch_references",
            "shared_structure_axes_workholding_and_utilities",
        ),
        "preliminary": ("interface_loads_and_incompatible_media",),
        "detailed": (
            "changeover_cleaning_and_mode_enforcement",
            "combined_energy_hazard_and_collision_analysis",
        ),
        "release": ("individual_and_combined_mode_qualification_reference",),
    },
}


def get_path(data: Any, path: str) -> Any:
    value = data
    for key in path.split("."):
        if not isinstance(value, dict) or key not in value:
            return None
        value = value[key]
    return value


def is_filled(value: Any) -> bool:
    if value is None:
        return False
    if isinstance(value, str):
        normalized = value.strip()
        if not normalized:
            return False
        upper = normalized.upper()
        if upper in {"TBD", "TODO", "UNKNOWN", "N/A", "NA"}:
            return False
        return True
    if isinstance(value, (list, dict)):
        return len(value) > 0
    return True


def cumulative_stage_items(mapping: dict[str, tuple[str, ...]], stage: str) -> list[tuple[str, str]]:
    items: list[tuple[str, str]] = []
    target_index = STAGES.index(stage)
    for candidate in STAGES[: target_index + 1]:
        for item in mapping.get(candidate, ()):
            items.append((candidate, item))
    return items


def selected_processes(data: dict[str, Any]) -> set[str]:
    raw = get_path(data, "process.machine_types")
    if not isinstance(raw, list):
        return set()
    selected: set[str] = set()
    for value in raw:
        if isinstance(value, str):
            key = value.strip().lower().replace("-", "_")
            branch = PROCESS_ALIASES.get(key) or PROCESS_ALIASES.get(key.replace("_", " "))
            if branch:
                selected.add(branch)
    return selected


def audit(data: dict[str, Any], stage: str) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    target_index = STAGES.index(stage)

    declared_stage = data.get("design_stage")
    if declared_stage not in STAGES:
        errors.append(f"design_stage: expected one of {', '.join(STAGES)}")
    elif STAGES.index(declared_stage) < STAGES.index(stage):
        warnings.append(f"design_stage declares {declared_stage!r}, but audit target is {stage!r}")

    for introduced_at, path in cumulative_stage_items(REQUIRED_BY_STAGE, stage):
        if not is_filled(get_path(data, path)):
            errors.append(f"[{introduced_at}] {path}: missing, empty, or unresolved")

    if STAGES.index(stage) >= STAGES.index("concept"):
        axes = data.get("axes")
        if not isinstance(axes, list) or not axes:
            errors.append("[concept] axes: add at least one axis object")
        else:
            for index, axis in enumerate(axes):
                if not isinstance(axis, dict):
                    errors.append(f"axes[{index}]: expected an object")
                    continue
                for introduced_at, path in cumulative_stage_items(AXIS_REQUIRED_BY_STAGE, stage):
                    if not is_filled(get_path(axis, path)):
                        errors.append(f"[{introduced_at}] axes[{index}].{path}: missing, empty, or unresolved")
                orientation = str(axis.get("orientation") or "").lower()
                gravity_axis = (
                    "vertical" in orientation
                    or "gravity" in orientation
                    or orientation.strip() in {"z", "z-axis", "z axis"}
                    or orientation.strip().startswith("z ")
                )
                if target_index >= STAGES.index("preliminary") and gravity_axis:
                    if not is_filled(axis.get("brake_or_counterbalance")):
                        errors.append(
                            f"[preliminary] axes[{index}].brake_or_counterbalance: gravity-axis retention not resolved"
                        )

    processes = selected_processes(data)
    raw_types = get_path(data, "process.machine_types")
    if isinstance(raw_types, list) and raw_types and not processes:
        warnings.append(
            "process.machine_types contains no recognized process alias; add the branch manually and extend the audit for novel processes"
        )

    for process in sorted(processes):
        branch = get_path(data, f"process_specific.{process}")
        if not isinstance(branch, dict):
            errors.append(f"process_specific.{process}: missing branch object")
            continue
        if branch.get("applicable") is not True:
            errors.append(f"process_specific.{process}.applicable: set true for selected process")
        for candidate in STAGES[1 : target_index + 1]:
            for field in PROCESS_REQUIRED[process].get(candidate, ()):
                if not is_filled(branch.get(field)):
                    errors.append(f"[{candidate}] process_specific.{process}.{field}: missing, empty, or unresolved")

    requirements = data.get("requirements")
    if isinstance(requirements, list):
        seen_ids: set[str] = set()
        for index, requirement in enumerate(requirements):
            if not isinstance(requirement, dict):
                errors.append(f"requirements[{index}]: expected an object with id, statement, and verification")
                continue
            for field in ("id", "statement", "verification"):
                if not is_filled(requirement.get(field)):
                    errors.append(f"requirements[{index}].{field}: missing")
            requirement_id = requirement.get("id")
            if isinstance(requirement_id, str):
                if requirement_id in seen_ids:
                    errors.append(f"requirements[{index}].id: duplicate {requirement_id!r}")
                seen_ids.add(requirement_id)

    if not is_filled(get_path(data, "scope.authority_having_jurisdiction")):
        warnings.append("scope.authority_having_jurisdiction is unresolved; confirm before detailed design")
    if not is_filled(get_path(data, "compliance.primary_source_evidence")):
        warnings.append("no primary-source compliance evidence recorded; course references are not release authority")
    if get_path(data, "network_and_data.applicable") is True and not is_filled(
        get_path(data, "network_and_data.threat_model_reference")
    ):
        warnings.append("network/data is applicable but no cybersecurity threat model is recorded")

    return errors, warnings


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Audit CNC machine design questionnaire coverage. A clean result is not engineering approval."
    )
    parser.add_argument("input", type=Path, help="filled machine-design-input.json")
    parser.add_argument("--stage", choices=STAGES, help="target gate; defaults to design_stage in the file")
    parser.add_argument("--strict", action="store_true", help="return failure when warnings remain")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        data = json.loads(args.input.read_text(encoding="utf-8"))
    except FileNotFoundError:
        print(f"ERROR: input not found: {args.input}", file=sys.stderr)
        return 2
    except (OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: cannot read valid JSON from {args.input}: {exc}", file=sys.stderr)
        return 2

    if not isinstance(data, dict):
        print("ERROR: questionnaire root must be a JSON object", file=sys.stderr)
        return 2

    stage = args.stage or data.get("design_stage")
    if stage not in STAGES:
        print(f"ERROR: select --stage from {', '.join(STAGES)}", file=sys.stderr)
        return 2

    errors, warnings = audit(data, stage)

    print(f"CNC machine design intake audit: {args.input}")
    print(f"Target stage: {stage}")
    print("Coverage only: this result is not design, safety, or compliance approval.")
    if errors:
        print(f"\nMissing or unresolved ({len(errors)}):")
        for message in errors:
            print(f"- ERROR {message}")
    if warnings:
        print(f"\nWarnings ({len(warnings)}):")
        for message in warnings:
            print(f"- WARNING {message}")
    if not errors and not warnings:
        print("\nNo stage-gated coverage gaps detected.")
    else:
        print(f"\nSummary: {len(errors)} error(s), {len(warnings)} warning(s)")

    if errors or (args.strict and warnings):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

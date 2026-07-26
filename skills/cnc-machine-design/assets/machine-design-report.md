# Machine design package

**Machine:** [name / identifier]

**Revision:** [revision]

**Design stage:** [stage]

**Owner:** [owner]

**Technical authority:** [name]

**Safety authority:** [name]

**Date:** [date]

## 1. Executive design decision

- Intended use:
- Selected architecture:
- Governing performance requirements:
- Governing load cases:
- Safety/compliance position:
- Cost and schedule position:
- Release status:
- Top unresolved risks:

## 2. Scope and governance

### Included

[Scope]

### Excluded

[Exclusions]

### Stakeholders, users, and approvals

[Roles]

### Jurisdiction and authority

[Installation location, authority having jurisdiction, sale territory, certification path]

## 3. Requirements baseline

| ID | Requirement | Value/range and units | Condition | Source | Verification | Status |
|---|---|---|---|---|---|---|
| REQ-001 | | | | | | |

## 4. Assumption and unknown register

| ID | Assumption / unknown | Bounds | Impact if wrong | Owner | Closure evidence | Status |
|---|---|---|---|---|---|---|
| ASM-001 | | | | | | |

## 5. Architecture and trade study

### Alternatives

| Criterion | Weight/rationale | Concept A | Concept B | Concept C |
|---|---|---|---|---|
| | | | | |

### Selected architecture

[Kinematics, axis stack, moving members, process-force loop, foundation, workholding, process head, utilities, control and safety boundaries]

### Rejected alternatives

[Reason each was rejected and what evidence could reopen it]

## 6. Interfaces and coordinate definition

| Interface ID | From | To | Mechanical | Electrical | Fluid/data | Datum/protocol | Owner |
|---|---|---|---|---|---|---|---|
| IF-001 | | | | | | | |

[Coordinate systems, origins, axis signs, work/tool offsets and transformations]

## 7. Load cases and engineering budgets

| Load case | Description | Forces/moments/energy | Combination | Duration/cycles | Requirement |
|---|---|---|---|---|---|
| LC-001 | | | | | |

| Budget | System limit | Allocation | Combination rule | Integration margin | Status |
|---|---|---|---|---|---|
| Accuracy | | | | | |
| Deflection | | | | | |
| Thermal drift | | | | | |
| Cycle time | | | | | |
| Power/heat | | | | | |
| Cost | | | | | |

## 8. Calculation ledger

| ID | Requirement | Load case | Model/source | Inputs and units | Result | Allowable | Margin | Verification |
|---|---|---|---|---|---|---|---|---|
| CALC-001 | | | | | | | | |

### Structural and thermal

[Stress, deflection, buckling, fatigue, joints, modes, heat, drift, foundation and transport]

### Guidance, transmission and actuation

[Rail/bearing loads and life, screw/rack/belt checks, motor/drive torque-speed-duty, inertia, regeneration, brakes and hard stops]

### Process subsystem

[Process-specific sizing and qualification]

### Electrical and enclosure

[Load list, protection/SCCR, conductors, DC bus/regeneration, grounding/EMC, enclosure heat and utilities]

### Controls and motion

[Rates, latency, feedback, trajectory, tuning/stability, errors, state machine, faults and recovery]

## 9. Mechanical design specification

[Frame, gantry, Z/axes, guides, transmissions, actuators, process head, workholding, material handling, guarding, extraction, cooling, lubrication, service and transport]

## 10. Electrical design specification

[Power, disconnect/protection, supplies, drives, panel/enclosure, conductors/cables, grounding/bonding/shielding, connectors, I/O, safety circuits and documentation]

## 11. Controls, software, and data specification

[Controller, feedback, real-time behavior, motion profiles, modes, state machine, HMI, faults, network, cybersecurity, configuration, test, release, backup and recovery]

## 12. Process specification

[Materials/parts, tooling/consumables, media/utilities, parameter window, quality outputs, waste/emissions and qualification]

## 13. Safety and compliance

### Applicability matrix

| ID | Regulation/code/standard/customer rule | Jurisdiction | Edition/date | Applicable clauses/subject | Primary source | Evidence | Owner |
|---|---|---|---|---|---|---|---|
| STD-001 | | | | | | | |

### Hazard and risk-reduction log

| Hazard ID | Lifecycle task | Initiating event and harm | Initial risk | Inherent measure | Guard/control | Information/PPE | Residual risk | Verification |
|---|---|---|---|---|---|---|---|---|
| HAZ-001 | | | | | | | | |

### Safety functions

| SF ID | Hazard controlled | Trigger | Safe state | Required performance | Architecture | Fault response | Validation evidence |
|---|---|---|---|---|---|---|---|
| SF-001 | | | | | | | |

### Stored-energy isolation

[Electrical, gravitational, kinetic, pneumatic, hydraulic, vacuum, pressure, thermal, spring, capacitor and software-controlled energy]

### Residual risks

[Labels, manuals, training, PPE, access restrictions and owner acceptance]

## 14. Facility and utility specification

[Foundation/floor, installation path, lifting, electrical, air, water, drain, gas, extraction, HVAC, network, environmental conditions and utility failure]

## 15. BOM and sourcing

| Item | Manufacturer / part number | Qty | Critical ratings | Approved source | Alternate | Lead time | Lifecycle | Cost | Risk |
|---|---|---:|---|---|---|---|---|---:|---|
| | | | | | | | | | |

## 16. Manufacturing, assembly, and installation

[Make/buy, special processes, datum/tolerance strategy, weld-machine-coat sequence, assembly, inspection, alignment, wiring/piping, software load, shipping, installation and as-built capture]

## 17. Verification and acceptance matrix

| Verification ID | Requirement(s) | Method | Setup/instrument/uncertainty | Conditions/sample | Acceptance criterion | Evidence | Status |
|---|---|---|---|---|---|---|---|
| VER-001 | | | | | | | |

[Factory acceptance, site acceptance, commissioning, process capability and requalification triggers]

## 18. Reliability, maintenance, and lifecycle

[Targets, failure modes, diagnostics, component life, lubrication, preventive/predictive maintenance, spares, obsolescence, cleaning, software updates and decommissioning]

## 19. Cost and schedule

| Cost category | Estimate | Basis | Confidence | Contingency | Owner |
|---|---:|---|---|---:|---|
| | | | | | |

| Milestone | Entry criteria | Exit evidence | Planned date | Owner | Status |
|---|---|---|---|---|---|
| | | | | | |

## 20. Open issues, deviations, and release decision

| ID | Type | Description | Impact | Compensating control | Owner | Due/review | Closure evidence | Status |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |

### Approval

- Technical approval:
- Safety validation approval:
- Quality/acceptance approval:
- Operations/maintenance acceptance:
- Release authority and date:
- Configuration baseline:

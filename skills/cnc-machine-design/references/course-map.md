# Course routing map

Use this map to search the course selectively. Resolve paths from the course repository root. Prefer numbered and `section-*` lesson files; ignore `module-*master-outline.md`, compiled alternate drafts, generated website copies, and PDFs unless visual layout is specifically needed.

## Contents

- Core design sequence
- Process branches
- Production and lifecycle branches
- Appendices
- Search protocol

## Core design sequence

| Design concern | Primary source | Typical searches |
|---|---|---|
| Requirements, structural philosophy, load paths, datums, stiffness, thermal behavior, welding, materials | `Module-01-Mechanical-Frame-and-Structure/` | `deflection`, `load case`, `stiffness`, `datum`, `thermal`, `weld`, `natural frequency` |
| Vertical and gravity axes, Z-stage architecture, counterbalance, alignment, spindle mounting, cable management | `Module-02-Vertical-Axis-and-Z-Stage/` | `gravity`, `counterbalance`, `brake`, `Z-axis`, `vertical`, `alignment` |
| Rails, bearings, ball screws, lead screws, rack and pinion, belts, preload, life, lubrication | `Module-03-Linear-Motion-Systems/` | `L10`, `preload`, `critical speed`, `buckling`, `rack`, `belt`, `linear guide` |
| Controllers, drives, power supplies, I/O, interlocks, wiring, shielding, enclosures, commissioning | `Module-04-Control-Electronics/` | `load`, `drive`, `power supply`, `interlock`, `wire`, `shield`, `ground`, `enclosure` |
| EMI/EMC mechanisms, cable/shield/filter/grounding design, testing and standards | `Module-13-EMI-EMC-for-Motion-Control/` | `common mode`, `shield`, `filter`, `ground`, `emissions`, `immunity`, `standard` |
| LinuxCNC HAL, real-time control, I/O, custom components, Mesa hardware and diagnostics | `Module-14-LinuxCNC-HAL-and-Real-Time-Control/` | `HAL`, `real-time`, `latency`, `Mesa`, `thread`, `fault` |
| G-code, coordinate systems, motion commands, canned cycles, post-processing, dialects and simulation | `Module-15-G-Code-Standards-and-Post-Processing/` | `coordinate`, `G-code`, `post`, `simulation`, `dialect` |
| CAD, DFM, GD&T, drawings, assembly and process-specific design | `Module-16-CAD-Design-for-Manufacturable-Parts/` | `GD&T`, `tolerance`, `drawing`, `DFM`, `assembly`, `documentation` |
| Composites, ceramics, difficult materials, dust and surface finishing | `Module-17-Advanced-Materials-Composites-and-Ceramics/` | `composite`, `ceramic`, `dust`, `fracture`, `finish` |
| Sensors, data acquisition, networking, digital twins, MES and cybersecurity | `Module-18-Industry-4-0-for-CNC-Manufacturing/` | `sensor`, `protocol`, `network`, `cybersecurity`, `MES`, `digital twin` |
| PID, trajectory planning, motion profiles, multi-axis coordination, look-ahead and troubleshooting | `Module-19-Advanced-Control-Systems/` | `PID`, `trajectory`, `jerk`, `look-ahead`, `following error`, `tuning` |
| Cutting mechanics, speed, feed, engagement, tool materials, coolant and chip management | `Module-20-Feeds-and-Speeds/` | `chip load`, `surface speed`, `feed`, `depth`, `coolant`, `tool life` |
| Metrology, GD&T, CMM, probes, roughness, capability and machine-tool testing | `Module-21-Metrology-and-Precision-Measurement/` | `uncertainty`, `repeatability`, `Cpk`, `ISO 230`, `roughness`, `inspection` |

## Process branches

Read only the branches matching the intended machine or credible alternatives.

| Machine/process | Source | Coverage |
|---|---|---|
| Plasma cutting | `Module-05-Plasma-Cutting/` | Torch and power system, consumables, fume/dross, THC, workflow, cut quality and safety |
| Spindle/router/mill | `Module-06-Spindle-and-Rotary-Tools/` | Spindle and motor selection, cooling, VFD, tooling, bearings, runout, chip/dust control and interlocks |
| Fiber laser | `Module-07-Fiber-Laser/` | Source, optics, beam delivery, cutting head, assist gas, material handling, parameters and laser safety |
| Abrasive waterjet | `Module-08-Waterjet-Cutting/` | Pump, cutting head, abrasive delivery, fluid mechanics, catcher/table, safety and process optimization |
| Pick and place | `Module-09-Pick-and-Place-Robot/` | Architecture, end effectors, vision, motion control, programming, integration and safeguarding |
| Robotic arm/cell | `Module-10-Robotic-Arm/` | Kinematics, joints, end effectors, planning, force control, workcell integration and safety |
| Large-format FDM | `Module-11-Large-Format-FDM-3D-Printing/` | Gantry, extruder, heated bed, materials, thermal management, slicing and print quality |
| Water-jet-guided laser | `Module-12-Water-Jet-Guided-Laser-Cutting/` | Optical/fluid principles, nozzle, architecture, parameters, integration, safety and applications |
| Inspection/metrology machine | `Module-21-Metrology-and-Precision-Measurement/` | Measurement architecture, probes/scanners, uncertainty, environmental control, calibration, traceability and acceptance |
| Hybrid machine | Every applicable process module plus Modules 01-04, 13, 16, 19 and 21 | Shared structure/axes/utilities, mode control, incompatible media, combined hazards and cross-process qualification |

## Production and lifecycle branches

| Concern | Source |
|---|---|
| Quality system, process maps, suppliers, inspection, nonconformance, root cause and audits | `Module-22-Quality-Management-Systems-QMS/` |
| Facility layout, storage, maintenance, environmental control and shop management | `Module-23-Shop-Organization-and-Management/` |
| Value stream, setup reduction, TPM, cellular design, error proofing, standardized work and metrics | `Module-24-LEAN-Strategies-for-CNC-Manufacturing/` |
| Ergonomics, fatigue, shift work and human sustainability | `Module-25-Work-Life-Balance-in-CNC-Manufacturing/` |
| Business planning, capital, equipment, facility, suppliers, staffing, risk, scaling and case studies | `Module-26-CNC-Business-Ownership-and-Management/` |

## Appendices

| Appendix | Use |
|---|---|
| `Appendices/appendix-A-material-properties.md` | Material property screening; verify final values against controlled supplier data |
| `Appendices/appendix-B-hardware-specifications.md` | Hardware selection prompts and typical specifications |
| `Appendices/appendix-C-motor-drive-sizing.md` | Motor, drive, torque, speed, inertia and regeneration sizing |
| `Appendices/appendix-D-linear-motion.md` | Linear motion selection and sizing |
| `Appendices/appendix-E-electrical-standards.md` | Electrical standards orientation; verify current adopted editions and jurisdiction |
| `Appendices/appendix-F-gcode-reference.md` | Programming reference |
| `Appendices/appendix-G-safety-standards.md` | Safety standards orientation; verify current applicability and editions |
| `Appendices/appendix-H-lubrication.md` | Lubricant selection and intervals |
| `Appendices/appendix-I-conversions.md` | Unit conversions |
| `Appendices/appendix-J-troubleshooting.md` | Failure modes and diagnostic paths |
| `Appendices/appendix-K-vendors.md` | Sourcing leads; verify current vendors and products |
| `Appendices/appendix-L-resources.md` | Further primary and secondary sources |
| `Appendices/appendix-M-glossary.md` | Terminology normalization |
| `Appendices/appendix-P-mathematics.md` | Mathematical methods and engineering formulas |
| `Appendices/appendix-Q-qms-templates.md` | Quality records and templates |
| `Appendices/appendix-R-organization-templates.md` | Shop and organization templates |
| `Appendices/appendix-S-lean-templates.md` | Lean implementation templates |
| `Appendices/appendix-T-business-templates.md` | Business planning templates |

Appendices N and O are contact/update metadata, not engineering authority.

## Search protocol

1. Start with the design concern and the corresponding directory above.
2. List canonical lessons:

   ```bash
   rg --files <module-directory> -g '*.md' -g '!module-*'
   ```

3. Search narrowly:

   ```bash
   rg -n -i 'critical speed|buckling|reflected inertia' <module-directory> Appendices/
   ```

4. Read the complete surrounding section before using a formula or recommendation.
5. Record the exact source path and heading in the calculation or decision ledger.
6. Verify current codes, standards, regulations, and vendor ratings against primary official sources before release.

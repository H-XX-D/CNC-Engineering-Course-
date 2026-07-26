# Machine design parameter catalog

This catalog defines the minimum parameter families the skill must consider. It is deliberately extensible: a machine-specific hazard analysis, selected technology, authority having jurisdiction, vendor interface, or novel process can introduce additional parameters.

For every numeric parameter record: value, unit, tolerance/range, operating or worst-case condition, source, confidence, owner, requirement ID, and verification method. For every selection record: alternatives, decision criteria, rationale, interfaces, failure mode, and approval.

## Contents

1. Governance and scope
2. Product and process requirements
3. Parts, materials, and work envelope
4. Performance and duty cycle
5. Architecture and kinematics
6. Load cases and structural design
7. Guidance, transmission, and actuation
8. Process equipment
9. Electrical power and electronics
10. Controls, feedback, software, and data
11. Safety, compliance, and human factors
12. Utilities, environment, and facility
13. Manufacturing, assembly, and logistics
14. Metrology, verification, and commissioning
15. Reliability, maintenance, and lifecycle
16. Cost, schedule, sourcing, and documentation
17. Conditional process branches

## 1. Governance and scope

- Project name, machine identifier, revision, design stage, status, owner, technical authority, safety authority, reviewers, approvers, and change-control method.
- Problem statement, intended use, reasonably foreseeable misuse, users, stakeholders, success measures, exclusions, assumptions, constraints, dependencies, and fixed interfaces.
- New design, retrofit, copy, research prototype, production machine, commercial product, or one-off fixture.
- Design life in years, shifts, operating hours, cycles, starts, tool changes, maintenance access events, and expected relocation count.
- Confidentiality, export, intellectual-property, data-retention, and documentation obligations.
- Jurisdictions, installation location, sale/distribution territory, authority having jurisdiction, certification/listing expectations, customer standards, and contract hierarchy.

## 2. Product and process requirements

- Primary and secondary machine processes; process combinations and changeover requirements.
- Value proposition: prototype flexibility, production rate, accuracy, material range, unattended operation, portability, training, research, or cost.
- Input state, transformation, output state, acceptable defects, scrap handling, rework path, and traceability.
- Target parts per hour/shift, takt time, cycle time, setup time, changeover time, warm-up time, planned availability, and maximum recovery time.
- Operator skill assumptions, staffing, loading mode, supervision, remote access, and unattended-operation policy.
- Existing upstream/downstream equipment, line interfaces, data interfaces, material flow, and responsibility boundaries.

## 3. Parts, materials, and work envelope

- Minimum, typical, and maximum part dimensions; stock dimensions; nesting or batch arrangement; fixtures; pallets; and access clearance.
- Minimum, typical, and maximum part, stock, fixture, pallet, tool, cable carrier, and moving assembly mass.
- Material families, grades, hardness, thickness/diameter range, coatings, reflectivity, conductivity, flammability, toxicity, dust/fume behavior, moisture sensitivity, and temperature limits.
- Required axis travel, usable work envelope, overtravel, homing clearance, tool-change clearance, inspection clearance, service clearance, and guarding envelope.
- Coordinate system, origin strategy, datum scheme, work offsets, tool offsets, handedness, axis naming, rotary-axis conventions, and transformation requirements.
- Workholding method, clamping force, allowable distortion, datum repeatability, sensing, mistake proofing, chip/debris access, and quick-change needs.

## 4. Performance and duty cycle

- Positioning accuracy, bidirectional repeatability, resolution, minimum command increment, straightness, flatness, squareness, backlash, reversal error, following error, contour error, and drift.
- Surface finish, kerf/feature width, dimensional tolerance, geometric tolerance, edge quality, burr/dross, heat-affected zone, porosity, layer quality, placement accuracy, or other process outputs.
- Maximum and typical velocity, acceleration, deceleration, jerk, cornering behavior, settling time, move profile, synchronized-axis performance, and homing repeatability.
- Static stiffness at tool center point, allowable deflection by load case, dynamic compliance, minimum natural frequency, damping, chatter margin, and vibration limits.
- Thermal warm-up, ambient range, heat loads, gradient limits, allowable thermal drift, coolant stability, enclosure equilibrium, and compensation policy.
- Continuous/intermittent ratings, duty cycle by process state, peak duration, start-stop frequency, production schedule, maintenance windows, and degraded modes.
- Noise, vibration, heat, emissions, energy consumption, consumables, and environmental performance targets.

Do not accept one number labeled “precision.” Separate accuracy, repeatability, resolution, stability, uncertainty, and process capability.

## 5. Architecture and kinematics

- Machine archetype: fixed gantry, moving gantry, moving table, cantilever, bridge, Cartesian, CoreXY, delta, SCARA, articulated arm, parallel mechanism, rotary table, or hybrid.
- Number and type of controlled, coupled, slaved, redundant, and manual axes; degrees of freedom; singularities; and software kinematics.
- Moving members, load path to ground, Abbe offsets, force-loop length, center of mass, tipping/stability envelope, and foundation interface.
- Axis stacking order, travel direction, gravity direction, cable/hose motion, collision volumes, lost motion, and service positions.
- Modularity, scalability, transport splits, lifting points, leveling, anchoring, isolation, and expansion interfaces.
- Architecture alternatives, trade criteria, rejected concepts, and selection rationale.

## 6. Load cases and structural design

- Coordinate frame and sign convention for every load case.
- Static weights, payloads, clamping loads, cutting/process forces, drive forces, bearing reactions, cable/hose drag, vacuum loads, fluid pressure, magnetic forces, and operator/service loads.
- Dynamic acceleration, deceleration, jerk, impact, collision, emergency-stop, imbalance, rotating unbalance, cyclic, resonance, and transport loads.
- Abnormal loads: jam, tool crash, seized bearing, lost counterbalance, broken transmission, pressure loss, dropped part, thermal runaway, fire response, and single-fault safe state.
- Load combinations, probabilities, occurrence conditions, design allowables, factors of safety, fatigue cycles, stress concentrations, and acceptance criteria.
- Material specification, condition, anisotropy, modulus, yield/ultimate strength, fatigue properties, density, thermal expansion, conductivity, damping, corrosion, weldability, machinability, and data source.
- Beam/plate/shell geometry, section properties, joint stiffness, bolted/welded/bonded interfaces, contact/preload, foundation compliance, and modeled boundary conditions.
- Deflection and error budget allocation from frame, gantry, Z-axis, bearings, drive, spindle/head, fixture, workpiece, foundation, thermal effects, and metrology.
- Stress, fatigue, buckling, local crippling, bearing/contact stress, fastener, weld, adhesive, foundation, lifting, and transport checks.
- Modal targets, excitation frequencies, damping strategy, isolation, finite-element model assumptions, mesh convergence, correlation plan, and test points.
- Thermal sources, sinks, paths, gradients, time constants, expansion directions, symmetry, isolation, cooling, warm-up, sensors, and compensation.

## 7. Guidance, transmission, and actuation

For each axis record independently:

- Travel, orientation, moving mass, payload, center of mass, process load, friction, preload, external drag, speed, acceleration, jerk, duty, life, and contamination.
- Guide type, arrangement, rail size, carriage count, spacing, orientation, preload, static/dynamic capacity, moment capacity, life target, lubrication, sealing, mounting accuracy, and datum preparation.
- Transmission type: ball screw, lead screw, rack and pinion, belt, cable, linear motor, hydraulic/pneumatic cylinder, direct rotary, gearbox, or hybrid.
- Pitch/module, diameter, length, end support, reduction, efficiency, backlash, compliance, critical speed, buckling, tooth/belt load, tension, thermal growth, and lubrication.
- Motor type, torque-speed curve, continuous and peak torque, speed, inertia, thermal class, supply, feedback, brake, environmental rating, connector, and shaft load.
- Drive/amplifier voltage, current, peak duration, control mode, feedback compatibility, tuning range, regenerative energy handling, safe-torque-off capability, and fault outputs.
- Reflected inertia, inertia ratio policy, RMS torque, peak torque, speed margin, acceleration margin, thermal margin, regeneration, holding torque, and gravity-axis retention.
- Coupling, pulley, gearbox, pinion, bearing, shaft, key/spline/clamp, alignment, balance, guarding, and service life.
- Homing, limits, hard stops, overtravel energy absorption, absolute position retention, manual recovery, and brake/counterbalance behavior.

## 8. Process equipment

- Tool/process head type, operating envelope, rating, duty, interfaces, mass, center of gravity, reactions, accuracy/runout, consumables, failure modes, and replacement method.
- Tool/consumable range, holder, changer, magazine, offsets, life monitoring, breakage detection, presetting, and inventory.
- Process media: coolant, lubricant, assist gas, plasma gas, water, abrasive, resin, filament/pellet, adhesive, vacuum, air, hydraulic fluid, and extraction flow.
- Workholding, spoilboard/table, slats, catcher, bed, vacuum zones, fixtures, pallet systems, grounding/work lead, and sacrificial elements.
- Chip, dust, fume, mist, dross, abrasive, wastewater, scrap, heat, light, radiation, and noise capture or disposal.
- Process parameter window, recipe control, calibration, traceability, quality sensing, and acceptance coupon/artifact.

## 9. Electrical power and electronics

- Available utility voltage, phase, frequency, grounding system, capacity, source impedance, disconnect location, backup power, generator compatibility, and facility constraints.
- Complete load list with quantity, nominal/peak/inrush/regenerative power, power factor, harmonic behavior, duty, simultaneity, and safety criticality.
- Main disconnect, branch protection, overcurrent devices, contactors, transformers, power supplies, DC buses, braking resistors, energy storage, discharge time, and lockout points.
- Short-circuit current rating, interrupting ratings, coordination/selectivity, conductor ampacity, derating, voltage drop, insulation, bend radius, flex life, and fire rating.
- Enclosure material, dimensions, ingress/environmental rating, segregation, heat dissipation, cooling, condensation control, filtration, spacing, service clearances, and labeling.
- Protective bonding, grounding topology, shield termination, reference potentials, isolation, surge/transient protection, EMI filters, ferrites, cable separation, and routing.
- Connectors, pinouts, keying, current/voltage rating, mating cycles, strain relief, drag chain, flex cable, hose/cable grouping, and field replacement.
- I/O voltage levels, current budgets, sourcing/sinking, analog ranges, resolution, isolation, noise immunity, diagnostic coverage, and spare capacity.
- Electrical drawings, wire numbers, terminal plan, panel layout, cable schedule, labels, test points, and as-built update process.

## 10. Controls, feedback, software, and data

- Controller/platform, real-time requirements, cycle times, latency/jitter budgets, supported kinematics, axis count, I/O count, licensing, lifecycle, and recovery.
- Control mode per axis, command and feedback rates, trajectory planner, interpolation, look-ahead, motion limits, tuning method, filters, feedforward, and following-error limits.
- Encoder/resolver/scale type, location, resolution, accuracy, interpolation, index/absolute protocol, electrical interface, environmental rating, and diagnostic coverage.
- Open-loop versus closed-loop boundary, dual-loop behavior, backlash/thermal compensation, calibration maps, and error persistence.
- Machine state model, operating modes, permissions, startup, homing, reset, pause, resume, stop categories, safe state, fault latching, recovery, and manual/jog behavior.
- HMI users, controls, indicators, alarms, units, language, accessibility, recipe management, overrides, confirmation, and audit trail.
- PLC/HAL/firmware/software architecture, repositories, versions, configuration, coding standard, simulation, tests, release signing, rollback, backups, and obsolescence.
- Network interfaces, protocols, addressing, time synchronization, remote access, authentication, authorization, segmentation, logging, update policy, and cybersecurity threat model.
- Data ownership, retention, sampling, storage, privacy, cloud dependency, offline behavior, export, traceability, and disaster recovery.

## 11. Safety, compliance, and human factors

- Intended use and foreseeable misuse, lifecycle phases, exposed people, tasks, hazards, initiating events, harm severity, exposure, avoidance, and initial risk.
- Hierarchy of controls: inherent design, guards/protective devices, information/training, and personal protective equipment.
- Mechanical, electrical, thermal, pressure, vacuum, hydraulic, pneumatic, laser/radiation, plasma/arc, fire/explosion, chemical, dust/fume, noise, ergonomic, software, and cybersecurity hazards.
- Guard type, material, openings, reach distance, viewing needs, access frequency, interlocks, guard locking, defeat resistance, trapped-person escape, and validation.
- Emergency stops, protective stops, safe torque off, brake control, energy isolation, dissipation, restart prevention, reset location, and stop-time measurement.
- Safety-related control architecture, required performance/reliability target, diagnostics, fault exclusions, component data, proof-test interval, and validation plan.
- Lockout/tagout energy inventory: electrical, gravitational, kinetic, pneumatic, hydraulic, vacuum, thermal, pressure, springs, capacitors, fluids, and stored program state.
- Fire detection/suppression, combustible loading, hot work, gas cylinders, ventilation, spill control, wastewater, hazardous materials, and emergency response.
- Ergonomic reach, posture, force, visibility, lighting, noise, loading height, maintenance access, lifting, sharp edges, pinch points, and human error controls.
- Applicable laws, regulations, codes, consensus standards, customer specifications, adopted editions, jurisdiction, authority, deviations, certification path, and evidence.
- Residual risks, labels, manual warnings, training, PPE, restricted access, supervision, and owner acceptance.

Never use a disclaimer as a substitute for hazard reduction or required compliance.

## 12. Utilities, environment, and facility

- Ambient temperature, humidity, altitude, dust, conductive contamination, water, corrosives, vibration, shock, lighting, electromagnetic environment, clean-room needs, and indoor/outdoor use.
- Floor loading, flatness, foundation, anchors, isolation, ceiling height, doors, aisle, crane/forklift access, shipping splits, installation route, and seismic/wind requirements.
- Electrical power, compressed air quality/pressure/flow, vacuum, water quality/pressure/flow, drainage, wastewater, gas types/pressure/flow, coolant, extraction, network, and HVAC.
- Heat rejection, ventilation makeup air, exhaust discharge, noise boundary, fire protection, environmental permits, and waste handling.
- Facility interfaces, connection points, shutoffs, regulators, filtration, monitoring, alarms, and utility-failure safe states.

## 13. Manufacturing, assembly, and logistics

- Make/buy strategy, supplier capability, material certificates, special processes, qualified weld procedures, heat treatment, coating, machining envelope, and inspection capability.
- Datum flow, tolerance stack, fits, surface finish, geometric controls, shim/adjustment strategy, alignment features, error correction, and interchangeability.
- Weld sequence, distortion allowance, stress relief, machining-after-weld, bonding preparation, bolted-joint preload, torque method, locking, and witness marks.
- Assembly sequence, tooling, fixtures, cleanliness, lubrication, cable/hose installation, calibration, software load, and in-process inspection.
- Lifting points, center of gravity, shipping restraints, corrosion protection, packaging, shock/tilt monitoring, disassembly, installation, leveling, anchoring, and requalification.
- Configuration identification, serial numbers, drawing/BOM/software revision alignment, deviations, nonconformance, rework, and as-built capture.

## 14. Metrology, verification, and commissioning

- Requirement-specific verification method: analysis, inspection, demonstration, test, certification, or similarity with justified applicability.
- Instrument type, range, resolution, accuracy, uncertainty, calibration status, environmental controls, fixture, setup, repetitions, sample size, and data retention.
- Geometry tests: level, straightness, flatness, squareness, parallelism, backlash, reversal, positioning, repeatability, volumetric error, spindle runout, and tool-center-point error.
- Dynamic tests: speed, acceleration, jerk, following error, contouring, settling, vibration, resonance, stop time/distance, collision handling, and sustained duty.
- Thermal tests: warm-up, steady state, gradients, drift, cooling recovery, ambient changes, and compensation.
- Process tests: representative materials, thicknesses, geometries, tools, recipes, edge/surface quality, capability, consumable life, and worst-case combinations.
- Electrical/controls tests: insulation, protective bonding, protection, I/O, fault insertion, power interruption, regeneration, EMC pre-compliance, network failure, backup/restore, and cybersecurity controls.
- Safety validation: guards, interlocks, stops, reset/restart, safe states, single faults, energy isolation, labels, manuals, and residual-risk acceptance.
- Factory acceptance, site acceptance, commissioning sequence, punch list, release authority, and requalification triggers.

## 15. Reliability, maintenance, and lifecycle

- Reliability target, availability target, mean time to repair, criticality, failure modes, diagnostic coverage, degraded modes, and recovery time.
- Bearing, rail, screw, belt, gearbox, spindle/head, pump, filter, fan, seal, cable, relay/contactor, brake, and consumable life assumptions.
- Lubricants, points, quantities, intervals, compatibility, automatic systems, low-level/pressure detection, contamination control, and records.
- Preventive/predictive maintenance tasks, intervals, skill, tools, access, lockout, calibration, acceptance limits, and return-to-service tests.
- Spare parts, approved equivalents, shelf life, storage, lead time, obsolescence monitoring, vendor support, and last-time-buy strategy.
- Cleaning, waste, decontamination, software updates, backups, cybersecurity patches, incident logs, and service documentation.
- End-of-life disassembly, hazardous material handling, recycling, data removal, and disposal.

## 16. Cost, schedule, sourcing, and documentation

- Capital ceiling, target cost, contingency, engineering labor, tooling, facility work, certification, freight, installation, training, spares, consumables, utilities, maintenance, and lifecycle cost.
- Schedule milestones, dependencies, long-lead items, design reviews, prototype, procurement, fabrication, integration, test, certification, installation, and ramp.
- Supplier, country, lead time, minimum order, currency, logistics, approved alternatives, counterfeit risk, lifecycle status, warranty, support, and qualification.
- BOM with manufacturer part number, description, quantity, revision, approved source, unit cost, mass, criticality, and compliance evidence.
- Required documents: requirements, architecture, calculations, risk assessment, standards matrix, drawings, schematics, software/configuration, BOM, manufacturing/assembly instructions, inspection/test plans, reports, manuals, training, maintenance, spares, declarations/certificates, and as-built dossier.

## 17. Conditional process branches

### Spindle/router/mill

- Material and tool range, spindle type, power, continuous/peak torque, speed range, constant-power/torque regions, taper/collet, tool interface, runout, bearing life, balance grade, VFD, braking, cooling, warm-up, tool change, probing, coolant/mist, chip/dust extraction, and fire risk.

### Plasma

- Material/thickness, plasma source, current, duty, torch type, consumables, gases, pressure/flow, pierce/cut height, torch-height control, arc voltage, work lead, high-frequency start, EMI controls, water/slat table, fume extraction, dross, fire watch, and cut-quality targets.

### Fiber laser

- Material/thickness/reflectivity, source type and wavelength, power, beam quality, fiber/delivery limits, optics, focus range, cutting head, height sensing, assist gases, pressure/flow/purity, nozzle, enclosure, laser class, access control, interlocks, viewing, fire detection, fume extraction, and optical safety validation.

### Abrasive waterjet

- Material/thickness, pressure, flow, pump type, intensifier/direct drive, orifice, mixing tube, abrasive type/mesh/flow, hopper, catcher/tank, water quality, chiller, high-pressure plumbing, whip protection, pressure release, sludge/wastewater, noise, taper/kerf, and maintenance life.

### Water-jet-guided laser

- Material/thickness/reflectivity, laser source/wavelength/power/beam quality, water pressure/flow/quality/temperature, optical coupling, nozzle/orifice, focus and standoff control, jet stability, high-pressure plumbing/restraints/release, cooling, enclosure, laser classification/interlocks, fume/wastewater, combined optical/pressure hazards, and qualification window.

### Additive/FDM

- Polymer/feedstock, filament/pellet system, nozzle, melt temperature, flow, extruder force, heater power, thermal runaway protection, bed size/flatness/temperature, chamber temperature, ventilation, layer height, bead width, shrinkage/warping, slicing, material handling/drying, fire detection, and print qualification.

### Pick and place/robotic cell

- Payload, reach, degrees of freedom, cycle time, repeatability, singularities, inertia, end effector, gripping force/vacuum, part variation, vision, lighting, calibration, conveyors/fixtures, collision zones, collaborative/non-collaborative operation, safeguarded space, force/speed limits, and recovery.

### Inspection/metrology machine

- Measurands, feature/material range, measurement volume, accuracy and uncertainty target, test-uncertainty ratio policy, sensor/probe/scanner type, probing force, kinematics, fixture/datums, environmental control, vibration, thermal soak, calibration artifacts, traceability chain, sampling path, data processing, uncertainty budget, verification, and requalification.

### Hybrid or novel process

- Name every constituent process and complete each applicable branch. Add interface loads, incompatible media/contamination, changeover, shared utilities, mode confusion, combined energy, software mode enforcement, cross-process hazards, and cross-process verification. Novel processes require an added parameter branch and audit rule before detailed design.

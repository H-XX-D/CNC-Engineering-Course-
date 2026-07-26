# End-to-end machine design questionnaire

Use this as a living requirements interview, not a one-time form. Enter `TBD` for unknowns and `N/A - <reason>` for inapplicable items. Attach a requirement ID to every binding answer and record units, tolerance/range, condition, source, owner, and verification method for every numeric target.

## 0. Record control

- Project / machine name:
- Machine identifier:
- Questionnaire revision and date:
- Design stage: discovery / concept / preliminary / detailed / release
- Project owner:
- Technical authority:
- Safety authority:
- Reviewers and approvers:
- Change-control location:
- Related requirements, drawings, calculations, risk file, and BOM:

## 1. Mission, scope, and governance

1. What problem must the machine solve?
2. What is the intended use? What is explicitly outside scope?
3. Is this a new design, retrofit, research prototype, internal production machine, or commercial product?
4. Who will operate, load, program, maintain, clean, troubleshoot, install, and decommission it?
5. What foreseeable misuse, unusual operator behavior, or unauthorized access must be considered?
6. What measurable outcomes determine success?
7. What interfaces or technologies are fixed, and why are they fixed?
8. What assumptions have not yet been verified?
9. What contractual, customer, confidentiality, IP, export, or data obligations apply?
10. What countries, states, sites, or markets will install or receive the machine?
11. Who is the authority having jurisdiction? Is third-party certification/listing expected?
12. What is the design life in years, operating hours, cycles, starts, and relocations?

## 2. Process and product

1. Select every process:
   - [ ] Router / spindle cutting
   - [ ] Milling
   - [ ] Plasma cutting
   - [ ] Fiber laser cutting
   - [ ] Abrasive waterjet
   - [ ] Water-jet-guided laser
   - [ ] Additive / FDM
   - [ ] Pick and place
   - [ ] Robotic arm / workcell
   - [ ] Inspection / metrology
   - [ ] Hybrid
   - [ ] Other:
2. What enters the machine, what transformation occurs, and what must leave it?
3. List all part/stock materials, grades, thicknesses, hardnesses, coatings, and hazardous properties.
4. What are the minimum, typical, and maximum part and stock dimensions and masses?
5. What defects are acceptable, reworkable, or automatic rejects?
6. What dimensional, geometric, surface, edge, thermal, placement, or visual quality is required?
7. What part traceability, recipe, lot, operator, tool, and inspection records are required?
8. What representative and worst-case qualification parts will prove the process?

## 3. Throughput and operating model

1. Required parts per hour/shift and takt time:
2. Maximum cycle, setup, loading, unloading, tool/consumable change, and recipe-change time:
3. Shift pattern, hours/day, days/week, planned availability, and peak demand:
4. Continuous and intermittent states with duty cycle and duration:
5. Warm-up, stabilization, cleaning, calibration, and preventive-maintenance windows:
6. Manual, supervised automatic, or unattended operation? Under what conditions?
7. Required recovery time after common faults, power loss, tool breakage, or interrupted cycle:
8. Upstream/downstream material, data, and control interfaces:

## 4. Work envelope and workholding

1. Required X/Y/Z/rotary travel and usable process envelope:
2. Overtravel, homing, tool-change, probe, loading, guarding, and service clearances:
3. Axis naming, positive directions, origins, datums, work offsets, and coordinate transformations:
4. Stock, fixture, pallet, spoilboard/table, catcher, conveyor, and workholding arrangement:
5. Workholding force, allowable part distortion, datum repeatability, mistake proofing, and presence sensing:
6. Maximum fixture/pallet/tool/process-head/cable-carrier mass and center of gravity:
7. Material loading method, loading height, reach, crane/forklift needs, and collision zones:
8. Chip/debris/fluid evacuation and access around the part:

## 5. Performance requirements

For each value state typical/worst case, units, tolerance, environment, load, and verification method.

- Positioning accuracy by axis:
- Bidirectional repeatability by axis:
- Command/mechanical resolution by axis:
- Backlash/reversal error:
- Straightness, flatness, squareness, parallelism, and volumetric accuracy:
- Maximum following and contour error:
- Allowable static tool-to-work deflection by load case:
- Thermal drift after warm-up and over operating range:
- Required velocity, acceleration, deceleration, jerk, and settling time by axis:
- Required coordinated-motion/cornering performance:
- Minimum structural natural frequency or dynamic-compliance target:
- Vibration/chatter and surface-quality limits:
- Noise, heat, energy, emissions, dust/fume/mist, wastewater, and consumables targets:

## 6. Architecture and kinematics

1. Candidate architectures considered:
2. Selected architecture and trade-study reference:
3. Fixed/moving gantry, moving table, cantilever, bridge, Cartesian, parallel, articulated, or hybrid:
4. Controlled, slaved, redundant, coupled, manual, and gravity axes:
5. Axis stack order and moving members:
6. Complete process-force loop and path to the foundation:
7. Abbe offsets, centers of mass, tipping envelope, and singularities:
8. Cable, hose, vacuum, gas, coolant, and extraction motion through full travel:
9. Modularity, expansion, transport splits, leveling, anchoring, and isolation:
10. Service and safe-recovery positions:

## 7. Load-case inventory

For every case record direction, point of application, magnitude/range, duration, cycles, combination, source, uncertainty, and acceptance criterion.

- [ ] Gravity and dead weight
- [ ] Payload and fixture
- [ ] Clamping/workholding
- [ ] Cutting/process reaction
- [ ] Acceleration/deceleration/jerk
- [ ] Friction, preload, cable/hose drag
- [ ] Pressure, vacuum, hydraulic/pneumatic
- [ ] Rotating imbalance and vibration
- [ ] Tool change and material handling
- [ ] Jam, crash, seized bearing, broken tool/transmission
- [ ] Emergency stop and uncontrolled energy
- [ ] Lost brake/counterbalance/pressure/vacuum/power
- [ ] Thermal gradients and runaway
- [ ] Operator/service/maintenance
- [ ] Foundation, anchoring, tipping, seismic/wind
- [ ] Lifting, transport, shipping shock
- [ ] Other:

## 8. Structure, joints, and thermal design

1. Frame/gantry/Z/bed materials, grades, conditions, property sources, and corrosion protection:
2. Section geometry, plate thicknesses, spans, supports, and foundation model:
3. Datum hierarchy and mounting-surface requirements:
4. Welded, bolted, bonded, cast, extruded, filled, or composite joints:
5. Joint preload, slip, contact, stiffness, fatigue, locking, and inspection strategy:
6. Deflection/error budget allocation from tool to workpiece:
7. Stress, buckling, fatigue, local/contact, weld, fastener, adhesive, anchor, and lifting checks required:
8. Modal targets, excitation map, damping/isolation, FEA plan, and physical correlation:
9. Heat sources/sinks, gradients, time constants, expansion directions, symmetry, and compensation:
10. Warm-up, coolant/chiller, enclosure cooling, sensors, and thermal acceptance tests:
11. Fabrication sequence, weld distortion, stress relief, machining, alignment, and adjustability:

## 9. Axis worksheet - repeat for every axis

- Axis name, type, orientation, and travel:
- Moving mass, payload, center of mass, and gravity component:
- Process, inertia, friction, preload, cable/hose, abnormal, and stop loads:
- Maximum/typical velocity, acceleration, jerk, duty, and life:
- Linear/rotary guide type, size, arrangement, spacing, orientation, preload, ratings, seals, and lubrication:
- Guide mounting datums, tolerances, fasteners, and alignment method:
- Transmission type and geometry: screw/rack/belt/cable/linear/direct/gearbox:
- Pitch/module/diameter/ratio/efficiency/backlash/compliance/tension/supports:
- Critical speed, buckling, tooth/belt/cable load, thermal growth, and life results:
- Motor type/model, torque-speed curve, voltage/current, continuous/peak torque, speed, inertia, feedback, brake, and thermal rating:
- Drive model, control mode, current/voltage, regeneration, safe torque off, feedback, and faults:
- RMS/peak torque, speed, reflected inertia, acceleration, regeneration, and thermal margins:
- Coupling/gearbox/pulley/pinion/shaft/bearing details and ratings:
- Home, limit, hard stop, overtravel, absolute position, manual recovery, and brake/counterbalance behavior:
- Axis verification and acceptance criteria:

## 10. Process head and media

1. Process-head/tooling type, model, mass, center of gravity, ratings, interfaces, and replacement method:
2. Tool/consumable range, holders, offsets, life, breakage/wear detection, and inventory:
3. Process force, torque, heat, pressure, radiation/light, gas/fluid, debris, vibration, and EMI outputs:
4. Coolant, lubricant, gas, air, water, abrasive, resin/feedstock, vacuum, or hydraulic media requirements:
5. Supply quality, pressure, flow, temperature, purity, storage, monitoring, shutoff, and failure state:
6. Chip, dust, fume, mist, dross, abrasive, wastewater, scrap, heat, radiation, and noise control:
7. Recipe/parameter window, permissions, traceability, sensing, and calibration:
8. Process-specific branch completed below? yes/no/reference:

## 11. Electrical power and panel

1. Available voltage, phase, frequency, grounding system, capacity, source impedance/fault current, and disconnect:
2. Complete load list with nominal, peak, inrush, regeneration, duty, simultaneity, and criticality:
3. Main/branch protection, interrupting ratings, SCCR, selectivity, and lockout points:
4. Transformers, AC/DC supplies, DC buses, stored energy, braking resistors, discharge, and ride-through:
5. Conductor/cable type, ampacity, flex, bundling/ambient derating, voltage drop, insulation, routing, and bend radius:
6. Enclosure rating/material/size, segregation, clearances, heat losses, cooling, filtration, condensation, and service access:
7. Protective bonding, grounding, shields, isolation, surge/transient protection, EMC filters, ferrites, and cable separation:
8. Connectors, pinouts, keying, ratings, strain relief, mating cycles, and field replacement:
9. I/O voltage/current/analog ranges, isolation, noise, diagnostic coverage, and spare capacity:
10. Required single-line, schematics, panel layout, terminal plan, wire/cable schedule, labels, and test points:

## 12. Controls, feedback, software, and data

1. Controller/platform, lifecycle, licenses, real-time requirements, supported axes/kinematics, and I/O capacity:
2. Control mode, servo/trajectory rates, latency/jitter, motion limits, look-ahead, interpolation, and tuning method:
3. Feedback devices, location, resolution, accuracy, protocol, environment, and diagnostic coverage:
4. Open/closed-loop boundaries, dual-loop behavior, compensation, calibration maps, and persistence:
5. Machine modes and complete startup/home/run/pause/stop/fault/reset/recovery state model:
6. HMI users, controls, indications, alarms, units, accessibility, overrides, recipes, and audit trail:
7. PLC/HAL/firmware/software repositories, versions, tests, simulation, release, signing, backup, rollback, and obsolescence:
8. Networks, protocols, segmentation, authentication, authorization, remote access, logs, patches, and threat model:
9. Data sampling, ownership, retention, privacy, storage, cloud/offline behavior, export, backup, and disaster recovery:
10. Behavior on power, feedback, communication, sensor, actuator, utility, storage, and controller failure:

### 12A. Pneumatic, hydraulic, and vacuum power

For each applicable medium record source, pressure, flow, quality/filtration, temperature, volume, duty, stored energy, components, ratings, monitoring, isolation, discharge/release, containment, leaks, utility loss, safe state, maintenance, and verification.

- Pneumatic circuits and actuators:
- Hydraulic circuits, pumps, accumulators, actuators, valves, cooling, and containment:
- Vacuum generation, reservoirs, zoning, sensing, part retention, and loss-of-vacuum response:

## 13. Safety and compliance

1. Hazard-analysis method, owner, lifecycle scope, review date, and risk-acceptance authority:
2. List each mechanical, electrical, thermal, pressure, fluid, laser/radiation, plasma/arc, fire/explosion, chemical, dust/fume, noise, ergonomic, software, and cyber hazard.
3. For each hazard: initiating event, exposed person/task, harm, severity, exposure, avoidance, existing controls, initial risk, additional reduction, residual risk, and verification.
4. Inherent design measures applied before guards, warnings, training, or PPE:
5. Guards, openings, reach, strength, visibility, access, interlocks/locking, defeat resistance, escape, and validation:
6. Emergency/protective stops, safe torque off, brakes, energy isolation/dissipation, reset, restart prevention, and stop-time tests:
7. Safety-related control target, architecture, diagnostics, fault exclusions, proof tests, and validation:
8. Lockout/tagout inventory for every stored energy source:
9. Fire/explosion prevention, detection, suppression, ventilation, gas cylinders, hot work, spills, and emergency response:
10. Ergonomic reach, posture, force, loading height, visibility, lighting, noise, lifting, maintenance, and human-error controls:
11. Jurisdictions, applicable regulations/codes/standards, editions/dates, authority, certification, deviations, and evidence:
12. Labels, manuals, training, PPE, restricted access, supervision, residual risks, and owner acceptance:

## 14. Facility, utilities, and environment

1. Installation address, indoor/outdoor use, altitude, ambient temperature/humidity, dust/water/corrosives, vibration/shock, and electromagnetic environment:
2. Floor/foundation capacity, flatness, anchors, isolation, ceiling, doors, aisles, installation route, crane/forklift, and seismic/wind needs:
3. Electrical, air, vacuum, water, drain, wastewater, gas, coolant, extraction, network, HVAC, and fire-protection connections:
4. Utility pressure/flow/quality/temperature/capacity, connection, shutoff, monitoring, alarms, and failure behavior:
5. Heat rejection, makeup air, exhaust discharge, noise boundary, environmental permits, and waste handling:

## 15. Manufacturing, assembly, and installation

1. Make/buy decisions, supplier capabilities, special processes, certificates, qualified procedures, and inspection:
2. Datum flow, tolerance stack, fits, finishes, GD&T, shim/adjustment, alignment, correction, and interchangeability:
3. Weld, heat treat, machining, coating, bonding, bolt-preload, cleanliness, and preservation sequence:
4. Assembly order, fixtures/tools, in-process checks, lubrication, cables/hoses, software load, and calibration:
5. Lifting, center of gravity, shipping restraints, packaging, split/reassembly, installation, leveling, anchoring, and requalification:
6. Serial/configuration identification, drawings/BOM/software alignment, deviations, nonconformance, rework, and as-built capture:

## 16. Verification, commissioning, and acceptance

1. Verification method and acceptance criterion for every requirement:
2. Instruments, range, resolution, accuracy, uncertainty, calibration, environment, fixture, repetitions, and data retention:
3. Geometry/positioning/repeatability/backlash/squareness/volumetric/runout tests:
4. Speed/acceleration/jerk/contour/settling/vibration/resonance/stop/duty tests:
5. Thermal warm-up, steady-state, gradient, drift, recovery, and ambient tests:
6. Representative and worst-case process tests and capability acceptance:
7. Electrical, protection, bonding, I/O, fault-insertion, interruption, regeneration, EMC, backup/restore, and cyber tests:
8. Guard, interlock, stop, reset/restart, safe-state, single-fault, isolation, label, manual, and residual-risk validation:
9. Factory acceptance, site acceptance, commissioning steps, punch list, release authority, and requalification triggers:

## 17. Reliability, maintenance, and lifecycle

1. Reliability, availability, repair-time, diagnostic, degraded-mode, and recovery requirements:
2. Critical component life, failure modes, derating, inspections, and replacement criteria:
3. Lubricants, points, amounts, intervals, compatibility, contamination control, automation, and monitoring:
4. Preventive/predictive tasks, intervals, tools, skill, access, isolation, records, and return-to-service tests:
5. Spares, equivalents, shelf life, storage, lead time, obsolescence, warranty, and vendor support:
6. Cleaning, decontamination, waste, software patches, backups, logs, and service records:
7. Decommissioning, hazardous materials, recycling, data removal, and disposal:

## 18. Cost, schedule, sourcing, and documentation

1. Capital ceiling, target, contingency, and lifecycle-cost horizon:
2. Engineering, tooling, facility, certification, freight, installation, training, spares, consumables, utilities, and maintenance costs:
3. Milestones, reviews, dependencies, prototype, procurement, long-lead items, fabrication, integration, testing, certification, installation, and ramp:
4. Supplier, country, lead time, MOQ, currency, alternatives, counterfeit risk, lifecycle, warranty, support, and qualification:
5. BOM fields and configuration-control process:
6. Required requirements, calculations, risk, standards, drawings, schematics, software, BOM, manufacturing, inspection, test, manual, training, maintenance, spares, certificates, and as-built records:

## 19. Process-specific branch: spindle/router/mill

- Material/tool range; spindle type/model; continuous/peak power and torque; speed range; taper/collet; runout; bearings; balance; VFD; braking; cooling; warm-up; tool change; probing; coolant/mist; chip/dust extraction; fire risk; cutting-force and chatter model; qualification cuts:

## 20. Process-specific branch: plasma

- Source/current/duty; torch; consumables; gases; pressure/flow; pierce/cut height; THC; arc voltage; work lead; HF start; EMI controls; water/slat table; fume extraction; dross/fire; material/thickness process window; qualification cuts:

## 21. Process-specific branch: fiber laser

- Material/thickness/reflectivity; source/wavelength/power/beam quality; delivery/optics/focus/head; height sensing; assist gas pressure/flow/purity; nozzle; cooling; enclosure/class/access/interlocks/viewing; fire/fume; optical safety; qualification cuts:

## 22. Process-specific branch: abrasive waterjet

- Material/thickness; pressure/flow; pump; intensifier/direct drive; orifice/mixing tube; abrasive type/mesh/flow/hopper; catcher/tank; water/chiller; high-pressure plumbing/restraints/release; sludge/wastewater/noise; taper/kerf; maintenance life; qualification cuts:

### 22A. Process-specific branch: water-jet-guided laser

- Material/thickness/reflectivity; laser source/wavelength/power/beam quality; water pressure/flow/quality/temperature; optical coupling; nozzle/orifice; focus/standoff/height control; jet stability; cooling; high-pressure plumbing/restraints/release; enclosure/class/interlocks; fume/wastewater; combined laser/pressure hazards; qualification cuts:

## 23. Process-specific branch: additive/FDM

- Feedstock; filament/pellet handling/drying; extruder; nozzle; melt/flow; heater/bed/chamber power and temperatures; runaway protection; layer/bead; shrinkage/warping; cooling/ventilation/fire; slicing; motion-flow synchronization; qualification builds:

## 24. Process-specific branch: pick-and-place/robotic cell

- Payload/inertia; reach/DOF/singularities; cycle/repeatability; joints/drives; end effector; grip/vacuum/retention; part variation; vision/lighting/calibration; conveyors/fixtures/tracking; collision/safeguarded space/collaboration; recovery; qualification cycle:

### 24A. Process-specific branch: inspection/metrology

- Measurands and feature/material range; measurement volume; accuracy/uncertainty; uncertainty-ratio policy; sensor/probe/scanner; probing force; kinematics; fixtures/datums; environmental and vibration control; thermal soak; calibration artifacts and traceability; sampling path; data processing; uncertainty budget; verification and requalification:

### 24B. Process-specific branch: hybrid machine

- Constituent processes and completed branch references; shared structure/axes/workholding/utilities; interface loads; incompatible media/contamination; changeover and cleaning; mode indication/authorization/enforcement; combined energy and hazards; cross-process collision/interlock analysis; qualification in every individual and combined mode:

## 25. Open-items register

| ID | Unknown / decision / risk | Why it matters | Owner | Needed by | Closure evidence | Status |
|---|---|---|---|---|---|---|
| | | | | | | |

## 26. Approval

- Discovery baseline approved by/date:
- Concept architecture approved by/date:
- Preliminary design approved by/date:
- Detailed design approved by/date:
- Safety validation approved by/date:
- Release approved by/date:
- Approved deviations and expiration/review points:

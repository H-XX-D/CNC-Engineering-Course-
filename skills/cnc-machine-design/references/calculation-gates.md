# Calculation and verification gates

Use this as a minimum analysis checklist, not a universal formula sheet. Select models that match geometry, boundary conditions, materials, control architecture, and failure modes. Record source paths and headings from the course plus any controlling official or vendor sources.

## Contents

- Calculation ledger contract
- Requirements and budgets
- Structure and thermal behavior
- Linear motion and bearings
- Drives and motors
- Process subsystem
- Electrical and enclosure
- Controls and motion quality
- Safety engineering
- Metrology and release

## Calculation ledger contract

Assign every analysis an ID such as `CALC-STR-001`. Record:

| Field | Required content |
|---|---|
| Requirement | One or more stable requirement IDs |
| Load case | Named normal, abnormal, service, transport, or fault condition |
| Model | Formula, simulation, test correlation, or controlled spreadsheet |
| Inputs | Value, unit, tolerance/range, condition, source, confidence |
| Assumptions | Explicit, bounded, owned, and testable |
| Result | Nominal and worst-case result with units |
| Allowable | Limit and authoritative source |
| Margin | Utilization, margin, or factor of safety with required convention |
| Sensitivity | Dominant uncertain inputs and effect on decision |
| Evidence class | Estimate, calculation, simulation, bench test, or machine test |
| Verification | Test/inspection method, acceptance criterion, and owner |

Reject unitless intermediate work unless the quantity is physically dimensionless. Run an independent unit and order-of-magnitude check for every safety- or architecture-critical result.

## Requirements and budgets

Before component sizing:

- Allocate accuracy/error, stiffness/deflection, thermal drift, cycle time, mass, power, heat, I/O, network latency, cost, and reliability budgets.
- Identify root-sum-square versus worst-case aggregation and justify independence assumptions.
- Separate typical, rated, and worst-case conditions.
- Define factors of safety or design margins by failure mode rather than applying one universal factor.
- Name conflicts: speed versus force, span versus stiffness, preload versus life/heat, accuracy versus cost, enclosure versus serviceability, and throughput versus risk.

Gate: allocated subsystem budgets reconcile with system requirements and leave explicit integration margin.

## Structure and thermal behavior

Minimum applicable checks:

- free-body diagrams and reaction loads for all governing cases;
- axial, bending, shear, torsional, bearing/contact, fastener, weld, adhesive, and foundation stresses;
- static displacement at the tool center point and workpiece datum;
- Euler or inelastic buckling where compression and slenderness apply;
- fatigue or cumulative damage for cyclic members and joints;
- joint/contact compliance and preload loss;
- natural frequencies, mode shapes, excitation map, separation margin, and damping;
- thermal expansion, gradients, heat paths, time constants, warm-up, symmetry, and compensation;
- lifting, transport, anchoring, tipping, seismic/wind, and service loads where applicable.

Common first-order models include beam deflection such as `delta = F L^3 / (48 E I)` only for the matching simply supported center-load case, axial growth `delta_L = alpha L delta_T`, and frequency models derived from the actual boundary conditions. Do not transplant coefficients between support cases.

Gate: the complete tool-to-workpiece error loop meets static, dynamic, and thermal budgets under traceable load combinations, with FEA correlated to hand calculations or tests when used.

## Linear motion and bearings

For each axis check:

- equivalent radial, axial, and moment loads on each carriage/bearing;
- static safety and dynamic life using the manufacturer’s applicable exponent and factors;
- rail/carriage spacing, load sharing, preload, mounting accuracy, and edge loading;
- ball/lead screw torque, axial capacity, column buckling, critical speed, DN/speed limit, support-bearing life, whip, and thermal growth;
- rack tooth/contact load, pinion life, mesh alignment, lubrication, backlash, and rack-joint transitions;
- belt/cable tension, tooth load, span vibration, stretch/compliance, pulley bearing load, fatigue, and retention;
- lubrication type, quantity, interval, contamination, seals, purge, and failure detection;
- hard-stop load and overtravel energy absorption.

Gate: capacity and life margins hold at worst position, orientation, acceleration, process load, preload, and contamination condition.

## Drives and motors

Build a torque/force-versus-time profile rather than sizing from one peak:

- `F_total` includes inertia, gravity, process, friction, preload, cable/hose drag, pressure, and contingency;
- convert transmission force to motor torque with actual ratio, pitch/radius, and efficiency;
- calculate RMS/continuous torque and peak torque with duration;
- check maximum motor speed, torque-speed curve, voltage/back-EMF limit, current limit, and field-weakening/constant-power region;
- calculate motor, transmission, and reflected load inertia plus acceptable control margin;
- evaluate acceleration time/distance, jerk, settling, and process disturbance rejection;
- calculate kinetic/potential energy during stop, regeneration, DC bus rise, braking resistor duty, and power-loss behavior;
- verify gravity-axis brake/counterbalance capacity, engage timing, proof test, and controlled lowering;
- check gearbox/coupling/shaft/key/clamp loads, torsional stiffness, backlash, balance, bearing loads, and life;
- check motor/drive thermal duty, enclosure ambient, altitude derating, cooling loss, and stall conditions.

Gate: the complete motor-drive-transmission-axis system meets motion requirements over the full operating envelope with continuous, peak, thermal, regeneration, and fault margins.

## Process subsystem

### Spindle and cutting

- cutting speed, chip load, feed rate, radial/axial engagement, material removal rate, torque, power, tool deflection, holder interface, spindle torque-speed envelope, bearing/load limit, runout, chatter/excitation, coolant/chip extraction, and tool life.

### Plasma

- source current/duty, material/thickness process window, pierce/cut height, traverse range, torch-height-control dynamics, gas flow/pressure, extraction airflow/capture, table heat/water effects, work lead, EMI energy paths, and consumable life.

### Laser

- source power and duty, spot/focus and optical limits, material/thickness process window, assist gas pressure/flow/storage, head clearance and height control, enclosure/beam containment, heat/fire load, extraction, and cooling. Use qualified laser-safety analysis and current official limits; do not derive safe exposure from the course alone.

### Waterjet

- pressure/flow/hydraulic power, orifice and mixing-tube operating window, abrasive flow/storage, reaction load, traverse/process window, high-pressure component ratings/fatigue, accumulator energy, pressure decay, catcher capacity, water/chiller load, and sludge/wastewater.

### Water-jet-guided laser

- laser power/duty and optical limits, water pressure/flow/quality/temperature, coupling efficiency, nozzle/orifice operating window, jet stability, focus/standoff control, high-pressure component ratings/fatigue, stored pressure energy and decay, cooling, laser containment/interlocks, fume/wastewater, and combined optical/pressure fault cases.

### Additive

- melt/flow rate, extruder force/torque, heater and bed power, warm-up energy/time, chamber loss, thermal runaway detection, motion/flow synchronization, shrinkage, cooling, and sustained duty.

### Robots and handling

- reach/singularity analysis, payload and inertia tensor, joint torque-speed duty, deflection, gripper force/vacuum, part retention in stop/fault, cycle-time simulation, collision energy, vision resolution/field/depth, calibration uncertainty, and conveyor tracking.

### Inspection and metrology

- measurement-volume kinematics, probe/scanner force and access, sensor range/resolution/accuracy, complete uncertainty budget, environmental and thermal sensitivity, fixture/datum contribution, calibration artifact uncertainty, traceability chain, sampling strategy, algorithm validation, and requalification interval.

### Hybrid processes

- close every constituent process gate, then calculate shared-axis and structural load combinations, utility simultaneity, interface loads, incompatible-media contamination, mode-transition energy, collision envelopes, fault propagation, and worst-case combined operation. Validate both isolated and combined modes.

Gate: vendor ratings, calculations, and representative process trials cover the worst credible material/part/recipe combination.

## Electrical and enclosure

Minimum checks:

- connected, demand, peak, inrush, and regenerative load by operating state;
- supply capacity, transformer and power-supply rating, DC bus, storage, discharge, and ride-through;
- branch protection, interrupting rating, available fault current, SCCR, coordination, and disconnects;
- conductor ampacity, bundling/ambient/flex derating, voltage drop, insulation, protective bonding, and touch-current considerations;
- contactor/relay/switch/connector make, break, utilization, inrush, fault, and lifecycle ratings;
- enclosure heat balance, component losses, ambient/altitude, filter fouling, fan/pump failure, condensation, and surface temperature;
- I/O current budget, analog error/noise, isolation, surge/transient, grounding, shielding, filter, cable separation, and EMC pre-compliance;
- compressed air, hydraulic, gas, heater, laser, plasma, pump, spindle, and auxiliary interlocks in the energy-control architecture.

Gate: a reviewed single-line, load list, protection study appropriate to risk, schematics, panel layout, I/O schedule, cable schedule, and thermal analysis agree with selected hardware.

## Controls and motion quality

Minimum checks and evidence:

- sample/servo/trajectory rates, latency and jitter budgets, step-rate or fieldbus capacity;
- encoder/scale resolution and accuracy, interpolation, quantization, electrical bandwidth, and feedback location;
- command resolution, mechanical transmission resolution, accuracy, repeatability, backlash, compliance, and following-error budget;
- trajectory limits, look-ahead, acceleration/jerk, coordinated motion, corner error, settling, and cycle time;
- plant identification or measured response, loop stability margins, resonance/notch filters, feedforward, disturbance rejection, and saturation;
- homing/limits/absolute position behavior, power-cycle state, brake sequencing, loss of feedback, communication loss, and recovery;
- state-machine review, mode controls, permissions, fault latching, reset/restart prevention, alarms, logs, and configuration control;
- network capacity, failure behavior, security boundaries, backup, restore, update, rollback, and offline operation.

Gate: simulation or calculation predicts performance and instrumented machine tests confirm it under representative loads and fault cases.

## Safety engineering

Safety is not closed by a numerical score alone. Perform a lifecycle hazard analysis and document risk reduction in the hierarchy of controls.

Applicable calculations/tests can include:

- stopping time and distance under worst load, speed, brake state, and energy condition;
- protective-device separation distance using current applicable standards and measured stop time;
- guard strength, opening/reach, retention, viewing and material compatibility;
- stored-energy magnitude and verified dissipation/isolation time;
- safety-related control reliability/performance using current component data and the selected standard;
- exhaust capture, hazardous concentration, heat/fire load, pressure-fluid energy, noise exposure, and ergonomic loads;
- safe payload retention, gravity-axis drop prevention, pressure loss, and single-fault behavior;
- fault injection for interlocks, emergency stops, safe torque off, brake control, feedback loss, network loss, restart, and reset.

Gate: a qualified reviewer approves the hazard log, current applicability matrix, safety requirements, risk-reduction implementation, validation plan, test evidence, and residual-risk communication. A disclaimer does not satisfy this gate.

## Metrology and release

- Build an uncertainty budget for every acceptance measurement.
- Require instrument resolution and uncertainty appropriate to the tolerance; do not use nominal display resolution as accuracy.
- Define setup, environment, warm-up, sampling, repetitions, reversal, loading, data reduction, outlier policy, and acceptance rule before testing.
- Verify geometry, positioning, repeatability, thermal drift, dynamic contouring, process output, sustained duty, safety functions, utilities, EMC behavior, recovery, documentation, and training as applicable.
- Use capability metrics only with a stable process, justified distribution/sampling, and specification limits tied to requirements.
- Correlate calculations and simulations with test; investigate material discrepancies rather than averaging them away.

Release gate: every critical requirement has acceptable evidence or an approved, time-bounded deviation with compensating controls. Open safety-critical requirements block release.

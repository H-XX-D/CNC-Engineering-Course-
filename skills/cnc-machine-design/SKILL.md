---
name: cnc-machine-design
description: Design, specify, review, and validate CNC and mechatronic machines from initial use case through requirements, architecture, engineering calculations, safety, compliance, sourcing, commissioning, and release. Use for CNC routers, mills, plasma cutters, laser cutters, waterjets, additive machines, pick-and-place systems, robotic cells, retrofits, axis upgrades, design reviews, machine requirement documents, parameter intake, trade studies, calculation ledgers, verification plans, and end-to-end machine design questionnaires.
---

# CNC Machine Design

Convert a machine idea into a traceable engineering package. Use the bundled questionnaire to discover requirements, route technical questions into the course, calculate with explicit assumptions and units, and stop at safety or evidence gates rather than inventing certainty.

## Start every design

1. Locate the course root. When this skill is inside the course repository, use the directory two levels above this file. Otherwise ask for a checkout or work from user-supplied sources.
2. Copy `assets/machine-design-questionnaire.md` and `assets/machine-design-input.json` into the project workspace. Never overwrite a filled copy.
3. Record the design stage: `discovery`, `concept`, `preliminary`, `detailed`, or `release`.
4. Interview in short rounds. Ask only the highest-impact unresolved questions, fill facts already supplied, and record unknowns as `TBD`. Use `N/A` only with a reason.
5. Run `python3 scripts/audit_intake.py <filled-input.json> --stage <stage>` after each round.
6. Maintain stable requirement IDs, assumption IDs, calculation IDs, hazard IDs, and verification IDs. Connect every calculation and test to the requirement it supports.

Do not treat completion of the questionnaire as proof that the machine is safe or fit for service. The questionnaire is a coverage control; engineering evidence closes requirements.

## Work through five gates

### 1. Discovery gate

Freeze the problem before selecting components:

- intended process, parts, materials, users, operating environment, and production objective;
- work envelope, payload, utilities, facility limits, budget, schedule, and jurisdiction;
- measurable targets for accuracy, repeatability, resolution, speed, acceleration, throughput, surface quality, and duty cycle;
- prohibited outcomes and non-negotiable safety constraints.

Reject solution-first requirements such as “use a NEMA 34 motor” unless the user identifies them as a fixed interface constraint.

### 2. Concept gate

Generate at least two feasible architectures when the design is not already constrained. Compare kinematics, load paths, process compatibility, serviceability, risk, cost, and verification burden. Select with a traceable trade study; do not choose by familiarity alone.

Define:

- axis count, travels, coordinate conventions, moving masses, and vertical/gravity axes;
- frame and gantry topology, datum strategy, linear guidance, drive transmission, motors, feedback, and control class;
- process head, workholding, material handling, enclosure, extraction, cooling, lubrication, and utilities;
- control boundaries, energy-isolation points, safe states, and human interaction.

### 3. Preliminary-design gate

Establish load cases and close first-order sizing. Read `references/calculation-gates.md` before calculating. For every result show:

- governing requirement and load case;
- formula or model, units, inputs, source, assumptions, and uncertainty;
- nominal result, allowable limit, margin or factor of safety, and sensitivity to dominant inputs;
- validation method and unresolved risks.

Do not confuse resolution with accuracy, static stiffness with dynamic stability, component ratings with system capability, or standards references with certification.

### 4. Detailed-design gate

Resolve interfaces and implementation evidence:

- drawings, datums, tolerances, fits, preload, fasteners, weld sequence, cable routing, connectors, grounding, shielding, cooling, lubrication, guarding, and service access;
- exact component part numbers with vendor datasheets, derating, lifecycle status, and approved alternatives;
- electrical load list, schematics, protection, conductor sizing, enclosure heat, I/O list, state machine, fault behavior, and software configuration;
- hazard log with risk-reduction measures and verification evidence;
- BOM, make/buy decisions, manufacturing plan, inspection plan, and configuration baseline.

For current regulations, codes, standards, and vendor specifications, verify against primary official sources. State jurisdiction, edition/date, applicability, and authority having jurisdiction. The course is educational guidance, not a substitute for a licensed engineer, certification body, or regulatory authority.

### 5. Release gate

Require objective evidence before declaring the machine released:

- requirements traceability has no unexplained gaps;
- calculations and drawings are reviewed and revision controlled;
- safety functions, stopping behavior, guarding, interlocks, emergency stops, energy isolation, and fault recovery are tested;
- geometric accuracy, repeatability, process capability, thermal stability, EMC behavior, duty cycle, and acceptance criteria are verified where applicable;
- manuals, maintenance schedules, spares, training, residual-risk notices, and as-built records exist;
- deviations and waivers name an owner, rationale, expiration/review point, and compensating control.

## Route into the course

Read `references/course-map.md` to choose only relevant module files. Use `rg` to find formulas, worked examples, failure modes, and standards discussions inside those modules. Do not load the million-word corpus wholesale.

Read these bundled resources as needed:

- `references/parameter-catalog.md`: field definitions, units, conditional branches, and evidence expectations.
- `references/calculation-gates.md`: minimum analyses and release checks by subsystem.
- `references/course-map.md`: course module and appendix routing.
- `assets/machine-design-questionnaire.md`: human interview and workshop form.
- `assets/machine-design-input.json`: machine-readable intake baseline.
- `assets/machine-design-report.md`: final design-package structure.

## Produce the design package

Use `assets/machine-design-report.md` as the output skeleton. At minimum deliver:

1. scope, exclusions, stakeholders, and design stage;
2. requirements and assumption registers;
3. selected architecture and rejected alternatives;
4. load cases and calculation ledger;
5. mechanical, electrical, controls, software, process, and facility specifications;
6. safety, regulatory, and standards applicability record;
7. BOM and sourcing risks;
8. manufacturing, assembly, alignment, and commissioning plan;
9. verification matrix and acceptance criteria;
10. maintenance, documentation, training, residual risks, and open issues.

Label estimates, unverified vendor claims, simulations, calculations, bench tests, and machine tests distinctly. Never present one evidence class as another.

## Audit the questionnaire

Run:

```bash
python3 scripts/audit_intake.py path/to/machine-design-input.json --stage discovery
```

The script reports missing stage-gated and process-conditional fields. A clean audit means the intake is populated for that stage; it does not approve the design. Fix the source questionnaire rather than suppressing missing fields.

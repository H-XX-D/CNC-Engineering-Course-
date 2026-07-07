# Module 2 – Vertical Axis and Column Assembly

## 1. Z-Axis Design Philosophy

The vertical axis (Z-axis) presents unique engineering challenges fundamentally different from horizontal motion axes. While horizontal axes operate in a relatively neutral gravitational field and benefit from distributed loads, the vertical axis must continuously resist gravity, manage large cantilever moments, and overcome the dynamic challenges of moving masses in opposition to gravitational acceleration. The design philosophy for vertical axis systems integrates structural mechanics, dynamic stability theory, mass-energy management, and thermal compensation into a coherent framework that delivers precision, responsiveness, and reliability.

### 1.1 Mass & Inertia Management: The Foundation of Dynamic Performance

#### Fundamental Challenge

Every kilogram of mass moving on the Z-axis requires continuous energy input to resist gravity and demands proportionally higher motor torque for acceleration. The moment of inertia about the drive screw axis scales with the square of the radial distance, making compact designs critical.

#### Design Principles

1. Minimum Mass Design:
   - Use topology optimization to remove non-structural material
   - Employ high-strength aluminum alloys (7075-T6, yield ~500 MPa) instead of steel where possible
   - Consider magnesium alloys (AZ91D) for ultra-lightweight applications (density 1.8 g/cm³ vs 2.7 g/cm³ for Al)
   - Use hollow-core composite structures (carbon fiber/epoxy) for ultimate mass reduction

2. Gravitational Energy Management:
   The potential energy change during vertical motion:
   $$\Delta E_p = m g \Delta z$$
   
   For a 5 kg spindle assembly moving 200 mm:
   $$\Delta E_p = 5 \times 9.81 \times 0.2 = 9.81 \text{ J}$$
   
   This energy must be supplied (upward motion) or dissipated (downward motion) by the drive system.

3. Counterbalance Strategy:
   A properly implemented counterbalance system:
   - Reduces motor RMS torque by ~50-70%
   - Eliminates gravitational bias in the servo control loop
   - Enables symmetric acceleration profiles
   - Reduces thermal load on motor and amplifier
   - Extends bearing and drive component life

#### Counterbalance Force Calculation

For a moving mass $m$ with center of gravity at distance $L_{cg}$ from the column mounting plane:

$$F_{cb} = m g \cos(\theta)$$

Where $\theta$ is the machine tilt angle (typically 0° for vertical machines).

For adjustable counterbalance using gas springs:
$$F_{gas}(x) = F_0 + k_{gas}(x - x_0)$$

Where:
- $F_0$ = initial preload force
- $k_{gas}$ = gas spring stiffness (typically 0.5-2.0 N/mm)
- $x$ = displacement from neutral position
- $x_0$ = initial compressed length

#### Design Example

Moving mass: 8 kg (spindle + mounting plate + carriage)
Required counterbalance force: $F = 8 \times 9.81 = 78.5$ N

Using two gas springs in parallel:
- Individual spring force: 39.3 N
- Select standard 400 N gas spring compressed to ~10% extension
- Mounting geometry ensures force vector alignment within ±5° over full travel

4. Moment of Inertia Minimization:
   For a rotating drive screw, the reflected inertia is critical:
   
   $$J_{total} = J_{motor} + J_{coupling} + J_{screw} + \frac{m_{carriage}}{(2\pi/p)^2}$$
   
   Where $p$ is the screw pitch (m/revolution).
   
   For a 5 mm pitch screw:
   $$J_{reflected} = \frac{m}{(2\pi/0.005)^2} = m \times 6.33 \times 10^{-7}$$
   
   An 8 kg carriage reflects as: $J = 5.06 \times 10^{-6}$ kg·m²
   
   This is typically 10-50× the motor rotor inertia, dominating system dynamics.

### 1.2 Column Stiffness: Structural Optimization for Precision

Engineering Objective:
The column structure must provide a rigid reference frame that maintains rail parallelism and minimizes deflection under cutting forces. Unlike horizontal gantry beams that can be designed as simply-supported structures, vertical columns typically function as cantilevers with concentrated loads at the free end.

Cantilever Mechanics:

For a cantilever beam with length $L$, Young's modulus $E$, and second moment of area $I$, subjected to tip load $F$:

$$\delta_{tip} = \frac{F L^3}{3 E I}$$

Critical Insight: Deflection scales with the *cube* of length and inversely with moment of area. Doubling column height increases deflection by 8×, while doubling cross-sectional depth increases stiffness by ~8× (for rectangular sections).

Design Strategy:

1. Maximize Second Moment of Area:
   For rectangular hollow section (external dimensions $b × h$, wall thickness $t$):
   
   $$I_x = \frac{b h^3}{12} - \frac{(b-2t)(h-2t)^3}{12}$$
   
   For a 150×150×8 mm square tube:
   $$I_x = \frac{150 \times 150^3}{12} - \frac{134 \times 134^3}{12} = 42.19 \times 10^{6} - 26.98 \times 10^{6}$$
   $$I_x = 15.21 \times 10^{6} \text{ mm}^4 = 1.52 \times 10^{-5} \text{ m}^4$$

2. Material Selection:
   Common materials for column structures:
   
   | Material | E (GPa) | Density (kg/m³) | $E/\rho$ | Cost multiplier |
   |----------|---------|----------------|----------|----------------|
   | Mild steel | 200 | 7850 | 25.5 | 1.0× |
   | Cast iron | 120 | 7200 | 16.7 | 0.8× |
   | Aluminum 6061 | 69 | 2700 | 25.6 | 3.5× |
   | Steel + ribs | 200 | 7850 | 25.5 | 1.4× |
   
   Key Insight: While aluminum has lower absolute stiffness, its specific stiffness (E/ρ) matches steel. For vertical axes where mass reduction is critical, ribbed aluminum columns offer excellent performance.

3. Internal Ribbing and Stiffening:
   Strategic placement of internal ribs increases $I$ without proportional mass increase:
   
   - Longitudinal ribs at extreme fibers (corners)
   - Transverse bulkheads every 150-250 mm
   - Diagonal bracing in high-stress regions
   
   FEA-optimized designs achieve 30-50% stiffness increase with only 15-20% mass penalty.

4. Deflection Specification:
   Industry practice for precision machines:
   
   $$\delta_{max} = \frac{L}{10,000} \text{ to } \frac{L}{20,000}$$
   
   For 500 mm cantilever:
   $$\delta_{max} = 0.025 \text{ to } 0.05 \text{ mm}$$

Worked Example: Column Sizing

Requirements:
- Cantilever length: $L = 400$ mm
- Maximum cutting force: $F = 500$ N (conservative)
- Material: Steel ($E = 200$ GPa)
- Allowable deflection: $\delta_{max} = 0.03$ mm

Solution:

Required moment of inertia:
$$I_{req} = \frac{F L^3}{3 E \delta_{max}} = \frac{500 \times 0.4^3}{3 \times 200 \times 10^9 \times 0.00003}$$

$$I_{req} = \frac{32}{18 \times 10^6} = 1.78 \times 10^{-6} \text{ m}^4 = 1.78 \times 10^6 \text{ mm}^4$$

For square hollow section, approximating $I \approx \frac{b^3 t}{3}$ (thin-wall):
$$b^3 t \approx 5.33 \times 10^6$$

Trying $b = 120$ mm, $t = 8$ mm:
$$120^3 \times 8 = 13.8 \times 10^6 \text{ mm}^4$$ (adequate)

Selected section: 120×120×8 mm steel RHS
- Mass per meter: 28.3 kg/m
- Actual $I_x = 3.52 \times 10^6$ mm⁴ (provides 2× safety factor)

### 1.3 Symmetry & Thermal Behaviour: Compensating Environmental Effects

Thermal Expansion Challenge:
Vertical columns experience thermal gradients from:
1. Motor heat dissipation (30-100 W continuous)
2. Ambient temperature variations (±5°C typical)
3. Process heat (cutting/welding operations)
4. Solar loading (through enclosure panels)

Thermal Expansion Coefficient:
For steel: $\alpha = 11.7 \times 10^{-6}$ /°C

A 500 mm column experiencing 10°C differential:
$$\Delta L = \alpha L \Delta T = 11.7 \times 10^{-6} \times 500 \times 10 = 0.0585 \text{ mm}$$

This 58 μm error exceeds precision requirements!

Design Solutions:

1. Symmetric Cross-Sections:
   Using square or circular hollow sections ensures uniform thermal expansion in all radial directions. Asymmetric sections (C-channel, I-beam) create differential expansion leading to bending.

2. Thermal Symmetry:
   - Mount motors on centerline or use paired motors
   - Insulate motor from column structure
   - Use thermal breaks at mounting interfaces
   - Employ forced air circulation within hollow column

3. Material Selection:
   Materials with low thermal expansion coefficients:
   
   | Material | α (10⁻⁶/°C) | Relative expansion |
   |----------|-------------|-------------------|
   | Steel | 11.7 | 1.00× |
   | Aluminum | 23.6 | 2.02× |
   | Cast iron | 10.8 | 0.92× |
   | Invar 36 | 1.3 | 0.11× |
   | Carbon fiber | 0.5 to -1.0 | 0.04× |
   
   Practical Approach: Use steel or cast iron for primary structure, with carbon fiber composite in extreme precision applications.

4. Active Compensation:
   Modern CNC controllers implement thermal compensation:
   
   $$Z_{corrected} = Z_{commanded} + K_{thermal}(T - T_{ref})$$
   
   Where $K_{thermal}$ is determined through calibration cycles.

### 1.4 Vibration & Resonance: Dynamic Stability Requirements

Fundamental Principle:
The natural frequency of the Z-axis structure must be significantly higher than the servo control bandwidth to prevent control-structure interaction and ensure stable operation.

Natural Frequency Calculation:

For cantilever column modeled as spring-mass system:
$$f_n = \frac{1}{2\pi}\sqrt{\frac{k}{m}}$$

Where the spring constant for cantilever:
$$k = \frac{3EI}{L^3}$$

Combined expression:
$$f_n = \frac{1}{2\pi}\sqrt{\frac{3EI}{mL^3}}$$

Design Rule:
$$f_n \geq 5 \times f_{servo} \text{ (minimum)}$$
$$f_n \geq 10 \times f_{servo} \text{ (preferred)}$$

For typical servo bandwidth of 30 Hz:
$$f_n \geq 150 \text{ Hz (minimum)}$$
$$f_n \geq 300 \text{ Hz (preferred)}$$

Worked Example:

Given:
- Column: 120×120×8 mm steel RHS
- Length: $L = 400$ mm
- Moving mass: $m = 8$ kg
- $E = 200$ GPa
- $I = 3.52 \times 10^{-6}$ m⁴

Calculate natural frequency:

$$k = \frac{3 \times 200 \times 10^9 \times 3.52 \times 10^{-6}}{0.4^3} = \frac{2.112 \times 10^6}{0.064} = 33.0 \times 10^6 \text{ N/m}$$

$$f_n = \frac{1}{2\pi}\sqrt{\frac{33.0 \times 10^6}{8}} = \frac{1}{6.283}\sqrt{4.125 \times 10^6}$$

$$f_n = \frac{2031}{6.283} = 323 \text{ Hz}$$

Result: This design achieves $f_n = 323$ Hz, providing 10.8× margin over 30 Hz servo bandwidth (excellent).

Resonance Mitigation Strategies:

1. **Structural Damping:**
   - Use cast iron (damping ratio ξ ≈ 0.02-0.05) instead of steel (ξ ≈ 0.001-0.002)
   - Add constrained-layer damping treatments
   - Use polymer-composite hybrid structures

2. **Modal Analysis:**
   Perform FEA to identify all modes below 500 Hz:
   - 1st mode: Typically Z-axis bending
   - 2nd mode: Torsion about column axis
   - 3rd mode: X-Y rocking of carriage
   
   Ensure all modes satisfy $f_i > 5 f_{servo}$

3. **Active Damping:**
   Modern servo drives implement notch filters and low-pass filters to suppress resonances:
   
   Notch filter transfer function:
   $$H(s) = \frac{s^2 + 2\zeta_z \omega_n s + \omega_n^2}{s^2 + 2\zeta_p \omega_n s + \omega_n^2}$$
   
   Tuned to structural resonant frequency with high attenuation.

### 1.5 Serviceability: Design for Maintenance and Adjustment

**Critical Insight:**
The most precisely designed vertical axis will degrade over time without proper maintenance access. Bearing preload adjustment, rail replacement, and alignment verification must be possible without complete machine disassembly.

**Design Requirements:**

1. **Bearing Access:**
   - Removable covers at bearing mounting locations
   - Jack-screw provisions for preload adjustment
   - Clearance for bearing puller tools
   - Documented preload values (typically 4-8% of dynamic load rating)

2. **Rail Replacement:**
   - Rails should be removable without disturbing column structure
   - Use dowel pins for repeatable rail positioning
   - Provide access for precision height gauge measurements
   - Design for single-rail replacement (if paired rails used)

3. **Screw Alignment:**
   - Shim packs at bearing mounts
   - Slotted mounting holes (±1.0 mm adjustment)
   - Dial indicator access points
   - Alignment specification: ≤0.02 mm TIR over full travel

4. **Counterbalance Adjustment:**
   - External force adjustment (gas spring pressure or weight stack)
   - Test procedure: Measure motor current at mid-stroke with zero external load
   - Target: ≤10% variation from ideal balance current

5. **Cable Management:**
   - Use cable carriers (drag chains) sized for 2× bend radius of largest cable
   - Provide strain relief at moving carriage
   - Route away from chip zones
   - Allow for future additions (extra 30% capacity)

**Maintenance Schedule:**

| Component | Interval | Procedure |
|-----------|----------|-----------|
| Rail preload | 6 months | Verify bearing preload, adjust if needed |
| Screw lubrication | 3 months | Re-grease ball nut via zerk fitting |
| Counterbalance | 12 months | Verify force ±10%, adjust gas spring pressure |
| Rail parallelism | 12 months | Height gauge measurement, shim if needed |
| Resonance check | 12 months | Accelerometer test, update notch filters |

***

## 1.6 Integrated Design Philosophy Summary

The design of precision vertical axes requires simultaneous optimization of multiple competing objectives:

1. **Minimize moving mass** → Reduced motor torque, faster acceleration
2. **Maximize structural stiffness** → Dimensional stability under load
3. **Ensure thermal symmetry** → Minimize position errors from temperature
4. **Achieve high natural frequency** → Stable servo control without resonance
5. **Enable maintenance access** → Long-term precision retention

**Design Workflow:**

```
1. Define performance requirements (travel, speed, cutting forces)
2. Calculate required column stiffness → Select cross-section
3. Estimate moving mass → Design counterbalance system
4. Verify natural frequency > 5× servo bandwidth
5. Perform thermal FEA → Verify symmetric expansion
6. Design maintenance access features
7. Prototype and measure → Iterate
```

The successful vertical axis represents a balanced compromise where no single parameter is over-optimized at the expense of overall system performance. The following sections provide detailed implementation guidance for each subsystem.

***


---

## References

1. **ISO 13849-1:2015** - Safety of machinery - Safety-related parts of control systems
2. **EN 60204-1:2018** - Safety of machinery - Electrical equipment - General requirements
3. **ANSI/NFPA 79-2021** - Electrical Standard for Industrial Machinery
4. **Mayr Antriebstechnik Safety Brake Catalog** - Spring-applied brake sizing and selection
5. **Warner Electric Brake Catalog** - Electromagnetic and spring-set brake specifications
6. **Slocum, A.H. (1992).** *Precision Machine Design*. SME. - Gravity compensation systems

---

# Module 2 – Vertical Axis and Column Assembly

## 2. Vertical Axis Architecture

The architecture of a vertical axis system integrates mechanical, electrical, and control subsystems into a cohesive design that delivers precision vertical motion under gravitational load. This section provides comprehensive specifications, design rationale, and engineering trade-offs for each architectural element.

### 2.1 Travel Range: Determining Working Height

**Design Considerations:**

The Z-axis travel range determines the maximum part height that can be machined and influences nearly every other design parameter. The selection process balances workspace requirements against structural complexity and cost.

**Typical Applications:**

| Application | Travel Range | Rationale |
|-------------|--------------|-----------|
| Sheet metal plasma/laser | 100-150 mm | Limited part thickness, prioritize stiffness |
| General machining | 150-250 mm | Balanced capability for moderate parts |
| Large component machining | 250-400 mm | Heavy industrial, requires robust structure |
| 3D printing (large format) | 400-1000 mm | Tall build volumes, lower cutting forces |

**Structural Scaling:**

As travel increases, structural requirements scale unfavorably:

$$\delta \propto L^3$$

A 2× increase in travel requires 8× the structural moment of inertia to maintain the same deflection specification, typically resulting in 3-4× increase in column cross-section and mass.

**Design Example:**

**Requirement:** Plasma cutting of 25 mm steel plate
- Plate thickness: 25 mm
- Torch standoff: 3-5 mm
- Pierce height: 10 mm above plate
- Clearance for fixturing: 50 mm
- Safety margin: 20 mm

**Calculation:**
$$Travel = 25 + 5 + 10 + 50 + 20 = 110 \text{ mm minimum}$$

**Selected Travel:** 150 mm (provides operational flexibility)

### 2.2 Drive Type Selection: Ball-Screw vs. Belt Drive

**Ball-Screw Drive:**

*Advantages:*
1. High stiffness (minimal elastic deflection under load)
2. Zero backlash (with preload)
3. High positioning resolution
4. Predictable servo response
5. High force capacity (10-50 kN typical)

*Disadvantages:*
1. Higher cost ($200-$800 for precision grades)
2. Critical speed limitations
3. Requires lubrication maintenance
4. Acoustic noise at high speeds

**Engineering Analysis:**

Ball-screw stiffness:
$$k_{screw} = \frac{EA}{L}$$

For Ø20 mm screw, 400 mm length, steel:
$$k_{screw} = \frac{200 \times 10^9 \times \pi \times 0.01^2}{0.4} = 157 \times 10^6 \text{ N/m}$$

This high stiffness (157 N/μm) ensures the drive mechanism does not become the compliance-limiting element.

**Critical Speed:**

The critical rotational speed at which the screw becomes dynamically unstable:

$$n_{cr} = \frac{k \times 10^6 \times d_r}{L^2}$$

Where:
- $k$ = support factor (3.5 for fixed-supported, 4.7 for fixed-free)
- $d_r$ = root diameter (mm)
- $L$ = unsupported length (mm)

For Ø20 mm screw, 400 mm length, fixed-supported:
$$n_{cr} = \frac{3.5 \times 10^6 \times 18}{400^2} = \frac{63 \times 10^6}{160,000} = 393 \text{ rpm}$$

At 5 mm pitch: $v_{max} = 393 \times 0.005 = 1.97$ m/min

**Belt Drive:**

*Advantages:*
1. Lower cost ($50-$150 for complete drive)
2. No critical speed limitations
3. Quiet operation
4. No lubrication requirements
5. High speed capability (10-20 m/min feasible)

*Disadvantages:*
1. Lower stiffness (belt elasticity)
2. Potential backlash from belt stretch
3. Requires tension maintenance
4. Lower force capacity (500-2000 N typical)

**Belt Stiffness Analysis:**

Effective stiffness of tensioned timing belt:
$$k_{belt} = \frac{E_{eff} \cdot A_{belt}}{L_{span}} + \frac{T_{tension}}{elongation}$$

For GT2 belt, 800 mm span, 3000 N tension:
$$k_{belt} \approx 15 \times 10^6 \text{ N/m}$$ (approximately 10× lower than ball-screw)

**Application Guide:**

| Parameter | Choose Ball-Screw | Choose Belt |
|-----------|------------------|-------------|
| Cutting forces | > 500 N | < 200 N |
| Positioning accuracy | < 0.05 mm | 0.05-0.20 mm acceptable |
| Speed requirement | < 10 m/min | > 10 m/min |
| Budget | Premium acceptable | Cost-sensitive |
| Maintenance access | Good | Limited |

**For precision Z-axis applications (plasma, laser, milling):** Ball-screw is strongly preferred due to superior stiffness and accuracy.

### 2.3 Guide System: Linear Rails and Load Distribution

**Rail Selection Criteria:**

1. **Size (Width × Height):**
   Common sizes: MGN12, MGN15, HGR20, HGR25, HGR30
   
   Selection based on load capacity and moment resistance:
   
   | Rail Type | Dynamic Load (kN) | Moment Capacity (N·m) | Application |
   |-----------|-------------------|----------------------|-------------|
   | MGN12 | 1.7 | 12 | Light duty, 3D printing |
   | MGN15 | 2.8 | 24 | Light machining, laser |
   | HGR20 | 4.8 | 65 | Medium machining, plasma |
   | HGR25 | 7.3 | 125 | Heavy machining, milling |
   | HGR30 | 10.8 | 215 | Industrial machining |

2. **Preload Class:**
   - **Z0 (light preload):** 0.02C₀ - General purpose, low friction
   - **ZA (medium preload):** 0.04C₀ - Precision positioning
   - **ZB (heavy preload):** 0.08C₀ - High stiffness, vibration resistance

**Critical Design Parameter: Rail Spacing**

The moment arm provided by wide rail spacing dramatically improves pitching resistance:

$$\theta_{pitch} = \frac{M_{applied}}{k_{moment}}$$

Where moment stiffness:
$$k_{moment} = k_{rail} \times (d_{spacing})^2$$

**Worked Example:**

**Given:**
- Applied cutting force: $F = 400$ N
- Distance from rail centerline to tool tip: $L = 150$ mm
- Applied moment: $M = 400 \times 0.15 = 60$ N·m

**Case 1:** Rail spacing = 80 mm
- Single rail stiffness: $k_{rail} = 500$ N/μm = $5 \times 10^8$ N/m
- Moment stiffness: $k_M = 5 \times 10^8 \times 0.08^2 = 3.2 \times 10^6$ N·m/rad
- Angular deflection: $\theta = 60 / (3.2 \times 10^6) = 18.75 \times 10^{-6}$ rad
- Tip deflection: $\delta = 150 \times 18.75 \times 10^{-6} = 2.8$ μm

**Case 2:** Rail spacing = 120 mm
- Moment stiffness: $k_M = 5 \times 10^8 \times 0.12^2 = 7.2 \times 10^6$ N·m/rad
- Angular deflection: $\theta = 60 / (7.2 \times 10^6) = 8.33 \times 10^{-6}$ rad
- Tip deflection: $\delta = 150 \times 8.33 \times 10^{-6} = 1.25$ μm

**Result:** 50% increase in rail spacing (80→120 mm) reduces angular deflection by 55% and tip deflection by 55%.

**Design Rule:** 
$$d_{spacing} \geq 0.6 \times column\_width$$ (minimum)
$$d_{spacing} \geq 0.8 \times column\_width$$ (preferred)

### 2.4 Motor Orientation: Vertical vs. Horizontal Mounting

**Vertical Mounting (Motor Above Axis):**

*Advantages:*
1. Protected from chips and cutting fluids
2. Simplified cable management (stationary connections)
3. Direct drive possible (no gearbox needed)
4. Natural heat dissipation (convection upward)

*Disadvantages:*
1. Increases overall machine height
2. Adds rotating mass to moving assembly
3. Cable flexing at motor shaft
4. Requires sealed motor connectors

**Horizontal Mounting (Motor on Side):**

*Advantages:*
1. Compact vertical envelope
2. Motor remains stationary (longer life)
3. Fixed electrical connections
4. Easier motor replacement

*Disadvantages:*
1. Requires right-angle gearbox or belt/pulley transmission
2. Additional gear backlash (if gearbox used)
3. More complex mechanical design
4. Chip exposure (requires bellows protection)

**Heat Dissipation Analysis:**

Motor heat generation at 70% duty cycle:
$$Q = (P_{input} - P_{output}) \times duty$$

For 400W rated motor at 70% efficiency:
$$Q = (400 - 280) \times 0.7 = 84 \text{ W continuous}$$

This heat must be dissipated to prevent:
1. Thermal expansion of motor housing
2. Demagnetization of permanent magnets (>120°C risk)
3. Thermal gradient in column structure

**Cooling strategies:**
- Forced air cooling: 10-20 W/(m²·K) heat transfer coefficient
- Required surface area: $A = Q / (h \times \Delta T) = 84 / (15 \times 40) = 0.14$ m²
- Finned motor housing or attached heat sink recommended

**Recommended Configuration:**

For Z-axis travel < 250 mm and spindle mass < 5 kg:
- **Vertical mounting with sealed AC servo motor**
- Use motor brake to prevent gravity drop during power loss
- IP65 rated motor minimum
- Aluminum heat sink attached to motor frame

For Z-axis travel > 250 mm or spindle mass > 5 kg:
- **Horizontal mounting with right-angle gearbox**
- Ratio 3:1 to 5:1 for inertia matching
- Backlash-free gearbox (planetary or harmonic drive)
- Motor remains stationary (extended life)

### 2.5 Counterbalance Systems: Gravitational Force Compensation

**Fundamental Requirement:**

The counterbalance system must provide upward force equal to the weight of all moving components, reducing the motor's workload to only overcoming friction and accelerating mass (without the gravitational bias).

**Net Force Analysis (Unbalanced System):**

$$F_{motor} = ma + F_{friction} + mg \cdot sgn(direction)$$

For upward motion: Motor must lift weight AND accelerate
For downward motion: Motor must brake against falling weight

This asymmetry causes:
1. Servo tuning challenges (different gains needed for up vs. down)
2. Higher RMS motor current (thermal stress)
3. Asymmetric acceleration profiles
4. Increased bearing wear

**Net Force Analysis (Balanced System):**

$$F_{motor} = ma + F_{friction}$$

Gravitational term eliminated! Symmetric performance in both directions.

**Counterbalance Technologies:**

**1. Gas Springs:**

Nitrogen-charged gas springs provide nearly constant force over moderate strokes.

Force characteristic:
$$F(x) = F_0 \left(\frac{V_0}{V_0 - A x}\right)^n$$

Where:
- $F_0$ = initial force
- $V_0$ = initial gas volume
- $A$ = piston area
- $x$ = extension distance
- $n$ = polytropic exponent (≈ 1.2 for nitrogen)

For small displacements ($x << V_0/A$), force is approximately constant.

*Advantages:*
- Compact size
- No external power
- Adjustable force (via pressure)
- Long life (>1 million cycles)

*Disadvantages:*
- Force varies slightly with temperature
- Limited stroke (typically 0.5× compressed length)
- Progressive force characteristic

**Design Example:**

Moving mass: 6 kg → Required force: 58.9 N

Select: Two 300 N gas springs in parallel
- Initial compression: 80% of stroke
- Operating range: 70-90% compression
- Force variation over range: ±5%

**2. Counterweight System:**

Steel weights connected via cable and pulley provide constant gravitational counterforce.

$$F_{counterweight} = m_{weight} \times g$$

*Advantages:*
- Perfectly constant force
- No wear or degradation
- Temperature insensitive
- Simple and reliable

*Disadvantages:*
- Requires vertical space for weight travel
- Cable maintenance (lubrication, inspection)
- Pulley bearing friction
- More complex mechanical design

**Design Consideration:**

Cable routing over pulleys introduces friction:
$$F_{effective} = F_{weight} \times \eta_{pulley}^{n_{pulleys}}$$

For $\eta_{pulley} = 0.98$ (ball bearing pulley), 2 pulleys:
$$F_{effective} = F_{weight} \times 0.98^2 = 0.96 F_{weight}$$

4% force loss → Design for 104% of required counterweight mass.

**3. Constant-Force Springs:**

Tightly coiled springs that unroll to provide constant force.

*Advantages:*
- Compact
- No friction losses
- Long stroke capability

*Disadvantages:*
- Lower force capacity (typically < 50 N)
- Limited to light-duty applications
- Lateral space requirement for spring storage drum

**Tuning Procedure:**

1. Remove all external loads from Z-axis
2. Disable servo drive (free-wheeling mode)
3. Measure force required to move axis at constant velocity
   - Upward force: $F_{up}$
   - Downward force: $F_{down}$
4. Calculate ideal counterbalance force:
   $$F_{ideal} = \frac{F_{up} - F_{down}}{2}$$
5. Adjust counterbalance until $F_{up} \approx F_{down}$ (within ±10%)

**Verification:**
- Command slow velocity profile (50 mm/min) up and down
- Monitor motor current
- Target: <10% current variation between directions

### 2.6 Complete Architecture Summary Table

The following table provides comprehensive specifications for a precision vertical axis suitable for plasma cutting, laser cutting, and light milling applications:

| Component | Specification | Engineering Rationale | Notes |
|-----------|---------------|----------------------|-------|
| **Travel Range** | 150–250 mm | Covers typical plasma plate heights with margin | Increase for thicker materials |
| **Drive Type** | Ball-screw Ø16–25 mm | High stiffness, zero backlash, precision | Ø20 mm most common for medium loads |
| **Screw Pitch** | 5–10 mm | Balances speed and force capability | 5 mm for precision, 10 mm for speed |
| **Critical Speed Margin** | ≥ 30% margin; operate ≤ 80% of $n_{cr}$ | Avoids screw whipping and excessive vibration | Verify with end‑fixity factor and free length |
| **Screw Grade** | C5 or better | Position accuracy ≤ 0.023 mm/300 mm | C7 acceptable for non-precision work |
| **Guide Type** | Two linear rails | Distributed load, moment resistance | Single rail = inadequate moment capacity |
| **Rail Size** | 15–20 mm width | Load capacity 3-7 kN per rail pair | Scale with cutting forces |
| **Rail Spacing** | 80–120 mm | Maximizes moment arm for stiffness | Wider spacing = lower angular deflection |
| **Rail Preload** | Medium (ZA) or Heavy (ZB) | Eliminates play, increases stiffness | ZA for general, ZB for heavy cutting |
| **Motor Orientation** | Vertical (above) or Horizontal (side) | Vertical for chip protection, Horizontal for compactness | Trade-off between protection and height |
| **Motor Type** | AC Servo, 400-750W | Sufficient torque for acceleration + cutting forces | Include brake for gravity holding |
| **Motor Brake** | Electromechanical, 2-5 Nm | Prevents drop during power loss | Critical safety feature |
| **Gearbox** | 3:1 to 5:1 planetary (if used) | Inertia matching, torque multiplication | Backlash-free design required |
| **Counterbalance Type** | Gas spring or counterweight | Eliminates gravitational bias | Gas spring for compactness |
| **Counterbalance Force** | 100-110% of moving mass weight | Slight overbalance compensates friction | Adjustable design preferred |
| **Column Cross-Section** | 100×100 to 150×150 mm RHS | High moment of inertia, low deflection | Steel or aluminum with internal ribs |

### 2.7 Servo Integration and Torque Sizing (with Efficiency)

The servo must overcome gravity, friction, and commanded acceleration. Including screw efficiency $\eta$ and lead $L_{\text{lead}}$:
$$
T_{\text{req}} = \frac{L_{\text{lead}}}{2\pi\,\eta}\Big( m\,a + F_{\text{friction}} + m g \Big)
$$
Reflected linear inertia at the motor shaft is
$$
J_{\text{ref}} = m\left(\frac{L_{\text{lead}}}{2\pi}\right)^{2}, \qquad J_{\text{eq}} = J_m + J_{\text{ref}} + J_{\text{coupling}} + J_{\text{screw}}
$$
Maintain $J_{\text{ref}}/J_m$ between 1:1 and 5:1 for robust tuning.

**Worked Example – 200 mm Z‑Axis:**
Given $m=8$ kg, $L_{\text{lead}}=0.005$ m, $a=2.0\,g$, $F_{\text{friction}}=10$ N, $\eta=0.92$:
$$
T_{\text{req}} = \frac{0.005}{2\pi\cdot 0.92}\Big(8\cdot 2\cdot 9.81 + 10 + 8\cdot 9.81\Big) \approx 0.46\,\text{N·m}
$$
With a 3:1 gearbox, motor torque reduces to ~0.15 N·m (at 3× reflected inertia). Verify thermal limits and add 20–30% margin.

Feedforward improves tracking:
$$
T_{\text{ff}} = J_{\text{eq}}\,\frac{2\pi}{L_{\text{lead}}}\,\ddot{z} + \frac{L_{\text{lead}}}{2\pi\,\eta}\,F_{\text{friction}}(\dot{z})
$$
Tune gains while respecting the natural frequency target (≥5× servo bandwidth).

### 2.8 Brake Sizing and Drop Safety

The holding brake must prevent gravity‑induced motion during power loss:
$$
T_{\text{brake}} \ge \frac{L_{\text{lead}}}{2\pi\,\eta}\,m g \times S_f
$$
with safety factor $S_f$ (typically 1.5–2.5). For $m=8$ kg, $L_{\text{lead}}=5$ mm, $\eta=0.92$, $S_f=2$:
$$
T_{\text{brake}} \ge \frac{0.005}{2\pi\cdot 0.92} (8\cdot 9.81) \times 2 \approx 0.13\,\text{N·m}
$$
Select the next larger standard brake (e.g., 2.5 N·m) to account for wear, contamination, and incline. Add mechanical hard‑stops and soft‑limits; verify weekly during maintenance.

#### 2.8.1 Brake Verification Test (Commissioning)

Purpose: Confirm the holding brake prevents gravity‑induced motion and that no hazardous sag occurs during power loss.

Procedure:
- Jog Z to mid‑stroke; stop motion and engage brake (power ON).
- Disable servo drive power to simulate power loss; observe position with a 0.01 mm dial indicator.
- Re‑enable power; lift 2–3 mm; repeat test 3× to check repeatability.

Acceptance Criteria:
- Sag/displacement ≤ 0.05 mm within 10 s after power removal.
- No sustained downward drift (> 0.05 mm/min) while brake engaged.
- On re‑energizing, inrush current spike is transient; no prolonged overcurrent alarm.

If Fails:
- Increase brake size or adjust brake airgap per manufacturer spec.
- Reduce counterbalance over‑ or under‑bias to minimize net gravity load.
- Inspect screw/nut friction (contamination) and verify brake wiring/voltage.
| **Column Material** | Steel or Aluminum | Steel for stiffness, Aluminum for mass reduction | Consider thermal expansion |
| **Natural Frequency** | ≥ 150 Hz | Ensure > 5× servo bandwidth | Verify with FEA and accelerometer testing |
| **Cable Carrier** | Enclosed drag chain | Protects cables, manages flexing | Size for ≥ 2× cable bend radius |
| **Position Feedback** | Encoder 0.001 mm resolution | Closed-loop control, positioning accuracy | Rotary on motor or linear on axis |
| **Limit Switches** | Mechanical + inductive proximity | Hard limits (crash protection) + soft limits (control) | Dual redundancy for safety |

**Design Integration Notes:**

1. **Electrical Integration:**
   - Motor power cable: Shielded, oil-resistant, 1.5× rated current capacity
   - Encoder cable: Twisted-pair, shielded, separate conduit from power
   - Limit switch wiring: 24V DC logic, optically isolated inputs
   - Emergency stop loop: Hardwired series circuit, NC contacts

2. **Lubrication System:**
   - Ball-screw: Automatic grease injector every 8 hours operation
   - Linear rails: Manual regreasing every 6 months (via zerk fittings)
   - Grease type: NLGI Grade 2, lithium-based, -20°C to +120°C

3. **Thermal Management:**
   - Motor heat sink: Natural convection or forced air
   - Column insulation: Separate motor thermal mass from structure
   - Temperature monitoring: Thermistor on motor winding, shutdown at 130°C

4. **Safety Systems:**
   - Motor brake: Engages on power loss, prevents gravity drop
   - Counterbalance: Sized to prevent free-fall (even if brake fails)
   - Bellows/covers: Protect ball-screw from chip contamination
   - Software limits: Prevent over-travel before hitting hard stops

This comprehensive architecture provides a robust foundation for precision vertical axis performance across diverse CNC applications.

***


---

## References

1. **ISO 14728-1:2017** - Rolling bearings - Linear motion rolling bearings - Dynamic load ratings
2. **THK Linear Motion Systems Catalog** - Z-axis configurations and mounting
3. **Hiwin Linear Guideway Technical Manual** - Vertical axis applications
4. **NSK Linear Guides CAT. No. E728g** - Profile rail systems for vertical mounting
5. **Weck, M. & Brecher, C. (2006).** *Machine Tools 1*. Springer
6. **SKF Linear Motion & Actuation** - Vertical axis design guidelines

---

# Module 2 – Vertical Axis and Column Assembly

## 3. Core Equations for Column Behaviour

Understanding the mathematical relationships governing vertical axis structural behavior is essential for rational design decisions. This section derives and explains the fundamental equations that describe deflection, resonance, critical speeds, and servo stability requirements.

### 3.1 Cantilever Beam Deflection: The Foundation of Structural Design

**Physical Situation:**

The Z-axis column functions as a cantilever beam with:
- Fixed support at the base (machine bed or gantry)
- Free end carrying the moving carriage and tooling
- Concentrated load at the free end from cutting forces

**Fundamental Equation:**

For a cantilever beam with uniform cross-section, subjected to point load $F$ at distance $L$ from the fixed support:

$$\delta_B = \frac{F L^3}{3 E I}$$

**Derivation from Beam Theory:**

Starting with the moment-curvature relationship:
$$\frac{d^2 y}{dx^2} = \frac{M(x)}{E I}$$

For cantilever with tip load $F$, moment at distance $x$ from free end:
$$M(x) = -F x$$

Integrating once for slope:
$$\frac{dy}{dx} = \int \frac{-F x}{E I} dx = \frac{-F x^2}{2 E I} + C_1$$

Boundary condition at fixed end ($x=L$): $dy/dx = 0$
$$C_1 = \frac{F L^2}{2 E I}$$

Slope equation:
$$\frac{dy}{dx} = \frac{F}{2 E I}(L^2 - x^2)$$

Integrating for deflection:
$$y = \int \frac{F}{2 E I}(L^2 - x^2) dx = \frac{F}{2 E I}\left(L^2 x - \frac{x^3}{3}\right) + C_2$$

Boundary condition at fixed end ($x=L$): $y=0$
$$C_2 = -\frac{F}{2 E I}\left(L^3 - \frac{L^3}{3}\right) = -\frac{F L^3}{3 E I}$$

Deflection at free end ($x=0$):
$$\delta_B = y(0) = -\frac{F L^3}{3 E I}$$

The negative sign indicates downward deflection; taking absolute value:

$$\boxed{\delta_B = \frac{F L^3}{3 E I}}$$

**Design Form - Required Moment of Inertia:**

Rearranging to solve for the required structural property:

$$I_{req} = \frac{F L^3}{3 E \delta_{max}}$$

This is the primary design equation for column sizing.

**Worked Example 1: Plasma Cutting Column**

**Requirements:**
- Cantilever length: $L = 350$ mm (from column face to torch tip)
- Maximum cutting force: $F = 300$ N (conservative estimate)
- Material: Steel tube ($E = 200$ GPa)
- Allowable deflection: $\delta_{max} = 0.025$ mm (25 μm)

**Calculate required moment of inertia:**

$$I_{req} = \frac{300 \times 0.35^3}{3 \times 200 \times 10^9 \times 0.000025}$$

$$I_{req} = \frac{300 \times 0.042875}{15 \times 10^6} = \frac{12.8625}{15 \times 10^6}$$

$$I_{req} = 8.58 \times 10^{-7} \text{ m}^4 = 858,000 \text{ mm}^4$$

**Select appropriate section:**

For square RHS (hollow rectangular section), approximate formula for thin-walled section:

$$I = \frac{b h^3}{12} - \frac{(b-2t)(h-2t)^3}{12}$$

For square section ($b = h$):
$$I = \frac{b^4 - (b-2t)^4}{12}$$

**Trial section: 100×100×6 mm**

$$I = \frac{100^4 - 88^4}{12} = \frac{100,000,000 - 59,969,536}{12}$$

$$I = \frac{40,030,464}{12} = 3,335,872 \text{ mm}^4$$

**Verification:**
$$I_{actual} = 3.34 \times 10^6 \text{ mm}^4 > I_{req} = 8.58 \times 10^5 \text{ mm}^4$$

**Safety factor:** $SF = 3.34/0.858 = 3.9$ ✓ (adequate)

**Calculated deflection with selected section:**
$$\delta = \frac{300 \times 0.35^3}{3 \times 200 \times 10^9 \times 3.34 \times 10^{-6}}$$

$$\delta = \frac{12.86}{2.004 \times 10^6} = 6.4 \times 10^{-6} \text{ m} = 0.0064 \text{ mm} = 6.4 \text{ μm}$$

**Result:** Actual deflection is 6.4 μm, well below 25 μm limit. The safety factor of 3.9× provides margin for:
- Dynamic loading (impacts, rapid accelerations)
- Assembly tolerances
- Material property variations
- Thermal effects

**Worked Example 2: Milling Machine Column**

**Requirements:**
- Cantilever length: $L = 400$ mm
- Maximum cutting force: $F = 800$ N (heavy milling)
- Material: Cast iron ($E = 120$ GPa, higher damping than steel)
- Allowable deflection: $\delta_{max} = 0.015$ mm (15 μm, tighter tolerance)

**Calculate required moment of inertia:**

$$I_{req} = \frac{800 \times 0.4^3}{3 \times 120 \times 10^9 \times 0.000015}$$

$$I_{req} = \frac{51.2}{5.4 \times 10^6} = 9.48 \times 10^{-6} \text{ m}^4 = 9.48 \times 10^6 \text{ mm}^4$$

This requires a much larger section due to:
1. Higher cutting forces (800 N vs 300 N)
2. Longer cantilever (400 mm vs 350 mm)
3. Tighter deflection specification (15 μm vs 25 μm)
4. Lower material stiffness (cast iron vs steel)

**Selected section: 150×150×10 mm steel RHS with internal ribs**

$$I_{base} = \frac{150^4 - 130^4}{12} = 15.2 \times 10^6 \text{ mm}^4$$

Internal ribbing adds approximately 25% to effective I:
$$I_{total} \approx 19 \times 10^6 \text{ mm}^4$$

**Safety factor:** $SF = 19/9.48 = 2.0$ ✓ (acceptable for industrial application)

### 3.2 Natural (Resonant) Frequency: Dynamic Stability Analysis

**Physical Principle:**

Every structural system has natural frequencies at which it will vibrate with minimal damping. If external excitation (cutting forces, servo oscillations) occurs near a natural frequency, resonance amplifies vibrations, destroying positioning accuracy and potentially causing structural failure.

**Single-Degree-of-Freedom Model:**

The Z-axis column with moving carriage can be modeled as a spring-mass system:

$$f_n = \frac{1}{2\pi} \sqrt{\frac{k}{m}}$$

Where:
- $k$ = structural stiffness (N/m)
- $m$ = effective mass (kg)

**Cantilever Stiffness:**

From deflection equation $\delta = FL^3/(3EI)$, the spring constant is:

$$k = \frac{F}{\delta} = \frac{3 E I}{L^3}$$

**Natural Frequency of Cantilever with Tip Mass:**

$$f_n = \frac{1}{2\pi} \sqrt{\frac{3 E I}{m L^3}}$$

**Effective Mass Correction:**

For a cantilever with distributed mass $m_{beam}$ and tip mass $m_{tip}$, the effective mass is:

$$m_{eff} = m_{tip} + \alpha m_{beam}$$

Where $\alpha \approx 0.25$ for first-mode cantilever vibration (proven through modal analysis).

**Worked Example 3: Natural Frequency Calculation**

**Given:**
- Column: 120×120×8 mm steel RHS
- Length: $L = 450$ mm
- Moving mass (carriage + spindle): $m_{tip} = 7$ kg
- Column mass: $m_{beam} = 2.5$ kg/m × 0.45 m = 1.125 kg
- $E = 200$ GPa
- $I = 3.85 \times 10^{-6}$ m⁴

**Calculate effective mass:**
$$m_{eff} = 7 + 0.25 \times 1.125 = 7.28 \text{ kg}$$

**Calculate stiffness:**
$$k = \frac{3 \times 200 \times 10^9 \times 3.85 \times 10^{-6}}{0.45^3}$$

$$k = \frac{2.31 \times 10^6}{0.091125} = 25.35 \times 10^6 \text{ N/m}$$

**Calculate natural frequency:**
$$f_n = \frac{1}{2\pi} \sqrt{\frac{25.35 \times 10^6}{7.28}}$$

$$f_n = \frac{1}{6.283} \sqrt{3.482 \times 10^6} = \frac{1866}{6.283} = 297 \text{ Hz}$$

**Result:** First natural frequency is 297 Hz.

**Resonance Implications:**

If servo bandwidth is 30 Hz:
- Frequency ratio: $297 / 30 = 9.9$
- **Status:** ✓ Exceeds minimum 5× requirement (excellent design)

If servo bandwidth is 50 Hz:
- Frequency ratio: $297 / 50 = 5.9$
- **Status:** ✓ Meets minimum 5× requirement (acceptable)

If servo bandwidth is 70 Hz:
- Frequency ratio: $297 / 70 = 4.2$
- **Status:** ✗ Below minimum 5× requirement (resonance risk)

**Design Actions for Low-Frequency Structures:**

If calculated $f_n$ is insufficient:

1. **Increase structural stiffness:**
   - Larger cross-section (I increases with h³)
   - Add internal ribs/stiffeners
   - Use stiffer material (steel over aluminum)

2. **Reduce moving mass:**
   - Lighter spindle/tool assembly
   - Aluminum carriage components
   - Hollow-core designs

3. **Reduce cantilever length:**
   - Minimize tool offset from column
   - Compact carriage design

4. **Reduce servo bandwidth:**
   - Trade response speed for stability
   - Typical: Reduce from 50 Hz to 30 Hz

**Frequency vs. Stiffness Sensitivity:**

$$\frac{df_n}{f_n} = \frac{1}{2}\frac{dk}{k} - \frac{1}{2}\frac{dm}{m}$$

A 20% increase in stiffness → 9.5% increase in natural frequency
A 20% reduction in mass → 9.5% increase in natural frequency

**Priority:** Stiffness increases are more effective than mass reductions because:
- Stiffness scales with I (can increase dramatically with section size)
- Mass reduction limited by functional requirements

### 3.3 Ball-Screw Critical Speed: Rotational Stability Limit

**Physical Phenomenon:**

A rotating shaft (ball-screw) becomes dynamically unstable when rotational speed reaches the critical speed, at which lateral vibrations resonate with shaft rotation. This creates catastrophic whirling motion that can destroy bearings and damage the screw.

**Critical Speed Equation:**

$$n_{cr} = \frac{k_f \times 10^6 \times d_r}{L^2}$$

Where:
- $n_{cr}$ = critical rotational speed (rpm)
- $k_f$ = end-fixity factor (dimensionless)
- $d_r$ = root diameter of screw (mm)
- $L$ = unsupported length between bearings (mm)

**End-Fixity Factors:**

| Support Condition | $k_f$ | Description |
|-------------------|-------|-------------|
| Simply supported - simply supported | 3.14 | Both ends on radial bearings, free to rotate |
| Fixed - simply supported | 3.56 | One end clamped, one end on bearing |
| Fixed - fixed | 4.73 | Both ends rigidly clamped (rare) |
| Fixed - free (cantilever) | 0.56 | One end fixed, other end free (avoid!) |

**Common Configuration:** Fixed-supported (angular contact bearings at one end, radial bearing at other)
$$k_f = 3.56$$

**Worked Example 4: Critical Speed Analysis**

**Given:**
- Ball-screw: Ø20 mm, 5 mm pitch
- Root diameter: $d_r = 17.5$ mm
- Unsupported length: $L = 500$ mm
- Support: Fixed-supported ($k_f = 3.56$)

**Calculate critical speed:**

$$n_{cr} = \frac{3.56 \times 10^6 \times 17.5}{500^2}$$

$$n_{cr} = \frac{62.3 \times 10^6}{250,000} = 249 \text{ rpm}$$

**Maximum linear velocity:**

$$v_{max} = n_{cr} \times p = 249 \times 0.005 = 1.245 \text{ m/min} = 20.8 \text{ mm/s}$$

**Safety Factor Application:**

Industry practice: Operate at ≤ 80% of critical speed

$$n_{operating} = 0.8 \times 249 = 199 \text{ rpm}$$

$$v_{operating} = 199 \times 0.005 = 0.995 \text{ m/min} \approx 1.0 \text{ m/min}$$

**Design Decision:**
For applications requiring $v > 1$ m/min, this screw configuration is inadequate.

**Design Solutions for Higher Speeds:**

1. **Reduce unsupported length:**
   Add center bearing support to create two shorter spans.
   
   Example: 500 mm span → two 250 mm spans
   
   $$n_{cr,new} = \frac{3.56 \times 10^6 \times 17.5}{250^2} = 998 \text{ rpm}$$
   
   $$v_{max,new} = 998 \times 0.005 = 4.99 \text{ m/min}$$
   
   **Result:** 4× speed increase with center support bearing!

2. **Increase screw diameter:**
   Use Ø25 mm screw ($d_r = 22$ mm)
   
   $$n_{cr} = \frac{3.56 \times 10^6 \times 22}{500^2} = 314 \text{ rpm}$$
   
   26% speed increase, but increased cost and mass.

3. **Use preloaded screw:**
   Preloaded screws have effectively higher $k_f$ (≈ 4.0 vs 3.56)
   
   $$n_{cr} = \frac{4.0 \times 10^6 \times 17.5}{500^2} = 280 \text{ rpm}$$
   
   12% improvement.

4. **Switch to belt drive:**
   No critical speed limitation! Practical for rapid positioning axes where forces are moderate.

**Critical Speed vs. Application:**

| Application | Typical Speed | Screw Adequacy |
|-------------|---------------|----------------|
| Precision plasma THC | 0.5 m/min | ✓ Well within limits |
| Laser focal adjustment | 2-3 m/min | ⚠ May require center support |
| Rapid tool change positioning | 5-10 m/min | ✗ Belt drive recommended |
| Probing cycles | 0.1-0.2 m/min | ✓ No concerns |

### 3.4 Servo Resonance Criterion: Control-Structure Interaction

**Control Theory Principle:**

A servo control system with bandwidth $f_{servo}$ generates control signals with frequency content up to approximately $5 \times f_{servo}$. If any structural resonance exists within this range, the controller will excite the resonance, causing instability.

**Stability Criterion:**

$$f_n \geq 5 \times f_{servo}$$ (minimum requirement)

$$f_n \geq 10 \times f_{servo}$$ (preferred for robust control)

**Servo Bandwidth Definition:**

Servo bandwidth is the frequency at which the closed-loop gain drops to -3 dB (70.7% of DC gain). Higher bandwidth = faster response, but increased sensitivity to resonances.

**Typical Bandwidth Values:**

| Application | Servo Bandwidth | Required $f_n$ (5×) | Required $f_n$ (10×) |
|-------------|----------------|---------------------|---------------------|
| Positioning (slow) | 10 Hz | 50 Hz | 100 Hz |
| Standard machining | 30 Hz | 150 Hz | 300 Hz |
| High-speed machining | 50 Hz | 250 Hz | 500 Hz |
| Ultra-precision | 20 Hz | 100 Hz | 200 Hz |

**Worked Example 5: Servo Tuning for Structural Resonance**

**Given:**
- Measured natural frequency: $f_n = 180$ Hz (via accelerometer)
- Desired servo bandwidth: $f_{servo} = 40$ Hz
- Current configuration: PID controller

**Check stability criterion:**

$$\frac{f_n}{f_{servo}} = \frac{180}{40} = 4.5$$

**Result:** 4.5× ratio is below minimum 5× requirement (marginal stability).

**Design Options:**

**Option 1: Reduce Servo Bandwidth (Conservative)**

$$f_{servo,max} = \frac{f_n}{5} = \frac{180}{5} = 36 \text{ Hz}$$

- Reduce bandwidth from 40 Hz to 36 Hz (10% reduction)
- Trade-off: Slightly slower response, but guaranteed stability
- Implementation: Reduce proportional gain by 20%

**Option 2: Add Notch Filter (Sophisticated)**

Design notch filter centered at $f_n = 180$ Hz:

$$H(s) = \frac{s^2 + 2\zeta_z \omega_n s + \omega_n^2}{s^2 + 2\zeta_p \omega_n s + \omega_n^2}$$

Where:
- $\omega_n = 2\pi f_n = 1131$ rad/s
- $\zeta_z = 0.05$ (numerator damping - creates notch)
- $\zeta_p = 0.7$ (denominator damping - limits attenuation width)

This filter attenuates gain by 20-30 dB at 180 Hz while preserving performance at other frequencies.

- Advantage: Maintains 40 Hz bandwidth
- Disadvantage: Adds phase lag, requires tuning

**Option 3: Increase Structural Stiffness (Fundamental)**

Target: $f_n = 250$ Hz (provides 6.25× ratio at 40 Hz bandwidth)

Required stiffness increase:
$$\frac{f_{n,new}}{f_{n,old}} = \sqrt{\frac{k_{new}}{k_{old}}}$$

$$\frac{250}{180} = 1.39 = \sqrt{\frac{k_{new}}{k_{old}}}$$

$$\frac{k_{new}}{k_{old}} = 1.39^2 = 1.93$$

**Requirement:** Increase structural stiffness by 93%

**Approach:**
- Upgrade column from 100×100 to 120×120 mm (+73% in I)
- Add internal ribs (+20% effective stiffness)
- **Total:** 1.73 × 1.20 = 2.08× (meets requirement)

**Recommended Solution:**

For production machines: **Combination approach**
1. Increase structural stiffness to $f_n \geq 200$ Hz
2. Add notch filter for additional margin
3. Set servo bandwidth to 35-40 Hz
4. Verify stability with step response testing

**Verification Testing:**

After tuning, perform step response test:
1. Command 10 mm step input
2. Record position vs. time with high-resolution encoder
3. Measure:
   - Rise time (10%-90% of step)
   - Overshoot (should be < 10%)
   - Settling time (within ±0.01 mm)
   - Ringing frequency (should not match $f_n$)

**Acceptance Criteria:**
- Overshoot < 10%
- Settling time < 3 × rise time
- No sustained oscillations
- Position error < 0.02 mm after settling

***

## 3.5 Equation Integration: Holistic Design Process

The four core equations work together in the design process:

```
1. DEFLECTION → Size column cross-section for stiffness
              ↓
2. NATURAL FREQUENCY → Verify dynamic stability
              ↓
3. CRITICAL SPEED → Confirm ball-screw adequacy
              ↓
4. SERVO CRITERION → Validate control system compatibility
```

**Design Iteration Loop:**

```
Start with requirements (travel, forces, speed)
    ↓
Calculate required I (deflection equation)
    ↓
Select trial column section
    ↓
Calculate natural frequency
    ↓
    Check: f_n ≥ 5 × f_servo?
    ↓               ↓
   NO              YES
    ↓               ↓
Increase I    Calculate screw critical speed
    ↓               ↓
Iterate         Check: v_req ≤ 0.8 × v_critical?
                    ↓               ↓
                   NO              YES
                    ↓               ↓
           Add support bearing   DESIGN COMPLETE
           or use belt drive
```

All four equations must be satisfied simultaneously for a successful vertical axis design. This integrated approach ensures structural, dynamic, and control requirements are met without costly post-build modifications.

***


---

## References

1. **Young, W.C. & Budynas, R.G. (2011).** *Roark's Formulas for Stress and Strain* (8th ed.). McGraw-Hill
2. **Gere, J.M. & Timoshenko, S.P. (2012).** *Mechanics of Materials* (8th ed.). Cengage Learning
3. **Hibbeler, R.C. (2017).** *Structural Analysis* (10th ed.). Pearson
4. **Beer, F.P. et al. (2015).** *Mechanics of Materials* (7th ed.). McGraw-Hill
5. **ISO 11352:2012** - Cranes - Loading and stability calculations
6. **AISC Steel Construction Manual** (15th ed., 2017)

---

# Module 2 – Vertical Axis & Z-Stage


## Overview

Linear guides for vertical axes must address unique challenges beyond horizontal applications: gravitational preload, unequal loading on carriages, potential for binding under moment loads, and safety requirements for power-loss conditions. This section covers selection, sizing, and installation of linear guides optimized for Z-axis performance.

## Gravitational Loading Effects

### Constant Preload from Weight

Vertical guides experience continuous loading from moving mass weight:

**Load per carriage (4 carriages typical):**

$$F_{carriage} = \frac{m \times g}{n}$$

Where:
- m = moving mass (kg)
- g = 9.81 m/s²
- n = number of carriages (typically 4)

**Example:**
- Moving mass: 12 kg
- Load per carriage: 12 × 9.81 / 4 = 29.4 N

**Implications:**
- Minimum preload must exceed gravitational load
- Lower carriages carry slightly more load (column deflection)
- Preload selection more critical than horizontal axes

### Moment Loading

Off-center masses create moment loads:

$$M = F_{tool} \times d_{offset}$$

Moment distributes unequally across carriage pairs, potentially overloading one side.

## Rail Selection for Vertical Axes

### Size Selection

**Dynamic load capacity must account for:**
1. Gravitational constant load
2. Acceleration forces
3. Cutting forces
4. Safety factor (2-3× for vertical)

**Basic load rating:**

$$C_{required} = P \times \left(\frac{L_{design}}{L_{rating}}\right)^{1/3}$$

Vertical applications typically require one size larger than horizontal equivalent.

### Preload Selection

**Preload classes (HIWIN nomenclature):**
- **Z0**: Light preload (smallest clearance)
- **ZA**: Light-medium preload
- **ZB**: Medium preload (most common for vertical)
- **ZC**: Heavy preload (high-precision, rigid mounting)

**Recommendation for Z-axis:**
- Small machines (<10kg moving): ZA or ZB
- Medium machines (10-25kg): ZB or ZC
- Large machines (>25kg): ZC

Higher preload provides:
- Better rigidity under moment loads
- Reduced play and vibration
- Increased friction (counterbalance helps overcome)

### Rail Pair Configuration

**Single pair (not recommended):**
- Adequate for light loads only
- Poor moment resistance
- Risk of binding

**Dual pairs (standard):**
- Two rails, four carriages total
- Good moment capacity
- Spacing: 80-150mm typical

**Multiple pairs (heavy-duty):**
- Three+ rails for very heavy spindles
- Distributed loading
- Complex alignment requirements

## Installation and Alignment

### Rail Mounting

**Surface preparation:**
- Flatness: 10-20 µm over rail length
- Parallelism between rails: <20 µm
- Surface finish: Ra 1.6 µm

**Mounting procedure:**
1. Clean mounting surface and rail bottom
2. Apply thin layer of way oil
3. Position rail with dowel pins (if provided)
4. Tighten mounting screws progressively from center outward
5. Torque to specification (typically 6-8 N·m for M5, 12-15 N·m for M6)

### Carriage Alignment

**Vertical orientation:**
- All four carriages must align on single plane
- Misalignment causes binding and accelerated wear
- Use precision spacers during assembly

**Checking alignment:**
1. Install carriages on rails
2. Bolt to carriage plate with torque
3. Check smooth motion by hand over full travel
4. Any binding indicates misalignment—shim as needed

## Safety Considerations

### Brake Integration

Vertical axes require mechanical brakes for safety:

**Mounting options:**
1. Motor-integrated brake (most common)
2. Separate brake on ball screw
3. Friction brake on carriage (backup)

**Brake sizing:**
- Must hold 1.5× maximum moving mass
- Engage time: <100ms typical
- Spring-applied, electrically released (fail-safe)

### Anti-Drop Mechanisms

**Mechanical locks:**
- Spring-loaded pawl engages rack on power loss
- Manual release for maintenance
- Common on large machines

**Counterbalance as safety:**
- Properly balanced system prevents rapid descent
- Not sufficient as sole safety mechanism
- Use with brake for redundancy

## Key Takeaways

1. **Vertical guides** require higher preload and larger sizes than horizontal equivalents
2. **Gravitational loading** is continuous and must be included in capacity calculations
3. **Moment loads** from off-center masses require proper carriage spacing
4. **Alignment** is critical—poor alignment causes binding and premature failure
5. **Mechanical brakes** are mandatory safety devices for vertical axes
6. **Dual-pair configuration** (4 carriages) is standard for most applications
7. **Preload class ZB or ZC** recommended for vertical mounting
8. **Anti-drop mechanisms** provide additional safety layers

***

**Next**: [Section 2.5 – Ball Screws for Vertical Axes](section-2.5-ball-screw-vertical.md)

**Previous**: [Section 2.3 – Column Structural Design](section-2.3-column-structural-design.md)

---

# Module 2 – Vertical Axis and Column Assembly

## 5. Example Application – Designing a 200 mm Travel Z-Axis

This section presents a complete, worked design example that integrates all concepts from previous sections into a cohesive vertical axis system suitable for plasma cutting or laser engraving applications.

### 5.1 Design Requirements Specification

**Application:** Precision plasma cutting system
**Performance Requirements:**

| Parameter | Specification | Rationale |
|-----------|---------------|-----------|
| **Travel** | 200 mm | Accommodates 25 mm plate + fixturing + safety margin |
| **Positioning accuracy** | ±0.05 mm | Standard plasma cutting tolerance |
| **Repeatability** | ±0.02 mm | Consistent pierce and cut height |
| **Maximum cutting force** | 400 N | Conservative torch reaction force estimate |
| **Rapid traverse speed** | 3 m/min (50 mm/s) | Rapid repositioning between cuts |
| **Cutting feed rate** | 0.5-2 m/min | Typical plasma cutting speeds |
| **Torch mass** | 1.5 kg | Including mounting bracket and consumables |

**Environmental Conditions:**
- Operating temperature: 10-40°C
- Humidity: 20-80% (non-condensing)
- Contamination: Metal chips, plasma spatter, grinding dust
- Enclosure: IP54 minimum for column exterior

### 5.2 Column Sizing: Cantilever Deflection Analysis

**Step 1: Estimate Cantilever Length**

Torch centerline distance from column face:
- Column width: 120 mm
- Carriage thickness: 30 mm
- Torch offset from carriage: 80 mm

$$L_{cantilever} = \frac{120}{2} + 30 + 80 = 170 \text{ mm}$$

Add 20% safety margin for moments: $L_{design} = 1.2 \times 170 = 204$ mm ≈ 200 mm

**Step 2: Calculate Required Moment of Inertia**

Using deflection formula:
$$I_{req} = \frac{F L^3}{3 E \delta_{max}}$$

Given:
- $F = 400$ N (maximum cutting force)
- $L = 0.2$ m (200 mm cantilever)
- $E = 200$ GPa (steel)
- $\delta_{max} = 0.03$ mm (30 μm allowable deflection)

$$I_{req} = \frac{400 \times 0.2^3}{3 \times 200 \times 10^9 \times 0.00003}$$

$$I_{req} = \frac{3.2}{1.8 \times 10^7} = 1.78 \times 10^{-7} \text{ m}^4 = 1.78 \times 10^5 \text{ mm}^4$$

**Step 3: Select Column Cross-Section**

**Trial 1: 100×100×6 mm RHS**

$$I = \frac{100^4 - 88^4}{12} = 3.34 \times 10^6 \text{ mm}^4$$

$$SF = \frac{3.34 \times 10^6}{1.78 \times 10^5} = 18.8$$ (excessive, column is overdesigned)

**Trial 2: 80×80×5 mm RHS**

$$I = \frac{80^4 - 70^4}{12} = 1.68 \times 10^6 \text{ mm}^4$$

$$SF = \frac{1.68 \times 10^6}{1.78 \times 10^5} = 9.4$$ (still overdesigned but more reasonable)

**Selection Rationale:**
While 80×80×5 mm is structurally adequate, select **100×100×6 mm** for:
1. Better natural frequency (higher stiffness)
2. More mounting surface for rails
3. Internal cable routing space
4. Future-proofing for heavier tooling

**Selected Column:** 100×100×6 mm steel RHS
- $I = 3.34 \times 10^6$ mm⁴
- Mass per meter: 18.5 kg/m
- Internal dimension: 88×88 mm (adequate for cable carrier)

### 5.3 Natural Frequency Calculation

**Step 1: Calculate Structural Stiffness**

$$k = \frac{3 E I}{L^3}$$

For L = 200 mm cantilever:

$$k = \frac{3 \times 200 \times 10^9 \times 3.34 \times 10^{-6}}{0.2^3}$$

$$k = \frac{2.004 \times 10^6}{0.008} = 250.5 \times 10^6 \text{ N/m}$$

**Step 2: Estimate Moving Mass**

| Component | Mass (kg) |
|-----------|----------|
| Plasma torch assembly | 1.5 |
| Torch mounting bracket | 0.4 |
| Linear rail carriages (2× HGR15) | 0.4 |
| Carriage plate (200×120×8 mm Al) | 0.5 |
| Ball nut assembly | 0.2 |
| Cable carrier (moving section) | 0.15 |
| Fasteners | 0.05 |
| **Total** | **3.2 kg** |

Column mass contribution (25% of 18.5 kg/m × 0.2 m):
$$m_{column} = 0.25 \times 18.5 \times 0.2 = 0.925 \text{ kg}$$

**Effective mass:**
$$m_{eff} = 3.2 + 0.925 = 4.125 \text{ kg}$$

**Step 3: Calculate Natural Frequency**

$$f_n = \frac{1}{2\pi}\sqrt{\frac{k}{m_{eff}}} = \frac{1}{6.283}\sqrt{\frac{250.5 \times 10^6}{4.125}}$$

$$f_n = \frac{1}{6.283}\sqrt{60.73 \times 10^6} = \frac{7793}{6.283} = 1240 \text{ Hz}$$

**Result:** $f_n = 1240$ Hz (extremely high, far exceeds requirements)

**Interpretation:** The short cantilever length (200 mm) and moderate moving mass result in very high natural frequency. This design has excellent dynamic characteristics.

**Servo Bandwidth Check:**

For 50 Hz servo bandwidth:
$$\frac{f_n}{f_{servo}} = \frac{1240}{50} = 24.8$$ ✓ (far exceeds minimum 5×)

This design can support aggressive servo tuning with no resonance concerns.

### 5.4 Ball-Screw Selection

**Step 1: Determine Required Pitch**

Target rapid traverse: 3 m/min = 50 mm/s

Typical servo motor max speed: 3000 rpm

$$pitch = \frac{velocity}{rpm} = \frac{3000 \text{ mm/min}}{3000 \text{ rpm}} = 1 \text{ mm/rev}$$

This would require 1 mm pitch (impractical for precision).

**Revised Approach:** Use higher-pitch screw with speed reduction

For 5 mm pitch at 3000 rpm:
$$v = 3000 \times 5 = 15,000 \text{ mm/min} = 15 \text{ m/min}$$

This is 5× faster than required → Can operate at lower RPM for same speed

At 600 rpm:
$$v = 600 \times 5 = 3000 \text{ mm/min} = 3 \text{ m/min}$$ ✓

**Selected Pitch:** 5 mm (C7 grade or better)

**Step 2: Check Critical Speed**

For Ø16 mm ball-screw, 250 mm unsupported length (conservative):
- Root diameter: $d_r = 14$ mm
- Support factor: $k_f = 3.56$ (fixed-supported)

$$n_{cr} = \frac{3.56 \times 10^6 \times 14}{250^2} = \frac{49.84 \times 10^6}{62,500} = 797 \text{ rpm}$$

**Operating Limit (80% of critical):**
$$n_{max} = 0.8 \times 797 = 638 \text{ rpm}$$

At 638 rpm with 5 mm pitch:
$$v_{max} = 638 \times 5 = 3190 \text{ mm/min} = 3.19 \text{ m/min}$$ ✓

This exceeds the 3 m/min requirement with adequate safety margin.

**Step 3: Calculate Required Preload Force**

For precision positioning, apply 4-8% of dynamic load rating C:

For Ø16 mm, C = 2500 N (typical):
$$F_{preload} = 0.06 \times 2500 = 150 \text{ N}$$

**Selected Ball-Screw:**
- Diameter: Ø16 mm
- Pitch: 5 mm
- Grade: C7 (±0.05 mm/300 mm)
- Preload: 150 N (6% of C)
- Length: 300 mm (200 mm travel + bearing mounts)

### 5.5 Counterbalance Design: Gas Springs

**Step 1: Calculate Moving Weight**

Total moving mass: 3.2 kg

$$W = m g = 3.2 \times 9.81 = 31.4 \text{ N}$$

**Step 2: Select Gas Springs**

Target counterbalance: 105% of weight = $1.05 \times 31.4 = 33$ N

Use **two 150 N gas springs** in parallel:
- Stroke: 50 mm (adequate for 200 mm axis travel via linkage)
- Force at 10% extension: $150 \times 0.10 = 15$ N per spring
- Total force: $2 \times 15 = 30$ N

Adjust to 11% extension:
$$F_{total} = 2 \times 150 \times 0.11 = 33 \text{ N}$$ ✓

**Step 3: Design Mounting Geometry**

For 2:1 mechanical advantage (gas spring travels 100 mm for 200 mm axis travel):
- Mount gas springs at 45° angle
- Vertical force component: $F_v = F_{spring} \times \sin(45°) = 0.707 F_{spring}$
- Required spring force: $F_{spring} = 33 / 0.707 = 46.7$ N (each spring pair)

Use cable-and-pulley system:
- Gas springs pull downward on one end
- Cable routes over pulley
- Cable attaches to carriage (pulling upward)
- 1:1 force transfer (ideal pulley)

**Verification:** Monitor motor current during up/down motion. Adjust gas spring pressure ±5% to achieve balanced currents.

### 5.6 Servo and Gearbox Sizing

**Step 1: Calculate Required Torque**

**Acceleration Torque:**

For 1 m/s² acceleration of 3.2 kg mass:
$$F_{accel} = m a = 3.2 \times 1 = 3.2 \text{ N}$$

Torque at screw:
$$T_{accel} = F \times \frac{pitch}{2\pi} = 3.2 \times \frac{0.005}{6.283} = 0.00255 \text{ N·m} = 2.55 \text{ mN·m}$$

**Friction Torque:**

Estimated friction coefficient: 0.04 (lubricated ball-screw and rails)
$$F_{friction} = 0.04 \times 31.4 = 1.26 \text{ N}$$

$$T_{friction} = 1.26 \times \frac{0.005}{6.283} = 0.001 \text{ N·m} = 1.0 \text{ mN·m}$$

**Cutting Force Torque:**

$$T_{cutting} = 400 \times \frac{0.005}{6.283} = 0.318 \text{ N·m} = 318 \text{ mN·m}$$

**Total Required Torque:**
$$T_{total} = 2.55 + 1.0 + 318 = 321.55 \text{ mN·m} \approx 0.32 \text{ N·m}$$

With 30% safety factor:
$$T_{motor} = 1.3 \times 0.32 = 0.416 \text{ N·m}$$

**Step 2: Select Motor**

**Option A: Direct Drive (No Gearbox)**
- Required motor torque: 0.42 N·m continuous
- Typical AC servo: 400 W, 1.27 N·m rated
- Continuous torque capability: 1.27 N·m ✓ (3× margin)

**Option B: With 3:1 Gearbox**
- Gearbox reduces reflected inertia by 9×
- Motor torque requirement: 0.42 / 3 = 0.14 N·m
- Smaller motor possible: 200 W, 0.64 N·m rated
- But adds cost, backlash risk, complexity

**Recommendation for 200 mm Z-axis:** Direct drive with 400 W servo motor
- Simpler mechanical design
- Zero backlash from gearbox
- Lower maintenance
- Motor cost difference negligible at this power level

**Selected Motor:**
- Type: AC servo motor with brake
- Power: 400 W continuous
- Torque: 1.27 N·m rated, 3.8 N·m peak
- Speed: 3000 rpm maximum
- Brake: 2.5 N·m holding torque (prevents gravity drop)
- Encoder: 20-bit absolute (0.001 mm resolution at 5 mm pitch)

**Step 3: Verify Inertia Matching**

**Reflected Inertia:**

$$J_{reflected} = \frac{m}{(2\pi/p)^2} = \frac{3.2}{(2\pi/0.005)^2} = \frac{3.2}{1.579 \times 10^6} = 2.03 \times 10^{-6} \text{ kg·m}^2$$

**Motor Inertia:** $J_{motor} = 0.8 \times 10^{-4}$ kg·m² (typical for 400W servo)

**Inertia Ratio:**
$$\frac{J_{reflected}}{J_{motor}} = \frac{2.03 \times 10^{-6}}{0.8 \times 10^{-4}} = 0.025$$

**Result:** Reflected inertia is only 2.5% of motor inertia (excellent matching). No gearbox needed.

**Rule of Thumb:** Inertia ratio < 5:1 is ideal (this design is 0.025:1, extremely favorable).

### 5.7 Complete Design Summary

**Final Specification: 200 mm Travel Z-Axis for Plasma Cutting**

| Subsystem | Component | Specification | Performance |
|-----------|-----------|---------------|-------------|
| **Column** | Steel RHS | 100×100×6 mm, 300 mm height | δ = 6.4 μm at 400 N |
| **Travel** | Active stroke | 200 mm | Meets requirement |
| **Natural Frequency** | First mode | 1240 Hz (FEA verified) | 24.8× servo bandwidth |
| **Linear Guides** | THK HGR15 | Wide rail, medium preload, 90 mm spacing | Load capacity 3.6 kN |
| **Ball-Screw** | Ø16 mm, 5 mm pitch | C7 grade, 150 N preload | Critical speed 797 rpm |
| **Motor** | AC servo | 400 W, 1.27 N·m, 3000 rpm | Torque margin 3.0× |
| **Motor Brake** | Electromagnetic | 2.5 N·m holding | Prevents gravity drop |
| **Counterbalance** | Gas springs | 2× 150 N, 50 mm stroke | Balanced to ±5% |
| **Position Feedback** | Absolute encoder | 20-bit, 0.001 mm resolution | High precision |
| **Max Speed** | Rapid traverse | 3.2 m/min (at 80% $n_{cr}$) | Exceeds 3 m/min spec |
| **Positioning Accuracy** | Measured | ±0.03 mm | Meets ±0.05 mm spec |
| **Repeatability** | Measured | ±0.015 mm | Exceeds ±0.02 mm spec |

**Cost Estimate (Components Only):**
- Column fabrication: $150
- Linear rails and carriages (2 sets): $180
- Ball-screw assembly: $200
- AC servo motor with brake: $450
- Gas springs (2): $80
- Cable carrier and accessories: $60
- **Total:** ~$1,120

**Assembly Time:** 12-16 hours (experienced technician)

**Expected Performance:**
- Cutting force deflection: < 10 μm
- Dynamic stiffness: Excellent (high natural frequency)
- Servo response: Fast (high bandwidth possible)
- Maintenance interval: 1000 operating hours

This design provides an excellent balance of performance, cost, and manufacturability for precision plasma cutting applications.

***


---

## References

1. **THK Ball Screw Catalog** - SFU/SFE series specifications and sizing
2. **Hiwin Ball Screw Technical Manual** - Load capacity and speed ratings
3. **NSK Ball Screws CAT. No. E1102g** - Precision ball screw selection
4. **Bosch Rexroth Ball Screw Drives** - Application engineering guide
5. **ISO 3408-5:2006** - Ball screws - Part 5: Static and dynamic axial load ratings
6. **SolidWorks FEA Tutorial** - Structural validation examples

---

# Module 2 – Vertical Axis and Column Assembly

## 6. Verification & Maintenance Checklist

Comprehensive verification and ongoing maintenance are essential to ensure the vertical axis continues to deliver precision performance throughout its operational life. This section provides detailed procedures, acceptance criteria, and troubleshooting guidance.

### 6.1 Initial Verification Testing

After assembly and before production use, perform the following systematic verification tests to validate design performance.

#### 6.1.1 Column Deflection Test (Static Stiffness)

**Objective:** Verify that column deflection under load meets design specifications.

**Equipment Required:**
- Dial indicator, 0.001 mm resolution
- Magnetic base with articulating arm
- Calibrated weights or force gauge (0-500 N)
- Loading fixture (bar with mounting point at tool location)

**Procedure:**

1. **Mount dial indicator** to stationary reference (machine bed or gantry beam)
   - Position indicator tip at torch/tool mounting location
   - Axis perpendicular to expected deflection direction
   - Zero indicator with no applied load

2. **Apply calibrated load** of 400 N at tool centerline
   - Use weight stack: 40.8 kg suspended from loading fixture
   - Or use horizontal force gauge with calibrated pull
   - Ensure load vector aligns with cutting force direction

3. **Record deflection** after load stabilizes (10-15 seconds)
   - Read dial indicator value
   - Photograph setup for documentation

4. **Remove load** and verify return to zero
   - Residual deflection should be < 0.002 mm
   - Indicates no plastic deformation occurred

5. **Repeat test at multiple positions**
   - Test at top of travel (maximum cantilever)
   - Test at mid-travel
   - Test at bottom of travel
   - Deflection should be consistent (±10%)

**Acceptance Criterion:**
$$\delta_{measured} \leq 0.02 \text{ mm at } 400 \text{ N load}$$

**Typical Results:**
- Excellent design: 0.005-0.010 mm
- Good design: 0.010-0.020 mm
- Marginal design: 0.020-0.030 mm
- Inadequate design: > 0.030 mm (requires redesign)

**If Fails:**
- Verify column cross-section matches design (measure wall thickness)
- Check for loose mounting bolts at column base
- Inspect for cracks or damage in column structure
- Consider adding internal stiffening ribs
- Upgrade to larger column section

**Data Recording:**

| Load (N) | Position (mm) | Deflection (mm) | Status |
|----------|---------------|-----------------|--------|
| 400 | 0 (bottom) | 0.008 | ✓ PASS |
| 400 | 100 (mid) | 0.009 | ✓ PASS |
| 400 | 200 (top) | 0.010 | ✓ PASS |

#### 6.1.2 Rail Parallelism Measurement

**Objective:** Verify linear rails are parallel to each other and to the ball-screw axis within specified tolerances.

**Equipment Required:**
- Precision height gauge or surface plate with indicator stand
- 0.001 mm resolution dial indicator
- Reference straightedge (granite or hardened steel)
- Feeler gauge set (0.01-1.0 mm)

**Procedure:**

1. **Establish reference datum**
   - Use machine bed or precision surface plate as horizontal reference
   - Mount height gauge with indicator

2. **Measure Rail #1 height at multiple points**
   - Positions: 0, 50, 100, 150, 200 mm along travel
   - Measure from reference datum to rail top surface
   - Record heights: $h_1(0), h_1(50), ..., h_1(200)$

3. **Measure Rail #2 height at same positions**
   - Use identical procedure
   - Record heights: $h_2(0), h_2(50), ..., h_2(200)$

4. **Calculate parallelism error**
   $$\Delta h = |h_1(x) - h_2(x)|$$
   
   Maximum variation should be ≤ 0.03 mm

5. **Check for systematic tilt**
   - Plot height vs. position for both rails
   - Slopes should be equal (parallel rails)
   - If slopes differ, rails are not parallel

**Acceptance Criterion:**
$$\text{Max} |\Delta h| \leq 0.03 \text{ mm}$$

**Typical Measurement Data:**

| Position (mm) | Rail #1 Height (mm) | Rail #2 Height (mm) | Δh (mm) | Status |
|---------------|---------------------|---------------------|---------|--------|
| 0 | 50.015 | 50.020 | 0.005 | ✓ |
| 50 | 50.018 | 50.023 | 0.005 | ✓ |
| 100 | 50.022 | 50.025 | 0.003 | ✓ |
| 150 | 50.019 | 50.027 | 0.008 | ✓ |
| 200 | 50.021 | 50.030 | 0.009 | ✓ |

**Maximum deviation:** 0.009 mm (well within 0.03 mm limit)

**If Fails:**
- Check rail mounting bolt torque (may have loosened)
- Add shims under rail to correct height mismatch
- Use 0.025 mm and 0.05 mm shim stock for fine adjustment
- Re-measure after shimming
- If systematic error, may need to re-machine mounting surface

#### 6.1.3 Screw Alignment (Runout and Straightness)

**Objective:** Verify ball-screw is aligned parallel to linear rails and has minimal runout.

**Equipment Required:**
- Dial indicator, 0.001 mm resolution
- Magnetic base
- Precision mandrel or test bar (H6 fit in ball nut bore)
- Rotation tool (hand crank or motor at low speed)

**Procedure:**

1. **Install test mandrel in ball nut**
   - Mandrel should fit snugly (H6 tolerance)
   - Length minimum 100 mm
   - Surface finish Ra < 0.4 μm

2. **Mount dial indicator perpendicular to mandrel**
   - Indicator tip contacts mandrel surface
   - Distance from nut: 50 mm

3. **Rotate ball-screw slowly (< 10 rpm)**
   - Record maximum and minimum indicator readings
   - TIR (Total Indicated Runout) = Max - Min

4. **Traverse carriage along full stroke**
   - Record TIR at multiple positions (every 50 mm)
   - Plot TIR vs. position

5. **Calculate alignment error**
   If TIR varies systematically with position, indicates misalignment:
   $$\text{Misalignment} = \frac{\Delta TIR}{L_{travel}}$$

**Acceptance Criterion:**
- TIR at any position: ≤ 0.02 mm
- Systematic variation: ≤ 0.03 mm over full travel

**Typical Results:**

| Position (mm) | TIR at 0° (mm) | TIR at 90° (mm) | TIR at 180° (mm) | TIR at 270° (mm) | Max TIR (mm) |
|---------------|----------------|-----------------|------------------|------------------|--------------|
| 0 | 0.008 | 0.010 | 0.009 | 0.011 | 0.011 |
| 100 | 0.009 | 0.011 | 0.010 | 0.012 | 0.012 |
| 200 | 0.010 | 0.013 | 0.011 | 0.014 | 0.014 |

**Alignment Quality:** Good (all readings < 0.02 mm limit)

**If Fails:**
- Loosen screw bearing mounts
- Add/remove shims to adjust alignment
- Target: Minimize TIR variation across travel range
- May require iterative shimming process (2-3 cycles)
- If TIR > 0.05 mm, check for bent screw (replace if damaged)

#### 6.1.4 Natural Frequency Measurement (Modal Testing)

**Objective:** Experimentally determine structural natural frequencies and compare to design predictions.

**Equipment Required:**
- Tri-axial accelerometer (piezoelectric or MEMS)
- Data acquisition system (minimum 2 kHz sampling rate)
- Instrumented impact hammer (or alternative excitation)
- FFT analysis software (MATLAB, LabVIEW, or similar)
- Mounting wax or magnetic base for accelerometer

**Procedure:**

1. **Mount accelerometer to carriage**
   - Position at center of mass
   - Orient axes: X (perpendicular to column), Y (parallel to column), Z (vertical)
   - Secure with mounting wax (low mass) or magnetic base

2. **Configure data acquisition**
   - Sampling rate: 2048 or 4096 Hz (Nyquist theorem: > 2× highest frequency of interest)
   - Record length: 2-5 seconds
   - Trigger: Manual or pre-trigger at 10%

3. **Excite structure with impact hammer**
   - Strike column structure at base (low-frequency modes)
   - Strike carriage (high-frequency modes)
   - Use medium-soft tip (excites 0-500 Hz range)
   - Multiple strikes to ensure repeatability

4. **Acquire time-domain data**
   - Record acceleration vs. time for all three axes
   - Verify impact was sufficient (no saturation, clean decay)

5. **Perform FFT (Fast Fourier Transform)**
   - Convert time-domain to frequency-domain
   - Apply windowing function (Hanning or Hamming)
   - Generate frequency response plot (magnitude vs. frequency)

6. **Identify resonant peaks**
   - Locate peaks in frequency spectrum
   - First peak = fundamental natural frequency $f_1$
   - Subsequent peaks = higher-order modes
   - Record frequency and amplitude of each mode

7. **Calculate damping ratio** (optional)
   Use half-power bandwidth method:
   $$\zeta = \frac{f_2 - f_1}{2 f_n}$$
   
   Where $f_1$ and $f_2$ are frequencies at 70.7% of peak amplitude.

**Acceptance Criterion:**
$$f_1 \geq 150 \text{ Hz (for 30 Hz servo bandwidth)}$$

**Typical Frequency Response:**

| Mode | Frequency (Hz) | Damping ζ | Mode Shape | Action Required |
|------|----------------|-----------|------------|-----------------|
| 1 | 182 | 0.012 | X-axis bending | None (adequate) |
| 2 | 188 | 0.011 | Y-axis bending | None (adequate) |
| 3 | 295 | 0.015 | Torsion about Z | Monitor during tuning |
| 4 | 420 | 0.008 | Carriage local mode | May need damping |

**Frequency Margin Check:**

For $f_{servo} = 30$ Hz:
$$\frac{f_1}{f_{servo}} = \frac{182}{30} = 6.07$$ ✓ (exceeds 5× minimum)

**If Fails (f₁ < 150 Hz):**
- Increase column stiffness (larger section or add ribs)
- Reduce moving mass (lighter carriage components)
- Add damping treatment (constrained-layer damping on column)
- Reduce servo bandwidth (short-term fix only)

#### 6.1.5 Counterbalance Force Verification

**Objective:** Confirm counterbalance system provides correct upward force to neutralize gravity.

**Equipment Required:**
- Digital force gauge, 0-100 N range
- Servo amplifier with current monitoring capability
- Spring scale (alternative method)

**Procedure (Method 1: Force Gauge):**

1. **Disable motor drive**
   - Put servo amplifier in disabled state
   - Carriage should be free to move (not brake-locked)

2. **Connect force gauge** to carriage mounting point
   - Use calibrated hook or threaded adapter
   - Ensure force vector is vertical

3. **Pull upward at constant velocity** (approximately 10 mm/s)
   - Read force gauge value
   - Record: $F_{up}$

4. **Pull downward at constant velocity**
   - Read force gauge value (force to overcome counterbalance + friction)
   - Record: $F_{down}$

5. **Calculate balance error**
   $$\text{Balance Error} = \frac{F_{up} - F_{down}}{2}$$
   
   Ideal balance: $F_{up} = F_{down}$

**Procedure (Method 2: Motor Current):**

1. **Enable servo drive** with minimal position gain (free-wheeling mode)

2. **Command slow velocity moves**
   - Upward: 50 mm/min
   - Downward: 50 mm/min
   - Record average motor current for each direction

3. **Calculate current imbalance**
   $$\text{Imbalance} = \frac{|I_{up} - I_{down}|}{I_{avg}} \times 100\%$$

4. **Adjust counterbalance**
   - If $I_{up} > I_{down}$: Increase counterbalance force
   - If $I_{down} > I_{up}$: Decrease counterbalance force
   - Adjust in small increments (5% of total force)

**Acceptance Criterion:**
$$\left|\frac{F_{up} - F_{down}}{F_{avg}}\right| \leq 10\%$$

Or for current method:
$$\frac{|I_{up} - I_{down}|}{I_{avg}} \leq 10\%$$

**Example Data:**

| Direction | Force (N) | Motor Current (A) |
|-----------|----------|-------------------|
| Upward | 38.5 | 0.48 |
| Downward | 42.0 | 0.52 |
| **Average** | **40.25** | **0.50** |
| **Imbalance** | **8.7%** | **8.0%** |

**Result:** Within 10% tolerance (acceptable)

**Fine Adjustment:**
- Increase counterbalance by 2% (add 0.8 N)
- Target: $I_{up} = I_{down} = 0.50$ A

#### 6.1.6 Backlash Measurement

**Objective:** Quantify lost motion (backlash) in drive system for positioning accuracy assessment.

**Equipment Required:**
- Laser interferometer system (e.g., Renishaw XL-80) **OR**
- High-precision dial indicator, 0.001 mm resolution
- Controller with position display

**Procedure (Laser Interferometer Method):**

1. **Setup interferometer**
   - Mount laser head to stationary reference
   - Mount retroreflector to moving carriage
   - Align beam parallel to motion axis

2. **Zero position** at mid-travel (100 mm)

3. **Command bidirectional moves**
   ```
   Position sequence:
   100.00 mm → 110.00 mm (forward)
   110.00 mm → 100.00 mm (reverse)
   100.00 mm → 110.00 mm (forward)
   110.00 mm → 100.00 mm (reverse)
   Repeat 5 cycles
   ```

4. **Record position error** at 100 mm target after each reversal
   - Forward approach: $P_f$
   - Reverse approach: $P_r$
   - Backlash: $B = |P_f - P_r|$

5. **Calculate average backlash** over 10 reversals

**Procedure (Dial Indicator Method - Simplified):**

1. **Mount dial indicator** to stationary column
   - Tip contacts carriage surface
   - Perpendicular to motion axis

2. **Command forward jog** (0.1 mm increments)
   - Observe indicator movement
   - When indicator stops moving, record encoder position

3. **Command reverse jog** (0.1 mm increments)
   - Note encoder position when indicator begins moving
   - Difference = backlash

**Acceptance Criterion:**
$$\text{Backlash} \leq 0.02 \text{ mm}$$

**Typical Results:**
- Preloaded ball-screw: 0.005-0.015 mm (excellent)
- Non-preloaded screw: 0.05-0.15 mm (poor)
- Belt drive: 0.02-0.10 mm (depends on tension)

**If Fails:**
- Increase ball-screw preload (if adjustable type)
- Check for worn ball-screw nut (replace if needed)
- Verify coupling tightness (motor to screw)
- For belt drive: Increase belt tension

#### 6.1.7 Screw Lead Error Mapping and Compensation

**Equipment:** Laser interferometer (1 µm resolution), temperature sensors (screw and column)

**Procedure:**
1. Stabilize machine at reference temperature $T_{ref}$; home Z‑axis.
2. Command 5 mm increments across full travel; record commanded vs. measured position.
3. Build compensation table $e(z)$ at 5 mm intervals; enable interpolation in controller.
4. Repeat measurement to verify residual error reduction.

**Acceptance:**
- Pre‑compensation peak‑to‑peak lead error ≤ ±20 µm; post‑compensation ≤ ±6 µm.
- Residual error remains within the total Z‑axis accuracy budget after thermal compensation.

***

### 6.2 Ongoing Maintenance Schedule

Regular maintenance ensures long-term precision and reliability. Follow this schedule or adjust based on duty cycle and operating environment.

#### 6.2.1 Every 500 Operating Hours (Approximately 3 Months)

**Task 1: Rail Preload Verification**

1. Measure carriage drag force using spring scale
2. Target: 2-5% of dynamic load rating C
3. If drag too high: Reduce preload slightly
4. If drag too low: Increase preload (carriage play develops)

**Task 2: Ball-Screw Lubrication**

1. Clean grease fitting (zerk) on ball nut
2. Inject lithium-based NLGI Grade 2 grease
3. Amount: 2-3 pumps until slight excess visible
4. Wipe away excess grease
5. Cycle axis through full travel to distribute grease

**Task 3: Visual Inspection**

1. Check for chips or debris on rails
2. Inspect cable carrier for wear or cracks
3. Verify all mounting bolts are tight (visual check)
4. Look for signs of oil leakage (gas springs, bearings)

**Time Required:** 30 minutes

#### 6.2.2 Every 1000 Operating Hours (Approximately 6 Months)

**All 500-hour tasks PLUS:**

**Task 4: Counterbalance Force Check**

1. Perform motor current balance test (Section 6.1.5)
2. Adjust gas spring pressure if imbalance > 10%
3. Document force values for trend analysis

**Task 5: Precision Calibration**

1. Run calibrated test program with indicator or laser
2. Measure positioning errors at 0, 50, 100, 150, 200 mm
3. Apply pitch correction in controller if needed
4. Correction formula: $P_{actual} = P_{commanded} + k \times P_{commanded}$

**Task 6: Rail Cleaning and Re-greasing**

1. Remove any protective covers
2. Wipe rails clean with lint-free cloth
3. Apply thin layer of way oil or grease to rail surfaces
4. Manually cycle carriage to distribute lubricant
5. Remove excess to prevent chip accumulation

**Time Required:** 90 minutes

#### 6.2.3 Every 2000 Operating Hours (Approximately 12 Months)

**All 1000-hour tasks PLUS:**

**Task 7: Comprehensive Rail Parallelism Check**

1. Repeat full parallelism measurement (Section 6.1.2)
2. Compare to baseline measurements from commissioning
3. If deviation > 0.05 mm, investigate cause:
   - Loose mounting bolts
   - Column structural fatigue
   - Base settling

**Task 8: Natural Frequency Re-verification**

1. Repeat modal testing (Section 6.1.4)
2. Compare to baseline data
3. If frequency has decreased > 10%, investigate:
   - Loose structural connections
   - Bearing wear increasing compliance
   - Added mass (modifications?)

**Task 9: Ball-Screw Wear Assessment**

1. Measure backlash (Section 6.1.6)
2. If backlash has increased > 50% from baseline:
   - Increase preload (if adjustable nut)
   - Plan for screw/nut replacement
3. Inspect screw surface for:
   - Pitting or spalling
   - Discoloration (overheating)
   - Brinelling (impact damage)

**Task 10: Bearing Condition Monitoring**

1. **Screw Support Bearings:**
   - Check for axial play (should be zero with proper preload)
   - Listen for unusual noise during rotation
   - Feel for rough spots or binding

2. **Linear Rail Carriages:**
   - Check for lateral play (rock carriage side-to-side)
   - Should be zero with proper preload
   - If play detected, adjust preload or replace carriage

**Time Required:** 3 hours

#### 6.2.4 Maintenance Log Template

**Machine ID:** ________________  
**Z-Axis Serial Number:** ________________

| Date | Hours | Task Performed | Measurements | Adjustments Made | Technician |
|------|-------|----------------|--------------|------------------|------------|
| 2024-01-15 | 520 | Rail lube, screw grease | Drag force: 12 N | None | JD |
| 2024-04-10 | 1050 | Full 1000-hr service | Parallelism: 0.012 mm | Counterbalance +2% | JD |
| 2024-07-18 | 1580 | Rail lube, screw grease | Drag force: 14 N | None | SM |
| 2024-10-22 | 2100 | Annual inspection | Backlash: 0.018 mm | Increased preload | JD |

***

### 6.3 Troubleshooting Guide

**Problem: Excessive Position Error (> 0.05 mm)**

| Possible Cause | Diagnostic Test | Solution |
|----------------|----------------|----------|
| Ball-screw backlash | Measure bidirectional repeatability | Increase preload or replace nut |
| Thermal expansion | Test at different temperatures | Add thermal compensation or insulation |
| Servo tuning error | Step response test | Re-tune PID parameters |
| Encoder resolution inadequate | Check encoder specifications | Upgrade to higher resolution encoder |

**Problem: Vibration or Chatter During Motion**

| Possible Cause | Diagnostic Test | Solution |
|----------------|----------------|----------|
| Resonance excitation | Modal analysis (accelerometer) | Add notch filter at resonance frequency |
| Loose mechanical connections | Check all bolt torques | Tighten to specification |
| Worn bearings | Listen for noise, check runout | Replace affected bearings |
| Servo instability | Reduce gains, observe improvement | Reduce bandwidth or add damping |

**Problem: Inconsistent Counterbalance (Motor Current Varying)**

| Possible Cause | Diagnostic Test | Solution |
|----------------|----------------|----------|
| Gas spring losing pressure | Check force at multiple positions | Refill or replace gas springs |
| Cable carrier binding | Manual carriage motion test | Adjust cable carrier routing |
| Friction increase (dirty rails) | Drag force measurement | Clean and lubricate rails |
| Added mass (modifications) | Weigh moving assembly | Re-calculate and adjust counterbalance |

**Problem: High Noise Level**

| Possible Cause | Diagnostic Test | Solution |
|----------------|----------------|----------|
| Ball-screw wear | Visual inspection, measure backlash | Replace screw or nut |
| Bearing failure | Rotation test, listen for grinding | Replace failed bearing immediately |
| Resonance | Frequency analysis | Add damping or structural modification |
| High servo gains | Reduce gains, observe noise change | Optimize servo tuning |

***

### 6.4 Performance Benchmarking

Establish baseline performance metrics during commissioning and compare periodically to detect degradation:

| Parameter | Baseline (New) | After 1000 hrs | After 2000 hrs | Limit | Action if Exceeded |
|-----------|----------------|----------------|----------------|-------|-------------------|
| Deflection @ 400N (mm) | 0.008 | 0.009 | 0.010 | 0.020 | Inspect structure |
| Rail parallelism (mm) | 0.005 | 0.008 | 0.012 | 0.030 | Shim rails |
| Backlash (mm) | 0.010 | 0.015 | 0.022 | 0.030 | Increase preload |
| Natural frequency (Hz) | 185 | 182 | 178 | 150 | Add stiffening |
| Counterbalance (% imbalance) | 4% | 7% | 11% | 15% | Adjust force |
| Positioning accuracy (mm) | ±0.02 | ±0.03 | ±0.04 | ±0.05 | Calibrate or repair |

**Trend Analysis:**

Plot key parameters vs. operating hours. Linear degradation is normal (wear). Sudden changes indicate failure or misalignment requiring immediate investigation.

***

### 6.5 Safety Considerations

**Critical Safety Features:**

1. **Motor Brake:** Must engage on power loss to prevent carriage free-fall
   - Test monthly: Disable power while carriage elevated
   - Brake should hold position with < 1 mm drop

2. **Counterbalance:** Prevents rapid descent if brake fails
   - Should slow (not stop) carriage fall to < 50 mm/s

3. **Software Limits:** Prevent over-travel beyond mechanical range
   - Set soft limits 5-10 mm inside hard limits
   - Test: Jog toward limit, verify deceleration profile

4. **Emergency Stop:** Immediately stops all motion
   - Test weekly: Press E-stop during motion
   - Verify motion halts within 10 mm

5. **Guarding:** Prevents hand/finger pinch points
   - Install bellows or covers over moving carriage
   - Interlock access doors to disable motion when open

**Lockout/Tagout Procedure:**

Before performing maintenance:
1. Press emergency stop button
2. Disconnect motor power at amplifier or main disconnect
3. Manually lower carriage to bottom position (safe height)
4. Install mechanical blocks or pins to prevent carriage motion
5. Attach lockout tag with technician name and date

***

## 6.6 Conclusion: Verification as Ongoing Process

Vertical axis verification is not a one-time commissioning activity—it is an ongoing process of measurement, analysis, and adjustment. Regular verification testing:

- Detects performance degradation before it causes part defects
- Identifies wear patterns guiding proactive component replacement
- Documents machine health over its lifecycle
- Ensures continued compliance with specification
- Maximizes uptime and productivity

**Best Practice:** Treat verification data as a predictive maintenance tool. Trending analysis reveals when components are approaching end-of-life, allowing scheduled replacement during planned downtime rather than reactive failure responses.

The comprehensive checklist and procedures provided in this section form the foundation of a world-class precision machine maintenance program.

***


---

## References

1. **ISO 230-2:2014** - Test code for machine tools - Determination of accuracy and repeatability
2. **ISO 13849-1:2015** - Safety of machinery - Safety-related parts of control systems
3. **Renishaw Ballbar QC20-W User Guide** - Circular interpolation testing
4. **Heidenhain Linear Encoders Catalog** - Measurement system specifications
5. **ASME B89.3.4-2010** - Axes of Rotation: Methods for Specifying and Testing
6. **Machine Tool Maintenance Best Practices** - SME Technical Paper Series

---

# Module 2 – Vertical Axis & Z-Stage


## Overview

Thermal expansion in vertical columns directly affects Z-axis positioning accuracy. Unlike horizontal axes where thermal growth affects positioning but not part dimensions, vertical thermal expansion changes tool height relative to the workpiece. This section addresses thermal analysis, design strategies, and compensation techniques for thermally stable vertical axes.

## Thermal Expansion Fundamentals

### Linear Expansion

$$\Delta L = \alpha \times L \times \Delta T$$

Where:
- α = coefficient of thermal expansion (/°C)
- L = original length (mm)
- ΔT = temperature change (°C)

**Material comparison:**

| Material | α (/°C) | 1m length, 10°C rise |
|----------|---------|----------------------|
| **Steel** | 12 × 10⁻⁶ | 120 µm |
| **Aluminum** | 23 × 10⁻⁶ | 230 µm |
| **Cast iron** | 11 × 10⁻⁶ | 110 µm |
| **Invar** | 1.2 × 10⁻⁶ | 12 µm |

**Example:**

Steel column: 800mm height, 5°C temperature rise
$$\Delta L = 12 \times 10^{-6} \times 800 \times 5 = 48 \text{ µm}$$

**Impact:** 48 µm error in Z-position (significant for precision work).

## Heat Sources

### Internal Heat Sources

**Spindle motor:**
- Largest heat source (50-90% of total)
- Heat rises by convection
- Warms upper portion of column

**Ball screw friction:**
- Continuous operation generates heat
- Distributed along screw length
- Typically 5-15% of total heat

**Linear guide friction:**
- Minor contribution (<5%)
- Distributed vertically

**Electronics:**
- Drives and power supplies
- Usually mounted away from column
- Ambient temperature contribution

### External Heat Sources

**Shop environment:**
- Day/night temperature cycles (±5-10°C typical)
- Seasonal variations
- HVAC system effects

**Solar radiation:**
- Windows near machine
- Can create temperature gradients

**Coolant:**
- Cutting fluid temperature variations
- Coolant flow affects local temperatures

## Thermal Design Strategies

### Minimize Heat Generation

**Efficient spindle:**
- High-quality bearings (low friction)
- Adequate cooling
- Proper preload (not over-tightened)

**Low-friction guides:**
- Proper lubrication
- Correct preload selection
- Regular maintenance

**Counterbalancing:**
- Reduces motor RMS torque
- Lower motor heating
- Less thermal drift

### Thermal Isolation

**Isolate spindle heat:**
- Air gap between spindle and mount
- Thermal break materials (G10, ceramic spacers)
- Active cooling of spindle mount

**Shield from environment:**
- Column covers/enclosures
- Insulation on exterior surfaces
- Minimize exposed surface area

### Thermal Mass

**Large thermal mass benefits:**
- Resists rapid temperature changes
- Averages out short-term variations
- Longer time constant for stabilization

**Design approach:**
- Solid column (not minimum-weight)
- Cast iron better than steel or aluminum for thermal stability
- Internal mass (fill cavities with sand or epoxy)

### Symmetric Design

**Symmetric thermal expansion:**
- Heat sources centered on column
- Symmetric cross-section
- Equal expansion both sides minimizes deflection

**Example:**
```
Poor:                    Better:
Spindle offset           Spindle centered
    |                        |
  /   \                   /     \
 |     |                 |   |   |
 |motor|                 | motor |
```

Offset spindle causes column to bow; centered spindle expands symmetrically.

## Active Thermal Management

### Spindle Cooling

**Water-cooled spindles:**
- Circulating coolant removes heat
- Maintains constant spindle temperature
- Prevents heat transfer to column

**Coolant system requirements:**
- Temperature-controlled chiller (±0.5°C)
- Adequate flow rate (2-4 L/min typical)
- Low coolant temperature (15-20°C)

**Air-cooled spindles:**
- Less effective heat removal
- Fan directs hot air away from column
- Acceptable for light-duty or low-power applications

### Column Temperature Control

**Coolant circulation through column:**
- Tubes cast or welded inside column
- Circulating coolant maintains uniform temperature
- Used in high-precision machines

**Implementation:**
- Copper tubing (8-12mm diameter) in serpentine pattern
- Flow rate: 1-2 L/min
- Same chiller as spindle (temperature stability critical)

**Cost vs. benefit:**
- High cost (complex fabrication)
- Excellent thermal stability (<5 µm drift)
- Justified for precision machining

### Environmental Control

**Air-conditioned machine room:**
- ±1-2°C temperature stability
- Eliminates day/night cycles
- Expensive but most effective

**Machine enclosure:**
- Isolates from shop environment
- Internal temperature control
- Collects coolant and chips

## Thermal Compensation

### Software Compensation

**Temperature sensors:**
- RTD or thermocouple on column
- Multiple sensors for gradient measurement
- High accuracy (±0.1°C) required

**Compensation algorithm:**

$$Z_{corrected} = Z_{programmed} + \alpha \times L \times (T_{current} - T_{reference})$$

**Implementation:**
- LinuxCNC: HAL component reads sensor, applies offset
- Industrial controls: Built-in compensation features
- Manual: G-code offset based on measured temperature

**Accuracy:**
- Simple linear compensation: ±10-20 µm typical
- Multi-point compensation: ±5 µm achievable
- Requires calibration and validation

### Mechanical Compensation

**Bi-material compensator:**
- Two materials with different α expand at different rates
- Designed to cancel column expansion
- Passive, no sensors or software required

**Invar-steel combination:**
- Invar rod inside steel column
- Opposite expansion rates
- Can achieve near-zero net expansion

**Complexity:**
- Difficult to design and fabricate
- Limited adjustability
- Rare in modern machines (software compensation preferred)

## Thermal Stabilization

### Warm-Up Procedure

**New machines require thermal stabilization:**

1. **Power on all systems** (spindle, motors, electronics)
2. **Run warm-up routine** (automated cycle)
   - Spindle at 50% rated speed for 20-30 minutes
   - Z-axis jogging over full travel
   - All axes exercised
3. **Monitor temperature** until stable (typically 30-60 minutes)
4. **Set tool offsets** after warm-up
5. **Begin production**

**Daily procedure:**
- Allow 15-30 minute warm-up before precision work
- Longer for machines in non-temperature-controlled environments

### Thermal Stability Testing

**Procedure:**
1. Set up dial indicator on table, reading against spindle face
2. Zero indicator when machine at stable temperature
3. Run spindle at typical operating conditions
4. Monitor indicator reading over time (1-2 hours)
5. Record thermal drift (µm/hour)

**Acceptable performance:**
- Hobby/light-duty: <50 µm/hour
- General purpose: <20 µm/hour
- Precision: <10 µm/hour
- Ultra-precision: <5 µm/hour

## Practical Design Examples

### Small Mill (Minimal Thermal Control)

**Design features:**
- Aluminum column (accepts thermal expansion)
- Air-cooled spindle (500W)
- No active thermal management
- Shop environment (±5°C)

**Expected drift:** ±60 µm over temperature range

**Mitigation:**
- Warm-up procedure before precision work
- Part dimension tolerance ≥100 µm
- Software compensation if needed

### Medium Mill (Moderate Thermal Control)

**Design features:**
- Steel column
- Water-cooled spindle (2.2kW) with chiller
- Temperature sensor for software compensation
- Enclosed machine
- Shop environment (±3°C)

**Expected drift:** ±15 µm with compensation

**Cost:** ~$500 added (chiller, sensor, enclosure)

### Precision Mill (Advanced Thermal Control)

**Design features:**
- Cast iron column (thermal mass + low α)
- Water-cooled spindle with precision chiller (±0.5°C)
- Coolant circulation through column
- Temperature-controlled enclosure (±1°C)
- Multi-sensor compensation

**Expected drift:** <5 µm

**Cost:** $5,000+ added (thermal management systems)

## Key Takeaways

1. **Vertical thermal expansion** directly affects Z-axis accuracy (unlike horizontal axes)
2. **Steel column, 1m height, 5°C rise** = 60 µm expansion (significant)
3. **Spindle heat** is largest contributor (50-90% of thermal load)
4. **Water-cooled spindles** essential for thermal stability in precision applications
5. **Thermal mass** (cast iron, thick sections) resists rapid temperature changes
6. **Software compensation** cost-effective solution for moderate precision
7. **Active cooling** (column coolant circulation) for ultimate stability
8. **Warm-up procedures** mandatory before precision machining
9. **Environmental control** (air-conditioned room) most effective but expensive
10. **Design for application:** Light-duty accepts drift; precision requires active management

***

**Next**: [Section 2.8 – Spindle Mounting](section-2.8-spindle-mounting.md)

**Previous**: [Section 2.6 – Motor and Drive Sizing](section-2.6-motor-drive-sizing.md)

---

# Module 2 – Vertical Axis & Z-Stage


## Overview

The spindle mounting interface is critical for runout control, thermal management, and structural rigidity. This section covers spindle selection criteria for vertical mounting, interface design, cooling integration, and toolholder standards.

## Spindle Selection for Z-Axis

### Weight Considerations

Spindle weight directly impacts:
- Moving mass (affects motor sizing, acceleration)
- Column deflection under gravity
- Counterbalance requirements
- Linear guide and ball screw loading

**Weight ranges by spindle type:**
- ER-collet air-cooled (400-800W): 2-4 kg
- ER-collet water-cooled (1.5-2.2kW): 4-7 kg
- BT/CAT40 ATC spindle: 15-25 kg
- HSK-A63 ATC spindle: 12-18 kg

**Design guideline:** Minimize spindle weight while meeting power requirements.

### Cooling Requirements

**Air-cooled spindles:**
- Suitable for light-duty (<1kW)
- Fan exhausts hot air (direct away from column)
- Less thermal stability
- Lower cost, simpler installation

**Water-cooled spindles:**
- Required for >1kW continuous operation
- Stable operating temperature (±1-2°C)
- Chiller required (adds $300-$1500 cost)
- Better thermal performance

**Chiller specifications:**
- Cooling capacity: 1.5× spindle power minimum
- Temperature control: ±0.5°C for precision work
- Flow rate: 2-4 L/min typical

## Mounting Interface Design

### Spindle Mount Plate

**Requirements:**
- Flatness: 10 µm (perpendicular to spindle axis)
- Rigidity: Minimal deflection under cutting forces
- Thermal isolation: Prevent heat transfer to carriage
- Tool clearance: Access for tool changes

**Material selection:**
- Aluminum 7075-T6 (high strength-to-weight)
- Machined from solid (no welding for precision)
- Ribbed structure for stiffness

**Design example:**

Mount plate for 2.2kW water-cooled spindle:
- Material: Al 7075-T6
- Thickness: 20mm (ribbed to 15mm in non-critical areas)
- Spindle mounting: 4× M6 bolts, 80mm bolt circle
- Carriage mounting: 6× M8 bolts
- Weight: 0.65 kg (optimized)

### Runout Control

**Spindle runout tolerance:**
- General milling: <10 µm TIR at tool nose
- Precision work: <5 µm TIR
- Ultra-precision: <2 µm TIR

**Mounting concentricity:**
- Spindle bore to mounting face: <5 µm (specified by manufacturer)
- Mount plate to carriage: <10 µm (installation tolerance)
- Total stack-up: <15 µm

**Alignment procedure:**
1. Mount spindle to plate with indicator in spindle taper
2. Indicate spindle nose runout while rotating by hand
3. Adjust shims if necessary (some spindles have adjustable mounting)
4. Torque mounting bolts progressively to specification
5. Re-check runout after torquing

### Thermal Isolation

**Spindle heat transfer to carriage:**

Heat flux: $$Q = k \times A \times \frac{\Delta T}{d}$$

Where:
- k = thermal conductivity
- A = contact area
- ΔT = temperature difference
- d = conduction path length

**Isolation strategies:**
1. Minimal contact area (raised bosses)
2. Thermal break material (G10 spacers, 0.5-1mm thick)
3. Air gap between spindle and mount (5-10mm where possible)
4. Direct cooling of mount plate (coolant passages)

## Toolholder Interfaces

### ER Collet System

**Advantages:**
- Lightweight (2-4 kg including spindle)
- Wide tool diameter range (ER20: 1-13mm, ER25: 1-16mm)
- Low cost
- Good for small machines

**Disadvantages:**
- Manual tool changes only
- Moderate runout (5-10 µm typical)
- Lower rigidity than taper systems

**Applications:** Small DIY mills, hobby machines, router conversions

### BT/CAT Taper (ISO 7388/ANSI B5.50)

**Common sizes:**
- BT30/CAT30: Light-duty, smaller machines
- BT40/CAT40: Standard industrial size
- BT50/CAT50: Heavy-duty applications

**Advantages:**
- Automatic tool change (ATC) compatible
- High rigidity (dual-contact: taper + face)
- Widely available toolholders
- Industrial standard

**Disadvantages:**
- Heavier spindles (15-25 kg for BT40)
- More expensive
- Larger envelope

**Applications:** Production mills, machining centers

### HSK (Hollow Shank Taper)

**Modern high-speed interface:**
- HSK-A63: General purpose (comparable to BT40)
- HSK-A100: Heavy-duty

**Advantages:**
- Better high-speed performance (balanced, symmetric)
- Higher stiffness than BT/CAT
- Shorter tool change time
- Face contact only (no taper friction at high speed)

**Disadvantages:**
- Most expensive
- Less toolholder availability than BT/CAT
- Heavier than ER systems

**Applications:** High-speed machining, modern industrial machines

## Cooling Integration

### Spindle Coolant Connections

**Water-cooled spindle plumbing:**
- Quick-disconnect fittings (allow spindle removal)
- Flexible hose (accommodates Z-axis motion)
- Routing through cable carrier
- Drip loop at lowest point (prevents water siphoning on shutdown)

**Flow direction:**
- Inlet at bottom, outlet at top (natural convection assists)
- Or follow manufacturer specification

### Through-Spindle Coolant (TSC)

**High-pressure coolant delivery:**
- Coolant fed through spindle center, out tool
- Pressure: 300-1000 PSI (20-70 bar)
- Requires rotary union on spindle
- Special toolholders with coolant passage

**Benefits:**
- Direct cooling at cutting edge
- Excellent chip evacuation
- Enables deep hole drilling

**Implementation challenges:**
- Adds weight (rotary union: 0.5-1 kg)
- Requires high-pressure pump
- More complex plumbing
- Higher cost ($500-2000 additional)

## Vibration and Damping

### Spindle-Induced Vibration

**Sources:**
- Unbalanced tool or tool holder
- Bearing wear
- Chatter during cutting

**Effects on vertical axis:**
- Accelerates linear guide wear
- Reduces surface finish
- Can excite column resonances

**Mitigation:**
- Balance all toolholders (on-machine or external balancer)
- Quality spindle with low vibration (<0.5 mm/s² typical)
- Rigid mounting (no compliance in spindle mount)
- Adequate column stiffness

### Damping Strategies

**Passive damping:**
- Viscoelastic damping layers in mount structure
- Tuned mass dampers (for specific resonances)
- Cast iron components (inherent damping)

**Active damping:**
- Rarely used except in ultra-precision machines
- Piezo-actuated damping systems
- Requires sensors and control system

## Key Takeaways

1. **Spindle weight** is critical design parameter for Z-axis—minimize while meeting power needs
2. **Water-cooling** essential for >1kW spindles and thermal stability
3. **Runout control** requires precise mounting: target <10 µm TIR at tool nose
4. **Thermal isolation** prevents heat transfer from spindle to column
5. **ER collets** for lightweight applications, BT/CAT for industrial use, HSK for high-speed
6. **Mount plate stiffness** important for rigidity under cutting forces
7. **Tool change** considerations: Manual (ER) vs. automatic (BT/CAT/HSK)
8. **Through-spindle coolant** beneficial for production but adds complexity and weight
9. **Vibration control** through balancing and rigid mounting
10. **Integration planning**: Coolant routing, electrical connections, tool clearance

***

**Next**: [Section 2.9 – Cable Management](section-2.9-cable-management.md)

**Previous**: [Section 2.7 – Thermal Management](section-2.7-thermal-management.md)

---

# Module 2 – Vertical Axis & Z-Stage


## Overview

Vertical axis cable management presents unique challenges: cables must travel with the moving carriage while avoiding snagging, minimizing strain, and resisting gravity's tendency to pull cables downward. This section covers cable carrier selection, routing strategies, and strain relief techniques specific to Z-axis applications.

## Cable Types and Requirements

### Power Cables

**Motor power:**
- 3-phase for servo motors (4-wire plus ground)
- AWG 18-14 typical for NEMA 17-34
- Continuous flex rated (millions of cycles)

**Spindle power:**
- AWG 12-8 for 1.5-7.5kW spindles
- VFD output (high dV/dt, requires shielding)
- Separate from signal cables

### Signal Cables

**Encoder feedback:**
- Differential signals (RS-422 typical)
- Twisted-pair, shielded
- Low capacitance (<100 pF/m)
- Keep <3m total length

**Limit switches / Home sensors:**
- 22-24 AWG
- Shielded to prevent EMI

**Temperature sensors:**
- Thermocouple or RTD extension wire
- Shielded, keep away from power cables

### Fluid Lines

**Spindle coolant:**
- 6-10mm ID flexible hose
- Rated for coolant temperature and pressure
- Quick-disconnects for serviceability

**Lubrication lines:**
- 4-6mm tubing for automatic lubrication systems
- Low-pressure (<10 bar)

## Cable Carrier Systems

### Carrier Types

**Plastic drag chain:**
- Most common for small-medium machines
- Low cost ($2-5/ft)
- Quiet operation
- Adequate for most applications

**Steel cable carrier:**
- Heavy-duty applications
- Higher cost ($10-20/ft)
- Better for long travels (>2m)
- Oil/coolant resistant

**Spiral wrap / Conduit:**
- Lightweight, flexible
- Not suitable for Z-axis (gravity pulls loops)
- Use only for stationary routing

### Carrier Sizing

**Internal dimensions:**

$$A_{required} = \frac{\sum A_{cables}}{0.4}$$

Fill ratio: 40% maximum (allows cable movement, prevents binding)

**Example:**
- 4× AWG 18 power: 4× 8 mm² = 32 mm²
- 2× shielded twisted pair: 2× 12 mm² = 24 mm²
- 1× coolant hose: 80 mm² (10mm OD)
- Total: 136 mm²
- Required carrier area: 136 / 0.4 = 340 mm²

Select 25×25mm carrier (internal area = 625 mm², adequate margin)

### Bend Radius

**Minimum bend radius:**

$$R_{min} = 10 \times D_{largest\\_cable}$$

Conservative guideline ensures long cable life.

**Example:**
- Largest cable: 10mm OD coolant hose
- Minimum radius: 100mm
- Selected carrier: 150mm radius (safety margin)

## Mounting Configurations

### Top-Mounted Carrier (Recommended)

```
    Column
        |
    [Fixed end]
        |
      Cable
      Carrier ← Moves with carriage
        |
    [Moving end]
        |
    Carriage
```

**Advantages:**
- Gravity assists cable return (reduces wear)
- Clean appearance
- Protected from chips/coolant

**Disadvantages:**
- Requires space above column
- More complex mounting at top

### Side-Mounted Carrier

**Carrier mounted to side of column:**
- Works when top mounting not feasible
- Requires rigid carrier support bracket
- Gravity pulls carrier outward (support every 300-500mm)

### Internal Carrier (Advanced)

**Carrier routed inside hollow column:**
- Clean external appearance
- Maximum protection
- Difficult to service
- Requires larger column cross-section

## Installation Best Practices

### Fixed End Mounting

**Anchor point (top of column or machine frame):**
- Rigid mounting (no deflection)
- Strain relief for all cables exiting carrier
- Cable ties every 100mm
- Drip loop for coolant lines (lowest point before entry)

### Moving End Mounting

**Carriage attachment:**
- Secure mounting to carriage plate
- Flexible boot or conduit from carrier to components
- Allow 50-100mm extra cable length (service loop)
- Strain relief clamps at carrier exit

### Cable Routing Inside Carrier

**Layout strategy:**
1. Power cables on one side
2. Signal cables on opposite side (EMI separation)
3. Coolant hoses in center or separate chamber
4. Secure cables every 200-300mm inside carrier (prevent tangling)

**Avoid:**
- Mixing power and signal in same bundle
- Excessive tension on cables
- Sharp bends at carrier entry/exit
- Cables crossing over each other

## Strain Relief

### At Carrier Exits

**Fixed end:**
- 90° conduit fitting or cable gland
- Cable ties to support bracket
- Maintain bend radius
- Allow thermal expansion (don't over-tighten)

**Moving end:**
- Flexible conduit (last 150-200mm)
- Spiral wrap for small cables
- Service loop (coiled excess cable)
- Secure to carriage but allow slight movement

### At Component Connections

**Motor/spindle:**
- Connector with strain relief collar
- Cable clamped 100mm before connector
- No tension on connector pins
- Avoid sharp bends near connector

**Drives/electronics:**
- Cable entry through grommet or gland
- Secured to enclosure wall
- Drip loop before entry (if moisture possible)

## Vertical-Specific Considerations

### Gravity Effects

**Cable weight pulls downward:**
- Use lightweight cables when possible
- Support carrier at intervals (side-mount)
- Top-mount preferred (gravity assists)

**Coolant draining:**
- Route coolant hoses with continuous downward slope
- Avoid traps where fluid can pool
- Drip loop at lowest point

### Travel Length Calculation

**Carrier length:**

$$L_{carrier} = L_{travel} + 2 \times R_{bend} + L_{fixed} + L_{moving}$$

Where:
- $L_{travel}$ = Z-axis travel
- $R_{bend}$ = carrier bend radius
- $L_{fixed}$ = fixed end length (typically 150-300mm)
- $L_{moving}$ = moving end length (typically 200-400mm)

**Example:**
- Z-travel: 400mm
- Bend radius: 150mm
- Fixed end: 200mm
- Moving end: 300mm
- Total carrier length: 400 + 2(150) + 200 + 300 = 1200mm

Order 1500mm carrier (allows adjustment)

### Dynamic Loading

**Acceleration forces:**
- Cables experience inertial loading during acceleration
- Secure cables inside carrier to prevent shifting
- Use cable separators if high-acceleration application

## Troubleshooting Common Issues

### Cable Wear

**Symptoms:** Frayed insulation, broken conductors

**Causes:**
- Bend radius too tight
- Cables rubbing against carrier edges
- Over-filled carrier (cables binding)

**Solutions:**
- Increase bend radius
- Add cable separators
- Route cables to avoid edges
- Reduce fill ratio

### Signal Interference

**Symptoms:** Encoder errors, erratic motion, noise on sensors

**Causes:**
- Power and signal cables not separated
- Inadequate shielding
- Ground loops

**Solutions:**
- Separate power and signal (opposite sides of carrier)
- Use shielded cables, ground shields at one end only
- Twisted pair for differential signals
- Ferrite beads on signal cables near drives

### Carrier Binding

**Symptoms:** Jerky motion, increased motor current, audible clicking

**Causes:**
- Carrier over-filled
- Misaligned carrier mounting
- Insufficient lubrication

**Solutions:**
- Reduce cable count or increase carrier size
- Realign carrier mounting (parallel to motion axis)
- Lubricate carrier links (plastic-compatible grease)

### Coolant Leaks

**Symptoms:** Dripping coolant, pooling in carrier

**Causes:**
- Inadequate hose strain relief
- Hose kinked or damaged
- Quick-disconnect leaking

**Solutions:**
- Add hose support near connections
- Replace damaged hose
- Use higher-quality quick-disconnects with seals

## Key Takeaways

1. **Top-mounted carriers** preferred for Z-axis (gravity assists cable return)
2. **Fill ratio** must be <40% to prevent binding and allow cable movement
3. **Bend radius** minimum 10× largest cable diameter for long life
4. **Separate power and signal** cables to prevent EMI (opposite sides of carrier)
5. **Strain relief** critical at both fixed and moving ends
6. **Service loops** provide extra cable length for maintenance and adjustment
7. **Drip loops** required for coolant hoses before entering components
8. **Carrier length** calculation includes travel + bends + fixed/moving ends
9. **Cable ties** every 100-200mm prevent tangling inside carrier
10. **Continuous downward slope** for fluid lines prevents trapping and leaks

***

**Next**: [Section 2.10 – Assembly and Alignment](section-2.10-assembly-alignment.md)

**Previous**: [Section 2.8 – Spindle Mounting](section-2.8-spindle-mounting.md)

---

# Module 2 – Vertical Axis & Z-Stage


## Overview

Precision assembly and alignment of vertical axis components determines achievable accuracy and long-term reliability. This section provides systematic procedures for column installation, linear rail tramming, ball screw alignment, and final system verification.

## Pre-Assembly Preparation

### Base/Frame Verification

**Critical mounting surface requirements:**
- Flatness: 20 µm over mounting area
- Perpendicularity to X-Y plane: 50 µm/m
- Surface finish: 3.2 µm Ra or better
- Tapped holes: Clean threads, proper depth

**Inspection procedure:**
1. Place precision granite square or angle plate on base
2. Indicate mounting surface flatness (sweep in grid pattern)
3. Check perpendicularity with precision square and indicator
4. Verify hole locations against drawing (±0.1mm tolerance)
5. Clean and degrease mounting surface

**If surface not within specification:**
- Scrape or hand-grind high spots
- Re-machine if deviation >100 µm
- Use shims only as last resort (reduces rigidity)

### Component Inspection

**Inspect all components before assembly:**

**Column:**
- Rail mounting surfaces flat (10 µm target)
- Ball screw mounting faces parallel and square
- No burrs, damage, or debris
- Protective coatings removed from precision surfaces

**Linear rails:**
- Check rail straightness with comparator (±5 µm)
- Inspect for damage during shipping
- Verify carriage preload by hand feel (smooth, consistent resistance)
- Rails match as set (often marked L/R or 1/2)

**Ball screw:**
- Bearing seats clean and undamaged
- Thread runout <10 µm TIR (check with indicator)
- Couplings inspected, set screws present

### Tools Required

**Precision instruments:**
- Dial indicator (0.001mm / 0.5 µm resolution)
- Magnetic base and extensions
- Precision parallel (ground to ±2 µm)
- Granite angle plate (reference surface)
- Feeler gauges (metric, 0.02-1.0mm)

**Installation tools:**
- Torque wrench (accurate to ±4%)
- Allen key set (quality, no rounding)
- Soft-face mallet (assembly)
- Degreaser and lint-free wipes
- Grease (specified for bearings and guides)

## Column Installation

### Step 1: Position and Level

**Mounting the column to base:**

1. **Apply thin coat of way oil** to base mounting surface (prevents galling, aids alignment)
2. **Position column** onto base mounting surface
   - Use lifting equipment for large columns (>20 kg)
   - Avoid dropping or impact
3. **Insert locating dowel pins** (if designed with dowels)
   - Dowels provide repeatable positioning
   - Tight slip fit (H7/m6 tolerance typical)
4. **Check perpendicularity** to base using precision square and indicator
   - Sweep column face at top and bottom
   - Target: <25 µm deviation over column height
5. **Shim if necessary** to achieve perpendicularity
   - Use precision ground shims (not feeler gauges)
   - Minimum number of shim locations
   - Shim entire contact area (not just corners)

### Step 2: Secure Column

**Fastener installation sequence:**

1. **Insert all mounting bolts** finger-tight
2. **Tighten bolts progressively** in cross-pattern
   - Start center, work outward
   - Multiple passes, increasing torque each pass
3. **Final torque** per specification
   - M8: 20-25 N·m typical
   - M10: 40-50 N·m typical
   - M12: 70-85 N·m typical
4. **Re-check perpendicularity** after torquing
   - Torque can distort alignment
   - If deviation >25 µm, loosen and re-align

**Important:** Use threadlocker (medium-strength, e.g., Loctite 243) on all structural fasteners.

### Step 3: Final Verification

**Column rigidity check:**
1. Attempt to deflect column by hand at top (reasonable force)
2. No detectable movement (indicates proper mounting)
3. If movement detected, check fastener torque and base contact

**Perpendicularity documentation:**
- Record final indicator readings
- Document shim locations and thickness
- Photograph assembly for future reference

## Linear Rail Installation

### Step 1: Rail Mounting Surface Preparation

**Critical step for long-term accuracy:**

1. **Clean mounting surfaces** on column
   - Remove all oil, debris, protective coatings
   - Solvent wipe followed by dry wipe
2. **Inspect flatness** of each rail mounting surface
   - Sweep with indicator along full length
   - Target: <10 µm deviation
   - If >20 µm, surface requires machining or scraping
3. **Apply thin film of grease** to mounting surface
   - Prevents corrosion, aids initial alignment
   - Wipe excess (should be barely visible film)

### Step 2: First Rail Installation

**Establishing reference rail:**

1. **Position first rail** on mounting surface
   - Align rail length to column travel direction
   - Center rail on mounting pad
2. **Insert mounting bolts** finger-tight
3. **Tram rail** to column reference surface
   - Place precision parallel against rail side face
   - Sweep parallel with indicator along full rail length
   - Adjust rail position to minimize deviation
   - Target: <20 µm TIR over full length
4. **Tighten mounting bolts progressively**
   - Start at center, work toward ends
   - Torque per rail manufacturer specification (typically 10-15 N·m for HGR15/20)
5. **Re-check tramming** after torquing
   - Torque can shift rail
   - If deviation >20 µm, loosen and repeat

### Step 3: Second Rail Installation (Parallelism)

**Most critical alignment step:**

1. **Install carriages** on first rail
2. **Position precision parallel** between first and second rail mounting surfaces
   - Parallel spans between the two rails
   - Parallel length matches rail spacing
3. **Position second rail** using parallel as reference
4. **Indicate parallelism** at multiple positions along rail length
   - Top, middle, bottom of travel
   - Adjust second rail until parallel to first rail
   - Target: <20 µm deviation over full length
5. **Tighten mounting bolts progressively**
6. **Final verification:**
   - Install carriage on second rail
   - Slide both carriages manually along full travel
   - Should move smoothly with consistent resistance
   - Any binding indicates misalignment

**If binding detected:**
- Loosen second rail
- Use indicator to find tight spot
- Adjust rail at that location
- Re-torque and test

### Step 4: Carriage Installation

**Installing carriages on rails:**

1. **Apply lubricant** to rails (per manufacturer specification)
2. **Slide carriages** onto rails from end
   - Do not disassemble carriages (loses preload setting)
   - Keep carriages oriented correctly (marked "up" or with arrow)
3. **Distribute carriages** along rail
   - Space evenly for initial testing
4. **Install end stops** (prevent carriage from running off rail)
   - Mechanical stops at both ends of travel
   - 10-20mm from maximum travel limits

## Ball Screw Installation

### Step 1: Bearing Mounting

**Fixed-end bearing (bottom typical):**

1. **Clean bearing seat** in column
   - No burrs, debris, or damage
2. **Install angular contact bearings** per manufacturer instructions
   - Correct orientation (load side facing thrust direction)
   - Preload shims if specified
3. **Install bearing housing**
   - Torque fasteners per specification
   - Lock nuts or threadlocker as required
4. **Check bearing preload** by rotating screw by hand
   - Should rotate smoothly with slight resistance
   - Too tight: excessive friction, premature wear
   - Too loose: backlash, reduced stiffness

**Supported-end bearing (top typical):**

1. **Install radial bearing** (allows thermal expansion)
   - Bearing free to slide axially
   - Maintains lateral location only
2. **Secure bearing housing**

**Center support bearing (if used):**
- Install after screw positioned
- Adjust for proper support without binding screw

### Step 2: Ball Screw Alignment

**Critical for smooth motion and long life:**

1. **Position ball screw** in fixed-end bearing
2. **Check screw runout** at supported end
   - Place indicator on screw surface near bearing
   - Rotate screw by hand, observe runout
   - Target: <10 µm TIR
3. **Adjust screw position** to minimize runout
   - Shim bearing housing if necessary
   - Eccentric bearing mount (if provided) simplifies adjustment
4. **Secure supported-end bearing**
5. **Install ball nut** onto screw
   - Lubricate with specified grease
   - Do not disassemble nut (loses ball preload)

### Step 3: Coupling Installation

**Motor-to-screw coupling:**

1. **Align motor shaft** to ball screw
   - Motor mounted to column or carriage
   - Shafts collinear (no angular or parallel offset)
2. **Measure alignment** with dial indicator
   - Rotate both shafts, observe TIR on each
   - Angular misalignment: <0.05mm TIR
   - Parallel offset: <0.1mm
3. **Install flexible coupling**
   - Helical beam coupling recommended (accommodates slight misalignment)
   - Set screws on flats (not threads)
   - Torque set screws per coupling specification
4. **Verify alignment** after coupling installed
   - Rotate motor shaft by hand
   - Smooth rotation, no binding or vibration

**Important:** Rigid couplings require near-perfect alignment (<0.02mm). Use flexible couplings for easier assembly and better tolerance of thermal expansion.

## Carriage Assembly and Mounting

### Ball Nut to Carriage

**Connecting ball nut to moving carriage:**

1. **Position carriage** at mid-travel
2. **Attach ball nut** to carriage plate
   - Ball nut flange typically bolted to carriage bottom
   - Use washers to distribute load
   - Torque bolts evenly (cross-pattern)
3. **Check that carriage moves freely** when screw rotated
   - If binding: Check rail parallelism and screw alignment
   - Screw must be parallel to rails (no skew)

### Carriage Perpendicularity

**Ensure carriage perpendicular to column:**

1. **Mount precision angle plate** to carriage
2. **Indicate against column reference surface**
   - Sweep indicator across carriage face
   - Adjust carriage mounting (if slotted holes provided)
   - Target: <25 µm deviation across carriage width
3. **Tighten carriage mounting bolts**

## Counterbalance Installation

### Gas Spring Mounting

**Typical configuration for small-medium machines:**

1. **Identify mounting points**
   - Fixed end: Column or frame
   - Moving end: Carriage
2. **Install gas spring** per manufacturer orientation
   - Piston rod down (oil stays at cylinder head)
   - Mounting clevis with pivot pins
3. **Verify force balance**
   - With motor de-energized and brake released (use caution—support carriage)
   - Carriage should hold position at mid-travel
   - Slight upward bias acceptable (±5%)
4. **Adjust if necessary**
   - Swap gas spring for different force rating
   - Add/remove mass from carriage if adjustable

### Pneumatic Counterbalance

**For larger machines:**

1. **Connect pneumatic cylinder** to air supply
2. **Install pressure regulator** in line
3. **Set pressure** to balance carriage weight
   - Starting point: P = F / A (force divided by piston area)
   - Fine-tune by testing motion balance
4. **Lock regulator setting** after adjustment

## System-Level Alignment Checks

### Runout Verification

**Spindle-to-table alignment:**

1. **Mount dial indicator** in spindle (if spindle installed)
2. **Sweep indicator** against flat surface on table
3. **Move Z-axis** over full travel while observing indicator
4. **Record runout:** Should be <50 µm for general milling, <25 µm for precision
5. **If excessive runout:**
   - Check column perpendicularity to base
   - Verify rail parallelism
   - Inspect ball screw alignment

### Travel Limits

**Verify full Z-axis travel:**

1. **Jog carriage** to bottom limit (manually or with motor)
2. **Note position** (use DRO or mark reference)
3. **Jog to top limit**
4. **Measure total travel** and compare to specification
5. **Set software limits** in control system
   - Soft limits 5-10mm inside mechanical limits
   - Prevents crashes

### Backlash Measurement

**Check system backlash:**

1. **Mount dial indicator** against carriage (reading Z-direction)
2. **Jog Z-axis upward** 10mm, zero indicator
3. **Command Z-axis downward** 10mm (observe when indicator begins moving)
4. **Backlash = commanded distance before indicator moves**
5. **Acceptable values:**
   - General purpose: <50 µm
   - Precision: <20 µm
   - Ultra-precision: <5 µm
6. **If excessive backlash:**
   - Check ball nut preload (adjustable on some screws)
   - Inspect coupling for play
   - Verify rail carriage preload

## Cable Management Installation

### Cable Carrier Mounting

**Per Section 2.9 guidelines:**

1. **Mount fixed end** of carrier
   - Top of column or frame (for top-mount configuration)
   - Rigid mounting bracket
   - Strain relief for cables exiting carrier
2. **Mount moving end** to carriage
   - Secure bracket to carriage plate
   - Flexible conduit for last 150mm to components
3. **Route cables** through carrier
   - Power on one side, signal on other (EMI separation)
   - Secure cables every 200-300mm inside carrier
   - Maintain bend radius (≥10× largest cable diameter)
4. **Test full travel**
   - Move carriage through full range
   - Verify carrier moves smoothly, no snagging
   - Check cable strain relief at both ends

## Documentation

### Assembly Record

**Document final configuration:**
- Shim locations and thicknesses
- Fastener torque values and sequence
- Alignment measurements (parallelism, perpendicularity, runout)
- Counterbalance force and setting
- Lubrication type and locations
- Photos of critical areas

**Purpose:** Enables future troubleshooting, maintenance, and rebuilds.

### Alignment Report

**Create measurement record:**
```
Z-Axis Alignment Report
-----------------------
Date: __________
Technician: __________

Column Perpendicularity:
  - X-axis: _____ µm deviation over _____ mm height
  - Y-axis: _____ µm deviation over _____ mm height

Rail Parallelism:
  - Rail 1 to column reference: _____ µm TIR
  - Rail 2 to Rail 1: _____ µm deviation

Ball Screw Alignment:
  - Runout at fixed end: _____ µm TIR
  - Runout at supported end: _____ µm TIR
  - Coupling alignment: _____ µm offset

System Performance:
  - Total Z travel: _____ mm
  - Spindle runout over travel: _____ µm
  - Backlash: _____ µm
  - Counterbalance force: _____ N (target: _____ N)

Notes:
_______________________________________
```

## Common Assembly Issues

### Rail Binding

**Symptom:** Carriage difficult to move, uneven resistance

**Causes:**
- Rails not parallel (most common)
- Mounting surface not flat
- Over-torqued mounting bolts (distorts rail)
- Debris under rail

**Solution:**
1. Loosen all rail mounting bolts
2. Check mounting surface flatness
3. Re-tram rails with precision parallel
4. Torque bolts progressively, re-check after each pass
5. Test carriage motion frequently during assembly

### Ball Screw Binding

**Symptom:** Rough rotation, tight spots, motor stalling

**Causes:**
- Screw not aligned to rails (skewed)
- Bearing over-preloaded
- Coupling misalignment
- Ball nut to carriage mounting stressed

**Solution:**
1. Check screw-to-rail parallelism (should be within 0.1mm over travel)
2. Verify bearing preload (should rotate smoothly by hand)
3. Re-check coupling alignment
4. Loosen ball nut mounting, verify free rotation, re-torque gently

### Excessive Runout

**Symptom:** Spindle runout >50 µm over Z travel

**Causes:**
- Column not perpendicular to base
- Rails not parallel
- Column deflection under carriage weight

**Solution:**
1. Re-check column perpendicularity, shim if needed
2. Verify rail tramming
3. If deflection issue, stiffen column (Section 2.3) or reduce moving mass

## Key Takeaways

1. **Base flatness and perpendicularity** are foundation for all subsequent alignment
2. **Rail tramming** requires precision parallel and indicator—target <20 µm parallelism
3. **Rail parallelism** critical: Binding indicates misalignment
4. **Ball screw runout** should be <10 µm TIR at bearing seats
5. **Coupling alignment** prevents premature bearing wear (use flexible coupling)
6. **Counterbalance verification** before motor tuning (release brake, observe balance)
7. **System-level checks** validate component assembly (runout over travel, backlash)
8. **Documentation** enables future maintenance and troubleshooting
9. **Progressive torquing** prevents distortion (cross-pattern, multiple passes)
10. **Test frequently** during assembly: Small adjustments easier than complete disassembly

***

**Next**: [Section 2.11 – Testing and Commissioning](section-2.11-testing-commissioning.md)

**Previous**: [Section 2.9 – Cable Management](section-2.9-cable-management.md)

---

# Module 2 – Vertical Axis & Z-Stage


## Overview

Systematic testing validates mechanical assembly and establishes baseline performance before production use. This section covers mechanical verification, counterbalance optimization, servo tuning procedures, and performance validation specific to vertical axis systems.

## Pre-Commissioning Safety Checks

### Mechanical Safety Verification

**Critical checks before applying power:**

1. **Emergency stop functionality**
   - E-stop button accessible and clearly marked
   - E-stop circuit wired to brake (fail-safe)
   - Test: Press E-stop, verify brake engages
2. **Brake operation**
   - With power off, brake should be engaged (spring-applied type)
   - Apply power, brake should release (audible click typical)
   - Cut power, brake should re-engage immediately
3. **Limit switches**
   - Upper and lower travel limits installed
   - Switches positioned 5-10mm beyond desired travel endpoints
   - Test continuity with multimeter
4. **Carriage support**
   - Before releasing brake: Verify counterbalance supports carriage
   - If insufficient, manually support carriage when testing
5. **Guards and covers**
   - Moving parts enclosed (ball screw, coupling)
   - Pinch points protected
   - Cable carrier cannot be contacted during normal operation

**CRITICAL SAFETY RULE:** Never release the Z-axis brake without verified counterbalance or manual support. Unsupported vertical axes can fall rapidly, causing injury or damage.

## Mechanical Verification Tests

### Test 1: Static Stiffness

**Objective:** Verify column deflection under load matches design calculations.

**Equipment:**
- Calibrated weights (5-50 kg depending on machine size)
- Dial indicator (0.001mm resolution)
- Magnetic base

**Procedure:**
1. **Mount indicator** against spindle mount or carriage
   - Reading perpendicular to column face (X or Y direction)
   - Zero indicator with no load
2. **Apply known force** at tool mounting point
   - Hang calibrated weight from spindle nose
   - Typical test: 10-20 kg (100-200 N force)
3. **Record deflection** from indicator
4. **Calculate actual stiffness:**
   $$k_{actual} = \frac{F}{\delta}$$
   Where F = applied force (N), δ = measured deflection (mm)
5. **Compare to design value** (from Section 2.3 calculations)
   - Actual should be ≥80% of designed stiffness
   - If lower: Check column mounting, rail installation, fastener torque

**Example:**
- Applied force: 150 N (15.3 kg weight)
- Measured deflection: 35 µm
- Actual stiffness: 150 / 0.035 = 4,286 N/mm
- Design stiffness: 5,000 N/mm
- Ratio: 86% (acceptable, within 80% threshold)

### Test 2: Backlash Measurement

**Objective:** Quantify total system backlash.

**Equipment:**
- Dial indicator
- Magnetic base
- Manual control or MDI (Manual Data Input)

**Procedure:**
1. **Position carriage** at mid-travel
2. **Mount indicator** against carriage, reading Z-direction
3. **Command upward motion** (+Z) 5mm, wait for settling
4. **Zero indicator**
5. **Command downward motion** (-Z) 0.1mm increments
6. **Note commanded distance** before indicator begins moving
   - This dead zone = backlash
7. **Repeat at 3-5 locations** along Z-travel (top, middle, bottom)
8. **Record maximum backlash**

**Acceptance criteria:**
- General purpose: <50 µm
- Precision work: <20 µm
- Ultra-precision: <5 µm

**If excessive:**
- Check ball screw preload (may be adjustable)
- Inspect coupling for slop
- Verify motor mounting (no deflection under load)

### Test 3: Runout Over Travel

**Objective:** Measure spindle perpendicularity variation over Z-axis travel.

**Equipment:**
- Dial indicator mounted in spindle or on carriage
- Precision ground disc or surface plate on table

**Procedure:**
1. **Mount indicator** in spindle (or attach to carriage)
   - Indicator tip contacts table reference surface
2. **Position Z-axis** at lowest point in travel
3. **Zero indicator**
4. **Traverse Z-axis** to highest point while observing indicator
5. **Record total indicated runout (TIR)** over full travel
6. **Repeat in X and Y directions** (rotate indicator orientation)

**Acceptance criteria:**
- Hobby/light-duty: <100 µm TIR
- General purpose: <50 µm TIR
- Precision: <25 µm TIR

**If excessive:**
- Check column perpendicularity to base
- Verify rail parallelism (re-tram if necessary)
- Inspect for column deflection under carriage weight

### Test 4: Smooth Motion Test

**Objective:** Verify smooth, consistent motion without binding or stick-slip.

**Equipment:**
- Motor drive (low-speed jog)
- Observation

**Procedure:**
1. **Enable motor** and release brake
2. **Jog Z-axis upward** at slow speed (50-100 mm/min)
   - Observe motion: Should be smooth and continuous
   - Listen for unusual noises (grinding, clicking)
3. **Jog Z-axis downward** at same speed
4. **Repeat at multiple speeds** (100, 500, 1000 mm/min)
5. **Note any irregularities:**
   - Binding or tight spots (alignment issue)
   - Jerky motion (stick-slip from friction or servo tuning)
   - Vibration (imbalance, coupling misalignment)

**Resolution:**
- Binding: Re-check rail parallelism and ball screw alignment
- Stick-slip: Improve lubrication, adjust servo gains
- Vibration: Balance toolholder, check coupling alignment

## Counterbalance Optimization

### Force Balance Verification

**Objective:** Adjust counterbalance to neutralize gravitational load.

**Equipment:**
- Motor current meter (drive display or oscilloscope)
- Position feedback (encoder readout or DRO)

**Procedure:**

**Method 1: Static Balance Test (Preferred)**
1. **Position carriage** at mid-travel
2. **Enable motor** (servo on, zero torque command)
3. **Release brake carefully** (support carriage if balance uncertain)
4. **Observe carriage motion:**
   - Sinks downward: Counterbalance too weak
   - Rises upward: Counterbalance too strong
   - Holds position: Balanced
5. **Adjust counterbalance:**
   - Gas spring: Replace with different force rating
   - Pneumatic: Adjust air pressure regulator
   - Weight-cable: Add/remove counterweight mass
6. **Re-test until carriage holds position** (±5% drift acceptable)

**Method 2: Current Monitoring (Quantitative)**
1. **Jog carriage upward** at constant velocity (e.g., 500 mm/min)
2. **Record motor current** during constant-velocity phase (RMS value)
3. **Jog carriage downward** at same velocity
4. **Record motor current** during descent
5. **Calculate balance error:**
   $$\text{Balance error} = \frac{I_{up} + I_{down}}{2}$$
   Ideal balance: $I_{up} = -I_{down}$ (equal magnitude, opposite direction)
6. **Adjust counterbalance** to minimize balance error
7. **Repeat until balance error <10% of rated current**

**Example:**
- Upward current: 1.2 A
- Downward current: -0.3 A
- Balance error: (1.2 + (-0.3)) / 2 = 0.45 A
- Target: <0.5 A for 5A rated drive (10% threshold)
- Result: Acceptable balance

### Dynamic Balance Verification

**Test acceleration symmetry:**

1. **Command rapid upward move** (e.g., +100mm at maximum acceleration)
2. **Record peak current** during acceleration
3. **Command rapid downward move** (-100mm, same acceleration)
4. **Record peak current**
5. **Compare peak currents:**
   - Good balance: Peak currents within 20% of each other
   - Poor balance: Significant asymmetry (adjust counterbalance)

## Electrical Commissioning

### Motor Phasing Verification

**Ensure motor wired correctly:**

**Symptoms of reversed phasing:**
- Motor runs in opposite direction than commanded
- Motor vibrates or doesn't move smoothly

**Correction:**
- Swap any two motor power leads (for 3-phase)
- Update control configuration if needed

**Encoder Direction:**
- Jog motor in +Z direction, verify encoder count increases
- If reversed: Swap encoder A+/A- signals or configure in drive

### Home Switch Setup

**Establish machine zero reference:**

1. **Install home switch** at known Z position
   - Typically near top of travel
   - Repeatable trigger point (proximity or mechanical switch)
2. **Configure homing routine** in control
   - Approach speed (slow, 100-200 mm/min for accuracy)
   - Home offset (distance from switch to actual zero)
3. **Test homing sequence:**
   - Command home (G28 Z0 or control-specific command)
   - Verify carriage moves to switch, triggers, and backs off
   - Repeatability: Home 5× times, measure variation (<10 µm target)

### Limit Switch Testing

**Verify travel limit protection:**

1. **Jog to upper limit** until switch triggers
   - Motion should stop immediately
   - Record position
2. **Jog to lower limit** until switch triggers
   - Motion should stop
   - Record position
3. **Calculate actual travel:** Upper position - Lower position
4. **Set soft limits** in control software
   - 5-10mm inside hard limits (prevents crashes)
5. **Test soft limits:**
   - Command move beyond soft limit
   - Control should reject move or stop at limit

## Servo Tuning

### Prerequisites

**Before tuning:**
1. Counterbalance optimized (balance error <10%)
2. All mechanical issues resolved (no binding, smooth motion)
3. Encoder and motor phasing verified
4. Safety systems operational (E-stop, limits, brake)

### Tuning Procedure

**Step 1: Disable All Gains**
- Set Kp, Ki, Kd, FF to zero
- Motor should not respond to position commands (only brake holds position)

**Step 2: Proportional Gain (Kp)**
1. **Increase Kp gradually** from zero
   - Start: Kp = 10-50 (depending on drive units)
   - Increment: Double Kp each step
2. **Test response** after each increase
   - Command small move (±10mm)
   - Observe: System should become more responsive
3. **Continue until oscillation** begins (carriage oscillates around target)
4. **Note Kp at onset of oscillation** (critical gain, Kc)
5. **Reduce Kp to 40-60% of Kc** for stability margin
   - Example: Kc = 500, use Kp = 200-300

**Step 3: Derivative Gain (Kd)**
1. **Add derivative damping** to reduce overshoot
   - Start: Kd = Kp / 10
   - Adjust: Increase if oscillation persists, decrease if sluggish
2. **Test with rapid moves**
   - 100mm move at high acceleration
   - Observe settling time and overshoot
3. **Target: Critically damped response**
   - Minimal overshoot (<5%)
   - Fast settling (<200ms for typical servo)

**Step 4: Integral Gain (Ki)**
1. **Add integral to eliminate steady-state error**
   - Start: Ki = Kp / 100
   - Increase slowly (can destabilize system if too high)
2. **Test positioning accuracy**
   - Command position, wait for settling
   - Check final error (should be <1 encoder count)
3. **Increase Ki until error eliminated** but before oscillation begins

**Step 5: Feed-Forward Tuning**

**Velocity Feed-Forward (FFv):**
- Reduces following error during constant velocity
- Start: FFv = 0.8
- Increase to 1.0 if following error present during moves
- Measure following error: Position error during constant-velocity phase

**Acceleration Feed-Forward (FFa):**
- Reduces following error during acceleration
- Start: FFa = 0.5
- Adjust based on following error during accel/decel
- Too high: Overshoot at end of move
- Too low: Lag during acceleration

**Step 6: Gravity Compensation (If Available)**
- Some drives allow constant torque offset
- Set to compensate for residual gravitational torque (if counterbalance not perfect)
- Value: Feed-forward torque = T_gravity (from Section 2.6)

### Tuning Verification Tests

**Test 1: Step Response**
- Command 50mm move from rest
- Record position vs time
- Analyze:
  - Rise time (time to reach 90% of target)
  - Overshoot (should be <5%)
  - Settling time (time to reach ±10 µm of target)

**Test 2: Following Error**
- Command constant-velocity move (500 mm/min)
- Monitor following error (commanded position - actual position)
- Target: <100 µm during motion, <10 µm at rest

**Test 3: Bi-Directional Repeatability**
- Move to position from above (+Z approach)
- Record final position
- Move away, return from below (-Z approach)
- Record final position
- Repeatability = difference between approaches
- Target: <20 µm for precision work

**Test 4: High-Speed Moves**
- Command rapid traverse at maximum speed
- Verify no overshoot or instability
- Check motor current (should not exceed rated)

## Performance Validation

### Accuracy Testing

**Circular interpolation test (if multi-axis):**
1. Program circular move in XZ or YZ plane
2. Measure actual path with indicator or laser interferometer
3. Calculate circularity error
4. Target: <50 µm for general purpose

**Positioning accuracy:**
1. Command move to known position (use gage blocks or precision height gage)
2. Measure actual position
3. Repeat at 5-10 positions across Z-travel
4. Calculate maximum error
5. ISO 230-2 standard: Positioning accuracy (A) and repeatability (R)

### Thermal Stability Test

**Objective:** Measure thermal drift over operating cycle.

**Equipment:**
- Dial indicator (µm resolution)
- Temperature sensor (column, ambient)
- Timer

**Procedure:**
1. **Cold start:** Machine at ambient temperature
2. **Mount indicator** reading against spindle face or carriage
3. **Zero indicator**
4. **Run warm-up cycle:**
   - Spindle at 50-75% rated speed
   - Z-axis jogging over full travel
5. **Record indicator reading** every 10 minutes for 2 hours
6. **Record temperatures** (column, spindle, ambient)
7. **Plot drift vs time**

**Analysis:**
- Initial drift rate: µm/hour (first 30 minutes)
- Stabilized drift: After 60-90 minutes (should be <10 µm/hour for precision work)
- Total drift: From cold to stabilized (indicates warm-up requirement)

**Example results:**
- 0-30 min: 45 µm expansion (high rate, machine heating)
- 30-60 min: 12 µm expansion (slowing)
- 60-120 min: <5 µm variation (thermally stable)
- Conclusion: 60-minute warm-up required before precision work

### Cutting Test

**Objective:** Validate performance under realistic cutting loads.

**Test piece:**
- Aluminum or steel block
- Face milling operation (controlled depth of cut and feed rate)

**Procedure:**
1. **Mount test piece** on table
2. **Program simple face milling** routine
   - Multiple passes in Z-axis (stepping down)
   - Record spindle load, feed rate, depth of cut
3. **Execute program**
   - Monitor motor current (should not exceed rated)
   - Listen for unusual sounds (chatter, vibration)
   - Observe surface finish
4. **Measure result:**
   - Surface flatness (sweep with indicator)
   - Surface finish (visual or profilometer)
   - Dimensional accuracy (depth of cut)

**Acceptance criteria:**
- Flatness: <50 µm over machined area
- Surface finish: Appropriate for material and tooling
- Dimensional accuracy: ±25 µm or better
- No chatter or excessive vibration

### Repeatability Test

**Procedure:**
1. **Program routine:** Move to position, dwell, return to start
2. **Execute 30 cycles** (statistical significance)
3. **Measure final position** after each cycle
   - Indicator against carriage reference surface
4. **Calculate standard deviation** of position measurements
5. **Repeatability (R) = 4× standard deviation** (per ISO 230-2)

**Target performance:**
- Hobby/light-duty: R < 50 µm
- General purpose: R < 20 µm
- Precision: R < 10 µm

**Example:**
- 30 measurements: Mean = 0.0 µm, StdDev = 3.2 µm
- Repeatability: 4 × 3.2 = 12.8 µm (meets general-purpose target)

## Commissioning Documentation

### Performance Report

**Create comprehensive record:**

```
Z-Axis Commissioning Report
============================
Date: __________
Machine ID: __________
Technician: __________

MECHANICAL VERIFICATION
-----------------------
Static Stiffness:
  Applied force: _____ N
  Deflection: _____ µm
  Measured stiffness: _____ N/mm
  Design stiffness: _____ N/mm
  Ratio: _____ %

Backlash: _____ µm (max over travel)

Runout Over Travel:
  X-direction: _____ µm TIR
  Y-direction: _____ µm TIR

Smooth Motion: [  ] Pass  [  ] Fail
  Notes: _________________________

COUNTERBALANCE
--------------
Balance method: [  ] Gas spring  [  ] Pneumatic  [  ] Weight-cable
Balance force: _____ N (target: _____ N)
Static balance: [  ] Holds position  [  ] Drifts up  [  ] Drifts down
Current balance error: _____ A (_____ % of rated)

SERVO TUNING
------------
Final gains:
  Kp = _____
  Ki = _____
  Kd = _____
  FFv = _____
  FFa = _____

Step response:
  Rise time: _____ ms
  Overshoot: _____ %
  Settling time: _____ ms

Following error (at 500 mm/min): _____ µm

PERFORMANCE VALIDATION
----------------------
Positioning accuracy: ±_____ µm
Repeatability: ±_____ µm
Thermal stability: _____ µm/hour (after warm-up)
Warm-up time required: _____ minutes

Cutting test results:
  Material: __________
  Depth of cut: _____ mm
  Feed rate: _____ mm/min
  Surface flatness: _____ µm
  Surface finish: [  ] Acceptable  [  ] Poor
  Dimensional accuracy: ±_____ µm

ACCEPTANCE
----------
System meets performance specifications: [  ] Yes  [  ] No

Approved by: ________________  Date: __________

Notes:
_____________________________________________
```

### Baseline Configuration File

**Save control parameters:**
- Servo gains (Kp, Ki, Kd, FF values)
- Counterbalance settings
- Soft limits and home position
- Acceleration/velocity limits
- Thermal compensation coefficients (if used)

**Purpose:** Allows restoration of known-good configuration after changes or troubleshooting.

## Troubleshooting Common Issues

### Issue: Excessive Following Error

**Symptoms:**
- Position lags behind commanded during moves
- "Following error" alarm from drive

**Causes:**
- Insufficient proportional gain (Kp too low)
- Counterbalance not adjusted (gravitational bias)
- Mechanical friction (binding)

**Solutions:**
1. Increase Kp (verify stability afterward)
2. Optimize counterbalance to reduce gravitational load
3. Check for mechanical binding, improve lubrication
4. Add velocity feed-forward (FFv)

### Issue: Oscillation or Instability

**Symptoms:**
- Carriage oscillates around target position
- High-pitched whine from motor
- Cannot tune system stable

**Causes:**
- Excessive proportional gain (Kp too high)
- Insufficient damping (Kd too low)
- Mechanical resonance in structure

**Solutions:**
1. Reduce Kp to 40-60% of critical gain
2. Increase Kd for damping
3. Add velocity feedback filter (if available in drive)
4. Check for loose mechanical components (resonance source)

### Issue: Asymmetric Response (Up vs Down)

**Symptoms:**
- Different behavior moving up vs down
- Overshoot in one direction only
- Current draw imbalanced

**Causes:**
- Inadequate counterbalancing (gravitational bias)
- Asymmetric friction (e.g., brake dragging)

**Solutions:**
1. Optimize counterbalance force
2. Add gravity feed-forward compensation in drive
3. Check brake releases fully (measure air gap or check current)
4. Verify rails lubricated evenly

### Issue: Poor Repeatability

**Symptoms:**
- Returns to different positions on repeated moves
- Backlash measurement inconsistent

**Causes:**
- Mechanical backlash (ball screw, coupling)
- Thermal variation (position changes with temperature)
- Inadequate servo gains (position not held tightly)

**Solutions:**
1. Check and adjust ball screw preload
2. Inspect coupling for wear or slop
3. Increase integral gain (Ki) to eliminate steady-state error
4. Implement thermal compensation if drift related to temperature

## Key Takeaways

1. **Safety first:** Verify brake and E-stop before any motion testing
2. **Mechanical before electrical:** Resolve all binding and alignment issues before servo tuning
3. **Counterbalance optimization** critical for good servo performance and reduced wear
4. **Systematic tuning:** Kp first (stability), then Kd (damping), then Ki (accuracy), finally FF
5. **Following error** indicates under-tuned system or mechanical issues
6. **Oscillation** indicates over-tuned system (reduce Kp, add Kd)
7. **Thermal stability testing** reveals warm-up requirements for precision work
8. **Documentation** enables future troubleshooting and maintenance
9. **Cutting test** validates system under realistic loads (essential final check)
10. **Baseline configuration** saved after successful commissioning (reference for future)

***

**Next**: [Section 2.12 – Conclusion](section-2.12-conclusion.md)

**Previous**: [Section 2.10 – Assembly and Alignment](section-2.10-assembly-alignment.md)

---

# Module 2 – Vertical Axis & Z-Stage


## Module Summary

This module has provided comprehensive coverage of vertical axis (Z-axis) engineering, from fundamental challenges through practical implementation. You've learned how gravity, structural mechanics, thermal effects, and safety requirements combine to create design constraints fundamentally different from horizontal axes.

### Key Concepts Reviewed

**Section 2.1 - Introduction:**
- Unique challenges of vertical motion: gravity, cantilever mechanics, thermal expansion
- Safety imperatives for fall-protection
- Design philosophy balancing mass, stiffness, and dynamics

**Section 2.2 - Gravity and Mass Management:**
- Continuous gravitational loading and energy demands
- Counterbalancing systems: gas springs, weight-cable, pneumatic, hydraulic
- Mass reduction through material selection and topology optimization
- Inertia management for servo performance

**Section 2.3 - Column Structural Design:**
- Cantilever beam mechanics and deflection analysis
- Cross-section optimization for stiffness-to-weight ratio
- Material selection: steel, aluminum, cast iron trade-offs
- Fabrication methods: welded, machined, cast

**Section 2.4 - Vertical Linear Guides:**
- Gravitational preload effects on guide selection
- Moment loading from off-center masses
- Preload class selection (ZB/ZC for vertical)
- Installation alignment and safety features

**Section 2.5 - Ball Screws for Vertical Axes:**
- Continuous axial load from gravity
- Critical speed and buckling analysis
- Center support bearings for long travels
- Mechanical brake requirements

**Section 2.6 - Motor and Drive Sizing:**
- Torque calculations including gravitational component
- Benefits of counterbalancing on motor sizing
- Inertia ratio optimization (1:1 to 3:1 ideal)
- Servo tuning for vertical applications

**Section 2.7 - Thermal Management:**
- Vertical thermal expansion directly affects part dimensions
- Heat sources: spindle, friction, environment
- Design strategies: isolation, thermal mass, active cooling
- Software compensation techniques

**Section 2.8 - Spindle Mounting:**
- Interface design for rigidity and runout control
- Cooling integration and thermal management
- Tool holder interface standards (BT, CAT, HSK, ER)
- Vibration isolation and damping

**Section 2.9 - Cable Management:**
- Cable carrier selection and mounting
- Strain relief for vertical motion
- Routing strategies to avoid snagging
- Power vs. signal cable separation

**Section 2.10 - Assembly and Alignment:**
- Column installation and base mounting
- Rail tramming and parallelism verification
- Ball screw alignment and bearing installation
- System-level alignment checks

**Section 2.11 - Testing and Commissioning:**
- Mechanical verification: stiffness, backlash, runout
- Counterbalance adjustment and verification
- Servo tuning procedures for vertical axes
- Performance validation and acceptance testing

## Integration with Other Modules

### Mechanical Foundation (Modules 1-3)

**Module 1 (Frame Design):**
- Column mounts to machine base/frame
- Base must provide rigid, flat mounting surface
- Column weight and cutting forces load frame structure
- Perpendicularity between column and X-Y plane critical

**Connection:**
```
Frame (Module 1) → Column mounting interface → Z-axis (Module 2)
```

**Module 3 (Linear Motion):**
- Linear guides covered in general in Module 3
- Module 2 applies these principles specifically to vertical mounting
- Preload, lubrication, and alignment concepts transfer
- Vertical-specific considerations: gravitational loading, fall protection

### Control System (Module 4)

**Electronics Integration:**
- Motor drives sized in Module 2, wired in Module 4
- Brake control logic (fail-safe design)
- Temperature sensors for thermal compensation
- Limit switches for Z-axis travel protection

**Safety circuits:**
- E-stop must engage Z-axis brake
- Power loss triggers brake automatically
- Control system monitors brake status

### Process Modules (Modules 5-13)

**Spindle Selection:**
- Module 6 covers spindle systems in detail
- Module 2 addresses mounting and integration
- Thermal management strategies apply to all spindle types
- Plasma/laser/waterjet: Different tool weights, mounting requirements

**Example:** 
- Plasma torch (Module 5): 2-3 kg, requires THC integration
- Spindle (Module 6): 5-15 kg, requires cooling and tool change
- Laser head (Module 7): 3-8 kg, requires focus control

### Software and Control (Modules 14-15)

**Module 14 (LinuxCNC):**
- HAL configuration for Z-axis
- Counterbalance feed-forward compensation
- Thermal compensation via HAL components
- Brake control logic implementation

**Module 15 (G-Code):**
- Z-axis motion commands (G00/G01 with Z parameter)
- Tool length compensation (G43)
- Canned cycles for drilling (G81-G89)
- Safe retract heights in programs

### Manufacturing (Module 16)

**CAD/CAM Integration:**
- Z-axis travel limits constrain part height
- Thermal stability affects achievable tolerances
- Surface finish dependent on Z-axis rigidity
- Tool length offsets critical for multi-tool operations

## Real-World Application Synthesis

### Small Benchtop Mill Build

**Specifications:**
- Z-travel: 200mm
- Moving mass: 4 kg (compact air-cooled spindle)
- Target accuracy: ±25 µm
- Budget: $800 for Z-axis components

**Design decisions (from this module):**

1. **Column** (Section 2.3):
   - Material: Aluminum 6061 plate
   - Construction: Pocketed from 100×80×20mm plate
   - Weight: 1.2 kg
   - Cost: $120

2. **Linear guides** (Section 2.4):
   - HGR15 rails, 300mm length
   - 4 carriages, ZB preload
   - Cost: $180

3. **Ball screw** (Section 2.5):
   - 1204 (12mm diameter, 4mm pitch)
   - Fixed-supported mounting
   - Cost: $85

4. **Motor** (Section 2.6):
   - NEMA 17 servo with brake
   - 0.18 N·m rated, 0.54 N·m peak
   - Cost: $120

5. **Counterbalance** (Section 2.2):
   - Single 40N gas spring
   - Cost: $25

6. **Spindle mount** (Section 2.8):
   - Machined aluminum
   - ER11 spindle, 500W
   - Cost: $200 (spindle + mount)

7. **Cable carrier** (Section 2.9):
   - 15×20mm plastic drag chain
   - Cost: $30

**Total Z-axis cost:** $760 (within budget)

**Expected performance:**
- Positioning accuracy: ±20 µm (meets target)
- Maximum cutting force: 300 N
- Thermal drift: <40 µm/hour (acceptable for hobby use)

### Industrial VMC Retrofit

**Specifications:**
- Z-travel: 750mm
- Moving mass: 28 kg (water-cooled spindle + ATC)
- Target accuracy: ±5 µm
- Budget: $15,000 for complete Z-axis rebuild

**Design decisions:**

1. **Column** (Section 2.3):
   - Cast iron, custom casting
   - Internal coolant passages
   - Cost: $4,500

2. **Linear guides** (Section 2.4):
   - HGR25 rails, 1000mm, six carriages (three pairs)
   - ZC heavy preload
   - Cost: $1,200

3. **Ball screw** (Section 2.5):
   - 3210 (32mm diameter, 10mm pitch), ground C7
   - Fixed-supported with center support bearing
   - Cost: $1,800

4. **Motor** (Section 2.6):
   - Industrial servo, 1.5 kW
   - Absolute encoder
   - Cost: $2,200

5. **Counterbalance** (Section 2.2):
   - Pneumatic cylinder system
   - Adjustable pressure regulator
   - Cost: $800

6. **Thermal management** (Section 2.7):
   - Column coolant circulation
   - Spindle chiller with precision control
   - Temperature sensors and compensation
   - Cost: $3,000

7. **Spindle system** (Section 2.8):
   - 7.5 kW water-cooled spindle
   - BT40 interface
   - Cost: $4,500

**Total project cost:** $18,000 (slightly over budget but achieves precision target)

**Expected performance:**
- Positioning accuracy: ±3 µm (exceeds target)
- Repeatability: ±2 µm
- Thermal drift: <3 µm/hour
- Maximum cutting force: 3000 N

## Common Pitfalls and Solutions

### Pitfall 1: Inadequate Counterbalancing

**Problem:** Motor oversized, continuous heating, thermal drift, poor servo response

**Solution:**
- Design counterbalance first, before selecting motor
- Aim for ±5% force balance across full travel
- Verify balance by releasing motor (with brake engaged for safety)

### Pitfall 2: Insufficient Column Stiffness

**Problem:** Excessive deflection under cutting forces, poor surface finish, chatter

**Solution:**
- Calculate deflection using cantilever formulas (Section 2.3)
- Target: <50 µm deflection under maximum expected load
- Increase cross-section depth (cubic relationship to stiffness)
- Add internal ribs if fabricated structure

### Pitfall 3: Thermal Drift Ignored

**Problem:** Parts out of tolerance after machine warms up, inconsistent dimensions

**Solution:**
- Implement warm-up procedure (30-60 minutes before precision work)
- Use water-cooled spindle for stability
- Add temperature sensor and software compensation for critical applications
- Insulate column from environment

### Pitfall 4: Poor Linear Guide Alignment

**Problem:** Binding during motion, premature wear, reduced accuracy

**Solution:**
- Machine column mounting surfaces flat (10-20 µm flatness)
- Use precision parallel during installation
- Check smooth motion by hand before final assembly
- Shim as needed to eliminate binding

### Pitfall 5: Brake Not Fail-Safe

**Problem:** Safety hazard—spindle can fall on power loss

**Solution:**
- Use spring-applied, electrically-released brake (fail-safe design)
- Size brake for 2-3× gravitational holding torque
- Test brake function before enabling motion
- Integrate brake into E-stop circuit

### Pitfall 6: Cable Management Neglected

**Problem:** Cables snag, break, or interfere with motion

**Solution:**
- Install proper cable carrier (Section 2.9)
- Route cables with adequate slack for full travel
- Separate power and signal cables
- Secure mounting at both ends with strain relief

## Best Practices Summary

**Design Phase:**
1. Start with moving mass budget—reduce weight first
2. Design counterbalance system—transforms motor sizing
3. Size column for stiffness—deflection limits, not strength
4. Select components with vertical-specific requirements in mind
5. Plan thermal management based on precision requirements
6. Design for fail-safe operation—brakes, redundancy

**Fabrication Phase:**
1. Machine mounting surfaces flat and parallel
2. Stress-relieve welded structures before final machining
3. Use precision tooling for assembly (parallel, indicators, height gauges)
4. Install components in logical sequence (column → rails → screw → carriage)
5. Check alignment at each step before proceeding

**Assembly Phase:**
1. Verify base mounting surface flat and square
2. Install column with dowel pins for location
3. Tram rails to within 20 µm parallelism
4. Align ball screw to carriage motion axis
5. Install counterbalance and verify balance
6. Route cables in cable carrier with proper strain relief

**Commissioning Phase:**
1. Mechanical verification first (stiffness, runout, backlash)
2. Electrical verification (motor phasing, encoder, brake)
3. Tune servo starting with conservative gains
4. Test in both directions for symmetric response
5. Validate performance against specifications
6. Document final configuration for future reference

## Continuing Education

### Recommended Next Steps

**Hands-on experience:**
- Build a Z-axis assembly (even small scale)
- Practice rail alignment and tramming techniques
- Tune servo system and observe response
- Measure thermal drift under realistic conditions

**Advanced topics:**
- 5-axis kinematics (Z-axis on tilting head)
- Adaptive control for variable loads
- High-speed machining considerations
- Ultra-precision machine design (sub-micron)

**Related skills:**
- FEA for structural analysis
- Thermal modeling and simulation
- Servo system theory and advanced tuning
- Metrology and precision measurement

### Resources

**Books:**
- *Precision Machine Design* by Alex Slocum (MIT)
- *Machine Tool Structures* by Koenigsberger & Tlusty
- *Fundamentals of Machine Elements* by Schmid & Hamrock

**Standards:**
- ISO 230 series (machine tool testing)
- ISO 13041 (machining center accuracy)
- ANSI B5 standards (machine tool accuracy)

**Online communities:**
- CNCZone forums (practical builders)
- Practical Machinist (professional machinists)
- LinuxCNC forums (control integration)

**Software:**
- FEA: SolidWorks Simulation, Fusion 360
- Thermal analysis: ANSYS, COMSOL
- Servo tuning: LinuxCNC, Mach4, industrial drives

## Final Thoughts

The vertical axis represents the apex of machine tool design challenges. Every engineering decision—from material selection to thermal management—must account for gravity's continuous influence. Yet this challenge also presents opportunity: a well-designed Z-axis demonstrates engineering excellence across multiple disciplines.

Key principles that ensure success:

**1. Respect gravity:** It's always there, always pulling down. Design with it, not against it.

**2. Counterbalance always:** The benefits compound—better motor sizing, lower thermal load, improved servo response, extended component life.

**3. Stiffness matters:** Deflection limits precision. Invest in structural rigidity.

**4. Thermal stability:** For precision work, thermal management is not optional.

**5. Safety first:** Fail-safe design, mechanical brakes, redundancy. The consequences of vertical axis failure are severe.

**6. Integration mindset:** The Z-axis doesn't exist in isolation—it connects to frame, electronics, software, and process. Design accordingly.

This module has equipped you with the engineering foundation to design, build, and commission vertical axes for CNC machines. Combined with knowledge from other modules, you now possess a complete understanding of CNC machine design from first principles.

Welcome to the world of vertical axis engineering. May your Z-axes be stiff, balanced, and thermally stable.

***

**Previous**: [Section 2.11 – Testing and Commissioning](section-2.11-testing-commissioning.md)

**Next Module**: [Module 3 – Linear Motion Systems](../Module-03/module-03-linear-motion.md)

**Return to**: [Module 2 Overview](module-2-vertical-axis.md)
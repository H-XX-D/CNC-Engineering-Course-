# 20.6 Material-Specific Parameters

## Introduction

Different materials have vastly different machining characteristics. This section provides detailed parameter recommendations for common materials encountered in CNC machining.

**Material properties affecting machinability**:
- Hardness (resistance to cutting)
- Thermal conductivity (heat dissipation)
- Work hardening rate (surface hardening during cutting)
- Abrasiveness (tool wear rate)
- Chip formation characteristics

## Aluminum Alloys

### Material Characteristics

**Advantages**:
- Excellent machinability (200% rating vs 1018 steel)
- High thermal conductivity (dissipates heat well)
- Low cutting forces
- Good surface finish achievable
- Non-ferrous (can use PCD tools)

**Challenges**:
- Soft/gummy (can build up on tool edge)
- Long stringy chips (evacuation issues)
- Thermal expansion (dimensional control in precision work)

### Common Aluminum Alloys

**2024 (Aerospace)**:
- Machinability: Good
- Higher strength, lower ductility than 6061
- Slightly more difficult to machine

**6061 (General Purpose)**:
- Machinability: Excellent
- Most common structural aluminum
- Easy to machine, good finish

**7075 (High Strength)**:
- Machinability: Good
- Higher strength than 6061
- Machines similarly to 6061

**Cast Aluminum (A356, 319)**:
- Machinability: Fair to Good
- Contains silicon (abrasive)
- May have porosity
- Reduce speeds 20-30% vs wrought aluminum

### Recommended Parameters - Aluminum

**Cutting Speed**:
- HSS: 200-400 SFM
- Carbide: 600-1200 SFM
- PCD: 1500-4000 SFM (production environments)

**Feed Per Tooth**:
- Roughing: 0.008-0.015"
- Finishing: 0.003-0.006"

**Depth of Cut**:
- Roughing ADOC: 1.0-1.5× diameter
- Roughing WOC: 40-60% stepover
- Finishing: Light passes (0.020-0.060" radial)

**Example - 1/2" Endmill in 6061**:
- V = 900 SFM → N = 6876 RPM
- f_z = 0.010" (roughing)
- Z = 3 flutes (preferred for aluminum)
- F = 0.010 × 3 × 6876 = 206 IPM
- ADOC = 0.50", WOC = 0.25" (50%)
- MRR = 0.50 × 0.25 × 206 = 25.75 in³/min

### Tool Selection - Aluminum

**Endmills**:
- 2-3 flutes preferred (large chip gullets)
- High helix angle (40-50°)
- Polished flutes (reduces buildup)
- Sharp edge geometry
- Uncoated carbide or PCD

**Coatings**:
- Generally NOT recommended (promotes buildup)
- Exception: ZrN (zirconium nitride) works well
- PCD for high-volume production (100× tool life)

**Speeds/Feeds Philosophy**:
- Run fast and aggressive
- High RPM, high feed rates
- Deep ADOC, moderate WOC

### Coolant - Aluminum

**Options**:
1. **Flood coolant** (preferred for production)
   - Water-soluble oil or synthetic
   - Good chip evacuation
   - Prevents buildup

2. **Air blast** (good for hobby/small machines)
   - Clears chips effectively
   - No mess
   - High speeds keep tool cool

3. **Mist coolant** (compromise)
   - Some cooling, good chip clearing

**Never dry**: Aluminum can build up on tool (BUE), poor finish

### Common Issues - Aluminum

**Built-Up Edge (BUE)**:
- Aluminum welding to cutting edge
- **Solution**: Increase cutting speed, improve coolant, use polished tools

**Burrs**:
- Soft material tends to tear at exits
- **Solution**: Sharp tools, climb milling, light final passes, chamfer edges

**Poor Finish**:
- Usually from BUE or chip recutting
- **Solution**: Higher speeds, better chip evacuation, sharp tools

## Steel - Low Carbon (1018, A36, 12L14)

### Material Characteristics

**1018 Cold Rolled**:
- Machinability: 70% rating
- General-purpose mild steel
- Moderate cutting forces
- Good surface finish achievable

**12L14 (Free-Machining)**:
- Machinability: 170% rating (excellent)
- Sulfur added for chip breaking
- Best choice when machinability matters
- Slightly lower strength than 1018

**A36 (Structural)**:
- Machinability: 65% rating
- Hot rolled (scale on surface)
- Variable hardness
- More difficult than 1018

### Recommended Parameters - Mild Steel

**Cutting Speed**:
- HSS: 90-120 SFM
- Uncoated carbide: 250-350 SFM
- Coated carbide: 350-500 SFM

**Feed Per Tooth**:
- Roughing: 0.005-0.010"
- Finishing: 0.002-0.004"

**Depth of Cut**:
- Roughing ADOC: 0.5-1.0× diameter
- Roughing WOC: 40-50% stepover
- Finishing: 0.010-0.030" radial

**Example - 1/2" Coated Carbide in 1018**:
- V = 400 SFM → N = 3056 RPM
- f_z = 0.006" (roughing)
- Z = 4 flutes
- F = 0.006 × 4 × 3056 = 73 IPM
- ADOC = 0.50", WOC = 0.20" (40%)
- MRR = 0.50 × 0.20 × 73 = 7.3 in³/min

### Tool Selection - Mild Steel

**Endmills**:
- 4 flutes standard
- 30-35° helix angle
- TiAlN coating recommended
- Variable pitch reduces chatter

**Coolant**:
- Flood coolant strongly recommended
- Water-soluble oil or synthetic
- Improves tool life 2-3×

### Common Issues - Mild Steel

**Built-Up Edge**:
- Occurs at moderate speeds (100-200 SFM)
- **Solution**: Increase to 350+ SFM with carbide, use coolant

**Work Hardening** (A36, hot rolled):
- Surface harder than core
- **Solution**: Take heavier first cut (get through hardened layer), sharp tools

## Steel - Medium/High Carbon (1045, 4140, 4340)

### Material Characteristics

**1045**:
- Machinability: 60% rating
- Medium carbon (0.45% C)
- Harder than 1018, more wear resistant
- Heat treatable

**4140 (Alloy Steel)**:
- Machinability: 50% rating (annealed), 20-30% (hardened)
- Chromium-molybdenum alloy
- Very common for high-strength parts
- Machines well when annealed (< 28 HRC)

**4340 (High-Strength Alloy)**:
- Machinability: 45% rating
- Nickel-chromium-molybdenum alloy
- Tougher than 4140
- More difficult to machine

### Recommended Parameters - Alloy Steel

**Cutting Speed** (annealed condition):
- HSS: 50-80 SFM
- Uncoated carbide: 150-250 SFM
- Coated carbide: 250-400 SFM

**Feed Per Tooth**:
- Roughing: 0.004-0.008"
- Finishing: 0.001-0.003"

**Depth of Cut**:
- Roughing ADOC: 0.4-0.8× diameter
- Roughing WOC: 30-40% stepover
- More conservative than mild steel

**Example - 1/2" Coated Carbide in 4140 (Annealed)**:
- V = 300 SFM → N = 2292 RPM
- f_z = 0.005" (roughing)
- Z = 4 flutes
- F = 0.005 × 4 × 2292 = 46 IPM
- ADOC = 0.40", WOC = 0.15" (30%)
- MRR = 0.40 × 0.15 × 46 = 2.76 in³/min

### Hardened Steel (> 45 HRC)

**When to machine vs grind**:
- < 55 HRC: Carbide tools possible (difficult)
- 55-65 HRC: CBN or ceramic tools (hard turning)
- > 65 HRC: Grinding typically required

**Hard Turning Parameters** (CBN):
- V = 200-400 SFM
- Feed: 0.003-0.008 IPR
- DOC: 0.010-0.040"
- Light cuts, high precision

**Hard Milling** (65 HRC):
- V = 50-150 SFM
- f_z = 0.001-0.003"
- ADOC: 0.05-0.15× diameter (very light)
- Multiple passes required

## Stainless Steel

### Material Characteristics

**Challenges**:
- Work hardens rapidly during cutting
- Low thermal conductivity (heat concentrates at tool)
- Gummy/stringy chips
- Abrasive (high tool wear)

**Types**:
- **300 series** (304, 316): Austenitic, non-magnetic, most difficult
- **400 series** (416, 430): Martensitic/ferritic, easier to machine
- **17-4 PH**: Precipitation hardened, moderate machinability

### Recommended Parameters - 304 Stainless

**Cutting Speed**:
- HSS: 40-60 SFM
- Uncoated carbide: 100-150 SFM
- Coated carbide (TiAlN): 150-250 SFM

**Feed Per Tooth**:
- Roughing: 0.003-0.006"
- Finishing: 0.001-0.003"
- **Critical**: Must maintain minimum chip load (avoid work hardening)

**Depth of Cut**:
- Roughing ADOC: 0.3-0.6× diameter
- Roughing WOC: 30-40% stepover
- Conservative approach required

**Example - 1/2" TiAlN Coated in 304 SS**:
- V = 180 SFM → N = 1375 RPM
- f_z = 0.004" (roughing)
- Z = 4 flutes
- F = 0.004 × 4 × 1375 = 22 IPM
- ADOC = 0.25", WOC = 0.15" (30%)
- MRR = 0.25 × 0.15 × 22 = 0.83 in³/min

### Tool Selection - Stainless

**Requirements**:
- Sharp tools mandatory
- Positive rake geometry
- TiAlN or AlCrN coating
- Chip breaker geometry

**Strategy**:
- Never dwell (work hardening)
- Constant feed through cut
- Adequate chip load always
- Flood coolant essential

### Common Issues - Stainless

**Rapid Tool Wear**:
- Heat concentration
- **Solution**: Reduce speed 20%, ensure adequate feed, flood coolant

**Work Hardening**:
- Previous cuts harden surface
- **Solution**: Heavier cuts to get below hardened layer, sharp tools, no rubbing

**Poor Finish**:
- Gummy material tears
- **Solution**: Sharp tools, climb milling, adequate coolant

## Titanium Alloys

### Material Characteristics

**Ti-6Al-4V (Grade 5)** - Most Common:
- Machinability: 20% rating (very difficult)
- Low thermal conductivity (5× worse than steel)
- High chemical reactivity with tool materials
- High strength at elevated temperatures
- Springy (elastic deflection during cutting)

**Challenges**:
- Heat concentrates at tool edge
- Tools wear rapidly
- Can catch fire if chips accumulate
- Expensive material (minimize scrap)

### Recommended Parameters - Ti-6Al-4V

**Cutting Speed**:
- HSS: 40-60 SFM (not recommended)
- Uncoated carbide: 150-250 SFM
- Coated carbide: 200-350 SFM

**Feed Per Tooth**:
- Roughing: 0.003-0.006"
- Finishing: 0.001-0.003"
- Adequate chip load critical

**Depth of Cut**:
- Roughing ADOC: 0.2-0.5× diameter (conservative)
- Roughing WOC: 20-40% stepover
- Avoid heavy cuts (heat buildup)

**Example - 1/2" Coated Carbide in Ti-6Al-4V**:
- V = 250 SFM → N = 1910 RPM
- f_z = 0.004" (roughing)
- Z = 4 flutes
- F = 0.004 × 4 × 1910 = 31 IPM
- ADOC = 0.20", WOC = 0.15" (30%)
- MRR = 0.20 × 0.15 × 31 = 0.93 in³/min

### Tool Selection - Titanium

**Requirements**:
- Very sharp tools
- Positive rake geometry
- Carbide substrate (K or M grade)
- TiAlN or AlCrN coating

**Strategy**:
- Sharp tools, replace frequently
- Moderate speeds (not too fast - heat; not too slow - work hardening)
- Adequate feed always
- Copious coolant (flood, high pressure)

### Coolant - Titanium

**Critical for success**:
- Flood coolant mandatory
- High pressure (300+ PSI) if available
- Never dry cut (fire hazard)
- Never water-based (hydrogen embrittlement risk, fire risk)
- Use mineral oil or approved synthetic

### Safety - Titanium

**Fire Hazard**:
- Fine chips can ignite spontaneously
- Burns at 3000°F
- Water accelerates fire
- **Prevention**: Regular chip removal, no accumulation, Class D extinguisher available

## Cast Iron

### Material Characteristics

**Gray Cast Iron**:
- Machinability: Excellent (80-100% rating)
- Brittle chips (easy evacuation)
- Graphite flakes act as lubricant
- Abrasive (carbides in structure)
- Dry cutting preferred

**Ductile/Nodular Iron**:
- Machinability: Good (60-80%)
- More ductile than gray iron
- Stronger but slightly harder to machine

### Recommended Parameters - Gray Cast Iron

**Cutting Speed**:
- HSS: 60-100 SFM
- Uncoated carbide: 300-500 SFM
- Ceramic: 1000-2500 SFM (finishing)

**Feed Per Tooth**:
- Roughing: 0.006-0.012"
- Finishing: 0.003-0.006"
- Can use aggressive feeds

**Depth of Cut**:
- Roughing ADOC: 0.5-1.2× diameter
- Roughing WOC: 40-60% stepover

**Example - 1/2" Carbide in Gray Cast Iron**:
- V = 400 SFM → N = 3056 RPM
- f_z = 0.008" (roughing)
- Z = 4 flutes
- F = 0.008 × 4 × 3056 = 98 IPM
- ADOC = 0.50", WOC = 0.25" (50%)
- MRR = 0.50 × 0.25 × 98 = 12.25 in³/min

### Tool Selection - Cast Iron

**Endmills**:
- Uncoated carbide or ceramic
- 4 flutes standard
- Wear-resistant grade (K grade carbide)

**Coolant**:
- **Dry cutting preferred** (graphite self-lubricates)
- Air blast for chip clearing acceptable
- If coolant used: Light mist only (flood causes thermal shock)

### Common Issues - Cast Iron

**Abrasive Wear**:
- Hard carbides wear tools
- **Solution**: Use harder tool grades (ceramic for finishing), expect shorter tool life than steel

**Hard Spots**:
- White cast iron areas (very hard)
- **Solution**: Reduce speed 30%, sharp tools, carbide required

## Plastics and Composites

### Acrylic (PMMA)

**Characteristics**:
- Easy to machine
- Brittle (chips, not cracks)
- Melts if too slow or dull tools

**Parameters**:
- V = 500-1000 SFM
- f_z = 0.005-0.012"
- Sharp tools, high speed

**Coolant**:
- Air blast or dry
- Coolant optional (prevents melting in deep cuts)

### Delrin (Acetal)

**Characteristics**:
- Excellent machinability
- Tough, slippery
- Machines like aluminum

**Parameters**:
- V = 600-1200 SFM
- f_z = 0.006-0.015"
- Standard carbide tools

### Nylon (Polyamide)

**Characteristics**:
- Soft, gummy
- Absorbs moisture (dimensional changes)
- Builds up on tools

**Parameters**:
- V = 400-800 SFM
- f_z = 0.004-0.010"
- Sharp tools, high rake angles

### Carbon Fiber / Fiberglass Composites

**Characteristics**:
- Extremely abrasive
- Delamination risk
- Health hazard (dust control critical)

**Parameters**:
- V = 400-600 SFM (carbide), 800-1500 SFM (PCD)
- f_z = 0.002-0.006"
- Light ADOC to prevent delamination

**Tool Requirements**:
- PCD (diamond) strongly recommended
- Carbide wears out quickly (20% of life vs aluminum)
- Sharp tools prevent delamination

**Safety**:
- Dust collection mandatory
- Respiratory protection
- Skin/eye protection

## Exotic Alloys (Inconel, Hastelloy)

### Inconel 718

**Characteristics**:
- Machinability: 10% rating (extremely difficult)
- Extreme work hardening
- High strength at temperature
- Retains hardness even when red-hot

**Parameters**:
- V = 50-120 SFM (carbide)
- V = 200-400 SFM (ceramic)
- V = 300-600 SFM (CBN)
- f_z = 0.002-0.005"
- ADOC: 0.1-0.3× diameter (very light)

**Strategy**:
- Ceramic or CBN tools for production
- Extremely sharp carbide for limited runs
- Very rigid setup
- Flood coolant, high pressure
- Expect high tool wear

### Hastelloy C-276

**Similar to Inconel**:
- Extremely difficult
- Work hardens rapidly
- Low speeds, light cuts
- Carbide or ceramic tools

## Material Comparison Table

| Material | Machinability | Cutting Speed (Carbide) | Feed/Tooth | Tool Life | Difficulty |
|----------|---------------|-------------------------|------------|-----------|------------|
| Aluminum 6061 | 200% | 600-1200 SFM | 0.008-0.015" | Excellent | Easy |
| Brass | 300% | 400-800 SFM | 0.005-0.012" | Excellent | Very Easy |
| 1018 Steel | 70% | 250-350 SFM | 0.005-0.010" | Good | Moderate |
| 4140 Steel | 50% | 150-250 SFM | 0.004-0.008" | Moderate | Moderate |
| 304 Stainless | 40% | 100-150 SFM | 0.003-0.006" | Poor | Difficult |
| Ti-6Al-4V | 20% | 150-250 SFM | 0.003-0.006" | Poor | Very Difficult |
| Cast Iron | 80% | 300-500 SFM | 0.006-0.012" | Moderate | Easy |
| Inconel 718 | 10% | 50-120 SFM | 0.002-0.005" | Very Poor | Extremely Difficult |

## Summary

**Key takeaways by material family**:

**Aluminum**: Run fast and aggressive, worry about chip evacuation and buildup

**Mild Steel**: Standard parameters, coated carbide and coolant recommended

**Alloy Steel**: More conservative, sharp tools, adequate coolant critical

**Stainless**: Work hardening major concern, never rub, maintain chip load, sharp tools

**Titanium**: Heat management critical, expensive material demands care, safety concerns

**Cast Iron**: Easy to machine but abrasive, dry cutting preferred

**Plastics**: Sharp tools prevent melting, high speeds, watch for material-specific issues

**Exotics (Inconel)**: Specialized tooling required, expect high costs and slow machining

**General strategy**:
1. Identify material and condition (annealed, hardened, etc.)
2. Start with conservative parameters from this guide
3. Test cut and monitor tool wear, finish, forces
4. Optimize gradually based on results
5. Document successful parameters for future jobs

---

**Next**: [20.7 Tool Material Selection](section-20.7-tool-materials.md)

---

# 20.5 Depth of Cut and Width of Cut

## Terminology

**Depth of Cut (DOC)**: Also called Axial Depth of Cut (ADOC)
- The distance the tool plunges into material along its axis
- Vertical engagement in milling
- For endmills: How deep the tool cuts in Z-axis

**Width of Cut (WOC)**: Also called Radial Depth of Cut (RDOC)
- The distance the tool steps over laterally
- Horizontal engagement in milling
- For endmills: How much material engages the tool radially

**Stepover**: WOC expressed as percentage of tool diameter
- Example: 0.100" WOC with 0.500" endmill = 20% stepover

## Depth of Cut Guidelines

### General Recommendations

**Roughing Operations**:
- ADOC: 0.5× to 1.5× tool diameter
- Goal: Maximum material removal
- Deep cuts, light stepover preferred

**Finishing Operations**:
- ADOC: 0.010-0.100" (0.25-2.5mm)
- Goal: Final dimensions and surface finish
- Light cuts in all directions

### By Tool Type

**Square Endmills**:
- Maximum ADOC: Up to 1.5× diameter
- Typical roughing: 0.5-1.0× diameter
- Limited by flute length

**Example**: 1/2" endmill
- Maximum: 0.75" ADOC
- Typical: 0.25-0.50" ADOC

**Ball Endmills**:
- ADOC limited by effective diameter at depth
- Surface finish degrades with deep axial cuts
- Typical: 0.05-0.25× diameter for finishing

**Roughing Endmills** (corn cob):
- Serrated edges reduce cutting forces
- Can handle 2-3× diameter ADOC
- Designed for aggressive roughing

**Face Mills**:
- ADOC typically light: 0.060-0.200" per pass
- Wide coverage (WOC) compensates
- Multiple inserts share load

### By Material

**Aluminum**:
- Can handle deep cuts (1.0-1.5× diameter)
- Low cutting forces
- Excellent chip evacuation needed

**Mild Steel**:
- Moderate: 0.5-1.0× diameter
- Balance between MRR and tool life

**Stainless Steel**:
- Conservative: 0.3-0.6× diameter
- Work hardening concern with heavy cuts
- Reduce ADOC, increase feed per tooth

**Titanium**:
- Light: 0.2-0.5× diameter
- Low thermal conductivity
- Heat builds up quickly in deep cuts

**Cast Iron**:
- Moderate to deep: 0.5-1.2× diameter
- Abrasive but low cutting forces
- Dry cutting preferred

**Hardened Steel (>50 HRC)**:
- Very light: 0.05-0.15× diameter
- Carbide or CBN tools
- Multiple light passes

## Width of Cut Guidelines

### Slotting vs Side Milling

**Full Slotting** (WOC = 100% of diameter):
- Most demanding operation
- Both sides of tool engaged
- Poor chip evacuation
- Reduce feed rate 40-60%
- Avoid if possible

**Side Milling** (WOC < 50% of diameter):
- Preferred approach
- Better chip evacuation
- Lower cutting forces
- Standard feed rates applicable

**High-Speed Machining** (WOC < 20% of diameter):
- Light radial engagement
- Very high feed rates possible (chip thinning)
- Longer tool life
- Faster overall with multiple passes

### Recommended Stepover Percentages

**Roughing**:
- Standard: 40-60% of diameter
- Aggressive (aluminum): 50-75%
- Conservative (hard materials): 25-40%

**Semi-Finishing**:
- 20-40% of diameter
- Balance between MRR and finish

**Finishing**:
- 5-20% of diameter
- Often just 0.010-0.030" radial stock

**Example - 1/2" Endmill**:
- Roughing: 0.200-0.300" WOC (40-60%)
- Semi-finish: 0.100-0.200" WOC (20-40%)
- Finish: 0.025-0.100" WOC (5-20%)

### Climb vs Conventional Milling

**Climb Milling** (down milling):
- Tool rotation matches feed direction
- Chip thickness: thick to thin
- Advantages:
  - Better surface finish
  - Longer tool life
  - Less work hardening
  - Chips evacuate behind tool
- Disadvantages:
  - Requires backlash elimination
  - Can pull workpiece if not secured
  - Higher entry force

**Conventional Milling** (up milling):
- Tool rotation opposes feed direction
- Chip thickness: thin to thick
- Advantages:
  - Works with backlash in machine
  - Pushes work into table
  - Lower entry force
- Disadvantages:
  - Poorer surface finish
  - More work hardening
  - Shorter tool life
  - Chips evacuate toward tool

**Recommendation**: Use climb milling whenever possible (CNC with ballscrews)

## Material Removal Rate Optimization

### MRR Formula

$$MRR = ADOC \times WOC \times F$$

where all dimensions in same units (inches or mm)

**Example**:
- ADOC = 0.200"
- WOC = 0.300"
- F = 40 IPM
$$MRR = 0.200 \times 0.300 \times 40 = 2.4 \text{ in³/min}$$

### Optimization Strategy

**To maximize MRR while minimizing tool wear**:

Priority order for increasing parameters:
1. **Increase ADOC first** (least effect on tool life)
2. **Increase feed rate second** (moderate effect)
3. **Increase WOC third** (significant effect due to engagement angle)
4. **Increase cutting speed last** (greatest effect on tool life)

**Example comparison** - Target MRR = 3.0 in³/min:

**Option A**: ADOC = 0.5", WOC = 0.2", F = 30 IPM
**Option B**: ADOC = 0.2", WOC = 0.5", F = 30 IPM

Both achieve same MRR, but Option A (deep, narrow) produces:
- Lower cutting forces (less radial engagement)
- Better tool life
- Better surface finish (climb milling easier)

**Best practice**: "Deep and narrow" over "shallow and wide"

### Power-Limited Machining

**Maximum MRR from available power**:

$$MRR_{max} = \frac{P \times \eta}{U}$$

where:
- $P$ = spindle power (hp or kW)
- $\eta$ = efficiency (0.70-0.85 typical)
- $U$ = specific cutting energy (hp/(in³/min) or kW/(cm³/s))

**Example**:
3 HP spindle machining 1018 steel:
- U = 0.7 hp/(in³/min)
- η = 0.8
$$MRR_{max} = \frac{3 \times 0.8}{0.7} = 3.4 \text{ in³/min}$$

**Select DOC/WOC/F combination that achieves ~3 in³/min** (safety margin)

## Advanced Strategies

### Trochoidal Milling

**Technique**: Circular tool path with constant light radial engagement

**Parameters**:
- WOC: 5-15% of tool diameter
- ADOC: 1.0-2.0× tool diameter (deeper than conventional)
- Feed rate: 2-4× conventional (chip thinning compensation)

**Advantages**:
- Eliminates full slotting
- Constant tool loading
- Excellent chip evacuation
- Longer tool life (50-200%)
- Can machine full-depth slots efficiently

**Example - 1/2" Endmill**:
- Conventional slotting: ADOC = 0.25", WOC = 0.5", F = 20 IPM (reduced for slot)
- Trochoidal: ADOC = 0.75", WOC = 0.05", F = 60 IPM (much faster!)

**CAM software** generates trochoidal toolpaths automatically

### Adaptive Roughing

**Technique**: CAM varies WOC to maintain constant tool loading

**How it works**:
- Calculates engagement angle at every point
- Adjusts WOC to keep engagement constant
- Feed rate may also vary

**Advantages**:
- Maximum safe MRR throughout toolpath
- No sudden load changes (longer tool life)
- Fewer tool breakages
- 30-60% faster than conventional roughing

**Parameters**:
- Target engagement: 90-120° (vs 180° in slotting)
- ADOC: Aggressive (0.75-1.5× diameter)
- Feed rate: Optimized for target engagement

**Example**:
Pocketing with 1/2" endmill:
- Open area: WOC increases automatically (wider cuts)
- Corners: WOC decreases automatically (prevents overload)
- Constant cutting force maintained

### High-Speed Machining (HSM)

**Philosophy**: Many light passes at very high feed rates

**Parameters**:
- WOC: 5-20% of diameter (very light radial)
- ADOC: 0.25-0.75× diameter (moderate to deep)
- Feed rate: 2-5× conventional (compensate chip thinning)
- Cutting speed: 1.5-2× conventional

**Advantages**:
- Lower cutting forces (despite high feed)
- Better surface finish
- Longer tool life
- Less heat in workpiece (for aluminum)
- Can machine thin walls without deflection

**Requirements**:
- High-speed spindle (>15,000 RPM)
- Rigid machine
- CAM software with HSM toolpaths
- Sharp tools

**Example - Aluminum Part**:
- Conventional: WOC = 0.3", ADOC = 0.3", F = 80 IPM, V = 800 SFM
- HSM: WOC = 0.05", ADOC = 0.5", F = 300 IPM, V = 1200 SFM
- Result: Faster cycle time, better finish, longer tool life

### Dynamic Milling

**Combination of**:
- Trochoidal tool motion
- Adaptive engagement control
- High-speed machining principles

**Result**: Optimal performance across all scenarios

## Depth of Cut in Other Operations

### Turning

**DOC in turning**: Radial depth (amount removed from diameter)

**Roughing**:
- 0.060-0.200" DOC (0.120-0.400" off diameter)
- Limited by rigidity and power

**Finishing**:
- 0.005-0.030" DOC (0.010-0.060" off diameter)
- Surface finish priority

**Example**:
Turning 2.000" diameter to 1.500" (0.500" total):
- Roughing: 4 passes at 0.120" DOC = 0.480" removed
- Finishing: 1 pass at 0.020" DOC = 0.020" removed
- Final diameter: 1.500"

### Drilling

**DOC**: Not typically varied (drill diameter determines)

**Peck depth**: How far drill advances before retracting
- Standard drilling: Full depth, no pecking
- Deep holes (>3× diameter): Peck 0.5-1.0× diameter
- Very deep: Peck 0.25-0.5× diameter

**Example**: 1/4" drill, 2" deep hole
- Hole depth / diameter = 8:1 (deep)
- Peck depth = 0.25" (1× diameter)
- 8 pecks required

### Face Milling

**DOC**: Axial depth per pass

**Roughing**:
- 0.080-0.200" per pass
- Multiple passes to reach depth

**Finishing**:
- 0.020-0.060" per pass
- Often single pass for final dimension

**Large face mills** (>3"):
- Can take heavier DOC (more inserts)
- 0.150-0.300" roughing passes common

## Troubleshooting

### Problem: Tool Deflection / Poor Accuracy

**Symptoms**:
- Dimensions wrong (undersize pockets, oversize bosses)
- Taper in walls
- Poor surface finish on walls

**Likely causes**:
1. WOC too large (excessive side force)
2. Tool overhang too long
3. Feed rate too high

**Solutions**:
- Reduce WOC to 25-40% of diameter
- Reduce tool overhang if possible
- Reduce feed rate 20-30%
- Use larger diameter tool if clearance allows
- Take spring pass (no WOC, just trace final path)

### Problem: Tool Breakage

**Symptoms**: Catastrophic tool failure

**Likely causes**:
1. Full slotting (WOC = 100%)
2. ADOC too large for tool
3. Feed rate too high

**Solutions**:
- Avoid full slotting (use trochoidal or pre-drill)
- Reduce ADOC to 0.5× diameter or less
- Reduce feed rate 40-60%
- Use roughing endmill for heavy cuts

### Problem: Poor Surface Finish

**Symptoms**: Rough walls, chatter marks

**Likely causes**:
1. Too much WOC for finishing
2. Dull tool
3. Vibration

**Solutions**:
- Reduce WOC to 5-15% for finishing
- Replace tool
- Reduce tool overhang
- Change RPM ±15% to avoid resonance

### Problem: Slow Cycle Time

**Symptoms**: Machining takes too long

**Solutions**:
1. Increase ADOC (if not at limit)
2. Increase WOC to 50-60%
3. Increase feed rate (check minimum chip load)
4. Consider adaptive or trochoidal strategies
5. Increase cutting speed (monitor tool life)

### Problem: Excessive Tool Wear

**Symptoms**: Tools dull quickly, frequent changes

**Solutions**:
- Reduce WOC (radial engagement major factor)
- Reduce cutting speed 20-30%
- Ensure climb milling (not conventional)
- Improve coolant flow
- Check for work hardening (stainless)

## Practical Examples

### Example 1: Pocket Roughing in Aluminum

**Setup**:
- Material: 6061 Aluminum
- Pocket: 3" × 3" × 0.75" deep
- Tool: 1/2" 3-flute carbide endmill

**Strategy**: Deep cuts, moderate stepover

**Parameters**:
- ADOC: 0.50" (1× diameter)
- WOC: 0.25" (50% stepover)
- RPM: 6000
- Feed: 180 IPM (f_z = 0.010")

**Toolpath**:
- 2 passes in depth (0.50" + 0.25")
- Spiral entry, climb milling
- ~12 passes across width

**Cycle time**: ~8 minutes

### Example 2: Steel Part Finishing

**Setup**:
- Material: 1018 Steel
- Operation: Finish walls to size
- Stock remaining: 0.030" radial
- Tool: 1/2" 4-flute carbide endmill

**Strategy**: Light finishing passes

**Parameters**:
- ADOC: 0.75" (full depth, one pass)
- WOC: 0.015" radial (single spring pass)
- RPM: 2700
- Feed: 22 IPM (f_z = 0.002")

**Toolpath**:
- Climb milling critical for finish
- Constant Z height
- Two passes: 0.015" + spring pass (0.000")

### Example 3: Slotting Stainless Steel

**Setup**:
- Material: 304 Stainless
- Feature: 0.50" wide × 1.5" deep slot
- Tool: 1/2" 4-flute carbide endmill (coated)

**Problem**: Full slotting required (part geometry)

**Strategy**: Reduce parameters for slotting

**Parameters**:
- ADOC: 0.20" (conservative for slotting)
- WOC: 0.50" (100%, unavoidable)
- RPM: 2000
- Feed: 16 IPM (f_z = 0.002", reduced 50% for slot)

**Toolpath**:
- Plunge in center (or ramp down)
- 8 depth passes (0.20" × 7 + 0.10" final)
- Climb mill on one side, conventional on other (unavoidable in slot)

**Alternative**: Trochoidal slotting
- ADOC: 0.60" (3× deeper!)
- WOC: 0.05" (10%, circular path)
- Feed: 60 IPM (4× faster!)
- Faster overall despite more passes

### Example 4: Face Milling Cast Iron

**Setup**:
- Material: Gray cast iron
- Operation: Face large area (10" × 10")
- Tool: 3" face mill, 6 inserts

**Parameters**:
- ADOC: 0.100" per pass
- WOC: 2.7" (90% of diameter, efficient)
- RPM: 500
- Feed: 24 IPM (f_z = 0.008")

**Toolpath**:
- 4 passes to cover width (with 10% overlap)
- Dry cutting (no coolant)
- ~5 minutes per 0.100" depth

## Summary

**Key principles**:
1. Deep and narrow (high ADOC, low WOC) better than shallow and wide
2. Avoid full slotting when possible (worst case for tool)
3. Finishing requires light WOC (5-20% of diameter)
4. Climb milling preferred over conventional
5. MRR = ADOC × WOC × F (optimize all three)

**Optimization priorities**:
1. Increase ADOC (least tool wear impact)
2. Increase feed rate
3. Increase WOC
4. Increase cutting speed (most tool wear impact)

**Advanced strategies**:
- Trochoidal milling: Constant light engagement, deep cuts
- Adaptive roughing: CAM maintains constant loading
- HSM: Very light WOC, very high feed rates

**Decision framework**:
1. Determine operation type (roughing vs finishing)
2. Select ADOC based on tool size and material
3. Select WOC based on strategy (avoid full slotting)
4. Calculate MRR, check against machine power
5. Adjust parameters based on test cuts
6. Document optimal values for production

---

**Next**: [20.6 Material-Specific Parameters](section-20.6-material-parameters.md)

---

# 20.7 Tool Material Selection

## Overview

Cutting tool materials have evolved dramatically since the early days of machining. Selection depends on workpiece material, cutting conditions, and economic considerations.

**Tool material properties required**:
- **Hardness**: Must be harder than workpiece at cutting temperature
- **Toughness**: Resist fracture from impact and interrupted cuts
- **Wear resistance**: Maintain sharp edge under abrasion
- **Hot hardness**: Retain hardness at elevated temperatures
- **Chemical stability**: Resist diffusion and reaction with workpiece

**Trade-off**: Hardness vs toughness (cannot maximize both simultaneously)

## High-Speed Steel (HSS)

### Composition and Properties

**Typical composition (M2 grade)**:
- Iron base
- 18% Tungsten (or 5% Molybdenum in M42)
- 4% Chromium
- 1% Vanadium
- 0.8% Carbon

**Properties**:
- Hardness: 63-65 HRC
- Fracture toughness: Excellent (best of all tool materials)
- Hot hardness: Retains hardness to ~1000°F (540°C)
- Thermal conductivity: Moderate
- Cost: Low ($5-20 per tool)

### Types of HSS

**M-Series** (Molybdenum-based):
- M2: General purpose (most common)
- M42: Cobalt added (8%), better hot hardness
- M7: High molybdenum (8.75%), general purpose

**T-Series** (Tungsten-based):
- T1, T15: Higher tungsten content
- Better wear resistance, more expensive
- Less common today

**Powder Metallurgy HSS**:
- PM manufacturing process
- Finer, more uniform grain structure
- Better wear resistance and toughness
- 2-3× cost of conventional HSS

### Applications - HSS

**Best for**:
- Drilling (toughness critical)
- Tapping (high torque, shock loads)
- Reamers (long tool life needed)
- Complex form tools (grinding cost high)
- Interrupted cuts (milling slots, keyways)
- Low-speed operations (<200 SFM in steel)
- Hobby/DIY (low cost, can be resharpened)

**Not suitable for**:
- High-speed production (too slow)
- Hard materials (>35 HRC)
- High-temperature alloys

### Cutting Speeds - HSS

Compared to carbide, HSS runs at 50% of speed:

| Material | HSS Speed | Carbide Speed |
|----------|-----------|---------------|
| Aluminum | 200-400 SFM | 600-1200 SFM |
| Mild Steel | 90-120 SFM | 250-500 SFM |
| Stainless | 40-60 SFM | 150-250 SFM |
| Cast Iron | 60-100 SFM | 300-500 SFM |

## Cemented Carbide

### Composition and Properties

**Structure**:
- Tungsten carbide (WC) particles (90-95%)
- Cobalt (Co) binder (5-10%)
- Other carbides (TiC, TaC, NbC) for specific properties

**Manufacturing**:
- Powder metallurgy
- Pressed and sintered at 2500°F
- Very hard ceramic particles in tough metal matrix

**Properties**:
- Hardness: 90-93 HRA (much harder than HSS)
- Hot hardness: Retains hardness to ~1400°F (760°C) uncoated
- Thermal conductivity: Excellent (3× better than HSS)
- Fracture toughness: Good (but less than HSS)
- Cost: Medium ($20-80 per insert/tool)

### ISO Carbide Classification

**C1-C4 Grades** (Steel Cutting):
- **Higher cobalt content** (10-12%)
- **More tough**, less wear-resistant
- For steel (ferrous, non-abrasive)
- Can handle interrupted cuts

**C5-C8 Grades** (Cast Iron / Non-Ferrous):
- **Lower cobalt content** (3-6%)
- **Harder**, more wear-resistant, more brittle
- For cast iron, aluminum, non-ferrous
- Continuous cuts preferred

**ISO Color Code System**:

| Code | Color | Application | Characteristics |
|------|-------|-------------|-----------------|
| P | Blue | Steel, long chips | Tough, less wear-resistant |
| M | Yellow | Stainless steel | Versatile, intermediate properties |
| K | Red | Cast iron, short chips | Hard, wear-resistant, brittle |
| N | Green | Aluminum, non-ferrous | Very hard, for soft materials |
| S | Brown | High-temp alloys (Ti, Inconel) | Heat-resistant, tough |
| H | Grey | Hardened steel (>48 HRC) | Very hard, for hard turning |

**Example**: P20 carbide
- P = Steel cutting
- 20 = Medium toughness/hardness balance (10=very tough, 50=very hard)

### Carbide Grade Selection

**Rough machining / Interrupted cuts**:
- P10-P20 (steel)
- Need toughness to resist fracture
- Accept lower wear resistance

**Finishing / Continuous cuts**:
- P30-P50 (steel)
- Need wear resistance for longer tool life
- Less impact concern

**Cast iron / Aluminum**:
- K10-K20 (interrupted), K30-K40 (continuous)

**Stainless steel**:
- M15-M30 (versatile grades)
- Balance of toughness and wear resistance

## Coated Carbide

### Coating Purpose

**Benefits**:
- 2-10× tool life vs uncoated
- Higher speeds possible (30-100%)
- Reduced friction (lower forces)
- Thermal barrier (protect substrate)
- Chemical barrier (reduce diffusion)

**Structure**:
- Tough carbide substrate
- Hard, wear-resistant coating (2-20 μm thick)
- Best of both: tough core + hard surface

### Coating Methods

**CVD (Chemical Vapor Deposition)**:
- Process temperature: 1800-1900°F (1000°C)
- Coating thickness: 5-20 μm (thicker)
- Better adhesion
- Slightly rounded edge (from high temp)
- Best for: Roughing, interrupted cuts, general machining

**PVD (Physical Vapor Deposition)**:
- Process temperature: 900°F (500°C)
- Coating thickness: 2-5 μm (thinner)
- Sharper edge retained (lower temp)
- Wider variety of coatings possible
- Best for: Finishing, sharp edge required, small tools

### Common Coating Types

**TiN (Titanium Nitride)** - Gold color:
- First-generation coating (1970s)
- Hardness: 2400 HV
- Temperature limit: 1000°F (540°C)
- Cost: Low
- Application: General purpose, good visibility (gold = coated)

**TiCN (Titanium Carbonitride)** - Blue-gray:
- Hardness: 3000 HV (harder than TiN)
- Lower friction than TiN
- Better wear resistance
- Application: Steel machining, roughing

**TiAlN (Titanium Aluminum Nitride)** - Purple-violet:
- Hardness: 3500 HV
- Temperature limit: 1500°F+ (820°C)
- Forms Al₂O₃ barrier layer at high temperature
- Excellent oxidation resistance
- Application: High-speed machining, dry cutting, difficult materials

**AlCrN (Aluminum Chromium Nitride)** - Dark gray:
- Hardness: 3200 HV
- Superior oxidation resistance
- Good for abrasive materials
- Application: Mold making, hard materials

**AlTiN (Aluminum Titanium Nitride)** - Black/violet:
- Hardness: 4000+ HV (very hard)
- Excellent high-temp performance
- Application: High-speed steel machining

**Diamond (DLC - Diamond-Like Carbon)** - Black:
- Extremely low friction
- Very hard
- Application: Aluminum, non-ferrous (not for steel - carbon diffuses)

**Multi-layer Coatings**:
- TiN/TiCN/Al₂O₃ (CVD triple coating)
- Combines benefits: toughness + wear resistance + thermal barrier
- Most advanced coatings are multilayer (5-10+ layers)

### Coating Selection Guide

| Workpiece Material | Recommended Coating |
|--------------------|---------------------|
| Aluminum, brass | Uncoated or ZrN (not TiAlN - buildup risk) |
| Mild steel | TiAlN or TiCN |
| Stainless steel | TiAlN (heat resistance critical) |
| Cast iron | TiCN or uncoated |
| Hardened steel | AlTiN or AlCrN |
| Titanium | TiAlN |
| High-temp alloys | AlTiN or AlCrN |

## Ceramic Tools

### Composition and Properties

**Types**:

**Oxide Ceramics** (Al₂O₃):
- Pure aluminum oxide (white)
- Hardness: 1800-2000 HV
- Very brittle
- Best for: Cast iron finishing, hardened steel

**Silicon Nitride** (Si₃N₄):
- Gray color
- Higher fracture toughness than oxide ceramics
- Best for: Cast iron (interrupted cuts possible)

**SiAlON**:
- Silicon-Aluminum-Oxygen-Nitrogen compound
- Derivative of Si₃N₄
- Enhanced properties
- Best for: High-speed cast iron, heat-resistant alloys

**Whisker-Reinforced Ceramics**:
- SiC whiskers in Al₂O₃ matrix
- 50% higher toughness
- Better performance in steel

**Properties**:
- Hardness: 1800-2200 HV (harder than carbide)
- Hot hardness: Excellent (to 2400°F / 1315°C)
- Chemical stability: Excellent
- Fracture toughness: Poor (very brittle)
- Cost: High ($50-150 per insert)

### Applications - Ceramics

**Best for**:
- High-speed finishing (1000-2500 SFM on cast iron)
- Hardened steel turning (55-65 HRC)
- Continuous cuts (no interruption)
- When tool changes are expensive (long runs)

**Not suitable for**:
- Milling (interrupted cuts cause chipping)
- Low rigidity setups
- When coolant cannot be avoided (thermal shock)

**Cutting Conditions**:
- Very high speeds (2-5× carbide speeds)
- Light DOC (0.030-0.100")
- Dry cutting preferred (no thermal shock)
- Rigid setup mandatory

**Example - Cast Iron Finishing**:
- Ceramic insert
- V = 1500 SFM (vs 400 SFM carbide)
- DOC = 0.050"
- Feed = 0.012 IPR
- Dry cutting
- Mirror finish possible

## Cubic Boron Nitride (CBN)

### Properties

**Second hardest material** (after diamond):
- Hardness: 4500 HV
- Hot hardness: Excellent (to 3000°F / 1650°C)
- Chemically inert to ferrous metals (unlike diamond)
- Cost: Very high ($150-500 per insert)

**Structure**:
- Polycrystalline CBN (PCBN)
- Sintered under extreme pressure/temperature
- Usually bonded to carbide substrate (thin CBN layer)

### Applications - CBN

**Primary use: Hard ferrous materials**:
- Hardened steel (55-70 HRC)
- Chilled cast iron
- Hard facing materials
- High-temp alloys (Inconel, Waspaloy)

**"Hard Turning"** (replaces grinding):
- Finish turn hardened parts after heat treat
- 200-400 SFM in 60 HRC steel
- Ra 16-32 μin achievable
- Eliminates grinding operation (faster, more flexible)

**Benefits vs grinding**:
- Single-point process (simpler)
- Can machine complex shapes
- Faster for small quantities
- No grinding wheel dressing

**Cutting Conditions**:
- V = 200-600 SFM (material dependent)
- DOC = 0.010-0.050" (light)
- Feed = 0.003-0.010 IPR
- Coolant optional (can run dry)

**Tool Life**:
- 10-50× carbide life in hardened steel
- Economical despite high insert cost

### CBN Grades

**Low CBN content** (50-60%):
- More binder, tougher
- For interrupted cuts
- Lower hardness materials (50-55 HRC)

**High CBN content** (85-95%):
- Very hard, more brittle
- Continuous cuts only
- Hardest materials (60+ HRC)

## Polycrystalline Diamond (PCD)

### Properties

**Hardest tool material**:
- Hardness: 8000-10,000 HV
- Thermal conductivity: Highest of all materials (best heat removal)
- Wear resistance: Exceptional (100× carbide in aluminum)
- Cost: Very high ($200-800 per cutter)

**Structure**:
- Synthetic diamond particles sintered together
- Typically brazed as thin layer (0.5mm) on carbide substrate
- Random crystal orientation (unlike natural diamond)

### Applications - PCD

**Primary use: Non-ferrous metals**:
- Aluminum (best choice for production)
- Brass, bronze, copper
- Precious metals

**Also excellent for**:
- Composites (carbon fiber, fiberglass)
- Graphite
- Plastics (abrasive-filled)
- Wood and wood composites

**Cannot machine ferrous metals**:
- Carbon in diamond diffuses into steel at cutting temperature
- Diamond graphitizes (loses structure)
- Tool destroyed rapidly

**Cutting Conditions - Aluminum**:
- V = 1500-4000 SFM (3-5× carbide)
- Standard feed rates
- Extremely long tool life (100-200× carbide)
- High-volume production justifies cost

**Example - Aluminum Production**:
- Part requires 100,000 pieces
- Carbide tool life: 500 parts per edge
- PCD tool life: 50,000+ parts per edge
- Result: 2 PCD tools vs 200 carbide tools needed
- Labor savings >> PCD cost premium

### PCD Forms

**Brazed-tip tools**:
- PCD segment brazed to tool body
- Endmills, drills, routers
- Can be resharpened (diamond grind wheel)

**Insert form**:
- PCD layer on carbide insert
- Indexable (multiple edges)
- Replace when all edges worn

**Solid PCD** (rare):
- Entire cutting edge is diamond
- Very expensive
- Ultra-precision applications

## CVD Diamond Coatings

**Emerging technology**:
- Chemical vapor deposition of diamond film
- Thin coating (5-20 μm) on carbide
- Lower cost than PCD

**Applications**:
- Graphite machining (EDM electrodes)
- Composites
- Ultra-abrasive materials

**Limitations**:
- Coating adhesion challenges
- Cannot be resharpened (coating too thin)

## Tool Material Selection Guide

### By Workpiece Material

**Aluminum**:
- Standard: Uncoated carbide
- Production: PCD (100× life)
- Budget: HSS (hobby use)

**Mild Steel (1018)**:
- Standard: TiAlN coated carbide
- Budget: HSS
- Not recommended: Ceramic (better options exist)

**Alloy Steel (4140)**:
- Annealed: TiAlN or TiCN coated carbide
- Hardened (55-65 HRC): CBN or ceramic

**Stainless Steel**:
- TiAlN coated carbide (mandatory - heat resistance)
- M-grade (versatile grade)

**Titanium**:
- TiAlN or AlCrN coated carbide
- Sharp tools, frequent replacement

**Cast Iron**:
- Roughing: Uncoated or TiCN carbide
- Finishing: Ceramic (high-speed)

**Hardened Steel (>55 HRC)**:
- First choice: CBN (hard turning)
- Alternative: Ceramic
- Budget: Carbide (very slow, light cuts)

**Inconel / High-Temp Alloys**:
- Ceramic or CBN (high-speed)
- Coated carbide (lower speeds)

**Composites (carbon fiber)**:
- First choice: PCD
- Budget: Carbide (short life)

### By Operation Type

**Roughing / Heavy Cuts**:
- Tough grades (P10-P20 for steel)
- CVD coating (better adhesion)
- Larger edge radius (chip breaker)

**Finishing / Light Cuts**:
- Wear-resistant grades (P30-P50 for steel)
- PVD coating (sharper edge)
- Small edge radius or hone

**Interrupted Cuts (Milling)**:
- Toughest grades
- Lower hardness acceptable
- HSS excellent choice for slots, keyways

**Continuous Cuts (Turning)**:
- Harder grades acceptable
- Maximize wear resistance
- Ceramic or CBN for hard materials

**Drilling**:
- HSS preferred (toughness critical)
- Carbide for production (with through-coolant)

**High-Speed Machining**:
- Coated carbide (TiAlN)
- Sharp geometry
- Light cuts, high feeds

## Economic Considerations

### Tool Cost vs Performance

**Cost per cutting edge**:
- HSS: $5-20
- Uncoated carbide: $20-40
- Coated carbide: $30-80
- Ceramic: $50-150
- CBN: $150-500
- PCD: $200-800

**But cost per part is what matters**:

**Example - Aluminum Part (10,000 qty)**:

**Option A: Carbide**
- Tool cost: $40
- Parts per edge: 200
- Edges needed: 50
- Total tool cost: $2,000
- Cost per part: $0.20

**Option B: PCD**
- Tool cost: $600
- Parts per edge: 10,000
- Edges needed: 1
- Total tool cost: $600
- Cost per part: $0.06

**PCD is 70% cheaper per part** despite 15× higher tool cost!

### Decision Framework

**Low-volume** (< 100 parts):
- Use readily available tools (HSS, standard carbide)
- Tool cost matters more than life

**Medium-volume** (100-1,000 parts):
- Coated carbide optimal
- Balance tool cost and life

**High-volume** (> 1,000 parts):
- Optimize cost per part
- Advanced tooling (PCD, CBN) often justified
- Reduced downtime for tool changes

**Difficult materials**:
- May need specialized tooling even for low volume
- Carbide won't work on hardened steel (need CBN)
- Carbon fiber destroys carbide quickly (need PCD)

## Tool Life and Wear

### Typical Tool Life

| Tool Material | Relative Life (Steel) | Relative Life (Aluminum) |
|---------------|----------------------|-------------------------|
| HSS | 1× (baseline) | 1× |
| Uncoated Carbide | 3-5× | 5-10× |
| Coated Carbide | 5-15× | 8-15× |
| Ceramic | 10-30× (hard materials) | N/A |
| CBN | 20-50× (hardened steel) | N/A |
| PCD | N/A (not for ferrous) | 100-200× |

**Factors affecting tool life**:
1. Cutting speed (exponential effect via Taylor equation)
2. Workpiece hardness
3. Coolant effectiveness
4. Tool coating
5. Machine rigidity

### When to Change Tool

**Criteria**:
- Flank wear reaches limit (0.012" roughing, 0.006" finishing)
- Dimensional accuracy lost
- Surface finish degrades
- Cutting forces increase significantly
- Audible change (squealing, chattering)

**Before catastrophic failure**:
- Tool breakage causes scrap
- May damage workpiece, fixture, or machine
- Change tool when wear approaches limit

## Summary

**Tool material selection hierarchy**:

1. **Identify workpiece material and hardness**
2. **Determine operation** (roughing/finishing, continuous/interrupted)
3. **Select appropriate tool material** (use guide above)
4. **Choose specific grade** (toughness vs wear resistance)
5. **Select coating if applicable** (speed/life benefit vs cost)
6. **Verify performance and optimize**

**General recommendations**:
- **Aluminum**: Uncoated carbide or PCD (production)
- **Steel**: TiAlN coated carbide
- **Stainless**: TiAlN coated carbide (mandatory)
- **Cast iron**: Uncoated carbide or ceramic (finishing)
- **Hardened steel**: CBN or ceramic
- **Titanium**: TiAlN coated carbide
- **Composites**: PCD

**Economic principle**:
Optimize cost per part, not tool cost. Advanced tooling (PCD, CBN) often pays for itself in reduced cycle time, longer life, and less downtime.

---

**Next**: [20.8 Coolant and Chip Management](section-20.8-coolant-chip-management.md)

---

# 20.2 Cutting Mechanics and Tool Geometry

## Chip Formation Process

### Orthogonal Cutting Model

**Simplified 2D Model**: Single cutting edge perpendicular to cutting direction.

**Cutting Zones**:

**Zone 1 - Primary Shear Zone**:
- Material deforms plastically ahead of tool
- Chip forms by shearing along shear plane
- Angle φ (phi) = shear angle

**Zone 2 - Secondary Shear Zone**:
- Friction between chip and tool rake face
- Additional heat generation
- Affects chip curl and evacuation

**Zone 3 - Tertiary Zone**:
- Rubbing between tool flank and workpiece
- Generates finished surface
- Wear on tool flank face

### Shear Plane Angle

**Merchant's Equation**:
$$\phi = 45° + \frac{\alpha}{2} - \frac{\beta}{2}$$

where:
- φ = shear angle
- α (alpha) = rake angle (tool geometry)
- β (beta) = friction angle at tool-chip interface

**Key Insight**: Higher rake angle → higher shear angle → less deformation → lower cutting forces and heat.

**Example**:
- Rake angle α = 10°
- Friction angle β = 30° (typical for steel)
- φ = 45° + 5° - 15° = 35°

Lower friction (better lubrication): β = 20°
- φ = 45° + 5° - 10° = 40° (less deformation, easier cutting)

### Chip Types

**Continuous Chip**:
- Smooth, ribbon-like chip
- Ductile materials (low carbon steel, aluminum)
- Sharp tool, high speed, positive rake
- Good surface finish
- Problem: Long chips tangle

**Discontinuous Chip**:
- Segmented, broken chips
- Brittle materials (cast iron, brass)
- Low speed, negative rake, or built-up edge
- Poor surface finish
- Advantage: Easy chip removal

**Continuous with Built-Up Edge (BUE)**:
- Material welds to cutting edge
- Periodic detachment degrades finish
- Occurs at moderate speeds with steel
- Eliminated by increasing speed or better lubrication

**Serrated/Segmented Chip**:
- Saw-tooth appearance
- High-strength materials (titanium, Inconel)
- Adiabatic shear bands (localized heating and softening)
- Cyclic cutting forces (vibration risk)

### Cutting Force Components

**Three Force Components**:

**1. Primary Cutting Force (F_c)**:
- Direction of cutting velocity
- Largest component (60-80% of total)
- Determines power requirement

**2. Thrust Force (F_t)**:
- Perpendicular to cutting direction, in feed direction
- Causes tool deflection
- 20-40% of F_c

**3. Radial Force (F_r)**:
- Perpendicular to cutting direction and feed
- Relevant in milling (pushes away from center)
- 10-30% of F_c

**Force Measurement**:
Dynamometers measure forces during machining tests.

**Typical Values** (turning 1018 steel, 0.020" DOC, 0.010" feed):
- F_c ≈ 300 lb
- F_t ≈ 100 lb
- F_r ≈ 50 lb

### Specific Cutting Force

**Definition**: Cutting force per unit area of uncut chip.

$$k_s = \frac{F_c}{A_{chip}} = \frac{F_c}{DOC \times f}$$

**Typical Values**:

| Material | k_s (kpsi) | k_s (N/mm²) |
|----------|------------|-------------|
| Aluminum 6061 | 50-80 | 345-550 |
| Brass | 80-120 | 550-825 |
| Mild Steel 1018 | 150-250 | 1035-1725 |
| Alloy Steel 4140 | 250-400 | 1725-2760 |
| Stainless 304 | 300-450 | 2070-3100 |
| Titanium Ti-6Al-4V | 350-500 | 2415-3450 |
| Cast Iron | 100-180 | 690-1240 |

**Force Prediction**:
$$F_c = k_s \times DOC \times f$$

**Example**:
Turning 4140 steel, DOC = 0.100", feed = 0.008":
$$F_c = 300,000 \text{ psi} \times 0.100 \times 0.008 = 240 \text{ lb}$$

**Power Required**:
$$P = \frac{F_c \times V}{33,000}$$

where V is cutting speed (FPM), P in horsepower.

At 400 FPM:
$$P = \frac{240 \times 400}{33,000} = 2.9 \text{ hp}$$

### Chip Thickness and Width

**Uncut Chip Thickness (h)**:
In turning: h = feed per revolution

In milling: h varies with engagement angle θ:
$$h = f_z \sin\theta$$

**Maximum chip thickness** (90° engagement):
$$h_{max} = f_z$$

**Average chip thickness** (full slot, 180° engagement):
$$h_{avg} = f_z \times \frac{2}{\pi} \approx 0.64 f_z$$

**Chip Thinning Effect**:
In light radial cuts (< 25% diameter), chip thins:
$$h_{avg} = f_z \sqrt{\frac{RDOC}{D}}$$

**Example**:
1/2" endmill, RDOC = 0.050" (10%), f_z = 0.004":
$$h_{avg} = 0.004 \sqrt{\frac{0.050}{0.5}} = 0.004 \times 0.316 = 0.00126"$$

Chip is 68% thinner! Must increase f_z to maintain cutting action:
$$f_z = \frac{0.004}{0.316} = 0.0126"$$ (increase feed rate 3×)

## Tool Geometry

### Single-Point Tool Angles

**Rake Angle (α)**:
- Angle of tool face relative to workpiece surface
- Positive rake: Slopes away from cutting edge (easier cutting, weaker edge)
- Negative rake: Slopes toward cutting edge (stronger edge, higher forces)

**Typical Rake Angles**:
- Aluminum: +10° to +20° (soft, ductile)
- Steel: +5° to +15°
- Cast iron: 0° to +10° (brittle)
- Hardened steel: 0° to -5° (edge strength critical)

**Effect on Forces**:
10° increase in rake angle reduces cutting forces ~15-20%.

**Clearance Angle (γ)**:
- Angle between tool flank and workpiece
- Prevents rubbing behind cutting edge
- Typical: 5-10°

**Inclination Angle (λ)**:
- Angle of cutting edge relative to horizontal
- Controls chip flow direction
- Positive: Chips flow toward workpiece (turning away from tailstock)
- Negative: Chips flow away from workpiece

**End Cutting Edge Angle (ECEA)**:
- Reduces friction on trailing edge
- Typical: 5-15°

### Milling Tool Geometry

**Helix Angle**:
- Spiral of flutes around endmill
- 30-35° standard
- 40-50° high helix (aluminum, soft materials - better chip evacuation)
- 10-20° slow helix (cast iron, hardened steel - stronger edge)

**Radial Rake**:
- Rake angle viewed from front of tool
- Affects cutting forces

**Axial Rake**:
- Rake angle along helix
- Related to helix angle

**Relief Angle**:
- Clearance behind cutting edge
- Prevents rubbing on circumference

**Core Diameter**:
- Diameter of endmill body (excluding flutes)
- Larger core = more rigid tool (less deflection)

**Example - Endmill Selection**:
- Aluminum: 3-flute, 40° helix, large core, polished flutes
- Steel: 4-flute, 30° helix, variable pitch (chatter resistance)
- Titanium: 4-flute, 30° helix, sharp edge geometry, slow helix

### Number of Flutes

**Trade-offs**:

**Fewer Flutes (2-3)**:
- Larger chip gullets (better evacuation)
- Higher feed per tooth possible
- Faster feed rates at same RPM
- Less likely to clog
- Best for aluminum, deep slotting

**More Flutes (4-6+)**:
- Smoother cutting (more cuts per revolution)
- Better surface finish
- Lower chip load per tooth required
- Requires adequate chip clearance
- Best for steel, finishing operations

**Example**:
1/2" endmill at 3000 RPM, f_z = 0.003":
- 2-flute: F = 0.003 × 2 × 3000 = 18 IPM
- 4-flute: F = 0.003 × 4 × 3000 = 36 IPM (2× faster)

But 2-flute can handle higher f_z (larger gullets):
- 2-flute at f_z = 0.006": F = 36 IPM (same feed, less load per tooth)

### Tool Nose Radius

**Effect on Surface Finish**:
$$Ra = \frac{f^2}{32 r}$$

**Example**:
Feed = 0.010 IPR, nose radius = 1/32" (0.031"):
$$Ra = \frac{0.010^2}{32 \times 0.031} = 0.0001" = 100 \mu\text{in}$$

Doubling nose radius to 1/16":
$$Ra = \frac{0.010^2}{32 \times 0.0625} = 50 \mu\text{in (2× smoother)}$$

**Trade-off**:
- Larger radius: Better finish but higher cutting forces (more contact area)
- Smaller radius: Lower forces but rougher finish

**Typical Radii**:
- Roughing: 0.015-0.031" (sharp, low forces)
- Finishing: 0.031-0.062" (smoother finish)
- Precision finishing: 0.062-0.125" (mirror finish possible)

### Chip Breakers

**Purpose**: Break long, continuous chips into manageable segments.

**Mechanisms**:
- Groove on rake face causes chip to curl tightly
- Chip curls back and contacts workpiece or tool
- Stress concentration fractures chip

**Types**:
- Form-ground: Groove machined into insert
- Clamped: Separate chip breaker plate
- Geometry-based: Positive/negative lands, steps

**Selection**:
- Aggressive (deep groove): Heavy cuts, soft materials
- Moderate: General purpose
- Light (shallow groove): Finishing cuts, hard materials

**Without Chip Breaker**:
Long, stringy chips (hazardous, tangle, poor chip evacuation).

**With Chip Breaker**:
Short, 'C' or '6' shaped chips (safe, easy removal).

## Temperature Distribution

### Heat Sources

**Primary Shear Zone**: 60-80% of total heat
- Plastic deformation of material
- Proportional to shear force and shear velocity

**Secondary Shear Zone**: 20-30% of total heat
- Friction between chip and rake face
- Higher at low speeds (more contact time)

**Tertiary Zone**: 5-10% of total heat
- Friction between flank and workpiece
- Increases with tool wear

**Total Heat Generated**:
$$Q = F_c \times V \times J$$

where J = mechanical equivalent of heat (1 BTU = 778 ft-lb)

**Example**:
F_c = 250 lb, V = 400 FPM:
$$Q = \frac{250 \times 400}{778} = 128 \text{ BTU/min}$$

### Temperature Distribution

**Chip**: Carries away 60-80% of heat
- Higher speeds → more heat in chip (less contact time)
- Coolant on chip very effective

**Tool**: Absorbs 10-20% of heat
- Carbide conducts heat well (distributes along tool)
- Coating reduces heat transfer to substrate

**Workpiece**: Absorbs 10-20% of heat
- Low speeds → more heat in workpiece (longer contact)
- Thermal expansion affects precision

**Typical Cutting Temperatures**:

| Material | Temperature (°F) | Temperature (°C) |
|----------|------------------|------------------|
| Aluminum | 400-600 | 200-315 |
| Brass | 500-700 | 260-370 |
| Mild Steel | 800-1200 | 425-650 |
| Stainless Steel | 1000-1400 | 540-760 |
| Titanium | 1200-1600 | 650-870 |
| Inconel | 1400-1800 | 760-980 |

**Tool Material Limits**:
- HSS: 1000-1100°F (540-595°C) - loses hardness
- Uncoated carbide: 1400-1600°F (760-870°C)
- Coated carbide: 1800-2000°F (980-1095°C)
- Ceramic: 2200-2800°F (1200-1540°C)
- CBN: 2700-3300°F (1480-1815°C)

### Coolant Effects

**Functions of Coolant**:
1. **Cooling**: Removes heat from cutting zone
2. **Lubrication**: Reduces friction (secondary shear zone)
3. **Chip Flushing**: Evacuates chips from cut
4. **Corrosion Prevention**: Protects machine and workpiece

**Temperature Reduction**:
Flood coolant reduces cutting temperature 200-400°F compared to dry cutting.

**Effect on Tool Life**:
Reducing temperature from 1200°F to 1000°F can double tool life (due to exponential wear relationship).

**Thermal Shock**:
Intermittent cuts with coolant cause thermal cycling:
- Tool heats in cut
- Rapid cooling when exiting cut
- Cracking at cutting edge (comb cracks)

**Solution**: Flood coolant (continuous) or no coolant (consistent temperature).

## Tool Wear Mechanisms

### Abrasive Wear

**Mechanism**: Hard particles in workpiece scrape material from tool.

**Typical in**:
- Cast iron (hard carbides)
- Composites (glass or carbon fibers)
- Sand castings (sand inclusions)

**Wear Pattern**: Uniform wear on flank face

**Reduction Strategies**:
- Harder tool material (carbide > HSS)
- Reduce cutting speed
- Increase feed (less contact per cut)

### Adhesive Wear

**Mechanism**: Workpiece material welds to tool, tears away tool material when chip separates.

**Typical in**:
- Soft, ductile metals (aluminum, copper)
- Insufficient coolant/lubrication

**Wear Pattern**: Built-up edge (BUE) on rake face

**Reduction Strategies**:
- Increase cutting speed (less time for welding)
- Improve lubrication
- Coated tools (TiN, TiAlN reduce adhesion)

### Diffusion Wear

**Mechanism**: Atoms from tool diffuse into workpiece (or vice versa) at high temperatures.

**Typical in**:
- High-speed cutting of steel
- High temperatures (> 1400°F)

**Wear Pattern**: Crater wear on rake face

**Reduction Strategies**:
- Reduce cutting speed (lower temperature)
- Coated carbide (diffusion barrier)
- Ceramic or CBN tools (more stable at high temp)

### Oxidation Wear

**Mechanism**: Oxygen reacts with tool material at high temperatures, forming weak oxide layer.

**Typical in**:
- High-speed dry cutting
- Elevated temperatures (> 1500°F)

**Wear Pattern**: Flank wear, notching at depth of cut line

**Reduction Strategies**:
- Reduce cutting speed
- Use inert atmosphere (difficult in practice)
- Coatings (aluminum oxide protects)

### Thermal Cracking

**Mechanism**: Cyclic heating/cooling causes thermal stresses, cracks form perpendicular to cutting edge.

**Typical in**:
- Interrupted cuts (milling, facing)
- Flood coolant with intermittent cuts

**Wear Pattern**: Comb cracks perpendicular to edge

**Reduction Strategies**:
- Mist coolant or dry cutting (avoid thermal shock)
- Tougher tool grade (less brittle)
- Reduce cutting speed

### Mechanical Fracture

**Mechanism**: Excessive cutting forces or impact loads exceed tool strength.

**Typical in**:
- Aggressive cuts (too much DOC or feed)
- Chatter and vibration
- Interrupted cuts with hard inclusions

**Wear Pattern**: Chipping or complete edge failure

**Reduction Strategies**:
- Reduce DOC and feed
- More rigid setup (minimize vibration)
- Tougher tool grade (higher fracture toughness)

## Tool Life Criteria

### Flank Wear (VB)

**Measurement**: Width of wear land on tool flank.

**ISO Standard Tool Life**:
- Roughing: VB = 0.3 mm (0.012")
- Finishing: VB = 0.15 mm (0.006")

**Measurement Method**:
Toolmaker's microscope or optical comparator.

**Typical Progression**:
- Initial rapid wear (break-in, 0-2 minutes)
- Steady-state wear (linear, 2-30 minutes typical)
- Accelerated wear (exponential, end of life)

**Tool change** at beginning of accelerated wear phase.

### Crater Wear (KT)

**Measurement**: Depth of crater on rake face.

**Acceptable Limit**: KT = 0.06 + 0.3 × tool thickness (mm)

**Example**:
1/4" (6.35 mm) thick insert:
KT_max = 0.06 + 0.3 × 6.35 = 2.0 mm (0.080")

### Other Criteria

**Dimensional Accuracy**:
When workpiece size drifts out of tolerance, change tool.

**Surface Finish**:
When finish exceeds specification, change tool.

**Cutting Force**:
Dull tool shows 50-100% increase in forces.

**Audible**:
Experienced machinists hear when tool dulls (pitch changes, squealing).

### Taylor Tool Life Equation (Revisited)

$$V T^n = C$$

Rearranged to solve for tool life:
$$T = \left(\frac{C}{V}\right)^{1/n}$$

**Extended Form** (includes feed and DOC):
$$V T^n f^m DOC^p = C$$

where:
- $m$ ≈ 0.5-0.8 (feed exponent)
- $p$ ≈ 0.3-0.5 (DOC exponent)

**Key Insight**: Cutting speed has greatest effect on tool life (highest exponent when in VT^n form).

**Example Effect of Doubling Parameters**:
- 2× speed: Tool life × 0.06-0.25 (drastically reduced)
- 2× feed: Tool life × 0.4-0.6 (moderately reduced)
- 2× DOC: Tool life × 0.5-0.7 (moderately reduced)

**Strategy**: Increase feed and DOC before increasing speed (less impact on tool life).

## Machinability

### Definition

**Machinability**: Relative ease of machining a material, considering:
- Tool life
- Cutting forces
- Surface finish
- Chip formation

### Machinability Ratings

**AISI B1112 Steel = 100% (Reference)**

**Relative Machinability**:

| Material | Rating | Interpretation |
|----------|--------|----------------|
| Free-machining brass | 300 | 3× easier than B1112 |
| Aluminum 6061-T6 | 200 | 2× easier |
| AISI B1112 (reference) | 100 | Baseline |
| AISI 1018 steel | 70 | 30% more difficult |
| AISI 4140 steel | 50 | 2× more difficult |
| Stainless 304 | 40 | 2.5× more difficult |
| Titanium Ti-6Al-4V | 20 | 5× more difficult |
| Inconel 718 | 10 | 10× more difficult |

**Interpretation**:
Rating ≈ relative tool life at same cutting parameters.

**Example**:
Cutting 4140 at 200 SFM gives 30-minute tool life.
Same tool on aluminum 6061 at 200 SFM: ~60 minutes (2× longer).

### Factors Affecting Machinability

**Material Properties**:
- **Hardness**: Harder materials more difficult
- **Ductility**: Very ductile materials gum up (aluminum), very brittle chip poorly (cast iron)
- **Thermal conductivity**: Low conductivity (stainless, titanium) concentrates heat at tool
- **Work hardening**: Stainless hardens rapidly during cutting

**Microstructure**:
- **Grain size**: Finer grains → smoother surface but higher forces
- **Phase distribution**: Ferrite + pearlite in steel machines well
- **Inclusions**: Sulfides (MnS) improve machinability (free-machining grades)

**Additives**:
- **Lead** (Pb): Lubricates, breaks chips (banned in many regions)
- **Sulfur** (S): Forms MnS inclusions (B1112 has 0.16-0.23% S)
- **Phosphorus** (P): Increases brittleness, aids chip breaking

## Cutting Tool Materials

### High-Speed Steel (HSS)

**Composition**: Iron with 4% Cr, 18% W (or Mo), 1% V, 0.7% C (typical M2 grade)

**Properties**:
- Hardness: 63-65 HRC
- Toughness: Excellent (high fracture toughness)
- Temperature limit: 1000°F (540°C)
- Cost: Low ($5-20 per tool)

**Applications**:
- Drilling (flexibility important)
- Tapping (toughness critical)
- Low-speed operations
- Interrupted cuts
- DIY/hobby (low cost, regrindable)

**Speed Limitations**:
HSS limited to 50-200 SFM in steel (carbide 3-10× faster).

### Carbide

**Composition**: Tungsten carbide (WC) grains bonded with cobalt (Co).

**Grades**:
- **C1-C4**: More cobalt (10-15%), tougher, lower hardness (for steel)
- **C5-C8**: Less cobalt (3-6%), harder, more brittle (for cast iron, non-ferrous)

**Properties**:
- Hardness: 90-93 HRA (harder than HSS)
- Temperature limit: 1600°F (870°C) uncoated, 1800°F+ coated
- Thermal conductivity: 10× higher than HSS (better heat removal)
- Cost: Medium ($20-80 per insert)

**ISO Classifications**:
- **P (Blue)**: Steel
- **M (Yellow)**: Stainless steel (versatile)
- **K (Red)**: Cast iron, non-ferrous
- **N (Green)**: Aluminum, non-ferrous
- **S (Brown)**: High-temperature alloys (Inconel, Titanium)
- **H (Grey)**: Hardened steel (> 45 HRC)

**Example**: P20 carbide
- P = steel machining
- 20 = moderate toughness/hardness balance

### Coated Carbide

**Coating Methods**:
- **CVD** (Chemical Vapor Deposition): 1000°C, thicker coatings (5-20 μm)
- **PVD** (Physical Vapor Deposition): 500°C, thinner coatings (2-5 μm), sharper edge

**Common Coatings**:

**TiN (Titanium Nitride)** - Gold color:
- First generation coating
- Hardness: 2400 HV
- Temp limit: 1000°F (540°C)
- General purpose

**TiCN (Titanium Carbonitride)** - Blue-gray:
- Harder than TiN (3000 HV)
- Better wear resistance
- Steel machining

**TiAlN (Titanium Aluminum Nitride)** - Purple-violet:
- Excellent high-temp stability (1500°F+)
- Forms Al₂O₃ barrier at high temp
- High-speed machining, dry cutting

**AlCrN (Aluminum Chromium Nitride)** - Gray:
- Superior oxidation resistance
- Hard coatings, mold making

**Multilayer Coatings**:
TiN/TiCN/Al₂O₃ - combines benefits of each layer.

**Benefits**:
- 2-10× tool life vs uncoated
- Higher speeds possible (50-100% increase)
- Dry machining capable

### Ceramics

**Composition**: Aluminum oxide (Al₂O₃) with additives.

**Types**:
- **Oxide ceramics** (Al₂O₃): White, for cast iron and hardened steel
- **Silicon nitride** (Si₃N₄): Gray, for cast iron (higher toughness)
- **SiAlON**: Si-Al-O-N solid solution (Si₃N₄ derivative)

**Properties**:
- Hardness: 1800-2000 HV (harder than carbide)
- Temperature limit: 2400°F (1315°C)
- Toughness: Low (brittle)
- Chemical stability: Excellent

**Applications**:
- High-speed finishing (2000+ SFM on cast iron)
- Hardened steel (55-65 HRC)
- No coolant (thermal shock risk)

**Limitations**:
- Brittle (no interrupted cuts)
- Expensive ($50-150 per insert)
- Requires rigid setup

### Cubic Boron Nitride (CBN)

**Composition**: Cubic form of boron nitride (second hardest material after diamond).

**Properties**:
- Hardness: 4500 HV (approaching diamond)
- Temperature limit: 3000°F (1650°C)
- Chemically inert (doesn't react with ferrous metals)
- Cost: Very high ($150-500 per insert)

**Applications**:
- Hardened steel (55-70 HRC)
- Hard turning (replaces grinding)
- Aerospace alloys (Inconel, Waspaloy)
- Long tool life in hard materials (10-50× carbide)

**Form**:
- Solid CBN: All CBN (rare, expensive)
- Tipped CBN: Thin CBN layer on carbide substrate (common)

### Polycrystalline Diamond (PCD)

**Composition**: Synthetic diamond particles sintered under high pressure/temperature.

**Properties**:
- Hardness: 8000-10,000 HV (hardest tool material)
- Thermal conductivity: Highest (better heat removal than any other material)
- Toughness: Moderate (better than ceramic, worse than carbide)
- Cost: Very high ($200-800 per cutter)

**Applications**:
- Non-ferrous metals (aluminum, brass, copper)
- Composites (carbon fiber, fiberglass)
- Plastics and wood
- Ultra-long tool life (100× carbide in aluminum)

**Limitations**:
- **Cannot machine ferrous metals** (iron/steel) - carbon diffuses into steel at cutting temperature
- Expensive
- Sensitive to shock loads

**Forms**:
- Tipped tools: PCD brazed to carbide
- Solid PCD: Entire cutting edge is diamond (rare, expensive)
- CVD diamond: Thin film coating (emerging)

### Material Selection Guide

**Low-speed (<200 SFM), Interrupted Cuts, Toughness Required**:
→ HSS

**General Machining Steel (200-600 SFM)**:
→ Coated carbide (TiAlN)

**High-Speed Finishing Cast Iron (1000-2000+ SFM)**:
→ Ceramic (Si₃N₄)

**Hardened Steel (55-65 HRC)**:
→ CBN

**High-Volume Aluminum Production**:
→ PCD

**Composites, Non-Ferrous**:
→ PCD or solid carbide (uncoated)

## Summary

Understanding cutting mechanics enables intelligent selection of feeds, speeds, and tool geometry:

**Key Principles**:
1. Chip formation involves shear deformation and friction
2. Cutting forces scale with chip area (DOC × feed)
3. Temperature increases exponentially with speed
4. Tool wear results from abrasion, adhesion, diffusion, oxidation, and cracking
5. Tool material must match workpiece and cutting conditions

**Practical Applications**:
- Calculate forces to check machine/fixture capability
- Predict power requirements
- Select tool geometry for material (rake angle, helix, flutes)
- Choose tool material based on speed and workpiece
- Recognize wear patterns to optimize parameters

**Next Steps**:
Understanding mechanics provides foundation for:
- Calculating optimal cutting speeds (Section 20.3)
- Optimizing feed rates (Section 20.4)
- Troubleshooting problems (Section 20.9)

---

**Next**: [20.3 Cutting Speed and Spindle RPM Calculations](section-20.3-cutting-speed.md)

---

# 20.4 Feed Rate Optimization

## Understanding Feed Rate

**Feed Rate (F)**: The velocity at which the tool advances through the workpiece
- Units: Inches per minute (IPM) or millimeters per minute (mm/min)
- Programmed with F word in G-code: `G1 X2.0 F30` (move to X2.0 at 30 IPM)

**Feed rate determines**:
- Surface finish quality (primary factor)
- Chip load per tooth
- Cutting forces
- Material removal rate
- Cycle time

## Feed Per Tooth Concept

**Feed Per Tooth (f_z)**: The distance the tool advances per cutting edge

**This is the fundamental parameter** - most machining data specifies f_z, not feed rate.

**Relationship**:
$$F = f_z \times Z \times N$$

where:
- $F$ = feed rate (IPM or mm/min)
- $f_z$ = feed per tooth (inches or mm)
- $Z$ = number of flutes/teeth
- $N$ = spindle speed (RPM)

**Example 1**:
- 4-flute endmill
- 3000 RPM
- f_z = 0.003"
$$F = 0.003 \times 4 \times 3000 = 36 \text{ IPM}$$

**Example 2**:
- 2-flute endmill (same parameters otherwise)
$$F = 0.003 \times 2 \times 3000 = 18 \text{ IPM}$$

**Key insight**: More flutes = higher feed rate at same chip load

## Reverse Calculation (Feed Rate → Feed Per Tooth)

**When to use**: Given a feed rate, calculate actual chip load

$$f_z = \frac{F}{Z \times N}$$

**Example**:
Running 50 IPM with 3-flute mill at 4000 RPM:
$$f_z = \frac{50}{3 \times 4000} = 0.00417"$$

Check if this is appropriate for material and tool size.

## Recommended Feed Per Tooth Values

### By Material (Carbide Tools)

**Aluminum Alloys**:
- Roughing: 0.008-0.015" per tooth
- Finishing: 0.003-0.006" per tooth
- Note: Can handle high chip loads, excellent machinability

**Mild Steel (1018)**:
- Roughing: 0.005-0.010" per tooth
- Finishing: 0.002-0.004" per tooth

**Alloy Steel (4140)**:
- Roughing: 0.004-0.008" per tooth
- Finishing: 0.001-0.003" per tooth

**Stainless Steel (304)**:
- Roughing: 0.003-0.006" per tooth
- Finishing: 0.001-0.003" per tooth
- Note: Work hardens, avoid rubbing

**Titanium (Ti-6Al-4V)**:
- Roughing: 0.003-0.006" per tooth
- Finishing: 0.001-0.003" per tooth
- Note: Low thermal conductivity, sharp tools critical

**Cast Iron**:
- Roughing: 0.006-0.012" per tooth
- Finishing: 0.003-0.006" per tooth

**Plastics**:
- Roughing: 0.005-0.012" per tooth
- Finishing: 0.002-0.005" per tooth
- Note: Sharp tools to prevent melting

### By Tool Diameter

**General guideline**: Larger tools can handle larger chip loads (more rigid)

**Rule of thumb**: f_z ≈ 0.001-0.002" per 1/8" of diameter

| Tool Diameter | Roughing f_z | Finishing f_z |
|---------------|--------------|---------------|
| 1/8" (3mm) | 0.001-0.002" | 0.0005-0.001" |
| 1/4" (6mm) | 0.003-0.005" | 0.001-0.002" |
| 3/8" (10mm) | 0.004-0.007" | 0.002-0.003" |
| 1/2" (12mm) | 0.005-0.010" | 0.002-0.004" |
| 3/4" (20mm) | 0.007-0.012" | 0.003-0.005" |
| 1" (25mm) | 0.008-0.015" | 0.003-0.006" |

**Adjust down for**:
- Long tool overhang (> 3× diameter)
- Hard materials
- Poor machine rigidity
- Finishing operations

## Surface Finish Relationship

**Theoretical surface roughness**:
$$Ra = \frac{f_z^2}{32 \times r}$$

where:
- $Ra$ = average roughness (inches or μm)
- $f_z$ = feed per tooth
- $r$ = tool nose radius

**Example**:
f_z = 0.010", nose radius = 0.031" (1/32"):
$$Ra = \frac{0.010^2}{32 \times 0.031} = 0.0001" = 100 \text{ μin}$$

**Halving feed per tooth**:
f_z = 0.005":
$$Ra = \frac{0.005^2}{32 \times 0.031} = 0.000025" = 25 \text{ μin (4× smoother)}$$

**Key principle**: Surface finish improves quadratically with reduced feed per tooth

### Surface Finish Guidelines

| Application | Ra (μin) | Ra (μm) | Typical f_z |
|-------------|----------|---------|-------------|
| Rough machining | 200-500 | 5-12 | 0.008-0.015" |
| General machining | 63-125 | 1.6-3.2 | 0.004-0.008" |
| Precision finish | 16-63 | 0.4-1.6 | 0.001-0.003" |
| Mirror finish | 4-16 | 0.1-0.4 | 0.0005-0.001" |

**Achieving better finish**:
1. Reduce feed per tooth (most important)
2. Increase nose radius
3. Sharp tools
4. Higher RPM (more cuts per inch of travel)
5. Rigid setup (minimize vibration)
6. Climb milling (smoother engagement)

## Minimum Chip Load

**Critical concept**: Feed per tooth must be large enough for cutting, not rubbing.

**Minimum chip load**: ~0.0005" (0.01mm)

**Below minimum**:
- Tool rubs instead of cuts
- Rapid wear on tool flank
- Heat buildup
- Poor surface finish
- Potential tool breakage

**Example problem**:
- 4-flute endmill at 10,000 RPM
- Feed rate: 20 IPM
$$f_z = \frac{20}{4 \times 10000} = 0.0005"$$ (at minimum!)

**Better approach**:
- Reduce RPM to 5000
- Same feed rate: 20 IPM
$$f_z = \frac{20}{4 \times 5000} = 0.001"$$ (adequate chip load)

**Key insight**: Sometimes reducing RPM improves results by maintaining proper chip load

## Chip Thinning Effect

**Occurs in**: Light radial engagement (< 25% of tool diameter)

**Phenomenon**: Actual chip thickness is less than programmed feed per tooth

**Formula**:
$$h_{actual} = f_z \times \sqrt{\frac{RDOC}{D}}$$

where:
- $h_{actual}$ = actual average chip thickness
- $RDOC$ = radial depth of cut
- $D$ = tool diameter

**Example**:
- 1/2" endmill
- RDOC = 0.050" (10% of diameter)
- Programmed f_z = 0.004"

$$h_{actual} = 0.004 \times \sqrt{\frac{0.050}{0.5}} = 0.004 \times 0.316 = 0.00126"$$

Chip is 68% thinner than programmed!

**Solution**: Increase feed per tooth to compensate
$$f_z = \frac{0.004}{0.316} = 0.0126"$$

Increase feed rate 3× to maintain effective chip load.

**High-speed machining (HSM)** takes advantage of this:
- Very light radial cuts (5-10% of diameter)
- Very high feed rates (compensate for chip thinning)
- Lower cutting forces (despite high feed rate)
- Longer tool life

## Feed Rate Calculation Examples

### Example 1: Aluminum Pocket Milling

**Setup**:
- Material: 6061 Aluminum
- Tool: 1/2" 3-flute carbide endmill
- Cutting speed: 800 SFM
- Operation: Roughing

**Step 1**: Calculate RPM
$$N = \frac{3.82 \times 800}{0.5} = 6112 \text{ RPM}$$

**Step 2**: Select chip load
- Aluminum roughing: 0.010" per tooth

**Step 3**: Calculate feed rate
$$F = 0.010 \times 3 \times 6112 = 183 \text{ IPM}$$

**G-code**:
```gcode
S6112 M3
F183
G1 X2.0 Y1.0  (Mill at 183 IPM)
```

### Example 2: Steel Finishing

**Setup**:
- Material: 1018 Steel
- Tool: 1/2" 4-flute coated carbide endmill
- Cutting speed: 350 SFM
- Operation: Finishing

**Step 1**: Calculate RPM
$$N = \frac{3.82 \times 350}{0.5} = 2674 \text{ RPM}$$

**Step 2**: Select chip load
- Steel finishing: 0.002" per tooth

**Step 3**: Calculate feed rate
$$F = 0.002 \times 4 \times 2674 = 21 \text{ IPM}$$

### Example 3: Small Tool in Steel

**Setup**:
- Material: 4140 Steel
- Tool: 1/8" 4-flute endmill
- Max RPM: 10,000

**Step 1**: Desired cutting speed = 250 SFM
$$N = \frac{3.82 \times 250}{0.125} = 7640 \text{ RPM}$$ ✓ (within limit)

**Step 2**: Chip load for small tool
- 1/8" diameter: 0.0015" per tooth (conservative)

**Step 3**: Calculate feed rate
$$F = 0.0015 \times 4 \times 7640 = 46 \text{ IPM}$$

**Check minimum chip load**:
- 0.0015" > 0.0005" ✓ (adequate)

### Example 4: Face Milling

**Setup**:
- Material: Cast iron
- Tool: 3" face mill, 6 inserts
- Cutting speed: 400 SFM

**Step 1**: Calculate RPM
$$N = \frac{3.82 \times 400}{3.0} = 509 \text{ RPM}$$

**Step 2**: Chip load
- Cast iron: 0.008" per tooth

**Step 3**: Calculate feed rate
$$F = 0.008 \times 6 \times 509 = 24 \text{ IPM}$$

**Note**: All inserts engaged simultaneously in face milling (different from endmill where engagement varies)

## Adjusting Feed Rates

### Increase Feed When:

**1. Roughing operations**
- Goal: Maximum material removal
- Increase to upper range of chip load recommendations

**2. Aluminum / soft materials**
- Can handle 2-3× higher feeds than steel
- Use aggressive chip loads

**3. Rigid setup**
- Solid fixturing allows higher forces
- Increase 20-30%

**4. Sharp tools**
- New tools can handle higher feeds
- Increase 10-20%

**5. Proper coolant**
- Flood coolant enables higher feeds
- Better chip evacuation

**6. Light radial engagement (HSM)**
- Chip thinning allows 2-5× higher feed rate
- Compensate with formula above

### Reduce Feed When:

**1. Finishing operations**
- Surface finish priority
- Reduce to lower range (often 50% of roughing)

**2. Small tools (< 1/4")**
- Deflection risk
- Reduce 30-50%

**3. Long tool overhang**
- Tool chatter risk
- Reduce 20-40%

**4. Hard materials**
- Titanium, Inconel, hardened steel
- Reduce 30-50% from steel values

**5. Poor fixturing**
- Workpiece movement risk
- Reduce 30-50%

**6. Machine vibration**
- Reduce until chatter stops
- Often 20-40% reduction needed

**7. Tool wear**
- Dull tools need lower feeds
- Reduce 20-30% or change tool

## Feed Rate vs Material Removal Rate

**Material Removal Rate (MRR)**:
$$MRR = DOC \times WOC \times F$$

where:
- $DOC$ = depth of cut (axial)
- $WOC$ = width of cut (radial)
- $F$ = feed rate

**Units**: cubic inches per minute (in³/min) or cm³/min

**Example**:
- DOC = 0.200"
- WOC = 0.400"
- F = 40 IPM
$$MRR = 0.200 \times 0.400 \times 40 = 3.2 \text{ in³/min}$$

**Optimization strategy**:
To increase MRR, prioritize changes in this order:
1. Increase DOC (least effect on tool life)
2. Increase feed rate (moderate effect)
3. Increase cutting speed (greatest effect on tool life)

**Example comparison** (same MRR = 3.2 in³/min):

**Option A**: DOC = 0.1", WOC = 0.4", F = 80 IPM
**Option B**: DOC = 0.4", WOC = 0.4", F = 20 IPM

Both produce 3.2 in³/min, but Option B (deeper, slower) is gentler on tool.

## Adaptive Feed Rate Control

**Modern CAM systems** vary feed rate based on engagement:

**Full slot** (100% engagement):
- Reduce feed 40-60%
- High cutting forces

**50% engagement**:
- Standard feed rate

**Light engagement** (< 25%):
- Increase feed 100-300%
- Chip thinning compensation

**Corners** (direction change):
- Reduce feed 30-50%
- Prevent tool breakage from deceleration forces

**Example program** with adaptive feed:
```gcode
(Adaptive feed rates based on engagement)
G1 X1.0 F80    (Light engagement, high feed)
X2.0 Y1.0 F30  (Full slot, reduced feed)
G2 X3.0 Y0 I0.5 J0 F20  (Arc/corner, further reduced)
```

## Drilling Feed Rates

**Different approach**: Feed per revolution, not feed per tooth

**Formula**:
$$f_r = \frac{F}{N}$$

where $f_r$ = feed per revolution (IPR or mm/rev)

**Recommended feed per revolution**:

| Material | 1/8" drill | 1/4" drill | 1/2" drill | 1" drill |
|----------|-----------|-----------|-----------|----------|
| Aluminum | 0.004 | 0.008 | 0.015 | 0.025 |
| Steel | 0.002 | 0.005 | 0.010 | 0.020 |
| Stainless | 0.001 | 0.003 | 0.006 | 0.012 |
| Cast Iron | 0.003 | 0.006 | 0.012 | 0.020 |

**Example**:
1/4" drill in aluminum, 3000 RPM:
- f_r = 0.008 IPR
$$F = 0.008 \times 3000 = 24 \text{ IPM}$$

**Peck drilling**: Reduce feed rate 10-20% (frequent entry/exit shock)

## Troubleshooting Feed Rate Issues

### Problem: Poor Surface Finish

**Likely cause**: Feed too high

**Solution**:
- Reduce feed per tooth 30-50%
- Increase RPM (more cuts per inch)
- Check tool sharpness
- Verify minimum chip load still maintained

### Problem: Tool Breakage

**Likely cause**: Feed too high (overload)

**Solution**:
- Reduce feed 40-60%
- Check for chip thinning (increase if light engagement)
- Verify adequate spindle torque at RPM

### Problem: Tool Burning / Rapid Wear

**Likely cause**: Feed too low (rubbing)

**Solution**:
- Increase feed rate 50-100%
- Calculate actual chip load (check minimum 0.0005")
- May need to reduce RPM to maintain chip load

### Problem: Vibration / Chatter

**Causes**: Multiple possibilities

**Solutions to try**:
1. Increase feed 20-30% (heavier cut dampens vibration)
2. Decrease feed 20-30% (reduce forces)
3. Change RPM ±15%
4. Reduce DOC/WOC
5. Shorten tool overhang

### Problem: Machine Stalling

**Likely cause**: Feed too high for available power/torque

**Solution**:
- Reduce feed rate 30-50%
- If at low RPM: Reduce DOC (torque-limited)
- If at high RPM: Check spindle power rating

## Feed Rate Optimization Workflow

**Step 1**: Calculate baseline feed rate
- Use material/tool recommendations
- Calculate: F = f_z × Z × N

**Step 2**: Adjust for conditions
- Scale up/down based on factors above
- Check minimum chip load maintained

**Step 3**: Program and test
- Start at 75% of calculated feed
- Monitor sound, vibration, finish

**Step 4**: Optimize
- Gradually increase until:
  - Surface finish degrades, or
  - Vibration occurs, or
  - Machine power limit reached
- Back off 10-15% for production

**Step 5**: Document
- Record optimal parameters
- Note tool life achieved
- Update for future jobs

## Summary

**Key formulas**:
- Feed rate: $F = f_z \times Z \times N$
- Feed per tooth: $f_z = F / (Z \times N)$
- Surface finish: $Ra = f_z^2 / (32 \times r)$
- Chip thinning: $h = f_z \times \sqrt{RDOC/D}$

**Critical principles**:
1. Feed per tooth (chip load) is the fundamental parameter
2. Maintain minimum chip load (0.0005") to avoid rubbing
3. Surface finish improves with lower feed per tooth (quadratic relationship)
4. Compensate for chip thinning in light radial cuts
5. Balance feed rate for tool life, surface finish, and cycle time

**Decision framework**:
1. Select feed per tooth based on material and tool size
2. Calculate feed rate: F = f_z × Z × N
3. Adjust for operation (roughing vs finishing)
4. Compensate for chip thinning if applicable
5. Test and optimize based on results

---

**Next**: [20.5 Depth of Cut and Width of Cut](section-20.5-depth-width-of-cut.md)

---

# 20.8 Coolant and Chip Management

## Functions of Coolant

Coolant (also called cutting fluid) serves multiple critical functions:

### 1. Cooling

**Primary function**: Remove heat from cutting zone

**Heat generation**:
- 60-80% carried away by chip
- 10-20% absorbed by tool
- 10-20% enters workpiece
- Coolant intercepts heat before it damages tool or workpiece

**Temperature reduction**:
- Flood coolant: Reduces cutting temperature 200-400°F
- Tool life improvement: 2-5× (due to exponential wear/temperature relationship)

### 2. Lubrication

**Reduces friction**:
- Between chip and tool rake face (secondary shear zone)
- Between tool flank and workpiece (tertiary zone)

**Results**:
- Lower cutting forces (10-30% reduction)
- Better surface finish
- Reduced tool wear

**Most effective at low speeds** (<200 SFM):
- Longer contact time allows lubrication
- High speeds: Cooling function dominates (less time for lubrication)

### 3. Chip Flushing

**Evacuates chips** from cutting zone:
- Prevents chip recutting (surface finish)
- Prevents chip packing (tool breakage)
- Clears view for operator
- Critical in drilling (deep holes)

**Pressure matters**:
- Low pressure (gravity flow): Minimal flushing
- Medium pressure (50-100 PSI): Good flushing
- High pressure (300-1000 PSI): Excellent flushing, breaks chips

### 4. Corrosion Protection

**Protects metal surfaces**:
- Prevents rust on steel parts
- Protects machine ways and surfaces
- Maintains clean appearance

**Rust inhibitors** added to coolant formulations

## Types of Coolant

### Straight Oils (Mineral Oils)

**Composition**:
- Petroleum-based oil
- Additives: Sulfur, chlorine, phosphorus (extreme pressure)

**Properties**:
- Excellent lubrication
- Moderate cooling
- No mixing required (use straight)

**Applications**:
- Low-speed operations (tapping, threading, broaching)
- Difficult materials (stainless, titanium)
- Gear cutting, form tools
- Heavy-duty operations

**Advantages**:
- Best lubrication
- Good tool life
- No mixing issues

**Disadvantages**:
- Poor cooling vs water-based
- Smoke/mist at high speeds
- Fire hazard above 400°F
- Disposal issues
- Expensive

**Typical use**: 5-10% of metalworking operations

### Soluble Oils (Emulsifiable Oils)

**Composition**:
- Mineral oil (60-90%)
- Emulsifiers (allow mixing with water)
- Mixed with water at 5-20% concentration

**Properties**:
- Good lubrication (from oil)
- Good cooling (from water)
- Milky appearance when mixed

**Mixing ratios**:
- Heavy duty: 1:4 to 1:10 (oil:water) = 10-20%
- General purpose: 1:10 to 1:20 = 5-10%
- Light duty: 1:20 to 1:40 = 2.5-5%

**Applications**:
- General machining (milling, turning, drilling)
- Steel, aluminum, cast iron
- Most versatile coolant type

**Advantages**:
- Balance of cooling and lubrication
- Lower cost than straight oil
- Fire-safe (water-based)
- Easy to monitor (visual)

**Disadvantages**:
- Requires mixing and maintenance
- Bacterial growth (requires biocide)
- Separates over time (requires mixing)

**Typical use**: 50-60% of operations

### Semi-Synthetic Fluids

**Composition**:
- Small amount of mineral oil (2-30%)
- Chemical additives for lubrication
- Water-based
- Translucent to semi-transparent

**Properties**:
- Better cooling than soluble oils
- Good lubrication from additives
- Longer sump life
- Resistant to bacterial growth

**Mixing ratios**:
- 1:10 to 1:40 (typically 1:20) = 5%

**Applications**:
- General machining
- Aluminum (excellent choice)
- High-speed operations
- Grinding operations

**Advantages**:
- Excellent cooling
- Good lubrication
- Long sump life (3-6 months)
- Less bacteria than soluble oils
- Clean (no oil residue)

**Disadvantages**:
- More expensive than soluble oils
- Skin irritation (some users)
- Harder to monitor concentration

**Typical use**: 30-40% of operations

### Synthetic Fluids

**Composition**:
- No petroleum oil (water + chemical additives only)
- Synthetic lubricants and corrosion inhibitors
- Clear solution

**Properties**:
- Excellent cooling (highest of all)
- Moderate lubrication (chemical-based)
- Very long sump life (6-12 months)
- Excellent bacterial resistance

**Mixing ratios**:
- 1:20 to 1:100 = 1-5%

**Applications**:
- Grinding operations (cooling critical)
- High-speed machining
- Aluminum (excellent choice)
- Light-duty operations

**Advantages**:
- Best cooling performance
- Longest sump life
- Clean (no oil residue)
- Minimal bacterial growth
- Easy to see work (clear)

**Disadvantages**:
- Poorest lubrication
- Most expensive
- Not suitable for heavy cuts or difficult materials
- Staining issues on some metals

**Typical use**: 5-10% of operations

## Coolant Selection Guide

| Operation | Material | Recommended Coolant |
|-----------|----------|---------------------|
| High-speed milling | Aluminum | Semi-synthetic or synthetic |
| General milling | Steel | Soluble oil or semi-synthetic |
| Turning | Steel, stainless | Soluble oil |
| Drilling | All | Soluble oil (through-spindle) |
| Tapping | All | Straight oil or soluble oil (20%) |
| Threading | All | Straight oil |
| Grinding | All | Synthetic or semi-synthetic |
| Titanium | Titanium | Straight oil (never water-based) |
| Magnesium | Magnesium | Mineral oil (never water-based) |

**Special cases**:
- **Cast iron**: Dry cutting preferred (graphite self-lubricates)
- **Titanium**: Water-based causes fire risk and hydrogen embrittlement
- **Magnesium**: Water-based causes violent fire (burns at 3100°F)

## Coolant Delivery Methods

### Flood Cooling

**Description**: High-volume coolant flow over cutting area

**Flow rates**:
- Small machines: 1-5 GPM (gallons per minute)
- Large machines: 10-50 GPM

**Pressure**:
- Typical: 50-100 PSI (gravity + pump)
- High-pressure: 300-1000 PSI (optional)

**Advantages**:
- Excellent cooling
- Good chip flushing
- Covers large area
- Simple system

**Disadvantages**:
- Messy (splash, mist)
- Large sump required (30-100 gallons)
- Maintenance intensive
- Environmental concerns (disposal)

**Applications**: General production machining, most CNC operations

### Mist Cooling

**Description**: Atomized coolant mixed with compressed air

**Delivery**:
- Air pressure: 60-100 PSI
- Coolant flow: 2-20 ml/hour
- Creates fine mist

**Advantages**:
- Minimal coolant consumption
- Clean (little splash)
- Good visibility
- Small sump (1-5 gallons)

**Disadvantages**:
- Inhalation hazard (requires extraction)
- Poor chip flushing
- Limited cooling vs flood
- Not for heavy cuts

**Applications**: Light-duty milling, engraving, hobbyist machines

**Safety**: **Mist extraction system mandatory** (respiratory hazard)

### Minimum Quantity Lubrication (MQL)

**Description**: Micro-droplets of lubricant in air stream

**Delivery**:
- Flow rate: 2-50 ml/hour (extremely low)
- Air pressure: 60-90 PSI
- Directed at cutting edge

**Advantages**:
- Virtually dry machining (minimal fluid)
- No disposal issues
- Clean parts (no washing)
- Environmentally friendly
- Cost savings (minimal fluid consumption)

**Disadvantages**:
- Limited cooling (air blast only)
- Requires extraction
- More expensive equipment
- Not for all materials/operations

**Applications**:
- Aluminum machining
- Titanium (with straight oil)
- High-speed machining
- Environmentally sensitive operations

**Best results with**:
- High cutting speeds (less heat generation per unit)
- Sharp tools
- Light to moderate DOC

### Through-Tool (Through-Spindle) Coolant

**Description**: Coolant pumped through hollow tool, exits at cutting edge

**Pressure**:
- Standard: 300-500 PSI
- High-pressure: 1000-1500 PSI

**Advantages**:
- Excellent cooling at cutting edge
- Superior chip evacuation (drilling)
- Breaks chips (high pressure)
- Works in blind holes

**Disadvantages**:
- Requires special tooling (hollow tools)
- High-pressure pump needed ($3k-10k)
- Machine must support through-spindle coolant
- Higher tool cost

**Applications**:
- Deep hole drilling (> 3× diameter)
- Gun drilling
- Tapping (excellent chip clearing)
- High-performance machining

**Performance**:
- Tool life improvement: 50-200% in drilling
- Enables deeper holes (10× diameter possible)
- Faster speeds and feeds

### Dry Machining

**Description**: No coolant used

**Advantages**:
- No coolant cost
- No disposal cost
- Clean parts (no washing)
- No coolant-related health issues
- Environmentally friendly

**Disadvantages**:
- Limited tool life (no cooling)
- Lower speeds required
- Not suitable for all materials
- Heat in workpiece (distortion risk)

**When appropriate**:
- **Cast iron** (graphite self-lubricates - preferred!)
- **Aluminum** (good thermal conductivity, with air blast)
- **Brass** (free-machining, low forces)
- Finishing operations (light cuts, less heat)

**Requirements for success**:
- Coated tools (TiAlN)
- High cutting speeds (less time for heat transfer)
- Air blast for chip clearing
- Proper chip evacuation

## Coolant Concentration and Maintenance

### Measuring Concentration

**Why important**:
- Too dilute: Poor lubrication, corrosion, bacteria growth
- Too concentrated: Waste, residue, skin irritation, foaming

**Refractometer method** (most accurate):
- Measures refractive index of fluid
- Read Brix scale
- Convert to concentration using coolant factor
- Example: Read 5.0° Brix, factor = 1.0, concentration = 5%

**Measuring frequency**:
- Daily: High-use machines
- Weekly: General machines
- After adding water or coolant

**Correcting concentration**:
- Too dilute: Add concentrated coolant
- Too concentrated: Add water (soft water preferred)

### pH Management

**Target pH**: 8.5-9.5 (alkaline)

**Why important**:
- pH < 8.0: Bacterial growth, corrosion risk
- pH > 10.0: Skin irritation, foam, shortened sump life

**Measuring**: pH test strips or pH meter

**Correcting pH**:
- Too low: Add biocide (kill bacteria) or alkaline buffer
- Too high: Dilute with water or add buffer

### Bacterial Control

**Problem**: Water-based coolants support bacterial growth
- Smells: Rotten egg smell (sulfur bacteria)
- Appearance: Slime, discoloration
- pH drops: Bacteria produce acids

**Prevention**:
- Maintain proper concentration (bacteria thrive when dilute)
- Good aeration (bacteria are often anaerobic)
- Clean sump regularly
- Remove tramp oil (floating oil feeds bacteria)

**Treatment**:
- Biocides: Add per manufacturer spec
- Pasteurization: Heat coolant to 160°F for 30 minutes
- Replacement: Last resort if severe contamination

**Frequency**:
- Biocide: Every 2-4 weeks (preventive)
- Sump cleaning: Every 3-6 months

### Tramp Oil Removal

**Tramp oil**: Hydraulic oil, way oil, slideway oil contaminating coolant

**Problems**:
- Feeds bacterial growth
- Reduces cooling effectiveness
- Smoke/mist generation
- Shortened sump life

**Removal methods**:
- Skimmer: Floating belt or disk removes oil from surface
- Coalescer: Filters fine oil droplets
- Manual: Skim with absorbent pads

**Prevention**: Regular machine maintenance (stop leaks)

## Chip Management

### Chip Formation

**Ideal chips**: Short, broken segments (easy to handle, good evacuation)

**Problem chips**:
- Long, stringy chips (tangle, safety hazard)
- Fine dust (inhalation, fire/explosion risk)
- Hot chips (burn risk)

**Chip control methods**:
1. **Chip breaker geometry** on tool (most important)
2. **Proper coolant** (pressure breaks chips)
3. **Feed rate** (heavier feed = thicker, more brittle chips)
4. **Material properties** (brittle materials break naturally)

### Chip Breakers

**Function**: Force chip to curl tightly and fracture

**Types**:
- Form ground: Groove in rake face
- Clamped: Separate chip breaker piece
- Geometry: Built into insert design

**Selection**:
- Aggressive (deep groove): Heavy cuts, soft materials, long chips
- Moderate: General purpose
- Light (shallow groove): Finishing, hard materials, thin chips

**Material-specific**:
- Steel: Chip breakers very effective
- Aluminum: Less effective (ductile, soft)
- Cast iron: Not needed (brittle chips naturally)
- Stainless: Critical (gummy, stringy chips)

### Chip Evacuation

**Importance**:
- Prevents chip recutting (finish)
- Prevents chip packing (tool breakage)
- Allows coolant access to cutting zone
- Safety (keeps work area clear)

**Methods**:

**1. Gravity** (simplest):
- Machine bed slopes to chip pan
- Effective for heavy chips (steel, cast iron)
- Not effective for fine chips (aluminum)

**2. Coolant flushing**:
- High flow rate washes chips away
- Direction matters (aim chips toward drain)
- Through-tool coolant excellent for drilling

**3. Air blast**:
- Compressed air directed at cutting zone
- Effective for dry machining
- Caution: Creates airborne particles (extraction needed)

**4. Auger conveyors**:
- Screw conveyor in chip pan
- Moves chips to collection point
- Common on production machines

**5. Chip conveyor belts**:
- Hinged steel belt or magnetic belt
- Continuous removal from sump
- Separates chips from coolant (returns coolant)

**In drilling**:
- **Peck cycle**: Retract frequently to break and evacuate chips
- **Through-tool coolant**: Flushes chips out of hole
- **Chip breaker geometry**: Breaks long chips into segments

### Chip Disposal

**Volume**: Significant in production (hundreds of pounds per day)

**Options**:

**1. Scrap metal recycling**:
- Steel, aluminum, brass have scrap value
- Cleaner chips = higher value
- Dry chips more valuable (no coolant)

**2. Chip processing**:
- Centrifuge: Removes coolant (recovers coolant)
- Briquetting: Compresses chips into dense blocks
- Result: Easier transport, higher scrap value

**3. Waste disposal**:
- Chips with coolant = hazardous waste (expensive)
- Dry chips = metal scrap (value)
- **Incentive for dry machining or MQL**

**Safety**:
- Sharp chips (cut risk - use gloves, tools)
- Hot chips (burn risk - allow cooling)
- Never handle with bare hands while machine running
- Fire risk (magnesium, titanium fine chips)

## Safety Considerations

### Coolant Health Hazards

**Skin contact**:
- Dermatitis (irritation, rash)
- Bacterial contamination risk
- Chemical sensitivity

**Prevention**:
- Barrier cream before work
- Wash hands frequently
- Avoid prolonged contact
- Use gloves for chip handling

**Inhalation**:
- Mist/vapor from high-speed cutting
- Bacterial aerosols (legionella risk)
- Chemical irritants

**Prevention**:
- Mist collection system
- Good ventilation
- Regular coolant maintenance (control bacteria)

**Ingestion** (rare):
- Splashing into mouth
- Eating with contaminated hands

**Prevention**:
- Wash hands before eating
- No food/drink in machine area

### MSDS / SDS

**Material Safety Data Sheet**: Required for all coolants

**Contains**:
- Chemical composition
- Health hazards
- First aid procedures
- Handling and storage
- Disposal requirements
- Emergency contact

**Read and understand** before using any coolant.

### Fire Hazards

**Straight oils**:
- Flammable (flash point 300-450°F)
- Can ignite at high cutting temperatures
- Fire extinguisher accessible

**Water-based coolants**:
- Non-flammable (water-based)
- Safer for high-speed operations

**Special cases**:
- **Magnesium**: Water-based coolant causes violent fire
  - Use mineral oil only
  - Class D extinguisher required
- **Titanium**: Fine chips pyrophoric (self-ignite)
  - Never allow chip accumulation
  - Mineral oil only (water causes fire)

## Troubleshooting

### Problem: Poor Tool Life

**Possible causes**:
1. Insufficient cooling (dilute coolant)
2. Wrong coolant type (lubrication inadequate)
3. Low flow rate (not reaching cutting zone)

**Solutions**:
- Check concentration, increase if low
- Switch to soluble oil or straight oil (better lubrication)
- Increase flow rate, direct nozzle at cutting edge

### Problem: Poor Surface Finish

**Possible causes**:
1. Chip recutting (poor flushing)
2. Built-up edge (inadequate lubrication)
3. Coolant contamination (swarf, bacteria)

**Solutions**:
- Improve coolant direction and flow
- Increase concentration or switch to better lubricating coolant
- Clean and filter coolant

### Problem: Coolant Odor

**Cause**: Bacterial growth (anaerobic bacteria produce H₂S)

**Solutions**:
- Add biocide
- Increase concentration (bacteria thrive when dilute)
- Improve aeration (skim off floating oil, circulate coolant)
- Clean sump thoroughly
- If severe: Replace coolant

### Problem: Foaming

**Causes**:
1. Too concentrated
2. Contamination (detergent, soap)
3. Soft water (excessive)

**Solutions**:
- Dilute to proper concentration
- Avoid contamination (clean tools before using)
- Add defoamer (small amount)
- Change coolant if severe

### Problem: Rust on Parts

**Causes**:
1. Insufficient concentration (corrosion inhibitors diluted)
2. Low pH (acidic = corrosion)
3. Coolant aged (additives depleted)

**Solutions**:
- Increase concentration
- Check and correct pH (target 8.5-9.5)
- Replace coolant if old (>6 months)
- Dry parts promptly after machining

## Summary

**Coolant functions**:
1. Cooling (temperature control, tool life)
2. Lubrication (reduce forces, improve finish)
3. Chip flushing (evacuation, visibility)
4. Corrosion protection

**Coolant types**:
- **Straight oil**: Best lubrication, low-speed operations
- **Soluble oil**: Versatile, general machining
- **Semi-synthetic**: Good balance, aluminum, high-speed
- **Synthetic**: Best cooling, grinding, least lubrication

**Delivery methods**:
- **Flood**: Standard for production
- **Mist/MQL**: Clean alternative, requires extraction
- **Through-tool**: Best for drilling, tapping
- **Dry**: Cast iron preferred, environmentally friendly

**Maintenance essentials**:
- Monitor concentration (refractometer)
- Check pH weekly (target 8.5-9.5)
- Control bacteria (biocide, cleanliness)
- Remove tramp oil
- Replace coolant 2-4× per year

**Chip management**:
- Chip breakers on tools
- Adequate coolant flow
- Evacuation system (gravity, conveyor)
- Proper disposal (recycle dry chips)

**Safety priorities**:
- Skin protection (barrier cream, gloves)
- Mist extraction (inhalation risk)
- MSDS review (know hazards)
- Special materials (magnesium, titanium - fire risk)

**Economic benefits of proper coolant management**:
- 2-5× tool life improvement
- Better surface finish (less rework)
- Faster cutting speeds
- Reduced machine downtime

---

**Next**: [20.9 Troubleshooting and Optimization](section-20.9-troubleshooting.md)

---

# Module 20 – Feeds and Speeds: Optimizing CNC Machining Parameters

## Overview

Feeds and speeds are the fundamental parameters controlling CNC machining operations. Proper selection optimizes tool life, surface finish, cycle time, and part quality while preventing tool breakage and machine damage.

This module provides comprehensive guidance on calculating and optimizing cutting parameters for various materials, tools, and operations.

## Module Contents

### Section 20.1: Introduction to Feeds and Speeds
- Cutting parameter fundamentals
- Material removal rate concepts
- Economic optimization principles
- Safety considerations

### Section 20.2: Cutting Mechanics and Tool Geometry
- Chip formation process
- Tool geometry terminology
- Cutting forces and power
- Temperature distribution

### Section 20.3: Cutting Speed (Spindle RPM)
- Surface speed (SFM/m/min) calculations
- RPM formulas for different operations
- Material-specific recommendations
- Tool material considerations

### Section 20.4: Feed Rate Optimization
- Feed per tooth vs feed per revolution
- Chip load calculations
- Feed rate tables by material
- Adaptive feed rate strategies

### Section 20.5: Depth of Cut and Width of Cut
- Radial vs axial engagement
- Roughing vs finishing strategies
- Stepover percentage guidelines
- Chip thinning effects

### Section 20.6: Material-Specific Parameters
- Aluminum alloys
- Steel (mild, alloy, stainless, tool steel)
- Cast iron
- Titanium alloys
- Plastics and composites
- Exotic materials

### Section 20.7: Tool Material Selection
- High-speed steel (HSS)
- Carbide grades and coatings
- Ceramics and CBN
- Diamond tooling (PCD, CVD)
- Tool material vs workpiece matching

### Section 20.8: Coolant and Chip Management
- Coolant types and selection
- Flood vs mist vs dry machining
- Minimum quantity lubrication (MQL)
- Chip evacuation strategies

### Section 20.9: Troubleshooting and Optimization
- Tool wear patterns and diagnosis
- Surface finish problems
- Vibration and chatter
- Power and torque limitations

### Section 20.10: Advanced Topics
- High-speed machining (HSM)
- Trochoidal milling
- Adaptive roughing
- Tool path optimization

### Section 20.11: Calculators and Formulas
- Quick reference formulas
- Online calculator tools
- CAM software integration
- Real-time monitoring

### Section 20.12: Case Studies and Practical Examples
- Common machining scenarios
- Before/after optimization examples
- Industry best practices
- Economic analysis

---

## Key Learning Objectives

By the end of this module, you will be able to:

1. Calculate appropriate spindle RPM from surface speed and tool diameter
2. Determine optimal feed rates based on chip load and material
3. Select depth of cut and width of cut for roughing and finishing
4. Adjust parameters for different materials and tool types
5. Diagnose problems from tool wear patterns and surface finish
6. Optimize for tool life, cycle time, or cost per part
7. Apply high-speed machining strategies
8. Use CAM software effectively for parameter generation

---

## Prerequisites

- Module 6: Spindle Systems (spindle capabilities and limitations)
- Module 15: G-Code Programming (feed rate commands)
- Basic algebra (formulas and conversions)
- Understanding of materials (Module 17 helpful but not required)

---

## Course Integration

**Feeds and speeds connect to**:
- **Mechanical design** (Modules 1-3): Machine rigidity affects maximum practical cutting forces
- **Spindle systems** (Module 6): Spindle power and speed range constrains parameters
- **Tool holding** (Module 6): Runout and grip affect achievable surface finish
- **Materials** (Module 17): Advanced materials require specialized parameters
- **CAM programming** (Module 16): CAM generates toolpaths with embedded F&S

---

**Begin with**: [20.1 Introduction to Feeds and Speeds](section-20.1-introduction.md)

---

# 20.1 Introduction to Feeds and Speeds

## What Are Feeds and Speeds?

**Cutting Parameters**: The numerical values controlling how fast a cutting tool moves and rotates during machining.

**Three Primary Parameters**:

1. **Cutting Speed (V)**: The velocity at which the cutting edge passes through material
   - Measured in surface feet per minute (SFM) or meters per minute (m/min)
   - Determines spindle RPM for given tool diameter

2. **Feed Rate (F)**: The velocity at which the tool advances into the workpiece
   - Measured in inches per minute (IPM) or millimeters per minute (mm/min)
   - Determines thickness of material removed per revolution or per tooth

3. **Depth of Cut (DOC)**: The thickness of material removed in a single pass
   - Axial depth of cut (ADOC): How deep the tool plunges
   - Radial depth of cut (RDOC): How much the tool steps over

## Why Feeds and Speeds Matter

### Tool Life

**Tool wear rate** increases exponentially with cutting speed:

**Taylor Tool Life Equation**:
$$V T^n = C$$

where:
- $V$ = cutting speed
- $T$ = tool life (minutes until dullness)
- $n$ = Taylor exponent (material-dependent, typically 0.2-0.5)
- $C$ = constant for tool/material combination

**Example**:
For 1018 steel with carbide tool, $n$ = 0.25:
- At 400 SFM: Tool life = 60 minutes
- At 500 SFM (+25%): Tool life = 60 × (400/500)⁴ = 25 minutes (-58%)
- At 320 SFM (-20%): Tool life = 60 × (400/320)⁴ = 129 minutes (+115%)

**Key Insight**: Small changes in cutting speed produce large changes in tool life.

### Surface Finish

**Feed per tooth** is the primary factor affecting surface finish:

**Theoretical surface roughness** (Ra):
$$Ra = \frac{f_z^2}{32 r}$$

where:
- $f_z$ = feed per tooth (inches or mm)
- $r$ = tool nose radius

**Example**:
0.010" feed per tooth, 0.031" nose radius:
$$Ra = \frac{0.010^2}{32 \times 0.031} = 0.0001" = 100 \mu\text{in}$$

Halving feed per tooth: Ra = 25 μin (4× smoother)

**Practical surface finish** also depends on:
- Tool sharpness and wear
- Vibration and chatter
- Material properties
- Coolant effectiveness

### Cycle Time

**Material Removal Rate (MRR)**:
$$MRR = DOC \times WOC \times F$$

where:
- $DOC$ = depth of cut
- $WOC$ = width of cut (radial engagement)
- $F$ = feed rate

**Example**:
- DOC = 0.100"
- WOC = 0.500"  
- Feed = 40 IPM
- MRR = 0.100 × 0.500 × 40 = 2.0 cubic inches per minute

To remove 20 cubic inches: Time = 20 / 2.0 = 10 minutes

**Optimization Trade-off**:
- Faster speeds → More MRR but shorter tool life
- Balance tool cost and cycle time for minimum cost per part

### Machine Power and Torque

**Specific Cutting Energy (U)**: Power required to remove unit volume of material

| Material | U (hp/(in³/min)) | U (W/(cm³/s)) |
|----------|------------------|---------------|
| Aluminum 6061 | 0.15-0.25 | 0.7-1.1 |
| Mild Steel 1018 | 0.60-0.80 | 2.7-3.6 |
| Stainless 304 | 1.0-1.5 | 4.5-6.8 |
| Titanium Ti-6Al-4V | 1.2-1.8 | 5.4-8.1 |
| Cast Iron | 0.40-0.60 | 1.8-2.7 |

**Power Required**:
$$P = MRR \times U \times K$$

where $K$ is inefficiency factor (typically 0.7-0.9)

**Example**:
Machining 1018 steel at MRR = 2.0 in³/min:
- $P$ = 2.0 × 0.70 × 0.80 = 1.1 hp at spindle
- Motor power required: 1.1 / 0.75 (efficiency) = 1.5 hp minimum

**Torque at Spindle**:
$$T = \frac{P \times 5252}{RPM}$$

where:
- $T$ = torque (lb-ft)
- $P$ = power (hp)
- RPM = spindle speed

**Example**:
1.1 hp at 2000 RPM:
$$T = \frac{1.1 \times 5252}{2000} = 2.9 \text{ lb-ft}$$

**Machine Limitations**:
- Spindle power curve limits MRR at low RPM (torque limited)
- Maximum spindle power limits MRR at high RPM (power limited)
- Must check both power and torque when selecting parameters

## Historical Context

### Early Manual Machining

**Pre-1900**:
- Belt-driven machines with discrete speeds (step pulleys)
- Feeds and speeds selected by machinist experience
- "Run it until it smokes, then back off a bit"
- No scientific optimization

**Early 20th Century**:
- Frederick W. Taylor (1906): Scientific study of metal cutting
- Developed Taylor Tool Life Equation
- Established optimization principles (minimum cost vs maximum production)
- Machinery's Handbook (1914): First comprehensive speed/feed tables

### CNC Era

**1950s-1970s**:
- Numerical control enables precise, repeatable parameters
- Computer-aided calculations
- Coated carbide tools expand speed ranges

**1980s-Present**:
- CAM software automates parameter selection
- Tool manufacturers provide extensive databases
- High-speed machining strategies
- Adaptive control systems adjust parameters in real-time

## Fundamental Concepts

### Cutting Speed vs Spindle Speed

**Cutting Speed (V)**: The speed at which the cutting edge moves through material (SFM or m/min)
- Independent of tool size
- Material-dependent (aluminum faster than steel)

**Spindle Speed (N)**: Rotational speed of spindle (RPM)
- Depends on tool diameter
- Machine-limited (max RPM varies by spindle)

**Relationship**:
$$N = \frac{12 V}{\pi D} = \frac{3.82 V}{D}$$ (Imperial: SFM, inches, RPM)

$$N = \frac{1000 V}{\pi D} = \frac{318.3 V}{D}$$ (Metric: m/min, mm, RPM)

**Example (Imperial)**:
Machining aluminum (V = 600 SFM) with 1/2" endmill:
$$N = \frac{3.82 \times 600}{0.5} = 4584 \text{ RPM}$$

Same speed with 2" face mill:
$$N = \frac{3.82 \times 600}{2.0} = 1146 \text{ RPM}$$

**Key Insight**: Larger tools run slower RPM for same cutting speed.

### Feed Per Tooth vs Feed Rate

**Feed Per Tooth (f_z)**: Distance tool advances per cutting edge
- Primary specification in machining data
- Typical range: 0.001-0.020" (0.025-0.50 mm)

**Feed Per Revolution (f_r)**: Distance tool advances per spindle revolution
- For single-point tools (turning, boring)
- $f_r = f_z \times Z$ (where $Z$ = number of teeth)

**Feed Rate (F)**: Tool advance speed (IPM or mm/min)
$$F = f_z \times Z \times N$$

**Example**:
4-flute endmill at 3000 RPM with f_z = 0.003":
$$F = 0.003 \times 4 \times 3000 = 36 \text{ IPM}$$

**G-Code Example**:
```gcode
S3000 M3      (Spindle 3000 RPM, CW)
F36           (Feed rate 36 IPM)
G1 X2.0 Y1.0  (Linear move at 36 IPM)
```

### Material Removal Rate

**MRR Calculation**:

**Milling**:
$$MRR = ADOC \times RDOC \times F$$

**Turning**:
$$MRR = DOC \times F \times \pi D$$

**Drilling**:
$$MRR = \frac{\pi D^2}{4} \times F$$

**Units**:
- Imperial: cubic inches per minute (in³/min)
- Metric: cubic centimeters per minute (cm³/min)

**Example - Slot Milling**:
- 1/2" endmill (full slot, RDOC = 0.5")
- ADOC = 0.25"
- Feed = 30 IPM
- MRR = 0.25 × 0.5 × 30 = 3.75 in³/min

### Chip Load (Feed Per Tooth)

**Definition**: The thickness of material removed by each cutting edge.

**Factors Affecting Chip Load**:

**1. Material Hardness**:
- Soft materials (aluminum): Higher chip loads (0.008-0.020")
- Hard materials (titanium, hardened steel): Lower chip loads (0.001-0.004")

**2. Tool Diameter**:
- Larger tools: Higher chip loads (more rigid)
- Smaller tools: Lower chip loads (deflection risk)

**Rule of Thumb**: Chip load ≈ 0.001-0.002" per 1/8" diameter

**3. Number of Flutes**:
- Fewer flutes (2-3): Larger chip loads, better chip evacuation
- More flutes (4-6): Smaller chip loads, smoother finish

**4. Engagement**:
- Full slot: Reduce chip load 25-50%
- Light radial (<25% diameter): Increase chip load (chip thinning effect)

**Minimum Chip Load**:
Below 0.0005", tool may rub instead of cut:
- Rapid wear
- Poor surface finish
- Heat buildup
- Potential tool breakage

**Always maintain minimum chip load**, even if it means reducing RPM.

## Optimization Strategies

### Maximum Production Rate

**Objective**: Remove material as fast as possible.

**Approach**:
1. Select highest cutting speed tool can withstand
2. Maximize DOC and WOC within machine power limits
3. Increase feed rate until surface finish or power limit reached
4. Accept shorter tool life (frequent tool changes acceptable)

**Applications**:
- High-volume production
- Automated tool changers available
- Material cost > labor cost

### Maximum Tool Life

**Objective**: Minimize tool changes and downtime.

**Approach**:
1. Reduce cutting speed 20-30% below maximum
2. Moderate DOC and feed rates
3. Ensure adequate coolant
4. Monitor wear and change tool before failure

**Applications**:
- Unattended machining (lights-out operations)
- Expensive or difficult tool changes
- Critical parts (tool breakage unacceptable)

### Minimum Cost Per Part

**Objective**: Lowest total cost (material + labor + tooling + overhead).

**Cost Per Part**:
$$C_{part} = \frac{t_{cycle}}{60}(C_{labor} + C_{overhead}) + \frac{t_{cycle}}{T_{tool}}C_{tool change}$$

where:
- $t_{cycle}$ = cycle time (minutes)
- $C_{labor}$ = labor rate ($/hour)
- $C_{overhead}$ = machine rate ($/hour)
- $T_{tool}$ = tool life (minutes of cutting)
- $C_{tool change}$ = cost to change tool (tool cost + labor)

**Optimal Cutting Speed** (minimum cost):
$$V_{opt} = V_{max} \left[\frac{1}{n}\left(\frac{C_{tool change}/T_{max}}{C_{labor} + C_{overhead}}\right)\right]^{1/(1-n)}$$

**In Practice**:
- Calculate cost per part at several speeds
- Plot cost vs speed curve
- Select minimum point (often 15-25% below max speed)

### Best Surface Finish

**Objective**: Achieve required surface roughness.

**Approach**:
1. Reduce feed per tooth (primary factor)
2. Use sharp tools with polished cutting edges
3. Increase spindle speed (more cuts per inch of travel)
4. Optimize tool geometry (larger nose radius)
5. Finish passes with minimal RDOC (< 0.020")

**Applications**:
- Cosmetic surfaces
- Sealing surfaces
- Precision fits
- Mating surfaces

## Safety Considerations

### Tool Breakage Hazards

**Causes of Tool Breakage**:
- Excessive feed rate (overload)
- Too much DOC for tool diameter
- Spindle stall (insufficient torque)
- Vibration and chatter
- Workpiece movement (poor fixturing)
- Tool collision (programming error)

**Risks**:
- Flying tool fragments (eye hazard)
- Workpiece damage (scrap part)
- Spindle damage (bent shaft, bearing damage)
- Machine crash

**Prevention**:
- Conservative parameters for first cuts
- Gradual parameter increase (test and verify)
- Monitor spindle load (audible feedback, load meter)
- Proper fixturing and clamping
- Simulation and verification of G-code

### Fire Hazards

**Combustible Materials**:
- Magnesium chips ignite easily (burn at 3100°F)
- Titanium chips pyrophoric when fine
- Composite dust explosive

**Prevention**:
- No water-based coolant on magnesium or titanium
- Mineral oil or approved coolants only
- Regular chip removal (no accumulation)
- Fire extinguisher (Class D for metal fires)

### Chip Hazards

**Sharp Chips**:
- Steel chips cut skin easily
- Long stringy chips wrap around tools (entanglement risk)

**Prevention**:
- Chip breaker geometry on tools
- Proper coolant pressure (break chips)
- Eye protection mandatory
- Gloves for chip removal (machine stopped!)
- Never remove chips by hand while machine running

### Coolant Hazards

**Health Risks**:
- Mist inhalation (respiratory irritation)
- Skin contact (dermatitis)
- Bacterial growth (bio-contamination)

**Prevention**:
- Mist collection system
- Proper coolant maintenance (pH, concentration)
- Skin barrier cream
- Wash hands frequently
- Material Safety Data Sheet (MSDS) review

## Parameter Starting Points

### Quick Reference by Material

| Material | Cutting Speed | Feed per Tooth | Notes |
|----------|---------------|----------------|-------|
| Aluminum 6061 | 600-1200 SFM | 0.005-0.015" | High speed, high feed |
| Brass | 400-800 SFM | 0.003-0.010" | Similar to aluminum |
| Mild Steel 1018 | 200-400 SFM | 0.003-0.008" | Moderate speed |
| Alloy Steel 4140 | 150-300 SFM | 0.002-0.006" | Harder, slower |
| Stainless 304 | 100-200 SFM | 0.002-0.005" | Work hardens, carbide tools |
| Tool Steel (RC 60) | 50-150 SFM | 0.001-0.003" | Very hard, carbide/ceramic |
| Titanium Ti-6Al-4V | 150-250 SFM | 0.002-0.005" | Low speed, sharp tools |
| Cast Iron | 250-500 SFM | 0.004-0.010" | Brittle chips, dry cut |
| Plastics (acrylic) | 500-1000 SFM | 0.003-0.010" | Sharp tools, avoid melt |
| Carbon Fiber | 500-800 SFM | 0.002-0.006" | Diamond tools, dust control |

**Note**: These are conservative starting points for carbide tooling. Adjust based on tool manufacturer data and actual results.

### Depth of Cut Guidelines

**Roughing**:
- ADOC: 0.5-1.5× tool diameter
- RDOC: 0.05-0.20× tool diameter (slotting avoid if possible)
- Goal: Maximum MRR without excessive load

**Finishing**:
- ADOC: 0.010-0.100" (light cut)
- RDOC: 0.010-0.030" (climb mill for best finish)
- Goal: Final dimensions and surface finish

**Example - 1/2" Endmill**:
- Roughing: ADOC = 0.5", RDOC = 0.1" (20% stepover)
- Finishing: ADOC = 0.030", RDOC = 0.015"

## Measurement and Verification

### Measuring Actual Feed Rate

**Method 1: Timed Distance**:
1. Jog to known start position
2. Execute G-code move (known distance)
3. Time with stopwatch
4. Calculate: Feed Rate = Distance / Time (convert to IPM or mm/min)

**Method 2: G-code Display**:
Most CNC controls display actual feed rate in real-time.

**Method 3: Chip Measurement**:
Measure chip thickness and compare to theoretical:
$$f_z = \frac{\text{chip thickness}}{\sin(\text{engagement angle})}$$

### Measuring Spindle Speed

**Tachometer**:
Optical or contact tachometer measures actual RPM.

**Sound Analysis**:
Spindle tone changes with RPM (experienced machinists "hear" speed).

**Strobe Light**:
Mark on spindle, strobe flashes sync with rotation.

**Control Display**:
Modern controls display commanded and actual RPM.

## Common Misconceptions

**Myth 1**: "Faster is always better"
- **Reality**: Faster RPM reduces tool life exponentially. Balance speed and life.

**Myth 2**: "More flutes = better"
- **Reality**: More flutes reduce chip space, risk clogging. 2-3 flutes often best for aluminum.

**Myth 3**: "Cutting oil prevents all problems"
- **Reality**: Poor parameters with coolant still fail. Coolant enhances good parameters.

**Myth 4**: "Speeds and feeds tables are exact"
- **Reality**: Tables are starting points. Adjust for specific machine, tool, and setup.

**Myth 5**: "Big machines need slow speeds"
- **Reality**: Machine rigidity enables higher speeds, not lower. Small machines may need conservative parameters due to flex.

## Learning Path

**Beginner** (Sections 20.1-20.3):
- Understand feed rate, spindle speed, DOC basics
- Calculate RPM from SFM
- Use manufacturer's starting values
- Focus on safe, conservative parameters

**Intermediate** (Sections 20.4-20.7):
- Optimize chip load for material
- Adjust for tool wear and life
- Select appropriate tooling grades
- Interpret tool wear patterns

**Advanced** (Sections 20.8-20.12):
- High-speed machining strategies
- Real-time adaptive control
- Economic optimization
- Troubleshoot complex problems

## Summary

Feeds and speeds are the foundation of successful CNC machining. Proper selection balances tool life, surface finish, cycle time, and cost.

**Key Principles**:
1. Cutting speed primarily affects tool life (exponential relationship)
2. Feed rate primarily affects surface finish (quadratic relationship)
3. MRR = DOC × WOC × F determines production rate
4. Always maintain minimum chip load (avoid rubbing)
5. Tables are starting points - adjust based on results
6. Safety first: conservative parameters until proven

**Next Steps**:
- Learn cutting mechanics (Section 20.2)
- Master RPM calculations (Section 20.3)
- Optimize feed rates (Section 20.4)
- Apply to specific materials (Section 20.6)

---

**Next**: [20.2 Cutting Mechanics and Tool Geometry](section-20.2-cutting-mechanics.md)

---

# 20.3 Cutting Speed and Spindle RPM Calculations

## Understanding Cutting Speed

**Cutting Speed (V)**: The velocity at which the cutting edge moves through material
- Imperial: Surface Feet per Minute (SFM)
- Metric: Meters per Minute (m/min)

**Spindle Speed (N)**: The rotational speed in RPM

**Why this matters**: Cutting speed determines tool wear and temperature. Same cutting speed = similar tool conditions regardless of tool size.

## RPM Calculation Formulas

### Imperial System

$$N = \frac{12 \times V}{\pi \times D} = \frac{3.82 \times V}{D}$$

**Quick approximation**: $N \approx \frac{4 \times V}{D}$

**Examples**:
- Aluminum 600 SFM, 1/2" endmill: N = 3.82 × 600 / 0.5 = 4584 RPM
- Steel 300 SFM, 2" face mill: N = 3.82 × 300 / 2.0 = 573 RPM

### Metric System

$$N = \frac{1000 \times V}{\pi \times D} = \frac{318.3 \times V}{D}$$

**Example**: Aluminum 200 m/min, 12mm endmill: N = 318.3 × 200 / 12 = 5305 RPM

### Reverse Calculation (RPM → SFM)

$$V = \frac{N \times D}{3.82} \text{ (Imperial)}$$

$$V = \frac{N \times D}{318.3} \text{ (Metric)}$$

## Recommended Cutting Speeds

### Ferrous Metals

| Material | HSS | Uncoated Carbide | Coated Carbide |
|----------|-----|------------------|----------------|
| Mild Steel 1018 | 90-120 | 250-350 | 350-500 |
| Alloy Steel 4140 | 50-80 | 150-250 | 250-400 |
| Stainless 304 | 40-60 | 100-150 | 150-250 |
| Tool Steel (annealed) | 40-60 | 100-150 | 150-250 |
| Tool Steel (hardened) | - | 50-150 | CBN: 200-400 |
| Cast Iron (gray) | 60-100 | 300-500 | Ceramic: 1000-2500 |

### Non-Ferrous Metals

| Material | HSS | Carbide | PCD |
|----------|-----|---------|-----|
| Aluminum 6061 | 200-400 | 600-1200 | 1500-4000 |
| Brass | 200-300 | 400-800 | - |
| Bronze | 90-150 | 300-600 | - |
| Copper | 100-150 | 300-500 | - |

### Exotic Alloys

| Material | Carbide | Ceramic/CBN |
|----------|---------|-------------|
| Titanium Ti-6Al-4V | 150-250 | - |
| Inconel 718 | 50-120 | 200-600 |
| Hastelloy | 40-80 | - |

### Non-Metals

| Material | Cutting Speed (SFM) |
|----------|---------------------|
| Plastics (acrylic, nylon) | 300-1200 |
| Carbon Fiber/Composites | 400-1500 (PCD recommended) |
| Wood | 300-1200 |
| Foam (tooling board) | 800-1500 |

## Operation-Specific Calculations

### Turning with Constant Surface Speed (CSS)

**Problem**: As diameter decreases, cutting speed drops if RPM stays constant.

**Solution**: Use CSS mode
```gcode
G96 S350 M3    (CSS mode, 350 SFM)
G50 S2000      (Max RPM limit)
```

Controller automatically adjusts: N = 3.82 × V / D_current

**Example**:
- At 2.0" diameter: 669 RPM
- At 1.5" diameter: 892 RPM (auto-adjusted)
- At 1.0" diameter: 1337 RPM (auto-adjusted)

### Drilling

Use drill diameter, but reduce RPM 25-50% for deep holes (>3× diameter) to improve chip evacuation.

**Example**: 1/4" drill, aluminum, 2" deep hole
- Standard: 300 SFM → 4584 RPM
- Deep hole: 2500 RPM (reduced for chip clearance)

### Reaming

Reduce cutting speed 50% compared to drilling (more flutes, finishing operation).

### Tapping

Not based on cutting speed optimization. Use:
$$N = \frac{F}{TPI}$$ or $$N = \frac{F}{P}$$ (metric)

## Adjusting Cutting Speeds

### Reduce Speed When:
- Tool material limited (HSS = 50% of carbide speeds)
- Machine lacks rigidity (reduce 20-30%)
- Small/long tools prone to deflection (reduce 20-50%)
- Interrupted cuts (reduce 10-30%)
- No coolant on steel (reduce 20-40%)

### Increase Speed When:
- High-speed machining with light engagement (increase 50-100%)
- Excellent fixturing and rigidity (increase 10-20%)
- Flood coolant available (increase 10-20%)
- Coated tools (increase 30-50% over uncoated)

## Spindle Limitations

### Typical RPM Ranges
- Manual mills: 60-4,000 RPM
- Hobby CNC: 1,000-10,000 RPM
- VMC (40-taper): 8,000-15,000 RPM
- VMC (30-taper): 12,000-20,000 RPM
- High-speed spindle: 24,000-60,000+ RPM

### Power vs Torque
- **Low RPM**: Torque-limited (heavy cuts possible)
- **High RPM**: Power-limited (light cuts only)

Formula: $T = \frac{P \times 5252}{N}$ (lb-ft, hp, RPM)

## Troubleshooting

**Tool burning/smoking**: Reduce RPM 25-40%, increase feed rate, check tool sharpness

**Poor surface finish**: Increase RPM 20-30% (aluminum/steel), check for tool wear

**Chatter**: Change RPM ±10-20% to shift away from resonance frequency

**Tool breakage**: Check feed rate first, reduce DOC if at low RPM (torque-limited)

## Summary

**Key principles**:
1. Use formula: N = 3.82 × V / D (Imperial) or N = 318.3 × V / D (Metric)
2. Select cutting speed based on material and tool material
3. Adjust for machine rigidity, tool size, and application
4. Always use CSS for turning operations
5. Check spindle limits (min/max RPM, power curve)

---

**Next**: [20.4 Feed Rate Optimization](section-20.4-feed-rate.md)
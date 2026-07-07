# Section 16.8: Assembly Design

## Introduction

Most mechanical systems consist of multiple parts working together. Assembly design in CAD involves not just modeling individual components, but defining how they fit, move, and interact. Good assembly design ensures parts can be manufactured individually, assembled efficiently, and serviced when needed. This section covers assembly modeling strategies, design for assembly (DFA) principles, and best practices for creating robust, manufacturable assemblies.

## Assembly Modeling Approaches

### Bottom-Up Design

**Process:**
1. Design individual parts independently
2. Create assembly file
3. Insert parts into assembly
4. Apply mates/constraints to position parts

**Advantages:**
- Parts can be designed and detailed independently
- Multiple designers can work in parallel
- Parts can be reused in different assemblies
- Part files remain independent (easier file management)

**Disadvantages:**
- Interface dimensions must be coordinated manually
- Changes to one part may not propagate to mating parts
- Risk of mismatched interfaces

**Best for:**
- Standard parts (bolts, bearings, purchased components)
- Modular designs with well-defined interfaces
- Large teams working on subsystems

**Example workflow:**
```
1. Design motor mount plate (separate file)
2. Design motor bracket (separate file)
3. Download motor CAD model (vendor)
4. Create assembly file
5. Insert all parts
6. Apply mates to align mounting holes
7. Check for interference
```

### Top-Down Design

**Process:**
1. Create assembly file first
2. Create skeleton sketch with critical interfaces
3. Design parts in context of assembly
4. Parts reference assembly geometry or other parts

**Advantages:**
- Interface dimensions automatically coordinated
- Changes propagate to all affected parts
- Parts designed to fit perfectly from the start
- Visualize whole system during design

**Disadvantages:**
- Complex file dependencies (external references)
- Cannot easily reuse parts in other assemblies
- File management more difficult
- Circular references can cause errors

**Best for:**
- Custom designs with many interfaces
- Single designer projects
- Designs where fit is critical
- Weldments and fabricated structures

**Example workflow:**
```
1. Create assembly file
2. Create master skeleton sketch:
   - Motor mounting face
   - Shaft centerline
   - Bolt pattern locations
3. Create motor mount part in assembly (references skeleton)
4. Create bracket in assembly (references motor mount and skeleton)
5. Parts automatically align because they share references
```

### Middle-Out (Hybrid) Approach

**Process:**
- Define key interface parts first (top-down)
- Add standard/purchased parts (bottom-up)
- Create detail parts referencing interface parts (hybrid)

**Advantages:**
- Balances control with flexibility
- Critical interfaces coordinated
- Non-critical parts independent

**Best for:**
- Most real-world projects
- Teams with mix of custom and standard parts

## Mates and Constraints

### Common Mate Types

**Coincident:**
```
Aligns two faces or planes flush together

Example: Mounting plate bottom surface coincident with base surface
```

**Concentric:**
```
Aligns two cylindrical or circular features on same axis

Example: Shaft concentric with bearing inner race
```

**Distance:**
```
Maintains specific distance between features

Example: Spacer maintaining 10mm gap between two plates
```

**Parallel:**
```
Keeps two planes or axes parallel (but not coincident)

Example: Top plate parallel to bottom plate in multi-level structure
```

**Perpendicular:**
```
Maintains 90° relationship between features

Example: Vertical post perpendicular to base plate
```

**Angle:**
```
Maintains specific angle between features

Example: Bracket at 45° angle to mounting surface
```

**Tangent:**
```
Maintains tangent relationship between surfaces

Example: Belt tangent to pulleys
```

### Mate Strategy

**Best practices:**

**1. Constrain incrementally:**
```
Each part has 6 degrees of freedom (DOF):
  3 translations (X, Y, Z)
  3 rotations (about X, Y, Z)

Apply mates to remove DOF until fully constrained (0 DOF remaining)
```

**2. Use geometric mates before distance mates:**
```
Good sequence:
  1. Coincident (align primary surfaces)
  2. Concentric (align holes/shafts)
  3. Distance (set specific spacing)

Poor sequence:
  1. Distance, distance, distance → over-constrained, conflicts
```

**3. Avoid redundant mates:**
```
Over-constrained assembly = mate conflicts = unstable model

Example of redundancy:
  - Part already located with 3 mates (fully constrained)
  - Adding 4th mate creates conflict if dimensions don't perfectly match
```

**4. Ground primary component:**
```
"Ground" or "fix" one part as reference (usually base plate, frame)
All other parts mate relative to grounded part or previously constrained parts
```

## Design for Assembly (DFA) Principles

### Minimize Part Count

**Every additional part increases:**
- Design time (CAD modeling, drawings, revisions)
- Manufacturing cost (setup, inspection, handling)
- Inventory complexity (storage, tracking, stock-outs)
- Assembly labor (pick, orient, fasten)
- Potential failure points (joints, fasteners)
- Service difficulty (disassembly, part replacement)

**Real-World Cost Impact:**

**Rule of thumb:** Each additional part adds $3-8 in total cost (design + manufacturing + assembly + inventory).

| Cost Factor | Per Additional Part | 10-Part Assembly | 50-Part Assembly |
|-------------|---------------------|------------------|------------------|
| Design/Documentation | $50-150 (one-time) | $500-1,500 | $2,500-7,500 |
| Manufacturing setup | $2-5/part | $20-50/unit | $100-250/unit |
| Assembly labor | $1-3/part | $10-30/unit | $50-150/unit |
| **Total per unit** | **$3-8** | **$30-80** | **$150-400** |

**Strategies to Reduce Part Count:**

**Example 1: Combine Parts (Motor Bracket)**

**Amateur Design (bolted construction):**
- Base plate: 1 part, $15
- 2× L-brackets: 2 parts, $12 each = $24
- 8× M6 screws: $0.50 each = $4
- Assembly time: 12 minutes @ $30/hr = $6
- **Total: 11 parts, $49 per assembly**

**Professional Design (single bent bracket):**
- One-piece sheet metal bracket (laser cut + brake press)
- Material + cutting: $8
- Bending: $3
- **Total: 1 part, $11 per assembly**

**Savings: $38 per assembly (78% cost reduction) + 10 fewer parts to manage!**

**Example 2: Integral Features (Shaft Assembly)**

**Before (separate components):**
```
- Shaft: ⌀20mm × 150mm, $8
- Collar: ⌀20mm ID × ⌀30mm OD × 10mm, $6
- M6 setscrew: $0.75
- Assembly time: 3 minutes @ $30/hr = $1.50
Total: 3 pieces, $16.25
```

**After (machined shoulder):**
```
- Shaft with machined shoulder: ⌀20mm × 150mm with ⌀30mm × 10mm shoulder
- Material + machining: $12
Total: 1 piece, $12
```

**Savings: $4.25 per assembly (26%) + eliminates setscrew loosening failure mode**

**Example 3: Welded Frame Assembly**

**Bolted Frame (amateur approach):**
- 12 aluminum extrusion pieces: 12 × $8 = $96
- 48 corner brackets: 48 × $2 = $96
- 96 M6 screws: 96 × $0.40 = $38.40
- Assembly time: 2 hours @ $30/hr = $60
- **Total: 156 pieces, $290.40 per frame**

**Welded Frame (professional approach):**
- 12 aluminum extrusion pieces: 12 × $8 = $96
- Welding: 24 joints × $3/joint = $72
- **Total: 12 pieces (1 welded assembly), $168 per frame**

**Savings: $122.40 per frame (42% cost reduction) + eliminates 144 fasteners!**

**Part Count Decision Matrix:**

| Separate Parts? | Integrated Part? | Choose When... |
|-----------------|------------------|----------------|
| ✓ Bolted bracket (easy disassembly) | ✓ Welded/bent bracket (permanent) | Field service required? Bolted. One-time assembly? Integrated. |
| ✓ Shaft + collar (adjustable position) | ✓ Machined shoulder (fixed) | Position needs adjustment? Collar. Fixed position? Shoulder. |
| ✓ Multi-part (different materials) | ✓ Single-part | Need steel shaft in aluminum housing? Separate. Same material? Integrate. |

**When NOT to reduce part count:**
- Serviceability required (must replace worn components)
- Different materials needed (heat resistance, wear resistance)
- Adjustment needed (collars, spacers for position tuning)
- Manufacturing cost of integrated part > sum of separate parts

### Design for Ease of Assembly

**Self-Aligning Features:**
```
Chamfers on shafts and holes:
  - Lead-in for easier insertion
  - 0.5 mm × 45° chamfer typical

Tapered dowel pins:
  - Self-center as they insert
  - Pull parts into alignment
```

**Minimize Orientations:**
```
Assemble all parts from one direction (top-down assembly)
  - Gravity assists
  - Simpler fixturing
  - Faster assembly

Avoid: Assembly requiring flipping part multiple times
```

**Snap-Fits and Captive Hardware:**
```
Snap-fit features:
  - No separate fasteners
  - One-hand assembly
  - Common in plastic parts

Captive screws:
  - Screw stays in part (can't fall out or get lost)
  - Spring or snap ring retains screw
```

**Symmetry:**
```
Symmetric parts can be installed in any orientation
  - Reduces assembly errors
  - Faster assembly (no need to check orientation)

Example: Square plate with symmetric hole pattern
  - Can be rotated 90° and still fits
```

**Keying and Poka-Yoke (Error-Proofing):**
```
Asymmetric features prevent incorrect assembly

Examples:
  - Connector with one pin larger (can only plug in one way)
  - Mounting holes on offset pattern (part only fits one orientation)
  - Chamfer on one corner (visual indicator of correct orientation)
```

### Standardization

**Use common fasteners across assembly:**
```
Good: All M6 socket head cap screws (one tool size, bulk purchase)
Poor: M4, M5, M6, M8 screws mixed (multiple tools, small quantity purchases)
```

**Standard part libraries:**
```
Bearings: Select from standard sizes (6000, 6200, 6300 series)
Belts/pulleys: Standard pitches (GT2, HTD, etc.)
Linear guides: Standard rail sizes (15mm, 20mm, 25mm)
Motors: NEMA standard sizes
```

## Fastener Selection and Design

### Common Fastener Types

**Socket Head Cap Screw (SHCS):**
```
Advantages:
  - High strength
  - Compact head (flush or below surface)
  - Allen key drive (common, reliable)

Applications:
  - Structural connections
  - Where low-profile head needed
```

**Button Head Cap Screw:**
```
Advantages:
  - Lower profile than SHCS
  - Rounded head (aesthetics, safety)

Applications:
  - User-facing surfaces
  - Where very low profile desired
```

**Flat Head Socket Screw:**
```
Advantages:
  - Countersunk (fully flush surface)
  - Clean appearance

Applications:
  - Sliding surfaces
  - Where absolutely flush surface required

Disadvantage:
  - Requires countersink (extra machining operation)
```

**Hex Head Bolt:**
```
Advantages:
  - High torque capacity (larger wrench contact)
  - Inexpensive

Applications:
  - Heavy structural joints
  - High-torque applications

Disadvantage:
  - Large head (requires clearance)
```

**Set Screw:**
```
Advantages:
  - Flush or recessed (no protrusion)
  - Locks components on shafts

Applications:
  - Collars, pulleys on shafts
  - Locating pins

Types:
  - Cup point (most common, mars shaft slightly)
  - Flat point (doesn't mar shaft)
  - Cone point (high friction)
```

### Fastener Sizing and Specification

**Hole clearances:**

| Screw Size | Close Clearance | Normal Clearance | Loose Clearance |
|------------|------------------|------------------|-----------------|
| M3 | 3.2 mm | 3.4 mm | 3.6 mm |
| M4 | 4.3 mm | 4.5 mm | 4.8 mm |
| M5 | 5.3 mm | 5.5 mm | 5.8 mm |
| M6 | 6.4 mm | 6.6 mm | 7.0 mm |
| M8 | 8.4 mm | 9.0 mm | 10.0 mm |
| M10 | 10.5 mm | 11.0 mm | 12.0 mm |

**CAD approach:**
```
Parameters:
  screw_size = "M6"
  clearance_type = "normal"

  If screw_size == "M6" AND clearance_type == "normal":
    hole_diameter = 6.6 mm
```

**Thread engagement:**
```
Minimum thread engagement:

Steel into steel: 1× nominal diameter
  M6 screw → 6 mm min engagement

Aluminum into aluminum: 1.5× nominal diameter
  M6 screw → 9 mm min engagement

Plastic: 2× nominal diameter (or use threaded insert)
  M6 screw → 12 mm engagement OR heat-set insert
```

**Counterbore dimensions:**

| Screw Size | Socket Head Cap Screw | Button Head |
|------------|------------------------|-------------|
| M3 | ⌀6 mm × 3 mm deep | ⌀5.5 mm × 2 mm |
| M4 | ⌀7.5 mm × 4 mm deep | ⌀7 mm × 2.5 mm |
| M5 | ⌀9.5 mm × 5 mm deep | ⌀8.5 mm × 3 mm |
| M6 | ⌀11 mm × 6 mm deep | ⌀10 mm × 3.5 mm |
| M8 | ⌀14 mm × 8 mm deep | ⌀13 mm × 4.5 mm |

**Countersink dimensions (flat head screws):**
```
Countersink angle: 90° or 82° (match screw)
Diameter: Screw head diameter + 0.5 mm clearance

M6 flat head: ⌀12 mm countersink × 82° angle
```

### CAD Modeling of Fasteners

**Simplified representation (recommended):**
```
Model:
  - Clearance hole in parts
  - Cosmetic screw in assembly (simplified cylinder)

Don't model:
  - Threads (complex geometry, slows CAD)
  - Exact head geometry

Benefits:
  - Faster model performance
  - Easier to swap fastener sizes
  - Drawings show simplified holes (easier to dimension)
```

**Fastener libraries:**
```
Most CAD systems include:
  - Standard fastener libraries (ANSI, ISO)
  - Automatic hole creation
  - BOM generation with part numbers

Example: SolidWorks Toolbox, Fusion 360 Insert > McMaster-Carr
```

## Interference Detection

### Checking for Collisions

**Interference check tools in CAD:**
```
Detect overlapping geometry:
  - Parts occupying same physical space
  - Impossible to assemble as designed

Process:
  1. Select all parts in assembly (or specific subset)
  2. Run interference detection
  3. Review report (volume of interference, location)
  4. Fix design (adjust dimensions, clearances)
```

**Clearance check:**
```
Verify minimum spacing between parts:
  - Ensure tool access for fastener installation
  - Provide clearance for thermal expansion
  - Allow for tolerance stack-up

Example:
  Minimum clearance: 2 mm between all non-mating parts
  If clearance < 2 mm → Warning, review design
```

### Dynamic Interference (Motion Studies)

**For assemblies with moving parts:**
```
Simulate motion through full range of travel
Check for:
  - Parts colliding during movement
  - Cable/wire interference
  - Adequate clearance throughout motion

Example: Robot arm
  - Simulate all joint rotations
  - Check arm doesn't collide with base, obstacles
  - Verify end effector workspace
```

## Subassemblies

### When to Create Subassemblies

**Logical grouping:**
```
Subassembly when:
  - Parts assembled together as unit
  - Unit can be tested independently
  - Simplifies top-level assembly
  - Parts always used together

Examples:
  - Motor + mounting bracket + coupling = motor_mount_assembly
  - PCB + standoffs + enclosure = electronics_module
  - Bearing + shaft + spacers = shaft_assembly
```

### Subassembly Structure

**Hierarchical organization:**
```
Top_Level_Assembly
├─ Frame_Subassembly
│  ├─ Base_Plate
│  ├─ Vertical_Posts (4x)
│  └─ Top_Plate
├─ Motion_System_Subassembly
│  ├─ Linear_Rails (2x)
│  ├─ Carriages (2x)
│  └─ Mounting_Blocks (4x)
├─ Drive_System_Subassembly
│  ├─ Motor
│  ├─ Motor_Bracket
│  ├─ Coupling
│  └─ Leadscrew
└─ Hardware
   ├─ M6_SHCS (24x)
   ├─ M6_Washers (24x)
   └─ M6_Nuts (24x)
```

**Benefits:**
- Each subassembly can be assigned to different team member
- Subassemblies can be performance-tested independently
- Simplified BOM structure
- Easier assembly instructions (build subassemblies first, then combine)

## Bill of Materials (BOM)

### BOM Structure

**Indented BOM:**
```
1. Main_Assembly
   1.1 Frame_Subassembly
       1.1.1 Base_Plate (1x)
       1.1.2 Vertical_Post (4x)
       1.1.3 Top_Plate (1x)
       1.1.4 M6×20 SHCS (16x)
   1.2 Motor_Mount_Subassembly
       1.2.1 Motor_Bracket (1x)
       1.2.2 NEMA_23_Motor (1x) [PURCHASED]
       1.2.3 M5×16 SHCS (4x)
   1.3 Hardware_Kit
       1.3.1 M6_Washer (16x)
       1.3.2 M6_Locknut (16x)
```

**Flat BOM (for purchasing):**
```
Part Number | Description | Qty | Source | Unit Cost | Total
------------|-------------|-----|--------|-----------|------
BP-001 | Base Plate | 1 | In-house | $15.00 | $15.00
VP-002 | Vertical Post | 4 | In-house | $8.00 | $32.00
TP-003 | Top Plate | 1 | In-house | $12.00 | $12.00
MB-004 | Motor Bracket | 1 | In-house | $6.00 | $6.00
MOT-NEMA23 | NEMA 23 Stepper | 1 | Vendor A | $45.00 | $45.00
M6x20-SHCS | M6×20 Socket Cap | 16 | McMaster | $0.25 | $4.00
M5x16-SHCS | M5×16 Socket Cap | 4 | McMaster | $0.18 | $0.72
...
TOTAL | | | | | $114.72
```

### BOM Management in CAD

**Automatic BOM generation:**
```
CAD systems can auto-generate BOM from assembly:
  - Part names
  - Quantities (counts instances)
  - Custom properties (material, finish, source)
  - Mass/weight
```

**Custom properties to include:**
```
Part-level properties:
  - Part number (unique ID)
  - Description
  - Material
  - Finish/coating
  - Source (in-house, purchased, vendor name)
  - Unit cost
  - Lead time

Assembly-level:
  - Assembly number
  - Revision
  - Designer
  - Date
```

**BOM export formats:**
```
- Excel (.xlsx) - Most common, easy editing/sharing
- CSV - Universal import to ERP/MRP systems
- PDF - Distribution to suppliers, assembly technicians
```

## Assembly Documentation

### Exploded Views

**Purpose:**
- Show how parts fit together
- Assembly/disassembly instructions
- Service manuals

**Creating exploded views in CAD:**
1. Create new configuration/state ("exploded")
2. Move parts outward along logical assembly paths
3. Add "explosion lines" showing part relationships
4. Render with part balloons (number each part)

### Assembly Instructions

**Step-by-step documentation:**
```
Step 1: Attach vertical posts to base plate
  - Parts: Base plate (1), Vertical posts (4), M6×20 SHCS (16)
  - Tools: 5mm Allen key
  - Torque: 8 Nm
  - Image: Exploded view showing bolt locations

Step 2: Install motor mount subassembly
  - Parts: Motor mount subassembly (preassembled)
  - Parts: M6×25 SHCS (4)
  - Tools: 5mm Allen key
  - Torque: 10 Nm
  - Image: Motor mount positioned on frame
...
```

**CAD-generated assembly instructions:**
- Fusion 360: Animate assembly sequence
- SolidWorks: Composer (dedicated assembly instruction tool)
- Manual: Screenshots of each assembly step

## Practical Example: Linear Actuator Assembly

### Design Requirements

**System:** Linear actuator for CNC application

**Components needed:**
- Frame structure
- Linear guides (2x rails)
- Carriage plate
- Leadscrew and nut
- Motor mount and motor
- Coupling
- Hardware

### Assembly Design Process

**Step 1: Define interfaces (top-down)**
```
Master skeleton sketch:
  - Rail mounting surface (datum A)
  - Rail spacing (200 mm)
  - Carriage travel (300 mm stroke)
  - Motor mounting location
```

**Step 2: Design frame (in-context)**
```
Frame_Base_Plate:
  - References skeleton rail spacing
  - Mounting holes for rails (M5 tapped, 50 mm spacing)
  - Motor mounting face

Frame_End_Plates (2x):
  - Mount to base plate
  - Support leadscrew bearings
```

**Step 3: Add purchased parts (bottom-up)**
```
Insert from libraries:
  - Linear rails (HGH20, 400 mm length)
  - Linear carriages (HGH20CA)
  - Leadscrew (1605, 350 mm)
  - Ballnut (1605)
  - NEMA 23 motor
  - Flexible coupling (8mm to 16mm)
  - Bearings (6004-2RS for leadscrew support)
```

**Step 4: Design custom parts (in-context)**
```
Carriage_Plate:
  - Mounting holes match linear carriage bolt pattern (references carriage)
  - Ballnut pocket (references ballnut dimensions)
  - Payload mounting holes (50×50 mm pattern)

Motor_Mount_Bracket:
  - References motor bolt pattern
  - Positions motor axis concentric with leadscrew
  - Mounts to frame end plate
```

**Step 5: Add hardware**
```
From fastener library:
  - M5×12 SHCS (16x) - Rail mounting
  - M4×12 SHCS (8x) - Carriage mounting
  - M5×20 SHCS (4x) - Motor mounting
  - M6×20 SHCS (8x) - End plate mounting
```

**Step 6: Verify and document**
```
Interference check: Pass (no collisions)
Motion study: Carriage travels full 300 mm stroke, no interference
BOM generated: 45 line items total
Exploded view created
Assembly instructions: 8 steps
```

### DFA Review

**Optimizations applied:**
```
✓ All fasteners: M4, M5, M6 (3 sizes only, 2 hex keys)
✓ Assembly direction: All from top (gravity-assisted)
✓ Subassemblies: Motor + bracket preassembled and tested
✓ Alignment features: Dowel pins locate end plates to base
✓ Standard parts: Rails, bearings, hardware all off-the-shelf
```

## Summary

Effective assembly design requires planning beyond individual part geometry:

**Assembly Modeling:**
- Bottom-up: Independent parts, later assembled (flexible)
- Top-down: Parts designed in assembly context (coordinated interfaces)
- Hybrid: Best of both approaches

**DFA Principles:**
1. Minimize part count (combine, integrate, weld/bond)
2. Design for ease of assembly (self-aligning, one-direction, snap-fits)
3. Standardize fasteners and parts
4. Use keying and poka-yoke (error-proofing)

**Fasteners:**
- Select appropriate types (SHCS, button head, flat head)
- Specify correct clearances and engagement
- Use simplified models in CAD (performance)

**Verification:**
- Interference detection (static)
- Motion studies (dynamic)
- BOM accuracy (purchasing, costing)

**Documentation:**
- Exploded views
- Assembly instructions
- BOM (indented and flat formats)

**Next section** covers how to generate engineering drawings and technical documentation from CAD models.

***

**Next:** [Section 16.9: Documentation and Engineering Drawings](section-16.9-documentation-drawings.md)

**Previous:** [Section 16.7: Process-Specific Design](section-16.7-process-specific-design.md)

---

# Section 16.2: CAD Fundamentals

## Introduction

Think of CAD fundamentals as learning to write before writing novels. You can create complex parts without mastering basics, but they'll be fragile, hard to edit, and difficult for others to understand. This section teaches you the **professional foundations** that separate stable, maintainable CAD models from amateur "spaghetti models" that break when you change a single dimension.

**Why fundamentals matter:**
- **Bad sketch:** Change one dimension → entire model fails → spend 2 hours rebuilding
- **Good sketch:** Change any dimension → model updates cleanly in seconds
- **Impact:** The difference between 5-minute design changes and throwing away your model and starting over

These principles apply to **all CAD software** (FreeCAD, Fusion 360, SolidWorks, Inventor, Onshape). The buttons and menus differ, but the underlying concepts are universal.

## Sketching Best Practices

### The Foundation of Parametric Design

Every 3D feature begins with a 2D sketch. The quality of your sketches directly impacts model stability, editability, and manufacturability.

### Sketch Fully Defined vs. Under-Defined

Understanding constraint status is like the difference between a building on a solid foundation vs. quicksand.

**Fully Defined Sketch (Professional Standard):**
```
Visual indicator: All geometry BLACK (or fully constrained color)
Status: ✓ Fully Defined
What this means:
  - Every line, arc, point has exact position/size defined
  - Nothing can move unless you change a dimension/constraint
  - Editing is predictable (change one thing, others stay fixed)
  - Model won't break when you modify parent features
```

**Under-Defined Sketch (Amateur Warning Sign):**
```
Visual indicator: Geometry BLUE or GREEN (software dependent)
Status: ⚠ Under-Defined
What this means:
  - Some lines/points can move freely
  - Sketch can "shift" unexpectedly during edits
  - Parent feature changes may cause catastrophic shifts
  - Downstream features may fail unpredictably
```

**Real-world example:**

**Amateur approach:**
```
Draws rectangle, adds one dimension (50mm width)
- Rectangle height: undefined (blue)
- Position: undefined (blue)
- Later edits cause rectangle to shift position
- All features built on this sketch break
```

**Professional approach:**
```
Draws rectangle, fully constrains:
1. Width = 50mm (dimension)
2. Height = 30mm (dimension)
3. Bottom-left corner coincident with origin (constraint)
4. Bottom edge horizontal (constraint)

Result: All geometry BLACK, fully defined
Changes are predictable, model never breaks unexpectedly
```

**Rule:** If you see blue/green lines in your sketch, you're not done. Keep adding constraints/dimensions until everything is black (fully defined).

**Exception:** Sketches for design exploration where you deliberately want flexibility—but these should NEVER be used for final manufacturing models.

### Constraint Strategy

**The Golden Rule: Geometry First, Dimensions Second**

Think of constraints as answering two questions:
1. **What shape?** (Geometric constraints: parallel, perpendicular, tangent, etc.)
2. **What size?** (Dimensional constraints: 50mm, ⌀10mm, 45°, etc.)

**Why this order matters:**
- Geometric constraints are "free" (no specific values, just relationships)
- They reduce degrees of freedom quickly
- They make the sketch more robust (changing one dimension doesn't break relationships)
- Dimensions added last only control size, not relationships

**Step-by-Step Constraint Workflow:**

**Phase 1: Draw Rough Geometry**
```
Draw approximate shape (don't worry about exact sizes yet)
- Rectangle for plate
- Circles for holes
- Lines for edges
Everything will be blue/green (under-defined) - this is OK for now
```

**Phase 2: Apply Geometric Constraints (Define Relationships)**

1. **Horizontal/Vertical** - Align features to coordinate axes
   - Example: "Make bottom edge horizontal" → ensures part aligns with machine axes

2. **Coincident** - Connect endpoints, center points
   - Example: "Rectangle corner coincident with origin" → fixes position

3. **Concentric** - Align holes, shafts, arcs
   - Example: "4 holes concentric with construction circle" → bolt pattern

4. **Parallel/Perpendicular** - Define relationships between lines
   - Example: "Side edge perpendicular to bottom edge" → ensures square corners

5. **Tangent** - Smooth transitions between arcs and lines
   - Example: "Fillet tangent to both edges" → smooth blend

6. **Symmetric** - Mirror features about centerlines
   - Example: "Holes symmetric about vertical centerline" → balanced design

7. **Equal** - Make multiple features identical size
   - Example: "All 4 holes equal diameter" → consistency without specifying size yet

**Phase 3: Add Dimensions (Define Sizes)**

8. **Length/Distance** - Size linear features
   - Example: "Plate width = 100mm"

9. **Radius/Diameter** - Size circular features
   - Example: "Holes = ⌀6.6mm" (M6 clearance)

10. **Angles** - Define non-orthogonal relationships
    - Example: "Bracket angle = 45°"

**Real Example: Sketching a Mounting Plate**

```
Starting point: Empty sketch (everything blue/undefined)

Step 1: Draw rough rectangle, 4 circles inside
Status: All blue (under-defined)

Step 2: Geometric constraints
- Bottom edge → HORIZONTAL
- Left edge → VERTICAL
- Bottom-left corner → COINCIDENT with origin
- 4 holes → SYMMETRIC about both centerlines
- 4 holes → EQUAL diameter
Status: Some geometry now black (partially defined)

Step 3: Dimensions
- Rectangle width → 100mm
- Rectangle height → 80mm
- Hole diameter → 6.6mm
- Hole spacing → 75mm × 55mm
Status: ALL BLACK (fully defined)

Result: Robust sketch that won't break during edits
```

**Pro Tip: Use construction geometry**
```
Instead of dimensioning between holes directly:

❌ Bad: Dimension from hole center to hole center (creates dependency chain)

✓ Good: Create construction rectangle, make holes coincident with corners
  - Dimension the construction rectangle
  - Holes automatically update when rectangle changes
  - More robust, easier to modify
```

### Sketch Origin and Axes

**Always reference the sketch origin strategically:**

```
Manufacturing-Friendly Origin Placement:
┌─────────────────────────────┐
│                             │
│    Part symmetry line → ─┬─ │
│                          │  │
│                          │  │
│    Machining datum    → ─┼─ │ ← Origin at intersection
│    (hole center, edge)   │  │    of critical features
│                          │  │
└─────────────────────────────┘
```

**Good origin choices:**
- Part centerline (for symmetric parts)
- Machining datum (primary locating feature)
- Critical mounting hole center
- Corner of stock material (for nesting efficiency)

**Poor origin choices:**
- Random location in middle of sketch
- Corner of part that will be cut off
- Feature that may be removed in design iterations

### Sketch Hygiene

**Do:**
- Use construction lines for reference geometry (shown as dashed lines)
- Break complex shapes into multiple simple features
- Name sketches descriptively ("mounting_plate_profile", "bolt_pattern")
- Keep one sketch per feature when possible
- Use sketch patterns for repeated features

**Don't:**
- Create unnecessarily complex splines when simple arcs will do
- Over-constrain (adding redundant dimensions)
- Leave dangling sketch geometry
- Mix critical and cosmetic features in same sketch
- Create self-intersecting profiles

## Feature-Based Modeling

### Building Blocks of 3D Parts

Think of features as LEGO blocks for CAD—each one adds or removes material in a specific way. Professional CAD models are built from a logical sequence of features, not random geometry.

**Why feature order matters:**
Your CAD software builds the part step-by-step, like following a recipe. Change an early step, and everything after it updates (or breaks if poorly designed). Understanding features helps you create models that are:
- **Editable:** Change dimensions without breaking the model
- **Logical:** Other people can understand your design intent
- **Manufacturable:** Features map directly to machining operations

### Additive Features

**Extrude**
- Most common feature
- Converts 2D sketch into 3D by extending perpendicular to sketch plane
- Manufacturing consideration: Extrude depth = machining depth (longer = more cycle time)

```
Sketch Profile → [Extrude 25mm] → 3D Boss
     □                                ▄▄▄
                                     ████
```

**Revolve**
- Creates axially symmetric parts
- Perfect for turned components
- Manufacturing consideration: Design for lathe or mill-turn operations

```
Sketch Profile → [Revolve 360°] → Turned Part
     ▐▌                              ●●●
                                    ●   ●
                                     ●●●
```

**Loft**
- Blends between multiple profiles
- Good for streamlined shapes
- Manufacturing consideration: Complex lofts may require multi-axis machining

**Sweep**
- Follows a profile along a path
- Useful for tubes, pipes, complex channels
- Manufacturing consideration: Ensure sweep path is accessible to tooling

### Subtractive Features

**Cut Extrude**
- Removes material
- Represents milling, drilling, boring operations
- Manufacturing consideration: Depth-to-diameter ratio matters (deep pockets are slow/risky)

**Revolve Cut**
- Removes material axially
- Represents turning, grooving, boring
- Manufacturing consideration: Ensure tool can reach without interference

**Hole Feature**
- Specialized feature for drilled/tapped holes
- Includes standard sizes (ANSI, ISO)
- Manufacturing consideration: Use standard drill sizes, tap sizes

**Chamfer**
- Beveled edge (45° typical)
- Removes sharp edges
- Manufacturing consideration: Easier to program than fillets, quick to execute

**Fillet**
- Rounded edge
- Strengthens parts, improves appearance
- Manufacturing consideration: Radius must match available tool sizes

### Pattern Features

**Linear Pattern**
- Repeats features in straight lines
- Perfect for bolt patterns, ventilation holes
- Manufacturing consideration: Aligns with axis of motion = faster machining

**Circular Pattern**
- Repeats features around an axis
- Good for bolt circles, gear teeth
- Manufacturing consideration: May require rotary axis or indexing

**Mirror**
- Reflects features across plane
- Ensures perfect symmetry
- Manufacturing consideration: Consider if part can be flipped in fixture

### Feature Order and Parent-Child Relationships

Features build upon each other, creating a dependency tree:

```
Base Extrude (Sketch1)
  ├─ Fillet1
  ├─ Hole1 (Sketch2)
  │   └─ Hole Pattern1
  └─ Cut Extrude (Sketch3)
      └─ Chamfer1
```

**Critical Principle:** Child features depend on parent features. If you delete or modify a parent, children may fail.

**Best Practices:**
- Place critical features early in the tree
- Place cosmetic features (small fillets, chamfers) late
- Group related features together
- Avoid creating complex interdependencies

### Feature Editing and Suppression

**Edit Feature:** Double-click to change parameters
**Suppress Feature:** Temporarily remove without deleting (useful for analyzing base geometry)
**Rollback Bar:** Move backwards in feature tree to edit earlier features

## File Organization and Naming Conventions

### Project Structure

Organize CAD files for team collaboration and long-term maintenance:

```
Project_Name/
├── CAD/
│   ├── Parts/
│   │   ├── Structural/
│   │   ├── Brackets/
│   │   ├── Hardware/
│   │   └── Custom/
│   ├── Assemblies/
│   │   ├── Subassemblies/
│   │   └── Final_Assembly/
│   ├── Drawings/
│   │   ├── Parts/
│   │   └── Assemblies/
│   └── Templates/
├── CAM/
│   ├── Toolpaths/
│   ├── Setup_Sheets/
│   └── Post_Processed/
├── Documentation/
│   ├── BOM/
│   ├── Specifications/
│   └── Change_Orders/
└── Archive/
    └── Previous_Versions/
```

### Naming Conventions

**Part Files:**
```
[Project]-[Assembly]-[Part]-[Revision].[ext]

Examples:
CNC_Table-Frame-Left_Rail-RevB.sldprt
Plasma_Cutter-Torch_Assy-Nozzle_Cap-RevA.step
Robot_Arm-Gripper-Jaw_Left-RevC.FCStd
```

**Assembly Files:**
```
[Project]-[Assembly_Name]-[Revision].[ext]

Examples:
CNC_Table-Frame_Assembly-RevA.sldasm
Waterjet-Cutting_Head_Assy-RevB.step
```

**Drawing Files:**
```
[Project]-[Part/Assy]-Drawing-[Revision].[ext]

Examples:
CNC_Table-Left_Rail-Drawing-RevB.pdf
Plasma_Cutter-Torch_Assy-Drawing-RevA.dwg
```

### Version Control Strategies

**Revision Levels:**
- **RevA:** Initial release for manufacturing
- **RevB, C, D...:** Sequential changes (document changes in ECO)
- **Proto1, Proto2...:** Prototype iterations (not for production)
- **Dev:** Development/experimental (not released)

**Change Documentation:**
Maintain a change log in each file or external ECO (Engineering Change Order):
```
RevA: Initial release
RevB: Increased hole diameter from 8mm to 10mm per ECO-2024-015
RevC: Added lightening pockets per weight reduction study
```

**File Format Selection:**

| Format | Use Case | Editability | Compatibility |
|--------|----------|-------------|---------------|
| .sldprt, .ipt, .FCStd | Native working files | Full | Software-specific |
| .step, .stp | Neutral 3D exchange | None | Universal |
| .iges, .igs | Legacy 3D exchange | None | Universal (older) |
| .dxf | 2D profiles (plasma/laser/waterjet) | Limited | Universal |
| .dwg | Engineering drawings | Full (AutoCAD) | Near-universal |
| .pdf | Drawing distribution | None | Universal |
| .stl | 3D printing, visualization | None | Universal (mesh only) |

**Best Practice:** Maintain native files for editing, export neutral formats (STEP) for sharing with other CAD systems or CAM software.

## Multi-Body Part Design

### When to Use Multi-Body Modeling

Multi-body parts contain multiple solid bodies within a single part file.

**Good Use Cases:**
1. **Weldments:** Design all components in context, then split for fabrication
2. **Cast/Molded Parts:** Model core and cavity in same file
3. **Assembly-Level Features:** Create cuts or holes that affect multiple parts
4. **Process Planning:** Separate features by manufacturing operation

**Example - Welded Frame:**
```
Single Part File: Frame_Weldment.sldprt
  Body1: Base_Plate
  Body2: Vertical_Post_Left
  Body3: Vertical_Post_Right
  Body4: Top_Rail
  [Assembly feature: weld beads modeled as features]
```

**Advantages:**
- All components stay in perfect alignment
- Shared features (holes through multiple parts) maintain consistency
- Can derive individual part files from bodies
- Faster than assembly for simple structures

**Disadvantages:**
- Can become slow with many bodies
- BOM generation more complex
- Some CAM software prefers separate files

### Deriving Parts from Multi-Body

Most CAD systems allow "Save Bodies" or "Derive Part" to extract individual bodies as separate files:

```
Frame_Weldment.sldprt
  ├─ [Save Body] → Base_Plate.sldprt
  ├─ [Save Body] → Vertical_Post_Left.sldprt
  ├─ [Save Body] → Vertical_Post_Right.sldprt
  └─ [Save Body] → Top_Rail.sldprt
```

Derived parts can then be detailed with drawings, programmed in CAM, and manufactured independently while maintaining design intent from master weldment.

## Part vs. Assembly Modeling

### When to Create a Part

**Single-piece parts:**
- Machined from one piece of stock
- Cast or molded as single item
- Sheet metal part (even if bent—single flat pattern)
- 3D printed object (even if complex)

### When to Create an Assembly

**Multiple components that:**
- Are manufactured separately
- Use different materials
- Can move relative to each other
- Need independent documentation
- Are purchased items (fasteners, bearings, motors)

**Subassemblies:**
Group related parts into subassemblies for:
- Logical organization (motor_mount_assy, control_panel_assy)
- Independent testing/qualification
- Outsourced fabrication (vendor builds subassembly)
- Pattern/reuse (multiple identical subassemblies)

## Design Libraries and Standardization

### Creating Reusable Content

**Part Templates:**
- Start new designs with pre-configured units, material, views
- Include company logo, revision blocks
- Set default tolerance standards

**Feature Libraries:**
- Save commonly used features (bolt patterns, mounting brackets, lightening pockets)
- Insert into new designs with drag-and-drop

**Standard Parts Library:**
- Hardware (screws, nuts, washers, pins)
- Commercial components (bearings, motors, linear guides)
- Company-standard brackets, spacers, fixtures

**Naming Standards:**
```
ISO4762_M8x25_Socket_Head_Cap_Screw.step
SKF_6204_Deep_Groove_Ball_Bearing.step
McMaster_92196A111_Washer.step
```

### Benefits of Standardization

1. **Design Speed:** Don't re-model common parts
2. **Manufacturing Efficiency:** Standard parts = bulk purchasing, interchangeability
3. **Reduced Errors:** Proven designs, correct dimensions
4. **Simplified BOM:** Standard part numbers, vendor codes
5. **Training:** New designers learn consistent methods

## Practical Exercise: Design a Mounting Bracket

### Objective
Create a simple L-bracket demonstrating fundamental CAD techniques.

**Requirements:**
- 100mm x 80mm x 3mm plate (vertical)
- 100mm x 60mm x 3mm plate (horizontal)
- Four M6 mounting holes in vertical plate (80mm x 50mm bolt pattern)
- Two M8 mounting holes in horizontal plate (50mm spacing)
- All holes 10mm from edges
- 5mm fillet at inside corner
- 2mm chamfer on all outer edges

### Step-by-Step Process

**1. Create Vertical Plate Sketch (Front Plane)**
- Rectangle: 100mm x 80mm, centered on origin
- Fully constrain with dimensions
- Name sketch: "vertical_plate_profile"

**2. Extrude Vertical Plate**
- Extrude: 3mm thickness
- Direction: towards you (positive)
- Name feature: "vertical_plate"

**3. Create Horizontal Plate Sketch (Top face of vertical plate)**
- Rectangle: 100mm x 60mm
- Constrain bottom edge coincident with top of vertical plate
- Name sketch: "horizontal_plate_profile"

**4. Extrude Horizontal Plate**
- Extrude: 3mm thickness
- Direction: perpendicular to vertical plate
- Merge result with vertical plate body
- Name feature: "horizontal_plate"

**5. Add Inside Fillet**
- Select inside corner edge
- Fillet radius: 5mm
- Name feature: "corner_fillet"

**6. Create M6 Hole Pattern Sketch (On vertical plate face)**
- Rectangle construction lines: 80mm x 50mm, centered
- Four circles at rectangle corners, diameter 6.6mm (M6 clearance)
- Fully constrain
- Name sketch: "m6_bolt_pattern"

**7. Cut Extrude M6 Holes**
- Through all
- Name feature: "m6_mounting_holes"

**8. Create M8 Hole Pattern Sketch (On horizontal plate face)**
- Two circles, 50mm spacing, centered on plate
- Diameter: 8.8mm (M8 clearance)
- Position 10mm from front edge
- Name sketch: "m8_bolt_pattern"

**9. Cut Extrude M8 Holes**
- Through all
- Name feature: "m8_mounting_holes"

**10. Chamfer All Outer Edges**
- Select all outer edges (avoid inside fillet)
- Chamfer: 2mm x 45°
- Name feature: "edge_chamfers"

**11. Assign Material**
- Material: Aluminum 6061-T6 (or Mild Steel)

**12. Save File**
- Filename: Bracket-L_Shape-100x80-RevA.[ext]

### Verification Checklist

- [ ] All sketches fully constrained (no blue lines)
- [ ] All features named descriptively
- [ ] Feature tree organized logically
- [ ] Material assigned
- [ ] File saved with proper naming convention
- [ ] Can edit any dimension and model updates without errors

## Summary

This section covered the foundational skills for robust CAD modeling:

1. **Sketching:** Fully constrained sketches with strategic origin placement
2. **Features:** Proper use of extrudes, cuts, holes, fillets, chamfers, patterns
3. **Organization:** File structures, naming conventions, version control
4. **Multi-body:** When and how to use multiple bodies in single part
5. **Libraries:** Standardization for efficiency and consistency

Master these fundamentals before moving to advanced parametric techniques in the next section.

***

**Next:** [Section 16.3: Parametric Modeling](section-16.3-parametric-modeling.md)

**Previous:** [Section 16.1: Introduction](section-16.1-introduction.md)

---

# Section 16.11: Advanced CAD Techniques

## Introduction

Modern CAD tools offer powerful advanced capabilities that go beyond traditional geometric modeling. These techniques—including FEA simulation, topology optimization, generative design, and surface modeling—enable engineers to create lighter, stronger, more efficient parts while reducing development time. This section introduces advanced CAD methods particularly relevant to CNC manufacturing and design optimization.

## Finite Element Analysis (FEA)

### What is FEA?

**Finite Element Analysis:**
Computational method that divides complex geometry into small elements (mesh) and solves physics equations to predict behavior under loads.

**Common FEA analyses:**
- **Structural (stress/strain):** How part deforms under mechanical loads
- **Thermal:** Temperature distribution, heat transfer
- **Modal:** Natural frequencies, vibration modes
- **Fatigue:** Predicted life under cyclic loading
- **Buckling:** Critical loads causing instability

### FEA Workflow in CAD

**Step 1: Define Material Properties**
```
Select from library or custom:
  - Elastic modulus (stiffness)
  - Poisson's ratio
  - Yield strength
  - Density
  - Thermal conductivity (thermal analysis)

Example: Aluminum 6061-T6
  E = 69 GPa
  ν = 0.33
  σ_yield = 276 MPa
  ρ = 2700 kg/m³
```

**Step 2: Apply Loads and Constraints**
```
Constraints (boundary conditions):
  - Fixed support: No displacement, no rotation
  - Pinned support: No displacement, free rotation
  - Roller support: No displacement perpendicular, free sliding

Loads:
  - Forces (N)
  - Pressures (Pa)
  - Torques (N·m)
  - Gravity
  - Thermal (temperature, heat flux)
```

**Step 3: Create Mesh**
```
Mesh = discretization of geometry into small elements

Mesh quality:
  - Finer mesh → More accurate, slower computation
  - Coarser mesh → Faster, less accurate

Adaptive meshing:
  - Fine mesh near stress concentrations (holes, corners)
  - Coarse mesh in low-gradient regions
```

**Step 4: Solve**
```
CAD FEA solver calculates:
  - Displacement at each node
  - Stress and strain in each element
  - Safety factor (yield strength / max stress)
```

**Step 5: Review Results**
```
Visualization:
  - Stress contour plots (color-coded stress distribution)
  - Displacement plots (exaggerated deformation)
  - Safety factor plots

Check:
  - Maximum stress < Material yield strength?
  - Deflection < Allowable limit?
  - Safety factor ≥ Design target?
```

### Using FEA for Design Optimization

**Iterative design improvement:**

**Example: Bracket weight reduction**

**Iteration 1 (Initial Design):**
```
Solid bracket: 10mm thick
FEA results:
  - Max stress: 50 MPa
  - Safety factor: 5.5 (276 MPa / 50 MPa)
  - Mass: 150 g

Observation: Over-designed (excessive safety factor)
```

**Iteration 2 (Reduce thickness):**
```
Bracket: 6mm thick
FEA results:
  - Max stress: 85 MPa
  - Safety factor: 3.2
  - Mass: 90 g

Result: Still safe, 40% weight reduction
```

**Iteration 3 (Add lightening pockets):**
```
Bracket: 6mm thick + pockets in low-stress regions
FEA results:
  - Max stress: 95 MPa (pockets placed where stress was low)
  - Safety factor: 2.9
  - Mass: 70 g

Result: 53% weight reduction vs. original, still adequate safety factor
```

**Parametric FEA:**
```
Link bracket thickness to parameter:
  bracket_thickness = 6 mm

Run FEA for range:
  4mm, 5mm, 6mm, 7mm, 8mm

Plot: Stress vs. Thickness
Find optimum: Minimum thickness meeting safety factor ≥ 2.0
```

### FEA Best Practices

**Validate with real-world testing:**
- FEA is a prediction, not absolute truth
- Verify critical designs with physical testing
- Calibrate FEA models against test data

**Understand assumptions:**
- Linear elastic analysis (most common): Valid for small deformations, below yield
- Ignores manufacturing defects, residual stresses
- Material properties vary (use conservative values)

**Mesh sensitivity:**
- Run analysis with coarse, medium, fine mesh
- If results converge (similar values), mesh adequate
- If results vary significantly, refine mesh further

**Safety factors:**
- FEA shows theoretical perfect part
- Apply safety factors to account for:
  - Material property variation
  - Manufacturing defects
  - Unknown loads
  - Fatigue (cyclic loading)

## Topology Optimization

### What is Topology Optimization?

**Automated design optimization:**
CAD software removes material from regions experiencing low stress, leaving only load-bearing structure.

**Input:**
- Design space (volume where material allowed)
- Loads and constraints
- Material
- Target mass reduction (e.g., 50% lighter)

**Output:**
- Organic, complex geometry
- Material only where needed for strength
- Often resembles bone structure, tree branches

### Topology Optimization Workflow

**Step 1: Define Design Space**
```
Envelope defining maximum part size:
  - Everything outside this space is void (non-design space)
  - Everything inside is available for material removal

Non-design space:
  - Mounting holes (must remain)
  - Interface surfaces (can't be modified)
  - Load application points
```

**Step 2: Set Objectives and Constraints**
```
Objective:
  - Minimize mass
  - Minimize compliance (stiffness)
  - Minimize stress

Constraints:
  - Mass reduction target (retain 40% of original)
  - Stress limit (< 100 MPa)
  - Deflection limit (< 0.5 mm)

Manufacturing constraints:
  - Minimum wall thickness (2 mm)
  - Extrusion direction (no undercuts)
  - Symmetry (if required)
```

**Step 3: Run Optimization**
```
Software iteratively removes material:
  1. Run FEA
  2. Identify low-stress elements
  3. Remove material from low-stress regions
  4. Re-run FEA
  5. Repeat until target met or stress limits reached
```

**Step 4: Interpret Results**
```
Optimization output:
  - Density plot (0 = void, 1 = solid material, intermediate = transition)
  - Organic, complex shapes
  - Smooth surfaces in commercial tools, faceted in research tools
```

**Step 5: Reconstruct Geometry**
```
Optimization result is mesh/cloud:
  - Not directly manufacturable
  - Must recreate in CAD with clean surfaces

Process:
  1. Smooth the mesh
  2. Extract surface
  3. Rebuild using CAD surfacing tools (NURBS, T-splines)
  4. Add fillets, chamfers, manufacturing features
  5. Validate with FEA (does cleaned-up version still meet requirements?)
```

### Topology Optimization for CNC Manufacturing

**Manufacturing constraints during optimization:**

**Milling constraints:**
```
✓ Specify tool access direction (e.g., top-down only)
✓ Set minimum feature size (based on tool diameter)
✓ Avoid undercuts (or split part for multi-setup)

Result: Machinable topology
```

**Example:**
```
Bracket optimized with "Z-axis tool access only" constraint:
  → All features accessible from top
  → No overhangs requiring 5-axis
  → Can be milled in single setup (3-axis machine)
```

**Additive manufacturing (3D printing) constraints:**
```
✓ Overhang angle limit (45° for FDM)
✓ Minimum wall thickness (2 mm for FDM)
✓ Symmetry (if desired)

Result: 3D-printable organic structures
```

### Hybrid Workflow: Topology Optimization + CNC

**Design process:**
```
1. Topology optimize for minimum mass
   (No manufacturing constraints → absolute optimum)

2. Review result: Complex organic shape
   (Not machinable)

3. Simplify geometry:
   - Interpret key load paths
   - Recreate with manufacturable features (pockets, ribs, webs)
   - Inspired by topology but simplified

4. FEA validate simplified version
   (Close to optimized performance? If not, iterate)

5. Final design: Near-optimal, manufacturable
```

**Example: Motor mount bracket**
```
Topology result: Complex organic web structure (impossible to mill)

Interpreted design:
  - Three main ribs (follow primary load paths from topology)
  - Pockets between ribs (remove material where topology showed void)
  - Standard corner radii (3 mm, millable with 6 mm endmill)

Result:
  - 45% lighter than original solid bracket
  - 90% of theoretical optimum strength
  - Millable in single setup (3-axis)
```

## Generative Design

### Generative Design vs. Topology Optimization

**Generative design:**
- Explores thousands of design alternatives
- User defines requirements (loads, constraints, materials, manufacturing method)
- AI generates multiple solutions
- User selects from gallery of options

**Topology optimization:**
- Single solution for given constraints
- Less exploration, more targeted

**Generative design platforms:**
- Autodesk Fusion 360 (Generative Design workspace)
- nTopology
- Frustum (Generate)

### Generative Design Workflow

**Step 1: Define Problem**
```
Preserve geometry:
  - Mounting interfaces (holes, bosses)
  - Load application points

Obstacle geometry:
  - Regions where material not allowed (clearances)

Loads and constraints:
  - Forces, torques
  - Fixed surfaces, pinned locations
```

**Step 2: Set Manufacturing Method**
```
Select from:
  - Unrestricted (any shape, for 3D printing)
  - 2-Axis milling (features from one direction)
  - 3-Axis milling (features from multiple setups)
  - 5-Axis milling (complex surfaces)
  - Casting (requires draft angles, no undercuts)

Software applies appropriate constraints automatically
```

**Step 3: Set Materials**
```
Allow multiple materials:
  - Aluminum, steel, titanium, composites
  - Software explores designs for each material

Material selection impacts results:
  - Aluminum → Larger sections (lower stiffness)
  - Steel → Smaller sections (higher stiffness)
  - Titanium → Optimized for aerospace (strength + lightweight)
```

**Step 4: Set Objectives**
```
Minimize:
  - Mass
  - Cost
  - Deflection
  - Safety factor (target value)

Maximize:
  - Stiffness
  - Natural frequency

Weight objectives:
  - Mass: 60% importance
  - Cost: 40% importance
```

**Step 5: Generate and Review**
```
Software generates 50-200 design alternatives
  - Sorts by objectives (lightest, stiffest, cheapest)
  - Displays gallery of options
  - Each option shows mass, stress, deflection, cost estimate

User reviews:
  - Compare designs
  - Check aesthetics (some look better than others)
  - Select finalist(s) for detailed FEA validation
```

**Step 6: Refine and Manufacture**
```
Selected design may need cleanup:
  - Add fillets for stress concentration reduction
  - Add chamfers for assembly
  - Adjust dimensions to standard sizes (e.g., round hole to nearest 0.5 mm)

Export for manufacturing:
  - CAM programming (milling, 3D printing)
  - Engineering drawings
```

### Generative Design for CNC

**Example: Robotic arm link**

**Requirements:**
```
Loads: 50 kg payload, 500 mm cantilever
Material: Aluminum 7075-T6
Manufacturing: 3-axis milling
Mass target: < 200 g
Safety factor: ≥ 2.5
```

**Generative design results:**
```
100 designs generated:
  - Lightest: 145 g (complex organic ribs)
  - Cheapest to manufacture: 180 g (simple pockets, faster machining)
  - Best stiffness: 210 g (exceeds mass target, but highest natural frequency)

Selected: 155 g design
  - Meets mass target
  - Manufacturable in 2 setups (flip once)
  - Clean geometry (easy to program in CAM)
```

## Surface Modeling

### When to Use Surface Modeling

**Solid modeling (most CAD):**
- Enclosed volumes
- Boolean operations (union, subtract)
- Good for: Mechanical parts, housings, brackets

**Surface modeling:**
- Open or closed surfaces (no volume)
- NURBS, Bezier, T-splines
- Good for: Complex curves, aesthetic designs, reverse engineering

**CNC applications for surface modeling:**
```
✓ Mold and die design (complex 3D surfaces)
✓ Aerospace (wing surfaces, fairings)
✓ Automotive (body panels, trim)
✓ Consumer products (organic shapes, ergonomic grips)
✓ Artistic/sculptural components
```

### Surface Modeling Tools

**Loft:**
```
Create surface between multiple profile curves
Applications:
  - Airfoil shapes
  - Bottle contours
  - Transitional surfaces
```

**Sweep:**
```
Extrude profile along path curve
Applications:
  - Tubing with varying cross-section
  - Handrails
  - Pipe bends
```

**Boundary surface:**
```
Surface defined by edge curves in U and V directions
Precise control over tangency, curvature
Applications:
  - Class-A surfaces (automotive design)
  - Complex organic shapes
```

**Patch/Fill:**
```
Fill gap between multiple edges
Applications:
  - Closing complex surface models
  - Blending between surfaces
```

### Surface-to-Solid Workflow

**CAD process:**
```
1. Create surfaces (loft, sweep, boundary)
2. Trim surfaces to desired boundaries
3. Knit surfaces together (create watertight skin)
4. Thicken surface → Solid body
   OR
5. Use surface as sculpting reference, model solid separately
```

**CAM from surfaces:**
```
Multi-axis toolpaths:
  - 3+2 axis (indexed positioning)
  - Full 5-axis (simultaneous motion)

Surface finish machining:
  - Ball endmill follows surface
  - Small stepover for smooth finish
  - Often requires HSM (high-speed machining) for efficiency
```

## Multi-Body and Master Model Techniques

### Multi-Body Part Design

**Applications:**

**Weldments:**
```
Single part file, multiple solid bodies:
  - Body1: Base plate
  - Body2: Upright post (left)
  - Body3: Upright post (right)
  - Body4: Cross brace

Benefits:
  - All bodies in perfect alignment (designed in context)
  - Shared features (holes through multiple bodies)
  - Can derive individual part files (for detailing, fabrication)
```

**Machining from complex stock:**
```
Body1: Final part
Body2: Stock shape (casting, forging)

CAM:
  - Import both bodies
  - Use Body2 as stock
  - Toolpaths remove material to create Body1
```

### Master Model (Skeleton) Technique

**Top-down design approach:**

**Master skeleton:**
```
Assembly-level sketch or part containing:
  - Critical interface dimensions (datums, bolt patterns)
  - Motion envelopes
  - Clearance zones
  - Key reference planes

All parts reference this skeleton:
  - Change skeleton → All parts update
  - Ensures consistency across assemblies
```

**Example: Linear actuator master model**
```
Skeleton defines:
  - Rail spacing (200 mm)
  - Stroke length (300 mm)
  - Motor mounting position
  - Leadscrew axis

Parts derived from skeleton:
  - Frame: References rail spacing, stroke length
  - Motor mount: References motor position, leadscrew axis
  - Carriage: References rail spacing, stroke constraints
  - End caps: Reference overall length, bearing positions

Benefit:
  - Change stroke length in skeleton (300→400 mm)
  - All parts automatically resize/reposition
```

## Reverse Engineering and Mesh Processing

### Scanning Physical Parts

**3D scanning technologies:**
- Laser triangulation scanners
- Structured light scanners
- Photogrammetry (camera-based)
- CMM touch probes

**Output: Point cloud or mesh**

### Mesh-to-CAD Workflow

**Step 1: Scan and clean point cloud**
```
Remove noise, outliers
Align multiple scans (if needed)
Decimate (reduce point count for performance)
```

**Step 2: Mesh generation**
```
Create triangulated surface from point cloud
Software: MeshLab, Geomagic, Artec Studio
```

**Step 3: Mesh-to-CAD conversion**

**Approach A: Automatic (for simple geometry)**
```
Software detects features:
  - Planes → Extract flat faces
  - Cylinders → Extract hole axes, diameters
  - Spheres, cones → Extract primitives

Reconstruct solid model from detected features
```

**Approach B: Manual (for complex geometry)**
```
Import mesh as reference
Trace key features in CAD:
  - Sketch critical profiles
  - Extrude, revolve to match mesh
  - Iteratively refine until CAD matches scan

Mesh remains visible as guide, final CAD is clean solid model
```

**Approach C: Direct mesh editing (organic shapes)**
```
Edit mesh directly (subdivision surfaces, T-splines)
Smooth, sculpt, refine
Export as solid (if possible) or surface model
```

### Applications in CNC

**Replacement parts:**
```
Scan original part (no CAD available)
→ Reverse engineer CAD model
→ Program CNC to manufacture duplicate
```

**Mold/die design:**
```
Scan physical prototype (clay model, 3D print)
→ Create CAD surface
→ Design mold cavity around scanned geometry
→ CNC machine mold
```

**Quality inspection:**
```
Scan manufactured part
→ Compare to CAD model (deviation analysis)
→ Identify out-of-tolerance regions
→ Adjust CNC program if systematic errors detected
```

## Summary

Advanced CAD techniques extend beyond basic solid modeling:

**FEA (Finite Element Analysis):**
- Predict stress, deflection, safety factors
- Iteratively optimize designs
- Validate before manufacturing

**Topology Optimization:**
- Automated material removal from low-stress regions
- Lightweight, efficient structures
- Requires reconstruction for CNC manufacturing

**Generative Design:**
- AI explores thousands of design alternatives
- User selects from options (lightest, cheapest, stiffest)
- Specify manufacturing method (milling constraints applied automatically)

**Surface Modeling:**
- Complex organic shapes (molds, dies, aesthetic parts)
- Multi-axis CNC machining
- NURBS, loft, sweep, boundary surfaces

**Multi-Body and Master Models:**
- Weldments, assemblies designed in context
- Top-down design (skeleton drives all parts)
- Ensures consistency across complex assemblies

**Reverse Engineering:**
- 3D scan physical parts
- Mesh-to-CAD conversion
- Manufacture replacement parts, inspect quality

**Integration with CNC:**
- Optimized geometries must be manufacturable
- Apply manufacturing constraints during optimization
- Validate with CAM simulation before production

**Next section** concludes the module with a comprehensive summary and future directions for CAD design in manufacturing.

***

**Next:** [Section 16.12: Conclusion](section-16.12-conclusion.md)

**Previous:** [Section 16.10: CAD-CAM Integration](section-16.10-cad-cam-integration.md)

---

# Section 16.3: Parametric Modeling

## Introduction

**Parametric modeling is like writing a smart program for your part instead of just drawing it.**

Imagine two designers both create a 100mm × 50mm bracket with 4 mounting holes:

**Designer A (Static Model):**
- Hard-codes every dimension
- Change bracket size → manually move every hole, edge, fillet
- Takes 30 minutes to resize
- High chance of errors (forgetting to update something)

**Designer B (Parametric Model):**
- Defines: `bracket_width = 100mm`, holes automatically positioned relative to edges
- Change `bracket_width = 120mm` → entire model updates instantly
- Takes 5 seconds to resize
- Zero errors (relationships enforce design intent)

**This isn't just about speed—it's about:**
- **Design exploration:** Try 10 sizes in 1 minute instead of 5 hours
- **Part families:** One model = many sizes (small/medium/large brackets)
- **Optimization:** Rapidly iterate based on analysis/testing
- **Manufacturing flexibility:** Adjust to available stock sizes instantly

**The secret:** You're not drawing geometry—you're encoding **design logic** that generates geometry.

## Understanding Design Intent

### What is Design Intent?

Design intent is the underlying logic that defines **why** your part is shaped the way it is, not just **what** it looks like.

**Example: Mounting Bracket**

**Poor Design (No Intent):**
```
- Hole1: diameter = 8mm, center at X=25, Y=25
- Hole2: diameter = 8mm, center at X=75, Y=25
```
If you change the bracket width from 100mm to 120mm, the holes stay at X=25 and X=75—no longer properly positioned.

**Good Design (With Intent):**
```
- Hole1: diameter = bolt_size, center at distance = edge_margin from left edge
- Hole2: diameter = bolt_size, center at distance = edge_margin from right edge
- Constraint: holes remain concentric with Y-axis centerline
```
Now changing bracket width automatically repositions holes correctly because the design intent (holes near edges, centered vertically) is encoded.

### Capturing Design Intent

**Ask yourself:**
- What dimensions are fixed (driven by standards, purchased parts)?
- What dimensions are variable (adapt to design changes)?
- What relationships must be maintained (symmetry, alignment, clearances)?
- What features drive other features (primary locating features)?

## Parameters and Variables

**Think of parameters as the "control panel" for your part.**

Instead of hunting through sketches to change a dimension, you adjust one value and the entire model updates.

### Global Parameters

Global parameters (also called "equations" or "variables") define values that can be used throughout your model.

**Real-World Scenario:**

You're designing a custom enclosure. Client says "make it bigger" after you've finished.

**Without Parameters (Pain):**
- Open 8 different sketches
- Change 24 individual dimensions
- Hope you didn't miss any
- Time: 20 minutes
- Risk: High (easy to miss something)

**With Parameters (Easy):**
- Change `enclosure_length = 300 mm` to `enclosure_length = 350 mm`
- Model regenerates automatically
- Time: 10 seconds
- Risk: Zero (relationships enforce consistency)

**Syntax varies by CAD system:**
```
FreeCAD:        bracket_width = 100 mm
SolidWorks:     "bracket_width" = 100
Fusion 360:     bracket_width = 100 mm
Inventor:       bracket_width = 100 mm
```

### Common Parameter Types

**1. Dimensional Parameters (The Foundation)**

These are your basic measurements—the "source of truth" for sizes.

```
plate_length = 200 mm
plate_width = 100 mm
plate_thickness = 3 mm
hole_diameter = 8 mm
edge_margin = 10 mm
```

**When to Use:**
- Primary dimensions that might change
- Values controlled by standards (bolt sizes, stock material)
- Customer-specified dimensions

**2. Derived Parameters (The Smart Ones)**

These calculate automatically based on other parameters.

```
hole_spacing = plate_length - (2 * edge_margin)
plate_area = plate_length * plate_width
bolt_clearance = hole_diameter + 0.5 mm
```

**Real Example - Mounting Plate:**
```
plate_length = 200 mm            ← You control this
edge_margin = 10 mm              ← You control this
hole_spacing = plate_length - (2 * edge_margin)    ← Calculates automatically = 180mm

Change plate_length to 250mm → hole_spacing becomes 230mm (no manual calculation!)
```

**3. Conditional Parameters (The Decision Makers)**

These parameters make decisions based on logic.

```
fillet_radius = if(plate_thickness < 5 mm, 2 mm, 5 mm)
min_wall_thickness = max(3 mm, plate_thickness * 2)
```

**Real Example - Material-Dependent Thread Depth:**
```
# Tapped holes need different depths in different materials
thread_depth = if(material == "Aluminum",
                  bolt_diameter * 1.5,     ← Aluminum: 1.5× diameter
                  bolt_diameter * 1.0)     ← Steel: 1.0× diameter

M8 bolt in aluminum → 12mm thread depth
M8 bolt in steel → 8mm thread depth
(Model automatically adjusts when you change material parameter!)
```

**4. Material-Based Parameters (The Physical Properties)**

```
density_steel = 7850 kg/m³
weight = volume * density_steel
```

**Real Example - Weight Calculation:**
```
# Automatic weight calculation for cost estimation
material = "Aluminum_6061"
density = 2700 kg/m³              ← Aluminum density
volume = (calculated by CAD)      ← CAD automatically computes volume

weight_kg = (volume / 1000000) * (density / 1000)
weight_lbs = weight_kg * 2.205

material_cost_per_kg = 8.50
estimated_material_cost = weight_kg * material_cost_per_kg
```

Change material to steel → density becomes 7850 kg/m³ → weight and cost recalculate instantly!

### Parameter Organization

**Poor Organization (Chaos):**
```
d1 = 200
w = 100
t = 3
h = 8
m = 10
```
**Problem:** What does "d1" mean? What's "m"? Impossible to maintain.

***

**Good Organization (Clear & Maintainable):**
```
# ============================================
# PLATE DIMENSIONS
# ============================================
plate_length = 200 mm
plate_width = 100 mm
plate_thickness = 3 mm

# ============================================
# HOLE PATTERN
# ============================================
hole_diameter = 8 mm          # M8 clearance
hole_count = 4
hole_spacing_x = 150 mm
hole_spacing_y = 75 mm
edge_margin = 10 mm           # Minimum distance from edge

# ============================================
# MANUFACTURING FEATURES
# ============================================
fillet_radius = 5 mm          # Internal corners
chamfer_size = 2 mm           # External edges (deburring)
min_wall_thickness = 3 mm     # Structural minimum

# ============================================
# DERIVED CALCULATIONS (Auto-Update)
# ============================================
actual_hole_spacing_x = plate_length - (2 * edge_margin)
actual_hole_spacing_y = plate_width - (2 * edge_margin)
plate_weight_kg = (plate_length * plate_width * plate_thickness / 1000000) * (density / 1000)
```

**Benefits:**
- ✓ Anyone can understand at a glance
- ✓ Easy to find what you need to change
- ✓ Comments explain context
- ✓ Grouped logically

### Naming Best Practices

| ❌ Bad Name | ✓ Good Name | Why Good is Better |
|------------|-------------|-------------------|
| `dia1` | `mounting_hole_clearance_M8` | Describes purpose, size, and bolt type |
| `L` | `base_plate_length` | Clear which length (base vs cover vs bracket) |
| `offset` | `hole_edge_margin` | Specifies what's being offset |
| `r` | `corner_fillet_radius` | Indicates location and feature type |
| `x` | `motor_bolt_spacing_horizontal` | Describes purpose and direction |

**Pro Tip:** Use names that will make sense to you 6 months from now (or to a coworker who has to edit your model).

## Linking Dimensions to Parameters

**This is where the magic happens—connecting your sketches to the parameter "control panel."**

### Direct Parameter References

Instead of entering numeric values in sketches, reference parameters:

**Before (Hard-Coded):**
```
Rectangle: 200 x 100
```
**Problem:** Change size → must manually edit sketch, find dimension, change value, repeat for every sketch that uses this size.

***

**After (Parametric):**
```
Rectangle: plate_length x plate_width
```
**Benefit:** Change size → change ONE parameter (`plate_length`), ALL sketches using it update automatically!

**Step-by-Step: Converting Hard-Coded to Parametric**

**Scenario:** You've drawn a mounting plate with hard-coded 200mm × 100mm rectangle.

**Step 1: Define Parameter**
```
Open Parameters/Equations panel
Add: plate_length = 200 mm
Add: plate_width = 100 mm
```

**Step 2: Link Sketch Dimension**
```
Double-click the "200" dimension in sketch
Delete "200"
Type: plate_length
Press Enter
```

Dimension now shows "plate_length" instead of "200mm"—it's LINKED!

**Step 3: Test It**
```
Change parameter: plate_length = 250 mm
Watch sketch update automatically to 250mm
```

**Before vs After:**

| Task | Hard-Coded | Parametric |
|------|-----------|-----------|
| Initial setup | 2 minutes | 5 minutes (define parameters) |
| First size change | 10 minutes (edit 6 sketches) | 10 seconds (change 1 parameter) |
| Second size change | 10 minutes | 10 seconds |
| Third size change | 10 minutes | 10 seconds |
| **Total time after 3 changes** | **32 minutes** | **5 min 30 sec** |

**Parametric pays for itself FAST.**

### Equations in Dimensions

Most CAD systems allow equations directly in dimension fields—you don't even need to create a named parameter!

**Real Examples:**

```
Extrude depth: plate_thickness * 2
  ↳ Boss height is always double the plate thickness

Hole position: plate_length / 2
  ↳ Hole stays centered even when plate length changes

Pattern spacing: (plate_length - 2 * edge_margin) / (hole_count - 1)
  ↳ Holes evenly distributed between margins, regardless of plate size
```

**Practical Example - Motor Mount Hole Pattern:**

```
# Parameters defined:
plate_length = 200 mm
edge_margin = 15 mm
hole_count = 4

# In sketch, dimension hole #2 position from hole #1:
Horizontal distance = (plate_length - 2 * edge_margin) / (hole_count - 1)
                    = (200 - 30) / 3
                    = 56.67 mm

# Change plate to 300mm:
New spacing = (300 - 30) / 3 = 90 mm
(All 4 holes redistribute automatically!)
```

**Pro Tip:** Use equations for **derived** values, named parameters for **primary** values you change often.

### Master Sketch Technique

**This is the "foundation blueprint" approach—one sketch controls everything.**

A master sketch contains critical parameters and reference geometry that drives multiple features.

**Why Use Master Sketches?**
- **Single source of truth** for complex geometry (bolt patterns, mounting interfaces)
- **Change once, update everywhere**
- **Prevents dimension drift** (when multiple features slowly get out of sync)

**Example: Bolt Pattern Master Sketch**

**Scenario:** Designing adapter plate for a motor with 4-hole mounting pattern.

**Master_Sketch (on reference plane):**
```
Construction rectangle: mounting_width x mounting_height
  ↳ Represents motor flange outline

Four construction points at rectangle corners
  ↳ Exact bolt hole locations

Construction circle: bolt_circle_diameter
  ↳ Reference for circular bolt pattern (if needed)

Reference dimensions ALL parametric:
  - mounting_width = 80 mm
  - mounting_height = 80 mm
  - bolt_circle_diameter = 113 mm
```

**Features driven by master sketch:**
```
Feature 1: Hole Pattern
  - Projects from 4 construction points in master sketch
  - Diameter = mounting_hole_clearance

Feature 2: Mounting Boss
  - Extrudes around bolt_circle from master sketch
  - Adds material for structural support

Feature 3: Clearance Pocket
  - Offsets from construction rectangle in master sketch
  - Creates recess for motor flange

Feature 4: Alignment Pin Holes
  - References midpoints of construction rectangle sides
```

**The Payoff:**

Motor manufacturer updates bolt pattern from 80mm × 80mm to 90mm × 90mm:

**Without Master Sketch:**
- Edit 4 hole positions individually
- Adjust boss diameter manually
- Recalculate clearance pocket
- Reposition alignment pins
- Time: 30+ minutes
- Risk: Holes misaligned, parts don't fit

**With Master Sketch:**
- Change: `mounting_width = 90 mm`, `mounting_height = 90 mm`
- ALL features update in perfect alignment
- Time: 10 seconds
- Risk: Zero

**Master Sketch Best Practice:**

✓ **Use construction geometry** (doesn't create physical features, just references)
✓ **Keep it simple** (only critical layout geometry)
✓ **Fully constrain** (black sketch—no uncertainty)
✓ **Name clearly** ("Motor_Interface_Master" not "Sketch017")

❌ **Don't overload** with unrelated geometry
❌ **Don't use for non-critical features** (cosmetic details don't need master sketch)

## Design Tables and Configurations

### Creating Part Families

Design tables (also called "configurations" or "family tables") allow one model to represent multiple size variations.

**Example: Standard Bracket Sizes**

| Configuration | plate_length | plate_width | plate_thickness | hole_diameter |
|---------------|--------------|-------------|-----------------|---------------|
| Small         | 100 mm       | 80 mm       | 3 mm            | 6 mm          |
| Medium        | 150 mm       | 120 mm      | 5 mm            | 8 mm          |
| Large         | 200 mm       | 160 mm      | 6 mm            | 10 mm         |
| XLarge        | 250 mm       | 200 mm      | 8 mm            | 12 mm         |

**Single CAD file contains all four variants**—select configuration when inserting into assembly or generating drawings.

### Configuration-Specific Features

Suppress or enable features based on configuration:

```
Configuration: Light_Duty
  - Lightening_Pockets: SUPPRESSED
  - Reinforcement_Ribs: SUPPRESSED

Configuration: Heavy_Duty
  - Lightening_Pockets: SUPPRESSED
  - Reinforcement_Ribs: ACTIVE

Configuration: Weight_Optimized
  - Lightening_Pockets: ACTIVE
  - Reinforcement_Ribs: SUPPRESSED
```

### Bill of Materials Impact

Configurations affect BOM generation:
- Each configuration can have unique part number
- Shared configurations reduce inventory (one drawing, multiple sizes)
- CAM programs can reference specific configuration

## Relationships and Constraints

### Geometric Relationships

**Symmetry:**
```
Feature1 and Feature2: Symmetric about vertical centerline
```
Ensures balanced design, simplifies machining (can use part centerline as datum).

**Concentric:**
```
Hole_Center and Boss_Center: Concentric
```
Maintains alignment through design changes.

**Tangent:**
```
Fillet and Adjacent_Surfaces: Tangent
```
Ensures smooth transitions, critical for flow paths, stress distribution.

**Parallel/Perpendicular:**
```
Mounting_Face and Reference_Datum: Perpendicular
```
Captures manufacturing setup requirements.

### Algebraic Relationships

**Ratios:**
```
hole_diameter = shaft_diameter * 1.05    # 5% clearance
wall_thickness = hole_diameter * 1.5      # Strength requirement
```

**Summations:**
```
total_length = section1_length + section2_length + section3_length
```

**Conditionals:**
```
thread_depth = if(material == "Aluminum", nominal_diameter * 1.5, nominal_diameter * 1.0)
```

### Inter-Part Relationships (Top-Down Design)

In assemblies, parts can reference each other:

```
Assembly: Motor_Mount
  Part: Base_Plate
    mounting_hole_spacing = Motor.bolt_pattern_spacing
    base_width = Motor.flange_width + 2 * clearance

  Part: Cover_Plate
    cover_width = Base_Plate.base_width    # Matches base plate
    cover_length = Base_Plate.base_length
```

**Caution:** Excessive inter-part references can make assemblies fragile. Use sparingly for truly dependent features.

## Advanced Parametric Techniques

### Suppression Equations

Automatically suppress/unsupppress features based on parameters:

```
Suppression equation for Lightening_Pockets:
  plate_thickness > 5 mm AND weight_optimization == TRUE
```

Feature appears only when both conditions met.

### Derived Patterns

Pattern count or spacing driven by overall dimensions:

```
Rib_Count = floor(plate_length / rib_spacing)
```

As plate gets longer, rib count automatically increases to maintain spacing.

### Linked External Files

Reference external parameter files (Excel, CSV, text):

**parameters.csv:**
```
parameter,value,unit
plate_length,200,mm
plate_width,100,mm
bolt_size,M8,
```

CAD model imports parameters from file. Entire product line updates when file changes.

**Use case:** Customer-specific variants, automated design generation.

### Parametric Curves and Splines

Define curves mathematically:

```
Spiral cam profile:
  radius(θ) = base_radius + (pitch * θ / 360°)
  x = radius * cos(θ)
  y = radius * sin(θ)
```

**Applications:** Cam profiles, turbine blades, custom spring geometry.

## Practical Parametric Design: Configurable Motor Mount

### Design Requirements

Create a parametric motor mount that adapts to different NEMA stepper motor sizes:
- NEMA 17: 42mm body, M3 mounting holes, 31mm bolt spacing
- NEMA 23: 56mm body, M5 mounting holes, 47.14mm bolt spacing
- NEMA 34: 86mm body, M6 mounting holes, 69.6mm bolt spacing

Additional requirements:
- Base plate extends 15mm beyond motor body on all sides
- Mounting holes for base plate: 10mm from corners
- Central shaft clearance hole: motor shaft diameter + 2mm
- Plate thickness: 6mm for NEMA 17/23, 8mm for NEMA 34

### Parameter Definition

```
# Motor Parameters (Configuration-Specific)
motor_body_size = 42 mm           # NEMA 17
motor_bolt_spacing = 31 mm
motor_mounting_hole = 3.3 mm      # M3 clearance
motor_shaft_diameter = 5 mm

# Derived Parameters
base_plate_size = motor_body_size + 2 * 15 mm
base_hole_edge_distance = 10 mm
shaft_clearance_diameter = motor_shaft_diameter + 2 mm

# Conditional Parameter
plate_thickness = if(motor_body_size > 60 mm, 8 mm, 6 mm)
```

### Modeling Steps

**1. Create Configuration Table**

| Config   | motor_body_size | motor_bolt_spacing | motor_mounting_hole | motor_shaft_diameter |
|----------|-----------------|--------------------|--------------------|----------------------|
| NEMA_17  | 42              | 31                 | 3.3                | 5                    |
| NEMA_23  | 56              | 47.14              | 5.3                | 6.35                 |
| NEMA_34  | 86              | 69.6               | 6.6                | 14                   |

**2. Base Plate Sketch**
```
Square: base_plate_size x base_plate_size
Centered on origin
```

**3. Extrude Base Plate**
```
Depth: plate_thickness
```

**4. Motor Mounting Hole Pattern Sketch**
```
Construction square: motor_bolt_spacing x motor_bolt_spacing
Centered on origin
Four circles at square corners
Diameter: motor_mounting_hole
```

**5. Central Shaft Clearance**
```
Circle: diameter = shaft_clearance_diameter
Centered on origin
```

**6. Base Mounting Holes**
```
Construction square:
  (base_plate_size - 2 * base_hole_edge_distance) x
  (base_plate_size - 2 * base_hole_edge_distance)
Four circles at corners
Diameter: 6.6 mm (M6 clearance for base mounting)
```

**7. Cut Holes**
```
Through all
```

**8. Chamfer Edges**
```
All outer edges: 2mm x 45°
```

### Testing Configurations

Switch between NEMA_17, NEMA_23, NEMA_34 configurations:
- All holes reposition correctly
- Base plate resizes appropriately
- Thickness changes for NEMA_34
- All clearances maintained

### Manufacturing Benefits

- **One CAD file** = Three product variants
- **One drawing** (with configuration table) = Simplified documentation
- **CAM program** can reference configurations = Automated toolpath generation
- **Design changes** propagate to all sizes = Reduced engineering time

## Design for Change: Building Robust Parametric Models

### Anticipating Modifications

**Ask during initial design:**
- Which dimensions might change based on customer requirements?
- What features might be added or removed later?
- How might manufacturing process change affect design?

**Build flexibility early:**
```
# Instead of hard-coding:
hole_depth = 20 mm

# Use ratio that adapts:
hole_depth = plate_thickness * 3
```

### Preventing Over-Constraint

**Symptoms of over-constraint:**
- Cannot change dimensions without errors
- Features constantly failing
- Sketch becomes over-defined

**Solutions:**
- Use construction geometry for reference, not multiple dimensions
- Let parameters drive multiple features instead of independent dimensions
- Leverage symmetry constraints instead of individual dimensions

### Parent-Child Management

**Minimize dependencies:**
- Critical features first (locating features, primary datums)
- Independent features when possible
- Group related features
- Cosmetic features last (fillets, chamfers)

**Reorder features** if child features fail when editing parent.

## Parametric Modeling for Different Manufacturing Processes

### Sheet Metal (Plasma/Laser/Waterjet)

**Key Parameters:**
```
material_thickness = 3 mm
kerf_width = 0.5 mm              # Process-dependent
min_feature_size = kerf_width * 3
bend_radius = material_thickness * 1.5    # For bending operations
hole_to_edge = material_thickness * 2     # Minimum distance
```

**Flat pattern parameters:**
```
bend_allowance = (π/2) * (bend_radius + k_factor * material_thickness)
developed_length = flat1_length + flat2_length + bend_allowance
```

### Milling

**Key Parameters:**
```
smallest_tool_diameter = 3 mm
min_internal_radius = smallest_tool_diameter / 2
pocket_depth_max = smallest_tool_diameter * 3    # Depth-to-diameter ratio
wall_thickness_min = material_thickness / 3
```

**Feature constraints:**
```
fillet_radius >= min_internal_radius
pocket_depth <= pocket_depth_max
```

### Turning

**Key Parameters:**
```
bar_stock_diameter = 25 mm
max_part_diameter = bar_stock_diameter - 1 mm    # Stock allowance
min_wall_thickness = 2 mm
thread_depth = thread_nominal_diameter * 1.5     # Aluminum
groove_width = tool_width + 0.2 mm               # Tool clearance
```

### 3D Printing (FDM)

**Key Parameters:**
```
nozzle_diameter = 0.4 mm
layer_height = 0.2 mm
min_wall_thickness = nozzle_diameter * 2
max_overhang_angle = 45°                         # Without support
bridge_max_span = 10 mm
hole_compensation = -0.2 mm                      # Holes print small
```

**Feature validation:**
```
if wall_thickness < min_wall_thickness:
    warning("Wall too thin for reliable printing")
```

## Summary

Parametric modeling transforms CAD from static geometry into intelligent, adaptable designs:

1. **Capture Design Intent:** Encode the "why" behind your geometry
2. **Use Parameters:** Global variables drive dimensions throughout the model
3. **Create Relationships:** Geometric and algebraic constraints maintain design logic
4. **Build Configurations:** One model, multiple variants
5. **Design for Change:** Anticipate modifications, build flexibility early
6. **Process-Specific Parameters:** Tailor parametric approach to manufacturing method

**Next level:** Apply these parametric techniques while implementing DFM principles in Section 16.4.

***

**Next:** [Section 16.4: Design for Manufacturability Principles](section-16.4-dfm-principles.md)

**Previous:** [Section 16.2: CAD Fundamentals](section-16.2-cad-fundamentals.md)

---

# Section 16.4: Design for Manufacturability (DFM) Principles

## Introduction

Design for Manufacturability (DFM) is the practice of designing parts to be easy, economical, and reliable to manufacture. Good DFM doesn't mean sacrificing performance—it means achieving required performance through the most efficient manufacturing methods. Every design decision has a manufacturing cost: complex geometry requires more machine time, tight tolerances demand precision tooling, and custom features necessitate specialized equipment.

This section establishes universal DFM principles applicable across all CNC processes, with process-specific details covered in Section 16.7.

## The DFM Mindset

**DFM is about asking "how will this be made?" WHILE you design, not after.**

The best DFM engineers mentally simulate the manufacturing process as they add features. They see the cutting tool, the fixturing, the measurement tools—not just the finished geometry.

### Think Like a Machinist

Before finalizing any design, run through these questions:

**1. How will this be made?**

Let's see how this thinking transforms a simple design decision:

**Scenario:** Adding a 20mm deep pocket to a part.

**Amateur Designer:**
- Draws 20mm deep pocket
- Moves on to next feature

**DFM-Aware Designer:**
- "20mm deep pocket... what tool diameter can I use?"
- "If I use 6mm endmill, depth-to-diameter ratio = 20/6 = 3.3× (acceptable)"
- "But 10mm endmill would be more rigid (ratio = 2×), cut faster"
- "Can I widen the pocket to 15mm minimum to allow 10mm tool? Let me check if function allows..."
- [Checks loads, clearances]
- "Yes, can widen to 16mm. Now I can use 10mm tool = faster cutting, better finish, lower cost"

**Time spent thinking: 2 minutes. Cost savings: 30% faster machining.**

***

**2. What can go wrong?**

**Real Example - Thin-Wall Part:**

Designer creates a part with 1.5mm walls in aluminum.

**Questions to ask:**
- "Will thin walls deflect under cutting forces?"
  - YES → Poor dimensional accuracy, surface finish
- "Can walls be thicker?"
  - Check loads: 2.5mm walls provide same strength with safety margin
- "If walls must be thin, what's the mitigation?"
  - Leave extra stock (3mm walls), machine to final 1.5mm in light finishing pass
  - Add temporary support structures (tabs), remove after machining

**Result:** Part actually works, instead of scrapping 10 pieces before figuring out the problem.

***

**3. How can this be simplified?**

**Real Example - Cable Management Bracket:**

**Initial Design:**
- Curved mounting surface (matches curved enclosure perfectly)
- Custom radius: 127mm (exact radius of enclosure)
- Requires 3D ball-endmill surfacing = 45 minutes machine time

**Simplified Design:**
- Flat mounting surface with 3 contact points (edge + 2 bosses)
- Only bosses match curve (small features = fast to machine)
- Contact area 90% same, stress distribution identical (FEA verified)
- Machining time: 8 minutes

**Key insight:** Perfect form-fit isn't always required. Three points define a plane—often enough for mounting.

### The Cost Hierarchy of Manufacturing Features

**Understanding this hierarchy is the SECRET to low-cost design.**

Every feature you add falls somewhere on this cost ladder. DFM is about climbing DOWN the ladder whenever possible.

**From cheapest to most expensive:**

**1. No feature at all (Cost: $0)**
   - Best feature is one you design out entirely
   - **Example:** "Do we really need that lightening pocket? Part is only 50g, weight isn't critical here."
   - **Savings:** If you don't make it, it costs nothing

**2. Standard feature with standard tooling (Cost: 1× baseline)**
   - Drilled hole with standard drill bit
   - Chamfer with standard 45° chamfer mill
   - Square pocket with standard endmill
   - **Example:** ⌀8mm drilled hole (standard 8mm drill bit)
   - **Cost:** Fast, cheap, every shop has these tools

**3. Standard feature with custom size (Cost: 1.5-2×)**
   - Reamed hole to precise diameter (drill, then ream)
   - Tapped hole (drill, tap)
   - **Example:** ⌀8mm hole reamed to ⌀8.00 H7 (precision fit)
   - **Cost:** Extra operation (reaming after drilling), but still standard tools

**4. Custom feature with standard tooling (Cost: 2-3×)**
   - Complex organic pocket (requires long toolpath, multiple passes)
   - Non-standard geometry requiring many tool changes
   - **Example:** Curved pocket with varying depth (sculptured surface)
   - **Cost:** Standard endmill, but LONG cycle time (complex programming, many passes)

**5. Custom feature requiring specialized tooling (Cost: 4-6×)**
   - T-slot (requires T-slot cutter)
   - Dovetail (requires dovetail cutter)
   - Woodruff key seat (requires Woodruff cutter)
   - **Example:** T-slot for workholding clamps
   - **Cost:** Special tool purchase ($50-200), tool setup, limited cutting speeds

**6. Feature requiring multi-axis machining (Cost: 5-10×)**
   - Compound angle holes (3+2 or 5-axis)
   - Complex sculptured surfaces (5-axis continuous)
   - **Example:** Angled hole through curved surface
   - **Cost:** Requires 5-axis machine ($500k+ vs $50k for 3-axis), specialized programming, longer setup

**7. Feature requiring secondary operations (Cost: 3-8×)**
   - Hand deburring (every edge = labor time)
   - Manual polishing
   - Assembly of sub-components
   - **Example:** Mirror-polished surface (machine, then hand-polish for hours)
   - **Cost:** Labor-intensive, non-automated, inconsistent results

**8. Feature requiring outside processing (Cost: 10-20×)**
   - EDM (electrical discharge machining for sharp corners, hard materials)
   - Heat treatment (hardening, stress relief)
   - Special coatings (anodizing, electroplating)
   - **Example:** Sharp internal corner (requires EDM)
   - **Cost:** Ship to vendor, wait in queue, ship back, quality issues = expensive, slow

***

**Real-World Example: Feature Cost Comparison**

Let's design a mounting bracket with 4 holes. Watch how hole spec affects cost:

| Feature Specification | Cost Category | Machining Operation | Time per Part | Cost per Part |
|----------------------|---------------|-------------------|---------------|---------------|
| ⌀8.5mm drilled holes (clearance) | Category 2 | Drill 4 holes | 2 minutes | $5 (baseline) |
| ⌀8.0mm reamed holes (precision) | Category 3 | Drill ⌀7.8 + ream ⌀8.0 | 6 minutes | $12 |
| ⌀8.0mm holes, positioned ±0.01mm | Category 6 | Drill + ream on CNC mill with precision fixturing | 15 minutes | $35 |
| ⌀8.0mm holes, mirror finish inside | Category 7 | Drill + ream + hand-hone each hole | 45 minutes | $95 |

**Same bracket, different hole specs: $5 vs $95 per part (19× cost difference!)**

**Question to ask:** "Does our application really need precision-positioned, mirror-finished holes? Or will clearance holes work?"

**Answer 90% of the time:** Clearance holes work fine.

**DFM Goal:** Keep features in categories 1-3 whenever possible. Categories 4-8 should require written justification (performance data, analysis, or customer spec).

## Universal DFM Principles

### 1. Minimize Part Count

**Every part adds cost:**
- Design time
- Drawing creation
- BOM line item
- Inventory management
- Quality inspection
- Assembly labor
- Potential failure point

**Strategies:**
- Combine multiple parts into single machined piece when practical
- Use common parts across product line
- Eliminate purely cosmetic components
- Consider multi-body design (weldment instead of bolted assembly)

**Example:**
```
Before DFM: Sensor bracket assembly
  - Mounting plate (milled)
  - Vertical riser (milled)
  - Angle bracket (purchased)
  - 6x M4 screws
  - 6x M4 nuts
  Total: 14 parts

After DFM: Single bent sheet metal bracket
  - One part (laser cut + bent)
  Total: 1 part
```

**Result:** 93% reduction in part count, eliminated machining, reduced assembly time.

### 2. Design for Standard Tooling

**Standard tools are:**
- Readily available
- Inexpensive
- Well-documented (feeds, speeds, tool life)
- Stocked by most machine shops

**Common standard tools:**

| Feature | Standard Tool | Sizes |
|---------|---------------|-------|
| Holes | Twist drills | Fractional, metric, number, letter |
| Counterbores | Counterbore tools | Match socket head cap screw sizes |
| Countersinks | 82° or 90° countersinks | Various diameters |
| Threads | Taps (manual/CNC) | Standard thread pitches |
| Pockets | Square endmills | 1/16" to 1" (metric equivalents) |
| Fillets | Ball endmills, radius endmills | Standard radii (1/16", 1/8", 1/4", etc.) |
| Chamfers | Chamfer mills | 45°, 60°, 82°, 90° |

**DFM Rules:**
- **Internal corners:** Radius ≥ smallest available endmill radius (typically 1.5mm / 1/16")
- **Holes:** Use standard drill sizes; avoid fractional millimeters (6.5mm okay, 6.3mm less common)
- **Threads:** Use standard pitches (M6×1.0, not M6×0.9)
- **Fillets:** Use tool radii (3mm, 6mm, 10mm) rather than arbitrary values (3.7mm)

**Poor DFM Example:**
```
Internal pocket with 0.5mm corner radii
→ Requires custom 1mm endmill
→ Tool fragile, expensive, slow cutting
→ High tool wear, frequent breakage
```

**Good DFM Example:**
```
Internal pocket with 1.5mm corner radii
→ Uses standard 3mm endmill
→ Robust tool, fast cutting, long life
→ Low cost, reliable process
```

### 3. Minimize Setups and Operations

**Every time you flip, rotate, or reposition a part, you pay for it.**

Each setup introduces:
- **Setup time:** 10-30 minutes to fixture, probe, indicate part (even if cutting takes 2 minutes!)
- **Datum shift errors:** Every repositioning = new reference, new chance for error
- **Potential misalignment:** Multi-setup tolerances stack up (±0.05mm per setup)
- **Labor cost:** Machinist must manually load, indicate, verify each setup

**Real Cost Example:**

Part requires 3 setups:
- Setup 1: 20 min setup + 5 min machining
- Setup 2: 20 min setup + 3 min machining
- Setup 3: 15 min setup + 2 min machining
- **Total: 55 min setup + 10 min cutting = 65 min total**

Same part redesigned for 1 setup:
- Setup 1: 20 min setup + 12 min machining
- **Total: 32 min**

**Cost savings: 51% reduction in cycle time, just from reducing setups!**

***

**Single-Setup Design Features:**

**✓ All critical features accessible from one direction**
```
Example: Motor mount plate
- All mounting holes drilled from top
- All pockets machined from top
- Bottom surface left as-sawn (doesn't need machining)
Result: 1 setup, part held in vise, done in 15 minutes
```

**✓ Symmetric parts (can flip and maintain datums)**
```
Example: Adapter plate (identical top/bottom)
- Machine top features in Setup 1
- Flip using same fixture, bottom features identical
- No re-indicating needed (symmetric datums)
Result: 2 setups, but second setup takes 2 minutes (fast flip)
```

**✓ Features designed for standard vise/fixture holding**
```
✓ Flat parallel surfaces for vise jaws
✓ Through-holes for fixture pins (repeatable location)
✓ Edges accessible (vise doesn't block tool)

❌ Curved gripping surfaces (custom soft jaws required)
❌ Features on all 6 sides (requires tombstone fixture)
❌ Undercuts that block standard clamping
```

***

**Multi-Setup Considerations (When Unavoidable):**

**Provide locating features for repeatable second-setup alignment:**

**Poor approach:**
```
Setup 1: Machine top features
Setup 2: Flip part, eyeball alignment, clamp, hope for the best
Result: ±0.5mm misalignment between setups
```

**Professional approach:**
```
Setup 1: Machine top features + two precision dowel pin holes
Setup 2: Flip part onto fixture with matching dowel pins
Result: ±0.01mm repeatable alignment between setups
```

**Real Example - Two-Sided Bracket:**

**Design includes:**
- Two ⌀6mm holes on top (Setup 1)
- Precision pocket on bottom (Setup 2)

**How to ensure alignment:**
1. **Setup 1 operations:**
   - Mill top surface (datum A)
   - Drill two ⌀6mm holes with ±0.02mm position tolerance
   - These become alignment features for Setup 2

2. **Setup 2 operations:**
   - Flip part onto fixture with ⌀6mm alignment pins (matching hole pattern)
   - Part now located precisely relative to Setup 1 datums
   - Machine bottom pocket with guaranteed alignment to top holes

**Key principle:** First setup creates precision features that locate second setup.

***

**Example: Milled Block**

**Poor DFM (3 setups = 65 minutes):**
```
Setup 1: Mount in vise (jaws on sides)
  - Top face milling (5 min)
  - Top holes drilled (3 min)
  - Setup time: 20 min

Setup 2: Flip part upside down
  - Bottom face milling (4 min)
  - Bottom holes drilled (2 min)
  - Setup time: 20 min

Setup 3: Stand part on end (90° rotation, custom fixture)
  - Side pockets machined (2 min)
  - Setup time: 15 min

Total: 55 min setup + 16 min cutting = 71 min
Cost at $60/hr shop rate = $71
```

**Good DFM (1 setup = 30 minutes):**
```
Setup 1: Mount in vise (jaws on finished ends)
  - Top face milling (5 min)
  - All holes drilled from top (4 min)
  - Side pockets machined with extended-length endmill (3 min)
  - Bottom face left as-sawn (adequate surface finish)
  - Setup time: 20 min

Total: 20 min setup + 12 min cutting = 32 min
Cost at $60/hr shop rate = $32

Savings: $39 per part (55% cost reduction!)
```

**Design changes that enabled 1-setup:**
- Bottom surface spec changed to "as-sawn" (function allows this)
- Side pocket depth reduced from 25mm to 18mm (allows standard-length tool to reach from top)
- Bottom holes eliminated (redesigned to use through-holes from top with nuts on bottom)

**Key insight:** Small design changes (that don't affect function) = massive manufacturing savings.

### 4. Design for Material Removal Efficiency

**Material removal rate (MRR) drives cycle time:**
```
MRR = Width of Cut × Depth of Cut × Feed Rate
```

**DFM strategies to maximize MRR:**

**Large Pockets:**
- Allow large diameter roughing tools
- Minimize depth (deep pockets require slow, multiple passes)
- Avoid thin floors (can flex, require light cuts)

**Holes:**
- Use drilling instead of milling when possible (faster)
- Through holes faster than blind holes (no dwell, easier chip evacuation)
- Larger holes can use circle milling if no standard drill available

**Thin Walls:**
- Avoid when possible (slow cutting to prevent deflection)
- If required, provide temporary support structures (design to be removed in secondary op)

### 5. Tolerance Only What Matters

**Tolerances cost money:**

| Tolerance Range | Relative Cost | Typical Process |
|-----------------|---------------|-----------------|
| ±0.5 mm | 1× (baseline) | Sawing, plasma cutting |
| ±0.1 mm | 1.5× | Standard milling, turning |
| ±0.05 mm | 2× | Careful milling, ground surfaces |
| ±0.01 mm | 4× | Precision grinding, wire EDM |
| ±0.005 mm | 8× | Cylindrical grinding, lapping |
| ±0.001 mm | 16× | Ultra-precision machining |

**DFM approach:**
- **Identify critical dimensions:** What affects fit, function, safety?
- **Apply appropriate tolerance:** Match process capability to requirement
- **Leave non-critical dimensions as standard tolerance:** Reduces cost, simplifies inspection

**Example: Motor mount plate**
```
Critical dimensions (tight tolerance):
  - Motor bolt pattern: ±0.05 mm (must align with motor)
  - Central shaft hole: +0.02/0 mm (shaft clearance)

Non-critical dimensions (standard tolerance):
  - Overall plate size: ±0.5 mm (cosmetic, no functional impact)
  - Mounting hole positions: ±0.2 mm (slots or clearance holes)
```

**Rule of thumb:** If it doesn't mate with another part or affect performance, it doesn't need a tight tolerance.

### 6. Avoid Undercuts and Re-Entrant Features

**Undercut:** Feature that cannot be accessed without tool interference or part repositioning.

**Common undercuts:**
- Internal threads longer than thread relief allows
- Grooves on inner diameter without through-bore access
- Pockets under overhanging surfaces

**DFM solutions:**
- **Redesign to eliminate:** Extend pocket to edge, remove overhang
- **Split part:** Two-piece design, assemble after machining
- **Accept secondary operation:** Manual deburring, EDM, etc.

**Example:**
```
Poor DFM: T-slot fully enclosed in block
  → Requires specialized broaching or EDM
  → Expensive, slow, specialized equipment

Good DFM: T-slot open on one side
  → Standard T-slot cutter from side entry
  → Fast, inexpensive, standard process
```

### 7. Design for Adequate Rigidity

**Part deflection during machining causes:**
- Dimensional inaccuracy
- Poor surface finish
- Tool breakage
- Scrapped parts

**DFM strategies:**

**Ribs and Gussets:**
```
Thin plate alone: flexible, chatters
Thin plate + ribs: rigid, machines well
```

**Appropriate Wall Thickness:**
```
Minimum wall thickness guidelines:
  Aluminum: 1.5 mm (thin-wall), 3 mm (standard)
  Steel: 2 mm (thin-wall), 5 mm (standard)
  Plastic: 2 mm (thin-wall), 4 mm (standard)
```

**Closed Sections:**
```
Open channel: low torsional rigidity
Closed tube: high torsional rigidity (4×-10× stiffer)
```

**Proper Fixturing Design:**
- Provide clamping surfaces parallel to cutting forces
- Avoid long unsupported spans
- Design-in fixture contact points

### 8. Specify Appropriate Surface Finish

Surface finish impacts both function and cost:

| Finish | Ra (µm) | Process | Relative Cost | Applications |
|--------|---------|---------|---------------|--------------|
| Rough | 6.3-12.5 | As-sawn, plasma cut | 1× | Non-contact surfaces |
| Machined | 1.6-3.2 | Standard milling/turning | 1.5× | General machined parts |
| Fine | 0.8-1.6 | Finish milling, grinding | 3× | Sliding surfaces, seals |
| Precision | 0.2-0.8 | Grinding, honing | 6× | Bearing surfaces, hydraulic seals |
| Mirror | <0.2 | Polishing, lapping | 10×+ | Optical surfaces, mating faces |

**DFM approach:**
- Specify finish only where needed (sealing surfaces, bearing journals, aesthetic faces)
- Leave non-critical surfaces as-machined
- Avoid specifying "mirror finish" unless truly required

### 9. Use Chamfers Instead of Fillets (External Edges)

**External edges:**

**Chamfers:**
- Faster to machine (single-pass with chamfer mill)
- Easier to program
- Removes burrs in same operation
- Good for assembly (lead-in for mating parts)

**Fillets:**
- Require ball endmill or radius tool
- Multiple passes for large radii
- Slower cycle time
- Better for stress concentration reduction

**DFM rule:** Use chamfers for assembly edges, fillets only where stress relief required.

**Internal corners (pockets):**
Always have radius (cannot have sharp corner with rotating tool). Radius = tool radius minimum.

### 10. Design for Inspection and Quality Control

**Inspectable features:**
- Accessible to measurement tools (calipers, micrometers, CMM probes)
- Clear datums for measurement reference
- Critical dimensions easy to verify

**Avoid:**
- Features measurable only with specialized gauges
- Dimensions requiring complex trigonometry to verify
- Internal features impossible to inspect without destructive testing

**DFM aids for inspection:**
- Provide datum surfaces (flat, perpendicular reference planes)
- Include witness marks or measurement reference points
- Design-in gauge access (clearance for probe, caliper jaws)

## DFM Optimization Workflow

### Step 1: Functional Requirements Analysis

Document what the part **must** do:
- Load bearing: What forces, moments, deflection limits?
- Interface: What parts mate with it? What tolerances required?
- Environment: Temperature, corrosion, wear resistance?
- Lifecycle: One-off prototype vs. production quantities?

### Step 2: Initial Design (Function-Focused)

Create design that meets functional requirements without worrying about manufacturing yet.

### Step 3: DFM Review

Systematically review design against DFM principles:

**Checklist:**
- [ ] All internal corners have adequate radii for standard tools?
- [ ] Features accessible from minimal setups?
- [ ] Tolerances appropriate for function (not over-specified)?
- [ ] Materials readily available in required form/size?
- [ ] Surface finish specified only where required?
- [ ] Part can be securely fixtured?
- [ ] No undercuts or features requiring special tooling?
- [ ] Hole sizes match standard drills/reamers?
- [ ] Thread sizes/pitches are standard?

### Step 4: Design Optimization

**Iterate to improve manufacturability:**
- Increase corner radii where possible
- Reduce pocket depths
- Relax non-critical tolerances
- Combine features to reduce setups
- Replace complex geometry with simpler approximations

### Step 5: Manufacturing Process Selection

Choose processes based on:
- Geometry (2D profile → plasma/laser; 3D features → milling)
- Material (plastic → FDM; metal → machining)
- Quantity (prototype → 3D print; production → casting/machining)
- Tolerance (loose → plasma; tight → milling/grinding)
- Surface finish (rough → waterjet; smooth → milling)

### Step 6: Prototype and Refine

- Build physical prototype
- Gather manufacturing feedback
- Measure actual vs. intended results
- Iterate design based on lessons learned

## Practical Example: Bracket Optimization

### Initial Design (Function-Focused)

**Requirements:**
- Supports 50 kg load at 200 mm cantilever
- Mounts to 80/20 extrusion (8mm slot)
- Provides M8 threaded mounting point for payload

**Initial CAD:**
```
- 10mm thick aluminum plate, 80mm × 100mm
- Complex curved reinforcement ribs
- Custom 7.2mm holes for 80/20 mounting (tight fit)
- M8 threaded hole tapped perpendicular to main surface
- Radiused corners (arbitrary 4.7mm radius)
- Polished finish specified on all surfaces
```

**Manufacturing assessment:**
- Curved ribs require 3D surfacing (slow)
- 7.2mm holes require reaming (extra operation)
- Tapped hole orientation difficult to fixture
- 4.7mm radius requires custom tool
- Polished finish adds 200% cost

### DFM-Optimized Design

**Optimizations applied:**

1. **Simplified ribs:** Straight diagonal ribs (2D profile extrude) instead of curved
2. **Standard holes:** 8.5mm clearance holes (standard drill) instead of 7.2mm reamed
3. **Hole orientation:** Thru-holes with nuts instead of tapped holes (easier access)
4. **Standard radius:** 5mm corner radius (standard 10mm ball endmill)
5. **Finish:** As-machined on non-visible surfaces, chamfer edges instead of polish
6. **Material optimization:** FEA shows 8mm plate sufficient; reduce from 10mm

**Results:**
- Machining time: 45 min → 15 min (67% reduction)
- Tool changes: 8 → 4 (simpler program)
- Material cost: 10% reduction (thinner plate)
- Cycle time per part: 3× faster
- **Total cost reduction: 55%**
- Still meets all functional requirements (FEA verified)

### Key DFM Changes Summary

| Aspect | Before DFM | After DFM | Benefit |
|--------|-----------|-----------|---------|
| Ribs | Curved 3D surfaces | Straight 2D extrudes | Simpler toolpaths |
| Holes | 7.2mm reamed | 8.5mm drilled | Eliminated reaming op |
| Threads | Tapped M8 | Through-holes + nuts | Easier fixturing |
| Corners | 4.7mm radius | 5mm radius | Standard tool |
| Finish | Polished | As-machined + chamfer | Eliminated polishing |
| Material | 10mm plate | 8mm plate | Reduced cost, weight |

## Common DFM Mistakes and Solutions

### Mistake 1: Over-Engineering for "Future Flexibility"

**Problem:**
Adding features "just in case" they're needed later increases cost now with uncertain future benefit.

**Solution:**
Design for current requirements. Modern CAD makes revisions easy if needs change.

### Mistake 2: Copying Consumer Product Aesthetics

**Problem:**
Consumer products often use molding/stamping processes that create shapes difficult/expensive to machine.

**Solution:**
Embrace machined aesthetic (clean lines, chamfered edges, visible tooling marks on non-critical surfaces).

### Mistake 3: Ignoring Material Stock Sizes

**Problem:**
Designing 65mm wide part when stock comes in 50mm or 75mm widths wastes material.

**Solution:**
Check material supplier catalogs during design phase; adjust dimensions to minimize waste.

### Mistake 4: Specifying Impossible Tolerances

**Problem:**
Specifying ±0.01mm on large plastic part (plastic moves ±0.5mm with temperature/humidity changes).

**Solution:**
Understand material behavior and process capability; specify tolerances achievable and meaningful.

### Mistake 5: Designing in a Vacuum

**Problem:**
Not consulting with machinists, suppliers, or manufacturing engineers until design is "final."

**Solution:**
Early involvement of manufacturing expertise prevents costly redesigns.

## DFM Resources and Tools

### Software Tools

**DFM Analysis Built into CAD:**
- SolidWorks DFMXpress: Automated DFM checks
- Fusion 360 Manufacture workspace: Toolpath simulation reveals issues
- FreeCAD Path workbench: Visualize machining operations

**Standalone DFM Tools:**
- DFMPro: Comprehensive DFM analysis plugin
- aPriori: Cost estimation and DFM feedback

### Knowledge Resources

**Machinist's Handbooks:**
- Machinery's Handbook (comprehensive reference)
- CNC Machining Handbook (DFM-focused)

**Online Resources:**
- Protolabs Design Tips (free guides for various processes)
- SendCutSend Design Guide (sheet metal DFM)
- Xometry Design Guide (multi-process DFM)

**Supplier Capabilities:**
Most machine shops publish capability charts:
- Minimum feature sizes
- Tolerance capabilities
- Standard materials/stock sizes
- Available tooling

**Use these during design to ensure compatibility.**

## Summary

DFM is not about compromising design quality—it's about achieving required performance through efficient manufacturing methods:

1. **Minimize part count** and complexity
2. **Design for standard tooling** (corner radii, hole sizes, thread pitches)
3. **Minimize setups** (single-setup designs when possible)
4. **Maximize material removal efficiency** (pockets, holes, wall thickness)
5. **Tolerance only critical features** (cost increases exponentially with precision)
6. **Avoid undercuts** and inaccessible features
7. **Design for rigidity** (ribs, appropriate wall thickness)
8. **Specify surface finish** only where needed
9. **Prefer chamfers** over fillets (external edges)
10. **Design for inspection** (accessible, measurable features)

**Next section** covers how to properly specify tolerances and use GD&T to communicate design intent unambiguously.

***

**Next:** [Section 16.5: Tolerancing and GD&T](section-16.5-tolerancing-gdt.md)

**Previous:** [Section 16.3: Parametric Modeling](section-16.3-parametric-modeling.md)

---

# Module 16 – CAD Design for Manufacturable Parts

## 1. Introduction

CAD (Computer-Aided Design) is the foundation for manufacturable CNC parts. Good CAD practices ensure parts are accurate, cost-effective, and compatible with downstream CAM and fabrication processes.

## 2. Design for Manufacturability (DFM)

- Minimize complex features that require specialized tooling.
- Use standard hole sizes and fillets for ease of machining.
- Design with tolerances appropriate to process capabilities.

## 3. Parametric Modeling

- Use constraints and parameters for scalable designs.
- Create master sketches for robust part families.
- Link dimensions to global variables for easy updates.

## 4. Drawing & Detailing

- Dimension critical features and reference datums.
- Include material specs, finish, and tolerances.
- Export drawings as PDF

---

# Section 16.9: Documentation and Engineering Drawings

## Introduction

Engineering drawings are the universal language of manufacturing. While your CAD model contains all geometric information, drawings communicate design intent, specifications, and manufacturing requirements to machinists, inspectors, and assemblers. Well-executed drawings ensure parts are made correctly the first time, reducing errors, scrap, and costly rework.

This section covers drawing standards, view selection, dimensioning strategies, and best practices for creating clear, unambiguous technical documentation.

## Drawing Standards

### International Standards

**ASME Y14.5 (United States):**
- Geometric Dimensioning and Tolerancing (GD&T)
- Dimensioning and tolerancing practices
- Widely used in North America

**ISO 128 / ISO 1101 (International):**
- Technical drawings general principles
- Geometrical tolerancing
- Used globally, especially in Europe and Asia

**Third-Angle vs. First-Angle Projection:**
```
Third-angle (ASME, North America):
  Object between observer and projection plane
  Top view above front view
  Right view to right of front view

First-angle (ISO, Europe):
  Projection plane between observer and object
  Top view below front view
  Right view to left of front view
```

**Symbol to indicate projection type:**
- Third-angle: Truncated cone symbol
- First-angle: Opposite truncated cone orientation

**Consistency:** Use one standard throughout a project. Most CAD systems default to third-angle (ASME).

### Drawing Sheet Formats

**Standard sheet sizes:**

| Size | ANSI (inches) | ISO (mm) |
|------|---------------|----------|
| A | 8.5 × 11 | A4: 210 × 297 |
| B | 11 × 17 | A3: 297 × 420 |
| C | 17 × 22 | A2: 420 × 594 |
| D | 22 × 34 | A1: 594 × 841 |
| E | 34 × 44 | A0: 841 × 1189 |

**Sheet selection:**
- Simple parts: A or A4
- Complex parts, assemblies: B or A3
- Large assemblies, layouts: C, D, or larger

### Title Block

**Required information:**
```
┌─────────────────────────────────────────┐
│ [Drawing Views]                         │
│                                         │
│                                         │
│                                         │
├─────────────────────────┬───────────────┤
│ TITLE BLOCK             │ Rev │ Date    │
│ Part Name: Motor Bracket│ A   │2024-3-15│
│ Part Number: MB-2024-001│     │         │
│ Material: AL 6061-T6    │     │         │
│ Finish: Anodize Type II │     │         │
│ Designer: [Name]        │     │         │
│ Drawn: [Date]          │     │         │
│ Scale: 1:1             │     │         │
│ Sheet: 1 of 1          │     │         │
└─────────────────────────┴───────────────┘
```

**Essential title block fields:**
- Part name / description
- Part number (unique identifier)
- Revision level
- Material specification
- Finish / coating
- Scale
- Designer / drafter
- Date drawn / revised
- Sheet number (if multi-sheet)
- Company name / logo

## View Selection

### Orthographic Projection

**Standard views:**
```
Front view: Primary view (most detail, natural orientation)
Top view: Looking down from above
Right side view: Looking from right side
Left side view: Looking from left side (rarely used with right view)
Bottom view: Looking up from below (rarely needed)
Rear view: Looking from behind (rarely needed)
```

**Minimum views principle:**
- Use only the views necessary to fully define the part
- Typical simple part: 2-3 views
- Symmetrical parts: May need only 1-2 views + note "SYMMETRIC ABOUT CENTERLINE"

**View selection strategy:**
1. **Front view:** Most informative orientation, shows primary features
2. **Top/Side view:** Shows features not clear in front view
3. **Auxiliary/Section views:** Only if standard views insufficient

### Section Views

**When to use section views:**
- Internal features (pockets, bores, cavities)
- Complex internal geometry
- Wall thicknesses
- Assembly interfaces

**Section view types:**

**Full Section:**
```
Cutting plane passes completely through part
Shows entire internal cross-section
Most common type
```

**Half Section:**
```
Quarter of part removed
Shows both exterior and interior in single view
Good for symmetric parts
```

**Offset Section:**
```
Cutting plane offsets to pass through multiple features
Shows features not on same plane
```

**Broken-Out Section:**
```
Small local section (doesn't extend across entire view)
Shows specific internal detail
```

**Section line conventions:**
```
General purpose (most materials): 45° hatching
Cast iron: Random broken lines
Aluminum/magnesium: Wider spacing 45° lines
```

**Section view labeling:**
```
Cutting plane line: A-A
Section view title: SECTION A-A
Scale (if different from main): SCALE 2:1
```

### Detail Views

**Magnified detail of small features:**
```
Main view: Part at 1:2 scale
Detail A: Specific feature at 2:1 scale (magnified)

Label:
  On main view: "DETAIL A" with circle around feature
  Detail view: "DETAIL A" with "SCALE 2:1"
```

**When to use:**
- Threads, small chamfers, complex small features
- Avoid cluttering main view with dimensions
- Clarify geometric complexity

### Auxiliary Views

**View projected at angle to standard views:**

**When needed:**
- Features at angles (not parallel to standard planes)
- True size/shape of angled surfaces
- Hole patterns on angled faces

**Example:**
```
Part with surface at 30° to horizontal
Standard views show surface foreshortened (not true size)
Auxiliary view perpendicular to angled surface shows true dimensions
```

## Dimensioning Strategies

### Dimensioning Principles

**Dimension once:**
- Each feature dimensioned only once
- Avoid redundant dimensions (causes conflicts if tolerances differ)

**Dimension to function:**
- Show dimensions the way the part will be inspected
- Relate features that interact (mating surfaces, bolt patterns)

**Chain vs. Baseline Dimensioning:**

**Chain dimensioning (avoid):**
```
├─ 25 ─┼─ 30 ─┼─ 25 ─┤
Tolerance stack-up: ±0.1 + ±0.1 + ±0.1 = ±0.3mm total
```

**Baseline dimensioning (preferred):**
```
├─ 25 ─┤
├──── 55 ────┤
├──────── 80 ────────┤
Each dimension independent, from common datum
Tolerance: Each dimension ±0.1mm (no stack-up)
```

**Datum-based dimensioning:**
```
All critical dimensions referenced to datum surfaces (A, B, C)
Matches GD&T approach
Aligns with manufacturing setup and inspection
```

### Dimension Placement

**Outside the view (preferred):**
```
        50
    ├────────┤
    ┌────────┐
    │        │  30
    │        │  ↕
    └────────┘
```

**Inside the view (only if necessary):**
- Avoid when possible (clutters view)
- Use for large parts where outside dimension too far from feature

**Leader lines:**
```
Use for holes, callouts, notes
Arrow points to feature
Text at end of leader, horizontal
```

**Dimension line spacing:**
```
First dimension: 10mm from part outline
Subsequent dimensions: 6-8mm spacing between lines
Prevents crowding, improves readability
```

### Dimensioning Specific Features

**Holes:**
```
⌀8.0 +0.1/0  (diameter, unilateral tolerance)
⌀8.0 ±0.05   (diameter, bilateral tolerance)
⌀8 THRU      (through hole, no depth specified)
⌀10 ↧15      (counterbore: diameter 10, depth 15)
⌀8 ⌴90°      (countersink: diameter 8, 90° angle)
```

**Threads:**
```
M6×1.0 – 6H  (metric thread, 6mm diameter, 1mm pitch, 6H fit class)
M8×1.25 THRU (metric thread through-hole)
M6×1.0 ↧12   (metric thread, 12mm deep)
1/4-20 UNC   (unified coarse thread, 1/4" diameter, 20 TPI)
```

**Chamfers:**
```
2 × 45°      (2mm × 45° chamfer)
1 × 30°      (1mm × 30° chamfer)
C2           (shorthand for 2 × 45°)
```

**Fillets and Radii:**
```
R5       (radius 5mm)
R5 TYP   (radius 5mm typical - applies to all similar features)
SR3      (spherical radius 3mm)
```

**Slots:**
```
Width × Length
Example: 8 × 50 SLOT
```

**Patterns:**
```
4× ⌀6.5      (4 places, diameter 6.5mm)
8× ⌀10 EVENLY SPACED ON ⌀100 BOLT CIRCLE
```

## Tolerances and Notes

### General Tolerance Notes

**Block tolerance note:**
```
UNLESS OTHERWISE SPECIFIED:
  - Decimal dimensions: ±0.1 mm
  - Angular dimensions: ±1°
  - Chamfers: 0.5 × 45°
  - Fillets: R2
  - Surface finish: 3.2 µm Ra
  - Break all sharp edges
```

**Benefits:**
- Reduces clutter (don't tolerance every dimension individually)
- Establishes shop capabilities
- Only critical features get specific callouts

### Specific Tolerance Callouts

**Critical dimensions:**
```
50.00 ±0.02   (tight tolerance for functional feature)
25 +0.05/0    (unilateral tolerance, hole clearance)
100 ±0.5      (loose tolerance, non-critical)
```

**GD&T callouts:**
```
Position: ⊕ ⌀0.1 (M) | A | B |
Flatness: ⬜ 0.05
Perpendicularity: ⊥ 0.08 | A |

(Refer to Section 16.5 for detailed GD&T)
```

### Material and Finish Notes

**Material specification:**
```
MATERIAL: ALUMINUM 6061-T6 PER ASTM B209
MATERIAL: STEEL 1018 CRS
MATERIAL: STAINLESS STEEL 304
MATERIAL: DELRIN (ACETAL COPOLYMER)
```

**Surface finish:**
```
[Triangle symbol] 3.2   (Surface finish 3.2 µm Ra)
[Triangle symbol] 1.6   (Finish 1.6 µm Ra on specific surface)
```

**Coating/finish:**
```
FINISH: ANODIZE TYPE II, CLEAR, MIL-A-8625
FINISH: POWDER COAT, RAL 9005 (BLACK)
FINISH: ZINC PLATE, CLEAR CHROMATE
FINISH: MACHINE FINISH, NO COATING
```

**Heat treatment:**
```
HEAT TREAT: HARDNESS 50-55 HRC AFTER QUENCH & TEMPER
HEAT TREAT: STRESS RELIEVE AT 550°F FOR 4 HOURS
```

### Manufacturing Notes

**Machining notes:**
```
DEBURR ALL EDGES
BREAK SHARP EDGES 0.2mm MAX
DO NOT MACHINE SURFACE [A] (as-cast, as-rolled, etc.)
ALL HOLES ±0.1 UNLESS NOTED
```

**Assembly notes (on assembly drawings):**
```
APPLY LOCTITE 243 TO THREADS BEFORE ASSEMBLY
TORQUE FASTENERS TO 10 N·m
GREASE BEARING WITH MOBILITH SHC 100
```

**Inspection notes:**
```
INSPECT PER FIRST ARTICLE INSPECTION (FAI)
CRITICAL DIMENSIONS MARKED WITH [★]
CMM INSPECTION REQUIRED
```

## Drawing Types

### Detail Drawing (Part Drawing)

**Purpose:** Fully defines single part for manufacturing

**Contents:**
- Multiple orthographic views
- Dimensions (all features)
- Tolerances (GD&T, +/-, general)
- Material specification
- Surface finish
- Notes (machining, finishing)
- Title block

**When to create:**
- Every custom-designed part
- Parts manufactured in-house
- Parts sent to vendors for fabrication

### Assembly Drawing

**Purpose:** Shows how parts fit together

**Contents:**
- Assembly views (orthographic, isometric, exploded)
- Item balloons (numbered references to BOM)
- Critical assembly dimensions (overall size, key interfaces)
- Assembly notes (torque specs, adhesives, orientations)
- Bill of Materials (BOM)

**What NOT to include:**
- Individual part dimensions (those go on detail drawings)
- Manufacturing details of parts

**Types of assembly drawings:**

**General assembly:**
```
Shows entire product assembled
Overall dimensions
Subassembly callouts
```

**Subassembly drawing:**
```
Specific subassembly detail
Parts list for subassembly only
Assembly sequence
```

**Exploded assembly:**
```
Parts separated along assembly axis
Clearly shows how parts fit together
Numbered balloons match BOM
Assembly instructions reference this
```

### Installation Drawing

**Purpose:** Guide end-user installation

**Contents:**
- Mounting dimensions
- Required clearances
- Utilities (power, air, coolant connections)
- Foundation requirements (floor mounting, vibration isolation)
- Safety zones (keep clear areas)

### Fabrication Drawing (for cutting processes)

**Purpose:** Guide 2D cutting operations (plasma, laser, waterjet, sheet metal)

**Contents:**
- Flat pattern (unfolded geometry)
- Bend lines and bend angles (sheet metal)
- Material thickness
- Edge finish requirements
- Nesting layout (multiple parts per sheet)

**Formats:**
- DXF export (2D geometry for CAM)
- PDF drawing (notes, material, finish)

## CAD-to-Drawing Workflow

### Creating Drawings from 3D Models

**Typical process:**

**1. Create drawing file from part/assembly:**
```
CAD systems:
  - SolidWorks: New Drawing from part
  - Fusion 360: Create Drawing
  - FreeCAD: TechDraw workbench
```

**2. Insert views:**
```
- Select front view orientation
- Auto-project top, side views
- Add section views where needed
- Add detail views for small features
```

**3. Adjust view scale:**
```
Simple parts: 1:1 (actual size)
Large parts: 1:2, 1:5, 1:10 (reduced)
Small parts: 2:1, 5:1 (enlarged for clarity)

Show scale in view title or general note
```

**4. Add dimensions:**
```
- Import model dimensions (smart dimensioning)
- Add manufacturing-relevant dimensions
- Remove redundant CAD dimensions
- Apply baseline/ordinate dimensioning for critical features
```

**5. Add GD&T callouts:**
```
- Define datums
- Add feature control frames
- Specify tolerances
```

**6. Add notes:**
```
- General notes (material, finish, tolerances)
- Specific notes (manufacturing instructions)
- Revision notes
```

**7. Populate title block:**
```
- Part number, name
- Material
- Scale
- Designer, date
- Revision level
```

**8. Review and export:**
```
- Check: All features dimensioned?
- Check: Tolerances appropriate?
- Check: Views clear and uncluttered?
- Export PDF for distribution
```

### Drawing Best Practices

**Clarity:**
- Avoid dimension crowding (use multiple views)
- Use appropriate scale (large enough to read, not wastefully large)
- Consistent line weights (thick for part outline, thin for dimensions)

**Completeness:**
- Every manufacturing feature dimensioned
- All tolerances specified (specific or general)
- Material and finish clearly stated

**Consistency:**
- Same dimensioning style throughout
- Consistent units (don't mix mm and inches)
- Consistent terminology in notes

**Simplicity:**
- Fewest views necessary
- Avoid unnecessary complexity
- Standard symbols and abbreviations

## Revision Control

### Revision Levels

**Revision naming:**
```
Prototype: Proto-1, Proto-2, ... (not released for production)
Released: RevA, RevB, RevC, ... (production versions)
  OR: Rev 1.0, Rev 1.1, Rev 2.0, ...
```

**Revision block on drawing:**
```
┌─────┬────────────────────┬──────┬──────┐
│ Rev │ Description        │ Date │ By   │
├─────┼────────────────────┼──────┼──────┤
│ A   │ Initial release    │ 3/15 │ JDoe │
│ B   │ Increased hole ⌀  │ 4/02 │ JDoe │
│ C   │ Added chamfers     │ 5/10 │ ASmith│
└─────┴────────────────────┴──────┴──────┘
```

### Engineering Change Orders (ECO)

**Formal change process:**
```
1. Identify need for change (field failure, design improvement, cost reduction)
2. Document change in ECO:
   - ECO number (unique ID)
   - Description of change
   - Reason for change
   - Parts affected
   - Effectivity (which serial numbers get change)
3. Approve ECO (engineering manager, QA, production)
4. Update drawings, CAD models
5. Increment revision level
6. Notify affected parties (manufacturing, purchasing, QA)
```

**Change annotation on drawing:**
```
Cloud/bubble around changed feature
Reference to ECO number in revision block
```

## Export Formats

### File Formats for Different Uses

**PDF (Portable Document Format):**
```
Use: Distribution to machinists, vendors, inspection
Advantages:
  - Universal (any device, no special software)
  - Non-editable (prevents unauthorized changes)
  - Searchable text (if created from CAD, not scanned)
  - Compact file size
```

**DWG/DXF (AutoCAD formats):**
```
Use: Sharing editable drawings, CAM import (2D)
Advantages:
  - Industry standard
  - Editable in AutoCAD, compatible CAD systems
  - 2D geometry for CAM (plasma, laser, waterjet)
Disadvantages:
  - Version compatibility issues
  - Can be altered
```

**STEP (ISO 10303):**
```
Use: 3D model exchange (CAD to CAD, CAD to CAM)
Advantages:
  - Neutral format (cross-platform)
  - Preserves 3D geometry, assemblies
  - Industry standard for 3D model exchange
```

**IGES (older 3D exchange format):**
```
Use: Legacy systems
Disadvantages:
  - Less reliable than STEP
  - Use STEP instead when possible
```

**STL (Stereolithography):**
```
Use: 3D printing, visualization
Advantages:
  - Universal for 3D printing
  - Simple mesh format
Disadvantages:
  - Faceted (not smooth curves)
  - No dimensional accuracy (mesh approximation)
  - Use for visualization and 3D printing only, NOT manufacturing drawings
```

## Summary

Engineering drawings translate CAD models into manufacturing instructions:

**Drawing Standards:**
- ASME Y14.5 (North America) or ISO 128/1101 (International)
- Third-angle or first-angle projection (be consistent)
- Standard sheet sizes (ANSI A-E or ISO A4-A0)

**View Selection:**
- Minimum views to fully define part
- Section views for internal features
- Detail views for small/complex features
- Auxiliary views for angled surfaces

**Dimensioning:**
- Dimension once per feature
- Baseline dimensioning (avoid tolerance stack-up)
- Datum-based (matches manufacturing setup)
- Clear, uncluttered placement

**Tolerances and Notes:**
- General tolerance block (default for non-critical dimensions)
- Specific tolerances for critical features
- GD&T for complex geometric requirements
- Material, finish, manufacturing notes

**Drawing Types:**
- Detail drawings (individual parts)
- Assembly drawings (BOM, balloons, assembly notes)
- Fabrication drawings (2D cutting, flat patterns)

**Revision Control:**
- ECO process for changes
- Revision history on drawing
- Change clouds/annotations

**Next section** covers preparing CAD models for CAM programming and the handoff to manufacturing.

***

**Next:** [Section 16.10: CAD-CAM Integration](section-16.10-cad-cam-integration.md)

**Previous:** [Section 16.8: Assembly Design](section-16.8-assembly-design.md)

---

# Section 16.10: CAD-CAM Integration

## Introduction

The transition from CAD design to CAM (Computer-Aided Manufacturing) programming is a critical handoff point. Well-prepared CAD models import cleanly into CAM software, enabling efficient toolpath generation. Poorly prepared models cause errors, require manual fixes, and waste programming time. This section covers best practices for preparing CAD models for CAM, common pitfalls, and optimization strategies.

## Understanding the CAD-CAM Workflow

### The Complete Pipeline

```
CAD Model → Export → Import to CAM → Setup → Toolpath Generation → Simulation → Post-Processing → G-code → CNC Machine
```

**CAD responsibilities:**
- Accurate geometry
- Proper file format
- Feature organization
- Stock definition
- Coordinate system establishment

**CAM responsibilities:**
- Tool selection
- Toolpath strategies
- Feeds and speeds
- Operation sequencing
- G-code generation

**Overlap zone (CAD can help CAM):**
- Feature recognition geometry
- Work coordinate setup
- Stock modeling
- Fixture clearance zones

## CAD Model Preparation for CAM

### Geometry Quality

**Clean, valid solid models:**
```
✓ Closed, watertight solids (no gaps, missing faces)
✓ No self-intersecting surfaces
✓ No duplicate/overlapping geometry
✓ Proper face normals (consistent inside/outside)
✗ Surface models (CAM needs solids for volume calculations)
✗ Sketch geometry mixed with 3D solids
✗ Construction geometry left visible
```

**CAD cleanup checklist:**
- [ ] Delete construction geometry before export
- [ ] Verify solid model (not surface) using CAD validation tools
- [ ] Check for small sliver faces (merge or remove)
- [ ] Ensure all features properly merged/subtracted

### Feature Recognition

**CAM software recognizes standard features:**
- Holes (through, blind, countersunk, counterbored)
- Pockets (rectangular, irregular)
- Bosses (raised features)
- Slots
- Faces (planar surfaces to mill)

**Design features CAM can recognize:**

**Holes:**
```
Simple cylindrical holes:
  ✓ Single diameter (or stepped diameters)
  ✓ Blind or through
  ✓ Perpendicular to face
```

**Pockets:**
```
Enclosed perimeter:
  ✓ Clear floor
  ✓ Defined depth
  ✓ Radiused internal corners
  ✓ No undercuts
```

**Faces:**
```
Planar surfaces to machine:
  ✓ Flat, bounded regions
  ✓ Accessible to tool without interference
```

**Design to aid feature recognition:**
```
✓ Use CAD hole features (not extruded cuts) — CAM recognizes as drill operations
✓ Create pockets as distinct features (not complex boolean operations)
✓ Separate features for different operations (rough pocket, finish walls separately)
```

### Coordinate Systems and Work Offsets

**Work Coordinate System (WCS):**
- Origin point (X0, Y0, Z0)
- Axis orientation (X, Y, Z directions)
- Matches machine setup and fixturing

**CAD should define WCS matching manufacturing setup:**

**Example 1: Vise-mounted part**
```
Origin: Top-left corner of stock
  X+ → Right
  Y+ → Away from operator
  Z+ → Up from top face

Rationale:
  - Easy to locate with edge finder
  - Matches common machine convention
  - Positive Z moves tool up (safe)
```

**Example 2: Part on fixture plate**
```
Origin: Center of locating hole
  (CAM references hole center, not corner)

Datum features:
  - Locating pin in center hole (X, Y, rotation reference)
  - Part bottom surface on fixture plate (Z reference)
```

**CAD approach:**
- Create coordinate system in CAD at intended WCS origin
- Export geometry with this origin
- CAM imports with correct zero point

### Stock Definition

**Stock = raw material before machining**

**CAD can model stock:**
```
1. Create stock body (separate from part)
   - Rectangular bounding box
   - Cylindrical bar (for turning)
   - Actual stock shape (casting, forging)

2. Position part within stock
   - Leave machining allowance on all machined faces
   - Show as-received surfaces (no machining needed)

3. Export both part AND stock to CAM
```

**Stock modeling benefits:**
- CAM calculates material removal volume
- Toolpath avoids air cutting (faster cycle time)
- Simulation shows stock removal (visualize machining sequence)

**Example: Milled block from plate stock**
```
Stock: 100 × 100 × 25 mm aluminum plate
Part: 95 × 95 × 20 mm (machined all faces)
Stock allowance: 2.5 mm on X, Y sides; 5 mm on top face; bottom face as-received

CAD model:
  - Part body: final dimensions
  - Stock body: 100 × 100 × 25 mm block positioned around part
  - Export both to CAM
```

### Multi-Setup Models

**Parts requiring multiple setups:**

**Approach 1: Single CAD file with setup features**
```
CAD file contains:
  - Final part geometry
  - Datum features (locating holes, surfaces for Setup 2)
  - Notes indicating which features machined in which setup
```

**Approach 2: Separate CAD files per setup**
```
Part_Setup1.step: Geometry as appears after Setup 1 (includes stock for Setup 2)
Part_Setup2.step: Final geometry

CAM workflow:
  - Import Part_Setup1 → program Setup 1 operations
  - Import Part_Setup2 → program Setup 2 operations (using Setup 1 geometry as stock)
```

**Datum establishment for Setup 2:**
```
Setup 1: Create precision locating holes, datum surfaces
Setup 2: Reference these features in CAM for work offset
```

## File Formats for CAM

### 3D Model Formats

**STEP (.step, .stp):**
```
Advantages:
  ✓ Industry standard (ISO 10303)
  ✓ Preserves solid model data
  ✓ Cross-platform compatibility
  ✓ Supports assemblies
  ✓ Retains feature information (some CAM systems)

Best for: Most CAM workflows (milling, turning)
```

**IGES (.iges, .igs):**
```
Advantages:
  ✓ Widely compatible

Disadvantages:
  ✗ Older standard
  ✗ Less reliable than STEP (translation errors common)
  ✗ May lose feature data

Use: Only if CAM system doesn't support STEP (rare)
```

**Native CAD formats:**
```
SolidWorks (.sldprt), Inventor (.ipt), Fusion 360 (.f3d)

Advantages:
  ✓ No translation (if CAM supports native format)
  ✓ Full feature tree available (advanced CAM feature recognition)

Disadvantages:
  ✗ CAM system must support specific CAD format
  ✗ Version compatibility issues

Best for: Integrated CAD/CAM (Fusion 360, SolidWorks CAM)
```

### 2D Profile Formats

**DXF (.dxf) / DWG (.dwg):**
```
Use: 2D cutting operations (plasma, laser, waterjet, wire EDM)

Export from CAD:
  - Flatten 3D part to 2D profile
  - OR create sketch of cut profile
  - Export as DXF

CAM import:
  - Recognizes lines, arcs, circles, splines
  - Generates cutting toolpaths from profile geometry
```

**SVG (.svg):**
```
Use: Some laser cutters, hobbyist CAM software

Less common in industrial applications
```

### Mesh Formats (Avoid for CAM)

**STL (.stl):**
```
Disadvantages for CAM:
  ✗ Faceted (approximation of curves)
  ✗ No dimensional accuracy
  ✗ CAM must triangulate → poor toolpaths

Use ONLY for:
  ✓ 3D printing
  ✓ Visualization

DO NOT use for milling, turning, cutting CAM programs
```

## CAM Software Feature Recognition

### Automatic Feature Recognition

**CAM systems with feature recognition:**
- Autodesk Fusion 360
- Mastercam
- GibbsCAM
- SolidCAM
- Tebis

**How it works:**
```
1. Import CAD model (STEP or native)
2. CAM analyzes geometry
3. Identifies features:
   - Holes (drill candidates)
   - Pockets (2D/3D milling candidates)
   - Faces (face milling candidates)
4. Suggests appropriate toolpaths
5. Operator reviews, accepts, modifies
```

**Example recognition:**
```
CAD model: Block with 6 holes, 2 pockets, top face

CAM recognizes:
  - 6 holes → "Spot drill + drill operations recommended"
  - 2 pockets → "2D adaptive clearing recommended"
  - Top face → "Face milling recommended"

Operator:
  - Accepts hole operations
  - Modifies pocket strategy (wants roughing + finishing passes)
  - Accepts face milling
```

**Design to maximize recognition:**
- Use standard hole features in CAD (not Boolean cuts)
- Create pockets with clear boundaries
- Separate features for different machining strategies

### Manual Feature Selection

**CAM without automatic recognition:**
- Operator manually selects faces, edges, profiles
- Defines operations (2D contour, pocket, drill, etc.)
- More time-consuming but full control

**CAD can still help:**
- Clear, simple geometry
- Features separated into distinct faces/bodies
- Named features or layers (some CAM systems can filter by name/layer)

## Common CAD-to-CAM Issues and Solutions

### Issue 1: Missing or Invalid Geometry

**Symptoms in CAM:**
- Import fails or gives errors
- Geometry appears incomplete
- Toolpath generation fails

**Root causes:**
- Surface model instead of solid
- Open edges (non-watertight)
- Corrupt CAD file

**Solutions:**
```
In CAD:
  ✓ Validate solid model (CAD checker tool)
  ✓ Export as STEP (most reliable translation)
  ✓ Simplify complex features if causing export issues

In CAM:
  ✓ Increase import tolerance (if allowed)
  ✓ Use "heal" or "repair" tools
  ✓ Manually rebuild problem features
```

### Issue 2: Incorrect Units

**Symptoms:**
- Part appears 25.4× too large or too small
- Dimensions don't match drawing

**Root cause:**
- CAD model in mm, CAM interprets as inches (or vice versa)

**Solutions:**
```
In CAD:
  ✓ Verify model units before export (File properties)
  ✓ Include units in filename: "Part_mm.step" or "Part_inch.step"

In CAM:
  ✓ Check import units dialog
  ✓ Measure known dimension after import to verify
```

### Issue 3: Complex Geometry Slows CAM

**Symptoms:**
- CAM software slow or crashes
- Toolpath calculation takes hours

**Root causes:**
- Excessive detail (small fillets, chamfers everywhere)
- Complex splines/surfaces
- High-polygon count imported from mesh

**Solutions:**
```
In CAD:
  ✓ Simplify non-critical features (remove tiny fillets)
  ✓ Use "defeaturing" tools (remove cosmetic details)
  ✓ Create separate "CAM model" (simplified version)

Example:
  Design model: 50 fillets, engraved logo, fine knurling
  CAM model: Essential geometry only (critical dimensions, machined features)
```

### Issue 4: Feature Not Recognized

**Symptoms:**
- CAM doesn't auto-detect holes, pockets
- Must manually program every feature

**Root cause:**
- Feature geometry doesn't match CAM expectations
  (e.g., angled hole, non-cylindrical pocket)

**Solutions:**
```
In CAD:
  ✓ Use standard feature types (hole wizard, not extruded cuts)
  ✓ Keep features perpendicular to setup face when possible
  ✓ Simplify pocket geometry (avoid complex multi-level pockets)

In CAM:
  ✓ Manually define features CAM doesn't recognize
  ✓ Adjust recognition settings (tolerances, angle limits)
```

### Issue 5: Coordinate System Mismatch

**Symptoms:**
- Part appears rotated or offset in CAM
- Toolpaths in wrong location

**Root cause:**
- CAD origin ≠ CAM work offset expectation
- Axis orientation mismatch

**Solutions:**
```
In CAD:
  ✓ Define explicit coordinate system at machining origin
  ✓ Export from this coordinate system
  ✓ Document origin location on drawing

In CAM:
  ✓ Redefine WCS to match CAD intent
  ✓ Translate/rotate geometry after import if needed
  ✓ Verify setup before toolpath generation
```

## Optimizing CAD Models for Efficient CAM Programming

### 1. Organize Features by Operation

**Group similar features:**
```
All through-holes on top face:
  - CAM can pattern drill operation
  - Faster programming

Mixed features scattered:
  - CAM must program each individually
  - Slower, error-prone
```

**CAD approach:**
- Linear or circular patterns for repeated features
- Consistent feature types (all holes same depth if possible)

### 2. Minimize Setups

**Design features accessible from single direction:**
```
✓ All critical machining from top face
✓ Bottom face as-received or rough-machined only

✗ Critical features on top, sides, bottom
  → Multiple setups, longer CAM programming time
```

**If multiple setups required:**
- Provide locating features (dowel pin holes)
- Document setup sequence on drawing
- Consider separate CAD files per setup

### 3. Use Standard Tool Sizes

**CAD model with standard corner radii:**
```
Internal corner radii: 1.5 mm, 3 mm, 6 mm (match common tool sizes)

CAM benefits:
  ✓ Uses standard tools already in library
  ✓ Faster programming (no custom tool creation)
  ✓ Lower tooling cost (standard endmills readily available)
```

**CAD model with arbitrary radii:**
```
Internal corner radii: 2.3 mm, 4.7 mm, 5.9 mm

CAM challenges:
  ✗ Requires custom tool definition
  ✗ May need special-order tooling
  ✗ Slows programming
```

### 4. Provide Stock Models

**Include stock body in export:**
```
CAM benefits:
  ✓ Automatic stock-to-part calculation
  ✓ Optimized roughing toolpaths (removes only necessary material)
  ✓ Simulation shows actual material removal
```

**Without stock model:**
```
CAM must:
  - Manually define bounding box
  - Conservative toolpaths (assumes more stock)
  - Longer cycle times (unnecessary air cutting)
```

### 5. Name Features Logically

**Named features (if CAM supports):**
```
CAD feature names:
  - Mounting_Holes_M6
  - Main_Pocket
  - Datum_A_Face
  - Thread_M8x1.25

CAM import:
  - Can filter/select features by name
  - Organize operations logically
  - Easier to review program
```

## Integrated CAD/CAM Systems

### All-in-One Platforms

**Autodesk Fusion 360:**
```
Integrated CAD + CAM in same environment:
  ✓ No export/import (seamless transition)
  ✓ Full parametric history available to CAM
  ✓ Changes in CAD auto-update CAM (with warnings)

Workflow:
  1. Design in CAD workspace
  2. Switch to Manufacture workspace (same file)
  3. Define setups, operations directly on CAD model
  4. Generate toolpaths
  5. Simulate
  6. Post-process to G-code
```

**SolidWorks CAM (CAMWorks):**
```
CAM plugin for SolidWorks:
  ✓ Works directly on SolidWorks files
  ✓ Feature recognition from native feature tree
  ✓ Parametric CAM (dimensions change → toolpaths update)
```

**Mastercam for SolidWorks:**
```
Integrated CAM for SolidWorks users:
  ✓ Reads native SolidWorks files
  ✓ Associates to SolidWorks features
  ✓ Separate Mastercam license required
```

### Advantages of Integrated Systems

**Single file workflow:**
- No export/import steps
- Reduced file management
- CAD changes trigger CAM review (warnings if toolpaths affected)

**Full feature access:**
- CAM sees entire parametric history
- Better feature recognition
- Can suppress features for CAM (without affecting design)

**Associativity:**
- Change CAD dimension → CAM toolpaths update automatically (or flag for review)
- Ensures CAM always matches current design

### Standalone CAM Systems

**Separate CAM software:**
```
Examples:
  - Mastercam (standalone)
  - GibbsCAM
  - Edgecam
  - BobCAD-CAM

Workflow:
  1. Design in any CAD (SolidWorks, Fusion, FreeCAD, etc.)
  2. Export neutral format (STEP)
  3. Import to CAM system
  4. Program operations
  5. Generate G-code
```

**Advantages:**
- Choose best CAD for design, best CAM for programming
- Powerful CAM features (5-axis, advanced toolpath strategies)
- Independent updates (CAD and CAM software on separate release cycles)

**Disadvantages:**
- Extra import/export step
- No automatic update if CAD changes
- Must manually re-import revised models

## Verification and Simulation

### CAM Simulation

**Verifying toolpaths before machining:**
```
CAM simulation shows:
  ✓ Tool removing material from stock
  ✓ Finished part dimensions
  ✓ Potential collisions (tool holder, fixtures)
  ✓ Gouges or uncut areas

Check:
  - Does simulated part match CAD model?
  - Any missed features?
  - Any over-cutting (crashes)?
  - Tool holder clearance?
```

**CAD role in simulation:**
- Provide accurate stock model (simulation starts here)
- Model fixtures, clamps if possible (check clearances)

### Post-Simulation Review

**Compare simulation result to CAD:**
```
Overlay simulated part on original CAD:
  ✓ Perfect match → Toolpaths correct
  ✗ Differences → Review toolpath issues

Common issues caught:
  - Uncut material (tool too large, no clearance)
  - Over-cut (tool compensated wrong direction)
  - Missing operations
```

## Summary

Efficient CAD-to-CAM integration requires thoughtful CAD model preparation:

**CAD Model Quality:**
- Clean, valid solid models (no gaps, overlaps)
- Organized features (by operation, accessibility)
- Proper coordinate systems (match setup)

**File Formats:**
- STEP (preferred for 3D machining)
- DXF (2D cutting)
- Native formats (integrated CAD/CAM)

**Feature Recognition:**
- Design standard features (holes, pockets)
- Use CAD feature tools (not Boolean operations)
- Simplify geometry (remove unnecessary complexity)

**Stock Definition:**
- Model stock body
- Export with part
- Enables optimized toolpaths

**Common Issues:**
- Invalid geometry: Validate before export
- Unit mismatches: Document units clearly
- Complex geometry: Simplify CAM models
- Coordinate mismatches: Define explicit WCS

**Integrated vs. Standalone CAM:**
- Integrated: Seamless, associative, single file
- Standalone: Flexible, powerful, extra import step

**Verification:**
- Simulate toolpaths in CAM
- Compare result to CAD model
- Catch errors before machining

**Next section** covers advanced CAD techniques including simulation, topology optimization, and cutting-edge design methods.

***

**Next:** [Section 16.11: Advanced Techniques](section-16.11-advanced-techniques.md)

**Previous:** [Section 16.9: Documentation and Drawings](section-16.9-documentation-drawings.md)

---

# Section 16.1: Introduction to CAD Design for Manufacturing

## Overview

Think of CAD as the universal translator between your ideas and physical parts. Every CNC-machined component—from a simple bracket to a complex aerospace fitting—starts its life as digital geometry in CAD software. But here's the crucial insight: **a beautiful 3D model doesn't guarantee a manufacturable part**.

This module teaches you to think like both a designer AND a machinist. You'll learn to create CAD models that are not just geometrically correct, but optimized for real-world manufacturing. The difference between an amateur CAD model and a professional one isn't artistic flair—it's understanding how your digital design translates to cutting tools, machine motions, and manufacturing costs.

**Real-world impact:** A well-designed CAD model can reduce machining time by 50%, eliminate secondary operations, and prevent costly mistakes. A poorly designed model might look perfect on screen but be impossible to manufacture—or cost 10× more than necessary.

## The Role of CAD in the Manufacturing Workflow

### Design-to-Manufacturing Pipeline

Every manufactured part flows through this pipeline:

```
CAD Model → CAM Programming → G-code Generation → CNC Machining → Finished Part
    ↓              ↓                  ↓                  ↓
 Design Intent   Toolpaths      Machine Code      Physical Reality
```

**What happens at each stage:**

1. **CAD Model (You are here):** Define shape, dimensions, tolerances, material
2. **CAM Programming:** Convert geometry into cutting tool movements
3. **G-code Generation:** Translate toolpaths into machine-specific commands
4. **CNC Machining:** Machine physically cuts material following G-code
5. **Finished Part:** Inspect dimensions, test function, deliver product

**Why CAD decisions matter:**

Let's look at a simple example—a pocket (rectangular cavity) in a metal block:

**Poor CAD Design:**
- Internal corners specified as sharp 90° angles
- **Problem:** Rotating cutting tools CANNOT create sharp internal corners
- **Impact:** CAM programmer must add corner radii manually, or machinist must use EDM (expensive, slow)
- **Cost:** 3× longer machining time, potential $200+ EDM charge

**Optimized CAD Design:**
- Internal corners have 3mm radius (matches common 6mm endmill)
- **Result:** Standard tool cuts pocket in single operation
- **Impact:** Fast, cheap, no special operations needed
- **Cost:** Baseline manufacturing cost

This ONE design decision (corner radius) makes the difference between a $50 part and a $200 part. Multiply this across hundreds of features and you see why CAD matters.

### Integration with Course Modules

Module 16 synthesizes knowledge from all previous modules in this course:

| Previous Module | CAD Integration |
|----------------|----------------|
| Module 1-2: Mechanical Frame & Axes | Understanding machine constraints and work envelopes |
| Module 3: Linear Motion | Designing within machine accuracy and repeatability |
| Module 4: Control Electronics | Coordinating design with machine capabilities |
| Module 5: Plasma Cutting | Designing for kerf width, pierce points, and material warping |
| Module 6: Spindle & Milling | Tool access, corner radii, surface finish requirements |
| Module 7: Fiber Laser | Heat-affected zones, edge quality, thin wall design |
| Module 8: Waterjet | Taper compensation, abrasive limitations |
| Module 9-10: Robotics | Pick-and-place features, assembly considerations |
| Module 11: Large FDM | Additive manufacturing design principles |
| Module 12: Hybrid Systems | Multi-process optimization |
| Module 13: EMI/EMC | Enclosure design, grounding features |
| Module 14: LinuxCNC HAL | Custom fixtures and workholding design |
| Module 15: G-code | Understanding how CAD geometry becomes motion commands |

## What Makes a Design "Manufacturable"?

A "manufacturable" design is one that can be made **reliably, economically, and at the required quality level** with available equipment and processes. It's not enough for a part to be theoretically possible to make—it must be practical.

### The Four Pillars of DFM (Design for Manufacturability)

Think of these as your design health check. Every feature you add should pass all four tests:

**1. Process Compatibility: "Can we actually make this?"**

Ask yourself:
- Can the required features be created with available machines? (3-axis mill, plasma cutter, 3D printer, etc.)
- Can cutting tools physically access all surfaces without hitting fixtures or other part features?
- Do feature sizes match machine capabilities? (hole too small for available drills? pocket deeper than tool can reach?)

**Real example:**
- ❌ **Bad:** Designing a plasma-cut part with 0.5mm holes (plasma kerf is ~2mm—physically impossible)
- ✓ **Good:** Holes ≥6mm diameter for plasma, or mark small holes to be drilled in secondary operation

**2. Economic Viability: "Can we make this at reasonable cost?"**

Manufacturing cost drivers:
- **Setup time:** How many times must part be repositioned/re-fixtured?
- **Tool changes:** Does part require 15 different tools or 3?
- **Material waste:** Does design use standard stock sizes efficiently?
- **Secondary operations:** Does part need grinding, EDM, heat treatment, special coating?

**Real example:**
- ❌ **Bad:** Bracket requiring milling from solid billet (80% material waste, 2 hours machine time)
- ✓ **Good:** Same bracket laser-cut from plate + bent (90% material utilization, 5 minutes cutting + 2 minutes bending)

**3. Quality Achievement: "Will parts consistently meet specs?"**

Consider:
- Are tolerances achievable with the chosen process? (plasma ±0.5mm typical, milling ±0.05mm typical)
- Are critical dimensions specified clearly (GD&T, datums, inspection points)?
- Can features be inspected? (internal cavity with no access = can't measure = can't verify)

**Real example:**
- ❌ **Bad:** Specifying ±0.01mm tolerance on plasma-cut edge (process incapable)
- ✓ **Good:** ±0.5mm tolerance on plasma-cut perimeter, ±0.05mm on milled mounting holes (matched to process)

**4. Production Efficiency: "Can we make this quickly and repeatably?"**

Efficiency factors:
- **Automation potential:** Can parts be batch-processed? Can robot load/unload?
- **Fixturing:** Does part self-locate, or require complex custom fixtures?
- **Inspection:** Are critical dimensions easy to measure with standard tools?
- **Assembly:** If multi-part, does it assemble easily or require precise alignment jigs?

**Real example:**
- ❌ **Bad:** Asymmetric part with no obvious "this side up" features (assembly errors, slow)
- ✓ **Good:** Keyed features (one pin larger, offset holes) that only fit one way (foolproof, fast)

### Common CAD Mistakes That Impact Manufacturing

Even experienced designers make these mistakes. Learn to spot them early:

**Geometric Issues (Shape problems):**

| Mistake | Why It's a Problem | Fix |
|---------|-------------------|-----|
| Sharp internal corners (0 radius) | Rotating cutting tools are round—can't cut sharp internal corners | Add radius ≥ tool radius (typically 1.5-3mm) |
| Walls thinner than 2mm (metal) | Thin walls flex during cutting, causing poor accuracy, tool breakage | Increase to ≥2mm (aluminum) or ≥3mm (steel) |
| Deep narrow pockets (depth > 3× width) | Tool deflection, chatter, slow cutting, potential breakage | Widen pocket or reduce depth if possible |
| Undercuts (features requiring 5-axis or special tools) | Requires expensive multi-axis machining or EDM | Redesign to eliminate or split into multiple parts |
| Holes smaller than material thickness (plasma/laser) | Heat can't dissipate, kerf too wide for feature | Holes ≥ material thickness, or drill in secondary op |

**Specification Issues (Communication problems):**

| Mistake | Why It's a Problem | Fix |
|---------|-------------------|-----|
| Everything toleranced ±0.01mm | Precision costs money; over-spec = overpaying | Only critical features get tight tolerances |
| No tolerances specified | Machinist guesses; parts might not fit | Use general tolerance note + specific callouts for critical dims |
| "Make it smooth" (vague finish spec) | Smooth to whom? What Ra value? | Specify surface finish in Ra (e.g., "3.2 µm Ra" or "125 µin Ra") |
| Missing material spec | Shop guesses or asks, delaying production | Always specify material (e.g., "AL 6061-T6", "Steel 1018") |
| Dimensions to hidden features | Can't measure, can't verify | Dimension to visible, accessible features |

**Process Mismatch (Using wrong process for feature):**

| Mistake | Why It's a Problem | Better Approach |
|---------|-------------------|----------------|
| Plasma-cut part with ±0.1mm tolerance | Plasma capable of ±0.5mm typically | Use laser (±0.1mm) or mill critical features after plasma rough-cut |
| Mirror-polished waterjet edge | Waterjet leaves abrasive texture (~3-6 µm Ra) | Specify "as-cut" or plan secondary grinding/polishing |
| Tight tolerance perpendicular to FDM layers | Layer adhesion varies; weak and inaccurate in Z | Orient part so critical dimensions are in XY plane (parallel to layers) |
| Mixing processes without thought | Some combos work great, others create problems | Understand process strengths (e.g., waterjet rough-cut + milling finish = excellent) |

**Real-world example of cascading mistakes:**

A designer creates a motor mount bracket:
1. ❌ Sharp internal corners (geometric issue)
2. ❌ All dimensions ±0.01mm (over-toleranced)
3. ❌ Specified for plasma cutting (process mismatch—plasma can't achieve ±0.01mm)
4. ❌ No material specified (specification issue)

**Result:** Quote comes back 10× higher than expected. Machinist explains sharp corners need EDM, tight tolerances require post-plasma milling, and they need material clarification before quoting.

**Better approach:** Same bracket with:
1. ✓ 3mm corner radii (standard 6mm endmill)
2. ✓ ±0.5mm general tolerance, ±0.1mm on mounting holes only
3. ✓ Laser-cut profile + milled holes (appropriate processes)
4. ✓ Material: AL 6061-T6, 6mm plate

**Result:** Part made in 10 minutes, costs 1/10th the original design, performs identically.

## Learning Objectives

By the end of this module, you will be able to:

1. **Create CAD models with proper design intent** that capture both form and function
2. **Apply parametric modeling techniques** for efficient design iterations and part families
3. **Implement DFM principles** specific to milling, turning, plasma, laser, waterjet, and additive processes
4. **Select appropriate tolerances** based on process capabilities and functional requirements
5. **Use GD&T (Geometric Dimensioning and Tolerancing)** to communicate design intent unambiguously
6. **Choose materials** that balance performance, manufacturability, and cost
7. **Design assemblies** that optimize both part manufacture and assembly operations
8. **Generate complete engineering documentation** including drawings, BOMs, and specifications
9. **Prepare CAD models for CAM** with proper feature recognition and work coordinate setup
10. **Leverage advanced techniques** like simulation, topology optimization, and multi-body design

## CAD Software Landscape

### Open-Source Options

**FreeCAD**
- Fully parametric 3D CAD modeler
- Excellent for learning fundamental concepts
- Active community and extensive documentation
- Modules for mechanical design, sheet metal, FEM analysis
- Python scripting for automation
- **Best for:** Educational environments, Linux users, customization

**LibreCAD**
- 2D CAD for technical drawings
- Good for plasma/laser/waterjet flat pattern design
- DXF/DWG compatibility
- **Best for:** 2D cutting operations, legacy file compatibility

### Commercial Options (with free/student licenses)

**Fusion 360 (Autodesk)**
- Integrated CAD/CAM/CAE platform
- Cloud-based collaboration
- Excellent for hobbyists and small shops
- Built-in toolpath generation
- **Best for:** All-in-one workflow, beginners to intermediate users

**SolidWorks (Dassault Systèmes)**
- Industry-standard parametric modeler
- Extensive material and simulation libraries
- Large community and training resources
- **Best for:** Professional environments, complex assemblies

**Inventor (Autodesk)**
- Strong sheet metal and weldment capabilities
- Integrated stress analysis
- **Best for:** Mechanical design, frame structures

**Onshape**
- Cloud-native CAD (runs in web browser)
- Real-time collaboration
- Version control built-in
- **Best for:** Distributed teams, Chromebook users

### Specialized Tools

**OpenSCAD**
- Script-based parametric modeler
- Excellent for algorithmic design
- **Best for:** Programmers, parametric part families

**Blender (with CAD add-ons)**
- Primarily for artistic modeling
- Can be adapted for technical work
- **Best for:** Organic shapes, visualization

## Module Structure and Approach

This module follows a progressive learning path:

**Sections 16.2-16.3:** Foundational CAD skills (sketching, constraints, parametric modeling)

**Sections 16.4-16.6:** Manufacturing-focused design (DFM, tolerancing, material selection)

**Section 16.7:** Process-specific optimization for each CNC technology

**Sections 16.8-16.9:** Documentation and communication (assemblies, drawings)

**Sections 16.10-16.11:** Advanced integration (CAM preparation, simulation)

**Section 16.12:** Synthesis and real-world application

### Hands-On Projects Throughout

Each section includes practical exercises:
- Simple bracket optimization (Section 16.4)
- Tolerance stack-up analysis (Section 16.5)
- Multi-process part design (Section 16.7)
- Complete assembly with documentation (Section 16.8-16.9)
- CAD-to-CAM workflow (Section 16.10)

## The Designer's Mindset

The difference between an amateur and professional designer isn't software skill—it's **thinking about manufacturing while designing**. Here's how to rewire your brain:

### Think in Manufacturing Operations, Not Just Geometry

When you add a feature in CAD, mentally simulate how it will be made:

**Example: Adding a 10mm diameter hole**

**Amateur thinks:** "I need a hole here. [Draws circle, extrudes cut]. Done."

**Professional thinks:**
- "10mm hole... that's a standard drill size, good."
- "Is it through or blind? Through is faster (no depth control, better chip evacuation)."
- "Can I access it from the top? Or do I need a second setup?"
- "Are there other holes? Can I drill them in the same setup with same tool?"
- "Does it need tight tolerance? If yes, should I drill 9.5mm then ream to 10mm H7?"

**Result:** Professional's design takes 30 seconds to drill. Amateur's design might require special tooling, multiple setups, or be impossible to make.

### Design with Tolerances in Mind (Real Parts Aren't Perfect)

Your CAD model shows a 50.000mm dimension. In reality, you'll get:
- Plasma cut: 49.5 to 50.5 mm (±0.5mm typical)
- Laser cut: 49.9 to 50.1 mm (±0.1mm typical)
- CNC milled: 49.95 to 50.05 mm (±0.05mm typical)
- Precision ground: 49.99 to 50.01 mm (±0.01mm typical)

**Design principle:** Parts will vary. Design so that variation doesn't matter (or only specify tight tolerances where absolutely necessary).

**Example: Motor mount plate**
- Motor bolt holes: ±0.05mm (must align with motor mounting pattern)
- Overall plate size: ±0.5mm (doesn't matter, cosmetic)
- Plate thickness: ±0.2mm (doesn't matter, just needs to be strong enough)

**Cost impact:**
- If you tolerance everything ±0.01mm: $200 part (precision grinding required)
- If you tolerance intelligently: $20 part (standard milling)
- **Same function, 10× cost difference**

### Communicate Intent, Not Just Shape

Your CAD model and drawing should answer: **"What matters and why?"**

**Poor communication:**
- Every dimension specified to 3 decimal places
- No indication which features are critical
- Machinist has no idea what matters, so they either:
  - Over-inspect everything (expensive, slow)
  - Under-inspect (parts don't function)

**Good communication:**
- General tolerance note: "±0.2mm unless noted"
- Critical features marked: "⌀6.00 +0.02/0 (bearing fit—critical)"
- Datums specified: "Measure all dimensions from datum A (mounting surface)"
- Notes where helpful: "Holes A-B distance critical for motor alignment"

**Example note on a drawing:**
```
CRITICAL DIMENSIONS:
- Shaft hole ⌀20.00 H7 (bearing fit)
- Hole pattern 80×60 ±0.05 (motor mount interface)

NON-CRITICAL:
- Overall bracket dimensions (clearance only)
- Cosmetic chamfers (0.5mm nominal)
```

**Result:** Machinist knows exactly what matters, focuses inspection efforts appropriately, part costs less and functions correctly.

### Iterate Based on Manufacturing Feedback (First Design Is Never Best)

**Common designer trap:** "I spent 20 hours on this design, it's perfect, don't change it."

**Reality:** The person making the part often has insights you missed.

**Example conversation:**

**Designer:** "Here's my bracket design. All pockets are 15mm deep."

**Machinist:** "Why 15mm? That requires a deep-reach tool and slow cutting. If we made them 12mm deep, I could use a standard tool and cut them 3× faster. Does the part really need 15mm depth?"

**Designer:** "Let me check... actually no, 10mm would be fine structurally."

**Machinist:** "Perfect. 10mm I can machine with a stubby tool, very rigid, fast, cheap. Part will cost half as much."

**Designer:** [Updates CAD, notes for future: check pocket depths against tool availability]

### Balance Ideal vs. Practical

Sometimes the "perfect" design is too expensive to justify.

**Example: Lightweight bracket for robot arm**

**Ideal design (topology optimized):**
- Organic, flowing shapes
- 200g (lightest possible)
- Requires 5-axis machining
- **Cost: $800 per part**

**Practical design (simplified):**
- Straight ribs approximating topology result
- 280g (40% heavier, but still adequate)
- Requires 3-axis machining (2 setups)
- **Cost: $60 per part**

**Decision:** For a one-off robot? Maybe worth $800. For a product you'll make 100 of? The practical design saves $74,000 and delivers 95% of the performance.

**Good designers make these trade-offs consciously, documenting why decisions were made.**

## Looking Ahead

The following sections will build your skills systematically, from fundamental CAD techniques through advanced manufacturing optimization. Each concept will be reinforced with examples from real-world CNC applications, drawing on the processes covered throughout this course.

Remember: **The goal isn't just to create 3D models—it's to create manufacturable parts that perform their function reliably and economically.**

***

**Next:** [Section 16.2: CAD Fundamentals](section-16.2-cad-fundamentals.md)

**Previous Module:** [Module 15: G-code Programming](../Module-15/module-15-gcode.md)

---

# Section 16.6: Material Selection for Design

## Introduction

Material selection profoundly impacts both part performance and manufacturability. The "best" material balances functional requirements (strength, weight, corrosion resistance) with manufacturing constraints (machinability, availability, cost). This section guides you through the material selection process, emphasizing how material properties influence CAD design decisions and manufacturing processes.

### Why Material Selection Matters: Real-World Cost Impact

**Scenario 1: Over-Engineering the Material**

**Designer A's Approach (Amateur):**
- Bracket needs 200 MPa yield strength (safety factor already included)
- Chooses **304 Stainless Steel** (yield: 215 MPa) because "stainless is durable"
- Dimensions: 100mm × 50mm × 10mm bracket

**Cost breakdown:**
- Material: $4.00/kg × 0.393kg = **$1.57**
- Machining time: **45 minutes** (stainless is tough, work-hardens, requires slow feeds)
- Machine rate: $80/hr → **$60.00**
- Tool wear: **+$5.00** (carbide inserts wear faster on stainless)
- **Total: $66.57 per part**

**Designer B's Approach (Professional):**
- Same requirements: 200 MPa yield strength needed
- Chooses **Aluminum 7075-T6** (yield: 503 MPa) - exceeds requirements AND excellent machinability
- Same dimensions: 100mm × 50mm × 10mm bracket

**Cost breakdown:**
- Material: $8.00/kg × 0.135kg = **$1.08**
- Machining time: **15 minutes** (aluminum cuts easily, high speeds possible)
- Machine rate: $80/hr → **$20.00**
- Tool wear: **+$0.50** (minimal aluminum wear)
- **Total: $21.58 per part**

**Result: $45 saved per part (67% cost reduction) with BETTER strength (503 MPa vs 215 MPa)!**

**Scenario 2: Material Cost vs Total Cost**

Many designers focus only on material cost per kg and miss the total picture:

| Material | Cost/kg | Part Material Cost | Machining Time | Machining Cost | Tool Wear | **TOTAL COST** |
|----------|---------|-------------------|----------------|----------------|-----------|----------------|
| **Mild Steel 1018** | $2.50 | $0.98 | 30 min | $40 | $2 | **$42.98** |
| **Aluminum 6061-T6** | $4.50 | $1.22 | 12 min | $16 | $0.50 | **$17.72** |
| **304 Stainless** | $4.00 | $1.57 | 45 min | $60 | $5 | **$66.57** |

**Critical insight: Material cost is only 2-5% of total part cost. Machinability dominates.**

Aluminum has the HIGHEST material cost ($4.50/kg) but LOWEST total cost ($17.72) because it machines so quickly. Steel looks cheap at $2.50/kg but total cost is 2.4× higher than aluminum!

## Material Selection Criteria

### Functional Requirements

**Mechanical Properties:**
- **Strength:** Tensile, compressive, shear (load-bearing applications)
- **Stiffness:** Elastic modulus (deflection-critical applications)
- **Hardness:** Wear resistance, indentation resistance
- **Toughness:** Impact resistance, fracture resistance
- **Fatigue resistance:** Cyclic loading applications

**Physical Properties:**
- **Density:** Weight-critical applications (aerospace, robotics)
- **Thermal conductivity:** Heat sinks, thermal barriers
- **Thermal expansion:** Dimensional stability across temperatures
- **Electrical conductivity:** Grounding, shielding, current-carrying

**Environmental Resistance:**
- **Corrosion resistance:** Outdoor use, chemical exposure
- **UV resistance:** Sunlight exposure
- **Temperature range:** Operating environment (cryogenic to high-temp)
- **Chemical compatibility:** Specific chemicals, solvents, oils

### Manufacturing Considerations

**Machinability:**
- Cutting forces required
- Tool wear rate
- Achievable surface finish
- Achievable tolerances
- Chip formation and evacuation

**Material Availability:**
- Standard stock sizes (plate, bar, tube, sheet)
- Lead times and supply chain reliability
- Minimum order quantities
- Geographic availability

**Cost:**
- Raw material cost per kg/pound
- Machining cost (time × tooling wear)
- Scrap value (recyclability)
- Total cost of ownership

**Secondary Processes:**
- Heat treatment requirements
- Surface coating/finishing needs
- Weldability / joinability
- Post-processing complexity

## Common Engineering Materials

### Metals - Aluminum Alloys

**Advantages:**
- Lightweight (2.7 g/cm³, 1/3 weight of steel)
- Excellent machinability (high material removal rates)
- Good corrosion resistance (natural oxide layer)
- Wide range of alloys for different properties
- Recyclable with minimal property loss

**Disadvantages:**
- Lower strength than steel (alloy-dependent)
- Lower stiffness (E = 69 GPa vs steel's 200 GPa)
- Poor elevated temperature performance (>150°C)
- Galvanic corrosion with dissimilar metals

**Common Alloys:**

| Alloy | Properties | Applications | Machinability |
|-------|-----------|--------------|---------------|
| **6061-T6** | General purpose, weldable, corrosion resistant | Structural frames, brackets, general components | Excellent |
| **7075-T6** | High strength, aerospace grade | High-stress components, aerospace | Good |
| **2024-T3** | High strength, poor weld ability | Aircraft structures, high-stress parts | Good |
| **5052-H32** | Excellent corrosion resistance, formable | Sheet metal, marine environments | Good |
| **MIC-6** | Cast plate, low internal stress, very flat | Precision plates, tooling, machine beds | Excellent |

**Design Considerations for Aluminum:**
- Requires thicker cross-sections than steel for equivalent stiffness
- Excellent for heat sinks (thermal conductivity 205 W/m·K)
- Anodizing provides enhanced corrosion/wear resistance
- Threading: use thread inserts for high-cycle or high-load applications

### Metals - Steel Alloys

**Advantages:**
- High strength and stiffness
- Wide range of properties via heat treatment
- Magnetic (useful for fixturing)
- Low cost (carbon steel)
- Excellent weldability

**Disadvantages:**
- Heavy (7.85 g/cm³)
- Corrosion susceptibility (carbon steel)
- Lower machinability than aluminum (harder, generates more heat)

**Common Alloys:**

| Alloy | Properties | Applications | Machinability |
|-------|-----------|--------------|---------------|
| **1018 (Mild Steel)** | Low carbon, easy to weld, low cost | Structural, non-critical parts | Good |
| **1045** | Medium carbon, higher strength | Shafts, gears, general machine parts | Fair |
| **4140** | Alloy steel, heat treatable to high hardness | High-stress shafts, tooling, wear parts | Fair (annealed), Poor (hardened) |
| **304 Stainless** | Corrosion resistant, non-magnetic (austenitic) | Food equipment, marine, chemical | Fair (work-hardens) |
| **316 Stainless** | Superior corrosion resistance (molybdenum) | Marine, chemical, medical | Fair (work-hardens) |
| **17-4 PH Stainless** | High strength + corrosion resistance, heat treatable | Aerospace, pump shafts, marine hardware | Fair |

**Design Considerations for Steel:**
- Design for appropriate stock sizes (common: 1/4", 1/2", 3/4", 1" plate; 1/2", 1", 2" bar)
- Stainless requires higher cutting forces, sharp tools, generous coolant
- Carbon steel requires corrosion protection (paint, plating, oil)
- Heat treatment distortion: leave stock for final grinding if tight tolerances needed

### Metals - Brass and Bronze

**Brass (Copper + Zinc):**
- Excellent machinability (free-cutting grades)
- Good corrosion resistance
- Decorative appearance
- Low friction (bearing applications)
- Non-sparking (explosive environments)

**Bronze (Copper + Tin/Aluminum/other):**
- Superior wear resistance vs brass
- Excellent for bearings, bushings
- Good corrosion resistance
- More expensive than brass

**Common Alloys:**

| Alloy | Composition | Applications | Machinability |
|-------|------------|--------------|---------------|
| **360 Brass** | 61% Cu, 3% Pb | Free-machining, fittings, valves | Excellent |
| **C932 Bearing Bronze** | Cu-Sn-Ni | Bearings, bushings, wear surfaces | Good |
| **Aluminum Bronze** | Cu-Al | Marine hardware, high-strength bushings | Fair |

**Design Considerations:**
- Excellent for complex features (intricate shapes machine easily in brass)
- Natural lubricity: ideal for sliding contact
- Relatively expensive (copper cost)
- Low strength compared to steel/aluminum

### Plastics - Engineering Thermoplastics

**Advantages:**
- Lightweight
- Corrosion and chemical resistant
- Electrical insulation
- Low friction (some grades)
- Lower machining forces
- Wide color options (molded/extruded)

**Disadvantages:**
- Lower strength and stiffness than metals
- Thermal expansion (5-10× greater than metals)
- Creep under sustained load
- Temperature sensitivity
- Machining challenges (melting, gummy chips)

**Common Engineering Plastics:**

| Material | Properties | Applications | Machinability |
|----------|-----------|--------------|---------------|
| **Acetal (Delrin)** | High stiffness, low friction, good moisture resistance | Gears, bearings, structural parts | Excellent |
| **Nylon (PA)** | Tough, wear-resistant, chemical resistant | Gears, bushings, rollers | Good (moisture-sensitive) |
| **UHMW-PE** | Ultra-low friction, impact resistant | Sliding surfaces, liners, guides | Good (soft, requires sharp tools) |
| **Acrylic (PMMA)** | Transparent, rigid, scratch-resistant | Windows, light guides, displays | Excellent |
| **Polycarbonate (PC)** | High impact resistance, transparent | Safety shields, electronics housings | Good (requires low heat) |
| **PEEK** | High temp (260°C), high strength, chemical resistant | Aerospace, medical, high-performance | Fair (expensive, specialized) |
| **PTFE (Teflon)** | Extreme chemical resistance, lowest friction | Chemical equipment, non-stick surfaces | Poor (soft, tears easily) |

**Design Considerations for Plastics:**
- Account for thermal expansion (design clearances accordingly)
- Minimize thin walls (warping during machining/cooling)
- Use generous radii (stress concentrations more critical due to lower toughness)
- Sharp tools essential (dull tools melt plastic)
- Thread inserts for repeated assembly (molded or heat-set)

### Composites - Carbon Fiber and Fiberglass

**Carbon Fiber (CFRP):**
- Extremely high strength-to-weight ratio
- High stiffness-to-weight ratio
- Anisotropic properties (directional strength)
- Expensive
- Difficult to machine (abrasive, requires carbide/diamond tools)

**Fiberglass (GFRP):**
- Good strength-to-weight ratio
- Lower cost than carbon fiber
- Corrosion resistant
- Electrical insulation

**Design Considerations:**
- Typically molded/laid up, not machined from stock
- Machining used for trimming edges, drilling holes
- Drilling requires backer plate (prevent delamination)
- Specialized tooling (carbide/diamond)
- Dust hazards (health precautions required)

## Material Properties and CAD Design

### Strength and Safety Factors

**Basic stress calculation:**
```
Stress (σ) = Force / Area

Safety Factor (SF) = Material Yield Strength / Applied Stress
```

**Typical safety factors:**
- Static load, known materials, non-critical: SF = 1.5-2
- Dynamic load, well-characterized: SF = 2-3
- Unknown loads, critical application: SF = 3-5
- Impact/shock loading: SF = 5-10

**CAD implications:**
- Lower strength materials require thicker cross-sections
- FEA (Finite Element Analysis) helps optimize material distribution
- Parametric models allow quick material substitution with automatic resizing

### Stiffness and Deflection

**Deflection of beam under load:**
```
Deflection (δ) ∝ (Force × Length³) / (Elastic Modulus × Moment of Inertia)
```

**Key insight:** Geometry (moment of inertia) has greater impact than material elastic modulus.

**Example:**
```
Aluminum beam (E = 69 GPa): δ = 10 mm
Steel beam (same dimensions, E = 200 GPa): δ = 3.45 mm (2.9× stiffer)
Aluminum I-beam (same weight as solid steel): δ = 0.5 mm (20× stiffer!)
```

**CAD design strategy:**
- Don't just swap materials—optimize geometry
- Use ribs, gussets, I-beams, tubes instead of solid sections
- CAD sketches should reference elastic modulus parameter for deflection-critical designs

### Thermal Expansion Management

**Coefficient of Thermal Expansion (CTE):**

| Material | CTE (µm/m·°C) | 100mm part, 50°C ΔT |
|----------|---------------|---------------------|
| Aluminum 6061 | 23.6 | +0.118 mm |
| Steel (carbon) | 11.7 | +0.059 mm |
| Stainless 304 | 17.3 | +0.087 mm |
| Brass | 18.7 | +0.094 mm |
| Acetal (Delrin) | 106 | +0.530 mm |
| Nylon | 80 | +0.400 mm |

**Design implications:**

**Large structures:**
```
Aluminum frame, 1000mm long, 50°C temperature change:
  ΔL = 1000 × 23.6 × 50 / 1,000,000 = 1.18 mm growth

Design solutions:
  - Slotted mounting holes (allow movement)
  - Flexures or spring-loaded connections
  - Symmetrical expansion about center datum
```

**Mixed-material assemblies:**
```
Aluminum plate (CTE = 23.6) + steel fasteners (CTE = 11.7):
  Differential expansion causes stress

Design solutions:
  - Oversized clearance holes in aluminum
  - Belleville washers to maintain clamp load
  - Isolation bushings
```

**Precision applications:**
```
Use low-expansion materials:
  - Invar (CTE = 1.2) for metrology, optics
  - Titanium (CTE = 8.6) for aerospace
  - Carbon fiber (CTE ~0 in fiber direction)
```

### Machinability Index

**Relative machining cost (100 = free-machining brass):**

| Material | Machinability Rating | Tool Wear | Notes |
|----------|---------------------|-----------|-------|
| Free-cutting brass (360) | 100 | Very low | Benchmark material |
| Aluminum 6061-T6 | 90 | Low | Fast cutting, excellent finish |
| Aluminum 7075-T6 | 70 | Low | Harder than 6061 |
| Mild steel (1018) | 70 | Moderate | Higher cutting forces than Al |
| 4140 steel (annealed) | 55 | Moderate | Heat treatable |
| 304 Stainless | 45 | High (work-hardens) | Requires sharp tools |
| 316 Stainless | 40 | High | More difficult than 304 |
| Titanium (Ti-6Al-4V) | 30 | Very high | Specialized tooling/techniques |
| Inconel (nickel superalloy) | 15 | Extreme | Very slow, expensive |
| Acetal (Delrin) | 95 | Very low | Excellent plastic machinability |
| Nylon | 80 | Low | Moisture affects properties |
| Polycarbonate | 75 | Low | Requires low heat |

**Real-World Manufacturing Time Comparison**

**Part: 150mm × 100mm × 25mm block with 6 pockets (identical geometry, different materials)**

| Material | Rough Milling | Finish Milling | Tool Changes | Total Time | Cost @ $80/hr |
|----------|--------------|----------------|--------------|------------|---------------|
| **Aluminum 6061** | 18 min | 7 min | 1 | **25 min** | **$33** |
| **Brass 360** | 15 min | 6 min | 1 | **21 min** | **$28** |
| **Mild Steel 1018** | 28 min | 12 min | 2 | **40 min** | **$53** |
| **304 Stainless** | 55 min | 22 min | 3 | **77 min** | **$103** |
| **Titanium Ti-6Al-4V** | 120 min | 45 min | 6 | **165 min** | **$220** |
| **Inconel 718** | 280 min | 95 min | 12 | **375 min** | **$500** |

**Key insights:**
- **Stainless takes 3× longer than aluminum** (77 min vs 25 min)
- **Titanium takes 6.6× longer than aluminum** (165 min vs 25 min)
- **Inconel takes 15× longer than aluminum!** (375 min vs 25 min)

**Design impact:**
- Difficult-to-machine materials favor simpler geometries
- Complex features in Inconel = prohibitive cost
  - **Example:** 10-pocket design in aluminum = $75; same part in Inconel = $1,200 (16× cost!)
- Same features in aluminum = reasonable cost

## Material Availability and Stock Sizes

### Standard Forms

**Plate:**
- Thickness: 1/16", 1/8", 1/4", 3/8", 1/2", 3/4", 1", 1.5", 2" (and metric equivalents)
- Sheet size: 48" × 96" (4'×8'), 60" × 120" common

**Bar (Rectangular):**
- Common sizes: 1/4" × 1", 1/2" × 2", 1" × 1", etc.
- Lengths: 12 ft (144"), 6 ft (72") common

**Rod (Round):**
- Diameters: 1/4", 3/8", 1/2", 5/8", 3/4", 1", 1.25", 1.5", 2", etc.
- Lengths: 12 ft, 6 ft common

**Tube (Round):**
- OD × Wall: 1" OD × 0.065" wall, 2" OD × 0.125" wall, etc.
- Lengths: 12 ft, 6 ft common

**Tube (Square/Rectangular):**
- Sizes: 1"×1"×0.065", 2"×1"×0.125", etc.

### Design for Stock Sizes

**Good Practice (Professional Designer):**
```
Design part: 48mm thick
→ Use 50mm plate stock (standard), machine both sides to 48mm
→ Minimal waste: 4% material waste

Design part: 19mm diameter shaft
→ Use 20mm rod stock (standard), turn to 19mm
→ Minimal waste: 10% material waste
```

**Poor Practice (Amateur Designer):**
```
Design part: 73mm thick
→ No standard stock size!
→ Option A: Use 75mm plate (custom order, 8-week lead time, $450 minimum)
→ Option B: Use 80mm plate ($95 vs $65 for 75mm), 10% waste
→ Option C: Laminate 50mm + 25mm plates (adds welding, stress relief, $200 extra)

Design part: 17.5mm diameter shaft
→ No standard stock size!
→ Must machine from 20mm stock: 33% material waste
```

**Real-World Cost Comparison:**

**Part: Custom mounting plate**

| Design Choice | Stock Size | Stock Cost | Material Waste | Lead Time | Total Cost |
|--------------|------------|------------|----------------|-----------|------------|
| **73mm thick (poor)** | 80mm custom | $95 | 10% ($9.50) | 8 weeks | **$104.50** |
| **48mm thick (good)** | 50mm standard | $32 | 4% ($1.28) | In stock | **$33.28** |

**Result: 69% cost reduction + immediate availability by designing for standard stock!**

**CAD Parametric Approach:**
```python
# Define standard stock as parameter
stock_thickness = 50 mm    # Standard stock size (parameter)
finish_allowance = 1 mm     # Per side
final_thickness = stock_thickness - 2 * finish_allowance  # = 48 mm

# All features reference final_thickness
pocket_depth = final_thickness - 10 mm  # Updates automatically
```

**Benefits:**
- Change `stock_thickness = 75 mm` → entire design updates to 73mm final thickness
- Quickly explore different stock sizes to find best cost/performance balance
- Design intent captured: "Use standard stock, leave 1mm per side for finish"

## Material Selection Process

### Real-World Example: Robotic Arm Bracket

**Application:** Mounting bracket for robotic arm servo motor
**Environment:** Indoor manufacturing facility, room temperature
**Production volume:** 100 units

### Step 1: Define Requirements

**Create requirements matrix:**

| Requirement | Target | Minimum Acceptable | Why |
|-------------|--------|-------------------|-----|
| Tensile strength | 400 MPa | 300 MPa | Supports 50kg load with SF=3 |
| Elastic modulus | 70 GPa | 60 GPa | Max deflection <0.5mm |
| Density | <3 g/cm³ | <5 g/cm³ | Robot arm weight-sensitive |
| Corrosion resistance | Good | Fair | Indoor use, occasional cleaning |
| Operating temp | -10 to 60°C | 0 to 50°C | Factory environment |
| Machinability | Good | Fair | Complex geometry with pockets |
| Cost target | <$30/part | <$50/part | Budget constraint |

### Step 2: Screen Candidate Materials

**Eliminate materials that fail minimum requirements:**
```
✗ Mild steel 1018: Yield strength 250 MPa (FAIL: below minimum 300 MPa)
✗ Nylon 6: Elastic modulus 3 GPa (FAIL: below minimum 60 GPa)
✗ Acetal: Elastic modulus 3.1 GPa (FAIL: below minimum 60 GPa)
✓ Aluminum 6061-T6: Yield 276 MPa (marginal), E = 69 GPa (meets target), density 2.7 g/cm³ (excellent)
✓ Aluminum 7075-T6: Yield 503 MPa (exceeds!), E = 71.7 GPa (meets target), density 2.81 g/cm³ (excellent)
✓ Stainless 304: Yield 215 MPa (FAIL: below minimum 300 MPa) - ELIMINATED
✓ 4140 Steel: Yield 415 MPa (meets), E = 205 GPa (exceeds), density 7.85 g/cm³ (FAIL: too heavy)
```

**Remaining candidates:** Aluminum 6061-T6, Aluminum 7075-T6

### Step 3: Rank Candidates with Cost Analysis

**Weighted scoring (1-10 scale):**

| Material | Strength (30%) | Stiffness (20%) | Weight (20%) | Machinability (20%) | Cost (10%) | **Total Score** |
|----------|----------------|-----------------|--------------|---------------------|------------|-----------------|
| **Al 6061-T6** | 6 (marginal) | 7 (good) | 9 (excellent) | 9 (excellent) | 10 (best) | **7.5** |
| **Al 7075-T6** | 10 (exceeds) | 7 (good) | 9 (excellent) | 7 (good) | 6 (higher) | **8.2** |

**Detailed cost analysis:**

| Material | Part Volume | Material Cost | Machining Time | Machining Cost | Tool Wear | **Total** |
|----------|------------|---------------|----------------|----------------|-----------|-----------|
| **Al 6061-T6** | 180 cm³ | $2.20 | 22 min | $29.33 | $0.75 | **$32.28** |
| **Al 7075-T6** | 180 cm³ | $4.10 | 28 min | $37.33 | $1.20 | **$42.63** |

**Decision Point:**

- **6061-T6 score: 7.5** - Marginal strength (276 MPa), but **meets $30 target cost**
- **7075-T6 score: 8.2** - Excellent strength (503 MPa), but **$42.63 exceeds $30 target**

**Professional Analysis:**
```
Safety Factor check with 6061-T6:
  Required: 300 MPa minimum
  Actual: 276 MPa
  → FAILS minimum requirement by 8%

Decision: Must use 7075-T6 despite higher cost
  → Negotiate budget increase or redesign to reduce stress
```

**Final Decision: Aluminum 7075-T6**
- Meets all requirements with margin
- Cost: $42.63 per part (need budget approval for $12.63 overage)
- Alternative: Redesign bracket with ribs to reduce stress → might allow 6061-T6

### Step 4: Prototype and Validate

**Prototype Results:**
- Built 3 prototypes in Al 7075-T6
- Load testing: Applied 75kg (1.5× design load)
- Measured deflection: **0.32mm** (target: <0.5mm) ✓
- Stress concentration near mounting hole: **420 MPa** (material yield: 503 MPa) ✓
- **Conclusion: Design validated, proceed with production**

**Cost for 100-unit production:**
- Per-part cost: $42.63
- Setup cost (one-time): $350
- **Total: $4,613** ($46.13 per part including setup)

## Material-Specific Design Guidelines

### Designing with Aluminum

**Optimize for:**
- Thin walls with ribs (lightweight + rigid)
- Large pockets (easy material removal)
- Anodized finishes (specify type II or type III hardcoat)

**Real-World Example: Aluminum Enclosure Design**

**Amateur Design (solid construction):**
- 200mm × 150mm × 80mm solid-walled enclosure
- Wall thickness: 10mm everywhere
- Weight: 1,240g
- Material cost: $33.50
- Machining time: 65 minutes → $86.67
- **Total: $120.17**

**Professional Design (ribbed construction):**
- Same external dimensions
- Wall thickness: 3mm with 5mm ribs every 40mm
- Weight: 420g (66% lighter!)
- Material cost: $11.35 (66% savings)
- Machining time: 42 minutes (less material removal) → $56.00
- **Total: $67.35**

**Result: $52.82 saved per part (44% cost reduction) + 820g weight savings!**

**Avoid:**
- Thin unsupported walls (<2mm without ribs) → **Consequence:** Warping during machining, chatter marks
- Sharp inside corners (stress concentrations, tool access) → **Consequence:** Requires EDM ($150+ extra) or stress risers
- Direct steel contact (galvanic corrosion; use isolators) → **Consequence:** White corrosion powder forms, parts seize

**Thread Considerations:**

| Application | Thread Type | Cost | Strength | Use When |
|------------|-------------|------|----------|----------|
| Low-cycle assembly (<10×) | Tapped aluminum (1.5× depth) | $2 | Fair | Non-critical fastening |
| Medium-cycle (<100×) | Helicoil insert | $4 | Good | Frequent access panels |
| High-cycle or high-load | Threaded insert (PEM, etc.) | $6 | Excellent | Hinges, adjustments |

**Example:**
- M6 threads in 6061-T6 aluminum, 12mm engagement
- Direct tapping: Fails after ~50 assembly cycles
- Helicoil insert: Survives 500+ cycles (10× improvement, +$2 cost)

### Designing with Steel

**Optimize for:**
- Solid construction (strength advantage over aluminum)
- Welded assemblies (excellent weldability)
- Magnetic properties (holding, sensors)

**Avoid:**
- Unnecessary mass (heavy; optimize with pockets, holes)
- Thin stainless walls (work-hardens during machining)

**Corrosion protection:**
- Specify finish: paint, powder coat, zinc plate, chrome plate, or choose stainless

### Designing with Plastics

**Optimize for:**
- Smooth contours (low friction, self-lubricating)
- Electrical insulation
- Corrosion/chemical exposure
- Reduced weight

**Real-World Example: Sliding Guide Block**

**Metal Version (Aluminum 6061):**
- 50mm × 40mm × 20mm guide block
- Requires lubrication (grease every 500 cycles)
- Weight: 108g
- Material + machining: $18.50
- **Maintenance cost:** $120/year (labor for re-lubrication)

**Plastic Version (Acetal/Delrin):**
- Same dimensions
- Self-lubricating (no maintenance)
- Weight: 36g (67% lighter!)
- Material + machining: $12.30
- **Maintenance cost:** $0/year

**5-year total cost:**
- Aluminum: $18.50 + (5 × $120) = **$618.50**
- Acetal: $12.30 + $0 = **$12.30**
- **Savings: $606.20 (98% reduction!)** for appropriate plastic application

**Avoid:**
- Tight tolerances without specifying conditions → **Consequence:** Part dimensions change with temperature/humidity
  - Example: ⌀25.00mm Delrin shaft at 20°C → ⌀25.13mm at 45°C (out of tolerance!)
- Sharp corners (stress concentration critical) → **Consequence:** Crack initiation, brittle failure
- Thin sections prone to warping → **Consequence:** Part warps during machining from internal stresses

**Account for Thermal Expansion:**

**Example calculation:**
```
Delrin guide rail: 200mm long
CTE: 106 µm/m·°C
Temperature range: 15°C to 45°C (ΔT = 30°C)

Expansion = 200mm × (106/1,000,000) × 30°C = 0.636mm

Design clearance = 0.5mm (nominal) + 0.636mm (thermal) = 1.14mm minimum
```

**Poor Design:** 200mm rail with 0.5mm clearance → Binds at high temperature
**Good Design:** 200mm rail with 1.2mm clearance → Functions across full temperature range

**Practical guideline for plastic assemblies:**
- **Room temperature only:** Standard tolerances (±0.1mm)
- **Temperature variation 20-40°C:** Add +0.3mm clearance per 100mm length
- **Temperature variation 0-60°C:** Add +0.6mm clearance per 100mm length

## CAD Material Libraries

### Assigning Material Properties in CAD

Most CAD systems include material libraries:

**SolidWorks:** Material database with density, elastic modulus, Poisson's ratio, thermal properties
**Fusion 360:** Autodesk material library + custom materials
**FreeCAD:** Material editor with mechanical and thermal properties

**Benefits of assigning materials:**
1. **Automatic mass calculation** (BOM, weight estimates)
2. **FEA simulation** (stress, deflection, thermal analysis)
3. **Rendering** (realistic appearance)
4. **Cost estimation** (material cost × volume)

**Example - Parametric Material Selection:**
```
Material parameter: "Aluminum_6061"

Part properties (auto-calculated):
  Density: 2.70 g/cm³
  Volume: 150 cm³
  Mass: 405 g
  Material cost: $4.50/kg → $1.82 per part
```

Switch parameter to "Aluminum_7075":
```
  Density: 2.81 g/cm³
  Mass: 422 g
  Material cost: $8.00/kg → $3.38 per part
```

**Instant comparison** without leaving CAD.

## Summary

Material selection is a critical design decision affecting performance, manufacturability, and cost. This section has shown that **material cost is only 2-5% of total part cost**—machinability and design decisions are the real cost drivers.

**Key Takeaways:**

**1. Total Cost Thinking:**
- Aluminum costs $4.50/kg but total part cost = $17.72
- Steel costs $2.50/kg but total part cost = $42.98
- **Machinability matters more than material price!**

**2. Real Cost Impacts Demonstrated:**
- Material over-engineering: $66.57 vs $21.58 (67% savings with better material choice)
- Ribbed vs solid construction: $120.17 vs $67.35 (44% savings + 66% weight reduction)
- Standard vs custom stock: $104.50 vs $33.28 (69% savings by designing for standard sizes)
- Appropriate plastic application: $618.50 vs $12.30 over 5 years (98% lifecycle cost reduction)

**3. Machinability Time Multipliers:**
- Aluminum baseline: 25 minutes
- Stainless steel: 77 minutes (3× slower)
- Titanium: 165 minutes (6.6× slower)
- Inconel: 375 minutes (15× slower!)

**4. Key Decision Factors:**
- **Functional requirements:** Strength, stiffness, environmental resistance
- **Machinability:** Tool wear, cutting time (dominates cost)
- **Availability:** Standard stock sizes, lead times
- **Total cost:** Material + machining + secondary processes + lifecycle maintenance

**5. Material Categories:**
- **Aluminum:** Lightweight, excellent machinability, good corrosion resistance, best for complex features
- **Steel:** High strength/stiffness, weldable, magnetic, 2-3× slower machining than aluminum
- **Brass/Bronze:** Excellent machinability, decorative, bearing applications, expensive material cost
- **Plastics:** Lightweight, corrosion-resistant, electrical insulation, thermal expansion considerations critical
- **Composites:** High strength/stiffness-to-weight, expensive, difficult machining, typically molded

**6. CAD Integration Best Practices:**
- Assign materials in CAD for automatic mass/cost calculations
- Use parametric material properties (`stock_thickness`, `material_density`) for design optimization
- Design for standard stock sizes (saves 50-70% on material cost + eliminates lead time)
- Account for thermal expansion in assemblies (plastics expand 5-10× more than metals)
- Consider machinability when designing complex features (Inconel pocket = 16× cost vs aluminum!)

**Professional vs Amateur Mindset:**
- **Amateur:** "Material X is stronger, so I'll use that"
- **Professional:** "What's the minimum material performance needed? What's the total cost (material + machining + lifecycle)?"

**Next section** covers process-specific design considerations for each CNC technology in the course.

***

**Next:** [Section 16.7: Process-Specific Design Considerations](section-16.7-process-specific-design.md)

**Previous:** [Section 16.5: Tolerancing and GD&T](section-16.5-tolerancing-gdt.md)

---

# Section 16.5: Tolerancing and Geometric Dimensioning & Tolerancing (GD&T)

## Introduction

**No manufacturing process creates perfect parts. The question isn't "will there be variation?"—it's "how much variation can we afford?"**

Every dimension has variation—the art of engineering design is specifying how much variation is acceptable for function while remaining economical to produce. This section covers traditional tolerancing methods and introduces Geometric Dimensioning and Tolerancing (GD&T), the international language for precisely communicating design intent.

**Real-World Impact:**

**Scenario 1: Over-Toleranced Part**
- Designer specifies ±0.01mm on all 50 dimensions
- Shop quote: $450 per part (requires grinding, precision inspection)
- **Reality check:** Only 5 dimensions actually need ±0.01mm
- **Redesign** with appropriate tolerances: $85 per part
- **Savings:** $365 per part (81% cost reduction!)

**Scenario 2: Under-Toleranced Part**
- Designer leaves all tolerances unspecified
- Machinist assumes ±0.2mm (shop standard)
- Parts arrive: bearing hole is 20.35mm (should be 20.00mm +0.02/-0)
- **Result:** Bearings won't fit, 100 parts scrapped
- **Cost:** $8,500 scrap + $1,200 rework + 2 weeks delay

**The lesson:** Tolerancing is about communicating clearly what matters (and what doesn't).

## Understanding Manufacturing Variation

**Manufacturing variation is like archery—even the best archer doesn't hit the exact center every time.**

The goal is to define an acceptable "target zone" large enough to be economical, but small enough to ensure function.

### Sources of Variation

Understanding WHY variation occurs helps you tolerance intelligently:

**Machine-Related Variation:**
- Positioning accuracy (±0.005-0.05mm typical for CNC mills)
- Thermal expansion of machine components (20°C → 30°C = 0.01mm/meter in steel)
- Spindle runout (worn bearings = ±0.005-0.02mm radial error)
- Linear guide wear (older machines = looser positioning)
- Backlash in drive systems (direction reversal = small position error)

**Real Example:**
- Cold morning (15°C): Machine calibrated
- Afternoon (25°C): Machine body expanded 0.05mm
- Parts machined in afternoon: 0.05mm oversized on long dimensions
- **Solution:** Environmental temperature control OR wider tolerances

***

**Tool-Related Variation:**
- Tool deflection under cutting forces (thin tool + heavy cut = part undersized)
- Tool wear progression (first part vs 100th part = different sizes)
- Cutting edge sharpness variation (dull tool = larger burrs, worse finish)
- Tool runout in holder (tool wobbles = oversize holes)

**Real Example:**
- Drilling ⌀10mm holes with worn drill bit
- First hole: ⌀10.05mm (acceptable)
- 50th hole: ⌀10.18mm (out of tolerance!)
- **Solution:** Tool replacement schedule OR compensate in programming

***

**Material-Related Variation:**
- Inconsistent material properties (hardness varies = cutting forces vary)
- Internal stresses causing warping (thin walls bend after machining)
- Thermal expansion during/after machining (hot part = oversized, cools to smaller size)
- Grain structure variations (some areas cut cleaner than others)

**Real Example:**
- Machine aluminum part to exact size while hot from cutting
- Part cools overnight: shrinks 0.03mm
- **Result:** Part now undersized
- **Solution:** Allow cooldown before final measurement, or compensate for thermal expansion

***

**Process-Related Variation:**
- Fixturing repeatability (part position varies ±0.01-0.05mm between setups)
- Operator skill variation (manual operations = higher variation)
- Environmental conditions (temperature, humidity affect dimensions and tools)
- Measurement uncertainty (even measuring tools have ±0.001-0.01mm error)

**Real Example:**
- Inspector A measures part: 50.02mm (pass)
- Inspector B measures same part: 49.98mm (pass)
- **Actual size:** 50.00mm ±0.02mm (measurement uncertainty)
- **Solution:** Use calibrated instruments, establish inspection procedures

***

**Result:** Even well-controlled processes produce parts with dimensional variation.

**Key Insight:** Variation is NORMAL and EXPECTED. Good design accounts for it rather than fighting it.

### Process Capability

**Different processes have natural "comfort zones" for tolerance—push beyond them and costs skyrocket.**

| Process | Typical Tolerance | Best Achievable | Relative Cost | Limitations |
|---------|------------------|----------------|---------------|-------------|
| **Plasma Cutting** | ±0.5 mm | ±0.2 mm | 1× | Kerf width, heat distortion |
| **Laser Cutting** | ±0.1 mm | ±0.05 mm | 1.5× | Material thickness, heat input |
| **Waterjet** | ±0.15 mm | ±0.08 mm | 1.3× | Taper, abrasive variation |
| **CNC Milling** | ±0.05 mm | ±0.01 mm | 2× | Tool deflection, thermal effects |
| **CNC Turning** | ±0.025 mm | ±0.005 mm | 2× | Rigidity, tooling quality |
| **Wire EDM** | ±0.01 mm | ±0.002 mm | 8× | Wire diameter, thermal |
| **Grinding** | ±0.005 mm | ±0.001 mm | 6× | Wheel wear, thermal |
| **FDM 3D Printing** | ±0.3 mm | ±0.1 mm | 1× | Layer adhesion, shrinkage |
| **Resin 3D Printing** | ±0.1 mm | ±0.05 mm | 2× | Resin properties, curing |

**Tolerance Cost Multipliers (Relative to Standard Machining ±0.05mm):**

| Tolerance | Process Required | Cost Multiplier | Time Impact |
|-----------|-----------------|-----------------|-------------|
| ±0.5 mm | Standard plasma/laser | 0.3× | Fast |
| ±0.1 mm | Standard laser/milling | 1× (baseline) | Standard |
| ±0.05 mm | Careful milling | 1× | Standard |
| ±0.025 mm | Precision milling | 1.5× | +30% |
| ±0.01 mm | Grinding or EDM | 4× | +200% |
| ±0.005 mm | Precision grinding | 8× | +400% |
| ±0.001 mm | Ultra-precision (lapping) | 20× | +1000% |

**Real-World Example:**

**Part A: 100mm × 50mm plate with 4 mounting holes**

**Version 1 - Over-Toleranced:**
```
All dimensions: ±0.01mm
Hole positions: ±0.01mm
Surface finish: 0.4 µm Ra (mirror finish)
```
- **Process Required:** Precision grinding + hand polishing
- **Time:** 4 hours per part
- **Cost:** $320 per part @ $80/hr
- **Inspection:** CMM required (30 min, $60)
- **Total:** $380 per part

**Version 2 - Appropriately Toleranced:**
```
Overall dimensions: ±0.2mm (not critical)
Hole positions: ±0.05mm (functional requirement for motor mounting)
Surface finish: 3.2 µm Ra (standard milled)
```
- **Process Required:** Standard CNC milling
- **Time:** 25 minutes per part
- **Cost:** $33 per part @ $80/hr
- **Inspection:** Standard calipers (5 min, included)
- **Total:** $33 per part

**Savings: $347 per part (91% cost reduction!)** — Same function, 1/11th the cost.

***

**Key Insights:**

✓ **Stay within "typical" tolerance for each process** → Standard cost
✓ **Push to "best achievable"** → 2-4× cost increase
✓ **Exceed process capability** → 5-20× cost increase + secondary operations

**Design Rule:** Only specify tighter than "typical" tolerances when there's a documented functional need (bearing fit, precision assembly, sealing surface, etc.)

## Traditional Tolerancing Methods

### Plus/Minus Tolerancing

Most common method: nominal dimension ± tolerance value.

**Symmetric Tolerance:**
```
50 ±0.1 mm
  → Acceptable: 49.9 to 50.1 mm
```

**Asymmetric Tolerance:**
```
50 +0.2/-0.05 mm
  → Acceptable: 49.95 to 50.2 mm
```

**When to use asymmetric:**
- Mating features (shaft/hole) where one direction matters more
- Features limited by material removal (can't add material back)

### Limit Tolerancing

Specifies maximum and minimum dimensions directly:

```
Shaft diameter: 19.95 / 20.00 mm
Hole diameter:  20.10 / 20.15 mm
  → Guaranteed clearance: 0.10 to 0.20 mm
```

**Advantage:** Immediately clear what's acceptable; no mental math.

**Use case:** Critical mating features, manufacturing drawings.

### General Tolerance Notes

Specify default tolerances for undimensioned features:

```
UNLESS OTHERWISE SPECIFIED:
  - Decimal dimensions: ±0.1 mm
  - Angular dimensions: ±1°
  - Hole diameters: +0.2/0 mm
  - Surface finish: 3.2 µm Ra
```

**Advantage:** Reduces drawing clutter; only critical dimensions need individual callouts.

**Critical:** Must match shop capabilities. If shop standard is ±0.2mm, don't specify ±0.05mm as general tolerance.

### Tolerance Accumulation (Stack-Up)

**Problem:** Tolerances accumulate across chains of dimensions.

**Example:**
```
Part 1 length: 100 ±0.1 mm
Part 2 length: 100 ±0.1 mm
Part 3 length: 100 ±0.1 mm

Assembly length (3 parts end-to-end):
  Nominal: 300 mm
  Worst case: 299.7 to 300.3 mm  (±0.3 mm total variation)
```

**Worst-Case Stack-Up Formula:**
```
Total variation = ±(Tol₁ + Tol₂ + Tol₃ + ... + Tolₙ)
```

**Statistical Stack-Up (RSS - Root Sum Square):**
Assumes normal distribution of manufactured parts:
```
Total variation = ±√(Tol₁² + Tol₂² + Tol₃² + ... + Tolₙ²)
```

**Example with same parts:**
```
RSS stack: ±√(0.1² + 0.1² + 0.1²) = ±0.173 mm
```

**When to use RSS:** High-volume production where statistical variation applies.

**When to use worst-case:** Safety-critical applications, low volumes where statistics don't apply.

### Tolerance Chain Management

**Design strategy to minimize stack-up:**

**Poor approach (long chain):**
```
┌─────┬─────┬─────┬─────┐
│  A  │  B  │  C  │  D  │
└─────┴─────┴─────┴─────┘
 ←─────────────────────→
  Total = A+B+C+D ± (TolA + TolB + TolC + TolD)
```

**Better approach (direct dimension):**
```
┌─────┬─────┬─────┬─────┐
│  A  │     │     │     │
└─────┴─────┴─────┴─────┘
 ←─────────────────────→
  Total dimension specified directly ± single tolerance
```

**Best approach (datum-based dimensioning):**
All critical features measured from single datum = zero stack-up between them.

## Introduction to GD&T

### Why GD&T?

Traditional plus/minus tolerancing has limitations:

**Problem 1: Ambiguous Intent**
```
Hole position: X = 50 ±0.1, Y = 50 ±0.1
```
Does this create a ±0.1mm square zone, or ±0.141mm circular zone?
Different inspectors might interpret differently.

**Problem 2: Doesn't Control Form**
```
Surface: 100 ±0.1 mm
```
Surface could be bowed, twisted, tapered—as long as all points fall between 99.9 and 100.1mm.

**Problem 3: Doesn't Capture Functional Requirements**
A hole might be positioned perfectly but tilted at an angle—plus/minus tolerancing doesn't address orientation.

**GD&T Solution:**
Geometric Dimensioning and Tolerancing (ASME Y14.5 / ISO 1101) provides unambiguous symbols and rules for specifying:
- Form (straightness, flatness, circularity, cylindricity)
- Orientation (perpendicularity, parallelism, angularity)
- Location (position, concentricity, symmetry)
- Profile (surface profile, line profile)
- Runout (circular runout, total runout)

### GD&T Philosophy

**Key concepts:**

1. **Datums Define Reference Frames**
   - Datum = theoretically exact reference (surface, axis, plane)
   - Measurements made relative to datums, not arbitrary coordinate systems

2. **Feature Control Frames Specify Tolerances**
   - Standardized symbols eliminate ambiguity
   - Tolerance zones clearly defined (cylindrical, rectangular, etc.)

3. **Maximum Material Condition (MMC) Bonuses**
   - Parts that deviate from worst-case size get tolerance bonus
   - Encourages functional dimensioning

4. **Separation of Size and Form/Orientation/Location**
   - Diameter tolerance controls size
   - GD&T controls geometry independently

## GD&T Fundamentals

### Datum Reference Frames

Datums establish the coordinate system for measurements.

**Primary Datum (A):** Constrains 3 degrees of freedom
- Typically a flat surface (represents plane)
- Part sits against this surface

**Secondary Datum (B):** Constrains 2 more degrees of freedom
- Typically a perpendicular surface or axis
- Stops rotation, establishes direction

**Tertiary Datum (C):** Constrains final degree of freedom
- Completes the 3-2-1 locating scheme
- Fully defines part orientation

**Example: Rectangular Block**
```
Datum A: Bottom surface (establishes XY plane, constrains Z position and XY rotation)
Datum B: Left edge (establishes X direction, constrains X position and Z rotation)
Datum C: Front edge (establishes Y direction, constrains Y position)

Total: 6 degrees of freedom constrained (3 translation + 3 rotation)
```

**Datum Selection Priority:**
1. Primary: Most important mating surface or functional feature
2. Secondary: Perpendicular feature that defines orientation
3. Tertiary: Completes full constraint

**Real-World Example:**
Motor mount plate:
- Datum A: Mounting surface (bolts to machine)
- Datum B: Motor shaft bore (establishes rotation axis)
- Datum C: Locating pin hole (prevents rotation about shaft axis)

### Feature Control Frames

The "language" of GD&T—standardized symbols in rectangular boxes:

```
┌───┬────────┬───┬───┬───┐
│ ⊕ │ ⌀0.1   │ M │ A │ B │
└───┴────────┴───┴───┴───┘
 │      │      │   │   │
 │      │      │   │   └─ Secondary datum
 │      │      │   └───── Primary datum
 │      │      └───────── Material condition modifier
 │      └──────────────── Tolerance value
 └─────────────────────── Geometric characteristic symbol
```

### Common GD&T Symbols

**Form Controls (No Datum Required):**

| Symbol | Name | Controls | Tolerance Zone |
|--------|------|----------|----------------|
| — | Straightness | Line elements | Two parallel lines |
| ⬜ | Flatness | Surface | Two parallel planes |
| ○ | Circularity (Roundness) | Circular cross-sections | Two concentric circles |
| ⌭ | Cylindricity | Cylindrical surface | Two coaxial cylinders |

**Orientation Controls (Require Datum):**

| Symbol | Name | Controls | Tolerance Zone |
|--------|------|----------|----------------|
| ⊥ | Perpendicularity | 90° relationship to datum | Two parallel planes (or cylinder if applied to axis) |
| ∥ | Parallelism | Parallel relationship to datum | Two parallel planes (or cylinder) |
| ∠ | Angularity | Specific angle to datum | Two parallel planes at defined angle |

**Location Controls (Require Datum):**

| Symbol | Name | Controls | Tolerance Zone |
|--------|------|----------|----------------|
| ⊕ | Position | Location of feature | Cylindrical (holes) or rectangular (features) |
| ⌖ | Concentricity | Centerpoint alignment | Cylindrical about datum axis |
| ≡ | Symmetry | Symmetry about datum plane | Two parallel planes |

**Profile Controls:**

| Symbol | Name | Controls | Tolerance Zone |
|--------|------|----------|----------------|
| ⌓ | Profile of a Line | 2D profile tolerance | Equal bilateral or unilateral band |
| ⌒ | Profile of a Surface | 3D surface tolerance | Equal bilateral or unilateral 3D zone |

**Runout Controls:**

| Symbol | Name | Controls | Tolerance Zone |
|--------|------|----------|----------------|
| ↗ | Circular Runout | Surface variation at single cross-section | Radial distance at each position |
| ↗↗ | Total Runout | Surface variation along entire surface | Full surface composite variation |

### Material Condition Modifiers

**Maximum Material Condition (MMC) - Ⓜ:**
- For holes: smallest diameter
- For shafts: largest diameter
- Tolerance gets bonus as feature deviates from MMC

**Least Material Condition (LMC) - Ⓛ:**
- For holes: largest diameter
- For shafts: smallest diameter

**Regardless of Feature Size (RFS) - Default if no symbol:**
- Tolerance applies regardless of actual feature size

**Example - Positional Tolerance with MMC:**
```
Hole: ⌀10 +0.2/0 mm
Position tolerance: ⌀0.1 (M) relative to Datum A

If hole diameter = 10.0 mm (MMC):
  Position tolerance = ⌀0.1 mm

If hole diameter = 10.2 mm (LMC):
  Bonus tolerance = 0.2 mm
  Total position tolerance = ⌀0.3 mm
```

**Why this works:**
Larger hole = more clearance for mating fastener = can tolerate more position error.

## Practical GD&T Application Examples

### Example 1: Simple Mounting Plate

**Part:** Aluminum plate with four M6 mounting holes

**Drawing callouts:**

```
1. Datum A: Bottom surface
   Flatness: 0.05 mm

2. Hole diameters: ⌀6.6 +0.1/0 mm (4 places)

3. Hole positions: ⌀0.15 (M) | A |
   True position: 80mm x 60mm rectangular pattern centered on plate

4. Hole perpendicularity: ⊥ ⌀0.1 (M) | A |
```

**Interpretation:**
- Bottom surface must be flat within 0.05mm (reference for all other measurements)
- Holes between 6.6-6.7mm diameter (M6 clearance)
- Hole centers within ⌀0.15mm cylindrical zone from true position when holes at minimum diameter (6.6mm)
- Bonus tolerance: if hole is 6.7mm, position tolerance becomes ⌀0.25mm
- Holes must be perpendicular to bottom surface within ⌀0.1mm cylindrical zone at MMC

### Example 2: Shaft with Bearing Journals

**Part:** Steel shaft with two bearing mounting surfaces

**Drawing callouts:**

```
1. Datum A: Axis of left bearing journal
   (⌀20.00 / 19.98 mm)

2. Right bearing journal: ⌀20.00 / 19.98 mm
   Concentricity: ⌖ 0.02 | A |
   (Center axis must be within ⌀0.02mm cylindrical zone about Datum A axis)

3. Right bearing shoulder face:
   Perpendicularity: ⊥ 0.05 | A |
   (Surface must be within 0.05mm zone between two parallel planes perpendicular to Datum A)

4. Surface finish on bearing journals: 0.8 µm Ra
```

**Interpretation:**
- Left journal defines rotation axis (primary datum)
- Right journal must be concentric within 0.02mm (prevents bearing misalignment)
- Shoulder face perpendicular within 0.05mm (ensures bearing seats flat)
- Surface finish supports bearing operation (smooth rotation, reduced wear)

### Example 3: Machined Block with Perpendicular Hole

**Part:** Milled block with precision cross-hole

**Drawing callouts:**

```
1. Datum A: Bottom surface
   Flatness: 0.03 mm

2. Datum B: Front surface
   Perpendicularity: ⊥ 0.05 | A |

3. Cross-hole: ⌀8.00 / 7.98 mm
   Position: ⊕ ⌀0.05 (M) | A | B |
   Perpendicularity: ⊥ ⌀0.03 (M) | A |
```

**Interpretation:**
- Bottom surface flat within 0.03mm (foundation for all measurements)
- Front surface perpendicular to bottom within 0.05mm (establishes X-Y reference)
- Hole positioned within ⌀0.05mm cylindrical zone relative to Datum A and B intersection (at MMC)
- Hole axis perpendicular to Datum A within ⌀0.03mm cylindrical zone (at MMC)
- Bonus tolerance applies if hole diameter toward LMC (8.00mm)

## GD&T for CNC Processes

### Milling and Turning

**Achievable GD&T tolerances (typical CNC machining):**
- Flatness: 0.02-0.05 mm
- Perpendicularity: 0.02-0.05 mm
- Parallelism: 0.02-0.05 mm
- Position: ⌀0.05-0.1 mm
- Concentricity: 0.02-0.05 mm
- Cylindricity: 0.01-0.02 mm

**Tighter tolerances require:**
- Precision grinding
- Increased inspection
- Temperature-controlled environment

### Plasma, Laser, Waterjet (2D Cutting)

**GD&T typically not applied to edge geometry:**
- Edge perpendicularity poor (taper, dross, HAZ)
- Position tolerances loose (±0.1 to ±0.5mm)

**Where GD&T helps:**
- Flatness of starting material (purchase spec)
- Hole position for parts that undergo secondary machining

### 3D Printing (FDM)

**Challenges:**
- Layer lines create inherent straightness/flatness errors
- Anisotropic properties (different in Z vs XY)
- Shrinkage and warping

**Achievable GD&T:**
- Flatness: 0.2-0.5 mm (top/bottom surfaces)
- Position: ⌀0.3-0.5 mm
- Perpendicularity: 0.3-0.5 mm

**Workaround:** Design witness surfaces for secondary machining if tight GD&T required.

## Tolerance Analysis and Stack-Up with GD&T

### Fixed Fastener Assembly Example

**Problem:** Two plates bolted together. Ensure bolts always fit through both parts.

**Variables:**
- Bolt diameter: 6mm (M6)
- Clearance hole nominal: 6.6mm
- Hole tolerance: +0.1/0 (6.6-6.7mm)
- Hole pattern: 80mm x 60mm

**Without GD&T (traditional):**
```
Hole position: 40 ±0.1 mm from edges
Stack-up: ±0.1 + ±0.1 = ±0.2mm total variation between parts
Required clearance per hole: 6.6 - 6.0 = 0.6mm diameter
Available after stack-up: 0.6 - 2×0.2 = 0.2mm clearance (tight!)
```

**With GD&T and MMC:**
```
Hole diameter: 6.6 +0.1/0 mm
Position: ⌀0.1 (M) | A | B |

At MMC (6.6mm hole):
  Virtual condition = 6.6 - 0.1 = 6.5mm

At LMC (6.7mm hole):
  Virtual condition = 6.7 - 0.2 = 6.5mm (same!)

Clearance per hole: 6.6 - 6.0 = 0.6mm
Projected tolerance zone for mating: ⌀0.1mm guaranteed

Worst case: Both parts at opposite extremes
  Bolt sees virtual condition: 6.5mm
  Minimum hole: 6.6mm
  Guaranteed clearance: 0.1mm minimum (acceptable)
```

**Advantage:** MMC bonus tolerance makes manufacturing easier while guaranteeing assembly.

## Inspection and Verification

### Measuring GD&T Callouts

**Flatness:**
- Surface plate + dial indicator (manual)
- Coordinate Measuring Machine (CMM) with probe
- Laser scanner or optical comparator

**Position:**
- CMM probe measures hole centers
- Software calculates deviation from true position
- Compares to tolerance zone (cylindrical or rectangular)

**Perpendicularity:**
- Precision square + indicator (manual)
- CMM measures surface normal vectors
- Optical methods (autocollimator)

**Concentricity:**
- Part rotated on one datum, runout of other feature measured
- CMM measures multiple points, calculates axes

**Cylindricity:**
- CMM measures surface at multiple heights and angles
- Software generates best-fit cylinder, measures deviation

### Functional Gauging

**Go/No-Go Gauges:**
Simulate worst-case assembly condition.

**Example: Position gage for holes**
```
Gage pins diameter = Virtual Condition
  = Hole MMC - Position Tolerance
  = 6.6 - 0.1 = 6.5mm

If gage pins fit through all holes → Part PASS
If any pin doesn't fit → Part FAIL
```

**Advantage:** Fast, no calculations, anyone can use.

**Disadvantage:** Binary (pass/fail), doesn't indicate how far off.

## Summary

Proper tolerancing is critical for manufacturable, functional parts:

**Traditional Tolerancing:**
- Plus/minus dimensioning: simple, widely understood
- General tolerance notes: reduce drawing clutter
- Stack-up analysis: predict worst-case assembly variation
- Limitations: ambiguous, doesn't control form/orientation

**Geometric Dimensioning & Tolerancing (GD&T):**
- Unambiguous symbols (ASME Y14.5 / ISO 1101)
- Datums define reference frames
- Feature control frames specify exact tolerance zones
- Material condition modifiers (MMC) provide bonus tolerances
- Captures functional requirements precisely

**Best Practices:**
1. Match tolerances to process capabilities
2. Tolerance only critical features tightly
3. Use GD&T for complex parts, assemblies, high-volume production
4. Specify datums that match manufacturing and inspection methods
5. Consider inspection methods during design
6. Communicate with machinists—ensure tolerances are achievable

**Next section** covers how material selection impacts design decisions and manufacturability.

***

**Next:** [Section 16.6: Material Selection for Design](section-16.6-material-selection.md)

**Previous:** [Section 16.4: DFM Principles](section-16.4-dfm-principles.md)

---

# Section 16.7: Process-Specific Design Considerations

## Introduction

Each CNC manufacturing process has unique capabilities, constraints, and optimal design practices. This section synthesizes knowledge from Modules 5-12 of this course, providing CAD design guidelines tailored to each process. Understanding these process-specific considerations allows you to design parts that are not just manufacturable, but optimized for the intended production method.

## CNC Milling (Module 6)

### Process Overview

**Capabilities:**
- 3-axis: X, Y, Z motion (most common)
- 3+2 axis: 3-axis with tilting table/head (indexed positioning)
- Full 5-axis: Simultaneous 5-axis motion (complex surfaces)

**Typical tolerances:** ±0.05 mm (standard), ±0.01 mm (precision)

**Surface finish:** 1.6-3.2 µm Ra (standard), 0.8 µm Ra (finish passes)

### Design Guidelines for Milling

#### 1. Tool Access and Corner Radii

**Internal corners MUST have radius:**
```
Minimum radius = Tool diameter / 2

Practical minimum radius:
  - 1.5 mm (using 3 mm endmill) - common
  - 3 mm (using 6 mm endmill) - robust
  - 6 mm (using 12 mm endmill) - fast material removal
```

**Real-World Cost Impact:**

**Part: 150mm × 100mm aluminum bracket with 80mm × 50mm pocket**

| Corner Specification | Machining Method | Tool Size | Time | Cost @ $80/hr |
|---------------------|------------------|-----------|------|---------------|
| **R0 (sharp 90°)** | Wire EDM required | N/A | 120 min | **$160** |
| **R1.5 (3mm endmill)** | CNC milling | ⌀3mm | 45 min | **$60** |
| **R3 (6mm endmill)** | CNC milling | ⌀6mm | 18 min | **$24** |
| **R6 (12mm endmill)** | CNC milling | ⌀12mm | 12 min | **$16** |

**Key insights:**
- Sharp corners (R0) require EDM: **$160 cost, 7-day lead time**
- R3 corners with standard 6mm tool: **$24 cost (85% savings!), same-day turnaround**
- Larger radii = larger tools = faster material removal = lower cost

**Poor CAD design (Amateur):**
```
┌──────────┐
│          │
│  ┌────┐  │  ← Sharp 90° internal corners
│  │    │  │     IMPOSSIBLE to machine with rotating tool
│  └────┘  │     → Requires EDM: $160, 7-day lead time
│          │
└──────────┘
```

**Good CAD design (Professional):**
```
┌──────────┐
│          │
│  ┌────╮  │  ← R3 internal corners (matches 6mm endmill)
│  │    │  │     → Standard CNC milling: $24, same-day
│  └────╯  │
│          │
└──────────┘
```

**Optimal CAD design (Cost-conscious Professional):**
```
┌──────────┐
│          │
│  ┌────╮  │  ← R6 internal corners (matches 12mm endmill)
│  │    │╮ │     → Fast CNC milling: $16, 2-hour turnaround
│  └────╯╯ │     → 33% faster than R3 version!
│          │
└──────────┘
```

**Design decision workflow:**
1. **Does function REQUIRE sharp corner?** → 95% of time: NO
2. **What's the largest acceptable radius?** → Use that for fastest machining
3. **If sharp corner truly required:** Budget for EDM ($150-300 extra + lead time)

**T-slot exception:**
Undercut features possible with form tools, but limit depth and specify standard form cutter sizes.

#### 2. Pocket Depth Guidelines

**Depth-to-diameter ratio:**
```
Standard pockets: Depth ≤ 3 × Tool_Diameter
Deep pockets: Depth ≤ 5 × Tool_Diameter (slow, higher tool wear)

Example:
  6mm endmill → Maximum practical pocket depth = 18mm (standard), 30mm (deep)
```

**Reducing cycle time:**
- Shallow pockets machine faster (higher feeds/speeds)
- Multiple shallow pockets better than one deep pocket if design allows
- Contour pockets faster than zig-zag in many cases

#### 3. Wall Thickness

**Minimum wall thickness:**
```
Aluminum: 2-3 mm (standard), 1.5 mm (thin-wall with care)
Steel: 3-5 mm (standard), 2 mm (thin-wall)
Plastic: 3-4 mm (standard), 2 mm (thin-wall)
```

**Thin walls deflect during machining:**
- Leave extra stock, rough to near-final, finish in light passes
- Design temporary support tabs (remove in secondary op)
- Add ribs or gussets to strengthen during machining

#### 4. Through Holes vs. Blind Holes

**Through holes (preferred):**
- Faster (drill exit without dwell)
- Easier chip evacuation
- No depth tolerance issues
- Can be drilled from both sides if needed

**Blind holes (when necessary):**
- Specify depth to full diameter (not including drill point)
- Standard drill point angle: 118°
- Add extra depth for point clearance if mating part requires flat bottom

**CAD specification:**
```
Blind hole callout:
  ⌀8 mm × 20 mm deep
  + 4 mm point depth allowance
  = 24 mm total drilling depth
```

#### 5. Chamfers vs. Fillets (External Edges)

**Chamfers (preferred for machining):**
- Single-pass operation
- Faster cycle time
- Standard chamfer mill sizes: 45°, 60°, 82°, 90°
- Removes burrs in same operation
- Good for assembly lead-ins

**Fillets (when required):**
- Need ball endmill or corner radius endmill
- Multiple passes for large radii
- Slower cycle time
- Better for stress reduction in loaded parts

**CAD decision tree:**
```
External edge:
  └─ Is stress concentration a concern?
      ├─ YES → Use fillet (stress relief)
      └─ NO → Use chamfer (faster machining)
```

#### 6. Feature Accessibility

**3-Axis milling constraints:**
```
✓ Features accessible from top
✓ Vertical walls
✗ Undercuts (without flipping/repositioning)
✗ Compound angle holes
```

**Design for single setup:**
- All critical features on same side
- Minimize need for part flipping
- If flip required, design locating features (dowel pins, precision holes)

**Multi-setup design:**
```
Setup 1 (primary datum establishment):
  - Machine Datum A surface (reference plane)
  - Drill datum B and C locating holes

Setup 2 (using established datums):
  - Locate part using datum holes and pins
  - Machine all secondary features referenced to A, B, C
```

#### 7. Material-Specific Milling Considerations

| Material | Cutting Speed | Feed Considerations | Design Implications |
|----------|---------------|---------------------|---------------------|
| Aluminum | High (200-500 m/min) | High feeds possible | Complex features economical |
| Mild Steel | Medium (50-150 m/min) | Moderate feeds | Simpler features preferred |
| Stainless | Low (30-80 m/min) | Light feeds (work-hardens) | Minimize deep pockets, thin walls |
| Plastics | Variable | Risk of melting | Sharp tools, conservative speeds |

### Milling CAD Checklist

- [ ] All internal corners radiused ≥ 1.5 mm
- [ ] Pocket depths ≤ 3× tool diameter
- [ ] Wall thickness ≥ 2 mm (aluminum), ≥ 3 mm (steel)
- [ ] Through holes used instead of blind holes where possible
- [ ] Chamfers specified on external edges (unless stress relief needed)
- [ ] All features accessible from single setup when possible
- [ ] Datums specified for multi-setup parts
- [ ] Tolerances appropriate for milling capability (±0.05 mm standard)

***

## CNC Turning (Lathe Operations)

### Process Overview

**Capabilities:**
- Axially symmetric parts (cylindrical)
- External turning, facing, grooving, threading
- Internal boring, drilling, threading
- Typical tolerances: ±0.025 mm (standard), ±0.005 mm (precision)

### Design Guidelines for Turning

#### 1. Axial Symmetry Requirement

**Ideal for turning:**
```
Shafts, bushings, spacers, pulleys, threaded rods
  - All features concentric about central axis
  - Diameters, grooves, threads
```

**Not ideal for turning:**
```
Features off-axis (flats, cross-holes, keyways)
  - Requires secondary milling operations
  - Or mill-turn machine
```

#### 2. Diameter Changes and Shoulders

**Smooth transitions preferred:**
```
Gradual diameter reduction = efficient cutting
Sharp shoulders = tool changes, slower cycle time
```

**Undercuts and grooves:**
```
Groove width = Tool width + clearance
  Standard grooving tool widths: 2, 3, 4, 5, 6 mm

Minimize groove depth:
  Deep grooves = slow, potential chatter
  Depth < 2× width (preferred)
```

**Relief grooves for threads:**
```
Thread relief: Allow threading tool runout
  Width ≥ thread pitch × 2
  Depth ≥ thread depth × 1.2
```

#### 3. Length-to-Diameter Ratio

**Rigidity concerns:**
```
L/D < 3: Very rigid, no tailstock support needed
L/D = 3-10: Moderate, may need tailstock or steady rest
L/D > 10: Flexible, requires support, slow cutting
```

**CAD design optimization:**
- Reduce length where possible
- Add diameter where length required (↑ stiffness)
- Design for stock support (live centers, steady rests)

#### 4. Internal Features (Boring)

**Through bores (preferred):**
```
✓ Tool passes completely through
✓ Easier chip evacuation
✓ No depth tolerance issues
```

**Blind bores:**
```
Depth ≤ 4× Diameter (practical limit)
  Deeper = slow, risk of tool deflection/chatter
```

**Minimum bore diameter:**
```
Typically: ≥ 5 mm (small lathes)
           ≥ 10 mm (production lathes)
Limited by smallest available boring bar rigidity
```

#### 5. Threading Considerations

**External threads (standard):**
```
Thread relief groove required at shoulder
  Allows threading tool to exit cleanly

Chamfer start of thread:
  45° chamfer = easier assembly, protects thread start
```

**Internal threads:**
```
Thread relief groove or through-bore preferred
Blind tapped holes: ensure adequate thread engagement
  Steel into steel: 1× diameter
  Aluminum into aluminum: 1.5× diameter
```

**Standard pitches preferred:**
```
Metric: M6×1.0, M8×1.25, M10×1.5 (coarse standard)
Unified: 1/4-20, 5/16-18, 3/8-16 (coarse standard)
```

#### 6. Knurling

**Knurled surfaces for grip:**
```
Standard knurl patterns:
  - Diamond knurl (crossed diagonal)
  - Straight knurl (parallel to axis)

Knurl dimensions:
  - Increases diameter by ~0.1-0.2 mm
  - Specify diameter BEFORE knurling
  - Tolerance after knurling: ±0.2 mm typical
```

### Turning CAD Checklist

- [ ] Part is axially symmetric (or can be made so)
- [ ] Diameter changes have fillets/chamfers (not sharp shoulders)
- [ ] Grooves match standard tool widths
- [ ] Thread reliefs specified
- [ ] Length-to-diameter ratio < 10 (or supports designed)
- [ ] Through bores used when possible
- [ ] Standard thread pitches specified
- [ ] Tolerances appropriate for turning (±0.025 mm standard)

***

## Plasma Cutting (Module 5)

### Process Overview

**Capabilities:**
- 2D profiles from sheet metal
- Material thickness: 1-50 mm (typical systems)
- Typical tolerance: ±0.5 mm
- Kerf width: 1-4 mm (depending on material/thickness)

### Design Guidelines for Plasma Cutting

#### 1. Kerf Width Compensation

**Kerf = width of cut removed by plasma arc**
```
Design hole: ⌀50 mm
Kerf width: 2 mm
CAM compensation: Path offset inward by 1 mm (radius compensation)
Actual hole: ~⌀50 mm (after kerf)
```

**Real-World Example: Precision Holes in Plasma-Cut Parts**

**Amateur Mistake:**
- CAD model: ⌀25.0mm hole for ⌀25mm shaft
- Plasma cuts with 2mm kerf, NO compensation applied
- **Actual hole:** ⌀27mm (2mm oversized!)
- **Result:** Shaft has 2mm slop, part rejected

**Professional Approach:**
- CAD model: ⌀25.0mm hole (nominal dimension)
- CAM applies kerf compensation automatically
- Plasma torch path: ⌀24.0mm (offset inward 1mm radius)
- **Actual hole:** ⌀25.0mm ±0.5mm (within tolerance)
- **Result:** Part accepted

**Cost Impact of Kerf Compensation Errors:**

| Mistake | Consequence | Cost |
|---------|-------------|------|
| No compensation | 50-part batch rejected, all holes oversized | **$1,200 scrap** |
| Wrong compensation direction | Holes undersized, requires secondary drilling | **+$15 per part** |
| Correct compensation | Parts within tolerance | **$0 extra** |

**CAD Best Practice:**
- Model nominal dimensions (what you want final part to be)
- Let CAM software apply kerf compensation
- Don't manually adjust CAD unless you're compensating for known process variations
- Always run test cut on first part to verify actual dimensions

#### 2. Minimum Feature Size

**Minimum hole diameter:**
```
Min diameter ≥ Material thickness
  3 mm plate → ⌀3 mm holes okay
  10 mm plate → ⌀10 mm holes minimum
```

**Minimum slot width:**
```
Min width ≥ Material thickness
```

**Reason:** Thicker materials require higher power, larger kerf, harder to cut small features.

#### 3. Edge Quality and Taper

**Plasma cut edges are NOT square:**
```
Top edge: slight roundover (arc initiation)
Cut face: 1-5° taper
Bottom edge: dross (molten metal)
```

**CAD design implications:**
- Specify top or bottom surface as reference
- Don't expect tight fit assemblies without secondary machining
- If precision required, leave stock for milling/grinding

**Dross attachment:**
- Worse on bottom edge
- Thicker materials = more dross
- Design parts to hide bottom edge or plan for grinding

#### 4. Pierce Points and Lead-Ins

**Pierce point = where arc starts (burns through material)**
```
Never pierce:
  ✗ On finished edge
  ✗ In small holes
  ✗ On critical features

Pierce location:
  ✓ In scrap area
  ✓ Lead-in path from scrap to part edge
```

**CAD design tip:**
- Provide scrap areas for pierce points
- Avoid tiny internal cutouts (require pierce per feature)

#### 5. Corner Radii and Sharp Corners

**Plasma can cut sharp external corners:**
```
External 90° corners: Okay (slight radius from kerf)
```

**Internal corners have kerf radius:**
```
Internal corners: Minimum radius ~ kerf width / 2
  Kerf 2 mm → internal corners ~1 mm radius
```

**CAD approach:**
- External corners: can be sharp (CAD shows sharp, plasma will add slight radius)
- Internal corners: model with radius ≥ kerf/2 for accuracy

#### 6. Nesting and Material Utilization

**CAD design for nesting:**
```
Spacing between parts: ≥ 10 mm (allows cut path without interference)
Edge margin: ≥ 5 mm from sheet edge
```

**Part orientation:**
- Rectangular parts: align with sheet edges (minimize waste)
- Interlocking shapes for maximum material usage

**Material comes in standard sheets:**
```
Common sizes:
  4' × 8' (1220 × 2440 mm)
  5' × 10' (1525 × 3050 mm)
```

Design part dimensions to nest efficiently on standard sheets.

### Plasma Cutting CAD Checklist

- [ ] All parts are 2D profiles (no 3D features)
- [ ] Hole diameters ≥ material thickness
- [ ] Tolerances appropriate for plasma (±0.5 mm typical)
- [ ] Top or bottom edge specified as datum (not center of edge)
- [ ] Pierce point locations considered (scrap areas provided)
- [ ] Part designed for efficient nesting
- [ ] If tight tolerances needed, stock left for secondary machining

***

## Laser Cutting (Module 7)

### Process Overview

**Capabilities:**
- 2D profiles from sheet metal
- Material thickness: 0.5-25 mm (fiber laser typical)
- Typical tolerance: ±0.1 mm
- Kerf width: 0.1-0.5 mm (much smaller than plasma)

### Design Guidelines for Laser Cutting

#### 1. Precision and Tolerances

**Laser cutting is more precise than plasma:**
```
Achievable tolerances: ±0.1 mm (vs ±0.5 mm plasma)
Kerf width: 0.2 mm typical (vs 2-4 mm plasma)
Edge perpendicularity: Better (less taper)
```

**CAD implications:**
- Can design tighter-fitting assemblies
- Smaller features practical
- Tab-and-slot joints feasible

#### 2. Minimum Feature Size

**Thinner materials allow smaller features:**
```
Material | Min Hole Diameter | Min Slot Width
---------|-------------------|---------------
1 mm     | 1 mm              | 0.5 mm
3 mm     | 3 mm              | 1.5 mm
6 mm     | 6 mm              | 3 mm
12 mm    | 12 mm             | 6 mm

Rule: Min feature ≈ Material thickness
```

#### 3. Heat-Affected Zone (HAZ)

**Laser creates narrow heat-affected zone:**
```
HAZ width: 0.1-0.5 mm from cut edge
Material near cut edge:
  - Hardened (steel)
  - Annealed (aluminum)
  - Discolored (stainless - "blueing")
```

**CAD design considerations:**
- Avoid tight bends immediately adjacent to cut edge (HAZ is brittle)
- Leave ≥ 2 mm between cut edge and bend line
- If cosmetic appearance critical, specify edge finishing

#### 4. Tab-and-Slot Joints

**Laser precision enables snap-fit assemblies:**
```
Slot width = Tab width + Fit clearance

Press fit: Clearance = -0.05 to 0 mm (interference)
Slide fit: Clearance = +0.05 to +0.1 mm
Loose fit: Clearance = +0.2 to +0.3 mm
```

**Design example: Sheet metal enclosure**
```
3 mm material thickness
Slot width: 3.05 mm (slide fit for 3 mm tab)
Tab length: 10 mm (engagement length)
```

**CAD parametric approach:**
```
material_thickness = 3 mm
fit_clearance = 0.05 mm   # Slide fit
slot_width = material_thickness + fit_clearance
tab_width = material_thickness
```

#### 5. Engraving and Marking

**Laser can engrave surfaces (defocused beam):**
```
Engraving depth: 0.1-0.5 mm typical
Applications:
  - Part numbers
  - Logos, text
  - Reference marks
```

**CAD specification:**
```
Create sketch on part surface with text/graphics
Specify engraving depth in CAM (not part geometry)
```

#### 6. Cutting Order and Small Part Retention

**Small parts can tip into cut kerf before completion:**
```
Solution: Cut internal features first, external perimeter last
  - Keeps part supported until final cut
  - CAM software typically handles this automatically
```

**Micro-tabs:**
```
Small connecting tabs (0.5-1 mm) hold part to sheet
Broken off after cutting (leave small witness marks)
```

### Laser Cutting CAD Checklist

- [ ] Tolerances appropriate for laser (±0.1 mm achievable)
- [ ] Minimum feature sizes ≥ material thickness
- [ ] Tab-and-slot joints dimensioned with appropriate clearance
- [ ] Bend lines ≥ 2 mm from cut edges (HAZ consideration)
- [ ] Engraving/marking specified if needed
- [ ] Part retention (tabs or cutting order) considered for small parts

***

## Waterjet Cutting (Module 8)

### Process Overview

**Capabilities:**
- 2D profiles from virtually any material
- Material thickness: 0.5-200 mm (abrasive waterjet)
- Typical tolerance: ±0.15 mm
- Kerf width: 0.8-1.5 mm
- No heat-affected zone (cold cutting)

### Design Guidelines for Waterjet Cutting

#### 1. Taper Compensation

**Waterjet stream diverges as it penetrates material:**
```
Top surface: Entry point (smaller)
Bottom surface: Exit point (larger) due to jet expansion

Typical taper: 1-3° (depending on thickness, pressure, abrasive)

Example:
  12 mm thick material, 1.5° taper
  Top edge: 50.00 mm
  Bottom edge: 50.63 mm
  (larger by ~0.3 mm)
```

**CAD approach for critical dimensions:**
```
Specify which surface is critical:
  - Top surface critical: Cut with taper compensation
  - Bottom surface critical: Flip part orientation
  - Both critical: Secondary machining required
```

**Modern waterjet CAM:**
- 5-axis waterjet can tilt cutting head to compensate for taper
- Creates near-vertical edges even in thick material

#### 2. Material Thickness Considerations

**Waterjet excels at thick materials:**
```
Thickness | Cut Speed | Edge Quality
----------|-----------|-------------
3 mm      | Fast      | Excellent
12 mm     | Medium    | Good
25 mm     | Slow      | Fair
50 mm+    | Very slow | Requires slow feed for quality
```

**CAD design tip:**
- For thick materials (>25 mm), consider if plasma (steel) or bandsaw (rough cutting) + milling (finishing) is more economical

#### 3. Abrasive Considerations

**Abrasive creates slightly rough edge:**
```
Surface finish: 3-6 µm Ra (smooth pass)
              10-15 µm Ra (fast pass)

Not suitable for:
  - Sealing surfaces (without secondary finishing)
  - High-precision mating (tolerance too loose)
```

**CAD specification:**
- If smooth edge required, specify "quality pass" in CAM (slower cutting)
- If precision required, leave stock for grinding/milling

#### 4. No Heat-Affected Zone

**Major advantage over plasma/laser:**
```
✓ No thermal distortion
✓ No hardening (metals)
✓ No melting (plastics)
✓ Can cut composite/laminate materials without delamination
```

**Ideal materials for waterjet:**
- Hardened steel (already heat-treated)
- Aluminum (no HAZ concerns)
- Glass, stone, ceramics
- Composite materials (carbon fiber, fiberglass)

#### 5. Piercing and Delicate Features

**Piercing creates larger hole than cutting path:**
```
Pierce diameter: ~2× normal kerf width

Design approach:
  - Pierce in scrap area or large feature
  - Lead-in to final feature
  - Avoid piercing in small holes
```

#### 6. Stack Cutting

**Waterjet can cut multiple sheets stacked together:**
```
Stack 2-5 sheets of thin material
Cut all at once (economic for production runs)

Requirements:
  - Sheets must be clamped/secured (prevent shifting)
  - Top sheet can have slight variation from bottom sheet (taper)
```

**CAD approach:**
- Design allows for slight variation between parts (±0.2 mm)

### Waterjet Cutting CAD Checklist

- [ ] Tolerances appropriate for waterjet (±0.15 mm typical)
- [ ] Taper considered for thick materials (specify critical surface)
- [ ] Edge quality requirement specified (standard or quality pass)
- [ ] Pierce points located in scrap or large features
- [ ] Material thickness within waterjet capabilities
- [ ] If precision mating required, stock left for secondary machining

***

## FDM 3D Printing (Module 11)

### Process Overview

**Capabilities:**
- Complex 3D geometries
- Build volume: 200×200×200 mm (desktop) to 1000×1000×1000 mm (large format)
- Typical tolerance: ±0.3 mm (desktop), ±0.5 mm (large format)
- Layer height: 0.1-0.4 mm

### Design Guidelines for FDM

#### 1. Layer Orientation and Strength Anisotropy

**FDM parts are anisotropic (directional strength):**
```
Strength parallel to layers (XY): ~100%
Strength perpendicular to layers (Z): ~50-70%

Failure mode: Delamination between layers
```

**CAD design strategy:**
```
Orient part so primary loads are parallel to layer lines

Example: Hook design
  Poor orientation:  Load pulls perpendicular to layers → delamination
  Good orientation: Load pulls parallel to layers → high strength
```

**CAM decision (not CAD):**
- Part orientation set in slicer software
- But CAD designer should consider orientation during design

#### 2. Overhangs and Support Material

**Maximum overhang angle without support:**
```
45° rule: Angles ≤ 45° from vertical can self-support
          Angles > 45° require support material

Example:
  Wall at 30° from vertical: Okay without support
  Wall at 60° from vertical: Requires support
```

**Support material:**
```
Printed structure beneath overhangs
Must be removed after printing (manual or dissolvable)
Leaves rough surface where support contacted part
```

**Real-World Cost Impact: Bracket Design**

**Part: 80mm × 60mm × 40mm mounting bracket with overhang**

**Amateur Design (no consideration for supports):**
- Horizontal mounting flange (90° overhang)
- Requires dense support material underneath
- Print time: **6 hours**
- Support material: 45g PLA @ $0.05/g = **$2.25**
- Support removal time: **15 minutes** @ $30/hr = **$7.50**
- Surface finish: Rough on support contact areas (requires sanding)
- **Total extra cost from supports: $9.75 per part**

**Professional Design (45° chamfer instead of flat overhang):**
- Mounting flange with 45° chamfer (no support needed)
- Print time: **4.5 hours** (25% faster!)
- Support material: **$0**
- Support removal time: **$0**
- Surface finish: Clean on all surfaces
- **Total savings: $9.75 per part + better quality**

**Comparison for 50-part production run:**
- Amateur design: 50 × $9.75 = **$487.50 extra cost** + 12.5 hours labor
- Professional design: **$0 extra cost**, clean finish, 75 hours less print time

**CAD Design Strategies to Minimize Supports:**

| Design Feature | Poor (Needs Support) | Good (No Support) | Savings per Part |
|----------------|----------------------|-------------------|------------------|
| Mounting flange | Horizontal (90°) | 45° chamfer | $9.75 |
| Through hole | Vertical hole (ceiling) | Horizontal hole or teardrop | $3.50 |
| Overhang boss | Circular boss beneath | Chamfered or tiered | $5.25 |
| Cable channel | Enclosed tunnel | Open channel (print upside down) | $12.00 |

**CAD design to minimize supports:**
```
✓ Avoid overhangs > 45° (design with chamfers)
✓ Use chamfers instead of overhanging curves
✓ Orient part to minimize overhangs
✓ Add built-in support structures (tearaway tabs) if needed
✓ Use teardrop-shaped holes instead of circular (for horizontal holes)
✗ Don't create large flat overhanging surfaces
✗ Don't design features that create trapped pockets (support can't be removed)
```

#### 3. Bridging

**Bridging = horizontal unsupported span:**
```
Maximum bridge distance: 10-20 mm (material/printer dependent)

Example:
  Bridge across 10 mm gap: Usually okay
  Bridge across 50 mm gap: Requires support
```

**CAD design for bridging:**
```
✓ Keep horizontal unsupported spans < 15 mm
✓ Add vertical support columns if larger spans required
```

#### 4. Wall Thickness and Shell Design

**Minimum wall thickness:**
```
Single wall: 0.4 mm (nozzle diameter, fragile)
2 walls: 0.8 mm (minimum practical)
3 walls: 1.2 mm (good strength)
4+ walls: 1.6 mm+ (structural)

Recommended minimum: 2 mm (robust, easy to print)
```

**Shell and infill:**
```
Exterior shells: Solid (printer default: 2-4 perimeters)
Interior: Infill pattern (20% infill common)

Solid parts: 100% infill (slow, expensive, often unnecessary)
```

**CAD design:**
- Model solid geometry (CAD shows full part)
- Slicer software applies shell/infill settings
- No need to model infill in CAD

#### 5. Hole Compensation

**Holes print undersized:**
```
Designed hole: ⌀8 mm
Actual printed: ⌀7.7-7.9 mm (material shrinkage, thermal contraction)

Compensation:
  Design holes +0.2 to +0.3 mm oversized
  OR drill/ream after printing
```

**Vertical vs horizontal holes:**
```
Vertical holes (parallel to build axis):
  More accurate (circular cross-section each layer)

Horizontal holes (perpendicular to build axis):
  Less accurate (stair-stepping from layer lines)
  Oval cross-section if small diameter
```

**CAD parametric compensation:**
```
nominal_hole = 8 mm
fdm_compensation = 0.2 mm
print_hole_size = nominal_hole + fdm_compensation  # = 8.2 mm
```

#### 6. Threads and Fasteners

**Printed threads:**
```
Large threads (M10+): Can be printed directly
  - Coarse pitch preferred
  - Vertical orientation best

Small threads (M6 and smaller): Often unreliable
  - Use threaded inserts instead
```

**Threaded inserts (preferred):**
```
Heat-set inserts: Press into slightly undersized hole with soldering iron
  - Excellent pullout strength
  - Repeatable assembly/disassembly
  - Specify insert size (M3, M4, M5, etc.)

Press-fit inserts: Tapered threads cut into plastic
  - Good for low-cycle applications
```

**CAD approach:**
```
Model hole for insert, not threads:
  Heat-set insert: Hole = Insert OD - 0.2 mm (interference fit)
  Example: M3 insert (OD 4.6 mm) → ⌀4.4 mm hole
```

#### 7. Tolerances and Fits

**Clearance for sliding fits:**
```
Clearance = 0.3-0.5 mm (desktop FDM)
           0.5-0.8 mm (large format FDM)

Example: 8 mm shaft in bearing
  Shaft: ⌀8.0 mm
  Bearing hole: ⌀8.5 mm (0.5 mm clearance)
```

**Press fits:**
```
Interference = 0.1-0.2 mm (light press)
             0.3-0.5 mm (firm press, risk of cracking)
```

#### 8. Print-in-Place Assemblies

**Design parts that assemble as they print:**
```
Requirements:
  - Clearance ≥ 0.3 mm between moving parts
  - Vertical clearance ≥ 1 layer height (0.2 mm typical)

Examples:
  - Chain links
  - Hinges
  - Ball joints
```

**CAD design:**
```
Model assembly in assembled position
Ensure clearance between all moving parts
Verify no fused connections (slicer preview)
```

### FDM 3D Printing CAD Checklist

- [ ] Part oriented so loads parallel to layer lines
- [ ] Overhangs ≤ 45° (or support structures accepted)
- [ ] Horizontal unsupported spans ≤ 15 mm
- [ ] Wall thickness ≥ 2 mm for structural parts
- [ ] Holes oversized by 0.2 mm (compensation for shrinkage)
- [ ] Threaded inserts specified instead of printed threads (M6 and smaller)
- [ ] Tolerances appropriate for FDM (±0.3 mm desktop, ±0.5 mm large format)
- [ ] Print-in-place clearances ≥ 0.3 mm

***

## Hybrid Systems (Module 12)

### Combining Multiple Processes

**Common hybrid workflows:**

**1. Plasma/Laser + Milling:**
```
Step 1: Cut profile from plate (plasma/laser) - fast 2D cutting
Step 2: Mill precision features (holes, pockets, faces) - precise 3D machining

Advantages:
  - Saves milling time (profile already cut)
  - Better material utilization than milling from solid
```

**CAD approach:**
```
Design complete 3D part in CAD
Export 2D profile (DXF) for plasma/laser
Export 3D model for CAM milling program
Specify which features are cut vs milled
```

**2. 3D Print + Machining:**
```
Step 1: FDM print near-net shape - complex organic geometry
Step 2: Mill critical surfaces - precision datum and mating features

Advantages:
  - Complex geometry from 3D printing
  - Precision where needed from machining
```

**CAD approach:**
```
Model final part geometry
Add stock allowance on machined surfaces (0.5-1 mm)
Export STL for 3D printing (with stock)
Export STEP for CAM (final dimensions)
```

**3. Waterjet + Bending:**
```
Step 1: Waterjet cut flat pattern
Step 2: Brake press bend to final shape

Advantages:
  - Complex 2D profiles
  - 3D formed structure
  - No HAZ from waterjet (bending not affected)
```

**CAD approach:**
```
Model 3D folded part
Create flat pattern (sheet metal tools)
Export flat pattern DXF for waterjet
Specify bend lines, radii, angles for press brake
```

### Hybrid CAD Considerations

**Stock allowance for secondary machining:**
```
Plasma/laser cut → mill: +0.5-1 mm on machined faces
Waterjet cut → mill: +0.3-0.5 mm on machined faces
3D print → mill: +0.5-1 mm on machined faces
Casting → mill: +2-3 mm on machined faces
```

**Datum establishment:**
```
Primary process: Establishes locating features
Secondary process: References primary datums

Example:
  Waterjet: Cut perimeter and locating holes
  Milling: Use locating holes to fixture part, mill precision pockets
```

**Tolerance distribution:**
```
Rough process (plasma): ±0.5 mm
Finishing process (milling): ±0.05 mm on finished surfaces

Overall part: Mixed tolerances (specify which features are precision)
```

## Summary

Each CNC process has unique capabilities and constraints that influence CAD design. Understanding process-specific design rules can reduce costs by 40-90% while improving manufacturability.

### Cost Impact Summary: Process-Specific Design Decisions

This section demonstrated real-world cost impacts of process-aware CAD design:

| Process | Design Decision | Poor Design Cost | Good Design Cost | Savings |
|---------|----------------|------------------|------------------|---------|
| **Milling** | Corner radius (sharp vs R6) | $160 (EDM) | $16 (12mm endmill) | **90%** |
| **Plasma** | No kerf compensation | $1,200 (50-part scrap) | $0 (correct CAM) | **100%** |
| **FDM** | Support material | $9.75/part + rough finish | $0/part + clean | **100%** |

**Key Process Capabilities and Constraints:**

| Process | Tolerance | Key Design Considerations | Amateur Mistake | Cost Impact |
|---------|-----------|---------------------------|-----------------|-------------|
| **Milling** | ±0.05mm | Corner radii (R = tool radius), tool access, pocket depth | Sharp internal corners | +$140 per part (EDM) |
| **Turning** | ±0.025mm | Axial symmetry, L/D ratio <10, grooves, threading | High L/D (no tailstock) | Scrap from deflection |
| **Plasma** | ±0.5mm | 2D only, 1-4mm kerf, taper, pierce points | No kerf compensation | 100% scrap rate |
| **Laser** | ±0.1mm | 2D precision, small kerf (0.2-0.5mm), HAZ, tab-and-slot | Tight nested parts | Thermal warping |
| **Waterjet** | ±0.15mm | No HAZ, taper on thick materials, abrasive finish | Ignore taper | Fit issues on assemblies |
| **FDM** | ±0.3mm | Layer orientation, 45° overhangs, hole compensation, inserts | Horizontal overhangs | +$10/part support removal |
| **Hybrid** | Mixed | Stock allowance, datum references, tolerance distribution | No stock allowance | Part dimensions wrong |

### Critical Takeaways by Process

**CNC Milling:**
- **Corner radii cost hierarchy:** R0 = $160 (EDM) → R3 = $24 (6mm tool) → R6 = $16 (12mm tool)
- Larger corner radii = larger tools = faster machining = lower cost
- 95% of designs don't functionally require sharp corners

**Plasma Cutting:**
- **Kerf compensation errors:** $1,200 batch scrap vs $0 with proper CAM setup
- Always model nominal dimensions, let CAM compensate for kerf
- First-part verification critical (±0.5mm tolerance)

**FDM 3D Printing:**
- **Support material avoidance:** $9.75 savings per part + better surface finish
- 45° chamfer design rule eliminates most support needs
- 50-part run: $487 savings by designing for no supports

### Professional Design Workflow

**Step 1: Process Selection**
- Geometry: 2D (plasma/laser/waterjet) vs 3D (milling/FDM)
- Material: Metals (milling/plasma/laser/waterjet) vs Plastics (FDM/milling)
- Quantity: Low (<10) vs Medium (10-100) vs High (>100)
- Tolerance: Rough (±0.5mm) vs Standard (±0.1mm) vs Precision (±0.01mm)

**Step 2: Apply Process-Specific Rules**
- Reference this section's guidelines for chosen process
- Design parts that are EASY to make (not just possible)
- Larger radii, standard features, appropriate tolerances

**Step 3: Cost Validation**
- Review design against cost multipliers
- Sharp corners? EDM adds $150+
- Tight tolerances? Precision grinding adds 4-20× cost
- Support material? FDM adds $10+ per part

**Step 4: CAM Simulation**
- Visualize toolpaths before manufacturing
- Verify tool access, detect collisions
- Estimate accurate cycle times

**Step 5: First Article Inspection**
- Measure critical dimensions on first part
- Validate process capability
- Adjust if needed before full production

**Amateur vs Professional Mindset:**
- **Amateur:** "Design the perfect part, then figure out how to make it"
- **Professional:** "Design for the manufacturing process, optimizing cost and quality simultaneously"

**Next section** covers assembly design, bringing multiple manufactured parts together into functional systems.

***

**Next:** [Section 16.8: Assembly Design](section-16.8-assembly-design.md)

**Previous:** [Section 16.6: Material Selection](section-16.6-material-selection.md)

---

# Section 16.12: Conclusion

## Module Summary

Module 16 has provided a comprehensive journey through CAD design for manufacturable CNC parts, integrating knowledge from all previous modules in this course. You've learned to bridge the critical gap between design intent and manufacturing reality, creating parts that are not only functionally sound but also economical and reliable to produce.

### Key Learning Outcomes Achieved

**1. CAD Fundamentals and Parametric Modeling (Sections 16.1-16.3)**

You can now:
- Create fully constrained sketches with proper design intent
- Build robust parametric models that adapt intelligently to changes
- Use configurations and design tables to manage part families
- Organize files and manage versions professionally
- Apply master sketch techniques for coordinated designs

**2. Design for Manufacturability (Sections 16.4-16.6)**

You understand:
- Universal DFM principles that reduce cost and improve quality
- How to match tolerances to process capabilities
- GD&T fundamentals for unambiguous specification
- Material selection criteria balancing performance and manufacturability
- The cost hierarchy of manufacturing features

**3. Process-Specific Design (Section 16.7)**

You can design optimally for:
- **CNC Milling:** Tool access, corner radii, pocket depths, wall thickness
- **CNC Turning:** Axial symmetry, L/D ratios, threading, grooving
- **Plasma Cutting:** Kerf compensation, pierce points, taper considerations
- **Laser Cutting:** Precision features, HAZ management, tab-and-slot joints
- **Waterjet:** Taper compensation, thick materials, abrasive finishing
- **FDM 3D Printing:** Layer orientation, overhangs, hole compensation, inserts
- **Hybrid Systems:** Multi-process optimization, stock allowances

**4. Assembly and Documentation (Sections 16.8-16.9)**

You can:
- Design assemblies using top-down, bottom-up, or hybrid approaches
- Apply DFA principles to minimize parts and assembly complexity
- Select appropriate fasteners and specify clearances
- Create engineering drawings following ASME or ISO standards
- Generate BOMs and assembly documentation
- Manage revisions and engineering changes

**5. CAD-CAM Integration (Section 16.10)**

You know how to:
- Prepare CAD models for efficient CAM programming
- Choose appropriate file formats (STEP, DXF, native)
- Define work coordinate systems matching manufacturing setups
- Model stock for optimized toolpath generation
- Troubleshoot common CAD-to-CAM issues
- Leverage integrated vs. standalone CAM systems

**6. Advanced Techniques (Section 16.11)**

You've been introduced to:
- FEA for design validation and optimization
- Topology optimization for lightweight structures
- Generative design for exploring design alternatives
- Surface modeling for complex organic shapes
- Multi-body techniques for weldments and assemblies
- Reverse engineering from scanned parts

## Integration Across the Course

Module 16 synthesizes knowledge from all previous modules:

| Module | Integration into CAD Design |
|--------|----------------------------|
| **Modules 1-4: Machine Foundations** | Understanding machine work envelopes, accuracy limits, and coordinate systems informs design feasibility |
| **Module 5: Plasma Cutting** | Designing for kerf width, pierce points, heat distortion, and 2D profiles |
| **Module 6: Spindle/Milling** | Tool access, corner radii, pocket depths, surface finish requirements |
| **Module 7: Fiber Laser** | HAZ considerations, precision tolerances, thin-wall designs |
| **Module 8: Waterjet** | Taper compensation, thick material capabilities, no HAZ benefits |
| **Modules 9-10: Robotics** | Assembly automation features, pick-and-place considerations, gripper interfaces |
| **Module 11: Large FDM** | Additive manufacturing design rules, support structures, layer orientation |
| **Module 12: Hybrid Systems** | Multi-process optimization, stock allowances, datum establishment |
| **Module 13: EMI/EMC** | Enclosure design, grounding features, shielding effectiveness |
| **Module 14: LinuxCNC HAL** | Custom fixture design, work-holding considerations |
| **Module 15: G-code** | Understanding how CAD geometry translates to machine motion |

This integration enables you to make informed design decisions based on the complete manufacturing workflow.

## The Iterative Design Process

Successful CAD design for manufacturing is rarely linear. It follows an iterative cycle:

```
1. FUNCTIONAL REQUIREMENTS
   ↓
2. INITIAL CAD DESIGN (function-focused)
   ↓
3. DFM REVIEW
   • Process compatibility?
   • Material availability?
   • Tolerances achievable?
   • Cost reasonable?
   ↓
4. DESIGN OPTIMIZATION
   • Simplify geometry
   • Relax tolerances
   • Standard features
   ↓
5. ANALYSIS & VALIDATION
   • FEA (if structural)
   • CAM simulation
   • Tolerance stack-up
   ↓
6. PROTOTYPE & TEST
   • Physical validation
   • Measure actual vs. design
   • Gather manufacturing feedback
   ↓
7. REFINE DESIGN
   ↓
   (Iterate 2-7 until optimal)
   ↓
8. RELEASE FOR PRODUCTION
   • Finalize drawings
   • Create work instructions
   • Establish quality checks
```

**Key insight:** Each iteration improves the balance between functional performance and manufacturing efficiency.

## Best Practices Summary

### Design Phase

**Start with intent:**
- Understand why the part exists (function, interfaces, environment)
- Identify critical vs. non-critical features
- Document assumptions and requirements

**Design parametrically:**
- Capture design intent in parameters and relationships
- Build flexibility for future changes
- Create part families with configurations

**Apply DFM early:**
- Don't wait until design is "finished" to consider manufacturing
- Involve machinists/fabricators in design reviews
- Iterate based on manufacturing feedback

### Documentation Phase

**Dimension functionally:**
- Dimension the way the part will be inspected
- Use datum-based dimensioning (baseline, not chains)
- Apply GD&T for critical geometric relationships

**Specify appropriately:**
- Tolerances matched to process capabilities
- Material and finish clearly stated
- Manufacturing notes where helpful (not excessive)

**Maintain traceability:**
- Revisions documented with ECOs
- Part numbers and naming conventions consistent
- BOM accurate and up-to-date

### Manufacturing Handoff

**Prepare clean models:**
- Valid solids (no gaps, overlaps)
- Organized features
- Proper coordinate systems

**Export correctly:**
- STEP for 3D machining (universal, reliable)
- DXF for 2D cutting (plasma, laser, waterjet)
- PDF for drawings (universal distribution)

**Validate before release:**
- CAM simulation (verify toolpaths)
- Interference checks (assemblies)
- Drawing review (completeness, clarity)

## Common Pitfalls to Avoid

**Over-constraining designs:**
- Excessive tolerances increase cost without functional benefit
- Over-defined sketches make editing difficult
- Redundant dimensions cause conflicts

**Designing in isolation:**
- Not consulting with manufacturing before finalizing designs
- Ignoring material availability or standard stock sizes
- Specifying processes unavailable or uneconomical

**Poor file management:**
- Inconsistent naming conventions
- No version control
- Missing or incomplete documentation

**Ignoring manufacturing feedback:**
- Not iterating based on prototype results
- Dismissing machinist input on tooling/fixtures
- Failing to investigate root causes of manufacturing issues

**Complexity for its own sake:**
- Adding features that don't serve function
- Using advanced techniques (topology optimization, generative design) where simple designs suffice
- Over-engineering (excessive safety factors, tight tolerances everywhere)

## Tools and Resources for Continued Learning

### CAD Software

**Free/Open-Source:**
- FreeCAD (full parametric CAD, Python scripting)
- LibreCAD (2D drafting)
- OpenSCAD (script-based parametric design)

**Commercial (free for students/hobbyists):**
- Autodesk Fusion 360 (integrated CAD/CAM/CAE)
- Onshape (cloud-based, collaborative)
- SolidWorks (with educational license)

### Learning Platforms

**Online courses:**
- LinkedIn Learning (CAD software tutorials)
- Coursera / edX (mechanical design, manufacturing)
- YouTube (specific CAD techniques, project walkthroughs)

**CAD vendor resources:**
- Autodesk University (Fusion 360 learning paths)
- SolidWorks tutorials and certification programs
- FreeCAD wiki and forums

### Books and References

**Design:**
- *Machinery's Handbook* (comprehensive manufacturing reference)
- *Shigley's Mechanical Engineering Design* (fundamentals)
- *Product Design for Manufacture and Assembly* (Boothroyd, Dewhurst, Knight)

**GD&T:**
- *Fundamentals of GD&T* (Alex Krulikowski)
- ASME Y14.5-2018 standard (official GD&T specification)

**Manufacturing:**
- *Manufacturing Processes for Engineering Materials* (Kalpakjian, Schmid)
- *CNC Machining Handbook* (Alan Overby)

### Community and Forums

**CAD-specific:**
- FreeCAD Forum (community support, project showcase)
- SolidWorks Forum (official Dassault support)
- Autodesk Fusion 360 Community

**Manufacturing:**
- Practical Machinist (CNC programming, DFM advice)
- CNCzone (hobby and professional CNC)
- r/Machinists, r/CNC (Reddit communities)

**Engineering:**
- Eng-Tips Forums (professional engineering Q&A)
- GrabCAD (CAD model library, community)

## The Future of CAD for Manufacturing

### Emerging Trends

**AI-Assisted Design:**
- Generative design becoming more accessible
- AI suggests design improvements based on historical data
- Automated optimization for multiple objectives (cost, weight, strength)

**Cloud-Based Collaboration:**
- Real-time multi-user CAD (Onshape, Fusion 360 cloud)
- Distributed teams working on same model simultaneously
- Version control and branching (like software development)

**Digital Twins:**
- Virtual replicas of physical parts/assemblies
- Sensor data from manufactured parts fed back to CAD
- Predictive maintenance based on CAD+simulation+real-world data

**Additive + Subtractive Hybrid:**
- Designs optimized for hybrid processes (3D print + CNC finish)
- Lattice structures with machined interfaces
- Complex internal geometry (additive) + precision surfaces (CNC)

**Increased Automation:**
- Feature recognition improving (less manual CAM programming)
- Automated nesting and toolpath optimization
- MRP/ERP integration (design → BOM → procurement → scheduling)

### Skills for the Future

**Technical skills to develop:**
- Advanced simulation (FEA, CFD, thermal analysis)
- Generative design and topology optimization
- Surface modeling for complex geometry
- Scripting/automation (Python for FreeCAD, APIs for automation)

**Soft skills:**
- Collaboration across disciplines (design, manufacturing, quality)
- Systems thinking (understanding entire product lifecycle)
- Communication (translating technical to non-technical stakeholders)
- Continuous learning (tools and techniques evolve rapidly)

## Final Thoughts

CAD design for manufacturing is both an art and a science. The science comes from understanding materials, processes, and physics. The art comes from balancing competing requirements—strength vs. weight, precision vs. cost, complexity vs. manufacturability—to create elegant solutions.

**Remember:**
- The best CAD model is one that becomes a successful physical part
- Manufacturability is not a constraint—it's a design opportunity
- Iteration and collaboration lead to better results than perfection in isolation
- Never stop learning from manufacturing feedback

### Your Next Steps

**Immediate actions:**
1. Apply these principles to a real project (design, analyze, manufacture, evaluate)
2. Seek feedback from machinists and fabricators
3. Build a portfolio of CAD projects demonstrating skills learned
4. Contribute to open-source projects or online communities

**Ongoing development:**
1. Practice regularly (skills decay without use)
2. Learn adjacent skills (CAM programming, G-code, metrology)
3. Stay current with software updates and new features
4. Teach others (teaching reinforces your own understanding)

**Professional growth:**
1. Pursue certifications (CSWA, CSWP for SolidWorks; Fusion 360 certifications)
2. Attend trade shows and conferences (IMTS, EASTEC, Fabtech)
3. Network with professionals in design and manufacturing
4. Consider specialization (aerospace, medical devices, automotive, etc.)

## Course Integration: Your Path Forward

Having completed all 16 modules of this CNC Engineering Course, you now possess:

- **Mechanical knowledge** (frames, motion systems, spindles)
- **Process expertise** (plasma, laser, waterjet, milling, additive)
- **Control systems** (electronics, LinuxCNC, G-code)
- **Design skills** (CAD, DFM, tolerancing, documentation)

You're equipped to:
- Design complete CNC systems from scratch
- Optimize parts for specific manufacturing processes
- Program CNC machines
- Troubleshoot mechanical, electrical, and software issues
- Bridge the gap between design and manufacturing

**The journey doesn't end here—it begins.**

Go build something remarkable.

***

**Congratulations on completing Module 16 and the entire CNC Engineering Course!**

**Previous:** [Section 16.11: Advanced Techniques](section-16.11-advanced-techniques.md)

**Return to:** [Module 16 Main Page](module-16-cad-dfm.md)

**Course Overview:** [Main README](../../README.md)
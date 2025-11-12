# Section 24.17 – Advanced L.E.A.N. Concepts

## Overview

While the foundational L.E.A.N. tools—5S, SMED, Kanban, TPM, and Value Stream Mapping—provide tremendous value, advanced L.E.A.N. concepts take continuous improvement to the next level. These methodologies integrate L.E.A.N. with complementary frameworks like Theory of Constraints and Six Sigma, extend L.E.A.N. beyond the shop floor into product development and administration, and leverage digital technologies for enhanced performance.

This section explores advanced L.E.A.N. concepts that mature organizations use to achieve world-class performance. These tools are typically implemented after foundational L.E.A.N. practices are established and sustained.

**Important Note:** Don't try to implement all these advanced concepts simultaneously. Master the fundamentals first (Modules 23-24 core content), then selectively adopt advanced tools based on your organization's specific needs and maturity level.

## 17.1 Theory of Constraints (TOC) Integration

### What is Theory of Constraints?

**Theory of Constraints (TOC):** Management philosophy developed by Dr. Eliyahu Goldratt that states that any system's performance is limited by its constraints (bottlenecks). To improve the system, you must identify and exploit the constraint.

**Key Concept:** Every system has at least one constraint that limits throughput. Improvements elsewhere provide limited benefit until the constraint is addressed.

**TOC Core Principle:**
> "A chain is only as strong as its weakest link."

### The Five Focusing Steps

**TOC Methodology:**

**Step 1: IDENTIFY the Constraint**
- Find the bottleneck (resource with highest utilization, longest queue)
- In CNC shop: Often a specific machine, inspection, or setup process
- Use data: OEE, utilization rates, queue times

**Example:**
```
Machine Utilization Analysis:
- VF-3 Mill #1: 95% (CONSTRAINT - always has queue)
- VF-3 Mill #2: 70%
- Lathe #1: 60%
- CMM Inspection: 85%

Constraint: VF-3 Mill #1 (bottleneck limiting shop throughput)
```

**Step 2: EXPLOIT the Constraint**
- Maximize output from the constraint
- Eliminate downtime and waste at bottleneck
- Ensure constraint never waits for work

**Actions for CNC Constraint:**
- Eliminate unplanned downtime (rigorous PM, spare parts stocked)
- Optimize setups (SMED, quick-change fixtures)
- Run highest-value work on constraint (offload low-value work to non-constraints)
- Eliminate breaks and interruptions (buffer work, dedicated operator)
- Improve quality (zero defects from constraint to avoid rework)

**Step 3: SUBORDINATE Everything to the Constraint**
- Align all non-constraint resources to support the constraint
- Non-constraints should feed constraint (never let it starve)
- Don't maximize non-constraint utilization (creates excess WIP)

**Example:**
```
Non-Constraint Mill #2 (70% utilized):
- DON'T run it at 95% just to "keep it busy" (creates excess WIP)
- DO run it to keep buffer in front of Constraint Mill #1
- Subordinate its schedule to support constraint
```

**Step 4: ELEVATE the Constraint**
- Increase constraint capacity (if exploitation and subordination aren't enough)
- Options: Add equipment, add shifts, outsource, automation

**Elevation Actions:**
- Buy second VF-3 mill (add capacity)
- Add second shift on constraint machine
- Outsource overflow work
- Add automation (pallet changer, robot) to increase throughput

**Step 5: REPEAT (Find New Constraint)**
- Once constraint is broken, new constraint emerges
- Return to Step 1, identify new constraint
- Continuous improvement cycle

**Example:**
```
After adding 2nd VF-3 mill:
New constraint: CMM Inspection (now at 98% utilization)
Focus shifts to exploiting inspection bottleneck
```

### L.E.A.N. + TOC Integration

**Complementary Strengths:**

**L.E.A.N. Strengths:**
- Waste elimination across entire system
- Employee empowerment and engagement
- Continuous flow and pull production
- Kaizen culture

**TOC Strengths:**
- Focus on system bottleneck (highest ROI)
- Throughput accounting (financial impact)
- Buffer management (protect constraint)
- Rapid improvement (focused effort)

**Integrated Approach:**

**Use TOC to Prioritize L.E.A.N. Efforts:**
1. Identify constraint (TOC Step 1)
2. Apply L.E.A.N. tools to constraint first (VSM, SMED, TPM, Kaizen)
3. Focus improvement resources on bottleneck (highest impact)
4. Use L.E.A.N. for continuous improvement across system

**Example Integrated Application:**
```
Constraint: VF-3 Mill #1 (setup time 45 min, limits throughput)

Integrated Approach:
- TOC: Identify VF-3 as constraint, calculate throughput impact
- L.E.A.N.: Apply SMED to reduce setup to 15 min (3x improvement)
- Result: 30% increase in shop throughput (constraint capacity increased)
- TOC: New constraint emerges (inspection), repeat cycle
```

**Drum-Buffer-Rope (DBR) Scheduling:**

**TOC Scheduling Method:**

**Drum:** Constraint sets pace (schedule)
- Constraint is the "drum" beating the production rhythm
- All other resources sync to constraint schedule

**Buffer:** Inventory buffer protects constraint
- Time buffer (work waiting in front of constraint)
- Prevents constraint starvation (always has work)
- Typical buffer: 3-5 hours of work queued

**Rope:** Pull signal from constraint to material release
- Release raw material based on constraint consumption
- Prevents WIP overload (only release what constraint needs)

**DBR in CNC Shop:**
```
Drum: VF-3 Mill #1 schedule (constraint)
Buffer: 4 hours of rough-cut parts queued in front of VF-3
Rope: Release raw material to saws/lathes only when buffer consumed

Result: Controlled WIP, constraint never starves, smooth flow
```

### Practical Application in CNC Shop

**Step-by-Step TOC Implementation:**

**Week 1: Identify Constraint**
- Collect utilization data (all machines, inspection, processes)
- Identify bottleneck (highest utilization, longest queue)
- Calculate constraint throughput and value

**Week 2-4: Exploit Constraint**
- Apply SMED to reduce setup time
- Implement rigorous PM to eliminate downtime
- Optimize scheduling (batch sizes, sequencing)
- Cross-train operators (ensure constraint never waits for operator)

**Week 5-8: Subordinate Non-Constraints**
- Align upstream processes to feed constraint
- Create buffer in front of constraint (3-5 hours work)
- Don't over-produce at non-constraints

**Month 3-6: Measure and Elevate (if needed)**
- Track throughput improvement
- If constraint still limits (after exploitation), elevate (add capacity)
- Monitor for new constraint

**Ongoing: Repeat Cycle**
- Constraint shifts (after elevation)
- Repeat process with new constraint
- Continuous improvement focus on system bottleneck

## 17.2 L.E.A.N. Six Sigma (LSS)

### What is Six Sigma?

**Six Sigma:** Data-driven methodology for reducing variation and defects, achieving near-perfect quality (3.4 defects per million opportunities).

**Key Concepts:**
- **Statistical process control** (SPC, control charts)
- **DMAIC** methodology (Define, Measure, Analyze, Improve, Control)
- **Variation reduction** (Cpk, process capability)
- **Data-driven decisions** (not gut feel)

**Six Sigma Strengths:**
- Rigorous statistical analysis
- Root cause identification
- Variation reduction
- Quality improvement

**Six Sigma Weaknesses:**
- Can be slow (analysis paralysis)
- Requires statistical expertise (Black Belts, Green Belts)
- Less focus on speed and flow
- Can miss waste that doesn't affect quality

### L.E.A.N. + Six Sigma Integration

**Why Combine?**

**L.E.A.N. + Six Sigma = Powerful Combination**

**L.E.A.N. provides:**
- Speed (reduce lead time, increase flow)
- Waste elimination (all eight wastes)
- Employee engagement (Kaizen culture)
- Visual management (Gemba, Andon)

**Six Sigma provides:**
- Statistical rigor (understand variation)
- Root cause analysis (DMAIC, fishbone, 5 Whys with data)
- Quality focus (reduce defects, improve Cpk)
- Measurement systems (control charts, SPC)

**Combined Benefits:**
- Fast flow AND high quality
- Waste elimination AND variation reduction
- Employee engagement AND data-driven decisions
- Sustainable improvements (L.E.A.N. speed + Six Sigma control)

### LSS Methodology: DMAIC Meets L.E.A.N.

**Integrated DMAIC with L.E.A.N. Tools:**

**Define:**
- **L.E.A.N.:** Value stream mapping (identify process)
- **Six Sigma:** Project charter, VOC (Voice of Customer), CTQs (Critical to Quality)
- **Output:** Clear problem statement, scope, goals

**Measure:**
- **L.E.A.N.:** Current state VSM (lead time, cycle time, value-added ratio)
- **Six Sigma:** Data collection, baseline Cpk, control charts
- **Output:** Baseline performance (speed and quality)

**Analyze:**
- **L.E.A.N.:** Waste identification (8 wastes), process observation (Gemba)
- **Six Sigma:** Root cause analysis (fishbone, hypothesis testing, regression)
- **Output:** Root causes of waste and variation

**Improve:**
- **L.E.A.N.:** Future state VSM, Kaizen events, SMED, 5S
- **Six Sigma:** DOE (Design of Experiments), process optimization, poka-yoke
- **Output:** Implemented improvements (faster flow, less variation)

**Control:**
- **L.E.A.N.:** Standardized work, visual management, daily Kaizen
- **Six Sigma:** Control charts, SPC, process monitoring
- **Output:** Sustained improvements, continuous monitoring

### LSS Application in CNC Manufacturing

**Example: Reducing Scrap Rate on Precision Parts**

**Define:**
- **Problem:** 8% scrap rate on titanium aerospace parts (unacceptable, costly)
- **Goal:** Reduce to <2% scrap rate
- **L.E.A.N.:** Map current process (saw, mill, lathe, inspect)
- **Six Sigma:** Define CTQs (tolerance ±0.0005", surface finish 32 Ra)

**Measure:**
- **L.E.A.N.:** Cycle time, lead time, value-added analysis
- **Six Sigma:** Measure Cpk (current: 1.1, marginal), collect defect data (200 parts)
- **Baseline:** 8% scrap (16 parts/200), Cpk 1.1 (marginal capability)

**Analyze:**
- **L.E.A.N.:** Gemba observation (watch setups, operator techniques)
- **Six Sigma:** Pareto analysis (80% of defects are out-of-tolerance dimensions)
  - Fishbone diagram (5 Ms: Man, Machine, Material, Method, Measurement)
  - Root causes identified:
    1. Tool wear (not changing tools at optimal intervals)
    2. Fixture variability (worn fixture, inconsistent clamping)
    3. Temperature variation (parts machined at different times of day, thermal expansion)

**Improve:**
- **L.E.A.N.:** Kaizen event (team brainstorms solutions)
  - Implement tool life tracking (change tools at 80% of life, not 100%)
  - 5S tooling area (organize, label, standardize)
- **Six Sigma:** DOE (test optimal tool change interval, fixture clamping force)
  - Poka-yoke (fixture alignment pins, prevent incorrect loading)
  - Temperature compensation (program offsets for thermal expansion)

**Control:**
- **L.E.A.N.:** Standardized work (tool change intervals, fixture setup procedure)
  - Visual controls (tool life board, color-coded tools)
- **Six Sigma:** Control charts (Xbar-R charts for critical dimensions)
  - SPC monitoring (operator checks control charts, alerts on out-of-control)
- **Results:** Scrap reduced to 1.2%, Cpk improved to 1.67 (excellent capability)

### When to Use LSS vs. L.E.A.N. Alone

**Use L.E.A.N. Alone:**
- Waste is obvious (excessive WIP, long setups, poor layout)
- Speed is primary concern (lead time reduction)
- Problem is process flow, not variation
- Team lacks statistical expertise

**Use Six Sigma Alone:**
- Quality problem with complex, unknown root cause
- Variation is the primary issue (inconsistent dimensions, defects)
- Need statistical rigor (regulatory, critical applications)
- Time is less critical (can afford slower, thorough analysis)

**Use LSS (Combined):**
- Quality AND speed are both critical
- Complex problem (waste and variation)
- Mature organization (resources for both methodologies)
- High-value processes (aerospace, medical, automotive)

**Practical Tip:** Start with L.E.A.N. (faster, easier, more engaging). Add Six Sigma tools selectively when variation reduction is critical.

## 17.3 Hoshin Kanri (Policy Deployment)

### What is Hoshin Kanri?

**Hoshin Kanri:** Japanese strategic planning methodology that aligns organizational goals with daily actions. Translates to "direction management" or "policy deployment."

**Purpose:** Ensure everyone in organization works toward same strategic goals (no wasted effort on misaligned activities).

**Core Concept:**
> "Align the compass (strategy) with the steps (daily work)."

### The Hoshin Planning Process

**Annual Hoshin Cycle:**

**1. Establish Vision (3-5 Year Horizon):**
- Top management defines long-term vision
- Example: "Become the preferred supplier for aerospace precision components in Southwest region"

**2. Define Annual Breakthrough Objectives:**
- Identify 3-5 critical goals for the year (limit focus, avoid dilution)
- Example Annual Objectives:
  1. Reduce lead time from 4 weeks to 2 weeks
  2. Achieve AS9100 certification
  3. Increase on-time delivery from 85% to 98%

**3. Deploy to Levels (Catchball):**
- **Catchball:** Iterative dialogue between levels
  - Management proposes objectives ("throws ball down")
  - Lower levels propose tactics and commit ("throw ball back up")
  - Negotiate, align, finalize (iterative until alignment)

**Example Catchball:**
```
Top Management: "Reduce lead time to 2 weeks"
  ↓ (catchball)
Shop Manager: "We need faster setups and better scheduling"
  ↓ (catchball)
Setup Team: "We can achieve 30% setup reduction with SMED"
  ↑ (catchball)
Shop Manager: "30% setup reduction + new scheduling software = 35% lead time reduction"
  ↑ (catchball)
Top Management: "Agreed. Proceed with SMED and software investment."
```

**4. Create Action Plans (X-Matrix):**
- **X-Matrix:** Visual tool showing alignment of goals, strategies, tactics, metrics, owners
- Links: Annual objectives → Strategies → Tactics → Metrics → Owners

**Example X-Matrix (Simplified):**
```
Annual Objective: Reduce lead time to 2 weeks

Strategies:
1. Reduce setup time (SMED)
2. Improve scheduling (software + heijunka)
3. Reduce WIP (pull system)

Tactics (linked to strategies):
1.1 SMED Kaizen events on top 5 machines
1.2 Standardize fixtures and tooling
2.1 Implement JobBOSS scheduling software
2.2 Train schedulers on heijunka leveling
3.1 Implement supermarket for common parts
3.2 Kanban system for raw materials

Metrics:
- Average setup time (baseline: 45 min, target: 25 min)
- Lead time (baseline: 4 weeks, target: 2 weeks)
- WIP inventory turns (baseline: 6x/yr, target: 12x/yr)

Owners:
- SMED: Manufacturing Engineer
- Scheduling: Production Manager
- Pull System: Operations Manager
```

**5. Implement (PDCA):**
- Execute tactics (action plans)
- Use PDCA for each initiative (Plan-Do-Check-Act)

**6. Monthly/Quarterly Review:**
- Review progress against targets
- Identify obstacles (countermeasures)
- Adjust tactics if needed (flexibility within annual objectives)

**7. Annual Review:**
- Assess achievement of annual objectives
- Lessons learned
- Set next year's Hoshin (continuous cycle)

### Hoshin vs. Traditional Strategic Planning

**Traditional Strategic Planning:**
- Top-down (management decides, employees execute)
- Annual plan created, filed, forgotten
- No linkage between strategy and daily work
- No feedback loop (rigid plan)

**Hoshin Kanri:**
- Collaborative (catchball ensures buy-in and feasibility)
- Living document (monthly reviews, adjustments)
- Alignment from boardroom to shop floor (everyone knows how their work supports strategy)
- PDCA at all levels (flexible, adaptive)

### Hoshin in CNC Shop: Practical Example

**Scenario:** Small CNC shop (15 employees, $2.5M revenue)

**Vision (3-Year):** "Double revenue to $5M while maintaining quality and employee satisfaction"

**Year 1 Annual Objectives (Hoshin):**
1. Increase capacity 40% (add equipment, improve OEE)
2. Reduce scrap rate from 5% to 2%
3. Improve employee retention (reduce turnover from 30% to 10%)

**Deployment (Catchball):**

**Objective 1: Increase Capacity 40%**
- **Strategy:** Add 2 machines + improve OEE from 65% to 80%
- **Tactics:**
  - Purchase used VF-4 mill (Q1)
  - Implement TPM program (autonomous maintenance, planned PM)
  - SMED on top 3 bottleneck machines
- **Metrics:** OEE, machine utilization, throughput
- **Owner:** Operations Manager

**Objective 2: Reduce Scrap 5% → 2%**
- **Strategy:** Improve first-piece inspection + operator training + poka-yoke
- **Tactics:**
  - Implement first-off inspection checklist (standardized work)
  - Train operators on GD&T and tolerance interpretation
  - Kaizen event: Error-proof top 3 scrap-prone setups
- **Metrics:** Scrap rate, first-pass yield
- **Owner:** Quality Manager

**Objective 3: Improve Retention 30% → 10%**
- **Strategy:** Competitive wages + training + culture
- **Tactics:**
  - Wage survey, adjust pay to market rate (Q1)
  - Implement cross-training program (operator development)
  - Monthly team meetings (communication, engagement)
  - Kaizen suggestion system (employee empowerment)
- **Metrics:** Turnover rate, employee satisfaction survey
- **Owner:** HR/Owner

**Monthly Review:**
- Review metrics (OEE, scrap, turnover)
- Green (on track), Yellow (at risk), Red (off track)
- Red items: Root cause, countermeasures, action plan

**Results (End of Year 1):**
- Objective 1: ✅ Achieved 38% capacity increase (close to 40% target)
- Objective 2: ✅ Scrap reduced to 1.8% (exceeded target)
- Objective 3: ⚠️ Turnover reduced to 15% (improvement, but missed 10% target)
  - Year 2: Continue focus on retention, add benefits package

### Benefits of Hoshin Kanri

**1. Alignment:**
- Everyone works toward same goals (no wasted effort)
- Daily work clearly supports strategy

**2. Focus:**
- Limit to 3-5 objectives (avoid dilution)
- Resources concentrated on what matters most

**3. Engagement:**
- Catchball ensures buy-in (not top-down mandates)
- Employees contribute to planning (ownership)

**4. Flexibility:**
- Monthly reviews allow course correction
- PDCA at all levels (adapt to changing conditions)

**5. Accountability:**
- Clear owners, metrics, targets
- Transparent progress tracking

## 17.4 Quick Response Manufacturing (QRM)

### What is QRM?

**Quick Response Manufacturing (QRM):** Strategy focused on lead time reduction across all aspects of manufacturing enterprise (not just production, but also quoting, engineering, planning).

**Developed by:** Dr. Rajan Suri, University of Wisconsin-Madison

**Core Metric:** Manufacturing Critical-path Time (MCT)
- MCT = Total time from customer request to delivery (includes quoting, engineering, production, shipping)

**QRM Philosophy:**
> "Time is the ultimate competitive weapon. Reduce MCT, win customers."

### QRM vs. L.E.A.N.

**Similarities:**
- Both focus on waste elimination
- Both emphasize flow
- Both use cellular manufacturing

**Differences:**

| Aspect | L.E.A.N. | QRM |
|--------|----------|-----|
| **Primary Focus** | Waste elimination | Lead time reduction (time compression) |
| **Best Fit** | High-volume, repetitive production | High-mix, low-volume job shops |
| **Inventory** | Minimize (pull, JIT) | Strategic buffers (for speed, not waste) |
| **Lot Sizes** | Small batches (one-piece flow ideal) | POLCA-sized lots (right-sized for flow) |
| **Metrics** | Cost, quality, waste | MCT (Manufacturing Critical-path Time) |
| **Cell Triggering** | Kanban (pull) | POLCA cards (paired-cell overlapping loops) |

**Key Insight:** QRM adapts L.E.A.N. principles for job shop realities (high-mix, low-volume, custom products).

### QRM Core Concepts

**1. Focus on MCT (Not Cost):**

**Traditional Thinking:**
- Maximize machine utilization (keep machines busy)
- Large batch sizes (amortize setup costs)
- Result: Long lead times (batching and queuing)

**QRM Thinking:**
- Minimize MCT (total time customer waits)
- Right-sized batches (balance setup and flow)
- Result: Fast response (win time-sensitive customers)

**Example:**
```
Traditional (High Utilization):
- Batch size: 100 parts (minimize setups)
- Lead time: 6 weeks (parts queue behind large batches)
- Customer: Frustrated (slow response)

QRM (Low MCT):
- Batch size: 10 parts (faster flow, more setups)
- Lead time: 1 week (small batches flow quickly)
- Customer: Delighted (fast response, willing to pay premium)
```

**2. QRM Cells (Quick Response Cells):**

**Characteristics:**
- Dedicated teams (3-5 people)
- Focused on part families (similar routing, setup)
- Collocated equipment (reduce transport, improve communication)
- Ownership and accountability (team manages cell performance)

**Difference from L.E.A.N. Cells:**
- QRM cells handle higher mix (less repetition than L.E.A.N. cells)
- Emphasis on setup reduction (SMED critical for mix)
- Cross-training (team can run all machines in cell)

**3. POLCA (Paired-cell Overlapping Loops of Cards with Authorization):**

**Problem with Kanban in Job Shops:**
- Kanban works for repetitive parts (predictable demand)
- Job shops have high-mix, custom orders (Kanban doesn't fit)

**POLCA Solution:**
- Material control system designed for high-mix environments
- Cards authorize work between paired cells (not for specific parts)
- Controls WIP without forecasting specific part demand

**How POLCA Works:**

**Setup:**
- Identify cells (e.g., Cell A: Sawing, Cell B: Milling, Cell C: Finishing)
- Create POLCA cards for each cell pair (A-B, B-C, A-C)
- Limit number of cards (controls WIP)

**Operation:**
```
Job enters Cell A (Sawing):
- Requires POLCA card A-B (Cell A to Cell B authorization)
- If A-B card available: Job proceeds to Cell A
- If no A-B card: Job waits (queue controlled)

Job completes in Cell A:
- Moves to Cell B with POLCA card A-B
- Cell B starts work

Job completes in Cell B:
- POLCA card A-B returns to Cell A (reused for next job)
- Job moves to Cell C with POLCA card B-C

Result: WIP controlled between cells, but flexible for any part (not part-specific like Kanban)
```

**Benefits:**
- Controls WIP (prevents overload)
- Flexible (works for custom, high-mix orders)
- Simple (visual cards, easy to manage)

**4. Office QRM (QRMO):**

**Insight:** Office processes (quoting, engineering, order entry) often take longer than production.

**Example MCT Breakdown:**
```
Total MCT: 8 weeks
- Quoting: 2 weeks (25%)
- Engineering: 3 weeks (37.5%)
- Production: 2 weeks (25%)
- Shipping: 1 week (12.5%)

Bottleneck: Engineering (longest critical path component)
```

**QRM Office Cell:**
- Cross-functional team (sales, engineering, production planning)
- Dedicated to customer order fulfillment (quote to order release)
- Collocated (reduce handoffs, improve communication)
- Target: Reduce office MCT by 50-75%

### QRM Implementation in CNC Job Shop

**Step 1: Measure Baseline MCT**
- Track total time: Quote request → Delivery
- Breakdown: Quoting time, engineering time, production time, shipping time
- Identify longest components

**Step 2: Create QRM Cells**
- Organize shop into cells (part families: shafts, housings, brackets, etc.)
- Collocate equipment (saw, mill, lathe, deburr in one area)
- Assign dedicated teams

**Step 3: Implement POLCA**
- Define cell pairs
- Create POLCA cards (limit WIP)
- Train team on POLCA system

**Step 4: Reduce Setup Times (SMED)**
- Critical for high-mix cells (frequent changeovers)
- Target: <10 minute setups (enable small batches)

**Step 5: Office QRM**
- Create quote-to-order cell (cross-functional team)
- Streamline quoting process (templates, standardization)
- Reduce engineering time (design guidelines, reuse)

**Step 6: Track and Improve MCT**
- Measure MCT weekly
- Kaizen events targeting longest MCT components
- Goal: 50% MCT reduction in Year 1

### QRM Results (Typical)

**Lead Time Reduction:**
- 50-75% MCT reduction common
- Example: 8 weeks → 2-3 weeks

**Business Impact:**
- Win time-sensitive orders (competitive advantage)
- Premium pricing (fast response valued by customers)
- Increased sales (customers prefer fast lead times)

**QRM Success Story:**
```
Small CNC Shop (10 employees):
Before QRM: 6-week lead time, 60% on-time delivery, $1.2M revenue
After QRM (1 year): 1.5-week lead time, 95% on-time delivery, $1.8M revenue (+50%)

Key Changes:
- Implemented 3 QRM cells (shafts, housings, brackets)
- POLCA system (controlled WIP, improved flow)
- SMED (reduced setups from 45 min to 12 min average)
- Office QRM (reduced quote time from 5 days to 1 day)
```

## 17.5 L.E.A.N. Product Development

### Traditional Product Development Challenges

**Common Problems:**
- Long development cycles (18-36 months typical)
- Overdesigned products (features customers don't value)
- Late design changes (costly, delay launch)
- Poor manufacturability (design doesn't consider production constraints)
- Handoff waste (engineering → manufacturing → suppliers, poor communication)

**Result:** Slow time-to-market, high cost, products that miss customer needs.

### L.E.A.N. Product Development Principles

**1. Front-Load Design Decisions:**
- Invest time upfront (thorough planning, concept exploration)
- Evaluate alternatives early (parallel concept development)
- Freeze design earlier (reduce late changes)

**Benefit:** Fewer late changes (reduce cost and delay)

**2. Set-Based Concurrent Engineering:**

**Traditional (Point-Based):**
- Choose one design concept early
- Develop in detail
- If problems emerge, start over (rework)

**L.E.A.N. (Set-Based):**
- Develop multiple concepts in parallel (2-4 alternatives)
- Narrow set gradually (eliminate weak concepts based on data)
- Converge on best solution (informed decision, less rework)

**Example:**
```
Designing housing for aerospace component:

Set-Based Approach:
- Concept A: Aluminum 6061, traditional milling
- Concept B: Aluminum 7075, high-speed machining
- Concept C: Titanium, 5-axis machining
- Concept D: Composite, minimal machining

Evaluate all 4 (manufacturability, cost, weight, strength)
Narrow to 2 best (B and C)
Prototype both
Converge on Concept B (best balance of cost, weight, manufacturability)

Result: Better final design, less rework than point-based
```

**3. Design for Manufacturability (DFM):**
- Involve manufacturing early (not after design complete)
- Design rules (minimize machining complexity, standard tolerances, common materials)
- Feedback loops (prototype, test, refine)

**DFM Checklist (CNC):**
- [ ] Can part be machined with standard tooling?
- [ ] Are tolerances realistic and necessary (not over-specified)?
- [ ] Can part be fixtured easily (stable clamping surfaces)?
- [ ] Material specified is readily available?
- [ ] Design minimizes setups (features accessible without re-fixturing)?
- [ ] Surface finish requirements achievable with standard tooling?

**4. Value Focus (Voice of Customer):**
- Identify customer needs early (not assumptions)
- Prioritize features (critical few vs. nice-to-have)
- Eliminate waste (features that don't add customer value)

**Kano Model:** Classify features
- **Basic Needs:** Must-haves (dissatisfies if missing, doesn't excite if present)
- **Performance Needs:** More is better (satisfaction scales with performance)
- **Delighters:** Unexpected features (excite customers, differentiate)

**Focus development on:** Basics (meet all) + Performance (optimize key attributes) + Delighters (strategically select)

**5. Chief Engineer System (Toyota):**
- Single leader accountable for entire product (concept to launch)
- Authority and responsibility (decision-making power)
- Cross-functional coordination (engineering, manufacturing, suppliers, sales)

**Benefit:** Faster decisions, aligned vision, accountability

**6. Visual Management in Development:**
- **Obeya Room:** "Big room" where team collocates (walls covered with project status, issues, decisions)
- Visual planning (Gantt charts, milestone boards)
- Daily stand-ups (quick alignment, issue resolution)

### Applying L.E.A.N. PD in CNC Shop

**Scenario:** Developing new product line (custom brackets for industrial machinery)

**L.E.A.N. PD Application:**

**Phase 1: Front-Loading (Weeks 1-4)**
- Voice of Customer (interviews with 10 target customers, identify needs)
- Concept generation (engineering generates 4 bracket designs)
- Manufacturability review (machinist input on each concept)
- Narrow to 2 concepts (best balance of customer value and manufacturability)

**Phase 2: Set-Based Development (Weeks 5-8)**
- Parallel prototyping (both concepts machined, tested)
- Cost analysis (material, machining time, yield)
- Customer feedback (show prototypes, gather input)
- Converge on Concept A (best customer feedback, lowest cost)

**Phase 3: Design Refinement (Weeks 9-12)**
- DFM optimization (simplify machining, reduce setups)
- Fixture design (production-ready workholding)
- Process documentation (setup sheets, work instructions)
- Pilot run (10 units, validate process)

**Phase 4: Launch (Week 13)**
- Production release (standardized work in place)
- Visual controls (setup boards, inspection checklists)
- Feedback loop (track scrap, cycle time, customer satisfaction; Kaizen for continuous improvement)

**Result:** 13-week development (vs. 26-week traditional), better design, smooth launch

## 17.6 L.E.A.N. Office and Administrative Processes

### Why L.E.A.N. Office?

**Problem:** Manufacturing gets L.E.A.N. focus, but office processes often neglected.

**Reality:**
- Office processes (quoting, order entry, invoicing, procurement) are full of waste
- Long lead times (quote takes 1 week, order entry takes 3 days)
- Errors (rework, customer dissatisfaction)
- Hidden costs (time, frustration, lost sales)

**Opportunity:** Office L.E.A.N. can deliver similar gains to shop floor L.E.A.N. (50%+ lead time reduction common)

### The Eight Wastes in Office

**1. Defects:**
- Data entry errors (wrong quantities, prices, specifications)
- Incorrect quotes (cost customer goodwill, rework)

**2. Overproduction:**
- Printing reports no one reads
- Generating quotes for unqualified leads

**3. Waiting:**
- Waiting for approvals (bottleneck manager)
- Waiting for information (missing data, emails unanswered)

**4. Non-Utilized Talent:**
- Administrative staff not involved in improvement (ideas ignored)
- Over-qualified staff doing manual data entry (underutilized skills)

**5. Transportation:**
- Excessive email attachments (file versions, confusion)
- Physical paperwork routing (inefficient handoffs)

**6. Inventory:**
- Backlog of unprocessed orders (queue)
- Email inbox overload (hundreds of unread emails)

**7. Motion:**
- Searching for files (poor organization, no standardization)
- Excessive clicks in software (inefficient systems)

**8. Extra Processing:**
- Redundant data entry (same info entered in multiple systems)
- Over-detailed reports (information overload)

### L.E.A.N. Office Tools

**1. Value Stream Mapping (VSM) for Office:**

**Example: Quote-to-Order Process**

**Current State:**
```
Step 1: Customer quote request (email) → Sales inbox
  Wait: 1 day (sales checks email once/day)
Step 2: Sales reviews request, assigns to estimator
  Wait: 0.5 days (estimator backlog)
Step 3: Estimator quotes job (CAM programming time estimate, material cost)
  Process time: 3 hours
  Wait: 2 days (estimator sends to sales for approval)
Step 4: Sales reviews, adjusts price, sends to customer
  Process time: 0.5 hours
  Wait: 1 day (customer responds)
Step 5: Customer accepts, sales enters order in ERP
  Process time: 0.5 hours

Total Lead Time: 5 days
Total Process Time: 4.5 hours
Value-Added Ratio: 4.5 hrs / (5 days × 8 hrs) = 11% (89% waste!)
```

**Future State (L.E.A.N.):**
```
Step 1: Customer uses online quote form (automated)
  Wait: 0 (instant submission, triggers notification)
Step 2: Estimator receives notification, quotes immediately (standardized templates)
  Process time: 1 hour (templates reduce estimate time)
  Wait: 0 (immediate send to customer)
Step 3: Customer receives quote, accepts (click-to-accept)
  Wait: 1 day (customer decision time, unchanged)
Step 4: Order auto-enters ERP (integrated systems)
  Process time: 0 (automated)

Total Lead Time: 1 day
Total Process Time: 1 hour
Value-Added Ratio: 1 hr / (1 day × 8 hrs) = 12.5% (still room for improvement, but 5x faster lead time)
```

**Improvements:**
- Online quote form (standardized input, reduce errors)
- Automated notifications (eliminate waiting for email checks)
- Quote templates (reduce estimate time, improve consistency)
- System integration (eliminate manual order entry)

**Result:** 5 days → 1 day (80% lead time reduction)

**2. 5S for Office:**

**Sort:**
- Digital files: Delete old/obsolete files
- Emails: Unsubscribe from irrelevant lists, delete old emails
- Physical: Remove old documents, obsolete forms

**Set in Order:**
- Digital: Folder structure (logical, standardized)
- Emails: Folders/labels for categories (customers, projects, to-do)
- Physical: File cabinets organized, labeled

**Shine:**
- Digital: Regular file cleanup (quarterly purge)
- Physical: Clean desk policy, organized workspace

**Standardize:**
- File naming conventions (YYYY-MM-DD_ProjectName_Version.docx)
- Email templates (standardized responses)
- Process documentation (SOPs for common tasks)

**Sustain:**
- Monthly 5S audits
- Kaizen (continuous improvement of office organization)

**3. Standardized Work for Office:**

**Example: Order Entry Standardized Work**

**Before (No Standard):**
- Each person enters orders differently (inconsistent, errors)
- Time varies (15-45 min per order, depending on person)

**After (Standardized Work):**
- Step-by-step procedure documented (SOP)
- Time: 10 minutes (consistent)
- Quality: Zero data entry errors (checklist, verification)

**Standardized Work Elements:**
- **Takt Time:** 10 minutes per order (to keep up with demand)
- **Work Sequence:** Defined steps (enter customer, enter line items, verify totals, submit)
- **Standard WIP:** Max 5 orders in queue (pull system, don't overload)

**4. Visual Management for Office:**

**Visual Boards:**
- Quote board (columns: Requested, In Progress, Sent, Won, Lost)
- Order board (columns: Received, Entered, Released to Production, Shipped)
- Kanban board for admin tasks (To Do, In Progress, Done)

**Metrics Displayed:**
- Quote turnaround time (target: <1 day)
- Order entry time (target: <10 min)
- Past-due orders (target: 0)

**Color Coding:**
- Red folder: Urgent (requires action today)
- Yellow folder: Important (requires action this week)
- Green folder: Standard (normal priority)

**5. Kaizen for Office:**

**Small Improvements:**
- Email templates (save time, improve consistency)
- Keyboard shortcuts (reduce clicks, increase speed)
- Dual monitors (reduce window switching)
- Macros/scripts (automate repetitive tasks)

**Kaizen Events:**
- Focus on specific process (quote-to-order, invoicing, purchasing)
- Team brainstorms improvements
- Implement, measure results

### Office L.E.A.N. Results

**Typical Outcomes:**
- 50-75% reduction in process lead time
- 30-50% reduction in errors
- Employee satisfaction increase (less frustration, more value-added work)
- Customer satisfaction increase (faster quotes, accurate orders)

**Example:**
```
CNC Shop Office L.E.A.N. (6-month implementation):
Before:
- Quote turnaround: 4 days
- Order entry errors: 12%
- Customer complaints: 8/month

After:
- Quote turnaround: 1 day (75% reduction)
- Order entry errors: 2% (83% reduction)
- Customer complaints: 1/month (87% reduction)
```

## 17.7 Industry 4.0 and Digital L.E.A.N.

### What is Industry 4.0?

**Industry 4.0:** Fourth industrial revolution, characterized by digitalization, connectivity, and smart manufacturing.

**Key Technologies:**
- **IoT (Internet of Things):** Sensors, connected machines
- **Big Data & Analytics:** Real-time data analysis
- **Cloud Computing:** Centralized data storage, remote access
- **AI/Machine Learning:** Predictive analytics, optimization
- **Digital Twin:** Virtual model of physical system
- **Augmented Reality (AR):** Overlay digital info on physical world

**Industry 4.0 Revolutions:**
1. **Industry 1.0:** Mechanization (steam power, 1760s-1840s)
2. **Industry 2.0:** Mass production (electricity, assembly lines, 1870s-1914)
3. **Industry 3.0:** Automation (computers, CNC, robotics, 1970s-2000s)
4. **Industry 4.0:** Smart manufacturing (connectivity, data, AI, 2010s-present)

### Digital L.E.A.N. Integration

**L.E.A.N. + Industry 4.0 = Powerful Synergy**

**L.E.A.N. Provides:**
- Process optimization (eliminate waste first, then digitize)
- Standardized work (foundation for automation)
- Culture of improvement (leverage technology for Kaizen)

**Industry 4.0 Provides:**
- Real-time data (enhance Gemba, visual management)
- Predictive analytics (anticipate problems before they occur)
- Automation (reduce non-value-added work)
- Connectivity (improve communication, coordination)

**Caution:** Don't digitize waste. Apply L.E.A.N. first (optimize process), then digitize (enhance optimized process).

### Digital L.E.A.N. Applications in CNC

**1. IoT for Real-Time OEE:**

**Traditional OEE:**
- Manual data collection (operator logs downtime, counts parts)
- Delayed reporting (OEE calculated weekly or monthly)
- Inaccurate (human error, incomplete data)

**IoT-Enabled OEE:**
- Sensors on machines (monitor spindle run time, cycle count, alarms)
- Automatic data collection (no manual logging)
- Real-time dashboards (OEE displayed live on screens)
- Alerts (notify supervisor when OEE drops below threshold)

**Result:** Faster response (address downtime immediately), accurate data (eliminate manual errors), continuous visibility (Gemba on screens)

**2. Predictive Maintenance (AI + TPM):**

**Traditional PM:**
- Time-based (replace parts every X hours, regardless of condition)
- Reactive breakdowns (unplanned downtime)

**Predictive Maintenance:**
- Sensors monitor machine health (vibration, temperature, current draw)
- AI analyzes patterns (identify anomalies, predict failures)
- Alert before failure (schedule maintenance during planned downtime)

**Example:**
```
Spindle Bearing Failure Prediction:
- Vibration sensor detects increase in bearing frequency
- AI model predicts failure in 48 hours
- Alert sent to maintenance (schedule bearing replacement during weekend)
- Result: Zero unplanned downtime (vs. 8-hour spindle failure during production shift)
```

**3. Digital Kanban (e-Kanban):**

**Traditional Kanban:**
- Physical cards (can be lost, damaged)
- Manual scanning/movement

**e-Kanban:**
- Digital signals (triggered by barcode scan, sensor, system transaction)
- Automatic replenishment (MRP/ERP generates order when Kanban consumed)
- Real-time visibility (inventory levels displayed on dashboards)

**Example:**
```
Raw Material e-Kanban:
- Operator scans barcode when removing last bar from rack (triggers e-Kanban)
- ERP generates purchase requisition automatically
- Supplier receives order electronically
- Material delivered next day (JIT replenishment)
```

**4. Digital Twin for Process Optimization:**

**Digital Twin:** Virtual model of machine or process that mirrors physical system in real-time.

**Applications:**
- **Simulate before machining:** Test programs in virtual environment (detect collisions, optimize paths)
- **Monitor in real-time:** Virtual twin updates as physical machine runs (visualize process remotely)
- **Optimize:** Test parameter changes in virtual environment (find optimal speeds/feeds without scrap risk)

**Example:**
```
Complex 5-Axis Part:
- Create digital twin of Mazak 5-axis mill
- Load part program, simulate in twin
- Detect near-collision on 4th operation
- Adjust program in simulation
- Verify in twin (zero collisions)
- Load optimized program to physical machine (run confidently)

Result: Zero crash risk, optimized program before first chip
```

**5. Augmented Reality (AR) for Training and Maintenance:**

**AR Applications:**
- **Work instructions:** Overlay step-by-step instructions on machine (operator wears AR glasses, sees setup steps)
- **Maintenance guidance:** AR displays where to check oil, how to replace part (reduce errors, speed training)
- **Remote support:** Expert sees what technician sees (AR glasses), provides guidance in real-time

**Example:**
```
New Operator Setup Training:
- Operator wears AR glasses
- AR overlays fixture placement instructions on machine table (virtual guides)
- Operator follows AR instructions (places vise, clamps part)
- AR verifies correct setup (visual confirmation)
- Result: Faster training, fewer setup errors
```

**6. Cloud-Based MES (Manufacturing Execution System):**

**MES Integration:**
- Real-time production tracking (job status, machine status, operator status)
- Paperless shop floor (digital work orders, digital inspection forms)
- Centralized data (all production data in cloud, accessible anywhere)
- Analytics (identify bottlenecks, optimize scheduling)

**Example:**
```
Cloud MES in CNC Shop:
- Operator scans job traveler barcode (starts job in MES)
- MES displays work instructions on tablet (paperless)
- Operator completes job, scans completion (updates MES)
- MES tracks: Job lead time, machine utilization, operator efficiency
- Manager views dashboard remotely (real-time visibility)
- Weekly report auto-generated (no manual data compilation)
```

### Implementing Digital L.E.A.N. (Phased Approach)

**Phase 1: L.E.A.N. Foundation (Months 1-6)**
- Implement core L.E.A.N. (5S, VSM, SMED, TPM, Kanban)
- Establish stable, standardized processes
- Train team on L.E.A.N. principles

**Phase 2: Basic Digitization (Months 7-12)**
- Manual data collection → Digital data collection (spreadsheets, simple databases)
- Paper work orders → Digital work orders (tablets, MES)
- Manual OEE logs → Automated OEE tracking (sensors, basic IoT)

**Phase 3: Integration and Automation (Year 2)**
- Connect systems (ERP, MES, CAM, inspection)
- Automate workflows (e-Kanban, automatic replenishment)
- Real-time dashboards (OEE, production status, quality)

**Phase 4: Advanced Analytics (Year 3+)**
- Predictive maintenance (AI, machine learning)
- Digital twin (simulation, optimization)
- Advanced analytics (identify patterns, optimize processes)

**Critical Success Factors:**
- ✓ Start with L.E.A.N. (optimize before digitizing)
- ✓ Involve shop floor (operators must see value, not just management)
- ✓ Phased implementation (don't try to do everything at once)
- ✓ Training (team must understand and embrace technology)
- ✓ ROI focus (invest where payback is clear)

## Conclusion

Advanced L.E.A.N. concepts—Theory of Constraints, Lean Six Sigma, Hoshin Kanri, QRM, Lean Product Development, Lean Office, and Digital Lean—provide powerful tools for organizations that have mastered foundational L.E.A.N. practices.

**Key Takeaways:**

1. **Master Fundamentals First:** Don't jump to advanced concepts without solid foundation (5S, VSM, SMED, TPM, Kaizen).

2. **TOC Focuses L.E.A.N.:** Use Theory of Constraints to prioritize improvement efforts (focus on bottleneck for maximum impact).

3. **LSS Combines Speed and Quality:** Lean Six Sigma integrates waste elimination with variation reduction (powerful for high-value processes).

4. **Hoshin Aligns Organization:** Policy deployment ensures everyone works toward same strategic goals (eliminate wasted effort on misaligned initiatives).

5. **QRM Accelerates Job Shops:** Quick Response Manufacturing adapts L.E.A.N. for high-mix, low-volume environments (focus on lead time, POLCA for WIP control).

6. **Lean PD Speeds Development:** Apply L.E.A.N. to product development (front-load decisions, set-based engineering, DFM).

7. **Lean Office Unlocks Hidden Waste:** Office processes are full of waste (VSM, 5S, standardized work, visual management apply to administrative work).

8. **Digital Lean Enhances, Not Replaces:** Industry 4.0 technologies amplify L.E.A.N. gains (IoT for real-time OEE, predictive maintenance, e-Kanban, digital twin), but only after processes are optimized.

**Next Steps:**
- Assess your organization's L.E.A.N. maturity
- Select 1-2 advanced concepts that fit your needs (don't try all at once)
- Pilot in limited area, measure results, scale if successful
- Maintain focus on continuous improvement (PDCA always)

**Advanced L.E.A.N. is a journey, not a destination. Use these tools to continuously improve, adapt to changing markets, and achieve world-class performance.**

---

**Completed:** Section 24.17 – Advanced L.E.A.N. Concepts

**Next Section:** 24.18 – L.E.A.N. for CNC Job Shops (adapting L.E.A.N. tools for high-mix, low-volume environments)

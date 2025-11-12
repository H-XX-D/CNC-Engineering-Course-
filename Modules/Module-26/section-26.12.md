# Module 26 – CNC Business Ownership and Management

## Section 26.12 – Operations Management

### Overview

Operations management is the systematic direction and control of the processes that transform inputs (raw materials, labor, equipment) into outputs (finished products). For a CNC machine shop, excellent operations management is the difference between chaos and efficiency, loss and profit, stress and satisfaction.

While marketing brings customers and sales closes deals, operations management delivers on promises. No amount of excellent sales can compensate for poor operations—late deliveries, quality issues, and inefficiency will destroy customer relationships and profitability.

According to industry research, well-managed machine shops typically achieve:
- 15-25% higher profitability than poorly managed shops
- 30-40% better on-time delivery performance
- 50% lower scrap and rework rates
- 20-30% higher employee productivity
- Significantly lower owner stress and working hours

This section covers the essential systems and practices for managing efficient, profitable CNC shop operations.

## 12.1 Production Planning and Scheduling

### Understanding Production Planning vs. Scheduling

**Production Planning (Strategic):**
- What to produce and when (weeks/months ahead)
- Capacity requirements
- Material procurement timing
- Resource allocation
- Long-term workflow

**Production Scheduling (Tactical):**
- Specific job sequencing (days/weeks)
- Machine assignments
- Operator assignments
- Daily/weekly priorities
- Short-term optimization

Both are essential and interconnected.

### Production Planning Fundamentals

**Capacity Planning:**

Understanding your realistic capacity is the foundation of planning.

**Available Capacity Calculation:**

```
Single Machine Example:

Available hours per day: 8 hours
Working days per month: 22 days (accounting for weekends)
Gross available hours: 176 hours/month

Realistic deductions:
- Setup and programming: 30% (53 hours)
- Maintenance: 5% (9 hours)
- Unplanned downtime: 5% (9 hours)
- Gaps between jobs: 10% (18 hours)

Net available capacity: 87 hours/month (49% utilization)
```

**For accurate planning:**
- Calculate realistic capacity, not theoretical
- Track actual utilization over 3-6 months
- Use historical data for future planning
- Build in buffer for reality (Murphy's Law)

**Forward Loading vs. Backward Scheduling:**

**Forward Loading:**
- Start from today, schedule jobs in sequence
- Shows earliest possible completion dates
- Good for general capacity planning
- May result in late deliveries if overloaded

**Backward Scheduling:**
- Start from due date, work backward
- Determines latest possible start date
- Highlights conflicts and capacity issues
- Better for meeting customer commitments

**Example: Backward Scheduling**

```
Job Due Date: June 30
Required operations:
- Programming: 2 hours
- Setup: 1.5 hours
- Machining: 8 hours
- Inspection: 1 hour
- Finishing (deburr): 1.5 hours
Total time: 14 hours (rounded to 2 days allowing for other work)

Backward schedule:
- June 30: Due date (ship)
- June 29: Final inspection and packaging
- June 27-28: Machining and finishing
- June 26: Programming and setup
- Latest start: June 26
- Material must be available: June 25
```

### Job Sequencing and Prioritization

**Priority Factors:**

When multiple jobs compete for the same resources, how do you decide sequence?

**Weighted Priority System:**

| Factor | Weight | Calculation |
|--------|--------|-------------|
| Due Date | 40% | Days until due (sooner = higher priority) |
| Customer Tier | 25% | A-customer = 3, B = 2, C = 1 |
| Profitability | 20% | Margin % of job |
| Setup Efficiency | 15% | Group similar setups |

**Example Priority Calculation:**

```
Job A: Due in 3 days, A-customer, 45% margin, unique setup
Priority = (3×0.4) + (3×0.25) + (45×0.2) + (1×0.15) = 11.1

Job B: Due in 5 days, B-customer, 35% margin, can batch with current job
Priority = (5×0.4) + (2×0.25) + (35×0.2) + (3×0.15) = 10.95

Run Job A first (higher priority)
```

**Common Sequencing Rules:**

**First In, First Out (FIFO):**
- Simplest rule
- Fair to all customers
- Doesn't optimize for efficiency or profit
- Good for low-mix shops

**Earliest Due Date (EDD):**
- Prioritize by due date
- Minimizes late deliveries
- Doesn't consider profitability
- Can create inefficiency (constant setups)

**Shortest Processing Time (SPT):**
- Quick jobs first
- Maximizes throughput
- Good for customer satisfaction (fast turnaround)
- May delay large important jobs

**Critical Ratio (CR):**
```
CR = (Due Date - Today) / (Remaining Processing Time)

CR < 1.0 = Behind schedule (urgent)
CR = 1.0 = On schedule
CR > 1.0 = Ahead of schedule
```

Prioritize jobs with lowest CR.

**Hybrid Approach (Most Common):**

Combine rules based on situation:
- A-customers: Always priority
- Critical ratio < 1.0: Emergency priority
- Otherwise: Balance between efficiency (batch similar work) and fairness (FIFO)

### Production Planning Tools

**Manual Systems (0-5 jobs in queue):**

**Whiteboard/Dry Erase Board:**
- List of jobs in priority order
- Due dates
- Status (quoted, programming, setup, running, complete)
- Simple, visual, flexible
- Works for solo shops and very small operations

**Job Traveler/Router:**
- Paper document travels with job
- Lists all operations
- Sign-off at each step
- Simple tracking
- Prone to getting lost or damaged

**Spreadsheet (5-15 jobs in queue):**

**Simple Production Schedule:**

```
Job # | Customer | Part | Qty | Due Date | Hours | Status | Priority
------|----------|------|-----|----------|-------|--------|----------
1234  | ABC Inc  | Plate| 50  | 6/25/24  | 12    | Setup  | 1
1235  | XYZ Co   | Block| 25  | 6/27/24  | 8     | Program| 2
1236  | ABC Inc  | Pin  | 100 | 6/28/24  | 6     | Queue  | 3
```

Advantages:
- Flexible and customizable
- Free or low cost
- Easy to learn
- Adequate for small shops

Disadvantages:
- Manual updates required
- No automatic alerts
- Doesn't integrate with quoting or accounting
- Can become chaotic at scale

**Software Systems (15+ jobs in queue):**

**Job Shop Management Software:**

Popular options:
- **E2 Shop System** (comprehensive, expensive)
- **JobBOSS** (mid-market, popular)
- **Paperless Parts** (modern, quoting-focused)
- **Fulcrum** (simple, affordable)
- **Odoo** (open-source, customizable)

Features:
- Integrated quoting, scheduling, invoicing
- Real-time capacity visibility
- Automatic alerts for deadlines
- Material tracking
- Reporting and analytics
- Customer portals

Cost: $200-$1,000/month depending on system and users

**When to Invest in Software:**
- More than 15-20 active jobs at a time
- Multiple machines or employees
- Difficulty tracking status manually
- Missing deadlines due to visibility issues
- Ready to invest $3K-$12K annually

### Scheduling Best Practices

**1. Weekly Planning Session:**

Set aside time each week (Monday morning, Friday afternoon) to:
- Review upcoming week's schedule
- Identify conflicts or capacity issues
- Prioritize jobs
- Ensure material availability
- Communicate with customers if issues

**2. Daily Huddle (if employees):**

15-minute standup meeting each morning:
- What's being worked on today
- Any blockers or issues
- Priorities for the day
- Quick questions and coordination

**3. Visual Management:**

Make schedule visible:
- Whiteboard or monitor in shop
- Everyone sees current priorities
- Updates in real-time
- Reduces questions and confusion

**4. Buffer Time:**

Don't schedule to 100% capacity:
- Plan to 70-80% of available time
- Allows for unexpected issues
- Accommodates rush jobs
- Reduces stress

**5. Setup Batching:**

When possible, group similar jobs:
- Same material
- Same fixture
- Similar features
- Reduces setup time, increases capacity

**6. Communicate Proactively:**

- Update customers on progress
- Alert early if delays anticipated
- Don't wait until due date to reveal problem

## 12.2 Inventory Management

Inventory represents cash tied up in materials. Too much inventory drains cash and space. Too little inventory causes delays and missed opportunities. Balance is key.

### 12.2.1 Raw Material Inventory

**Types of Material Inventory:**

**Stock Material:**
- Common sizes kept on hand
- Standard materials (6061 aluminum, 12L14 steel, etc.)
- Fast-moving items
- Quick turnaround on quotes

**Job-Specific Material:**
- Purchased for specific job
- Exotic or unusual sizes
- Large quantities
- Customer-specified material

**Inventory Strategy by Shop Type:**

**Job Shop (High Mix, Low Volume):**
- Minimal stock material (cash flow concern)
- Mostly job-specific purchasing
- Quick access to local suppliers critical
- Balance: 10-20% stock, 80-90% job-specific

**Production Shop (Low Mix, High Volume):**
- Larger stock of commonly used materials
- Blanket orders with suppliers
- Just-in-time delivery for large quantities
- Balance: 30-50% stock, 50-70% job-specific

**Prototype Shop:**
- Wide variety of small quantities
- Stock common sizes in multiple materials
- Premium paid for quick access
- Balance: 40-60% stock, 40-60% job-specific

**Material Planning:**

**Economic Order Quantity (EOQ):**

Balance between ordering cost and holding cost:

```
EOQ = √(2 × Annual Demand × Order Cost / Holding Cost per Unit)

Example:
Annual demand for 1" 6061 aluminum round: 500 feet
Order cost (time, shipping, processing): $50 per order
Holding cost per foot per year: $2 (storage, capital, risk)

EOQ = √(2 × 500 × 50 / 2)
EOQ = √(25,000)
EOQ ≈ 158 feet per order

Order 158 feet at a time (or round to 12-foot lengths = 13 pieces)
```

**Reorder Point:**

When to reorder to avoid running out:

```
Reorder Point = (Demand per Day × Lead Time in Days) + Safety Stock

Example:
Average usage: 10 feet/day
Supplier lead time: 5 days
Safety stock: 2 days worth = 20 feet

Reorder Point = (10 × 5) + 20 = 70 feet

When inventory drops to 70 feet, place order
```

**ABC Analysis:**

Categorize inventory by value and usage:

**A-Items (High Value, High Usage):**
- 20% of items, 80% of value
- Tight control, frequent review
- Optimize ordering
- Examples: Common aluminum plate, standard steel rounds

**B-Items (Medium Value/Usage):**
- 30% of items, 15% of value
- Moderate control
- Periodic review
- Examples: Less common materials, moderate usage

**C-Items (Low Value, Low Usage):**
- 50% of items, 5% of value
- Loose control
- Order as needed or keep minimal stock
- Examples: Exotic materials, rarely used sizes

**Material Storage and Organization:**

**Best Practices:**

**1. Clear Labeling:**
- Material type and grade
- Size
- Purchase date
- Heat number (if critical)
- Job allocation (if job-specific)

**2. Organized Storage:**
- Vertical racks for plate and bar stock
- Horizontal racks for sheet
- Small parts bins for offcuts
- Keep similar materials together
- FIFO arrangement (first in, first out)

**3. Offcut Management:**

Decision tree for remnants:
- >24" useful length → Label and store (may use again)
- 12-24" → Save if common material, scrap if exotic
- <12" → Usually scrap unless special need

Keep offcut inventory under control:
- Review quarterly
- Scrap old or odd pieces
- Offcuts can become clutter costing space and time

**4. Tracking System:**

Minimum tracking:
- What material is in inventory
- Quantity on hand
- Location
- Reserved for specific jobs (if applicable)

Can use:
- Spreadsheet (small shops)
- Inventory module in job shop software
- Barcode system (advanced)

### 12.2.2 Tooling and Consumables

**Tooling Inventory Challenges:**

- High variety (hundreds of different tools)
- Wide price range ($5 drill to $500 specialty cutter)
- Wear and breakage (consumable)
- Hard to predict usage
- Expensive to have too much or too little

**Tooling Categories:**

**Standard Consumables:**
- Common drills, end mills, taps
- High turnover
- Keep stock on hand
- Order from distributor or online

**Special/Job-Specific Tools:**
- Custom tools for specific job
- Expensive
- Order as needed
- May keep if likely to repeat

**Durable Tooling:**
- Holders, collets, vises, fixtures
- Long life
- Capital investment
- Expand as needed

**Tooling Inventory Strategy:**

**Stock Tools (Keep on Hand):**

Based on usage analysis:
- Top 20 most-used tools (80/20 rule)
- Common sizes: #7 drill, 1/4-20 tap, 1/2" end mill, etc.
- 2-3 pieces of each stock tool
- Reorder when stock drops to 1

**Just-In-Time Tools:**
- Special or rarely-used tools
- Order when job requires
- Build into job lead time
- Keep if job repeats

**Vendor-Managed Inventory (VMI):**

For larger shops:
- Tooling distributor stocks consignment inventory at your location
- You use tools, they invoice and replenish
- No capital tied up
- Always have stock available
- Pay small monthly fee or slight price premium

**Tracking Tooling:**

**Minimum Tracking:**
- List of stock tools and par levels
- Physical inventory check monthly
- Reorder when low

**Better Tracking:**
- Tool usage by job (track cost accurately)
- Tool life tracking (predict replacement)
- Supplier and pricing database
- Inventory value tracking

**Consumables:**

**Common Consumables:**
- Cutting fluid/coolant
- Shop rags
- Deburring tools and abrasives
- Measuring fluids (layout blue, DyKem)
- Safety supplies (gloves, glasses, first aid)
- Cleaning supplies
- Office supplies

**Strategy:**
- Keep 30-60 day supply on hand
- Bulk purchase common items for cost savings
- Subscribe-and-save for predictable items
- Review annually for cost optimization

### 12.2.3 Work in Progress (WIP)

**WIP Definition:**

Jobs that are started but not complete. Material has been purchased, labor invested, but no revenue collected yet.

**WIP Challenges:**

**Cash Flow Impact:**
- Cash invested (material, labor) but not yet recovered
- Can't invoice until delivered
- Large WIP ties up significant cash

**Space Impact:**
- Partially completed jobs take up valuable floor space
- Clutter and disorganization
- Risk of damage or mixing up parts

**Scheduling Impact:**
- WIP represents committed capacity
- Must be completed before new work can start
- High WIP reduces flexibility

**Optimal WIP Management:**

**1. Limit WIP:**

**Lean principle: Minimize WIP to expose problems and improve flow**

Target: Complete jobs quickly rather than starting many jobs

**2. First In, First Out (FIFO):**

Finish what you start before starting new work:
- Reduces WIP
- Improves delivery time
- Prevents jobs from languishing

**3. Track WIP:**

Know at all times:
- What jobs are in progress
- Current status of each
- Value invested in each
- Expected completion

**4. Complete Jobs:**

Don't let jobs sit 90% complete:
- Common problem: last step delays (deburr, inspect, package)
- Set target: Complete within 1 week of machining
- Push completions, not just starts

**5. WIP Inventory:**

Monthly review:
- List all WIP jobs
- Age of each (days in progress)
- Value (material + labor invested)
- Action: Complete or escalate if aging

**Red Flag:** Job in WIP for >30 days without good reason (waiting customer approval, on hold, etc.)

### 12.2.4 Finished Goods

**When Finished Goods Inventory Makes Sense:**

**Production Shops:**
- Make-to-stock for regular customers
- Buffer inventory for stable demand
- Smooths production (make ahead in slow periods)

**Repeat Jobs:**
- Customer orders same part quarterly
- Make extra quantity, deliver over time
- Better efficiency, reduced setup frequency

**Consignment:**
- Stock inventory at customer location
- Customer uses as needed, invoices periodically
- Requires strong customer relationship and trust

**When to Avoid Finished Goods:**

**Job Shops:**
- High variety, low repeat
- Tying up cash in unsold inventory
- Risk of obsolescence

**Custom Work:**
- Parts designed for specific customer application
- No other use if customer doesn't take delivery
- Make-to-order only

**Finished Goods Management:**

**If You Hold FG Inventory:**

**1. Clear Ownership:**
- Customer PO and commitment to purchase
- Consignment agreement
- Your speculation (risky)

**2. Storage:**
- Organized, labeled clearly
- Protected from damage
- Segregated by customer
- Easy to locate and ship

**3. Tracking:**
- Quantity on hand
- Customer/PO
- Production date
- Shelf life (if applicable)

**4. Invoicing:**
- Standard: Invoice when shipped
- Consignment: Invoice when used
- Payment terms start from invoice

**5. Aging Review:**

Monthly review:
- FG >60 days old: Contact customer for delivery
- FG >90 days old: Escalate, get commitment or invoice
- FG >120 days old: Problem (customer changed plans, dispute, etc.)

## 12.3 Quality Control Systems

Quality control is not just inspection—it's a comprehensive system to ensure parts consistently meet specifications.

**Quality System Components:**

### 1. Incoming Inspection

**Material Verification:**

Upon receipt:
- Visual inspection (damage, corrosion, defects)
- Dimensional check (thickness, diameter)
- Material certification review (if provided)
- Hardness test (if critical)

**Document and accept or reject**

Many small shops skip this and later discover:
- Wrong material shipped
- Wrong size
- Damaged in shipping
- Non-conforming material

**Best Practice:** 5-10 minute incoming inspection saves hours of scrap and rework.

### 2. First Article Inspection (FAI)

**Before running production quantity:**

- Set up job
- Run one complete part
- Inspect fully against drawing
- Verify all dimensions, features, finishes
- Adjust process if needed
- Document acceptance
- Proceed with production

**Benefits:**
- Catches setup errors before making multiple bad parts
- Provides baseline for production
- Customer approval opportunity (for critical jobs)
- Reduces scrap

**FAI Documentation:**

For critical jobs or customers:
- Inspection report with actual measurements
- Comparison to drawing specs
- Sign-off by inspector and customer (if required)
- AS9102 standard for aerospace

### 3. In-Process Inspection

**During production run:**

- Periodic checks (every 5th part, 10th part, hourly, etc.)
- Verify critical dimensions
- Check tool wear (dimension drift)
- Catch problems before completing full run

**Frequency depends on:**
- Run quantity (more frequent for large runs)
- Process stability
- Part criticality
- Historical data

**Example: 100-piece run**
- FAI: First part (full inspection)
- In-process: Parts 10, 25, 50, 75 (critical dimensions)
- Final: Last part (full inspection)

### 4. Final Inspection

**Before packaging and shipping:**

- Visual inspection (burrs, damage, finish)
- Dimensional inspection (per drawing requirements)
- Functional check (if applicable)
- Quantity verification
- Documentation

**Inspection Levels:**

**Visual Only:**
- Simple parts
- Non-critical applications
- Trusted repeat jobs

**Sample Inspection:**
- Inspect 10% of parts
- Statistical sampling
- Medium-risk applications

**100% Inspection:**
- Critical applications (aerospace, medical)
- First-time jobs
- Customer requirement
- High-risk consequences

### 5. Inspection Documentation

**What to Document:**

**Minimum (All Jobs):**
- Certificate of Compliance (CoC): "Parts manufactured per drawing XXX, Rev Y"
- Quantity shipped
- Date
- Inspector signature

**Standard (Most Jobs):**
- CoC
- Inspection report (actual measurements for key dimensions)
- Material certification (if provided by mill)

**Full Documentation (Critical Jobs):**
- Complete FAI report
- Material cert with heat traceability
- In-process inspection records
- Final inspection report
- Calibration records for inspection equipment
- AS9102 or similar formal standard

**How Long to Retain:**
- Minimum: Duration of warranty period
- Standard: 7 years (matches tax records)
- Aerospace/Medical: Lifetime of product (can be decades)

### Quality Tools and Equipment

**Essential Inspection Tools:**

**Startup Shop Minimum:**
- 6" calipers (digital): $50-150
- 0-1" micrometer: $100-200
- Pin gauges set: $50-100
- Radius gauges: $20
- Thread gauges: $50-100
- Height gauge or depth micrometer: $100-200
- Square and straight edge: $50
- **Total: ~$500-$1,000**

**Growing Shop Additions:**
- Full micrometer set (0-6"): $500-1,000
- Indicator and mag base: $150-300
- Bore gauges: $200-500
- Thread micrometers: $150-300
- **Total: ~$1,500-$3,000**

**Advanced Shop:**
- Optical comparator: $3,000-10,000
- CMM (Coordinate Measuring Machine): $15,000-100,000+
- Surface roughness tester: $2,000-5,000
- Hardness tester: $3,000-10,000

**Calibration:**

Inspection equipment must be calibrated:
- Frequency: Annually (minimum), quarterly for critical tools
- Traceable to NIST standards
- Documented calibration certificates
- Out-of-tolerance tools removed from service

**Cost:**
- Caliper calibration: $30-50 each
- Micrometer calibration: $40-60 each
- Full shop calibration service: $300-1,000 annually

**DIY calibration (informal):**
- Gage blocks (calibrated reference standards): $200-1,000
- Check tools against gage blocks
- Document results
- Not acceptable for aerospace/medical but adequate for commercial work

## 12.4 Equipment Maintenance Programs

**Maintenance Philosophy:**

**Reactive (Run to Failure):**
- Fix when it breaks
- Minimal planned maintenance
- Lowest short-term cost
- Highest long-term cost (downtime, damage, lost production)

**Preventive (Time-Based):**
- Scheduled maintenance regardless of condition
- Based on calendar or hours
- Prevents most failures
- Some unnecessary maintenance

**Predictive (Condition-Based):**
- Monitor equipment condition
- Maintain based on actual need
- Optimal timing
- Requires monitoring systems and expertise

**For Small CNC Shops: Preventive maintenance is the practical approach**

### Preventive Maintenance (PM) Program

**Daily Maintenance (Operator):**

**Before starting machine:**
- Visual inspection (leaks, damage, unusual conditions)
- Clean work area and machine
- Check coolant level
- Verify chip evacuation working
- Lubrication check (auto-lube systems)

**End of shift:**
- Clean machine and work area
- Remove chips from machine
- Check for any issues noticed during run
- Log any problems

**Weekly Maintenance:**

- Detailed cleaning (ways, covers, table)
- Coolant top-off and condition check
- Lubricate manually-greased points
- Inspect tooling and tool holders
- Check air pressure
- Clean filters (if accessible)

**Monthly Maintenance:**

- Coolant change or treatment (depending on type)
- Hydraulic fluid level check
- Air filter replacement/cleaning
- Way oil reservoir check
- Inspect belts for wear
- Check for unusual noises or vibration
- Backup CNC program storage

**Quarterly Maintenance:**

- Detailed inspection of all systems
- Lubrication of all grease points
- Spindle taper cleaning and inspection
- Ball screw inspection
- Way condition check
- Coolant system cleaning
- Electrical cabinet cleaning (blow out dust)

**Annual Maintenance:**

- Full machine inspection by technician (may be DIY or professional)
- Accuracy check (laser alignment if warranted)
- Major coolant system service
- Replace worn components proactively
- Update any software/firmware
- Calibration verification

**Maintenance Tracking:**

**Minimum:**
- Maintenance log book
- Record date and what was done
- Note any issues found

**Better:**
- Scheduled PM checklist
- Sign-off when completed
- Issue tracking log
- Parts and supply usage log

**Software:**
- CMMS (Computerized Maintenance Management System)
- Automatic reminders based on calendar or hours
- History tracking
- Spare parts inventory

**For most small shops, a simple spreadsheet or notebook is adequate.**

### Spare Parts Strategy

**Critical Spares (Keep on Hand):**

Parts that would shut you down:
- Fuses and circuit breakers (correct ratings)
- Common belts (if applicable)
- Coolant pump (backup or rebuild kit)
- Air filters
- Basic electronics (contactors, relays specific to your machine)

**Readily Available (Order as Needed):**

- Toolholders (can get overnight)
- Collets (can get quickly)
- Standard fasteners
- Spindle bearings (if standard)

**Long Lead Time (Consider Stocking):**

- Machine-specific components
- Obsolete electronics for older machines
- Specialty bearings
- Control system components for older controls

**Balance:** Stock critical items that have long lead times. Don't over-invest in spares that are readily available.

**Vendor Relationships:**

- Establish relationship with local machine tool distributor
- Know who to call for emergency service
- Have parts diagrams and manuals accessible
- Keep list of serial numbers and specifications for ordering parts

## 12.5 Shop Floor Management

### 12.5.1 Daily Operations

**Daily Routine for Solo Shop:**

**Morning (30-60 min):**
- Check emails and messages
- Review schedule for day
- Prioritize tasks
- Ensure material and tooling available for day's work
- Quick shop walkthrough (clean, organized, safe?)

**Production Time (5-6 hours):**
- Focus on machining
- Minimize interruptions
- Batch similar tasks
- Take breaks to avoid fatigue errors

**Administrative Time (1-2 hours):**
- Quote follow-up
- Invoicing
- Ordering materials/tools
- Customer communication
- Planning next day

**End of Day (30 min):**
- Clean up shop
- Update job status
- Note any issues or needs for tomorrow
- Quick review: what got done, what didn't, why

**Daily Routine with Employees:**

**Morning Huddle (15 min):**
- Review today's priorities
- Assign tasks
- Address any blockers or issues
- Safety reminder
- Questions and coordination

**Throughout Day:**
- Monitor progress
- Problem-solving as issues arise
- Quality checks
- Customer communication
- Administrative work

**End of Day Review (10 min):**
- Recap accomplishments
- Identify any issues for tomorrow
- Thank team
- Confirm next day's plan

### 12.5.2 Problem Solving

**When Problems Arise:**

**Immediate Response Framework:**

**1. Assess (1-5 minutes):**
- What happened?
- Is anyone hurt? (safety first)
- Is equipment damaged?
- Is the part salvageable?
- What's the immediate impact?

**2. Contain (5-30 minutes):**
- Make safe
- Prevent further damage
- Isolate problem parts
- Protect other jobs from issue

**3. Communicate (Immediately):**
- Inform customer if delivery affected
- Alert team if equipment down
- Call for help if needed (technical support, etc.)

**4. Solve (Variable):**
- Quick fix if possible
- Proper fix if more involved
- Temporary workaround if waiting on parts/help

**5. Document (5-10 minutes):**
- What happened
- Root cause
- Solution implemented
- Preventive action

**Problem-Solving Method: 5 Whys**

**Example:**

**Problem:** Part scrapped due to wrong hole location

**Why #1:** Why was hole in wrong location?
→ Operator used wrong work offset

**Why #2:** Why did operator use wrong work offset?
→ Program called for G54, operator set up in G55

**Why #3:** Why did program and setup not match?
→ No standard procedure for work offset assignment

**Why #4:** Why is there no standard procedure?
→ Never documented best practices

**Why #5:** Why weren't best practices documented?
→ No system for capturing and sharing knowledge

**Root Cause:** Lack of documented procedures
**Solution:** Create standard work offset procedures and train team

### 12.5.3 Continuous Improvement

**Kaizen Philosophy:**

Small, incremental improvements over time create dramatic results.

**Continuous Improvement Culture:**

**1. Measure:**
- Track key metrics (see Section 16.5)
- Baseline current performance
- Identify trends

**2. Identify Opportunities:**
- What's causing problems repeatedly?
- Where do we waste time?
- What frustrates customers?
- What frustrates team?

**3. Prioritize:**
- Impact vs. effort matrix
- Quick wins (high impact, low effort) first
- Long-term initiatives second

**4. Implement:**
- Small experiments
- Test changes
- Measure results
- Standardize what works

**5. Repeat:**
- Never stop improving
- Celebrate progress
- Keep looking for next opportunity

**Improvement Examples:**

**Setup Time Reduction:**
- Shadow board for tools (find tools faster)
- Presetting tools offline
- Standard work holding
- 20% setup time reduction = 20% more capacity

**Quality Improvement:**
- First article inspection standard
- Setup checklist
- Scrap rate from 5% to 2% = 3% margin improvement

**Material Handling:**
- Organize stock by material type
- Label clearly
- Reduce time finding material from 15 min to 3 min per job

**Communication:**
- Standard quote template
- Faster quote response
- Win rate improves 5%

**Small improvements compound over time.**

## 12.6 Documentation and Procedures

### Why Documentation Matters

**Benefits:**
- Consistency (same result every time)
- Training (new employees learn faster)
- Quality (reduces errors and rework)
- Efficiency (don't reinvent the wheel)
- Scalability (knowledge doesn't live only in your head)
- Sellability (business has value beyond owner)

**Resistance:**
"I don't have time to write things down" is common objection.

**Reality:**
- Time spent documenting is recovered many times over
- Repeating explanations takes more time than writing once
- Mistakes from lack of documentation cost far more than documentation time

### What to Document

**Priority 1: Safety Procedures**

- Machine operation safety
- Emergency procedures
- Lockout/tagout
- First aid
- Chemical handling (cutting fluids, etc.)

**Priority 2: Critical Processes**

- Setup procedures for complex jobs
- First article inspection process
- Quality control requirements
- Shipping and packaging standards

**Priority 3: Standard Operating Procedures (SOPs)**

- Machine startup and shutdown
- Coolant management
- Tool presetting
- Quoting process
- Customer communication standards

**Priority 4: Job-Specific Documentation**

- Setup sheets for repeat jobs
- Fixture and work holding documentation
- Tool lists and feeds/speeds
- Inspection requirements
- Photos of setup

**Priority 5: Administrative Procedures**

- Quote process and templates
- Order processing
- Invoicing and payment
- Purchasing
- Vendor management

### Documentation Formats

**Simple and Practical:**

**One-Page Laminated Sheets:**
- Post near machine or process
- Visual with photos
- Bullet point steps
- Protects from shop environment

**Setup Sheets:**
```
JOB: ABC-12345 - Aluminum Adapter Plate
MATERIAL: 6061-T6 Aluminum, 1" Plate
FIXTURE: Kurt 6" Vise, Parallels
PROGRAM: ABC12345_V3.nc
WORK OFFSET: G54
TOOLS:
  T1: 1/2" 4-flute end mill (face)
  T2: #7 Drill (thru hole)
  T3: 1/4-20 Tap
  T4: 1/8" 2-flute end mill (pocket)
INSPECTION: Check dimensions A, B, C, and thread depth
NOTES: Watch for burr on exit of holes
```

**Photo Documentation:**
- Take photos of complex setups
- Store with job file
- Invaluable for repeat jobs

**Video (Advanced):**
- Record complex setups or procedures
- Great for training
- Smartphone video adequate
- Store in shared drive or YouTube (private)

**Where to Store:**

**Physical:**
- Binder or folder by machine
- Job traveler with job
- Posted on wall/machine

**Digital:**
- Shared drive (Google Drive, Dropbox, etc.)
- Job shop management software
- Wiki or knowledge base

**Accessible to who needs it, when they need it**

## 12.7 Technology and Software Systems

### 12.7.1 ERP (Enterprise Resource Planning)

**What is ERP?**

Integrated software system managing all business processes:
- Quoting and estimating
- Order management
- Scheduling
- Inventory
- Accounting
- Customer management
- Reporting

**Examples for Machine Shops:**
- E2 Shop System
- JobBOSS
- Shoptech
- Global Shop Solutions

**Benefits:**
- Single source of truth (all data in one system)
- Automated workflows
- Real-time visibility
- Reduced data entry
- Better decision-making

**Drawbacks:**
- Expensive ($10K-$50K+ setup, $300-$1,000+/month)
- Complex implementation (3-12 months)
- Requires training and discipline
- Overkill for very small shops

**When to Consider:**
- 5+ employees
- $1M+ annual revenue
- Multiple machines
- Complexity overwhelming simpler tools
- Ready to invest time and money

### 12.7.2 Job Tracking Software

**Simpler than full ERP:**

Focus on job management without full accounting integration

**Examples:**
- Paperless Parts (quoting and job management)
- Fulcrum (simple job tracking)
- Odoo (open-source, modular)
- Custom spreadsheets/databases

**Benefits:**
- Less expensive than full ERP ($50-$300/month)
- Easier to implement
- Focused functionality
- Good middle ground

**When to Consider:**
- 2-5 employees
- $250K-$1M revenue
- Outgrowing spreadsheets
- Not ready for full ERP investment

### 12.7.3 CAM Software

**Essential for CNC shops:**

**Entry Level:**
- Fusion 360 ($495/year, includes CAD+CAM)
- FreeCAD + CNC tools (free, limited)
- BobCAD-CAM ($1,500-$5,000)

**Mid-Level:**
- HSMWorks (Included with SolidWorks)
- MasterCAM Mill ($4,000-$6,000 base)
- SurfCAM ($4,000-$8,000)

**Professional:**
- MasterCAM (with modules): $10,000-$30,000
- Esprit ($15,000-$40,000)
- GibbsCAM ($10,000-$25,000)

**Selection Criteria:**
- Type of work (2.5D, 3D, multi-axis)
- Machine compatibility
- Learning curve
- Post processor quality
- Support and training
- Budget

**Most Common Progression:**
1. Start with Fusion 360 or entry-level
2. Learn fundamentals
3. Upgrade if capabilities needed and revenue supports

### 12.7.4 Inventory Management Systems

**Levels of Sophistication:**

**Level 1: Spreadsheet**
- List of materials and quantities
- Manual updates
- Free, simple
- Works for <50 SKUs

**Level 2: Dedicated Inventory Software**
- Barcode scanning
- Automatic reorder points
- Integration with purchasing
- $50-$300/month
- Examples: Sortly, inFlow, Fishbowl

**Level 3: Integrated with ERP/Job Software**
- Automatic consumption when job starts
- Real-time inventory levels
- Material costing accuracy
- Part of larger system cost

**For Most Small Shops:**
- Start with spreadsheet
- Move to dedicated system when inventory >100 items or frequent stock-outs
- Move to integrated when implementing full ERP

## Conclusion

Operations management is where strategy meets reality. You can have the best equipment, excellent customers, and strong sales—but if operations are chaotic, inefficient, or unreliable, the business will struggle.

**Key Takeaways:**

1. **Planning and Scheduling:** Realistic capacity planning and smart scheduling maximize efficiency and on-time delivery.

2. **Inventory Management:** Balance between too much (cash tied up) and too little (delays and lost opportunities).

3. **Quality Systems:** Consistent quality comes from systems, not just skill. Implement inspection at critical points.

4. **Maintenance:** Preventive maintenance prevents expensive failures and downtime. Small investment, large return.

5. **Daily Management:** Structured routines, problem-solving frameworks, and continuous improvement mindset drive excellence.

6. **Documentation:** What's written down can be repeated, taught, and improved. Undocumented knowledge is fragile.

7. **Technology:** Right-sized technology improves efficiency. Start simple, upgrade as complexity and revenue justify.

**Action Items:**

1. **Assess Current State:**
   - How effective is your current scheduling?
   - How well do you manage inventory?
   - Do you have documented procedures?
   - Rate each area: Green/Yellow/Red

2. **Prioritize Improvements:**
   - Which operational issues cause the most problems?
   - What quick wins are available?
   - What requires longer-term investment?

3. **Implement One Change:**
   - Don't try to fix everything at once
   - Pick one high-impact improvement
   - Implement fully, measure results
   - Then move to next

4. **Build Systems:**
   - Start documenting critical procedures
   - Create simple tracking systems
   - Train team on standards
   - Review and improve continuously

**Remember:**

Operations excellence is not achieved overnight. It's built through:
- Consistent daily disciplines
- Learning from problems
- Incremental improvements
- Systems and documentation
- Commitment to quality and efficiency

The shops that thrive long-term are those that build robust operational systems, not just rely on heroic individual effort.

**Next Section:**

Move on to Section 13: Customer Relationship Management, where we'll explore how to build and maintain profitable customer relationships.

---

*"Perfect is the enemy of good. Don't wait for perfect systems before starting. Start with simple systems and improve them over time. Progress over perfection."*

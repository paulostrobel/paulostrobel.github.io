---
layout: page
title: 5MW Data Center Thermal Optimization
description: 5MW facility pre-construction CFD analysis delivering 247% improvement in thermal compliance
img: assets/img/projects/chile-datacenter-thumb.jpg
importance: 1
category: work
client: Scala Data Center / Torres Eng.
---

## Client Profile

**Industry:** Scala Data Center / Torres Eng.  
**Location:** Chile  
**Facility:** 5MW critical mission environment with 640 server racks  
**Project Type:** Pre-construction thermal optimization and failure scenario analysis

---

## The Challenge

The client faced critical thermal management challenges in their planned 5MW data center facility before construction. The initial HVAC design featured 30 fan coil units (15 per side) with direct wall-mounted air delivery, but preliminary analysis revealed severe thermal distribution problems:

- **Only 26.9% of rack intake area** met ASHRAE recommended temperature ranges
- High-velocity air jets created recirculation zones in cold aisles
- Short distance between air supply grilles and equipment caused inadequate air distribution
- Hot spots formed at the beginning of rack rows, threatening equipment reliability
- Need to validate system resilience against equipment failures before construction

**Stakes:** Poor thermal design would result in equipment throttling, reduced lifespan, and potential downtime in a mission-critical facility. Post-construction fixes would be prohibitively expensive.

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.html path="assets/img/projects/chile-initial-temp.jpg" title="Initial Design Temperature Distribution" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Initial design showing significant hot spots (red zones) in cold aisles with only 26.9% of rack area meeting ASHRAE guidelines.
</div>

---

## Our Approach

### Phase 1: Initial Assessment

- Developed detailed CFD models
- Modeled 640 racks with 7.81kW heat dissipation per rack
- Simulated airflow patterns, temperature distributions, and pressure gradients throughout the facility
- Analyzed against ASHRAE TC 9.9 thermal guidelines for data centers

### Phase 2: Design Optimization

- Tested multiple air supply configurations including:
  - Variable jet angles (15°, 30°, 45°)
  - Bidirectional vs. unidirectional grilles
  - Strategic placement of flow resistance at cold aisle entrances
- Created automated Python workflows for rapid design iteration
- Evaluated 10+ configurations to identify optimal solution

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.html path="assets/img/projects/chile-velocity-vectors.jpg" title="Velocity Distribution Analysis" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Top view of elocity contour of plane 1.5m above the ground
</div>

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.html path="assets/img/projects/chile-intermediate.png" title="Intermediate Design Iterations" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Iterative testing of different air supply angles and flow patterns to optimize thermal distribution.
</div>

### Phase 3: Resilience Testing

- Simulated 4 equipment failure scenarios:
  - Adjacent fan coil failures
  - Opposite aligned fan coil failures
  - End-position equipment failures
- Conducted transient analysis to predict thermal response over time
- Compared 50% capacity vs. complete system shutdown scenarios

---

## Technical Specifications

**Cooling System:**

- 30 CRAH units @ 56,000 m³/h each
- Supply temperature: 21°C
- External air intake: 12,400 m³/h @ 9°C
- Hot aisle containment with plenum return

**CFD Methodology:**

- Solver: Finite volume RANS with k-ε turbulence model
- Convergence criteria: 1,000 iterations or 10⁻⁴ residuals
- Transient simulations: 30-second intervals with 0.5 second reporting

---

## Results & Impact

### Thermal Performance Improvement

<div class="row justify-content-sm-center">
    <div class="col-sm-8 mt-3 mt-md-0">
        {% include figure.html path="assets/img/projects/chile-final-temp.jpg" title="Optimized Design Temperature Distribution" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Final optimized design achieving 93.7% thermal compliance with uniform temperature distribution across all 640 racks.
</div>

**Key Metrics:**

- **Increased compliant rack area from 26.9% to 93.7%** (247% improvement)
- **Achieved 93.7% RCI_HI** (Rack Cooling Index) approaching industry target of 100%
- **Eliminated all critical hot spots** in initial design
- **Maintained uniform temperature distribution** across 640 racks

| Metric                 | Initial Design | Final Design | Improvement    |
| ---------------------- | -------------- | ------------ | -------------- |
| RCI_HI (% Compliant)   | 26.9%          | 93.7%        | +247%          |
| Hot Spots              | Multiple       | None         | 100% reduction |
| Temperature Uniformity | Poor           | Excellent    | Significant    |

### Solution Implementation

The optimal configuration featured:

- Strategic flow resistance at cold aisle entrances to reduce jet velocity
- Perpendicular air supply orientation
- Improved air distribution uniformity across all equipment rows

### Failure Scenario Insights

- **Scenario 1 (Adjacent failures):** Local temperature impact in 3 corridors
- **Scenarios 2 & 3 (Opposite failures):** Minimal impact due to door containment
- **Scenario 4 (End position):** Limited impact with slight temperature increase
- **System resilience:** Facility showed local response to failures rather than cascading effects

<div class="row">
    <div class="col-sm-6 mt-3 mt-md-0">
        {% include figure.html path="assets/img/projects/chile-failure-scenario.png" title="Failure Scenario Analysis" class="img-fluid rounded z-depth-1" %}
    </div>
<div class="caption">
    Equipment failure scenario testing
</div>
    <div class="col-sm-6 mt-3 mt-md-0">
        {% include figure.html path="assets/img/projects/chile-transient.png" title="Transient Response" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
   Transient thermal response showing time-to-failure predictions.
</div>

### Transient Analysis

- Complete system shutdown: Temperature exceeded limits within 30 seconds
- 50% capacity operation: Slower degradation but inadequate for sustained operation
- Critical time-to-failure data provided for UPS and backup system design

---

## Client Benefits

**Pre-Construction Value:**

- **Avoided costly post-construction remediation** by identifying design flaws before building
- **Enabled informed decisions** on HVAC capacity and redundancy requirements
- **Reduced project risk** through validated thermal performance predictions

**Operational Excellence:**

- Equipment temperatures maintained within ASHRAE recommended ranges
- Extended server lifespan through optimal thermal conditions
- Improved energy efficiency through optimized airflow distribution
- Clear understanding of failure mode impacts for operational planning

**Documentation & Knowledge Transfer:**

- Comprehensive technical report with temperature maps and velocity distributions
- Failure scenario playbook for operations team
- Transient response data for emergency procedures

---

## Technologies & Methods

**CFD Software:**

- ANSYS CFX
- OpenFOAM
- Custom RANS solvers with k-ε turbulence modeling

**Workflow Automation:**

- Python (parametric studies and post-processing)
- Automated mesh generation scripts
- Batch simulation management

**Visualization:**

- Tecplot (temperature contours and velocity vectors)
- Paraview (3D flow visualization)
- Custom reporting templates

---

## Project Deliverables

**Timeline:** 6 weeks

**Outputs:**

- Initial assessment and baseline CFD model
- 10+ design iterations with optimization recommendations
- 4 failure scenario simulations
- Transient analysis (2 scenarios)
- Final technical report with implementation guidelines
- Operations playbook for equipment failure response

<!-----

<div class="row justify-content-sm-center">
    <div class="col-sm-10 mt-3 mt-md-0">
        <blockquote class="blockquote">
            <p>"The pre-construction CFD analysis saved us from what would have been a catastrophic thermal design. The detailed failure scenarios gave us confidence in our redundancy planning."</p>
            <footer class="blockquote-footer">Project Engineering Lead, SCALA</footer>
        </blockquote>
    </div>
</div>

----->

## Related Projects

This case study demonstrates expertise applicable to:

- Mission-critical facility design
- HVAC system optimization
- Thermal management for high-density computing
- Pre-construction design validation
- Failure mode and effects analysis (FMEA)

**Industries served:** Data Centers, Telecommunications, Financial Services, Cloud Computing

**Interested in similar optimization for your facility?** [Contact me](/contact/) to discuss your thermal management challenges.

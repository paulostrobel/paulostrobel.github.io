---
layout: page
title: Data Center Thermal Excellence Through Plenum Design
description: 2.4MW facility with innovative plenum-based air distribution
img: assets/img/projects/chile-datacenter-thumb.png
importance: 2
category: work
---

## Client Profile

**Industry:** Scala Data Center  
**Location:** Chile  
**Facility:** 2.4MW critical mission environment with 366 server racks  
**Project Type:** Pre-construction thermal design optimization with resilience testing

---

## The Challenge

The client facility required a robust HVAC design capable of handling mixed rack densities (7.09kW server racks and 5kW network equipment) while maintaining thermal uniformity across 11 rack rows. The project faced several critical challenges:

- **Mixed heat load management:** Integration of 320 high-density server racks (7.09kW) with 46 network racks (5kW) requiring uniform cooling
- **Plenum-based distribution complexity:** Designing efficient air delivery through lateral plenum systems serving 14 CRAH units
- **Equipment failure resilience:** Validating system performance under 12+2 redundancy scenarios
- **Pre-construction validation:** No physical prototypes available; design decisions required complete confidence


<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.html path="assets/img/projects/curauma-geometry.png" title="Geometric Model" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    CFD geometric model showing 366 racks, lateral plenum distribution, and CRAH placement strategy.
</div>

---

## Our Approach

### Phase 1: Advanced Modeling Strategy
- Developed comprehensive CFD model using finite volume RANS solvers
- Implemented dual-density rack modeling: 7.09kW (server) and 5kW (network) loads
- Created detailed plenum geometry including supply and return air paths
- Validated mesh independence and convergence criteria 

### Phase 2: Flow Optimization
- Designed perforated screens at cold aisle entrances to condition airflow
- Optimized plenum opening areas strategically:
  - 60% porosity at extreme left opening (opposite unpaired rack row)
  - 70% porosity at fourth opening from left
  - 80% porosity for remaining openings
- Created 80% effective area screens at cold aisle entrances

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.html path="assets/img/projects/curauma-mesh.png" title="Numerical Mesh" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.html path="assets/img/projects/curauma-optimization.png" title="Flow Optimization Process" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Left: High-fidelity numerical mesh. Right: Iterative optimization of plenum opening configurations.
</div>

### Phase 3: Failure Scenario Analysis
- Simulated 2 critical failure scenarios:
  - Opposite CRAH units in-line failure
  - Adjacent CRAH unit failure
- Adjusted operating conditions for remaining units (57,341 m³/h at 23.7°C)
- Quantified temperature differentials across all CRAH units under failure conditions
- Validated plenum effectiveness in attenuating failure impacts

---

## Technical Specifications

**Cooling System:**
- 14 CRAH units @ 49,150 m³/h each (normal operation)
- 12 CRAH units @ 57,341 m³/h each (failure mode)
- Supply temperature: 23.1°C (normal), 23.7°C (failure mode)
- Hot aisle containment with overhead plenum return
- Lateral plenum distribution with optimized openings

**Rack Configuration:**
- 320 server racks @ 7.09kW each
- 46 network racks @ 5kW each
- Total IT load: 2.4MW at 100% simultaneity
- 11 rack rows with strategic equipment placement

---

## Results & Impact

### Exceptional Thermal Performance

<div class="row justify-content-sm-center">
    <div class="col-sm-8 mt-3 mt-md-0">
        {% include figure.html path="assets/img/projects/curauma-results-temp.png" title="Temperature Distribution" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Final design achieving 99% RCI_HI with near-perfect temperature uniformity across all rack intakes.
</div>

**Key Metrics:**
- **Achieved 99% RCI_HI** (Rack Cooling Index) - exceptional performance
- **Near-perfect thermal uniformity** across 366 racks
- **All equipment within ASHRAE A1-A4 recommended range** (18-27°C)
- **Zero hot spots** in normal operation

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.html path="assets/img/projects/curauma-results-velocity.png" title="Velocity Distribution" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.html path="assets/img/projects/curauma-results-inlet.png" title="Rack Inlet Temperatures" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Left: Optimized velocity distribution at 1.5m height. Right: Rack inlet temperature compliance map.
</div>

### Innovative Plenum Design Success

The strategic use of variable-porosity screens and plenum distribution delivered:

**Screen Configuration Results:**
- Variable porosity openings (60-80%) balanced flow distribution
- Cold aisle entrance screens (80% porosity) conditioned airflow velocity
- Eliminated recirculation zones common in direct-supply designs
- Enabled uniform air delivery despite mixed rack densities

**Design Features:**
- Plenum system effectively distributed airflow across 14 CRAH units
- Lateral supply configuration minimized jet impingement effects
- Overhead return plenum simplified routing and pressure drop
- 5% infiltration tolerance validated containment effectiveness

### Failure Scenario Validation

<div class="row justify-content-sm-center">
    <div class="col-sm-10 mt-3 mt-md-0">
        {% include figure.html path="assets/img/projects/curauma-failure-scenarios.png" title="Failure Scenarios Tested" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Two critical failure scenarios tested: opposite in-line units and adjacent units.
</div>

**Scenario 1: Opposite In-Line Failure**
- RCI maintained at 99% - negligible impact
- Plenum distribution effectively compensated for lost units
- No significant temperature increase in any zone

**Scenario 2: Adjacent Unit Failure**  
- RCI remained at 99% with minor local effects
- Small non-compliant area with maximum temperature below 35.4°C (within A2 limits)
- Remaining CRAH units showed balanced load increase (11-15°C ΔT)

| CRAH Unit | Base Operation ΔT | Scenario 1 ΔT | Scenario 2 ΔT |
|-----------|------------------|---------------|---------------|
| CRAH 1 (N/S) | 10.2°C / 9.6°C | 12.7°C / 13.4°C | 11.6°C / 10.9°C |
| CRAH 2 (N/S) | 12.0°C / 11.3°C | FAILED | 14.0°C / 12.2°C |
| CRAH 3 (N/S) | 12.2°C / 11.8°C | 14.2°C / 14.1°C | 14.0°C / 13.2°C |
| CRAH 4 (N/S) | 12.7°C / 11.9°C | 14.4°C / 14.2°C | FAILED / 13.8°C |
| CRAH 5 (N/S) | 13.5°C / 13.1°C | 15.2°C / 14.0°C | FAILED / 14.2°C |

*Note: Temperature differential between return and supply air*

<div class="row">
    <div class="col-sm-6 mt-3 mt-md-0">
        {% include figure.html path="assets/img/projects/curauma-failure1-results.png" title="Scenario 1 Results" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col-sm-6 mt-3 mt-md-0">
        {% include figure.html path="assets/img/projects/curauma-failure2-results.png" title="Scenario 2 Results" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Failure scenario results demonstrating robust thermal resilience through plenum design.
</div>

---

## Client Benefits

**Pre-Construction Confidence:**
- **Validated design before equipment procurement**, eliminating costly redesign risks
- **Proven 12+2 redundancy effectiveness** through comprehensive failure testing
- **Quantified CRAH loading** under normal and failure conditions for maintenance planning
- **Design documentation** providing operational baseline for future modifications

**Operational Excellence:**
- 99% of rack intake area within ASHRAE recommended temperatures
- Uniform cooling distribution despite mixed rack densities
- Exceptional system resilience with minimal failure impact
- Optimized energy efficiency through balanced CRAH loading

**Technical Innovation:**
- Variable-porosity plenum opening design maximizes flow uniformity
- Cold aisle entrance screens eliminate high-velocity jet effects
- Plenum-based distribution proves superior to direct-supply approach
- Mixed-density rack cooling methodology applicable to future expansions

**Risk Mitigation:**
- Computed performance under worst-case failure scenarios
- Documented temperature differentials guide preventive maintenance
- Pre-construction optimization avoided field modifications
- Hot spot elimination prevents equipment throttling and failures

---

## Technologies & Methods

**CFD Software:**
- ANSYS CFX 
- OpenFOAM 
- Dual-solver approach ensures result reliability

**Advanced Techniques:**
- Variable-porosity modeling for screen optimization
- Mixed heat load modeling for dual rack types
- Plenum flow distribution analysis
- Black-box rack methodology with momentum sources

**Automation & Efficiency:**
- Parametric screen porosity studies
- Batch simulation management for failure scenarios
- Automated convergence monitoring
- Python post-processing for temperature analysis

**Visualization:**
- Tecplot (temperature and velocity contours)
- Paraview (3D flow visualization)
- Custom ASHRAE compliance filtering
- Comparative failure scenario displays

---

## Project Deliverables

**Timeline:** 5 weeks

**Outputs:**
- Baseline CFD model with optimized plenum configuration
- Variable-porosity screen specification for fabrication
- 2 comprehensive failure scenario analyses
- CRAH loading tables for normal and failure operations
- Temperature differential tracking for maintenance scheduling
- Final technical report with ASHRAE compliance validation
- Design recommendations for future capacity expansion

---

<div class="row justify-content-sm-center">
    <div class="col-sm-10 mt-3 mt-md-0">
        <blockquote class="blockquote">
            <p>"The plenum optimization and failure analysis gave us complete confidence in our design. Achieving 99% thermal compliance before construction is exceptional."</p>
            <footer class="blockquote-footer">Engineering Lead, SCALA Data Centers</footer>
        </blockquote>
    </div>
</div>

---

## Key Differentiators

This project demonstrates advanced capabilities in:

**Plenum-Based Distribution Design:**
- Unlike simpler direct-supply systems, this approach requires sophisticated flow modeling
- Variable porosity optimization demands parametric CFD analysis
- Demonstrates expertise in complex air distribution networks

**Mixed-Density Cooling:**
- Successfully integrated 7.09kW and 5kW rack types in single environment
- Maintained uniform cooling despite 40% heat load variation
- Applicable to multi-tenant or phased deployment scenarios

**Failure Mode Engineering:**
- Comprehensive redundancy validation beyond typical "N+1" analysis
- Quantified impacts on remaining equipment during failures
- Provided operational guidelines for maintenance scenarios


---

## Related Expertise

This case study demonstrates expertise applicable to:
- High-density data center thermal design
- Plenum-based air distribution systems
- Mission-critical facility redundancy planning
- Multi-zone mixed-load cooling optimization
- HVAC failure mode and effects analysis (FMEA)

**Industries served:** Data Centers, Telecommunications, Financial Services, Healthcare IT Infrastructure

**Planning a mission-critical facility?** [Contact me](/contact/) to discuss thermal design validation and optimization strategies for your data center project.

---

## Comparison with Direct-Supply Approach

| Aspect | Direct Supply | Plenum Distribution (This Project) |
|--------|--------------|-----------------------------------|
| Flow uniformity | Moderate | Excellent (99% RCI) |
| Jet impingement risk | High | Eliminated |
| Failure resilience | Local impact | Distributed compensation |
| Mixed density handling | Challenging | Seamless |
| Installation complexity | Lower | Moderate |
| Operational flexibility | Limited | High |

---


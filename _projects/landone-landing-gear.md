---
layout: page
title: Landing Gear Shock Absorber Analysis – LANDOne Project
description: Multi-fidelity CFD framework for next-generation landing gear systems with ML-accelerated optimization
img: /assets/img/projects/landone-thumb.png
importance: 1
category: work
client: Airbus/Cranfield University
---

## Client Profile

**Industry:** Aerospace (Landing Gear Systems)
**Location:** UK (Multi-partner consortium)
**Project:** LANDOne - £37.8M Innovate UK/ATI initiative ([grant 10002411](https://gtr.ukri.org/projects?ref=10002411))
**Project Type:** Multi-fidelity CFD framework development with ML-accelerated design optimization

**Consortium Partners:** Airbus UK (Industrial Lead), University of Sheffield, Cranfield University, Safran Landing Systems, Triumph Group, Transense Technologies, and additional aerospace partners

---

## My Role

**Position:** Research Fellow in Multiphysics Software Development at Cranfield University

**Work Package:** Design Capability for Shock Absorbers (£798K)

I lead the development of automated multiphysics workflows in HPC/Cloud infrastructure for landing gear shock absorber systems. Key responsibilities include developing the SALSA software platform, building ML surrogate models, establishing validation protocols against NASA benchmarks, and delivering technical training workshops to consortium partners including Airbus.

---

## The Challenge

Landing gear shock absorbers are critical safety components that must perform reliably across extreme operating conditions. Traditional design methodologies relied on expensive physical testing and simplified analytical models, creating several challenges:

- **Limited Design Space Exploration:** Physical prototyping costs constrained parametric studies of orifice geometries, fluid properties, and dynamic profiles
- **Certification Requirements:** Need for validated computational methods and NASA aerospace standards
- **Computational Cost:** High-fidelity CFD simulations required days per case, preventing systematic optimization
- **Multi-Scale Complexity:** Performance must be validated across aircraft scales from military trainers to A320-class commercial aircraft
- **Transient Flow Physics:** Capturing cavitation, vortex shedding, flow separation, and compressibility effects in complex orifice geometries

**Stakes:** Inadequate shock absorber design impacts landing safety, aircraft certification timelines, and maintenance costs. The aerospace industry needed validated computational frameworks to accelerate development while meeting stringent certification standards.

<p align="center">
<img width="640" src="/assets/img/projects/shockabs.gif">
</p>
<div class="caption">
    Shock absorber compression showing fluid dynamics during landing impact.
</div>



---

## Our Approach

### Phase 1: Multi-Fidelity Framework Development

- Developed systematic Design of Experiments (DoE) approach integrating three fidelity levels
- **Low-Fidelity:** Rapid lumped-parameter physics models in Python (seconds per case)
- **Medium-Fidelity:** 2D axisymmetric RANS with k-ω SST turbulence (hours per case)
- **High-Fidelity:** 3D unsteady RANS with multiphase VOF and dynamic mesh (days per case)
- Validated framework across aircraft scales against NASA Milwitzky experimental data

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        <img src="/assets/img/projects/joblist_workflow.svg" title="SALSA joblist workflow" class="img-fluid rounded z-depth-1">
    </div>
</div>
<div class="caption">
    Automated Multi-Case Shock Absorber Simulation Pipeline for preprocessing, mesh generation, CFD solving, and post-processing
</div>

---

### Phase 2: SALSA Software Platform

Led development of SALSA (Shock Absorber simuLation SoftwAre), an open-source Python-based automation platform:

- **Parametric Geometry Generation:** FreeCAD/Gmsh-based with support for circular, semi-circular, square, and cutback orifice designs
- **Automated Workflow Management:** Preprocessing, mesh generation, multi-solver CFD (OpenFOAM, UCNS3D), and post-processing
- **Advanced Simulation Capabilities:** Static inlet flow, multiphase VOF, dynamic piston, dynamic orifice, and combined motion
- **Batch Processing:** CSV-based job list processing with HPC cluster integration (SLURM/PBS)

**Impact:** Reduces simulation setup time from days to hours, enabling systematic exploration of 44,236+ validated CFD cases.

---

### Phase 3: Validation & ML Acceleration

**Validation Protocols:**
- Benchmark against NASA Milwitzky drop test data (agreement within 5% for peak forces)
- Dixon and Ding discharge coefficient correlations (agreement within 3%)
- Cross-solver verification (OpenFOAM vs. Fluent)
- Mesh independence and timestep convergence studies

**Machine Learning Surrogate Models:**
- Training dataset: 44,236+ high-fidelity CFD cases
- Model performance: R² > 0.95 for force prediction, R² > 0.92 for discharge coefficient
- Computational speedup: 20-50x vs. direct CFD simulation
- Real-time prediction: <10ms per case enabling genetic algorithm optimization

<div class="row justify-content-sm-center">
    <div class="col-sm-8 mt-3 mt-md-0">
        <img src="/assets/img/projects/milwitzky-validation.png" class="img-fluid rounded z-depth-1">
    </div>
</div>
<div class="caption">
    Force-displacement validation against NASA Milwitzky drop test data.
</div>

---

## Technical Specifications

**Computational Tools:**
- **CFD Solvers:** OpenFOAM/Fluent (multiphase, dynamic mesh), UCNS3D (high-fidelity unsteady)
- **Turbulence Modeling:** k-ω SST (baseline), k-ε, LES for validation
- **Mesh Generation:** Gmsh 4.x with Python API
- **ML Framework:** TensorFlow/PyTorch, DEAP genetic algorithms

**Performance Metrics:**
- Typical simulation time: 6-48 hours on 64 cores
- Mesh sizes: 200K-2M cells for production runs
- Parallel efficiency: >85% scaling up to 128 cores

**HPC Infrastructure:**
- Cranfield Delta2: 512 cores, InfiniBand interconnect
- UK National Tier-1: ARCHER2
- Cloud platforms: AWS EC2

---

## Results & Impact

### Orifice Geometry Optimization

**Key Metrics:**
- **Achieved 30.3% efficiency improvement** through optimized geometry selection
- Characterized performance across circular, semi-circular, square, and cutback designs
- Semi-circular geometry reduces cavitation occurrence by 40% vs. sharp-edged designs
- Discharge coefficient validation: Cd = 0.74-0.77 (within 3% of Dixon theory)

| Geometry | Damping Performance | Cavitation Risk | Recommendation |
|----------|---------------------|-----------------|----------------|
| Rectangular | Highest pressure | High | Specific fluids applications |
| Semi-circular | Optimal balance | Low | Standard applications |
| Circular | Baseline | Medium | Standard applications |
| Cutback | Enhanced flow | High | Specific fluids and applications |

### Dynamic Mesh Capabilities

Successfully simulated coupled piston-orifice motion for adaptive damping systems:
- Reynolds number range: 6.4×10⁸ (highly turbulent flow)
- Peak pressure differential: 5.45 MPa
- Maximum domain velocity: 122 m/s through orifice contraction
- Validated against high-speed photography (oil splash arrival: 0.03s)

<p align="center">
  <img src="/assets/img/projects/phase_zoom.gif" width="100%" />
</p>
<p align="center">
  <img src="/assets/img/projects/phase.gif" width="100%" />
</p>
<div class="caption">
    Transient simulation: oil-air phase fraction showing interface dynamics during shock absorber compression.
</div>

<p align="center">
  <img src="/assets/img/projects/velocity.gif" width="100%" />
</p>
<div class="caption">
    Velocity field evolution through the orifice during dynamic compression.
</div>

<p align="center">
  <img src="/assets/img/projects/pressure.gif" width="100%" />
</p>
<div class="caption">
    Pressure distribution showing damping force generation through the orifice.
</div>

<p align="center">
  <img src="/assets/img/projects/temperature.gif" width="100%" />
</p>
<div class="caption">
    Temperature field showing thermal effects from viscous dissipation in the hydraulic fluid.
</div>

<p align="center">
  <img src="/assets/img/projects/dynamicorifice.gif" width="50%" />
</p>
<div class="caption">
   Dynamic mesh motion for metering pin simulations enabling variable damping analysis.
</div>

---

## Client Benefits

**Accelerated Development:**
- Reduce simulation setup time from days to hours (90% time savings)
- Enable rapid design space exploration with multifidelity apporah
- Systematic optimization delivering 30.3% efficiency improvements on damping performance withing orifice selection
- Parallel parameter studies: 100+ cases executed simultaneously

**Certification Support:**
- Validated methodologies 
- Comprehensive documentation supporting airworthiness approval
- Benchmark results against NASA experimental data (<5% error)
- Risk mitigation through validated virtual testing

**Cost Reduction:**
- Minimize expensive physical prototyping
- Identify optimal designs before manufacturing
- Design guidelines preventing cavitation-induced failures
- Enable "right first time" design philosophy

**Technical Innovation:**
- Open-source platform supporting future programs
- ML-accelerated optimization framework applicable to other components
- Multi-fidelity approach balancing accuracy and computational cost

---

## Technologies & Methods

**CFD Software:**
- OpenFOAM/Fluent: multiphase VOF, turbulence, dynamic mesh
- UCNS3D: high-fidelity open-source unsteady simulations
- Dual-solver approach ensures result reliability

**Automation & Efficiency:**
- Python 3.8+ (NumPy, Pandas, PyVista, Matplotlib)
- Gmsh parametric mesh generation
- HPC job management (SLURM, PBS)
- Git/GitHub with CI/CD pipelines

**Visualization:**
- ParaView 5.x (3D interactive visualization)
- PyVista (automated plot generation)
- Custom dashboards for design exploration

---

## Project Deliverables

**Timeline:** Ongoing (2022-present)

**Outputs:**
- Shock Absorber Software Suite: 15,000+ lines documented Python code
- Multi-fidelity CFD framework with OpenFOAM/UCNS3D integration
- ML surrogate models trained on 44,236+ LowFidelity cases
- Validation database against NASA and theoretical benchmarks
- Technical documentation
- Workshop materials and training for consortium partners
- 3 peer-reviewed publications, 5 conference presentations

---

## Key Differentiators

**Multi-Fidelity Integration:**
- Seamless transition between low, medium, and high-fidelity simulations
- Automated fidelity selection based on design stage requirements
- ML-driven computational resource optimization

**Aerospace-Grade Validation:**
- Rigorous V&V against NASA experimental data
- Cross-validated against multiple theoretical correlations

**Open-Source Innovation:**
- SALSA platform available for future landing gear programs
- Extensible to hydraulic actuators, fuel systems, dampers
- Technology transfer to automotive, defense, and industrial applications

---

## Related Expertise

This case study demonstrates expertise applicable to:
- Aerospace component design and optimization
- Multi-fidelity simulation frameworks
- Machine learning for engineering applications
- High-performance computing workflows
- Certification and standards compliance
- Multiphase flow and dynamic mesh CFD

**Industries served:** Aerospace, Defense, Automotive, Transportation, Industrial Machinery

---

*This work was conducted at Cranfield University as part of the LANDOne consortium (Innovate UK grant 10002411), a UK aerospace initiative advancing landing gear technology for next-generation aircraft.*

**Interested in applying advanced CFD and machine learning to your engineering challenges?** [Contact me](/contact/) to discuss how multi-fidelity modeling can accelerate your development programs.

---

## Publications

1. Silva, Paulo ASF, et al. "[Study of orifice design on oleo-pneumatic shock absorber](https://doi.org/10.3390/fluids9050108)." *Fluids* 9.5 (2024): 108.
2.  Sheikh Al-Shabab, Ahmed A., Bojan Grenko, **Paulo ASF Silva**, Antonis F. Antoniadis, Panagiotis Tsoutsanis, and Martin Skote. "[Unsteady multiphase simulation of oleo-pneumatic shock absorber flow](https://doi.org/10.3390/fluids9030068)." *Fluids* 9, no. 3 (2024): 68.
  
 3. Sheikh Al-Shabab, Ahmed A., **Paulo ASF Silva**, Bojan Grenko, Panagiotis Tsoutsanis, and Martin Skote. "[A Modular Multifidelity Approach for Multiphysics Oleo-Pneumatic Shock Absorber Simulations](https://dspace.lib.cranfield.ac.uk/server/api/core/bitstreams/278d9949-5469-4068-88f8-c935c6532eb3/content)." In *Cambridge Unsteady Flow Symposium*, pp. 137-151. Cham: Springer Nature Switzerland, 2024.

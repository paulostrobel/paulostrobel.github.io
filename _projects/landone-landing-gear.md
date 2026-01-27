---
layout: page
title: Landing Gear Shock Absorber Analysis – LANDOne Project
description: Multi-fidelity CFD framework for next-generation landing gear systems with ML-accelerated optimization (Research Fellow, Cranfield University)
img: assets/img/projects/landone-thumb.png
importance: 1
category: work
client: Airbus/Cranfield University
---

## Table of Contents
1. [Project Overview](#project-overview)
2. [The Challenge](#the-challenge)
3. [My Role: Research Fellow](#my-role)
4. [Technical Approach](#technical-approach)
   - [Phase 1: Multi-Fidelity Framework](#phase-1)
   - [Phase 2: SALSA Software Platform](#phase-2)
   - [Phase 3: Machine Learning Acceleration](#phase-3)
   - [Phase 4: Validation & Benchmarking](#phase-4)
5. [Technical Specifications](#technical-specifications)
6. [Results & Impact](#results-impact)
7. [Key Deliverables](#key-deliverables)
8. [Technologies & Methods](#technologies-methods)
9. [Skills Demonstrated](#skills-demonstrated)
10. [Client Benefits](#client-benefits)
11. [Future Directions](#future-directions)
12. [Related Expertise](#related-expertise)

---

<a name="project-overview"></a>
## Project Overview

**LANDOne (Landing Advances of the New Decade)** is a £37.8 million UK aerospace initiative funded by Innovate UK ([grant number 10002411](https://gtr.ukri.org/projects?ref=10002411)) and the Aerospace Technology Institute (ATI). Officially launched in 2022, the project is led by Airbus UK as industrial lead in partnership with the University of Sheffield, Cranfield University, and 10 additional aerospace, academic, and research partners. The project focuses on developing next-generation landing gear systems that are lighter, lower maintenance, and more environmentally sustainable.

**My Role:** Research Fellow in Multiphysics Software Development at Cranfield University

**Work Package:** Design Capability for Shock Absorbers (£798K)


**Consortium Partners:** Airbus UK (Industrial Lead), University of Sheffield, Cranfield University, Safran Landing Systems, Triumph Group, Transense Technologies, and additional aerospace industry partners

---
<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.html path="assets/img/projects/landone-thumb.png" title="Design Capability for Shock Absorbers" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Design Capability for Shock Absorbers
</div>



<a name="the-challenge"></a>
## The Challenge

Landing gear shock absorbers are critical safety components that must perform reliably across extreme operating conditions. Traditional design methodologies relied on expensive physical testing and simplified analytical models, creating several challenges:

- **Limited Design Space Exploration:** Physical prototyping costs constrained parametric studies of orifice geometries, fluid properties, and dynamic profiles
- **Certification Requirements:** Need for validated computational methods meeting DO-178C and NASA aerospace standards
- **Computational Cost:** High-fidelity CFD simulations required days per case, preventing systematic optimization
- **Multi-Scale Complexity:** Performance must be validated across aircraft scales from military trainers to A320-class commercial aircraft
- **Transient Flow Physics:** Capturing cavitation, vortex shedding, flow separation, and compressibility effects in complex orifice geometries

**Stakes:** Inadequate shock absorber design impacts landing safety, aircraft certification timelines, and maintenance costs. The aerospace industry needed validated computational frameworks to accelerate development while meeting stringent certification standards.

<p align="center">
<img width="640" height="833" src="/tests/Milwitzky/openfoamcase/imgs/shockabs.gif"></p>

---

<a name="my-role"></a>
## My Role: Research Fellow in Multiphysics Software Development

 I work on the development of a comprehensive multi-fidelity computational framework for oleo-pneumatic landing gear shock absorber analysis as part of the **"Design Capability for Shock Absorbers" work package (£798K)**. My main focus is on developing automated multiphysics workflows in HPC/Cloud infrastructure for landing gear shock absorber systems (LGSAs).

### Work Package Scope

**Aim:** Develop an AI-driven multi-physics (MP) and multifidelity (MF) computational framework for modeling various landing gear shock absorber (LGSA) concepts.

**Key Activities:**
- Development of automated computational multifidelity workflows in HPC/Cloud infrastructure
- Building surrogate models from high-fidelity simulations
- Testing, benchmarking, verification and validation of complete software ecosystem
- Extension to other aircraft sub-systems

**Key Innovation:** Advancing state-of-the-art methods for continuum modeling of multiphysics problems in landing gear shock absorber systems. Delivering an automated intelligent multi-fidelity multi-physics platform where ML techniques enable real-time decision-making regarding fidelity level, equations deployed, numerical methods, and models employed—optimizing computational cost and resources.

**Vision:** Provide an open-source software framework for shock absorber design usable at different design stages through multiple fidelity levels, with AI-driven computational efficiency. Ensure personnel readiness through workshops, tutorials, and documentation, and expand the tool to other aircraft components.

### Key Responsibilities

- **Multiphysics Software Development & Research Delivery:** Develop, maintain, and ensure timely completion of research deliverables, including automated computational workflows in HPC/Cloud infrastructure using OpenFOAM, UCNS3D, and custom Python frameworks
- **SALSA Software Platform Development:** Lead creation of SALSA (Shock Absorber simuLation SoftwAre), managing the open-source software packages and associated modeling/simulation tools developed by the research group
- **HPC & Cloud Computing:** Utilize Cranfield's Delta2 HPC facility, national Tier-1, and international Tier-0 HPC facilities for large-scale parallel computing and simulation campaigns
- **Communication & Publications:** Communicate research outputs through regular meetings, high-quality technical reports, and academic publications
- **Machine Learning Integration:** Build dataset for neural network surrogate models achieving R² > 0.95 for rapid design space exploration, enabling 20-50x computational speedup
- **Verification & Validation:** Establish rigorous software testing, benchmarking, and validation protocols against well-established computational and experimental results
- **Design Optimization:** Implement genetic algorithm optimization delivering  efficiency improvements in shock absorber performance
- **Technology Transfer & Training:** Lead technical training workshops for Airbus  participants and other organizations, providing demonstrations and supporting MSc courses
- **Teaching & Supervision:** Participate in teaching and supervision activities within the CFD msc on the Centre for Computational Engineering Sciences

---

<a name="technical-approach"></a>
## Technical Approach

<a name="phase-1"></a>
### Phase 1: Multi-Fidelity Computational Framework

The framework develops a systematic Design of Experiments (DoE) approach integrating three fidelity levels:

**Low-Fidelity Models:**
- Rapid lumped-parameter physics models for initial design screening
- Implemented in Python with analytical discharge coefficient correlations
- Enable quick parametric sweeps across design space (seconds per case)
- Jupyter notebook interface for interactive exploration

**Medium-Fidelity CFD:**
- 2D axisymmetric Reynolds-Averaged Navier-Stokes (RANS) simulations
- k-ω SST turbulence model for accurate shear layer prediction
- Balance accuracy and computational cost (hours per case)
- OpenFOAM-based solver implementation

**High-Fidelity CFD:**
- 3D unsteady RANS with dynamic mesh capabilities
- Multiphase VOF (Volume of Fluid) method for oil-air interface tracking
- Capture detailed flow physics including transient phenomena
- Computational time: days per case on HPC systems

**Key Achievement:** Successfully validate framework across aircraft scales from military trainers to A320-class commercial aircraft against NASA experimental data (Milwitzky benchmark).

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.html path="assets/img/projects/joblist_workflow.svg" title="SALSA joblist workflow" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Automated Multi-Case Shock Absorber Simulation Pipeline
 for preprocessing, mesh generation, CFD solving, and post-processing stages
</div>

---

<a name="phase-2"></a>
### Phase 2: SALSA Software Platform

Lead development of SALSA (Shock Absorber simuLation SoftwAre), an open-source Python-based automation platform featuring:

**Core Capabilities:**

1. **Parametric Geometry Generation**
   - Transitioned from CATIA to FreeCAD for open-source compatibility
   - Gmsh-based parametric meshing with adaptive refinement
   - Support for multiple orifice geometries:
     - Circular: Standard sharp-edged orifice
     - Semi-circular: Radiused inlet for reduced cavitation
     - Square: Rectangular cross-section for specific applications
     - Cutback: Angled outlet geometry for flow optimization
   - Valve configurations for pressure-controlled systems

2. **Automated Workflow Management**
   - **Preprocessing :**
     - Parameter validation and unit conversion
     - Equation of State (EOS) coefficient generation for hydraulic fluids
     - Piston velocity profile generation and visualization
     - Material property setup (viscosity, specific heat capacity)
   
   - **Mesh Generation:**
     - Automatic directory structure creation
     - Dynamic mesh configuration based on simulation type
     - Boundary condition setup and verification
     - Mesh quality checking and reporting
   
   - **CFD Solving:**
     - Multi-solver support (OpenFOAM, UCNS3D, Fluent)
     - Automatic solver selection:
       - `rhoSimpleFoam`: Steady-state single-phase
       - `rhoPimpleFoam`: Transient single-phase
       - `compressibleInterDyMFoam`: Multiphase with dynamic mesh
     - Parallel decomposition and HPC job management
     - Real-time monitoring and error detection
   
   - **Post-processing:**
     - PyVista-based VTK data extraction
     - Automated visualization generation (contours, animations, time series)
     - Performance metric calculation (discharge coefficient, Reynolds number, cavitation parameter)
     - JSON diagnostic output for database integration

3. **Advanced Simulation Capabilities**
   - **Static Inlet Flow:** Steady-state pressure drop analysis
   - **Multiphase Flow:** Oil-air interface tracking with VOF method
   - **Dynamic Piston:** Moving boundary simulations for compression analysis
   - **Dynamic Orifice:** Metering pin motion for variable damping
   - **Combined Motion:** Simultaneous piston and orifice movement

4. **Batch Processing & Parametric Studies**
   - CSV-based job list processing for large parameter sweeps
   - Automated case generation script
   - Results aggregation and comparative analysis
   - HPC cluster integration with SLURM/PBS scripts

**Impact:** Reduces simulation setup time from days to hours, enabling systematic exploration of design parameters including orifice geometry, fluid properties, and dynamic motion profiles. Generates 44,236+ validated CFD cases for machine learning training.


<a name="phase-3"></a>
### Phase 3: Machine Learning Acceleration

Implement Physics-Informed Neural Networks (PINNs) and surrogate modeling to accelerate design optimization:

**Training Dataset:** 44,236+ high-fidelity CFD cases covering:
- Orifice geometries: circular, semi-circular, square, cutback designs
- L/D ratios from 0.5 to 1.28
- Piston velocities: 0.5 to 3.0 m/s
- Initial pressures: 200 kPa to 800 kPa
- Oil levels: 60% to 90% chamber height
- Temperature ranges: 280 K to 350 K

**Model Architecture:**
- Input features: 28 geometric and operating parameters
- Hidden layers: 5 layers with 128-256 neurons each
- Activation function: ReLU with batch normalization
- Output predictions: Damping force, discharge coefficient, cavitation parameter
- Training approach: 80/10/10 train/validation/test split
- Optimization: Adam optimizer with learning rate scheduling

**Model Performance:**
- R² > 0.95 for force prediction (mean absolute error < 3%)
- R² > 0.92 for discharge coefficient (critical for design validation)
- 20-50x computational speedup vs. direct CFD simulation
- Real-time prediction: <10ms per case on standard CPU

**Application:** Enables real-time design optimization and uncertainty quantification during genetic algorithm iterations, reducing design cycle time from weeks to days.


---

<a name="phase-4"></a>
### Phase 4: Validation & Benchmarking

Establish rigorous validation protocols against multiple reference datasets:

**Primary Validation: NASA Milwitzky Experiments**
- Benchmark against classic shock absorber drop test data
- Validate force-stroke relationships and discharge coefficients
- Achieve agreement within 5% for peak forces
- Confirm cavitation inception predictions

**Theoretical Validation:**
- Dixon discharge coefficient correlations (empirical orifice flow theory)
- Ding discharge coefficient method (Reynolds number dependent)
- Agreement within 3% for L/D ratios 0.5-1.5
- Validate cavitation parameter calculations

**Cross-Solver Verification:**
- OpenFOAM vs. Fluent comparison for selected cases
- Verify consistency of pressure distributions
- Confirm velocity field predictions
- Validate dynamic mesh handling approaches

**Systematic Studies:**
- Mesh independence: Test 4 mesh resolutions (0.5mm to 2mm)
- Timestep convergence: Validate temporal discretization (1e-4s to 1e-3s)
- Turbulence model sensitivity: k-ω SST vs. k-ε comparison
- Multiphase VOF parameter tuning

<p align="center">
<img width="640" height="833" src=""assets/img/projects/milwitzky-validation.png"></p>

<div class="caption">
    Force-displacement validation against NASA Milwitzky drop test data.
</div>

---

<a name="technical-specifications"></a>
## Technical Specifications

**Computational Tools:**
- **CFD Solvers:** 
  - OpenFOAM/Fluent: multiphase, dynamic mesh, compressible flows
  - UCNS3D: high-fidelity unsteady simulations, parallel MPI+OpenMP
- **Turbulence Modeling:** k-ω SST (baseline), k-ε, LES for validation studies
- **Mesh Generation:** Gmsh 4.x with Python API for parametric geometry
- **Programming:** 
  - Python 3.8+ (NumPy, Pandas, PyVista, Matplotlib, Plotly, Pillow)
  - Bash scripting for workflow automation and HPC job submission
  - Fortran (UCNS3D solver development and modifications)
- **Machine Learning:** 
  - TensorFlow 2.x / PyTorch 1.x for neural network development
  - Scikit-learn for data preprocessing and validation
  - Genetic algorithms (DEAP library) for multi-objective optimization
- **Visualization:** 
  - ParaView 5.x for 3D interactive visualization
  - PyVista for automated plot generation
  - Custom Python scripts for dashboard creation
- **HPC Infrastructure:**
  - Cranfield Delta2: 512 cores, InfiniBand interconnect
  - UK National Tier-1 facilities: ARCHER2
  - AWS
- **Version Control:** Git with Github for collaborative development
- **Documentation:** LaTeX for technical reports and

**Validation Standards:**
- NASA technical reporting standards (STD-8719.13B)
- Systematic verification and validation (V&V) methodologies 

**Performance Metrics:**
- Typical simulation time: 6-48 hours on 64 cores (case dependent)
- Mesh sizes: 200K-2M cells for production runs
- Parallel efficiency: >85% scaling up to 128 cores
- Storage requirements: 1-100 GB per detailed case

---

<a name="results-impact"></a>
## Results & Impact

### Orifice Geometry Optimization

**Performance Quantification:**
- Characterize performance differences between circular, semi-circular, square, and cutback orifice designs
- Analyze L/D (Length-to-Diameter) ratios from 0.5 to 1.28 across operating conditions:
  - **Rectangular**: Highest damping pressures but increased cavitation risk
  - **Semi-circular**: Optimal for cavitation mitigation with gradual pressure recovery
  - **Circular**: Baseline configuration with well-established correlations
  - **Cutback**: Enhanced flow efficiency but geometry-sensitive performance
- **Achieve 30.3% efficiency improvement** through optimized geometry selection
- Generate design guidelines for geometry selection based on operating envelope


**Cavitation Analysis:**
- Identify cavitation inception conditions for each geometry
- Cavitation coefficient (Cc) range: 0.27 to 14.1 depending on operating conditions
- Quantify impact on damping force consistency
- Semi-circular geometry reduces cavitation occurrence by 40% compared to sharp-edged designs
- Provide design guidelines to avoid cavitation-induced performance degradation

**Discharge Coefficient Characterization:**
- Validate CFD predictions: Cd = 0.74-0.77 across operating range
- Excellent agreement with Dixon theory: Cd = 0.78 (within 3%)
- Confirm Reynolds number dependency as predicted by Ding correlation
- Generate L/D-specific correction factors for design calculations

---

### Dynamic Mesh Capabilities

Successfully simulate coupled piston-orifice motion for adaptive damping systems:
- Capture transient flow physics including vortex shedding and flow separation
- Validate dynamic mesh handling for moving piston simulations (compression velocities up to 3 m/s)
- Enable analysis of variable-orifice "smart" shock absorber concepts with metering pin motion
- Demonstrate simultaneous piston and orifice movement (most computationally challenging configuration)

**Example Performance Metrics (Dynamic Piston Case):**
- Reynolds number range: 6.4×10⁸ (highly turbulent flow)
- Peak bottom pressure: 8.58 MPa
- Pressure differential: 3.74 MPa (average), 5.45 MPa (peak)
- Oil splash arrival time: 0.03s (validated against high-speed photography)
- Maximum domain velocity: 122 m/s (through orifice contraction)


<p float="center">
  <img src="assets/img/projects/phase.gif" width="33%" />
  <img src="assets/img/projects/velocity.gif" width="33%" />
  <img src="assets/img/projects/pressure.gif" width="33%" />
</p>

<div class="caption">
    Transient simulation results for dynamic piston case: velocity magnitude (left), phase fraction showing oil-air interface (center), and pressure distribution (right)
</div>

<p float="center">
  <img src="assets/img/projects/dynamicorifice.gif" width="33%" />
</p>
<div class="caption">
    Adaptive shock absorber simulation showing simultaneous piston compression and metering pin motion, demonstrating variable orifice area control
</div>


<!-----

### Machine Learning Performance

**Surrogate Model Success:**

| Metric | Value | Impact |
|--------|-------|--------|
| Training Cases | 44,236 | Comprehensive design space coverage |
| Force Prediction R² | >0.95 | High accuracy for damping force (MAE < 3%) |
| Discharge Coefficient R² | >0.92 | Reliable flow characterization |
| Cavitation Parameter R² | >0.90 | Accurate inception prediction |
| Speedup Factor | 20-50x | Enabled real-time optimization (< 10ms per prediction) |
| Training Time | 6 hours | One-time cost on GPU cluster |

**Optimization Results:**
- Genetic algorithm iterations: 100+ generations (5000+ candidates evaluated)
- Design candidates evaluated: 10,000+ via surrogate model
- Computational time saved: 95% reduction vs. pure CFD (weeks → days)
- Final efficiency improvement: 30.3% relative to baseline
- Pareto front identification for multi-objective optimization (damping force vs. cavitation risk)

----->

### Consortium Impact

**Knowledge Transfer:**
- Deliver comprehensive technical documentation (200+ pages of methodology reports)
- Lead workshops for Airbus participants
- Establish best practices for shock absorber CFD analysis
- Create video tutorials and example cases for self-paced learning

**Scalable Methodology:**
- Demonstrate framework applicability from component-level to full aircraft landing gear systems
- Provide foundation for future landing gear development programs
- Extend to other hydraulic systems: actuators, dampers, pressure relief valves

**Publications & Dissemination:**
- 3 peer-reviewed journal articles (published/in review)
- 5 international conference presentations
- Technical reports delivered

---

<a name="key-deliverables"></a>
## Key Deliverables

**Software & Tools:**
1. **SALSA Software Suite:** Fully documented open-source CFD automation platform with:
   - Parametric geometry generation module
   - Automated meshing with quality control
   - Multi-solver integration (OpenFOAM, UCNS3D)
   - Post-processing and visualization pipeline
   - +15,000 lines of documented Python code

2. **Optimization Framework:** 
   - Genetic algorithm implementation with ML acceleration
   - Multi-objective optimization capability 
   - Sensitivity analysis tools
   - Uncertainty quantification module

**Documentation & Training:**
3. **Technical Reports:** 
   - Methodology documentation 
   - Validation studies against NASA and theoretical benchmarks
   - Best practices guide for aerospace CFD
   - Certification compliance documentation (DO-178C alignment)

4. **Workshop Materials:** 
   - 2-day workshop presentations with hands-on exercises
   - Example cases with step-by-step guides
   - Troubleshooting documentation

6. **Validation Database:** 
   - Extensive database benchmarked against NASA experimental data
   - Mesh independence study results
   - Timestep convergence analysis
   - Turbulence model comparison

**Research Outputs:**
7. **Parametric Design Database:** 
   - 44,236+ lowfidelity cases
   - Covering orifice geometries and operating conditions
   - JSON format for machine-readable access
   - Visualization dashboard for interactive exploration

8. **Design Guidelines:** 
   - Geometry selection criteria based on operating envelope
   - Cavitation avoidance strategies
   - Performance optimization recommendations
   - L/D ratio selection charts

---

<a name="technologies-methods"></a>
## Technologies & Methods

**Computational Fluid Dynamics:**
- OpenFOAM/Fluent: multiphase flow (VOF), turbulence modeling, dynamic mesh handling
- UCNS3D: high-fidelity unsteady simulations, parallel MPI+OpenMP, structured/unstructured grids
- Turbulence models: k-ω SST (primary), k-ε (validation), LES (reference cases)
- Multiphase: VOF method with MULES for interface capturing
- Dynamic mesh: layering, morphing, and topology change algorithms
- Compressible flow: Equation of State modeling for hydraulic fluids under extreme conditions

**Programming & Automation:**
- Python 3.8+ (NumPy, Pandas, PyVista, Matplotlib, Plotly, Pillow, SciPy)
- Object-oriented design patterns for modular code architecture
- Bash scripting for workflow automation (10+ production scripts)
- HPC job management: SLURM, PBS integration with automatic error recovery
- Git version control with github CI/CD pipelines
- Docker containerization for reproducible environments

**Engineering Tools:**
- Gmsh 4.x: parametric mesh generation with Python API scripting
- ParaView 5.x: 3D interactive visualization, batch rendering
- FreeCAD: parametric CAD generation (transitioned from CATIA for open-source compatibility)
- LaTeX: technical documentation with TikZ for diagrams
- Jupyter Lab: interactive notebook development for low-fidelity models

**Aerospace Standards:**
- NASA technical reporting standards (STD-8719.13B)
- Systematic validation and verification (V&V) methodologies per ISO/IEC/IEEE 29119
- Traceability matrix for requirements tracking
- Configuration management following industry best practices

**HPC Infrastructure:**
- Cranfield Delta2 HPC cluster (512 cores, InfiniBand network)
- UK National Tier-1 facilities: ARCHER2 access
- International Tier-0: partnership-based access for large campaigns
- Cloud platforms: AWS EC2 instances for development and testing

---

<a name="skills-demonstrated"></a>
## Skills Demonstrated

**Technical Expertise:**
- Advanced CFD for aerospace applications (multiphase, compressible, dynamic mesh)
- Multi-fidelity modeling and simulation framework design
- Machine learning integration with physics-based models (surrogate modeling, optimization)
- Optimization algorithms for engineering design (genetic algorithms, gradient-based methods)
- High-performance computing and workflow automation (MPI, OpenMP, job schedulers)
- Software engineering best practices (version control, testing, documentation, CI/CD)

**Aerospace Domain Knowledge:**
- Landing gear shock absorber physics (hydraulics, gas dynamics, multiphase flow)
- Certification standards (DO-178C, NASA requirements, airworthiness regulations)
- Orifice flow dynamics and cavitation (discharge coefficients, inception criteria)
- Transient multiphase flow phenomena (interface tracking, pressure wave propagation)
- Hydraulic fluid properties and equations of state

**Collaboration & Leadership:**
- Cross-organizational coordination with Airbus UK (Industrial Lead), University of Sheffield, Cranfield University, and 10+ aerospace partners including Safran Landing Systems, Triumph Group, and Transense Technologies
- Technical mentorship and training delivery (18 participants from 7 organizations, 4 workshops)
- Knowledge dissemination to technical and management audiences across the consortium
- Open-source software development and community building (GitHub collaboration)
- Project management: deliverable tracking, milestone planning, risk mitigation

**Software Engineering:**
- Scientific Python development (15,000+ lines of production code)
- Automation and workflow design 
- Documentation and user training (comprehensive guides, self paced tutorials)
- Version control and collaborative development (Git, code reviews)
- Testing and quality assurance (unit tests, integration tests, 95% coverage)
- DevOps practices (Docker, CI/CD pipelines)

---

<a name="client-benefits"></a>
## Client Benefits

**Accelerated Development:**
- Reduce simulation setup time from days to hours through SALSA automation (90% time savings)
- Enable rapid design space exploration with 20-50x ML speedup (weeks → days for optimization)
- Systematic optimization delivering 30.3% efficiency improvements over baseline designs
- Parallel parameter studies: 100+ cases executed simultaneously on HPC

**Certification Support:**
- Validate methodologies meeting DO-178C and NASA standards (certification-ready documentation)
- Comprehensive documentation supporting airworthiness approval (traceability matrices, V&V reports)
- Benchmark results against NASA experimental data (< 5% error on key metrics)
- Risk mitigation through validated virtual testing before physical prototypes

**Cost Reduction:**
- Minimize expensive physical prototyping through validated virtual testing (estimated 60% cost savings)
- Identify optimal designs before manufacturing (reduced iteration cycles)
- Provide design guidelines preventing cavitation-induced failures (improved reliability)
- Enable "right first time" design philosophy

**Technical Innovation:**
- Open-source SALSA platform supporting future programs (reusable framework)
- ML-accelerated optimization framework applicable to other components (actuators, valves)
- Multi-fidelity approach balancing accuracy and computational cost (flexible tool for different design stages)
- Establish computational best practices now adopted across consortium

**Exploitation Opportunities:**
- License specific versions of the developed computational framework for commercial applications
- Abundant exploitation opportunities for other industry applications beyond aerospace:
  - Automotive: suspension systems, dampers
  - Defense: recoil mechanisms, landing systems
  - Industrial machinery: vibration isolation, shock mitigation
- Academic publication and enrichment of teaching curricula in aerospace engineering programs
- Technology transfer to other aircraft components and systems (hydraulic actuators, fuel systems)

---

<a name="future-directions"></a>
## Future Directions

Building on LANDOne foundations, I am expanding expertise toward:

- **Building Aerodynamics & Urban Wind Simulation:** Applying CFD fundamentals to green building design and pedestrian wind environments, leveraging existing multi-fidelity framework
- **Advanced Optimization:** Enhanced multi-objective optimization frameworks for building energy efficiency, extending genetic algorithm approaches to building physics
- **Cloud-Native Workflows:** Containerized simulation pipelines (Docker, Kubernetes) for improved reproducibility and scalability across cloud platforms
- **Digital Twins:** Real-time performance monitoring and predictive maintenance applications, integrating ML surrogate models with sensor data streams
- **Industry 4.0 Integration:** Connecting CFD workflows with IoT sensors and real-time monitoring systems

---

<a name="related-expertise"></a>
## Related Expertise

This case study demonstrates capabilities applicable to:
- Aerospace component design and optimization (landing gear, actuators, fuel systems)
- Multi-fidelity simulation frameworks (low, medium, high fidelity integration)
- Machine learning for engineering applications (surrogate modeling, optimization)
- High-performance computing workflows (parallel CFD, job scheduling, data management)
- Certification and standards compliance (DO-178C, NASA, ISO)
- Open-source scientific software development (GitHub, documentation, community building)
- Multiphase flow simulation (VOF, interface tracking, cavitation)
- Dynamic mesh CFD (moving boundaries, topology changes)

**Industries served:** Aerospace, Defense, Transportation, Renewable Energy, Automotive, Industrial Machinery

---

*This work was conducted at Cranfield University as part of the LANDOne consortium (Innovate UK grant 10002411), a UK aerospace initiative advancing landing gear technology for next-generation aircraft led by Airbus UK as industrial lead.*

**Interested in applying advanced CFD and machine learning to your engineering challenges?** [Contact me](/contact/) to discuss how multi-fidelity modeling can accelerate your development programs.

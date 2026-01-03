---
layout: page
title: Landing Gear Shock Absorber Analysis – LANDOne Project
description: Multi-fidelity CFD framework for next-generation landing gear systems with ML-accelerated optimization
img: assets/img/projects/landone-thumb.png
importance: 1
category: work
---

## Project Overview

**LANDOne (Landing Advances of the New Decade)** is a £37.8 million UK aerospace initiative led by Airbus in partnership with the University of Sheffield, focused on developing next-generation landing gear systems for commercial and military aircraft. The project addresses critical challenges in shock absorber performance prediction and optimization through advanced computational frameworks.

**My Role:** CFD Specialist & Research Engineer

**Duration:** Multi-year collaborative research program

**Consortium:** Airbus, University of Sheffield, and 5 additional aerospace partners

---

## The Challenge

Landing gear shock absorbers are critical safety components that must perform reliably across extreme operating conditions. Traditional design methodologies relied on expensive physical testing and simplified analytical models, creating several challenges:

- **Limited Design Space Exploration:** Physical prototyping costs constrained parametric studies of orifice geometries, fluid properties, and dynamic profiles
- **Certification Requirements:** Need for validated computational methods meeting DO-178C and NASA aerospace standards
- **Computational Cost:** High-fidelity CFD simulations required days per case, preventing systematic optimization
- **Multi-Scale Complexity:** Performance must be validated across aircraft scales from military trainers to A320-class commercial aircraft
- **Transient Flow Physics:** Capturing cavitation, vortex shedding, flow separation, and compressibility effects in complex orifice geometries

**Stakes:** Inadequate shock absorber design impacts landing safety, aircraft certification timelines, and maintenance costs. The aerospace industry needed validated computational frameworks to accelerate development while meeting stringent certification standards.

<!-- Add image: LANDOne project overview or shock absorber geometry -->

---

## My Role: CFD Specialist & Research Engineer

As a CFD specialist within the LANDOne consortium, I developed and delivered a comprehensive multi-fidelity computational framework for oleo-pneumatic landing gear shock absorber analysis. My work bridged fundamental fluid dynamics research with practical aerospace engineering applications, contributing to the advancement of landing gear certification methodologies.

### Key Responsibilities

- **Multi-Fidelity Simulation Framework Development:** Designed and implemented integrated low, medium, and high-fidelity computational models using OpenFOAM, UCNS3D, and custom Python frameworks
- **SALSA Software Development:** Created SALSA (Shock Absorber simuLation SoftwAre), an open-source automated workflow for parametric shock absorber CFD analysis
- **Machine Learning Integration:** Developed neural network surrogate models achieving R² > 0.95 for rapid design space exploration, enabling 20-50x computational speedup
- **Design Optimization:** Implemented genetic algorithm optimization delivering 30.3% efficiency improvements in shock absorber performance
- **Workshop Delivery:** Led technical training sessions for 18 participants from 7 aerospace organizations across the UK consortium
- **Standards Compliance:** Ensured all methodologies met DO-178C and NASA aerospace certification requirements

---

## Technical Approach

### Phase 1: Multi-Fidelity Computational Framework

Developed a systematic Design of Experiments (DoE) approach integrating three fidelity levels:

**Low-Fidelity Models:**
- Rapid lumped-parameter physics models for initial design screening
- Enabled quick parametric sweeps across design space
- Computational time: seconds per case

**Medium-Fidelity CFD:**
- 2D axisymmetric Reynolds-Averaged Navier-Stokes (RANS) simulations
- Balanced accuracy and computational cost
- Computational time: hours per case

**High-Fidelity CFD:**
- 3D unsteady RANS with dynamic mesh capabilities
- Captured detailed flow physics including transient phenomena
- Computational time: days per case

**Key Achievement:** Successfully validated framework across aircraft scales from military trainers to A320-class commercial aircraft.

<!-- Add image: Multi-fidelity framework diagram or workflow -->

---

### Phase 2: SALSA Software Platform

Led development of an open-source Python-based automation platform featuring:

**Core Capabilities:**
- Parametric CAD geometry generation (transitioning from CATIA to FreeCAD)
- Automated mesh generation using Gmsh with adaptive refinement
- Multi-solver support (OpenFOAM, UCNS3D)
- Comprehensive post-processing with PyVista and Matplotlib
- Equation of State (EOS) calculations for hydraulic fluids under extreme conditions
- Batch processing capabilities for large-scale parametric studies

**Impact:** Reduced simulation setup time from days to hours, enabling systematic exploration of design parameters including orifice geometry, fluid properties, and dynamic motion profiles.

<!-- Add image: SALSA workflow diagram or user interface -->

---

### Phase 3: Machine Learning Acceleration

Implemented Physics-Informed Neural Networks (PINNs) and surrogate modeling to accelerate design optimization:

**Training Dataset:** 44,236+ high-fidelity CFD cases covering:
- Orifice geometries: circular, semi-circular, square, cutback designs
- L/D ratios from 0.5 to 1.28
- Various piston velocities and fluid properties

**Model Performance:**
- R² > 0.95 for force prediction
- R² > 0.92 for discharge coefficient
- 20-50x computational speedup vs. direct CFD simulation

**Application:** Enabled real-time design optimization and uncertainty quantification during genetic algorithm iterations.

<!-- Add image: Neural network architecture or training results -->

---

### Phase 4: Validation & Benchmarking

Established rigorous validation protocols:

- Benchmarked against Milwitzky experimental data from NASA Technical Reports
- Validated discharge coefficient predictions against published orifice flow theory
- Cross-verified results between OpenFOAM and UCNS3D solvers
- Systematic mesh independence and timestep convergence studies

---

## Technical Specifications

**Computational Tools:**
- **CFD Solvers:** OpenFOAM, UCNS3D
- **Turbulence Modeling:** k-ω SST, multiphase flow simulation
- **Mesh Generation:** Gmsh with adaptive refinement
- **Programming:** Python (NumPy, Pandas, PyVista, Plotly), bash scripting
- **Machine Learning:** TensorFlow/PyTorch for neural network surrogate models
- **Optimization:** Genetic algorithms for multi-objective optimization
- **Visualization:** ParaView, Matplotlib, custom plotting frameworks
- **CAD:** FreeCAD (transitioning from CATIA)
- **HPC:** Job management on high-performance computing clusters

**Validation Standards:**
- DO-178C aerospace software certification
- NASA technical reporting standards
- Systematic verification and validation methodologies

---

## Results & Impact

### Orifice Geometry Optimization

**Performance Quantification:**
- Characterized performance differences between circular, semi-circular, square, and cutback orifice designs
- Analyzed L/D ratios from 0.5 to 1.28 across operating conditions
- **Achieved 30.3% efficiency improvement** through optimized geometry selection

**Cavitation Analysis:**
- Identified cavitation inception conditions for each geometry
- Quantified impact on damping force consistency
- Provided design guidelines to avoid cavitation-induced performance degradation

<!-- Add image: Orifice geometry comparison results -->

---

### Dynamic Mesh Capabilities

Successfully simulated coupled piston-orifice motion for adaptive damping systems:
- Captured transient flow physics including vortex shedding and flow separation
- Validated dynamic mesh handling for moving piston simulations
- Enabled analysis of variable-orifice "smart" shock absorber concepts

<!-- Add image: Dynamic mesh simulation or vortex visualization -->

---

### Machine Learning Performance

**Surrogate Model Success:**

| Metric | Value | Impact |
|--------|-------|--------|
| Training Cases | 44,236 | Comprehensive design space coverage |
| Force Prediction R² | >0.95 | High accuracy for damping force |
| Discharge Coefficient R² | >0.92 | Reliable flow characterization |
| Speedup Factor | 20-50x | Enabled real-time optimization |

**Optimization Results:**
- Genetic algorithm iterations: 100+ generations
- Design candidates evaluated: 10,000+
- Final efficiency improvement: 30.3%

---

### Consortium Impact

**Knowledge Transfer:**
- Delivered comprehensive technical documentation and training materials
- Led workshops for 18 participants from 7 aerospace organizations
- Established best practices for shock absorber CFD analysis

**Open-Source Contribution:**
- Released SALSA framework to support broader aerospace community
- Published parametric database of validated simulation results
- Documented methodologies for certification compliance

**Scalable Methodology:**
- Demonstrated framework applicability from component-level to full aircraft landing gear systems
- Validated across multiple aircraft scales and operating conditions
- Provided foundation for future landing gear development programs

---

## Key Deliverables

**Software & Tools:**
1. **SALSA Software Suite:** Fully documented open-source CFD automation platform with parametric geometry generation, automated meshing, and post-processing
2. **Trained Neural Networks:** Surrogate models for rapid performance prediction across design space
3. **Optimization Framework:** Genetic algorithm implementation with ML acceleration

**Documentation & Training:**
4. **Technical Reports:** Comprehensive documentation of methodologies, validation studies, and best practices meeting aerospace standards
5. **Workshop Materials:** Training documentation and example cases for consortium partners
6. **Validation Database:** Extensive database of benchmarked results against NASA experimental data

**Research Outputs:**
7. **Parametric Design Database:** 44,236+ validated CFD cases covering orifice geometries and operating conditions
8. **Design Guidelines:** Recommendations for geometry selection, cavitation avoidance, and performance optimization

---

## Technologies & Methods

**Computational Fluid Dynamics:**
- OpenFOAM (multiphase flow, turbulence modeling)
- UCNS3D (high-fidelity unsteady simulations)
- k-ω SST turbulence model
- Dynamic mesh handling for moving geometry
- Equation of State modeling for hydraulic fluids

**Programming & Automation:**
- Python (NumPy, Pandas, PyVista, Plotly)
- Bash scripting for workflow automation
- HPC job management and batch processing
- Git version control

**Machine Learning:**
- Neural networks (TensorFlow/PyTorch)
- Physics-informed neural networks (PINNs)
- Genetic algorithms for optimization
- Surrogate modeling and uncertainty quantification

**Engineering Tools:**
- Gmsh (parametric mesh generation)
- ParaView (3D flow visualization)
- FreeCAD (parametric CAD, transitioning from CATIA)
- LaTeX (technical documentation)

**Aerospace Standards:**
- DO-178C compliance for software certification
- NASA technical reporting standards
- Systematic validation and verification methodologies

---

## Skills Demonstrated

**Technical Expertise:**
- Advanced CFD for aerospace applications
- Multi-fidelity modeling and simulation
- Machine learning integration with physics-based models
- Optimization algorithms for engineering design
- High-performance computing and workflow automation

**Aerospace Domain Knowledge:**
- Landing gear shock absorber physics
- Certification standards (DO-178C, NASA requirements)
- Orifice flow dynamics and cavitation
- Transient multiphase flow phenomena

**Collaboration & Leadership:**
- Cross-organizational coordination with Airbus, University of Sheffield, and 5 aerospace partners
- Technical mentorship and training delivery (18 participants, 7 organizations)
- Knowledge dissemination to technical and management audiences
- Open-source software development and community building

**Software Engineering:**
- Scientific Python development
- Automation and workflow design
- Documentation and user training
- Version control and collaborative development

---

## Client Benefits

**Accelerated Development:**
- Reduced simulation setup time from days to hours through SALSA automation
- Enabled rapid design space exploration with 20-50x ML speedup
- Systematic optimization delivering 30.3% efficiency improvements

**Certification Support:**
- Validated methodologies meeting DO-178C and NASA standards
- Comprehensive documentation supporting airworthiness approval
- Benchmarked results against NASA experimental data

**Cost Reduction:**
- Minimized expensive physical prototyping through validated virtual testing
- Identified optimal designs before manufacturing
- Provided design guidelines preventing cavitation-induced failures

**Technical Innovation:**
- Open-source SALSA platform supporting future programs
- ML-accelerated optimization framework applicable to other components
- Multi-fidelity approach balancing accuracy and computational cost

---

## Future Directions

Building on LANDOne foundations, I am expanding expertise toward:

- **Building Aerodynamics & Urban Wind Simulation:** Applying CFD fundamentals to green building design and pedestrian wind environments
- **Advanced Optimization:** Enhanced multi-objective optimization frameworks for building energy efficiency
- **Cloud-Native Workflows:** Containerized simulation pipelines for improved reproducibility and scalability
- **Digital Twins:** Real-time performance monitoring and predictive maintenance applications

---

## Related Expertise

This case study demonstrates capabilities applicable to:
- Aerospace component design and optimization
- Multi-fidelity simulation frameworks
- Machine learning for engineering applications
- High-performance computing workflows
- Certification and standards compliance
- Open-source scientific software development

**Industries served:** Aerospace, Defense, Transportation, Renewable Energy

---

*This work was conducted as part of the LANDOne consortium, a UK aerospace initiative advancing landing gear technology for next-generation aircraft.*

**Interested in applying advanced CFD and machine learning to your engineering challenges?** [Contact me](/contact/) to discuss how multi-fidelity modeling can accelerate your development programs.

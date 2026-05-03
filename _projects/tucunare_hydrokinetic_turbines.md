---
layout: page
title: Hydrokinetic Turbine Design & Optimization – Tucunaré Project
description: Multi-institutional hydrokinetic energy initiative — cavitation-free BEM optimization, CFD wake analysis, and diffuser-augmented design for 250 kW–1 MW current turbines downstream of Brazil's largest Amazon dam
img: /assets/img/projects/tucunare-thumb.png
importance: 100
category: work
client: Eletronorte / University of Brasília
---

## Project Overview

**Industry:** Renewable Energy (Hydrokinetic Power Generation)
**Location:** Downstream of UHE-Tucuruí, Rio Tocantins, Pará, Brazil (3°46'48.85"S, 49°38'42.81"W)
**Project:** Projeto Tucunaré – Multi-institutional hydrokinetic energy initiative funded by Eletronorte/Eletrobrás
**Project Type:** Design, optimization, and demonstration of horizontal-axis hydrokinetic turbines for river current energy extraction — from 250 kW rotor design to a planned 5 MW hydrokinetic park

**Consortium Partners:** University of Brasília (UnB), Federal University of Pará (UFPA), Federal University of Itajubá (UNIFEI), Federal University of Rio de Janeiro – COPPE (UFRJ), Federal University of Minas Gerais (UFMG), State University of Campinas (UNICAMP), Federal Fluminense University (UFF)

**Funding:** Eletronorte/Eletrobrás (Centrais Elétricas do Norte do Brasil S/A) — via the Tucuruí Hydroelectric Power Plant, the largest in the Brazilian Amazon

**Recognition:** "Project of the Year" – HydroVision Brasil

---

## My Role

**Position:** Research Assistant at the University of Brasília (2012–2018)

**My contribution:** Hydrokinetic Turbine Hydrodynamic Design and CFD Validation

I contributed to the design, optimization, and CFD validation of the horizontal-axis hydrokinetic turbine. Key responsibilities included developing Cavitation-aware BEM blade optimization, URANS wake CFD characterization, and diffuser-augmented BEM formulation — resulting in 4 peer-reviewed publications over 6 years (2012–2018)

---

## Project Background

Projeto Tucunaré was one of the first initiatives in Brazil to develop mini hydropower plants using hydrokinetic turbines at scale. The project aimed to harness the remnant kinetic energy from water discharged downstream of the Tucuruí Hydroelectric Power Plant — the largest in the Brazilian Amazon — by installing a hydrokinetic turbine park in the Rio Tocantins.

The project built upon three decades of hydrokinetic turbine development at the University of Brasília:

- **1st Generation (1991):** First successful hydrokinetic turbine in Brazil — a single axial turbine installed in a steady-flow river, operational for over a decade
- **2nd Generation (2000s):** Artisan-built turbines (300 W–2 kW) deployed across the Brazilian hinterland for rural electrification of isolated communities
- **3rd Generation (2010s):** Axial turbines designed for modern manufacturing, standardized production, and scalable deployment — the foundation of Projeto Tucunaré

Projeto Tucunaré comprised four main axes: (1) development of hydrokinetic turbine technology; (2) design and construction of a 500 kW–1 MW pilot unit with 3–4 blade horizontal-axis rotor, variable-speed generator, and rear diffuser for power amplification; (3) installation of the pilot on a floating anchored barge in the Rio Tocantins downstream of UHE-Tucuruí; and (4) a sustainable use strategy for the generated electricity, targeting local communities through fish farming cooperatives and agricultural processing.

The long-term vision was establishing a 5 MW hydrokinetic park — multiple turbine units deployed downstream of the dam — demonstrating the viability of distributed hydrokinetic generation integrated into Brazil's electricity sector.

<div class="row justify-content-sm-center">
    <div class="col-sm-5 mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/projects/tucunare-g3.png" title="3rd generation hydrokinetic turbine" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    3rd generation hydrokinetic turbine with diffuser enhancement — the design concept underlying Projeto Tucunaré. Source: Brasil Junior et al. (2006).
</div>

<div class="row justify-content-sm-center">
    <div class="col-sm-5 mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/projects/tucunare-thumb.png" title="Tucunaré turbine assembly" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Tucunaré turbine assembly: 10 m diameter rotor with generator-transmission housed in the nacelle bulb.
</div>

---

## The Challenge

Brazil's Amazon region contains vast untapped hydrokinetic energy potential from river currents, offering a renewable alternative for remote communities disconnected from the national grid. Designing efficient turbines for shallow river environments presented several technical challenges:

- **Cavitation Risk:** Shallow submersion depths (6 m) reduce hydrostatic pressure at blade surfaces, increasing vapor formation risk that erodes blades and reduces lifespan
- **Wake Interference:** Multi-turbine river arrays require accurate wake recovery predictions for optimal spacing — no prior CFD studies existed for river-deployed hydrokinetic turbines
- **Power Extraction Limits:** Bare turbines are constrained by the Betz limit (~59.3%), requiring diffuser augmentation strategies to increase power density
- **Free Surface Effects:** River surface proximity creates asymmetric flow conditions absent in wind turbine or open-ocean tidal turbine design
- **Validation Gap:** Limited experimental data for full-scale hydrokinetic turbines in river conditions demanded robust computational validation protocols

**Stakes:** Brazil's Northern region faces severe rural electrification challenges due to its biogeography — thousands of communities along river basins lack access to regular electricity services and depend on expensive diesel generators. Hydrokinetic turbines offer continuous, clean power from river currents, but the technology must overcome cavitation, wake interference, and power density limitations before it can be commercially deployed. The Tucuruí dam alone discharges enormous kinetic energy that goes unharvested — Projeto Tucunaré aimed to capture this remnant energy for local sustainable development, including fish farming cooperatives (Projeto Ipirá, 325 families) and agricultural processing for downstream communities.

---

## Our Approach

### Phase 1: Cavitation-Aware Blade Optimization (2014–2017)

Standard BEM methods design blades for maximum power, then check cavitation afterward — often requiring costly redesign iterations. This phase embedded the cavitation constraint directly into the optimization loop, eliminating that cycle. CFD confirmed vapor volume was eliminated around the optimized rotor with no loss in power coefficient.

Developed an innovative BEM optimization methodology that prevents cavitation directly during blade design rather than as a post-hoc correction:

- **Thoma Coefficient Criterion:** Accounts for radially-varying water column depth at each blade section — physically important because hydrostatic pressure differs between top and bottom of the rotor sweep in a submerged turbine
- **Inline Cavitation Constraint:** When relative velocity at a blade section exceeds the critical cavitation velocity, the methodology replaces W with the corrected value in the BEM equations
- **Chord Modification:** Blade chord is reduced near the tip where tangential velocity and cavitation risk are highest, with minimal impact on overall power coefficient
- **CFD Validation:** RANS simulations coupled with the Rayleigh-Plesset cavitation model confirmed vapor volume reduction around the optimized rotor
- **Benchmark Verification:** Validated against NREL Phase VI wind turbine experimental data

<div class="mt-3">
    {% include figure.liquid loading="eager" path="assets/img/projects/tucunare_NRELPHASE-VI-pressure_coefficients.png" title="NREL validation"  class="img-fluid rounded z-depth-1" %}
</div>
<div class="mt-3">
    {% include figure.liquid loading="eager" path="assets/img/projects/tucunare-nrelphasevi-powervalidation.png" title="Power validation" class="img-fluid rounded z-depth-1" %}
</div>
<div class="caption">
    Power as a function of inlet velocity: comparison with results available in the literature.
</div>

<div class="mt-3">
    {% include figure.liquid loading="eager" path="assets/img/projects/tucunare_NREL_surface_streamlines.png" title="Surface streamlines" class="img-fluid rounded z-depth-1" %}
</div>
<div class="caption">
Surface streamlines and radial section planes. Flow separation is visible near the tip (r/R > 0.8) in the uncorrected design and suppressed in the optimized blade.
</div>

<div class="mt-3">
    {% include figure.liquid loading="eager" path="assets/img/projects/tucunare-NRELPHASEVI-anemometers_rev1.png" title="Anemometer comparison" class="img-fluid rounded z-depth-1" %}
</div>
<div class="caption">
    Comparison of axial velocity between experimental (blue) and numerical (red) on: (a) Anemometer #1 (b) Anemometer #2.
</div>

<div class="mt-3">
    {% include figure.liquid loading="eager" path="assets/img/projects/Tucunare-NRELPHASEVI-Turbulence.png" title="Turbulence model comparison" class="img-fluid rounded z-depth-1" %}
</div>
<div class="mt-3">
    {% include figure.liquid loading="eager" path="assets/img/projects/Tucunare-Power-literature.png" title="Turbulence model effect" class="img-fluid rounded z-depth-1" %}
</div>
<div class="caption">
    Comparison of turbulence model effect on wind turbines.
</div>

<div class="mt-3">
    {% include figure.liquid loading="eager" path="assets/img/projects/Tucunare-cavitation-comparison.png" title="Cavitation comparison" class="img-fluid rounded z-depth-1" %}
</div>
<div class="caption">
    Cavitation in the rotors at 35 rpm. (a) corrected (b) uncorrected (c) geometrical comparison. Note the near-complete elimination of the vapor region (orange) in the corrected blade
</div>

<div class="mt-3">
    {% include figure.liquid loading="eager" path="assets/img/projects/Tucunare-cavitation-comparison_BEM.png" title="Chord distribution" class="img-fluid rounded z-depth-1" %}
</div>
<div class="caption">
    Corrected chord distribution, showing chord reduction near the blade tip to prevent cavitation.
</div>

<div class="mt-3">
    {% include figure.liquid loading="eager" path="assets/img/projects/Tucunare-cavitation-BEM.png" title="Cavitation comparison" class="img-fluid rounded z-depth-1" %}
</div>
<div class="caption">
    Local comparison of cavitation occurrence obtained by CFD, XFoil and BEM.
</div>

---

### Phase 2: Wake Characterization via URANS CFD (2015–2016)

Performed the first detailed CFD wake study for a hydrokinetic turbine in a river environment:

- **Solver:** ANSYS CFX with URANS and SST k-ω turbulence model
- **Computational Domain:** 31 m × 50 m × 150 m with turbine center at 6 m depth
- **Rotating Sub-Domain:** Cylindrical (6 m radius, 3 m length) with sliding mesh interface
- **Boundary Conditions:** 5% turbulence intensity inlet, free-slip top surface (river surface), atmospheric pressure outlet
- **Post-Processing:** Velocity profiles and TKE distributions across 11 downstream monitoring planes
- **Validation:** Benchmarked turbine against NREL Phase VI wind turbine experimental data from NASA Ames 24 × 36 m wind tunnel

<video src="/assets/img/projects/Tucunare-video-volumefraction.mp4" controls width="100%"></video>

<video src="/assets/img/projects/Tucunare-video-velocity.mp4" controls width="100%"></video>

<div class="mt-3">
    {% include figure.liquid loading="eager" path="assets/img/projects/tucunare-wake-tke.png" title="Wake flow analysis" class="img-fluid rounded z-depth-1" %}
</div>
<div class="caption">
    (a) Mean axial velocity, (b) turbulence kinetic energy (TKE) and (c) relative pressure downstream.
</div>

<div class="mt-3">
    {% include figure.liquid loading="eager" path="assets/img/projects/tucunare-wake-revel-isometric.png" title="Wake velocity profiles" class="img-fluid rounded z-depth-1" %}
</div>
<div class="caption">
    Wake velocity profiles at 11 downstream planes showing near-wake helical vortex structures and far-wake recovery.
</div>

---

### Phase 3: Diffuser-Augmented Turbine Design (2017–2018)

Extended BEM theory with a novel formulation that directly incorporates diffuser efficiency (η_d) — a step previous methods had omitted:

- **New BEM Formulation:** Derived expressions for axial induction factor _a_ and thrust coefficient that include diffuser viscous losses
- **Glauert Correction Extension:** New correction for high axial induction values in the presence of diffusers
- **Flanged Conical Diffuser Geometry:**
  - Inlet (nozzle) diameter: 1.01D
  - Nozzle length: 0.14D
  - Divergent opening angle: 4°
  - Total diffuser length: 1.5D
  - Flange height: D/2
- **CFD Validation:** Finite volume method with SST k-ω turbulence model; BEM-CFD discrepancy of only 0.28% for diffuser-augmented configuration

<div class="mt-3">
    {% include figure.liquid loading="eager" path="assets/img/projects/tucunare-Diffuser-BEM.png" title="BEM-CFD framework" class="img-fluid rounded z-depth-1" %}
</div>
<div class="caption">
    Framework for BEM-CFD coupled approach.
</div>

<div class="mt-3">
    {% include figure.liquid loading="eager" path="assets/img/projects/tucunare-diffuser-schematic.png" title="Diffuser geometry" class="img-fluid rounded z-depth-1" %}
</div>
<div class="caption">
    Geometrical illustration of conical and lens diffusers.
</div>

<div class="mt-3">
    {% include figure.liquid loading="eager" path="assets/img/projects/tucunare-diffuser-mesh.png" title="Mesh details" class="img-fluid rounded z-depth-1" %}
</div>
<div class="caption">
    Mesh details: (a) wake refinement (b) blade and diffuser topology (c) near wall treatment on the blade (d) tip gap between the blade and diffuser.
</div>

<div class="mt-3">
    {% include figure.liquid loading="eager" path="assets/img/projects/tucunare-nearplane.png" title="Velocity comparison" class="img-fluid rounded z-depth-1" %}
</div>
<div class="caption">
    Axial normalized velocity at 0.1D from the rotor plane on three configurations: diffuser-augmented turbines, open turbine, and only the diffusers.
</div>

<div class="mt-3">
    {% include figure.liquid loading="eager" path="assets/img/projects/tucunare-wake.png" title="Wake comparison" class="img-fluid rounded z-depth-1" %}
</div>
<div class="caption">
    Comparison of wake on shrouded and bare turbine: (a) mean axial velocity, (b) turbulence kinetic energy (TKE) and (c) relative pressure downstream.
</div>

---

## Technical Specifications

**Turbine Design Parameters:**

| Parameter             | Value        |
| --------------------- | ------------ |
| Rotor Diameter        | 10 m         |
| Number of Blades      | 3            |
| Airfoil Profile       | NACA 65₃-618 |
| Hub Diameter          | 1.2 m        |
| Rated Power           | 250 kW       |
| Design Velocity       | 2.5 m/s      |
| Submersion Depth      | 6 m          |
| Reynolds Number Range | 1–3 × 10⁶    |

**Computational Tools:**

- **BEM Optimization:** Custom Matlab/Python code with cavitation constraint and diffuser efficiency integration
- **Airfoil Analysis:** XFOIL via XFLR5 v6.58 (Cl, Cd, Cp_min polars)
- **CFD Solver:** ANSYS CFX (URANS, SST k-ω, Rayleigh-Plesset cavitation model)
- **Mesh:** Sliding mesh for rotating sub-domain; structured/unstructured hybrid
- **Validation Benchmarks:** NREL HARP_opt, NREL Phase VI wind tunnel data, Dixon & Ding discharge coefficients

---

## Results & Impact

### Cavitation Prevention

**Key Metrics:**

- **Vapor volume reduction** confirmed by CFD around the optimized rotor
- **Minimal power coefficient variation** — cavitation prevented without sacrificing energy capture
- Chord modification concentrated at blade tip sections (r/R > 0.7) where relative velocity is highest
- Validated against HARP_opt code with good agreement

### Wake Characterization

**Key Metrics:**

- **Near-wake extent:** 3 rotor diameters (30 m) with helical vortex structures
- **Full wake recovery:** 12 rotor diameters (120 m) downstream
- **Radial wake expansion:** 1.2R (6 m radius)
- **Free surface effect:** Directional TKE asymmetry between horizontal and vertical components
- **Practical implication:** Minimum array spacing of 12D for river deployments

| Wake Region | Extent            | Characteristics                           |
| ----------- | ----------------- | ----------------------------------------- |
| Near-wake   | 0–3D (0–30 m)     | Helical vortex structures, expanding wake |
| Transition  | 3D–8D (30–80 m)   | Vortex breakdown, mixing intensification  |
| Far-wake    | 8D–12D (80–120 m) | Velocity recovery to free-stream          |

### Diffuser-Augmented Performance

**Key Metrics:**

- **55% increase in power coefficient** with diffuser augmentation
- **1.5× power output** compared to bare turbine at optimal TSR
- **Velocity speed-up ratio:** 1.6× at rotor plane
- **Optimal TSR shift:** From 3.50–4.25 (bare) to 5.4 (diffuser-augmented)
- **Flatter Cp-TSR curve** — higher efficiency across wider operating range
- **Complete cavitation elimination** achievable with combined diffuser + BEM optimization
- **BEM-CFD discrepancy:** 4.45% bare turbine, 0.28% diffuser-augmented

| Configuration               | Optimal TSR | Cp           | Power Output  | Cavitation Risk |
| --------------------------- | ----------- | ------------ | ------------- | --------------- |
| Bare (Classical)            | 3.50–4.25   | ~0.45        | Baseline      | High at tip     |
| Bare (Cavitation-Optimized) | 3.50–4.25   | ~0.45        | Baseline      | Eliminated      |
| Diffuser-Augmented          | 5.4         | ~0.70 (+55%) | 1.5× Baseline | Eliminated      |

<div class="mt-3">
    {% include figure.liquid loading="eager" path="assets/img/projects/tucunare-cp-tsr-comparison.png" title="Power coefficient comparison" class="img-fluid rounded z-depth-1" %}
</div>
<div class="caption">
    (a) Power coefficient vs. TSR for open and shrouded turbines. (b) Power output as functions of the freestream velocity.
</div>

**Cavitation-Aware Design:**

- Only published BEM methodology that prevents cavitation inline during optimization rather than as post-hoc correction
- Accounts for radially-varying hydrostatic pressure unique to shallow submersion

**River-Specific CFD:**

- First wake study addressing free-surface effects on hydrokinetic turbine performance
- Quantified TKE asymmetry caused by river surface — absent in wind turbine or open-ocean literature

**Diffuser BEM Innovation:**

- First formulation to directly incorporate diffuser viscous efficiency into BEM equations
- 0.28% BEM-CFD agreement for diffuser-augmented case — exceptional accuracy for a reduced-order model

**Practical Impact:**

- Design toolkit applicable to river, tidal, and marine current turbines globally
- Array spacing guidelines directly usable for hydrokinetic farm planning

---

## Impact

**Renewable Energy Access:**

- Validated turbine design for remote Amazonian communities currently dependent on diesel generators
- 250 kW capacity suitable for small community electrification; project vision scaled to 5 MW park
- River current energy provides continuous, predictable power unlike solar or wind
- Location downstream of existing hydroelectric dams captures remnant kinetic energy that would otherwise be lost

**Sustainable Development Impact:**

- Energy designated for local fish farming cooperatives (Projeto Ipirá) supporting 325 families transitioning from artisanal fishing to sustainable aquaculture in the Tucuruí reservoir
- Identified uses: ice production for fish conservation during harvest, electric boats for tank-net management, cold storage for açaí and dairy processing in settlement projects
- Embedded within regional compensation plans (PIRTUC/PIRJUS) addressing social impacts of UHE-Tucuruí construction
- Multi-stakeholder governance model involving Eletronorte, municipal authorities, INCRA, EMBRAPA, and fishing cooperatives

**Design Methodology:**

- Cavitation-aware BEM tool prevents blade erosion at the design stage, extending turbine lifespan
- Wake spacing guidelines (12D) enable optimal multi-turbine river array planning
- Diffuser BEM formulation applicable to any shrouded turbine design worldwide

**Cost Reduction:**

- Inline cavitation constraint eliminates iterative design-test-redesign cycles
- BEM-based optimization runs in seconds vs. hours for full CFD, enabling rapid parametric studies
- Diffuser augmentation increases power per turbine, reducing the number of units needed for target capacity
- 3rd generation turbine design optimized for standardized manufacturing and production scale-up

**Technical Innovation:**

- First river-environment wake characterization for hydrokinetic turbines
- Novel BEM extension incorporating diffuser efficiency — previously omitted in published methods
- 4 peer-reviewed publications with 428+ combined citations across author's profile
- Part of a broader research ecosystem: bibliometric analysis identified 186 hydrokinetic publications in Brazil involving 346 authors across 5 research clusters

---

## Technologies & Methods

**Analytical Methods:**

- Blade Element Momentum (BEM) theory with cavitation constraint
- Glauert optimization with novel extensions for diffuser efficiency
- Thoma coefficient criterion with radially-varying depth correction

**CFD Software:**

- ANSYS CFX: URANS, SST k-ω turbulence, Rayleigh-Plesset cavitation
- Sliding mesh for rotating sub-domains
- Multiphase VOF for cavitation visualization

**Airfoil Tools:**

- XFOIL (via XFLR5 v6.58) for aerodynamic polars
- NACA 65₃-618 profile optimization across Re = 1–3 × 10⁶

**Validation:**

- NREL HARP_opt (BEM benchmark)
- NREL Phase VI wind tunnel data (CFD benchmark)
- Dixon & Ding discharge coefficient correlations

---

## Project Deliverables

**Timeline:** March 2012 – January 2018

**My Outputs:**

- Cavitation-aware BEM optimization methodology validated by CFD
- URANS wake characterization database for river-deployed hydrokinetic turbines
- Novel diffuser-augmented BEM formulation with efficiency integration
- Optimized blade geometry for 250 kW turbine rated at 2.5 m/s
- MSc Thesis: "Numerical Study of Horizontal Axis Hydrokinetic Turbines"
- 4 peer-reviewed journal publications, multiple conference presentations
- "Project of the Year" award at HydroVision Brasil

**Broader Projeto Tucunaré Scope:**

- Multi-institutional consortium across 7 Brazilian universities
- Turbine technology development: 500 kW–1 MW pilot with diffuser-enhanced rotor
- Floating barge deployment design for Rio Tocantins downstream of UHE-Tucuruí
- 5 MW hydrokinetic park master plan with environmental impact assessment
- Sustainable energy use strategy for local communities (fish farming, agricultural processing)
- Environmental licensing submitted for installation and operation

---

## Related Expertise

This case study demonstrates expertise applicable to:

- Renewable energy turbine design and optimization
- Blade Element Momentum theory and extensions
- Multiphase CFD with cavitation modeling
- Wake aerodynamics and turbine array optimization
- Rotating flow simulation and validation
- Free-surface flow effects
- Multi-stakeholder energy projects with social impact dimensions

**Industries served:** Renewable Energy, Hydropower, Tidal Energy, Marine Engineering, Aerospace (rotating machinery), Sustainable Development

## Future Work

I continued collaborating as external visiting researcher to the Laboratory of Energy and Environment at University of Brasilia.

The project was later extended for the Hydro-K Project (2015-2017). A R&D project sponsored ANEEL P&D Grant, with the partnership of AES-Brasil Company to develop applied research on a propeller horizontal axis hydrokinetic turbines. Numerical simulations and modeling, complemented by experiments in wind tunnel and field are conducted.

The Hydro-K project created and deploy a floating, modular hydrokinetic turbine that harnesses the kinetic energy of Amazonian rivers to generate clean, renewable electricity. The technology targets isolated riverside communities in the Amazon that currently lack access to the electrical grid and rely on polluting, inefficient energy sources such as diesel generators or wood burning.
The proposed solution involves a pilot implementation in selected communities to validate the turbine's technical, economic, and social viability. The project emphasizes participatory community management, environmental sustainability, and reduced fossil fuel dependence, while also exploring two revenue models — technology licensing and direct equipment sales — targeting rural communities, sanitation companies, and agribusiness operations near waterways.

Research was later extend to understand how fish and other aquatic organisms propel themselves offers valuable natural references for enhancing technology related to underwater devices like vehicles, propellers, and biomimetic robotics. Additionally, such research provides insights into fish evolution and ecological dynamics.

<video src="/assets/img/projects/Tucunare-Lambari-fish-interaction.mp4" controls width="100%"></video>

<div class="mt-3">
    {% include figure.liquid loading="eager" path="assets/img/projects/Tucunare-Lambari-fish-interaction_numesh.png" title="Fish turbine interaction" class="img-fluid rounded z-depth-1" %}
</div>
<div class="mt-3">
    {% include figure.liquid loading="eager" path="assets/img/projects/Tucunare-Lambari-fish-interaction_iso.png" title="Fish turbine interaction" class="img-fluid rounded z-depth-1" %}
</div>

<div class="caption">
    Fish and Turbine interaction, source: Macias et al. (2024)
</div>

---

_This work was conducted at the University of Brasília as part of Projeto Tucunaré, a multi-institutional initiative funded by Eletronorte/Eletrobrás for hydrokinetic energy development downstream of the Tucuruí Hydroelectric Power Plant in the Brazilian Amazon. The consortium included seven universities (UnB, UFPA, UNIFEI, UFRJ-COPPE, UFMG, UNICAMP, UFF) and was recognized as "Project of the Year" at HydroVision Brasil._

**Interested in applying advanced CFD and renewable energy expertise to your engineering challenges?** [Contact me](/contact/) to discuss how simulation-driven design can optimize your turbomachinery systems.

---

## Publications

1. Silva, Paulo ASF, Shinomiya, L. D., de Oliveira, T. F., Vaz, J. R. P., Mesquita, A. L. A., & Junior, A. C. P. B. "[Analysis of cavitation for the optimized design of hydrokinetic turbines using BEM](https://doi.org/10.1016/j.apenergy.2016.02.098)." _Applied Energy_ 185 (2017): 1281–1291.

2. Silva, Paulo ASF, Oliveira, T. F., Brasil Junior, A. C. P., & Vaz, J. R. P. "[Numerical study of wake characteristics in a horizontal-axis hydrokinetic turbine](https://doi.org/10.1590/0001-3765201620150652)." _Anais da Academia Brasileira de Ciências_ 88.4 (2016): 2441–2456.

3. da Silva, Paulo ASF, Shinomiya, L. D., de Oliveira, T. F., Vaz, J. R. P., Mesquita, A. L. A., & Junior, A. C. P. B. "[Design of hydrokinetic turbine blades considering cavitation](https://doi.org/10.1016/j.egypro.2015.07.343)." _Energy Procedia_ 75 (2015): 277–282.

4. Silva, Paulo ASF, Vaz, D. A. T. D. R., Britto, V., de Oliveira, T. F., Vaz, J. R. P., & Junior, A. C. P. B. "[A new approach for the design of diffuser-augmented hydro turbines using the blade element momentum](https://doi.org/10.1016/j.enconman.2018.03.093)." _Energy Conversion and Management_ 165 (2018): 801–814.

### Related Project References

5. van Els, R. H., Miranda, A. R. S., Vélez Echeverry, S. M., & Brasil Junior, A. C. P. "Hydrokinetic energy conversion — state of the art and perspectives in Brazil." (2018).

6. de Souza, J. S. A., Vélez Echeverry, S. M., van Els, R. H., Diniz, J. D. A. S., & Brasil Junior, A. C. P. "Uso sustentável da energia elétrica gerada por uma turbina hidrocinética no norte do Brasil." _Simpósio Brasileiro de Recursos Hídricos_ (2015).

7. Brasil Junior, A. C. P., Salomon, L. B. R., van Els, R. H., & Ferreira, W. O. "A New Conception of Hydrokinetic Turbine for Isolated Communities in Amazon." _IV Congresso Nacional de Engenharia Mecânica_ (2006).

8. Macías, Marianela Machuca, et al. "Numerical investigation of dimensionless parameters in carangiform fish swimming hydrodynamics." Biomimetics 9.1 (2024).

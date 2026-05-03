---
layout: page
title: Thermal CFD Optimization for Embraer Aerospace Manufacturing Data Center
description: Parametric CFD study of supply air angles and hot/cold aisle containment strategies, identifying the optimal cooling configuration for a mission-critical aerospace facility.

img: assets/img/projects/embraer-layout.png
importance: 2
category: work
client: Embraer / Fox Eng.
---

<div class="badges">
  <span class="badge bg-primary">214 kW Total Capacity</span>
  <span class="badge bg-success">30 Racks</span>
  <span class="badge bg-info">Parametric Optimization</span>
  <span class="badge bg-warning text-dark">Containment Comparison</span>
</div>

## Project Overview

Thermal performance analysis and design optimization for Embraer's data center facility at Gavião Peixoto, São Paulo, Brazil. The study combined **parametric supply angle optimization** with a **containment strategy comparison** to identify the cooling configuration that maximizes ASHRAE compliance across three distinct equipment corridors with different thermal densities and cooling architectures.

## The Challenge: Three Corridors, Three Cooling Strategies

The 129.6 m² facility houses 30 racks distributed across three equipment corridors (A–E), each with a fundamentally different cooling approach:

- **Corridor E (72 kW)**: In-row fancoil cooling with enclosed cold aisle and angled supply discharge at 45°
- **Corridors A–B (112 kW)**: Under-floor ventilation with floor-mounted fans (4,000 m³/h each) and variable containment configurations
- **Corridors C–D (30 kW)**: Downflow CRAH units delivering cold air through perforated raised floor tiles with variable porosity (30–54%)

The coexistence of in-row and under-floor cooling, combined with rack thermal densities ranging from 1 kW to 12 kW per unit, creates a multi-zone thermal environment where each corridor requires independent analysis and optimization. **The key engineering questions were**: what supply angle minimizes hot spots in Corridor E, and does cold aisle containment in the A–B corridors justify its implementation cost?

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/projects/embraer-layout.png" title="Data center layout with corridor and cooling configuration" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Facility floor plan showing the three cooling zones. 
</div>

## Supply Angle Parametric Study (Corridor E)

The in-row fancoils in Corridor E discharge cold air at 12°C into the enclosed cold aisle. The baseline design specified a 45° supply angle, directing air diagonally across the aisle. CFD analysis revealed that this configuration creates **high dynamic pressure opposing rack intake**, preventing cold air from reaching mid-corridor racks (E3–E5) and causing localized hot spots exceeding 45°C.

A parametric study was conducted across three supply angles (45°, 15°, and 5°) to quantify the effect on thermal uniformity and ASHRAE compliance.

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/projects/Embraer-corridorE-45deg.png" title="Temperature distribution in Corridor E at different supply 45 angles" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/projects/Embraer-corridorE-15deg.png" title="Temperature distribution in Corridor E at different supply 15 angles" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/projects/Embraer-corridorE-5deg.png" title="Temperature distribution in Corridor E at different supply 5 angles" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Temperature distribution in Corridor E at 1.5 m height for three supply angles. At 45° (top), cold air jets impinge on the opposite wall before reaching mid-corridor racks, creating hot spots near E5. Reducing the angle to 15° (middle) and 5° (bottom) progressively improves thermal uniformity by allowing cold air to enter racks before momentum carries it past.
</div>

The cross-sectional analysis at 10 cm from rack inlets quantified the improvement more precisely, showing how reduced supply angles allow the cold air to distribute more evenly across the full rack height.

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/projects/embraer-containment-comparison.png" title="Cross-sectional temperature at rack inlets for three supply angles" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Temperature distribution at 10 cm from rack inlets in Corridor E for 45°, 15°, and 5° supply angles. The 45° case shows concentrated hot spots near E5 (>45°C), while the 15° configuration achieves the most uniform distribution with peak temperatures limited to ~41°C near E3.
</div>

### ASHRAE Compliance Results — Corridor E

The parametric study demonstrated a clear relationship between supply angle and thermal compliance:

| ASHRAE Class  | 45° Supply | 15° Supply | 5° Supply |
| ------------- | ---------- | ---------- | --------- |
| A1 (T < 32°C) | 85.7%      | 96.8%      | 94.9%     |
| A2 (T < 35°C) | 87.7%      | 97.1%      | 96.3%     |
| A3 (T < 40°C) | 92.3%      | 97.6%      | 97.7%     |
| A4 (T < 45°C) | 94.5%      | 98.3%      | 99.3%     |
| T > 45°C      | 5.5%       | 1.7%       | 0.7%      |

The **15° configuration emerged as the optimal balance** between thermal uniformity and ASHRAE compliance, achieving 96.8% A1 compliance compared to 85.7% at the baseline 45° angle — a meaningful reduction in thermal risk with minimal hardware modification.

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/projects/embraer-ashrae-corridor-e.png" title="ASHRAE classification for Corridor E at three supply angles" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    ASHRAE thermal classification at rack inlets in Corridor E. Green (A1) through red (>45°C) zones mapped for each supply angle configuration. The 5° case achieves the lowest proportion above 45°C (0.7%), while the 15° case delivers the best overall uniformity across all classes.
</div>

## Containment Impact Analysis

With the supply angle optimized for Corridor E, the study turned to the main facility zone to evaluate the impact of cold aisle containment on thermal performance. Two scenarios were compared:

- **Scenario 1 (Enclosed)**: Cold aisle between rack rows A and B fully contained with physical barriers extending 15 cm above rack height
- **Scenario 2 (Open)**: Same corridor without containment, relying on natural airflow separation

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/projects/embraer-containment-comparison.png" title="Temperature comparison between enclosed and open containment" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Temperature distribution at 1.8 m height and cross-sections for enclosed (left) and non-enclosed (right) configurations. Plan views show similar global patterns, but cross-sections reveal the enclosed corridor maintains lower temperatures at rack inlets. The open configuration allows hot return air to infiltrate the cold aisle, particularly at upper rack heights.
</div>

### Rack-by-Rack Temperature Comparison

| Rack | Enclosed (°C) | Open (°C) |     | Rack | Enclosed (°C) | Open (°C) |
| ---- | :-----------: | :-------: | --- | ---- | :-----------: | :-------: |
| A0   |     20.1      |   21.8    |     | C1   |     14.2      |   12.9    |
| A1   |     23.8      |   27.7    |     | C2   |     18.7      |   19.8    |
| A2   |     13.7      |   17.9    |     | C3   |     15.1      |   19.4    |
| A3   |     18.7      |   23.8    |     | C4   |     14.5      |   14.2    |
| A4   |     26.1      |   26.0    |     | C5   |     13.0      |   12.3    |
| A5   |     16.0      |   27.8    |     | C6   |     14.5      |   13.1    |
| B0   |     16.7      |   13.7    |     | D1   |     23.8      |   21.3    |
| B1   |     20.8      |   26.8    |     | D2   |     25.6      |   21.1    |
| B2   |     24.1      |   29.6    |     | D3   |     28.1      |   23.3    |
| B3   |     17.1      |   17.5    |     | D4   |     22.5      |   23.3    |
| B4   |     17.9      |   21.9    |     | D5   |     15.5      |   21.6    |
| B5   |     16.5      |   30.7    |     | D6   |     14.5      |   17.6    |

Containment reduced inlet temperatures by an average of **4–6°C** in the A–B corridors, with the most significant improvements at racks furthest from the cooling source (A5: 16°C vs 27.8°C; B5: 16.5°C vs 30.7°C).

### ASHRAE Compliance — Containment Effect

| ASHRAE Class             | Enclosed — Non-compliant area | Open — Non-compliant area |
| ------------------------ | :---------------------------: | :-----------------------: |
| T > 45°C (all corridors) |           **2.3%**            |         **7.0%**          |
| A1 compliance (A–B avg)  |             91.2%             |           88.5%           |

The containment reduced the proportion of rack inlet area exceeding ASHRAE limits from **7.0% to 2.3%** — a threefold improvement that justified the containment investment for this facility.

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/projects/embraer-ashrae-containment.png" title="ASHRAE classification comparison for containment scenarios" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    ASHRAE thermal classification at rack inlets for all corridors. Left: enclosed configuration. Right: open configuration. The enclosed scenario shows substantially better compliance in the A–B corridors, while C–D corridors perform similarly in both cases as they are served by a separate cooling system.
</div>

## Under-Floor Airflow Characterization

The CFD analysis also revealed a critical insight about the raised floor plenum airflow. The suction from floor-mounted fans creates **strong directional flow under the raised floor**, leaving dead zones near racks A0, A1, A4, B1, B2, D1, and D2. In these regions, insufficient pressure differential across the perforated tiles restricts cold air delivery, contributing to the hot spots observed at low rack heights — a counter-intuitive finding given the proximity of these racks to the fans.

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/projects/embraer-underfloor-flow.png" title="Under-floor plenum airflow characterization" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Velocity vectors in the raised floor plenum showing how fan suction dominates the flow field. Dead zones with low velocity near racks A1, A4, B1, and B2 result in reduced perforated tile flow and localised hot spots at rack inlets despite proximity to cooling equipment.
</div>

## Facility Specifications

| Parameter           | Value                                           |
| ------------------- | ----------------------------------------------- |
| Floor Area          | 129.6 m²                                        |
| Raised Floor Height | 0.48 m                                          |
| Total Thermal Load  | 214 kW                                          |
| Total Racks         | 30                                              |
| Cooling Zones       | 3 (in-row + downflow + under-floor fans)        |
| Containment         | Corridor E enclosed; A–B variable (study focus) |
| Rack Density Range  | 1–12 kW per rack                                |

## Technical Approach

| Aspect            | Method                                                             |
| ----------------- | ------------------------------------------------------------------ |
| Software          | ANSYS CFX                                                          |
| Turbulence Model  | k-ω SST (Menter)                                                   |
| Tile Modeling     | Porous media with pressure-driven flow                             |
| Rack Modeling     | Porous volume with prescribed heat generation and directional flow |
| Mesh Resolution   | 1.4M nodes (Corridor E), 4M nodes (full facility per scenario)     |
| Mesh Independence | Three-level refinement study                                       |
| Supply Air        | 12°C (in-row), variable through perforated tiles                   |
| Assessment        | ASHRAE TC 9.9 thermal guidelines (Classes A1–A4)                   |

## Project Impact

This study delivered two actionable design recommendations for the Embraer facility:

- **Supply angle modification**: Reducing the in-row fancoil discharge angle from 45° to 15° improved A1 compliance from 85.7% to 96.8% in Corridor E — achievable through damper adjustment alone, requiring no additional hardware
- **Containment justification**: Cold aisle containment in Corridors A–B reduced non-compliant areas from 7.0% to 2.3%, providing quantified evidence for the containment investment decision
- **Plenum flow insight**: Identification of fan-suction-induced dead zones under the raised floor explained counter-intuitive hot spots near cooling equipment, informing future tile placement strategy

The parametric approach demonstrated here — systematically varying a single design parameter while holding others constant — exemplifies how CFD enables evidence-based design decisions that would be impractical through physical testing alone, particularly in operational facilities where downtime for experimentation is not an option.

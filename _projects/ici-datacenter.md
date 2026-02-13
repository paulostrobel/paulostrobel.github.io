---
layout: page
title: ICI Data Center
description: CFD thermal optimization for 3 MW mission-critical banking infrastructure with **disproportionate relationship between thermal density and cooling capacity in the processing zones** 
img: assets/img/projects/ici-terreo-tridimensional.png
importance: 2
client: Banco do Brasil/Fox Eng.
category: Data Center
---

<div class="badges">
  <span class="badge bg-primary">3.0 MW Total Capacity</span>
  <span class="badge bg-success">52 Fan Coil Units</span>
  <span class="badge bg-info">Two-Phase Optimization</span>
  <span class="badge bg-warning text-dark">Floor Fan Remediation</span>
</div>

## Project Overview

Thermal performance prediction and cooling optimization for the ICI-1  data center at Banco do Brasil's Central Technology Complex in Brasília, Brazil. The project encompassed **two floor levels with distinct thermal architectures**, combining baseline thermal mapping with a **floor fan optimization study** that achieved substantial improvements in ASHRAE compliance for high-density processing zones.



## The Challenge: Asymmetric Thermal Loads Across Two Floors

Mission-critical banking operations demanded:
- Zero tolerance for thermal events affecting financial transactions
- Fan coil unit optimization for heterogeneous load distribution
- N+1 redundancy validation under failure scenarios
- Compliance with stringent banking sector regulations

The ICI-1 complex spans two floors with fundamentally different thermal characteristics:

- **Ground Floor**: 856 m² with 1,670.8 kW thermal load across 28 CRAH units – featuring high-density processing zones with localized hotspots
- **1st Floor**: 1,220 m² with 1,337.8 kW thermal load across 24 CRAH units – better distributed load but with critical  zone with 6.62 kW/m² density

Both floors employ raised floor plenum cooling with cold aisle containment, but the **disproportionate relationship between thermal density and cooling capacity in the processing zones** created the primary engineering challenge: the Processing High-End zone contributes 41% of total thermal load while receiving only 28% of the cooling capacity.

The engineering question was clear: can the existing 52 fan coil units maintain ASHRAE compliance, and if not, what is the most cost-effective remediation strategy?

<div class="mt-3">
        {% include figure.liquid loading="eager" path="assets/img/projects/ici-terreo-tridimensional.png" title="Ground floor 3D model" class="img-fluid rounded z-depth-1" %}
</div>
<div class="mt-3">
        {% include figure.liquid loading="eager" path="assets/img/projects/ici-1pav-tridimensional.png" title="1st floor 3D model" class="img-fluid rounded z-depth-1" %}
</div>
<div class="caption">
    3D computational models of the ICI-1 data center.Top: Ground floor with high-density processing zone. Bottom: 1st floor with distributed processing areas.
</div>

<div class="mt-3">
        {% include figure.liquid loading="eager" path="assets/img/projects/ici-schematic-terreo.png" title="Ground floor 3D model" class="img-fluid rounded z-depth-1" %}
</div>
<div class="caption">
    Schematic of the zones thermal on the Ground Floor: Green (27.4 kW in 98 m<sup>2</sup>), Blue  (377 kW in 442 m<sup>2</sup>), Yellow (18.4 kW in 168 m<sup>2</sup>) and red (1248 kW in 248 m<sup>2</sup>)
</div>
<div class="mt-3">
        {% include figure.liquid loading="eager" path="assets/img/projects/ici-schematic-1pav.png" title="1st floor 3D model" class="img-fluid rounded z-depth-1" %}
</div>
<div class="caption">
    Schematic of the zones thermal on the 1st Floor: Green (95.9 kW in 222 m<sup>2</sup>), Blue  (582.3 kW in 491 m<sup>2</sup>), Yellow (78.2 kW in 123 m<sup>2</sup>), Purple (95 kW in 200 m<sup>2</sup>), Black (325 kW in 47.6 m<sup>2</sup>) and red (266 kW in 253 m<sup>2</sup>)
</div>

## Phase 1: Baseline Thermal Mapping

### Ground Floor Analysis

The initial CFD study compared two setpoint temperatures (**14°C** and **16°C**) to quantify the thermal performance across four distinct zones:  network switching, general storage, and high-density processing.

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/projects/ici-terreo-plano-1500mm.png" title="Temperature distribution at 1.5m height - ground floor" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Temperature distribution at 1.5m height for ground floor comparing 16°C (left) and 14°C (right) supply temperatures. The Processing zone (red) shows peak temperatures of 47°C and 41°C respectively, concentrated in racks furthest from CRAH units.
</div>

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/projects/ici-terreo_corte_xz_detalhe.png" title="CRAH return temperatures - ground floor" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
  Temperature field on the high density racks.
</div>

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/projects/ici-terreo_corte_corredor_processamento_vetores.png" title="CRAH return temperatures - ground floor" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

The analysis revealed a critical **capacity mismatch**: the highest density zone (red zone) required approximately 12 CRAH units operating at full capacity to handle its 1,248 kW load, but only 8 units were allocated operating at 75% capacity.


<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/projects/ici-terreo-retorno.png" title="CRAH return temperatures - ground floor" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    CRAH return air temperatures for ground floor showing thermal load distribution. Units 11-14 and 25-28 near the Processing zone operate significantly above design capacity, with units 14 and 28 exceeding 100% rated capacity.
</div>

Units 11-14 and 25-28 near the Processing zone operate significantly above design capacity, with units 14 and 28 exceeding 100% rated capacity
<div align="center">

| Fan Coil | Heat removal [kW] | Load [%] |
| :--- | :---: | :---: |
| Fan Coil 1 | 25.88 | 24.64 |
| Fan Coil 2 | 35.56 | 33.87 |
| Fan Coil 3 | 38.52 | 36.69 |
| Fan Coil 4 | 47.91 | 45.63 |
| Fan Coil 5 | 51.95 | 49.48 |
| Fan Coil 6 | 64.28 | 61.22 |
| Fan Coil 7 | 62.19 | 59.22 |
| Fan Coil 8 | 66.76 | 63.58 |
| Fan Coil 9 | 88.82 | 84.59 |
| Fan Coil 10 | 92.78 | 88.36 |
| Fan Coil 11 | 108.37 | 103.21 |
| Fan Coil 12 | 114.83 | 109.36 |
| Fan Coil 13 | 130.25 | 124.05 |
| Fan Coil 14 | 152.10 | 144.86 |
| Fan Coil 15 | 25.34 | 24.13 |
| Fan Coil 16 | 34.82 | 33.16 |
| Fan Coil 17 | 37.92 | 36.11 |
| Fan Coil 18 | 44.69 | 42.56 |
| Fan Coil 19 | 45.73 | 43.55 |
| Fan Coil 20 | 43.61 | 41.53 |
| Fan Coil 21 | 62.28 | 59.31 |
| Fan Coil 22 | 66.18 | 63.02 |
| Fan Coil 23 | 86.18 | 82.07 |
| Fan Coil 24 | 106.91 | 101.81 |
| Fan Coil 25 | 124.25 | 118.33 |
| Fan Coil 26 | 129.60 | 123.43 |
| Fan Coil 27 | 130.65 | 124.43 |
| Fan Coil 28 | 152.60 | 145.33 |

</div>


### Rack Inlet Temperatures – Ground Floor Baseline
<div align="center">

| Room / Area | 16°C Supply: Average | 16°C Supply: Max Intake | 14°C Supply: Average | 14°C Supply: Max Intake |
| :--- | :---: | :---: | :---: | :---: |
| **Zone A** (27.4 kW) | 18.3 | 20.4 | 15.9 | 17.7 |
| **Zone B** (18.4 kW) | 20.4 | 30.0 | 17.8 | 27.8 |
| **Zone C** (377 kW) | 19.8 | 25.3 | 18.0 | 24.6 |
| **Zone D** (1248 kW) | 28.3 | 48.0 | 25.4 | 42.0 |

</div>

The high-density processing zone (Zone D) exceeded ASHRAE A4 limits (45°C) at the 16°C setpoint, confirming the need for enhanced cooling in this critical area.

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/projects/ici-terreo-corte-processamento.png" title="Processing corridor cross-section" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Temperature distribution in the Processing zone cold aisle showing recirculation at corridor ends. The pattern results from opposing CRAH units (14 and 24) creating colliding air streams that prevent effective cooling of mid-corridor racks.
</div>

### 1st Floor Analysis

The 1st floor exhibited more uniform temperature distribution due to better load balancing, but two zones required attention: the mainframe processing area and the high-density switching zone (6.62 kW/m²).

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/projects/ici-1pav-plano-z.png" title="Temperature distribution at 1.5m height - 1st floor" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Temperature distribution at 1.5m height for 1st floor at 16°C (left) and 14°C (right) setpoints. Hot zones concentrate near the high-density areas, though temperatures remain more uniform than the ground floor.
</div>

### Rack Inlet Temperatures – 1st Floor Baseline

<div align="center">

| Zone | 16°C Supply: Mean | 16°C Supply: Max | 14°C Supply: Mean | 14°C Supply: Max |
| :--- | :---: | :---: | :---: | :---: |
| Zone E (312 kW) | 23.5 | **48.0** | 19.0 | 41.9 |
| Zone F (285 kW) | 28.1 | 39.5 | 25.8 | 37.5 |
| Zone G (198 kW) | 24.2 | 41.3 | 22.3 | 34.2 |
| Zone H (95 kW) | 22.7 | 35.9 | 19.9 | 34.7 |
| Zone I (48 kW) | 23.1 | 37.0 | 20.9 | 36.1 |
| Zone J (156 kW) | 28.2 | 37.0 | 25.1 | 36.1 |
| Zone K (142 kW) | 24.0 | 33.3 | 22.0 | 31.0 |
| Zone L (102 kW) | 23.0 | 32.5 | 21.3 | 28.3 |

</div>>

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/projects/ici-1pav-nexus-proc.png" title="Contained vs non-contained corridor comparison" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Comparison between contained (Zone E, left) and non-contained (Zone J, right) corridors. Despite Zone E having higher thermal density, the containment maintains better thermal separation. The non-contained corridor shows significant hot air recirculation from return paths.
</div>

## Phase 2: Floor Fan Optimization Study

Based on Phase 1 findings, the optimization study focused on the ground floor high-density processing zone (Zone D), implementing **100 floor-mounted fans** distributed across three corridors, each delivering 5,000 m³/h of directed airflow from the raised floor plenum.

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/projects/ici-ventiladores-alocados.png" title="Floor fan placement in Processing zone" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Floor fan placement configuration in the Processing zone cold aisles. The 100 fans were strategically positioned to direct plenum airflow toward the highest thermal density racks.
</div>

### Thermal Performance Improvement

The floor fan implementation achieved dramatic improvements in temperature distribution and uniformity:

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/projects/ici-ventiladores-150cm.png" title="Temperature with floor fans at 1.5m" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Temperature distribution at 1.5m height with floor fans active. The peak temperature dropped from 44°C (baseline) to 39°C, and the previously distinct hot/cold zones now show substantially better thermal integration.
</div>

### Comparative Results – Before and After Floor Fans

<div align="center">

| Zone | Baseline Mean (°C) | With Fans Mean (°C) | Baseline Max Intake (°C) | With Fans Max Intake (°C) |
| :--- | :---: | :---: | :---: | :---: |
| Zone A (45 kW) | 15.9 | 17.0 | 17.7 | 18.3 |
| Zone C (197 kW) | 18.0 | 18.9 | 24.6 | 25.5 |
| Zone B (180 kW) | 17.8 | 24.3 | 27.8 | 30.9 |
| Zone D (1,248 kW) | **25.4** | **16.8** | **42.0** | **33.1** |

</div>

The high-density processing zone (Zone D) saw **mean intake temperature drop from 25.4°C to 16.8°C** – a 34% reduction – while maximum intake fell from 42°C to 33.1°C, bringing the zone into full ASHRAE A1 compliance (<32°C) across most racks.

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/projects/ici-ventiladores-corte-xz.png" title="Cross-sectional view with floor fans" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Longitudinal cross-section showing airflow redirection with floor fans. The fans direct plenum air toward high-density zones, though this creates a secondary effect of reduced pressure in adjacent corridors (SW SAN).
</div>

### CRAH Load Redistribution

The floor fans fundamentally changed the thermal load distribution across CRAH units:

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/projects/ici-ventiladores-retorno.png" title="CRAH return temperatures with floor fans" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    CRAH unit thermal loads with floor fans active. The previously overloaded units 11-14 and 25-28 now operate within design capacity (70-99%), with more uniform load distribution across all 28 units.
</div>
<div align="center">

| Fan Coil | Removed [kW] | Load [%] |
| :--- | :---: | :---: |
| Fan Coil 1 | 26.3 | 25 |
| Fan Coil 2 | 25.6 | 24 |
| Fan Coil 3 | 30.6 | 29 |
| Fan Coil 4 | 37.8 | 36 |
| Fan Coil 5 | 42.1 | 40 |
| Fan Coil 6 | 57.2 | 54 |
| Fan Coil 7 | 60.0 | 57 |
| Fan Coil 8 | 74.9 | 71 |
| Fan Coil 9 | 73.7 | 70 |
| Fan Coil 10 | 85.7 | 82 |
| Fan Coil 11 | 98.7 | 94 |
| Fan Coil 12 | 84.1 | 80 |
| Fan Coil 13 | 92.2 | 88 |
| Fan Coil 14 | 96.4 | 92 |
| Fan Coil 15 | 34.5 | 33 |
| Fan Coil 16 | 33.6 | 32 |
| Fan Coil 17 | 46.1 | 44 |
| Fan Coil 18 | 51.6 | 49 |
| Fan Coil 19 | 44.3 | 42 |
| Fan Coil 20 | 59.3 | 57 |
| Fan Coil 21 | 78.3 | 75 |
| Fan Coil 22 | 86.5 | 82 |
| Fan Coil 23 | 79.3 | 76 |
| Fan Coil 24 | 90.5 | 86 |
| Fan Coil 25 | 103.4 | 98 |
| Fan Coil 26 | 97.3 | 93 |
| Fan Coil 27 | 104.3 | 99 |
| Fan Coil 28 | 103.2 | 98 |

**Heat removed in each Fan Coil**

</div>


## Facility Specifications

<div align="center">

| Parameter | Ground Floor | 1st Floor |
| :--- | :---: | :---: |
| Floor Area | 856 m² | 1,220 m² |
| Total Thermal Load | 1,670.8 kW | 1,337.8 kW |
| CRAH Units | 28 | 24 |
| CRAH Capacity (per unit) | 105.7 kW | 105.7 kW |
| Containment Type | Cold Aisle | Cold Aisle (partial) |
| Peak Density Zone | Zone D (3.14 kW/m²) | Zone E (6.62 kW/m²) |

</div>

## Technical Approach

<div align="center">

| Aspect | Method |
| :--- | :--- |
| **Software** | ANSYS CFX |
| **Turbulence Model** | $k$-$\epsilon$ with wall functions |
| **Tile Modeling** | Porous media (53% porosity) |
| **Rack Modeling** | Volumetric heat source with prescribed airflow (270 m³/h per kW) |
| **Floor Fans** | 5,000 m³/h per unit, directed discharge |
| **Supply Temperature** | 14°C and 16°C parametric study |
| **Assessment** | ASHRAE TC 9.9 (Classes A1–A4) |

</div>


## Project Impact

This study delivered critical findings for the Banco do Brasil ICI-1 facility:

- **Capacity mismatch identification**: Quantified the disparity between high-density zone thermal load (41% of total) and allocated cooling capacity (28% of total), providing evidence for infrastructure planning
- **Setpoint recommendation**: The 14°C supply temperature configuration achieved substantially better thermal compliance than 16°C, with peak temperatures reduced by 6°C in critical zones
- **Floor fan effectiveness**: Implementation of 100 floor fans reduced high-density zone mean intake temperature by 34% (25.4°C → 16.8°C) and brought maximum temperatures below ASHRAE A2 limits
- **Containment validation**: Comparison between contained (Zone E) and non-contained (Zone J) areas demonstrated the effectiveness of cold aisle containment even in lower-density areas

The two-phase approach – baseline mapping followed by targeted optimization – enabled the facility operators to prioritize interventions based on quantified thermal risk, focusing floor fan investment where it delivered maximum compliance improvement per unit cost.

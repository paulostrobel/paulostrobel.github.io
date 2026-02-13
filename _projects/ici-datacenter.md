---
layout: page
title: ICI-1 Data Center – Banco do Brasil
description: Two-phase CFD thermal optimization with floor fan remediation for 3 MW mission-critical banking infrastructure
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


The ICI-1 complex spans two floors with fundamentally different thermal characteristics:

- **Ground Floor**: 856 m² with 1,670.8 kW thermal load across 28 CRAH units – featuring high-density processing zones with localized hotspots
- **1st Floor**: 1,220 m² with 1,337.8 kW thermal load across 24 CRAH units – better distributed load but critical NEXUS zone with 6.62 kW/m² density

Both floors employ raised floor plenum cooling with cold aisle containment, but the **disproportionate relationship between thermal density and cooling capacity in the processing zones** created the primary engineering challenge: the Processing High-End zone contributes 41% of total thermal load while receiving only 28% of the cooling capacity.

The engineering question was clear: can the existing 52 fan coil units maintain ASHRAE compliance, and if not, what is the most cost-effective remediation strategy?

<div class="mt-3">
        {% include figure.liquid loading="eager" path="assets/img/projects/ici-terreo-tridimensional.png" title="Ground floor 3D model" class="img-fluid rounded z-depth-1" %}
</div>
<div class="mt-3">
        {% include figure.liquid loading="eager" path="assets/img/projects/ici-1pav-tridimensional.png" title="1st floor 3D model" class="img-fluid rounded z-depth-1" %}
</div>
<div class="caption">
    3D computational models of the ICI-1 data center.Top: Ground floor with high-density processing zone. Bottom: 1st floor with NEXUS and distributed processing areas.
</div>

## Phase 1: Baseline Thermal Mapping

### Ground Floor Analysis

The initial CFD study compared two setpoint temperatures (14°C and 16°C) to quantify the thermal performance across four distinct zones: tape library storage, network switching, general storage, and high-density processing.

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/projects/ici-terreo-plano-1500mm.pdf" title="Temperature distribution at 1.5m height - ground floor" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Temperature distribution at 1.5m height for ground floor comparing 16°C (left) and 14°C (right) supply temperatures. The Processing zone shows peak temperatures of 47°C and 41°C respectively, concentrated in racks furthest from CRAH units.
</div>

The analysis revealed a critical **capacity mismatch**: the Processing zone required approximately 12 CRAH units operating at full capacity to handle its 1,248 kW load, but only 8 units were allocated operating at 75% capacity.

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/projects/ici-terreo-retorno.pdf" title="CRAH return temperatures - ground floor" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    CRAH return air temperatures for ground floor showing thermal load distribution. Units 11-14 and 25-28 near the Processing zone operate significantly above design capacity, with units 14 and 28 exceeding 100% rated capacity.
</div>

### Rack Inlet Temperatures – Ground Floor Baseline

| Zone | Mean Temp (°C) | Max Intake (°C) | | Setpoint | 16°C | 14°C |
|------|:---:|:---:|-|------|:---:|:---:|
| Zone A (45 kW) | 18.3 | 20.4 | | Zone A | 15.9 | 17.7 |
| Zone B (180 kW) | 20.4 | 30.0 | | Zone B | 17.8 | 27.8 |
| Zone C (197 kW) | 19.8 | 25.3 | | Zone C | 18.0 | 24.6 |
| Zone D (1,248 kW) | 28.3 | **48.0** | | Zone D | 25.4 | **42.0** |

The high-density processing zone (Zone D) exceeded ASHRAE A4 limits (45°C) at the 16°C setpoint, confirming the need for enhanced cooling in this critical area.

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/projects/ici-terreo-corte-processamento.pdf" title="Processing corridor cross-section" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Temperature distribution in the Processing zone cold aisle showing recirculation at corridor ends. The pattern results from opposing CRAH units (14 and 24) creating colliding air streams that prevent effective cooling of mid-corridor racks.
</div>

### 1st Floor Analysis

The 1st floor exhibited more uniform temperature distribution due to better load balancing, but two zones required attention: the mainframe processing area and the high-density switching zone (6.62 kW/m²).

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/projects/ici-1pav-plano-z.pdf" title="Temperature distribution at 1.5m height - 1st floor" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Temperature distribution at 1.5m height for 1st floor at 16°C (left) and 14°C (right) setpoints. Hot zones concentrate near the high-density areas, though temperatures remain more uniform than the ground floor.
</div>

### Rack Inlet Temperatures – 1st Floor Baseline

| Zone | 16°C Mean | 16°C Max | 14°C Mean | 14°C Max |
|------|:---:|:---:|:---:|:---:|
| Zone E (312 kW) | 23.5 | **48.0** | 19.0 | 41.9 |
| Zone F (285 kW) | 28.1 | 39.5 | 25.8 | 37.5 |
| Zone G (198 kW) | 24.2 | 41.3 | 22.3 | 34.2 |
| Zone H (95 kW) | 22.7 | 35.9 | 19.9 | 34.7 |
| Zone I (48 kW) | 23.1 | 37.0 | 20.9 | 36.1 |
| Zone J (156 kW) | 28.2 | 37.0 | 25.1 | 36.1 |
| Zone K (142 kW) | 24.0 | 33.3 | 22.0 | 31.0 |
| Zone L (102 kW) | 23.0 | 32.5 | 21.3 | 28.3 |

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
        {% include figure.liquid loading="eager" path="assets/img/projects/ici-ventiladores-alocados.pdf" title="Floor fan placement in Processing zone" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Floor fan placement configuration in the Processing zone cold aisles. The 100 fans were strategically positioned to direct plenum airflow toward the highest thermal density racks.
</div>

### Thermal Performance Improvement

The floor fan implementation achieved dramatic improvements in temperature distribution and uniformity:

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/projects/ici-ventiladores-150cm.pdf" title="Temperature with floor fans at 1.5m" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Temperature distribution at 1.5m height with floor fans active. The peak temperature dropped from 44°C (baseline) to 39°C, and the previously distinct hot/cold zones now show substantially better thermal integration.
</div>

### Comparative Results – Before and After Floor Fans

| Zone | Baseline Mean (°C) | With Fans Mean (°C) | Baseline Max Intake (°C) | With Fans Max Intake (°C) |
|------|:---:|:---:|:---:|:---:|
| Zone A (45 kW) | 15.9 | 17.0 | 17.7 | 18.3 |
| Zone C (197 kW) | 18.0 | 18.9 | 24.6 | 25.5 |
| Zone B (180 kW) | 17.8 | 24.3 | 27.8 | 30.9 |
| Zone D (1,248 kW) | **25.4** | **16.8** | **42.0** | **33.1** |

The high-density processing zone (Zone D) saw **mean intake temperature drop from 25.4°C to 16.8°C** – a 34% reduction – while maximum intake fell from 42°C to 33.1°C, bringing the zone into full ASHRAE A1 compliance (<32°C) across most racks.

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/projects/ici-ventiladores-corte-xz.pdf" title="Cross-sectional view with floor fans" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Longitudinal cross-section showing airflow redirection with floor fans. The fans direct plenum air toward high-density zones, though this creates a secondary effect of reduced pressure in adjacent corridors (SW SAN).
</div>

### CRAH Load Redistribution

The floor fans fundamentally changed the thermal load distribution across CRAH units:

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/projects/ici-ventiladores-retorno.pdf" title="CRAH return temperatures with floor fans" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    CRAH unit thermal loads with floor fans active. The previously overloaded units 11-14 and 25-28 now operate within design capacity (70-99%), with more uniform load distribution across all 28 units.
</div>

## Facility Specifications

| Parameter | Ground Floor | 1st Floor |
|-----------|:---:|:---:|
| Floor Area | 856 m² | 1,220 m² |
| Total Thermal Load | 1,670.8 kW | 1,337.8 kW |
| CRAH Units | 28 | 24 |
| CRAH Capacity | 105.7 kW each | 105.7 kW each |
| Containment | Cold Aisle | Cold Aisle (partial) |
| Peak Density Zone | Zone D (3.14 kW/m²) | Zone E (6.62 kW/m²) |

## Technical Approach

| Aspect | Method |
|--------|--------|
| Software | ANSYS CFX |
| Turbulence Model | k-ε with wall functions |
| Tile Modeling | Porous media (53% porosity) |
| Rack Modeling | Volumetric heat source with prescribed airflow (270 m³/h per kW) |
| Floor Fans | 5,000 m³/h per unit, directed discharge |
| Supply Temperature | 14°C and 16°C parametric study |
| Assessment | ASHRAE TC 9.9 (Classes A1–A4) |

## Project Impact

This study delivered critical findings for the Banco do Brasil ICI-1 facility:

- **Capacity mismatch identification**: Quantified the disparity between high-density zone thermal load (41% of total) and allocated cooling capacity (28% of total), providing evidence for infrastructure planning
- **Setpoint recommendation**: The 14°C supply temperature configuration achieved substantially better thermal compliance than 16°C, with peak temperatures reduced by 6°C in critical zones
- **Floor fan effectiveness**: Implementation of 100 floor fans reduced high-density zone mean intake temperature by 34% (25.4°C → 16.8°C) and brought maximum temperatures below ASHRAE A2 limits
- **Containment validation**: Comparison between contained (Zone E) and non-contained (Zone J) areas demonstrated the effectiveness of cold aisle containment even in lower-density areas

The two-phase approach – baseline mapping followed by targeted optimization – enabled the facility operators to prioritize interventions based on quantified thermal risk, focusing floor fan investment where it delivered maximum compliance improvement per unit cost.

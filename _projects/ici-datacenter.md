---
layout: page
title: ICI Data Center
description: CFD thermal optimization for 3 MW mission-critical banking infrastructure with disproportionate relationship between thermal density and cooling capacity in the processing zones
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

Thermal performance prediction and cooling optimization for the ICI-1 data center at Banco do Brasil's Central Technology Complex in Brasília, Brazil. The project encompassed **two floor levels with distinct thermal architectures**, combining baseline thermal mapping with a **floor fan optimization study** that achieved substantial improvements in ASHRAE compliance for high-density processing zones.

## The Challenge: Asymmetric Thermal Loads Across Two Floors

Mission-critical banking operations demanded:
- Zero tolerance for thermal events affecting financial transactions
- Fan coil unit optimization for heterogeneous load distribution
- N+1 redundancy validation under failure scenarios
- Compliance with stringent banking sector regulations

The ICI-1 complex spans two floors with fundamentally different thermal characteristics:

- **Ground Floor**: 856 m² with 1,670.8 kW thermal load across 28 CRAH units – featuring high-density processing zones with localized hotspots
- **1st Floor**: 1,220 m² with 1,337.8 kW thermal load across 24 CRAH units – better distributed load but with critical zone with 6.62 kW/m² density

Both floors employ raised floor plenum cooling with cold aisle containment, but the **disproportionate relationship between thermal density and cooling capacity in the processing zones** created the primary engineering challenge: the Processing High-End zone contributes 41% of total thermal load while receiving only 28% of the cooling capacity.

The engineering question was clear: can the existing 52 fan coil units maintain ASHRAE compliance, and if not, what is the most cost-effective remediation strategy?

### Facility Overview Images

<div class="mt-3">
    {% include figure.liquid loading="eager" path="assets/img/projects/ici-terreo-tridimensional.png" title="Ground floor 3D model" class="img-fluid rounded z-depth-1" %}
</div>
<div class="mt-3">
    {% include figure.liquid loading="eager" path="assets/img/projects/ici-1pav-tridimensional.png" title="1st floor 3D model" class="img-fluid rounded z-depth-1" %}
</div>
<div class="caption">
    3D computational models of the ICI-1 data center. Top: Ground floor with high-density processing zone. Bottom: 1st floor with distributed processing areas.
</div>

### Thermal Zone Schematics

<div class="mt-3">
    {% include figure.liquid loading="eager" path="assets/img/projects/ici-schematic-terreo.bmp" title="Ground floor thermal zones" class="img-fluid rounded z-depth-1" %}
</div>
<div class="caption">
    Schematic of the thermal zones on the Ground Floor: 
    - Green: 27.4 kW in 98 m²
    - Blue: 377 kW in 442 m²
    - Yellow: 18.4 kW in 168 m²
    - Red: 1,248 kW in 248 m²
</div>

<div class="mt-3">
    {% include figure.liquid loading="eager" path="assets/img/projects/ici-3d-schematic-1pav.bmp" title="1st floor thermal zones" class="img-fluid rounded z-depth-1" %}
</div>
<div class="caption">
    Schematic of the thermal zones on the 1st Floor:
    - Green: 95.9 kW in 222 m²
    - Blue: 582.3 kW in 491 m²
    - Yellow: 78.2 kW in 123 m²
    - Purple: 95 kW in 200 m²
    - Black: 325 kW in 47.6 m²
    - Red: 266 kW in 253 m²
</div>

## Phase 1: Baseline Thermal Mapping

### Ground Floor Analysis

The initial CFD study compared two setpoint temperatures (**14°C** and **16°C**) to quantify the thermal performance across four distinct zones: network switching, general storage, and high-density processing.

### Rack Inlet Temperatures – Ground Floor Baseline

| Room / Area | 16°C Supply: Average | 16°C Supply: Max Intake | 14°C Supply: Average | 14°C Supply: Max Intake |
| :--- | :---: | :---: | :---: | :---: |
| **Zone A** (27.4 kW) | 18.3 | 20.4 | 15.9 | 17.7 |
| **Zone B** (18.4 kW) | 20.4 | 30.0 | 17.8 | 27.8 |
| **Zone C** (377 kW) | 19.8 | 25.3 | 18.0 | 24.6 |
| **Zone D** (1248 kW) | 25.4 | 42.0 | 25.4 | 42.0 |

The high-density processing zone (Zone D) exceeded ASHRAE A4 limits (45°C) at the 16°C setpoint, confirming the need for enhanced cooling in this critical area.

### Thermal Performance Visualization

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/projects/ici-terreo-plano-1500mm.png" title="Temperature distribution at 1.5m height - ground floor" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Temperature distribution at 1.5m height for ground floor comparing 16°C (left) and 14°C (right) supply temperatures. The Processing zone (red) shows peak temperatures of 47°C and 41°C respectively, concentrated in racks furthest from CRAH units.
</div>

## Phase 2: Floor Fan Optimization Study

Based on Phase 1 findings, the optimization study focused on the ground floor high-density processing zone (Zone D), implementing **100 floor-mounted fans** distributed across three corridors, each delivering 5,000 m³/h of directed airflow from the raised floor plenum.

### Thermal Performance Improvement

The floor fan implementation achieved dramatic improvements in temperature distribution and uniformity:

| Zone | Baseline Mean (°C) | With Fans Mean (°C) | Baseline Max Intake (°C) | With Fans Max Intake (°C) |
| :--- | :---: | :---: | :---: | :---: |
| Zone A (45 kW) | 15.9 | 17.0 | 17.7 | 18.3 |
| Zone C (197 kW) | 18.0 | 18.9 | 24.6 | 25.5 |
| Zone B (180 kW) | 17.8 | 24.3 | 27.8 | 30.9 |
| Zone D (1,248 kW) | 25.4 | 16.8 | 42.0 | 33.1 |

The high-density processing zone (Zone D) saw **mean intake temperature drop from 25.4°C to 16.8°C** – a 34% reduction – while maximum intake fell from 42°C to 33.1°C, bringing the zone into full ASHRAE A1 compliance (<32°C) across most racks.

## Project Impact

This study delivered critical findings for the Banco do Brasil ICI-1 facility:

- **Capacity mismatch identification**: Quantified the disparity between high-density zone thermal load (41% of total) and allocated cooling capacity (28% of total)
- **Setpoint recommendation**: The 14°C supply temperature configuration achieved substantially better thermal compliance than 16°C
- **Floor fan effectiveness**: Implementation of 100 floor fans reduced high-density zone mean intake temperature by 34%
- **Containment validation**: Demonstrated the effectiveness of cold aisle containment in managing thermal loads

The two-phase approach – baseline mapping followed by targeted optimization – enabled facility operators to prioritize interventions based on quantified thermal risk, focusing floor fan investment where it delivered maximum compliance improvement per unit cost.

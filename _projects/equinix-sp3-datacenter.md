---
layout: page
title: Equinix SP3 Data Center
description: CFD thermal analysis with perforated tile flow validation for 3.35 MW hyperscale facility
img: assets/img/projects/equinix-streamlines.png
importance: 2
category: work
---

<div class="badges">
  <span class="badge bg-primary">3.35 MW Total Capacity</span>
  <span class="badge bg-success">640 Racks</span>
  <span class="badge bg-info">CFD-Experimental Validation</span>
  <span class="badge bg-warning text-dark">Mixed Containment</span>
</div>

## Project Overview

Thermal performance prediction for Equinix's SP3 hyperscale data center complex in São Paulo, Brazil. The study focused on validating CFD predictions against experimental measurements and identifying thermal risks in a facility with **mixed containment configurations** and varying thermal densities across subzones.

## The Challenge: Mixed Configurations

Unlike uniform data center designs, SP3 presents a complex thermal environment where multiple factors interact simultaneously:

- **Mixed containment strategies** across different client subzones
- **Variable thermal densities** ranging from low-density storage to high-performance computing
- **Non-uniform tile distributions** driven by architectural constraints
- **Shared areas** with horizontally-oriented racks breaking conventional airflow patterns

In such environments, establishing clear cause-and-effect relationships between cooling delivery and thermal performance becomes challenging. A hot spot may result from insufficient tile flow, excessive local heat load, poor containment, or—most likely—a combination of all three. **This complexity is precisely why CFD analysis is essential**: it allows engineers to visualize and understand the interplay of these factors before problems manifest in production.

## Perforated Tile Flow Validation

A critical aspect of data center CFD is accurately predicting airflow through perforated floor tiles. The tiles were modeled as porous media with pressure-driven flow between the raised floor plenum and the IT environment, with flow direction aligned at 60° per industry best practices.

To validate the CFD model, predicted tile velocities were compared against **on-site experimental measurements** across both zones. Rather than focusing on point-by-point numerical agreement, the validation emphasizes qualitative pattern matching—ensuring the CFD captures the spatial distribution of high-flow and low-flow regions.

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/projects/equinix-tile-validation.png" title="CFD vs Experimental tile flow validation" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Perforated tile airflow validation for Zone 2.4. Top: CFD-predicted velocity contours showing flow distribution across tiles. Bottom: Experimental measurements categorized by flow rate ranges (m³/h). The qualitative agreement confirms the model captures the essential flow patterns, including regions of reduced airflow near the shared area.
</div>

The comparison reveals consistent patterns between simulation and measurement: areas with high tile flow in CFD correspond to high measured flow rates, while regions predicted to have restricted flow match the experimental observations. This qualitative agreement provides confidence that the CFD model can reliably identify thermal risks.

## Hot Spot Identification

With the validated model, thermal performance was assessed against ASHRAE recommended inlet temperature range (18-32°C). Areas exceeding this range are flagged as potential hot spots requiring attention.

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/projects/equinix-ashrae-compliance.png" title="ASHRAE temperature compliance" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    ASHRAE compliance visualization (18-32°C range). Green indicates compliant rack inlets; red highlights areas exceeding the recommended temperature range. The concentration of red in the shared area and high-density subzones reflects the combined effect of thermal load distribution and airflow delivery.
</div>

The analysis identified thermal risks primarily in:
- **Shared Area (Área Compartilhada)**: Horizontally-oriented racks disrupting conventional hot/cold aisle separation
- **High-density subzones**: Where thermal load concentration exceeds local cooling capacity
- **Regions with restricted tile flow**: Confirmed by both CFD prediction and experimental measurement

<div class="row">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/projects/equinix-thermal-contours-Plane-iso.png" title="Cold aisle temperature distribution" class="img-fluid rounded z-depth-1" %}
    </div>
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/projects/equinix-cold-aisle.png" title="Cold aisle temperature distribution" class="img-fluid rounded z-depth-1" %}
    </div>
</div>
<div class="caption">
    Top: 3D temperature contours in cold aisles showing thermal stratification. Bottom: Longitudinal cross-section through the Angola cold aisle revealing temperature gradients from supply (21°C, blue) to hot spots approaching 40°C (red) where cooling delivery is insufficient.
</div>

## Recommendations

Based on the CFD analysis and experimental validation, **tile-fan repositioning** was recommended to improve airflow delivery to the identified problem areas. By relocating active tiles to regions with confirmed flow deficits, the cooling system can better match the actual thermal load distribution.

## Facility Specifications

| Parameter | Zone A | Zone B|
|-----------|----------|----------|
| Floor Area | 1,542 m² | 1,549 m² |
| Design Capacity | 1,721 kW | 1,633 kW |
| As-Built Load | 441 kW | 410 kW |
| Containment | Mixed | Mixed |
| Supply Temperature | 21°C | 21°C |
| Tile Porosity | 54% | 54% |

## Technical Approach

| Aspect | Method |
|--------|--------|
| Software | ANSYS CFX |
| Turbulence Model | k-ε (RANS) |
| Tile Modeling | Porous media with pressure boundary |
| Rack Modeling | Prescribed heat flux with directional flow |
| Validation | On-site tile flow measurements |
| Assessment | ASHRAE TC 9.9 thermal guidelines |

## Project Impact

This study demonstrated the value of **validated CFD analysis** for complex data center environments. By combining numerical simulation with experimental measurements, the analysis provided:

- Confidence in model predictions through qualitative validation
- Clear identification of thermal risks before they impact operations
- Evidence-based recommendations for cooling system optimization
- Understanding of how mixed configurations create interacting thermal challenges

The methodology established here—CFD prediction validated against tile flow measurements, followed by ASHRAE compliance assessment—provides a template for thermal analysis of facilities where simple rules-of-thumb cannot capture the complexity of real-world configurations.

---
layout: post
title: What happens inside a moka pot? A 3D CFD look at stovetop coffee
date: 2026-11-15 10:00:00
description: A coupled boiler, puck and chamber simulation of a 3-cup moka pot in OpenFOAM-14, driven only by stove heat and the pressure it builds.
tags: cfd openfoam multiphase porous-media coffee
categories: cfd
thumbnail: assets/img/posts/moka-pot/thumb.jpg
toc:
  sidebar: left
---

Most coffee makers push water with a pump. A moka pot has no moving parts: the stove heats a
sealed tank of water, the pressure in that tank rises, and the water is forced up a funnel,
through a packed bed of ground coffee, and out of a spout into the upper chamber. Anyone who
has used one knows the end of the brew: a hiss and a gurgle as steam breaks through.

I wanted to see that whole sequence in a single simulation, with nothing prescribed except the
stove's heat. No inlet velocity and no imposed pressure. Here is what came out.

{% include video.liquid path="assets/video/moka-pot-cfd.mp4" class="img-fluid rounded z-depth-1" controls=true loop=true %}

<div class="caption">
    Full brew, 0 to 163 s. Mid-plane slices of water fraction, temperature, velocity magnitude and
    gauge pressure, with the water free surface in 3D on the right.
</div>

## The case

The geometry is a typical 3-cup aluminium pot: a 74 mm diameter boiler filled with 150 ml of
water at 20 °C, a funnel stem, a 15 mm deep coffee puck held between two perforated plates, and
the upper chamber with its central spout. The domain is fully 3D, meshed as a stacked O-grid
with 110,912 hexahedral cells.

{% include figure.liquid loading="eager" path="assets/img/posts/moka-pot/mesh.png" class="img-fluid rounded z-depth-1" zoomable=true %}

<div class="caption">
    The mesh: 3D half-cut, mid-plane, and cross-sections through the boiler and the upper chamber.
</div>

The physics, in short:

- **Flow:** OpenFOAM-14's `compressibleVoF` solver, two-phase water and air, laminar, with the
  energy equation solved in both phases.
- **Stove:** 400 W delivered into the bottom layer of water in the boiler. Part of it goes into
  heating the aluminium body (a lumped heat capacity of 135 J/K) and part is lost to the room.
- **Evaporation and pressure:** a custom `fvModel` I wrote for this case. It keeps the gas above
  the water at the saturation pressure for the current surface temperature (IAPWS-IF97), adds
  the vapour as gas mass, and takes the latent heat out of the water. The pressure that drives
  the flow is simply what this gas produces as the pot heats up.
- **Coffee puck:** a porous zone with Ergun (Darcy–Forchheimer) resistance,

$$
\frac{\Delta p}{L} = \frac{150\,\mu\,(1-\varepsilon)^2}{\varepsilon^3 d_p^2}\,U
                   + \frac{1.75\,\rho\,(1-\varepsilon)}{\varepsilon^3 d_p}\,U^2 ,
$$

with porosity $$\varepsilon = 0.40$$ and an Ergun-equivalent particle size chosen to give a
permeability of about $$10^{-13}\,\mathrm{m^2}$$, the right order for a moka puck. The grind
and tamping are the two knobs for a parametric study.

## Results

The run ends 15 s after the boiler water drops below the bottom of the stem, at 163.8 s of
simulated time.

{% include figure.liquid loading="eager" path="assets/img/posts/moka-pot/history.png" class="img-fluid rounded z-depth-1" zoomable=true %}

<div class="caption">
    Boiler temperature, pressure, flow into the stem, evaporation, water left in the boiler, and
    liquid in the upper chamber and the puck.
</div>

### A long, quiet start

For the first two minutes very little seems to happen. The boiler warms almost linearly, and
the pressure barely moves: 0.1 bar gauge at 93 s, 0.2 bar at 110 s. That is still enough to
push water slowly up the stem and into the coffee. By 107 s the puck is completely flooded, and
it stays that way until the very end. The first drop reaches the upper chamber at 115 s, while
the water surface is still at about 83 °C.

So the brew starts well before anything boils. The early push comes from the rising vapour
pressure and the heated air above the water, not from boiling.

{% include figure.liquid loading="eager" path="assets/img/posts/moka-pot/frame-120s.png" class="img-fluid rounded z-depth-1" zoomable=true %}

<div class="caption">
    t = 120 s: water just starting to come out of the spout, puck saturated, boiler at 0.26 bar.
</div>

### Then it all comes at once

The pressure curve is strongly non-linear because the saturation pressure of water is. Between
120 s and 150 s the boiler pressure goes from 0.26 to 1 bar gauge, and the coffee arrives:

| time                                  | water in upper chamber |
| ------------------------------------- | ---------------------: |
| 120 s                                 |                   6 ml |
| 140 s                                 |                  45 ml |
| 148.8 s (boiler runs dry at the stem) |                  75 ml |
| 155 s                                 |                 113 ml |
| end                                   |                 122 ml |

More than half the cup arrives in the 30 seconds before the boiler runs dry, when the water is
at its hottest.

### The gurgle

At 148.8 s the water level in the boiler falls below the bottom of the stem, and gas starts
going up with the liquid. This is the hiss and sputter at the end of a real brew. In the
simulation the pressure peaks right here, at 1.36 bar gauge and 153 s, with the boiler water
at about 120 °C. The flow into the stem peaks at 5.7 ml/s, then turns into slugs of liquid and
gas.

{% include figure.liquid loading="eager" path="assets/img/posts/moka-pot/frame-151s.png" class="img-fluid rounded z-depth-1" zoomable=true %}

<div class="caption">
    t = 151.5 s, the sputter phase: gas slugs in the stem, gas breaking into the funnel under the
    puck, and the last liquid being blown through to the chamber.
</div>

About 37 ml, close to a third of the cup, reach the chamber in the six seconds after the
boiler runs dry. Part of it is water that had been sitting in the puck, which drains from full
to nearly empty, and the rest is the last water from the stem and boiler. All of it is pushed
through by gas at the highest pressure and temperature of the whole brew.

This is consistent with the usual advice to take the pot off the heat when it starts to
gurgle: the last part of the brew goes through the coffee hotter and faster than the rest.

## What the model leaves out

This is a first baseline, and it has clear limits:

- **No validation yet.** I haven't compared these numbers with measured pressure or flow from
  a real pot.
- **Evaporation only at the surface.** The model keeps the gas at saturation for the water
  surface, but it doesn't resolve boiling at the hot floor. The floor water gets hotter than
  it would in reality (about 125 °C at the floor against 101 °C at the surface at 140 s).
- **A simple puck.** The porous zone adds flow resistance but takes up no volume, so it holds
  more water than a real puck would. Real pucks also swell as they wet and their permeability
  changes during the brew; here it stays constant.
- **No coffee chemistry.** The fluid is water. Extraction isn't solved.

## Running it

The case runs with OpenFOAM-14, built from source, on a Raspberry Pi 5, in serial (running in
parallel didn't help on this machine). The baseline took about 93 hours of wall-clock time for
164 s of brewing.

Next steps are a boiling model at the heated floor and a parametric sweep of grind size,
tamping and stove power.

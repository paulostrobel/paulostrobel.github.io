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

## Round two: a hexagonal pot, boiling, and a lid

The first run left three things I didn't like: it was slow, the hot floor didn't boil, and the
upper chamber had no lid. That last one matters more than it sounds. With the top of the model
open to the room, about 20 ml of water sprayed straight out during the gurgle, water a real
pot would have caught.

So I changed three things.

**A hexagonal pot, simulated as one sixth.** Most moka pots are octagonal or hexagonal on the
outside. I made the boiler and the upper chamber hexagonal, with the same cross-section area
as the round version, and kept the stem, basket and column round. A hexagon repeats every 60°,
so only one 60° slice needs to be meshed. Its two cut faces are joined by a periodic (rotational
`cyclic`) boundary: whatever leaves one face comes back in through the other. That's 20,391
cells instead of 110,912, and about 14× faster per simulated second. The full pot in the plots
and animation is the slice copied six times.

{% include figure.liquid loading="eager" path="assets/img/posts/moka-pot/hex-mesh.jpg" class="img-fluid rounded z-depth-1" zoomable=true %}

<div class="caption">
    The hexagonal pot, rebuilt from the 60° slice. The red lines in the cross-sections are the
    slice's periodic faces.
</div>

**Boiling at the floor.** The `fvModel` now also turns any tank water hotter than the boiling
point at the current pressure into vapour, over a relaxation time of 0.02 s. In the first run
the water at the floor got about 10 °C hotter than it should have. With boiling, it stays at
the boiling point: 121 °C at 149 s instead of 131 °C.

**A lid with a small vent.** The top of the upper chamber is now a wall, except a thin ring
2 mm wide next to the chamber wall. That's 352 mm² for the whole pot, enough for air and steam
to leave without any back-pressure.

I also had to add a temperature limiter. During the gurgle, one cell in the froth sent its
temperature to −900 K and crashed the first boiling run. Clipping temperatures to 280–450 K
fixed that. A side effect I didn't expect: the slow loss of water mass every run had shown,
about 5% over the brew, dropped to about 2%. A few bad cells seem to have been behind that too.

{% include video.liquid path="assets/video/moka-pot-hex-lid.mp4" class="img-fluid rounded z-depth-1" controls=true loop=true %}

<div class="caption">
    The hexagonal pot with boiling and a lid, 0 to 168.5 s.
</div>

The brew itself looks very similar. First water reaches the chamber at 117 s, the gurgle starts
at 153.5 s, and the pressure peaks at 1.33 bar gauge, a little lower than the round pot's 1.36 bar.
The difference is at the end:

|                            | round, open top | hexagon, open top | hexagon, boiling, lid |
| -------------------------- | --------------: | ----------------: | --------------------: |
| water in the upper chamber |          122 ml |            111 ml |            **140 ml** |
| lost out of the top        |           21 ml |             28 ml |              **4 ml** |

Out of 150 ml filled, 140 ml ends up in the cup and about 5 ml stays in the puck.

{% include figure.liquid loading="eager" path="assets/img/posts/moka-pot/hex-lid-157s.jpg" class="img-fluid rounded z-depth-1" zoomable=true %}

<div class="caption">
    t = 157.5 s, during the gurgle. The jet from the spout reaches the lid, which keeps the spray in the
    chamber.
</div>

{% include figure.liquid loading="eager" path="assets/img/posts/moka-pot/hex-comparison.png" class="img-fluid rounded z-depth-1" zoomable=true %}

<div class="caption">
    The three hexagonal runs: no boiling, boiling with an open top (it crashed at 154 s), and
    boiling with the lid.
</div>

## Grind, tamping and stove power

With a case that runs in about 6 hours, a small parametric sweep became possible. Starting from
the lidded hexagonal pot (9.2 µm grind, porosity 0.40, 400 W), I changed one setting at a time.
The "brew window" is the time from the first water in the upper chamber to the gurgle.

| change               | puck permeability [m²] | first water |  gurgle | brew window | peak pressure | in the cup |
| -------------------- | ---------------------: | ----------: | ------: | ----------: | ------------: | ---------: |
| none (baseline)      |                1.0e-13 |       117 s | 153.5 s |        36 s |      1.33 bar |     140 ml |
| finer grind, 7 µm    |                5.8e-14 |       123 s |   162 s |        39 s |      1.92 bar |     137 ml |
| coarser grind, 12 µm |                1.7e-13 |       111 s | 140.5 s |        29 s |      1.03 bar |     136 ml |
| harder tamp, ε 0.35  |                5.7e-14 |       124 s |   164 s |        40 s |      1.99 bar |     137 ml |
| lighter tamp, ε 0.45 |                1.7e-13 |       110 s | 140.6 s |        31 s |      1.01 bar |     137 ml |
| 300 W stove          |                1.0e-13 |       148 s |   193 s |        45 s |      1.16 bar |     135 ml |
| 600 W stove          |                1.0e-13 |        83 s |   106 s |        22 s |      1.78 bar |     139 ml |

**Grind and tamping are the same knob.** In this model both act only through the puck's
permeability. A 7 µm grind and a firm tamp to porosity 0.35 give almost the same permeability,
and the brews are nearly identical. The same goes for a 12 µm grind and a light tamp. A real
puck isn't that simple: grind changes how fast coffee dissolves, and tamping changes how the
puck swells. But for the flow, one number does most of the work.

**A tighter puck brews later and under more pressure.** Halving the permeability raises the
peak pressure from 1.33 to about 1.95 bar and delays the gurgle by about 9 s. The boiler has
to get hotter before it can push water through, so the water reaching the coffee is hotter
too.

{% include figure.liquid loading="eager" path="assets/img/posts/moka-pot/sweep-grind.png" class="img-fluid rounded z-depth-1" zoomable=true %}

<div class="caption">
    Grind size: 7 µm, 9.2 µm (baseline) and 12 µm.
</div>

**Stove power sets the clock.** At 600 W the first water arrives at 83 s and the whole brew
is over in 22 s, with the peak pressure at 1.78 bar. At 300 W it takes 148 s to start and
45 s to brew. Low heat stretches the brew out, which is the usual advice for a moka pot.

{% include figure.liquid loading="eager" path="assets/img/posts/moka-pot/sweep-stove.png" class="img-fluid rounded z-depth-1" zoomable=true %}

<div class="caption">
    Stove power: 300 W, 400 W (baseline) and 600 W.
</div>

**The cup hardly changes.** Every run ends with 135–140 ml in the upper chamber. With the
lid on, the settings change how fast and how hot the water goes through the coffee, not how
much of it ends up in the cup.

## What the model leaves out

It still has clear limits:

- **No validation yet.** I haven't compared these numbers with measured pressure or flow from
  a real pot.
- **Simple boiling.** Boiling at the floor is a relaxation to the boiling point, not resolved
  bubbles. It caps the floor temperature but doesn't model how bubbles stir the water.
- **A symmetric pot.** The 60° slice forces the flow to repeat six times around the pot, so it
  can't show a gurgle that sloshes to one side.
- **A simple puck.** The porous zone adds flow resistance but takes up no volume, so it holds
  more water than a real puck would. Real pucks also swell as they wet and their permeability
  changes during the brew; here it stays constant.
- **No coffee chemistry.** The fluid is water. Extraction isn't solved.

## Running it

The case runs with OpenFOAM-14, built from source, on a Raspberry Pi 5, in serial (running in
parallel didn't help on this machine). The baseline took about 93 hours of wall-clock time for
164 s of brewing.

The hexagonal slice takes about 6 hours for a full brew on the same Pi; the six sweep runs
took about two days. Next would be validation against a real pot with a pressure sensor, and
extraction: solving for dissolved coffee instead of plain water.

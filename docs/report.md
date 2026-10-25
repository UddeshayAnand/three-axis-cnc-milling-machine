# Technical report

## Problem and original approach

The project objective was a cost-effective, functioning three-axis CNC machine for teaching and demonstration. MDF, dowel nuts and bolts, linear guides, stepper motors and Mach3 are used in the implementation. CAD drawings document a mechanical assembly with screw-driven linear stages.

## Equations and units

For a directly coupled motor with N full steps/revolution, microstep subdivision m and screw lead L in mm/revolution:

`commanded steps/mm = N × m / L`

`nominal command increment (mm) = 1 / commanded steps/mm`

`pulse frequency (Hz) = commanded steps/mm × feed (mm/min) / 60`

Lead is axial travel per revolution and may differ from thread pitch for a multi-start screw. These formulas assume no belt or gearbox ratio.

For assumed motor torque T (N m) and screw efficiency eta:

`ideal axial force (N) = 2 × pi × T × eta / lead (m)`

For one ideal simply supported solid circular rail carrying a central load F:

`I = pi × d^4 / 64`

`deflection = F × span^3 / (48 × E × I)`

All beam quantities use SI units internally. Results are converted to millimetres. The example uses 10 N on one rail, 500 mm unsupported span, 8 mm diameter and an assumed 200 GPa modulus. Doubling unsupported span increases deflection eightfold; doubling diameter reduces it sixteenfold. Actual machine stiffness also depends on MDF, joint compliance, bearing clearances and tool overhang.

For the synthetic path, Euclidean segment lengths are summed in three dimensions. Ideal time equals length divided by feed. Acceleration, corner blending, cutting engagement and tool compensation are excluded. The rectangle is a tool-center trajectory.

## Results and interpretation

The demonstration yields 200 steps/mm, 0.005 mm nominal increments, 2 kHz pulse frequency, approximately 235.619 N ideal axial force and approximately 0.648 mm single-rail deflection under the stated artificial scenario. The 260 mm rectangle requires an ideal 26 seconds. The deflection calculation illustrates why unsupported span matters.

## Source and saved artifacts

The toolkit uses only the Python standard library. Its calculation source is in [engineering.py](../src/cnc_portfolio/engineering.py), and the demonstration inputs are in [demo.json](../config/demo.json). The supplied [summary](../results/summary.json), [path coordinates](../results/toolpath.csv), and [SVG diagram](../results/toolpath.svg) are the recorded computational example without requiring proprietary CAD or Mach3 access.

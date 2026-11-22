# Heading gain tuning

I changed the heading kp (the proportional gain of the heading controller) and ran the full demo for each value: a 60 deg heading step, and the waypoint mission with and without ocean current. All other gains stayed at their defaults. Each value was run once with the same noise seed.

| Heading kp | Rise time (s) | Overshoot (%) | Settling time (s) | Steady-state error (deg) | Peak roll/pitch (deg) | Mission RMS, with current (m) | Mission max, with current (m) | Mission RMS, no current (m) |
|---|---|---|---|---|---|---|---|---|
| 4.0 (default) | 1.62 | 4.4 | 7.12 | 0.42 | 4.78 | 0.224 | 0.484 | 0.147 |
| 6.0 | 1.16 | 2.6 | 5.34 | 0.24 | 4.40 | 0.241 | 0.551 | 0.170 |
| 8.0 | 0.88 | 1.9 | 1.48 | 0.15 | 4.08 | 0.244 | 0.578 | 0.186 |

## What I found
- A higher heading kp makes the heading step faster and smoother, with less overshoot, shorter settling time and smaller steady-state error.
- The waypoint mission got worse as kp went up: cross-track RMS rose about 9% with current and 27% without it, and the worst-case error rose about 19% with current.
- Most of the with-current penalty already appeared at kp 6.0, while the step improvement was only partial. So 6.0 is not a good compromise here.
- Settling time does not change smoothly (7.12, 5.34, 1.48 s), because it is measured against a narrow band of +/-2% around the target.
- The depth results did not change, so the depth and heading loops behave independently.

## Decision
I am keeping kp = 4.0 as the default, because tracking the path is the main job of the vehicle.

## What I don't know yet
- Why a faster heading response hurts path tracking. My guesses are that the vehicle swings through the waypoint corners, or that a higher kp amplifies sensor noise. I have not tested either.
- Each value was run once, so small differences are not reliable.

## Next
- Compare the corners in the mission plot at kp 4.0 and 8.0.
- Try changing the heading kd, and the guidance lookahead distance.
- Label each plot with its scenario and add gridlines.
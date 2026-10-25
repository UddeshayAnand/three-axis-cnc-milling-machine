import math


def positive(value, name):
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value) or value <= 0:
        raise ValueError(f"{name} must be a finite positive number")
    return value


def steps_per_mm(full_steps, microsteps, lead_mm):
    for value, name in ((full_steps, 'full_steps'), (microsteps, 'microsteps')):
        positive(value, name)
        if int(value) != value:
            raise ValueError(f"{name} must be an integer")
    return full_steps * microsteps / positive(lead_mm, 'lead_mm')


def pulse_rate(steps_mm, feed_mm_min):
    return positive(steps_mm, 'steps_mm') * positive(feed_mm_min, 'feed_mm_min') / 60


def ideal_axial_force(torque_nm, lead_mm, efficiency):
    positive(efficiency, 'efficiency')
    if efficiency > 1:
        raise ValueError('efficiency must not exceed one')
    return 2 * math.pi * positive(torque_nm, 'torque_nm') * efficiency / (positive(lead_mm, 'lead_mm') / 1000)


def rail_deflection_mm(load_n, span_mm, diameter_mm, youngs_modulus_pa):
    """Simply supported solid round rail, one central point load; metres internally."""
    force = positive(load_n, 'load_n')
    span = positive(span_mm, 'span_mm') / 1000
    diameter = positive(diameter_mm, 'diameter_mm') / 1000
    inertia = math.pi * diameter ** 4 / 64
    return force * span ** 3 / (48 * positive(youngs_modulus_pa, 'youngs_modulus_pa') * inertia) * 1000


def rectangle(width_mm, height_mm):
    w, h = positive(width_mm, 'width_mm'), positive(height_mm, 'height_mm')
    return [(0.0, 0.0, 0.0), (w, 0.0, 0.0), (w, h, 0.0), (0.0, h, 0.0), (0.0, 0.0, 0.0)]


def path_length_mm(points):
    points = list(points)
    if len(points) < 2:
        raise ValueError('At least two points are required')
    for point in points:
        if len(point) != 3 or any(isinstance(v, bool) or not isinstance(v, (int, float)) or not math.isfinite(v) for v in point):
            raise ValueError('Each point must contain three finite coordinates')
    return sum(math.dist(a, b) for a, b in zip(points, points[1:]))

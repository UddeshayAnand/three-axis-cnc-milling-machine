import math
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from cnc_portfolio.engineering import steps_per_mm, pulse_rate, ideal_axial_force, rail_deflection_mm, rectangle, path_length_mm


class EngineeringTests(unittest.TestCase):
    def test_known_calibration(self):
        self.assertEqual(steps_per_mm(200, 8, 8), 200)
        self.assertEqual(pulse_rate(200, 600), 2000)

    def test_lead_scaling(self):
        self.assertEqual(steps_per_mm(200, 8, 4), 2 * steps_per_mm(200, 8, 8))

    def test_work_energy_consistency(self):
        force = ideal_axial_force(1, 8, 0.3)
        self.assertAlmostEqual(force * 0.008, 2 * math.pi * 0.3)

    def test_beam_scaling(self):
        base = rail_deflection_mm(10, 500, 8, 200e9)
        self.assertAlmostEqual(rail_deflection_mm(10, 1000, 8, 200e9), base * 8)
        self.assertAlmostEqual(rail_deflection_mm(10, 500, 16, 200e9), base / 16)

    def test_closed_rectangle(self):
        points = rectangle(80, 50)
        self.assertEqual(points[0], points[-1])
        self.assertEqual(path_length_mm(points), 260)

    def test_three_dimensional_path(self):
        self.assertEqual(path_length_mm([(0, 0, 0), (3, 4, 12)]), 13)

    def test_invalid_inputs(self):
        for value in [0, -1, float('nan'), float('inf'), True, '8']:
            with self.subTest(value=value), self.assertRaises(ValueError):
                steps_per_mm(200, 8, value)
        with self.assertRaises(ValueError):
            steps_per_mm(200, 1.5, 8)
        with self.assertRaises(ValueError):
            ideal_axial_force(1, 8, 1.1)
        for points in [[], [(0, 0, 0)], [(0, 0), (1, 2)], [(0, 0, 0), (1, 2, float('nan'))]]:
            with self.assertRaises(ValueError):
                path_length_mm(points)


if __name__ == '__main__':
    unittest.main()

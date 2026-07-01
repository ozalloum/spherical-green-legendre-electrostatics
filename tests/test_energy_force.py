"""Tests for image energy and signed radial force formulas."""

import unittest

from src.observables import image_energy, signed_radial_force


class EnergyForceTest(unittest.TestCase):
    def test_image_energy_endpoint(self):
        self.assertAlmostEqual(image_energy(0.02), -0.5002000800320128, places=12)

    def test_signed_force_endpoint(self):
        self.assertAlmostEqual(signed_radial_force(0.02), -0.02001600960480192, places=12)


if __name__ == "__main__":
    unittest.main()

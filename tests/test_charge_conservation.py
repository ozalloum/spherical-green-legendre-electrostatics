"""Tests for total induced charge conservation."""

import unittest

import numpy as np

from src.observables import integrate_total_induced_charge, surface_charge_exact


class ChargeConservationTest(unittest.TestCase):
    def test_total_induced_charge_is_minus_one(self):
        theta = np.linspace(0.0, np.pi, 20001)
        sigma = surface_charge_exact(theta, b=0.45)
        total_charge = integrate_total_induced_charge(theta, sigma)
        self.assertAlmostEqual(total_charge, -1.0, places=6)


if __name__ == "__main__":
    unittest.main()

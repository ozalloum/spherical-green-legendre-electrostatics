"""Tests for the grounded-sphere boundary condition."""

import unittest

import numpy as np

from src.image_solution import image_potential


class BoundaryConditionTest(unittest.TestCase):
    def test_exact_potential_vanishes_on_boundary(self):
        theta = np.linspace(0.05, np.pi - 0.05, 200)
        phi = image_potential(r=1.0, theta=theta, b=0.45)
        self.assertLess(np.max(np.abs(phi)), 1.0e-12)


if __name__ == "__main__":
    unittest.main()

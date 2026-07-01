"""Derived electrostatic observables for the grounded-sphere problem."""

from __future__ import annotations

import numpy as np


def surface_charge_exact(theta, b: float):
    """Return the exact normalized induced surface charge density.

    The expression is

        sigma(theta) = -(1-b^2)/(4*pi*(1+b^2-2*b*cos(theta))^(3/2)).
    """
    if not (0.0 < b < 1.0):
        raise ValueError("b must satisfy 0 < b < 1.")

    theta = np.asarray(theta, dtype=float)
    denom = (1.0 + b**2 - 2.0 * b * np.cos(theta)) ** 1.5
    return -(1.0 - b**2) / (4.0 * np.pi * denom)


def image_energy(b: float):
    """Return the dimensionless image energy U(b)."""
    if not (0.0 < b < 1.0):
        raise ValueError("b must satisfy 0 < b < 1.")
    return -1.0 / (2.0 * (1.0 - b**2))


def signed_radial_force(b: float):
    """Return the signed radial force convention used in the manuscript."""
    if not (0.0 < b < 1.0):
        raise ValueError("b must satisfy 0 < b < 1.")
    return -b / (1.0 - b**2) ** 2


def integrate_total_induced_charge(theta, sigma):
    """Integrate sigma(theta) over the unit sphere using trapezoidal quadrature."""
    theta = np.asarray(theta, dtype=float)
    sigma = np.asarray(sigma, dtype=float)
    return 2.0 * np.pi * np.trapz(sigma * np.sin(theta), theta)

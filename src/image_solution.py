"""Exact image-charge Green-function solution for a grounded sphere."""

from __future__ import annotations

import numpy as np


def image_potential(r, theta, b: float):
    """Return the exact dimensionless image-charge potential.

    Parameters
    ----------
    r : array_like
        Dimensionless radius, 0 <= r <= 1.
    theta : array_like
        Polar angle in radians.
    b : float
        Dimensionless source position, 0 < b < 1.

    Returns
    -------
    numpy.ndarray
        Potential Phi_img(r, theta) in normalized units.
    """
    if not (0.0 < b < 1.0):
        raise ValueError("b must satisfy 0 < b < 1.")

    r = np.asarray(r, dtype=float)
    theta = np.asarray(theta, dtype=float)
    mu = np.cos(theta)

    physical = np.sqrt(r**2 + b**2 - 2.0 * r * b * mu)
    image = np.sqrt(r**2 + b**(-2) - 2.0 * r * b**(-1) * mu)

    return 1.0 / physical - (1.0 / b) / image

"""Finite Legendre-series approximation for the grounded-sphere problem."""

from __future__ import annotations

import numpy as np
from numpy.polynomial.legendre import legval


def legendre_potential(r, theta, b: float, L: int):
    """Return the finite-L Legendre-series potential.

    The implementation evaluates

        Phi_L(r, theta) = sum_{ell=0}^{L}
        [r_<^ell/r_>^(ell+1) - b^ell r^ell] P_ell(cos theta).

    Parameters
    ----------
    r : array_like
        Dimensionless radius, 0 <= r <= 1.
    theta : array_like
        Polar angle in radians.
    b : float
        Dimensionless source position, 0 < b < 1.
    L : int
        Maximum multipole degree.

    Returns
    -------
    numpy.ndarray
        Truncated Legendre potential Phi_L.
    """
    if not (0.0 < b < 1.0):
        raise ValueError("b must satisfy 0 < b < 1.")
    if L < 0:
        raise ValueError("L must be nonnegative.")

    r = np.asarray(r, dtype=float)
    theta = np.asarray(theta, dtype=float)
    mu = np.cos(theta)

    out = np.zeros(np.broadcast_shapes(r.shape, theta.shape), dtype=float)
    rb = np.broadcast_to(r, out.shape)
    mub = np.broadcast_to(mu, out.shape)

    r_less = np.minimum(rb, b)
    r_greater = np.maximum(rb, b)

    for ell in range(L + 1):
        coeffs = np.zeros(ell + 1)
        coeffs[-1] = 1.0
        p_ell = legval(mub, coeffs)
        radial = r_less**ell / r_greater**(ell + 1) - (b**ell) * (rb**ell)
        out += radial * p_ell

    return out

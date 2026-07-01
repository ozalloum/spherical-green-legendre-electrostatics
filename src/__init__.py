"""Spherical Green-Legendre electrostatics utilities.

Dimensionless units are used throughout:
    a = 1, q = 1, 1/(4*pi*epsilon0) = 1.
"""

from .image_solution import image_potential
from .legendre_solution import legendre_potential
from .observables import surface_charge_exact, image_energy, signed_radial_force
from .errors import relative_l2_error

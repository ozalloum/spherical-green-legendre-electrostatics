"""Error metrics used by the reproducibility workflow."""

from __future__ import annotations

import numpy as np


def relative_l2_error(approx, reference, mask=None):
    """Return relative L2 error ||approx-reference||_2 / ||reference||_2.

    Parameters
    ----------
    approx, reference : array_like
        Numerical arrays to compare.
    mask : array_like of bool, optional
        True values are included in the norm. If omitted, finite values are used.
    """
    approx = np.asarray(approx, dtype=float)
    reference = np.asarray(reference, dtype=float)

    if mask is None:
        mask = np.isfinite(approx) & np.isfinite(reference)
    else:
        mask = np.asarray(mask, dtype=bool) & np.isfinite(approx) & np.isfinite(reference)

    numerator = np.linalg.norm(approx[mask] - reference[mask])
    denominator = np.linalg.norm(reference[mask])
    if denominator == 0.0:
        raise ZeroDivisionError("Reference norm is zero.")
    return numerator / denominator

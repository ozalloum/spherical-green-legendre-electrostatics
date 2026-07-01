"""End-to-end reproduction entry point for the CPC manuscript.

This lightweight script verifies that the repository contains the expected
reproducibility folders and lists the CSV datasets used by the manuscript.
The full numerical reproduction workflow is also documented in the notebook
under notebooks/.
"""

from __future__ import annotations

from pathlib import Path


REQUIRED_DIRS = [
    "src",
    "tests",
    "data",
    "tables",
    "figures",
    "notebooks",
    "scripts",
    "metadata",
    "manuscript",
]


def main() -> None:
    root = Path(__file__).resolve().parents[1]

    missing_dirs = [name for name in REQUIRED_DIRS if not (root / name).exists()]
    if missing_dirs:
        raise FileNotFoundError(
            "Missing expected repository directories: " + ", ".join(missing_dirs)
        )

    data_files = sorted((root / "data").glob("*.csv"))
    table_files = sorted((root / "tables").glob("*.csv"))
    figure_files = sorted((root / "figures").glob("*"))

    print("Spherical Green-Legendre Electrostatics reproduction check")
    print(f"Repository root: {root}")
    print(f"Figure CSV files: {len(data_files)}")
    print(f"Table CSV files: {len(table_files)}")
    print(f"Figure files: {len(figure_files)}")
    print("Expected repository structure is present.")
    print("For full numerical reproduction, use the notebook in notebooks/.")


if __name__ == "__main__":
    main()

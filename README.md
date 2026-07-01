# Spherical Green-Legendre Electrostatics
![Reproducibility Check](https://github.com/ozalloum/spherical-green-legendre-electrostatics/actions/workflows/reproducibility-check.yml/badge.svg)

Reproducible Green-function and Legendre-series electrostatic solver for a point charge inside a grounded conducting sphere.

This repository supports the manuscript:

**A Reproducible Computational Framework for Green-Function and Legendre-Series Solutions in Spherical Electrostatics**  
Othman H. Y. Zalloum

## Purpose

This project provides a reproducible computational workflow for comparing the exact image-charge Green-function solution with finite Legendre-series truncations. It includes potential evaluation, induced surface charge density, image energy, signed radial force, multipole coefficient decay, computational-cost trends, and spatial truncation-error maps.

## Repository structure

```text
src/         Source-code modules for the analytical solution, Legendre solver, observables, and error metrics
tests/       Validation tests for boundary condition, charge conservation, and energy/force formulas
manuscript/  LaTeX manuscript and compiled PDF
figures/     Publication figures
data/        Figure CSV datasets
tables/      Table CSV datasets
notebooks/   Jupyter reproduction notebook
scripts/     Figure/data regeneration scripts
metadata/    Verification notes and included-file documentation
output/      Optional generated outputs
```

## Requirements

```bash
pip install numpy scipy matplotlib pandas jupyter
```

or, with Conda:

```bash
conda env create -f environment.yml
```

## Reproducing the results

The numerical data used in the manuscript are provided as CSV files in `data/` and `tables/`.

To check the repository structure, run:

```bash
python scripts/generate_all_results_cpc.py
```

To run the validation tests, run:

```bash
python -m unittest discover -s tests
```

## Citation

A formal citation and DOI will be added after journal submission or repository archiving.

## License

This repository is released under the MIT License.

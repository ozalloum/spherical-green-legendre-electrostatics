# Spherical Green-Legendre Electrostatics

Reproducible Green-function and Legendre-series electrostatic solver for a point charge inside a grounded conducting sphere.

This repository supports the manuscript:

**A Reproducible Computational Framework for Green-Function and Legendre-Series Solutions in Spherical Electrostatics**  
Othman H. Y. Zalloum

## Purpose

This project provides a reproducible computational workflow for comparing the exact image-charge Green-function solution with finite Legendre-series truncations. It includes potential evaluation, induced surface charge density, image energy, signed radial force, multipole coefficient decay, computational-cost trends, and spatial truncation-error maps.

## Repository structure

```text
manuscript/   LaTeX manuscript and compiled PDF
figures/      Publication figures
data/         Figure CSV datasets
tables/       Table CSV datasets
notebooks/    Jupyter reproduction notebook
scripts/      Figure/data regeneration scripts, if added
metadata/     Verification notes and included-file documentation
output/       Optional generated outputs
```

## Requirements

```bash
pip install numpy scipy matplotlib pandas jupyter
```

## Reproducing the results

Open the notebook in `notebooks/` or run the scripts in `scripts/` after installing the required Python packages. The numerical data used in the manuscript are provided as CSV files in `data/` and `tables/`.

## Citation

A formal citation and DOI will be added after journal submission or Zenodo deposition.

## License

This repository is released under the MIT License.

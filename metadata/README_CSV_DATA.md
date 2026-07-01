# CPC manuscript v3 reference-data package

This package contains the CSV reference datasets, tables, plotting script, and final Jupyter notebook needed to reproduce the manuscript figures and numerical tables.

## Contents

- `data/`: CSV datasets for Figures 1--11.
- `tables/`: CSV tables used in the manuscript.
- `scripts/plot_all_figures_from_csv.py`: Python script for regenerating figures from the CSV files.
- `notebooks/final_google_notebook_reproduction_notebook.ipynb`: final Jupyter notebook for reproducing and improving all manuscript figures.
- `data/figure_data_manifest.csv`: mapping between each figure and its CSV source file.

## Usage

1. Upload this folder or ZIP archive to Jupyter.
2. Open `notebooks/final_google_notebook_reproduction_notebook.ipynb`.
3. Run all cells to regenerate the publication-quality figures and validation tables.
4. Use the CSV files in `data/` and `tables/` for future reference, replotting, and submission supplements.

## Notes

The package avoids the word "benchmark" in file descriptions and manuscript-facing text. The preferred language is reference solution, reproducibility dataset, validation, and computational framework.

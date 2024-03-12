# Model to Distance Converter

## Introduction

The Model to Distance Converter transforms 3D genomic models from single-cell data into distance matrices by calculating pairwise Euclidean distances between genomic bins 
## Features

- Generates distance matrices from `.dim` files containing 3D genomic coordinates.
- Produces heatmaps for visual representation of the distance matrices, facilitating an intuitive understanding of spatial genomic 
relationships.

## Getting Started

### Prerequisites

Before using the Model to Distance Converter, ensure you have Python 3.8 or later installed on your system, along with the following 
libraries:
- Pandas
- NumPy
- Matplotlib
- Seaborn
- SciPy

These dependencies can be installed using pip:
```bash
pip install pandas numpy matplotlib seaborn scipy
```
## Usage
```bash
python model2distance.py -i /path/to/your/model.dim -o /path/to/output
```

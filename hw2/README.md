# Homework 2. LaTeX Generator Library

## Overview

This library provides functionality to generate LaTeX code for tables
and figures from Python data structures and to compile
LaTeX PDF format. This is an ideal starting point for Python
developers looking to integrate LaTeX generation into their
projects without prior LaTeX experience.

## Features

- **Table Generation**: Convert 2D lists into formatted LaTeX tables.
- **Figure Generation**: Integrate PNG images into LaTeX documents.
- **Library Packaging**: Code is packaged using setuptools for easy distribution and installation via PyPI.
- **Docker Integration**: Includes a Dockerfile to encapsulate LaTeX dependencies and build processes.

## Artifacts

- A sample `.tex` file demonstrating the table generation functionality.
- A PDF document compiled from LaTeX, featuring both the generated table and an embedded PNG image.
- [The Python package](https://pypi.org/project/latexgen/), available on PyPI, which can be installed using `pip install latexgen==0.3`.
- Dockerfile located in the `hw02` folder to reproduce the environment and build process.

## Usage
### Using Docker

To generate LaTeX pdf with table and image:

On Windows:
```
docker-compose up
```

on Linux:
```
docker compose up
```
This runs the `task2.py` that saves output to `artefacts/artefact.tex`.
Then it is compiled to `artefact/artefact.pdf` via `pdflatex`.

## Example of using `latexgen` library

```python
from latexgen import generate_table
latex_code = generate_table([[1, 2, 3], [4, 5, 6]])

image_path = "some/path/picture"
latex_image = generate_png(image_path)


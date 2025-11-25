# EartCARE ATLID readers

Make the EartCARE ATLID H5 files readable with xarray and netcdf4 compatible.

## Installation

```bash
pip install git+https://github.com/WillemMarais/atlidreader.git
```

## Command line interface

To convert an ATLID H5 file:
```bash
atlidtonetcdf convert ECA_EXBA_ATL_AER_2A_20240818T155957Z_20250721T104945Z_01271E.h5 [optional output file path]
```
The above command (without the square brackets) creates and output file `ECA_EXBA_ATL_AER_2A_20240818T155957Z_20250721T104945Z_01271E.nc`.

## Supported files

The following ATLID files are supported to thus far:

1. `ECA_EXBA_ATL_AER_2A*`

## Developer tools

Create the conda enviroment in which the developent is done:
```bash
/bin/bash scripts/create_dev_conda_env.bash
```
Then install pre-commit once the git repository has been cloned:
```bash
pre-commit install
```

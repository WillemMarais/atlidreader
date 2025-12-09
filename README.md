# EartCARE ATLID readers

Make the EartCARE ATLID H5 files readable with xarray and netcdf4 compatible.

## Prior to installing this package

For whatever reason the netcdf4 libraries installed via pip does not always work if you use conda and pip together. It is best to first create a conda enviroment, install the netcdf4 library via conda, and then install subsequent packages via pip. Either use the script `scripts/create_dev_conda_env.bash` create a conda enviroment for you (which is called `atlidreader`), or you can execute
```bash
(base) [willemm@server ~]$ conda create --name atlidreader "python<3.14" netcdf4 hatch gitpython pip -y -c conda-forge
```

## Installation

```bash
# Make sure that you are the correct conda environment
(base) [willemm@server ~]$ conda activate atlidreader
# Then install the atlid reader
(atlidreader) [willemm@server ~]$ pip install git+https://github.com/WillemMarais/atlidreader.git
```

## Command line interface

To convert an ATLID H5 file:
```bash
(atlidreader) [willemm@server ~]$ atlidtonetcdf convert ECA_EXBA_ATL_AER_2A_20240818T155957Z_20250721T104945Z_01271E.h5 [optional output file path]
```
The above command (without the square brackets) creates and output file `ECA_EXBA_ATL_AER_2A_20240818T155957Z_20250721T104945Z_01271E.nc`.

## Supported files

The following ATLID files are supported to thus far:

1. `ECA_EXBA_ATL_AER_2A*`

## Sample test files

A sample `ECA_EXBA_ATL_AER_2A*` is available in the SFTP directory
```
https://ftp.ssec.wisc.edu/pub/willemm/atlidreader/
```
For example,
```bash
(atlidreader) [willemm@server ~]$ wget https://ftp.ssec.wisc.edu/pub/willemm/atlidreader/ECA_EXBA_ATL_AER_2A_20240813T153830Z_20250721T104244Z_01193E.h5
(atlidreader) [willemm@server ~]$ atlidtonetcdf convert ECA_EXBA_ATL_AER_2A_20240813T153830Z_20250721T104244Z_01193E.h5
```
will produce a netcdf4 in the home directory:
```bash
(atlidreader) [willemm@server ~]$ ls -1 ECA_EXBA_ATL_AER_2A_20240813T153830Z_20250721T104244Z_01193E.nc
ECA_EXBA_ATL_AER_2A_20240813T153830Z_20250721T104244Z_01193E.nc
```

## Developer tools

Create the conda enviroment in which the developent is done:
```bash
/bin/bash scripts/create_dev_conda_env.bash
```
Then install pre-commit once the git repository has been cloned:
```bash
pre-commit install
```

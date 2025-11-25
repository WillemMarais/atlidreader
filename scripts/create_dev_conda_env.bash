#!/usr/bin/env bash

# Get the directory where the script is located
SCRIPTPATH="$( cd -- "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"/..

# Get the conda path
conda_dirP_str=$(dirname $(dirname $(which conda)))

# If the conda environment already exists, remove it
conda env list \
    | grep "\"${conda_dirP_str}/envs/atlidreader\"" > /dev/null 2>&1 \
    || conda remove --name atlidreader --all --yes

# Create environment
conda create --name atlidreader "python<3.14" hatch gitpython pip -y -c conda-forge

# First make sure that we are in the correct
# conda environment
source activate base
conda_env_str=$(printenv | grep -i conda | grep CONDA_DEFAULT_ENV | cut -d "=" -f 2)
if [ "$conda_env_str" != "atlidreader" ]; then
    conda activate atlidreader
fi

# Check that we are now in the correct conda
# environment
conda_env_str=$(printenv | grep -i conda | grep CONDA_DEFAULT_ENV | cut -d "=" -f 2)
if [ "$conda_env_str" != "atlidreader" ]; then
    echo "Could not enter the atlidreader conda environment."
    exit 1
fi

# Get the pip path to the new env
miniconda_dirP=$(dirname $(dirname $(which python)))
pip_fileP=${miniconda_dirP}/bin/pip
python_fileP=${miniconda_dirP}/bin/python3

# Install atlidreader
${pip_fileP} install -e ${SCRIPTPATH}

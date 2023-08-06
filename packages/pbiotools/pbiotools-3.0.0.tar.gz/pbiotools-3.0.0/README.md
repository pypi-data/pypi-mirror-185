# pbiotools [![install with bioconda](https://img.shields.io/badge/install%20with-bioconda-brightgreen.svg?style=flat)](http://bioconda.github.io/recipes/pbiotools/README.html) [![pypi releases](https://img.shields.io/pypi/v/pbiotools.svg)](https://pypi.org/project/pbiotools) [![CI](https://github.com/dieterich-lab/pbiotools/actions/workflows/ci.yml/badge.svg)](https://github.com/dieterich-lab/pbiotools/actions/workflows/ci.yml)

The `pbiotools` package provides miscellaneous bioinformatics and other supporting utilities for Python 3, including
programs used for Ribo-seq periodicity estimation. It is required for the installation of [Rp-Bp](https://github.com/dieterich-lab/rp-bp).
It combines utilities and programs from the defunct pymisc-utils (see [pyllars](https://github.com/bmmalone/pyllars))
and [riboseq-utils](https://github.com/dieterich-lab/riboseq-utils).

## Installation

To install from [PyPI](https://pypi.org/project/pbiotools/) using pip:

```
pip install pbiotools
```

To install from bioconda using conda, set up [bioconda](https://bioconda.github.io/#usage) if not already done, then:

```
conda install pbiotools
```

To get a docker container from biocontainers with pbiotools pre-installed:

```
docker pull quay.io/biocontainers/pbiotools:2.0.0--pyhdfd78af_0
```

To install the local VCS project in development mode, use the `--editable` or `-e` option, otherwise
this flag can be ignored.

Pinned version of selected dependencies are listed in the `requirements.txt` file for reproducible installation.

## Installation (virtual environment)

To install `pbiotools` and dependencies, first create a virtual environment:

```
python3 -m venv /path/to/virtual/environment
```

For information about Python virtual environments, see the [venv](https://docs.python.org/3/library/venv.html) documentation.
To activate the new virtual environment and install `pbiotools`:

```
# Activate the new virtual environment.
source /path/to/virtual/environment/bin/activate

# If necessary, upgrade pip and wheel or additional packages (such as setuptools if installing in editable mode).
pip install --upgrade pip setuptools wheel

# Clone the git repository
git clone https://github.com/dieterich-lab/pbiotools.git
cd pbiotools

# The period is required, it is the local project path (pbiotools)
pip --verbose install -r requirements.txt [-e] . 2>&1 | tee install.log

```

## Anaconda installation

The package can also be installed within an [anaconda](https://www.continuum.io/) environment.

```
# Create the anaconda environment.
conda create -n my_new_environment python=3.6 anaconda

# Activate the new environment.
source activate my_new_environment

# Clone the git repository
git clone https://github.com/dieterich-lab/pbiotools.git
cd pbiotools

pip --verbose install -r requirements.txt [-e] . 2>&1 | tee install.log
```

## Usage

There is currently limited documentation, see [docs](docs/bio.md).

## Uninstallation

To remove the `pbiotools` package if installed with pip:

```
pip uninstall pbiotools
```

To remove if installed with conda:

```
conda uninstall pbiotools
```

If the package is installed in a dedicated virtual environment, this environment can also be cleared or removed.

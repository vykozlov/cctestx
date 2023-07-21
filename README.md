cctestX
==============================

[![Build Status](https://jenkins.indigo-datacloud.eu/buildStatus/icon?job=Pipeline-as-code/DEEP-OC-org/cctestx/master)](https://jenkins.indigo-datacloud.eu/job/Pipeline-as-code/job/DEEP-OC-org/job/cctestx/job/master)

Cookiecutter test project for AI4OS / advanced branch

To launch it, first install the package then run [deepaas](https://github.com/indigo-dc/DEEPaaS):
```bash
git clone https://github.com/vykozlov/cctestx
cd cctestx
pip install -e .
deepaas-run --listen-ip 0.0.0.0
```
The associated Docker container for this module can be found in https://github.com/vykozlov/DEEP-OC-cctestx.

## Project structure
```
├── Jenkinsfile            <- Describes basic Jenkins CI/CD pipeline
├── LICENSE                <- License file
├── README.md              <- The top-level README for developers using this project
|
├── data
│   └── raw                <- The original, immutable data dump.
│
├── docs                   <- A default Sphinx project; see sphinx-doc.org for details
│
├── models                 <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks              <- Jupyter notebooks. Naming convention is a number (for ordering),
│                             the creator's initials (if many user development), 
│                             and a short `_` delimited description, e.g.
│                             `1.0-jqp-initial_data_exploration.ipynb`.
│
├── references             <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports                <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures            <- Generated graphics and figures to be used in reporting
|
├── tests                  <- Scripts to perfrom code testing
│
├── requirements.txt       <- The requirements file for reproducing the analysis environment, e.g.
│                             generated with `pip freeze > requirements.txt`
├── requirements-test.txt  <- The requirements file for the test environment
│
├── pyproject.toml         <- defines build system requirements of Python projects (e.g. pip install -e .)
|
├── cctestx    <- Source code for use in this project.
│   ├── __init__.py        <- Makes cctestx a Python (sub)package
│   │
│   ├── dataset            <- Scripts to download or generate data
│   │   └── make_dataset.py
│   │
│   ├── models             <- Scripts to train models and make predictions
│   │
│   ├── visualization      <- Scripts to create exploratory and results oriented visualizations
│   |   └── visualize.py
|   |
|   ├── config.py          <- Module to define CONSTANTS used across the AI-model python package
|   ├── predict.py         <- Module to describe inference pipeline
|   └── train.py           <- Module to describe training pipeline
│
├── tox.ini                <- tox file with settings for running tox; see tox.testrun.org
|
└── VERSION                <- file to define software version

```



## Testing

Testing process is automated by tox library. You can check the environments
configured to be tested by running `tox --listenvs`. If you are missing one
of the python environments configured to be tested (e.g. py310, py39) and
you are using `conda` for managing your virtual environments, consider using
`tox-conda` to automatically manage all python installation on your testing
virtual environment.

Tests are implemented following [pytest](https://docs.pytest.org) framework.
Fixtures and parametrization are placed inside `conftest.py` files meanwhile
assertion tests are located on `test_*.py` files.

The folder `tests/datasets` should contain minimalistic but representative
datasets to be used for testing. In a similar way, `tests/models` should
contain simple models for testing that can fit on your code repository.

After adding your dataset and models to the corresponding testing folders,
you should configure the corresponding fixtures on `tests/test_*/conftest.py`
with the names of your files. Additionally you can configure, add and
remove fixtures with required or optional parameters as needed by your
functions defined at the `api.__init__.py` module.

In case you do not have any checkpoint or model to test, you can use the
script `checkpoints_example.py` to generate a dummy model checkpoint that
can be used for testing purposes. The scripts consumes a file `train-dataset.npz`
from _DATA_PATH_ environment variable (default: `./data`) and generates a
checkpoint with the system timestamp at _MODELS_PATH_.

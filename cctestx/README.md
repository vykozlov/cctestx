cctestX
==============================

The structure here:

```
├── dataset            <- Subpackage to prepare a dataset or generate data
│   └── __init__.py    <- Main methods for public re-use, e.g. mkdata()
│
├── models             <- Subpackage to describe and create various AI models, build train and predict pipelines
│   └── __init__.py    <- Main methods for public re-use, e.g. create_model(), predict(), train()
|
├── visualization      <- Scripts for exploratory and results oriented visualizations
│   └── visualize.py
|
├── config.py          <- Module to define CONSTANTS used across the AI-model python package
└── __init__.py        <- Main methods for public re-use, e.g. imports mkdata(), predict(), train() (see above)

```
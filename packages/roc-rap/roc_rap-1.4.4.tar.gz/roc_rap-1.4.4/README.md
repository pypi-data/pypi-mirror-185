RAP PLUGIN README
=================

[![pipeline status](https://gitlab.obspm.fr/ROC/Pipelines/Plugins/RAP/badges/develop/pipeline.svg)](https://gitlab.obspm.fr/ROC/Pipelines/Plugins/RAP/pipelines)

This directory contains the source files of the Rpw dAta Processor (RAP), a plugin of the ROC pipelines dedicated to process RPW L0 data into L1.

RAP has been developed with the [POPPY framework](https://poppy-framework.readthedocs.io/en/latest/).

## Quickstart

### Installation with pip

To install the plugin using pip:

```
pip install roc-rap
```

NOTES:

    - It is also possible to install roc-rap from gitlab using the command `pip install roc-rap --extra-index-url https://__token__:<your_personal_token>@gitlab.obspm.fr/api/v4/projects/2052/packages/pypi/simple --trusted-host gitlab.obspm.fr`. A personnal access token is required to reach the package registry in the ROC Gitlab server.

### Installation from the repository

First, retrieve the `RAP` repository from the ROC gitlab server:

```
git clone https://gitlab.obspm.fr/ROC/Pipelines/Plugins/RAP.git
```

Then, install the package (here using (poetry)[https://python-poetry.org/]):

```
poetry install
```

NOTES:

    - It is also possible to clone the repository using SSH
    - To install poetry: `pip install poetry`
    - Default branch is `develop`

## Usage

The roc-rap plugin is designed to be run in a POPPy-built pipeline.
Nevertheless, it is still possible to import some classes and methods in Python files.

## Contacts

- xavier.bonnin@obspm.fr

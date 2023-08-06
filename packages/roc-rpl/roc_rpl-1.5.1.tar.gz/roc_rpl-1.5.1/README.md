RPL PLUGIN README
=================

[![pipeline status](https://gitlab.obspm.fr/ROC/Pipelines/Plugins/RPL/badges/develop/pipeline.svg)](https://gitlab.obspm.fr/ROC/Pipelines/Plugins/RPL/pipelines)

This directory contains the source files of the RPW Packet parsing Library (RPL), a plugin of the ROC pipelines dedicated to parse the RPW telemetry/command packets.

RPL has been developed with the [POPPY framework](https://poppy-framework.readthedocs.io/en/latest/).

## Quickstart

### Installation with pip

To install the plugin using pip:

```
pip install roc-rpl
```

NOTES:

    - It is also possible to install plugin from gitlab: `pip install roc-rpl --extra-index-url https://__token__:<your_personal_token>@gitlab.obspm.fr/api/v4/projects/2052/packages/pypi/simple --trusted-host gitlab.obspm.fr`. A personal access token is required to reach the package registry in the ROC Gitlab server.

### Installation from the repository

First, retrieve the `RPL` repository from the ROC gitlab server:

```
git clone https://gitlab.obspm.fr/ROC/Pipelines/Plugins/RPL.git
```

Then, install the package (here using (poetry)[https://python-poetry.org/]):

```
poetry install --extras "poppy"
```

NOTES:

    - It is also possible to clone the repositiory using SSH
    - To install poetry: `pip install poetry`
    - Default branch is `develop`

## Usage

The roc-rpl plugin is designed to be run in a POPPy-built pipeline.
Nevertheless, it is still possible to import some classes and methods in Python files.

For instance, to test that the installation has ended correctly, run:

```
python -c "from roc.rpl import packet_structure"
```

No message should be returned if the import works well.

## Authors

* Xavier BONNIN xavier.bonnin@obspm.fr (maintainer)
* Manuel DUARTE manuel.duarte@obspm.fr (author)
* Sonny LION sonny.lion@obspm.fr (author)

License
-------

This project is licensed under CeCILL-C.

Acknowledgments
---------------

* Solar Orbiter / RPW Operation Centre (ROC) team

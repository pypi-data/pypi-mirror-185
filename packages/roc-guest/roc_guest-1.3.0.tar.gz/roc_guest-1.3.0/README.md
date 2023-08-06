GUEST PLUGIN README
===================

The RPW Gse data ReqUESTer (GUEST) is a plugin used to handle data from GSE for RPW/Solar Orbiter (MEB GSE, ADS GSE).

GUEST is designed to be run in an instance of the ROC Ground Test SGSE (RGTS).

GUEST is developed with and run under the POPPY framework.

## Quickstart

### Installation with pip

To install the plugin using pip:

```
pip install roc-guest
```

### Installation from the repository (restricted access)

First, retrieve the `GUEST` repository from the ROC gitlab server:

```
git clone https://gitlab.obspm.fr/ROC/Pipelines/Plugins/GUEST.git
```

Then, install the package (here using (poetry)[https://python-poetry.org/]):

```
poetry install"
```

NOTES:

    - It is also possible to clone the repository using SSH
    - To install poetry: `pip install poetry`

## Usage

The roc-guest plugin is designed to be run in a POPPy-built pipeline.
Nevertheless, it is still possible to import some classes and methods in Python files.

## CONTACT

* roc dot support at sympa dot obspm dot fr

## License


This project is licensed under CeCILL-C.

## Acknowledgments

Solar Orbiter / RPW Operation Centre (ROC) team

# ROC IDB

A plugin to manage different IDB source/version for RPW/Solar Orbiter.

## User guide

### Pre-requisites

The following software must be installed:
- Python 3.8
- pip tool
- poetry (optional)
- git (optional)

### Install a stable release with pip

To install the roc-idb plugin with pip:

``pip install roc-idb``

## Nominal usage

roc-idb is designed to be called from a pipeline running with the POPPy framework.

The plugin can be used in Python programs using "import roc.idb".

## Developer guide

### Install a local copy from source files

To install a local copy of the roc-idb plugin:

1. Retrieve a copy of the source files from https://gitlab.obspm.fr/ROC/Pipelines/Plugins/IDB (restricted access)
2. Use `pip install` or `poetry install` command to install local instance

### Publish a new tag on Gitlab

1. Update the version using ``poetry version <bump_level>`` where <bump_level> can be patch, minor or major
2. Update the descriptor using ``poetry run python bump_descriptor.py``
3. Generate the new setup file using ``poetry run dephell deps convert``
4. Apply code formatters using ``poetry run pre-commit run -a``
5. Commit and tag

Authors
-------

* Xavier BONNIN xavier.bonnin@obspm.fr (maintainer)
* Sonny LION sonny.lion@obspm.fr (author)

License
-------

This project is licensed under CeCILL-C.

Acknowledgments
---------------

* Solar Orbiter / RPW Operation Centre (ROC) team

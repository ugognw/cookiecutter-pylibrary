Changelog
#########

All notable changes to this project will be documented in this file.

The format is based on `Keep a Changelog <https://keepachangelog.com/en/1.0.0/>`_,
and this project adheres to `Semantic Versioning <https://semver.org/spec/v2.0.0.html>`_.

`Unreleased`_

Added
~~~~~

* Coveralls integration for GitLab or GitHub
* Default GitHub actions and GitLab pipelines for changelog generation
* Optional markdown docs with Sphinx
* Organized development dependencies in `pyproject.toml`
* Optional development dependencies for testing, VCS control, and documentation

Changed
~~~~~~~

* setuptools -> Poetry for packagement management and building
* Transition from `setup.py` to `pyproject.toml`
* Tox -> Nox for managing test environments
* Replace pylint with Mypy for type-checking

Removed
~~~~~~~

* C-extension support
* Optional tests inside of packagement
* Optional coverage testing separate from tests
* Support for hosting domains other than `github.com` and `gitlab.com`

`0.0.1`_ (2023-06-24)
------------------

Added
~~~~~

* Forked from `ionelmc's version <https://github.com/ionelmc/cookiecutter-pylibrary>`_.

.. _Unreleased: https://github.com/ugognw/cookiecutter-pylibrary/tree/main
.. _`0.0.1`: https://github.com/ugognw/cookiecutter-pylibrary/tree/main

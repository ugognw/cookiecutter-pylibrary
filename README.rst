======================
cookiecutter-pylibrary
======================

Cookiecutter_ template for a Python library.

*Notes*:

* This is largely designed to address this `blog post about packaging python
  libraries <https://blog.ionelmc.ro/2014/05/25/python-packaging/>`_.

  * ... and it will save you from `packaging pitfalls
    <https://blog.ionelmc.ro/2014/06/25/python-packaging-pitfalls/>`_.
* There's a bare library using this template (if you're curious about the final
  result): https://github.com/ionelmc/python-nameless.
* If you have a web application (not a library) you might want to take a look at
  `django-docker <https://github.com/evozon/django-docker>`_.

.. contents:: Table of Contents

Features
--------

This is an "all inclusive" sort of template.

* Choice of various licenses.
* src/package directory structure
* tests outside of package
* nox_ for managing test environments for PyPy-3.10, Python 3.10, and 3.11
* Pytest_for testing Python 3.10 and 3.11
* *Optional* support for creating a tests matrix out of dependencies and python versions.
* Codacy_, CodeClimate_, Coveralls_ or Codecov_ for coverage tracking (using Tox_).
* Documentation with Sphinx_, ready for ReadTheDocs_.
* Ruff_ for static checks (so much faster than Flake8_!)
* Mypy_ for dynamic checks not covered by Ruff_
* Virtual environment management and package building/publishing with Poetry_ (with the option to install Poetry)
* CI/CD configuration for testing and building with GitHub Actions or GitLab CI/CD
* GitHub actions:
  - testing code functionality
  - testing documentation builds, links, docstrings
  - checking license compatability (using `pip-licenses`)
  - publishing tagged versions to PyPI (you must store a PyPI token as a secret in order for this to work)
* Configurations for:

  * bumpversion_ (bump2version_ required)
  * gitchangelog_
  * Pytest_
  * Mypy_
  * pre-commit_
  * black_
  * coverage_
  * Ruff_

Requirements
------------

Projects using this template have the following minimal dependencies:

* Poetry_ - for managing the virtual environment and building and publishing the package
* Click_ or Argparse_ - for the command-line interface

The following dependencies belong to optional dependency groups and may be removed during configuration via your responses to the `cookiecutter` prompts. The dependencies are grouped in the `pyproject.toml` by use:

dev
~~~

* Black_ - for code formating
* Ruff_ - for static checks (including those made by Isort_, Flake8_, Bandit_, Pyupgrade_, and Autoflake_)
* Pylint_ - for dynamic checks
* Cookiecutter_ - just for creating the project

test
~~~~

* Coverage_ - for code coverage analysis
* Pytest_ - for testing
  * with optional extensions `pytest-cov`, `pytest-datadir`, and `pytest-xdist`
* Tox_ - for running the tests in isolated environments

vcs
~~~

* Pre-commit_ - for running pre-commit git hooks (optional)
* bump2version_ - for updating version strings within the package (optional)
* gitchangelog_ - for auto-populating changelogs (optional)

docs
~~~~

* Sphinx_ - for building documentation
* sphinx-rtd-theme_, python-docs-theme_, sphinx-py3doc-enhanced-theme_, sphinx-book-theme_, furo_, or pydata-sphinx-theme_ - for documentation theming

Note that `poetry install` will not install the above dependencies. In order to install a particular group of dependencies along with the package, you must run::
  $ poetry install --with=<group>[,<group>]

where `<group>` is one of `dev`, `test`, `vcs`, or `docs`.

To get quickly started on a new system, just `install pip
<https://pip.pypa.io/en/latest/installing.html>`_. That's the bare minimum to required install Tox_ and Cookiecutter_. To install
them, just run this in your shell or command prompt::

  pip install tox cookiecutter

Usage and options
-----------------

This template is more involved than the regular `cookiecutter-pypackage
<https://github.com/audreyr/cookiecutter-pypackage>`_.

First generate your project::

  cookiecutter gh:ugognw/cookiecutter-pylibrary

You will be asked for these fields:

.. note:: Fields that work together usually use the same prefix. If you answer "no" on the first one then the rest
   won't have any effect so just ignore them. Maybe in the future cookiecutter will allow option hiding or something
   like a wizard.

.. list-table::
    :header-rows: 1

    * - Field
      - Default
      - Description

    * - ``full_name``
      - .. code:: python

            "Ugochukwu Nwosu"
      - Main author of this library or application (used in ``AUTHORS.rst`` and ``pyproject.toml``).

        Can be set in your ``~/.cookiecutterrc`` config file.

    * - ``email``
      - .. code:: python

            "ugognw@gmail.com"
      - Contact email of the author (used in ``AUTHORS.rst`` and ``pyproject.toml``).

        Can be set in your ``~/.cookiecutterrc`` config file.

    * - ``website``
      - .. code:: python

            "https://www.law-two.com"
      - Website of the author (used in ``AUTHORS.rst``).

        Can be set in your ``~/.cookiecutterrc`` config file.

    * - ``repo_username``
      - .. code:: python

            "ugognw"
      - GitHub user name of this project (used for GitHub link).

        Can be set in your ``~/.cookiecutterrc`` config file.

    * - ``project_name``
      - .. code:: python

            "Nameless"
      - Verbose project name, used in headings (docs, readme, etc).

    * - ``repo_hosting_domain``
      - .. code:: python

            "github.com"
      - Use ``"no"`` for no hosting (various links will disappear). You can also use ``"gitlab.com"``. If you desire CI/CD configuration, this should be consistent with the values for `github_actions` and `gitlab_ci_cd`.

    * - ``repo_name``
      - .. code:: python

            "python-nameless"
      - Repository name on GitHub (and project's root directory name).

    * - ``package_name``
      - .. code:: python

            "nameless"
      - Python package name (whatever you would import via a Python `import` statement).

    * - ``distribution_name``
      - .. code:: python

            "nameless"
      - PyPI distribution name (what you would ``pip install``).

    * - ``project_short_description``
      - .. code:: python

            "An example package [...]"
      - One line description of the project (used in ``README.rst`` and ``pyproject.toml``).

    * - ``release_date``
      - .. code:: python

            "today"
      - Release date of the project (ISO 8601 format) default to today (used in ``CHANGELOG.rst``).

    * - ``year``
      - .. code:: python

            "now"
      - Copyright year (used in Sphinx ``conf.py``).

    * - ``version``
      - .. code:: python

            "0.0.1"
      - Release version (see ``.bumpversion.cfg`` and in Sphinx ``conf.py``).

    * - ``test_matrix_separate_coverage``
      - .. code:: python

            "no"
      - Enable this to have a separate env for measuring coverage. Indicated if you want to run doctests or collect tests
        from ``src`` with pytest.
    * - ``setup_py_uses_setuptools_scm``
      - .. code:: python

            "no"
      - Enables the use of `setuptools-scm <https://pypi.org/project/setuptools-scm/>`_. You can continue using
        bumpversion_ with this enabled.
    * - ``command_line_interface``
      - .. code:: python

            "plain"
      - Option to enable a CLI (a bin/executable file). Available options:

        * ``plain`` - a very simple command.
        * ``argparse`` - a command implemented with ``argparse``.
        * ``click`` - a command implemented with `click <http://click.pocoo.org/>`_ - which you can use to build more complex commands.
        * ``no`` - no CLI at all.

    * - ``command_line_interface_bin_name``
      - .. code:: python

            "nameless"
      - Name of the CLI bin/executable file (set the console script name in ``pyproject.toml``).

    * - ``license``
      - .. code:: python

            "BSD license"
      - License to use. Available options:

        * BSD license
        * MIT license
        * ISC license
        * Apache Software License 2.0

        What license to pick? https://choosealicense.com/

    * - ``coveralls``
      - .. code:: python

            "yes"
      - Enable pushing coverage data to Coveralls_ and add badge in ``README.rst``.

    * - ``codecov``
      - .. code:: python

            "yes"
      - Enable pushing coverage data to Codecov_ and add badge in ``README.rst``.

        **Note:** Doesn't support pushing C extension coverage yet.

    * - ``codacy``
      - .. code:: python

            "yes"
      - Enable Codacy_ in your chosen CI/CD pipeline and add a corresponding badge in ``README.rst``.

        **Note:** After importing the project in Codacy, find the hexadecimal project ID from settings and replace it in badge URL

    * - ``codeclimate``
      - .. code:: python

            "yes"
      - Enable the Velocity GitHub Action by CodeClimate_ and a corresponding badge in ``README.rst``. **Note:** This will not be implemented if you select "gitlab.com"" as your repo hosting domain. Further, you will have to set the `VELOCITY_DEPLOYMENT_TOKEN` as a secret on your repo hosting site in order for CI/CD integration to work correctly.

    * - ``sphinx_docs``
      - .. code:: python

            "yes"
      - Have Sphinx documentation.

    * - ``sphinx_theme``
      - .. code:: python

            "sphinx-rtd-theme"
      - What Sphinx_ theme to use.

        Suggested alternative: `sphinx-py3doc-enhanced-theme <https://pypi.org/project/sphinx_py3doc_enhanced_theme>`__
        for a responsive theme based on the Python 3 documentation.

    * - ``sphinx_doctest``
      - .. code:: python

            "no"
      - Set to ``"yes"`` if you want to enable doctesting in the `docs` environment. Works best with
        ``test_matrix_separate_coverage == 'no'``.

        Read more about `doctest support in Sphinx <http://www.sphinx-doc.org/en/stable/ext/doctest.html>`_.

    * - ``sphinx_docs_hosting``
      - .. code:: python

            "repo_name.readthedocs.io"
      - Leave as default if your documentation will be hosted on readthedocs.
        If your documentation will be hosted elsewhere (such as GitHub Pages or GitLab Pages),
        enter the top-level URL.

    * - ``pypi_badge``
      - .. code:: python

            "yes"
      - By default, this will insert links to your project's page on PyPI.org.
        Note that if your package is not (yet) on PyPI, this will cause tox -e docs to fail.
        If you choose "no", then these links will not be created.

    * - ``pypi_disable_upload``
      - .. code:: python

            "no"
      - If you specifically want to be sure your package will never be
        accidentally uploaded to PyPI, you can pick "yes".

Developing the project
``````````````````````

To run all the tests, just run::

  tox

To see all the tox environments::

  tox -l

To only build the docs::

  tox -e docs

To build and verify that the built package is proper and other code QA checks::

  tox -e check

Releasing the project
`````````````````````
Before releasing your package on PyPI you should have all the tox environments passing.

Version management
''''''''''''''''''

This template provides a basic bumpversion_ configuration. It's as simple as running:

* ``bumpversion patch`` to increase version from `1.0.0` to `1.0.1`.
* ``bumpversion minor`` to increase version from `1.0.0` to `1.1.0`.
* ``bumpversion major`` to increase version from `1.0.0` to `2.0.0`.

You should read `Semantic Versioning 2.0.0 <http://semver.org/>`_ before bumping versions.

Building and uploading
''''''''''''''''''''''

Before building dists make sure you got a clean build area::

    rm -rf build
    rm -rf src/*.egg-info

Note:

    Dirty ``build`` or ``egg-info`` dirs can cause problems: missing or stale files in the resulting dist or
    strange and confusing errors. Avoid having them around.

Then you should check that you got no packaging issues::

    tox -e check

And then you can build the ``sdist``, and if possible, the ``bdist_wheel`` too::

    python setup.py clean --all sdist bdist_wheel

To make a release of the project on PyPI, assuming you got some distributions in ``dist/``, the most simple usage is::

    twine upload --skip-existing dist/*.whl dist/*.gz dist/*.zip

In ZSH you can use this to upload everything in ``dist/`` that ain't a linux-specific wheel (you may need ``setopt extended_glob``)::

    twine upload --skip-existing dist/*.(whl|gz|zip)~dist/*linux*.whl

For making and uploading `manylinux1 <https://github.com/pypa/manylinux>`_ wheels you can use this contraption::

    docker run --rm -itv $(pwd):/code quay.io/pypa/manylinux1_x86_64 bash -c 'set -eux; cd code; rm -rf wheelhouse; for variant in /opt/python/*; do rm -rf dist build *.egg-info && $variant/bin/python setup.py clean --all bdist_wheel; auditwheel repair dist/*.whl; done; rm -rf dist build *.egg-info'
    twine upload --skip-existing wheelhouse/*.whl
    docker run --rm -itv $(pwd):/code quay.io/pypa/manylinux1_i686 bash -c 'set -eux; cd code; rm -rf wheelhouse; for variant in /opt/python/*; do rm -rf dist build *.egg-info && $variant/bin/python setup.py clean --all bdist_wheel; auditwheel repair dist/*.whl; done; rm -rf dist build *.egg-info'
    twine upload --skip-existing wheelhouse/*.whl

Note:

    `twine <https://pypi.org/project/twine>`_ is a tool that you can use to securely upload your releases to PyPI.
    You can still use the old ``python setup.py register sdist bdist_wheel upload`` but it's not very secure - your PyPI
    password will be sent over plaintext.

Changelog
---------

See `CHANGELOG.rst <https://github.com/ionelmc/cookiecutter-pylibrary/blob/master/CHANGELOG.rst>`_.

Questions & answers
-------------------

There's no Makefile?

  Sorry, no ``Makefile`` yet. The Tox_ environments stand for whatever you'd have in a ``Makefile``.

Why does ``tox.ini`` have a ``passenv = *``?

  Tox 2.0 changes the way it runs subprocesses - it no longer passes all the environment variables by default. This causes
  all sorts of problems if you want to run/use any of these with Tox: SSH Agents, Browsers (for Selenium), Appengine SDK,
  VC Compiler and so on.

  `cookiecutter-pylibrary` errs on the side of convenience here. You can always remove ``passenv = *`` if you like
  the strictness.

Why is the version stored in several files (``pkg/__init__.py``, ``pyproject.toml``, ``docs/conf.py``)?

  We cannot use a metadata/version file [#]_ because this template is to be used with both distributions of packages (dirs
  with ``__init__.py``) and modules (simple ``.py`` files that go straight in ``site-packages``). There's no good place
  for that extra file if you're distributing modules.

  But this isn't so bad - bumpversion_ manages the version string quite
  neatly.

.. [#] Example, an ``__about__.py`` file.

Not Exactly What You Want?
--------------------------

No way, this is the best. :stuck_out_tongue_winking_eye:


If you have criticism or suggestions please open up an Issue or Pull Request.

.. _Tox: https://tox.wiki/
.. _Sphinx: http://sphinx-doc.org/
.. _Coveralls: https://coveralls.io/
.. _ReadTheDocs: https://readthedocs.org/
.. _Pytest: http://pytest.org/
.. _Pylint: https://pylint.readthedocs.io/en/latest/
.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _bumpversion: https://pypi.org/project/bump2version
.. _bump2version: https://github.com/c4urself/bump2version
.. _Codecov: http://codecov.io/
.. _Codacy: https://codacy.com/
.. _CodeClimate: https://codeclimate.com/
.. _Poetry: https://python-poetry.org
.. _gitchangelog: https://github.com/vaab/gitchangelog
.. _pre-commit: https://pre-commit.com
.. _Ruff: https://beta.ruff.rs/docs/

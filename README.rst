======================
cookiecutter-pylibrary
======================

Cookiecutter_ template for a Python library.

*Notes*:

* This is largely designed to address this `blog post about packaging python
  libraries <https://blog.ionelmc.ro/2014/05/25/python-packaging/>`_.
  * ... and it will save you from `packaging pitfalls
    <https://blog.ionelmc.ro/2014/06/25/python-packaging-pitfalls/>`_.
* Although this cookiecutter is based off of that of `ionelmc <https://github.com/ionelmc/cookiecutter-pylibrary>`_, it also takes inspiration from `python-blueprint <https://github.com/johnthagen/python-blueprint/tree/main>`_ and `cookiecutter-hypermodern-python <https://github.com/cjolowicz/cookiecutter-hypermodern-python/tree/main>`_

* There's a bare library using this template (if you're curious about the final
  result): https://github.com/ugognw/python-nameless.
* If you have a web application (not a library) you might want to take a look at
  `django-docker <https://github.com/evozon/django-docker>`_.

.. contents:: Table of Contents

Features
--------

This is an "all inclusive" sort of template.

* Choice of various licenses.
* Configuration to match your choice of hosting on GitHub or GitLab
* `src/package_name` directory structure
* tests outside of package
* Nox_ and nox-poetry_ for managing test environments for PyPy-3.10, Python 3.10, and 3.11
* pytest_ for testing (with `Coverage.py`_ for coverage analysis)
* Automated dependency updates with Dependabot_ (if hosting with GitHub)
* Documentation with Sphinx_, ready for ReadTheDocs_.
* Black_ - for code formating
* Ruff_ for static checks and import sorting
* mypy_ for type-checks to supplement Ruff_
* pre-commit_ - for running pre-commit git hooks (optional)
* Coveralls_, Codecov_ Codacy_, and/or `Code Climate`_ integration for coverage tracking
* Virtual environment management and package building/publishing with Poetry_
* CI/CD configuration for testing and building with GitHub Actions or GitLab CI/CD
  - testing code functionality
  - testing documentation builds, links, docstrings
  - checking license compatability (using pip-licenses_) whenever the `pyproject.toml` is changed
  - publishing tagged versions to PyPI (you must store a PyPI token as a secret in order for this to work)
* Version managing with bump2version_
* *Optional* support for testing across different platforms
* *Optional* command-line interface via argparse_, click_, `Python Fire`_, or Typer_
* Configurations for:
  * bumpversion_ (bump2version_ required)
  * gitchangelog_
  * pytest_
  * mypy_
  * pre-commit_
  * Black_
  * coverage_
  * Ruff_

Requirements
------------

Projects using this template have the following minimal dependencies:

* Poetry_
* click_, `Python Fire`_, or Typer_
* nox_ and nox-poetry_

To get quickly started on a new system, just `install pip
<https://pip.pypa.io/en/latest/installing.html>`_. That's the bare minimum to required install Cookiecutter_. To install
, just run this in your shell or command prompt::

  pip install cookiecutter

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

    * - ``project_name``
      - .. code:: python

            "Nameless"
      - Verbose project name, used in headings (docs, readme, etc).

    * - ``project_short_description``
      - .. code:: python

            "An example package [...]"
      - One line description of the project (used in ``README.rst`` and ``pyproject.toml``).

    * - ``package_name``
      - .. code:: python

            "nameless"
      - Python package name (whatever you would import via a Python `import` statement).

    * - ``distribution_name``
      - .. code:: python

            "nameless"
      - PyPI distribution name (what you would ``pip install``).

    * - ``repo_name``
      - .. code:: python

            "python-nameless"
      - Repository name on GitHub or GitLab (and project's root directory name).

    * - ``repo_hosting``
      - .. code:: python

            "github.com"
      - You can also use ``"gitlab.com"``. If you desire CI/CD configuration, this should be consistent with the values for `github_actions` and `gitlab_ci_cd`.

    * - ``repo_username``
      - .. code:: python

            "ugognw"
      - GitHub or GitLab user name of this project (used for GitHub/GitLab link).

        Can be set in your ``~/.cookiecutterrc`` config file.
    
    * - ``repo_main_branch``
      - .. code:: python
            "main"
      - The name of the default branch for this project.

    * - ``release_date``
      - .. code:: python

            "today"
      - Release date of the project (ISO 8601 format) default to today (used in ``CHANGELOG.rst``).

    * - ``year_from``
      - .. code:: python

            "now"
      - Copyright start year (used in Sphinx ``conf.py``).

    * - ``year_to``
      - .. code:: python

            "now"
      - Copyright end year (used in Sphinx ``conf.py``).

    * - ``keywords``
      - .. code:: python

            "now"
      - List of comma-separated keywords to use in `pyproject.toml` (e.g., `physics,math,chemistry`).

    * - ``version``
      - .. code:: python

            "0.0.1"
      - Release version (see ``.bumpversion.cfg`` and in Sphinx ``conf.py``).

    * - ``license``
      - .. code:: python

            "BSD license"
      - License to use. Available options:

        * BSD license
        * MIT license
        * ISC license
        * Apache Software License 2.0

        What license to pick? https://choosealicense.com/

    * - ``command_line_interface``
      - .. code:: python

            "plain"
      - Option to enable a CLI (a bin/executable file). Available options:

        * ``plain`` - a very simple command.
        * ``argparse`` - a command implemented with argparse_.
        * ``fire`` - a command implemented with `Python Fire`_.
        * ``typer`` - a command implemented with Typer_.
        * ``click`` - a command implemented with click_ - which you can use to build more complex commands.
        * ``no`` - no CLI at all.

    * - ``command_line_interface_bin_name``
      - .. code:: python

            "nameless"
      - Name of the CLI bin/executable file (verify that the console script name in ``pyproject.toml`` matches your desired implementation; see `here <https://python-poetry.org/docs/pyproject/#scripts>`_).

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

    * - ``coveralls``
      - .. code:: python

            "yes"
      - Enable pushing coverage data to Coveralls_ and add badge in ``README.rst``. Don't forget to add your repo on `https://coveralls.io <https://coveralls.io>`_!

    * - ``codecov``
      - .. code:: python

            "yes"
      - Enable pushing coverage data to Codecov_ and add badge in ``README.rst``. Don't forget to add your repo on `https://about.codecov.io <https://about.codecov.io>`_!

    * - ``codacy``
      - .. code:: python

            "yes"
      - Enable Codacy_ in your chosen CI/CD pipeline and add a corresponding badge in ``README.rst``. Don't forget to import your project on `https://www.codacy.com <https://www.codacy.com>`_! 

        **Note:** Displaying the Codacy badge is contingent on your project ID. If you don't input your project ID during the cookiecutter configuration step, you can still fill in your hexadecimal project ID in the badge URL in the `README.rst`.

    * - ``codacy_projectid``
      - .. code:: python

            "[Get ID from https://app.codacy.com/gh/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}/settings]"
      - Your Codacy_ hexadecimal project ID.

    * - ``codeclimate``
      - .. code:: python

            "yes"
      - Enable the Velocity GitHub Action by `Code Climate`_ and a corresponding badge in ``README.rst``. **Note:** This will not be implemented if you select "gitlab.com"" as your repo hosting domain. Further, you will have to set the `VELOCITY_DEPLOYMENT_TOKEN` as a secret on your repo hosting site in order for CI/CD integration to work correctly.

    * - ``gitchangelog``
      - .. code:: python

            "yes"
      - Whether or not to include gitchangelog_ as a dependency.

    * - ``github_actions``
      - .. code:: python

            "yes"
      - Whether or not to use GitHub Actions as your CI/CD framework.

    * - ``gitlab_ci_cd``
      - .. code:: python

            "yes"
      - Whether or not to use GitLab CI/CD as your CI/CD framework.

    * - ``test_on_osx``
      - .. code:: python

            "yes"
      - Whether or not to test your package on OSX in addition to Linux in CI/CD.

    * - ``test_on_windows``
      - .. code:: python

            "yes"
      - Whether or not to test your package on Windows in addition to Linux in CI/CD.

    * - ``pre_commit``
      - .. code:: python

            "yes"
      - Whether or not to enable pre-commit_.

    * - ``install_precommit_hooks``
      - .. code:: python

            "yes"
      - Whether or not to install pre-commit_ hooks. Requires that a .git repository exists in the current working directory.

    * - ``pytest_datadir``
      - .. code:: python

            "yes"
      - Whether or not to install pytest-datadir_ as a testing dependency.

    * - ``pytest_xdist``
      - .. code:: python

            "yes"
      - Whether or not to install pytest-xdist_ as a testing dependency.

    * - ``sphinx_docs``
      - .. code:: python

            "yes"
      - Have Sphinx documentation.

    * - ``sphinx_theme``
      - .. code:: python

            "furo"
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

    * - ``initialize_git_repository``
      - .. code:: python

            "yes"
      - Whether or not to initialize a Git repository using `git init`.

    * - ``install_package``
      - .. code:: python

            "yes"
      - Whether or not to include install the newly created package via Poetry_. If a virtual environment is not already active, this will create a new virtual environment in which to install the current package.

    * - ``activate_virtual_environment``
      - .. code:: python

            "yes"
      - Whether or not to include activate the virtual environment and install package upon project creation.

Developing the project
``````````````````````

To run all the tests, just run::

  nox

To see all the tox environments::

  nox -l

To only build the docs::

  nox -e docs

To build and verify that the built package is proper and other code QA checks::

  nox -e format,lint

Releasing the project
`````````````````````
Before releasing your package on PyPI you should have all the nox environments passing.

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

    nox -e format

And then you can build the ``sdist``, and if possible, the ``bdist_wheel`` too::

    poetry build

To make a release of the project on PyPI, assuming you got some distributions in ``dist/``, the most simple usage is::

    poetry build

You should set your PyPI credentials according to `here <https://python-poetry.org/docs/repositories/#configuring-credentials>`_.

Changelog
---------

See `CHANGELOG.rst <https://github.com/ionelmc/cookiecutter-pylibrary/blob/master/CHANGELOG.rst>`_.

FAQs
-------------------

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

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _Nox: https://nox.thea.codes/en/stable/
.. _nox-poetry: https://nox-poetry.readthedocs.io/
.. _pytest: http://pytest.org/
.. _Dependabot: https://github.com/dependabot/dependabot-core
.. _Sphinx: http://sphinx-doc.org/
.. _ReadTheDocs: https://readthedocs.org/
.. _Black: https://black.readthedocs.io/
.. _Ruff: https://beta.ruff.rs/docs/
.. _mypy: https://mypy.readthedocs.io/
.. _pre-commit: https://pre-commit.com
.. _Coverage: https://coverage.readthedocs.io/
.. _Coveralls: https://coveralls.io/
.. _Codecov: http://codecov.io/
.. _Codacy: https://codacy.com/
.. _CodeClimate: https://codeclimate.com/
.. _Poetry: https://python-poetry.org
.. _pip-licenses: https://github.com/raimon49/pip-licenses
.. _bumpversion: https://pypi.org/project/bump2version
.. _bump2version: https://github.com/c4urself/bump2version
.. _argparse: https://docs.python.org/3/library/argparse.html
.. _click: http://click.pocoo.org/
.. _`Python Fire`: https://github.com/google/python-fire
.. _Typer: https://typer.tiangolo.com
.. _gitchangelog: https://github.com/vaab/gitchangelog

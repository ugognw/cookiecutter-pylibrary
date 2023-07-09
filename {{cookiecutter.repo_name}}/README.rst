========
Overview
========
.. start-badges

.. list-table::
    :stub-columns: 1
{% if cookiecutter.sphinx_docs == "yes" %}
    * - code
      - |black| |mypy| |ruff|
    * - docs
      - |docs|
{%- endif %}
    * - tests
      - |
      {%- if cookiecutter.github_actions == 'yes' %} |github-actions|
      {%- elif cookiecutter.gitlab_ci_cd == 'yes' %} |gitlab-ci/cd|
      {%- endif -%}
        {{ '' }}
        | {%- if cookiecutter.coveralls == 'yes' %} |coveralls|{% endif -%}
          {%- if cookiecutter.codecov == 'yes' %} |codecov|{% endif -%}
        {{ '' }}
        {%- if cookiecutter.codacy == 'yes' or cookiecutter.codeclimate == 'yes' %}
        | {%- if cookiecutter.codacy == 'yes' and cookiecutter.repo_hosting == 'github.com' %} |codacy|{% endif -%}
          {%- if cookiecutter.codeclimate == 'yes' %} |codeclimate|{% endif -%}
        {%- endif -%}
{{ '' }}
{%- if cookiecutter.pypi_badge == "yes" or cookiecutter.repo_hosting_domain == "github.com" %}
    * - package
      - | |poetry| {% if cookiecutter.pypi_badge == "yes" %} |version| |wheel| |supported-versions| |supported-implementations|
        {{ '' }}{% endif %}
        {%- if cookiecutter.repo_hosting_domain == "github.com" %}| |commits-since|{% endif %}
{%- endif %}
{{ '' }}
.. |black| image:: https://img.shields.io/badge/%20style-black-000000.svg
    :target: https://github.com/psf/black
    :alt: Black
.. |mypy| image:: https://www.mypy-lang.org/static/mypy_badge.svg
    :target: https://mypy-lang.org/
    :alt: Mypy
.. |ruff| image:: https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v2.json
    :target: https://github.com/astral-sh/ruff
    :alt: Ruff
{%- if cookiecutter.sphinx_docs == "yes" -%}
{%- if 'readthedocs' in cookiecutter.sphinx_docs_hosting -%}
.. |docs| image:: https://readthedocs.org/projects/{{ cookiecutter.repo_name }}/badge/?style=flat
    :target: https://{{ cookiecutter.repo_name|replace('.', '') }}.readthedocs.io/
    :alt: Documentation Status
{%- elif 'gitlab' in cookiecutter.sphinx_docs_hosting and 'gitlab' in cookiecutter.repo_hosting_domain -%}
.. |docs| image:: {{ cookiecutter.__repo_url }}/badges/{{ cookiecutter.repo_main_branch }}/pipeline.svg
    :target: {{ cookiecutter.__repo_url }}/commits/{{ cookiecutter.repo_main_branch }}
    :alt: Documentation Status
{% endif %}
{% endif %}
{%- if cookiecutter.github_actions == 'yes' %}
.. |github-actions| image:: {{ cookiecutter.__repo_url }}/actions/workflows/github-actions.yml/badge.svg
    :alt: GitHub Actions Build Status
    :target: {{ cookiecutter.__repo_url }}/actions
{%- elif cookiecutter.gitlab_ci_cd == 'yes' %}
.. |gitlab-ci/cd| image:: https://gitlab.com/%{project_path}/badges/%{default_branch}/pipeline.svg
    :alt: GitLab CI/CD Pipeline Status
    :target: https://gitlab.com/%{project_path}/-/commits/%{default_branch}
{% endif %}
{%- if cookiecutter.coveralls == 'yes'%}
.. |coveralls| image:: https://coveralls.io/repos/{{ cookiecutter.repo_hosting | trim('.com') }}/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}/badge.svg?branch={{ cookiecutter.repo_main_branch }}
    :alt: Coverage Status
    :target: https://coveralls.io/{{ cookiecutter.repo_hosting | trim('.com') }}/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}?branch={{ cookiecutter.repo_main_branch }}
{% endif %}
{%- if cookiecutter.codecov == 'yes' %}
{%- if cookiecutter.repo_hosting == 'github.com' %}
{% set repo_abbrev = 'gh' %}
{%- elif cookiecutter.repo_hosting == 'gitlab.com'  %}
{% set repo_abbrev = 'gl' %}
{%- endif %}
.. |codecov| image:: https://codecov.io/{{ repo_abbrev }}/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}/branch/{{ cookiecutter.repo_main_branch }}/graphs/badge.svg?branch={{ cookiecutter.repo_main_branch }}
    :alt: Coverage Status
    :target: https://app.codecov.io/{{ cookiecutter.repo_hosting | trim('.com') }}/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}
{% endif %}
{%- if cookiecutter.codacy == 'yes' and cookiecutter.repo_hosting == 'github.com' %}
.. |codacy| image:: https://img.shields.io/codacy/grade/{{ cookiecutter.codacy_projectid }}.svg
    :target: https://www.codacy.com/app/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}
    :alt: Codacy Code Quality Status
{% endif %}
{%- if cookiecutter.codeclimate == 'yes' %}
.. |codeclimate| image:: https://codeclimate.com/github/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}/badges/gpa.svg
   :target: https://codeclimate.com/github/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}
   :alt: CodeClimate Quality Status
{% endif %}
{%- if cookiecutter.pypi_badge == "yes" %}
.. |version| image:: https://img.shields.io/pypi/v/{{ cookiecutter.distribution_name }}.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/{{ cookiecutter.distribution_name }}

.. |wheel| image:: https://img.shields.io/pypi/wheel/{{ cookiecutter.distribution_name }}.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/{{ cookiecutter.distribution_name }}

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/{{ cookiecutter.distribution_name }}.svg
    :alt: Supported versions
    :target: https://pypi.org/project/{{ cookiecutter.distribution_name }}

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/{{ cookiecutter.distribution_name }}.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/{{ cookiecutter.distribution_name }}
{% endif %}
{%- if cookiecutter.repo_hosting_domain == "github.com" %}
.. |commits-since| image:: https://img.shields.io/github/commits-since/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}/v{{ cookiecutter.version }}.svg
    :alt: Commits since latest release
    :target: https://{{ cookiecutter.repo_hosting_domain }}/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}/compare/v{{ cookiecutter.version }}...{{ cookiecutter.repo_main_branch }}
{% endif %}
.. |poetry| image:: https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json
    :alt: Poetry
    :target: https://python-poetry.org/

.. end-badges
{{ cookiecutter.project_short_description|wordwrap(119) }}
{% if cookiecutter.license != "no" %}
* Free software: {{ cookiecutter.license }}
{% endif %}
Installation
============

::

    pip install {{ cookiecutter.distribution_name }}

You can also install the in-development version with::
{% if cookiecutter.repo_hosting_domain == "github.com" %}
    pip install https://github.com/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}/archive/{{ cookiecutter.repo_main_branch }}.zip
{% elif cookiecutter.repo_hosting_domain == "gitlab.com" %}
    pip install https://gitlab.com/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}/-/archive/{{ cookiecutter.repo_main_branch }}/{{ cookiecutter.repo_name }}-{{ cookiecutter.repo_main_branch }}.zip
{% else %}
    pip install git+ssh://git@{{ cookiecutter.repo_hosting_domain }}/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}.git@{{ cookiecutter.repo_main_branch }}
{%- endif %}

Documentation
=============

{% if cookiecutter.sphinx_docs == "yes" %}
{{ cookiecutter.sphinx_docs_hosting }}
{% else %}
To use the project:

.. code-block:: python

    import {{ cookiecutter.package_name }}
{% endif %}

Development
===========

To run all the tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox

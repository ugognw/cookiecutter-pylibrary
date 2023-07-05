=========
Changelog
=========

All notable changes to this project will be documented in this file.

The format is based on `Keep a Changelog <https://keepachangelog.com/en/1.0.0/>`_,
and this project adheres to `Semantic Versioning <https://semver.org/spec/v2.0.0.html>`_.

{% set datestring -%}
{% if cookiecutter.release_date == 'today' -%}
{% now 'utc', '%Y-%m-%d' %}
{%- else %}{{ cookiecutter.release_date }}{% endif %}
{%- endset %}
{{ cookiecutter.version }} ({{ datestring }})
{% for _ in cookiecutter.version %}-{% endfor %}--{{ '-' * (datestring|length) }}-

Added
~~~~~
* First release on PyPI.

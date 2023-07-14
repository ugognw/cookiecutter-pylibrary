extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.coverage",
    "sphinx.ext.doctest",
    "sphinx.ext.extlinks",
    "sphinx.ext.ifconfig",
    "sphinx.ext.imgconverter",
    "sphinx.ext.napoleon",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
]
source_suffix = ".rst"
root_doc = 'index'
project = {{ cookiecutter.project_name|jsonquote }}
year = "{% if cookiecutter.year_from == cookiecutter.year_to %}{{ cookiecutter.year_from }}{% else %}{{ cookiecutter.year_from }}-{{ cookiecutter.year_to }}{% endif %}"
author = {{ cookiecutter.full_name|jsonquote }}
copyright = f"{year}, {author}"
version = release = {{ cookiecutter.version|jsonquote }}
exclude_patterns = ['build']
modindex_common_prefix = ['{{ cookiecutter.package_name }}.']
templates_path = ["."]

{%- if cookiecutter.repo_hosting == "github.com" %}
extlinks = {
    "issue": ("{{cookiecutter.__repo_url}}/issues/%s", "#"),
    "pr": ("{{cookiecutter.__repo_url}}/pull/%s", "PR #"),
}
{%- elif cookiecutter.repo_hosting == "gitlab.com" %}
extlinks = {
    "issue": ("{{cookiecutter.__repo_url}}/-/issues/%s", "#"),
    "mr": ("{{cookiecutter.__repo_url}}/-/merge_requests/%s", "PR #"),
}
{%- endif %}

# -- Options for sphinx.ext.autodoc ------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html#configuration

autoclass_content = 'class'

# -- Options for Napoleon ----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html#module-sphinx.ext.napoleon

napoleon_google_docstring = True
napoleon_use_ivar = True
napoleon_use_rtype = False
napoleon_use_param = False
napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = False

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "{{ cookiecutter.sphinx_theme|replace("-", "_") }}"
html_last_updated_fmt = '%a, %d %b %Y %H:%M:%S'
{%- if cookiecutter.sphinx_theme == "sphinx-rtd-theme" %}
# on_rtd is whether we are on readthedocs.org
on_rtd = os.environ.get("READTHEDOCS", None) == "True"

if not on_rtd:  # only set the theme if we are building docs locally
    html_theme = {{ cookiecutter.sphinx_theme }}

html_sidebars = {
    "**": ["searchbox.html", "globaltoc.html", "sourcelink.html"],
}
html_theme_options = {
    "githuburl": "https://{{ cookiecutter.repo_hosting }}/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}/",
}
{%- elif cookiecutter.sphinx_theme == "sphinx-py3doc-enhanced-theme" %}

{%- elif cookiecutter.sphinx_theme == "python-docs-theme" %}

{%- elif cookiecutter.sphinx_theme == "furo" %}
html_theme_options = {
    'source_repository': 'https://{{ cookiecutter.repo_hosting }}/{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}',
    'source_branch': '{{ cookiecutter.repo_main_branch }}',
    'source_directory': 'docs/source',
}
pygments_style = 'sphinx'
pygments_dark_style = 'monokai'
{%- else %}

{%- endif %}

smartquotes = True
html_split_index = False
html_short_title = f"{project}-{version}"

napoleon_use_ivar = True
napoleon_use_rtype = False
napoleon_use_param = False

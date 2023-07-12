import pathlib
import shutil
import subprocess
import sys


try:
    from click.termui import secho
except ImportError:
    warn = note = success = print
else:
    def warn(text):
        for line in text.splitlines():
            secho(line, fg="white", bg="red", bold=True)

    def note(text):
        for line in text.splitlines():
            secho(line, fg="yellow", bold=True)

    def success(text):
        for line in text.splitlines():
            secho(line, fg="green", bold=True)


if __name__ == "__main__":
    cwd = pathlib.Path().resolve()
    src = cwd / 'src'

{%- if 'readthedocs' not in cookiecutter.sphinx_docs_hosting %}
    cwd.joinpath('.readthedocs.yml').unlink()
{% endif %}

{%- if cookiecutter.command_line_interface == 'no' %}
    src.joinpath('{{ cookiecutter.package_name }}', '__main__.py').unlink()
    src.joinpath('{{ cookiecutter.package_name }}', 'cli.py').unlink()
{% endif %}

{%- if cookiecutter.github_actions == 'no' or cookiecutter.repo_hosting != 'github.com' %}
    shutil.rmtree(cwd.joinpath('.github'), ignore_errors=True)
{%- elif cookiecutter.gitlab_ci_cd == 'no' or cookiecutter.repo_hosting != 'gitlab.com' %}
    shutil.rmtree(cwd.joinpath('.gitlab'), ignore_errors=True)
    cwd.joinpath('.gitlab-ci.yml').unlink(missing_ok=True)
{% endif %}

{%- if cookiecutter.codecov == 'yes' %}
    cwd.joinpath('codecov.yml').unlink(missing_ok=True)
{%- endif %}

{%- if cookiecutter.pypi_disable_upload == 'yes' %}
    cwd.joinpath('.github', 'workflows', 'publish.yml').unlink(missing_ok=True)
    cwd.joinpath('.gitlab', 'templates', 'publish.yml').unlink(missing_ok=True)
{%- endif %}

{%- if cookiecutter.license == "no" %}
    cwd.joinpath('LICENSE').unlink()
{%- endif %}

    width = min(140, shutil.get_terminal_size(fallback=(140, 0)).columns)
{%- if cookiecutter.initialize_git_repository == 'yes' %}
    note(' Initializing Git repository '.center(width, "#"))
    _ = subprocess.check_call(['git', 'init'])
    _ = subprocess.check_call(['git', 'add', '--all'])
    _ = subprocess.check_call(['git', 'commit', ' -m', '"Add initial project skeleton."'])
    _ = subprocess.check_call(['git', 'tag', ' -m', 'v{{ cookiecutter.version }}'])
    _ = subprocess.check_call(['git', 'remote', 'add', 'origin', 'git@{{ cookiecutter.repo_hosting }}:{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}.git'])
    _ = subprocess.check_call(['git', 'push', ' -u', 'origin', '{{ cookiecutter.repo_main_branch }} v{{ cookiecutter.version }}'])
{%- endif %}
    package_installed = False
    venv_activated = False
{% if cookiecutter.install_package == 'yes' %}
    note(' Installing package and dependencies '.center(width, "#"))
    try:
        _ = subprocess.check_call(['poetry', 'install'])
        package_installed = True

{%- if cookiecutter.activate_virtual_environment %}
        note(' Activating virtual environment '.center(width, "#"))
        _ = subprocess.check_call(['source', '"$(poetry env info --path)"/bin/activate'])
        venv_activated = True
{%- endif %}
    except FileNotFoundError:
        note('Installing poetry'.center(width, "#"))
        _ = subprocess.check_call(
            [
                'curl',
                '-sSL',
                'https://install.python-poetry.org',
                '|',
                'python3',
                '-'
            ]
        )
        note('Poetry successfully installed'.center(width, "#"))
        _ = subprocess.check_call(['poetry', 'install'])
        package_installed = True
{% if cookiecutter.activate_virtual_environment %}
        note(' Activating virtual environment '.center(width, "#"))
        _ = subprocess.check_call(['source', '"$(poetry env info --path)"/bin/activate'])
        venv_activated = True
{%- endif %}
    except Exception:
            warn(
                'Unable to install Poetry.'.center(width, "#")
            )
            warn(
                'You will need to install Poetry in order to install the project and activate the virtual environment.'.center(width, "#")
            )
            warn(
                'https://python-poetry.org/docs/#installation.'.center(width, "#")
            )
{%- endif %}
    pre_commit_installed = False
{%- if cookiecutter.pre_commit == 'no' %}
    cwd.joinpath('.pre-commit-config.yaml').unlink()
{%- elif cookiecutter.install_precommit_hooks %}
    note(' Setting up pre-commit '.center(width, "#"))
    if cwd.joinpath('.git').exists():
        try:
            _ = subprocess.check_call(['pre-commit', 'install', '--install-hooks'])
            _ = subprocess.check_call(['pre-commit', 'autoupdate'])
            pre_commit_installed = True
        except FileNotFoundError:
            try:
                _ = subprocess.check_call(['pip', 'install', 'pre-commit'])
            except Exception:
                warn(
                'Unable to install pre-commit.'.center(width, "#")
                )

    else:
        print('Skipping precommit install.')
{%- endif %}
    success(' Successfully created `{{ cookiecutter.repo_name }}` '.center(width, "#"))
    print('See .cookiecutterrc for instructions on regenerating the project.')
    note('To get started run these:')
    commands = [
        'cd {{ cookiecutter.repo_name }}',
{%- if cookiecutter.initialize_git_repository == 'no' %}
        'git init',
{%- endif %}
    ]
{% if cookiecutter.pre_commit == 'yes' %}
    if not pre_commit_installed:
        commands.extend(('pre-commit install --install-hooks', 'pre-commit autoupdate'))
{% endif %}

    if not package_installed:
        commands.extend('poetry install')

    if not venv_activated:
        commands.extend('source "$(poetry env info --path)"/bin/activate')

{%- if cookiecutter.initialize_git_repository == 'no' %}
    commands.extend(
        (
            'git add --all',
            'git commit -m "Add initial project skeleton."',
            'git tag v{{ cookiecutter.version }}',
            'git remote add origin git@{{ cookiecutter.repo_hosting }}:{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}.git',
            'git push -u origin {{ cookiecutter.repo_main_branch }} v{{ cookiecutter.version }}'
        )
    )
{%- endif %}

    print('\n'.join(commands))
    cli_bin_name = '{{ cookiecutter.cli_bin_name }}'
    while cli_bin_name.endswith('.py'):
        cli_bin_name = cli_bin_name[:-3]

        if cli_bin_name == '{{ cookiecutter.package_name }}':
            warn('''
┌───────────────────────────────────────────────────────────────────────┐
│ ERROR:                                                                │
│                                                                       │
│     Your result package is broken. Your bin script named              │
│     {0} │
│                                                                       │
│     Python automatically adds the location of scripts to              │
│     `sys.path`. Because of that, the bin script will fail             │
│     to import your package because it has the same name               │
│     (it will try to import itself as a module).                       │
│                                                                       │
│     To avoid this problem you have two options:                       │
│                                                                       │
│     * Remove the ".py" suffix from `cli_bin_name`. │
│                                                                       │
│     * Use a different `package_name` {1} │
└───────────────────────────────────────────────────────────────────────┘
'''.format(
                '"{{ cookiecutter.cli_bin_name }}" will shadow your package.'.ljust(65),
                '(not "{0}").'.format(cli_bin_name).ljust(32)))
            sys.exit(1)
        break

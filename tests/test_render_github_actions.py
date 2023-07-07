from jinja2 import Environment, FileSystemLoader
import pathlib


def test_render_cookiecutter():
    env = Environment(
        loader=FileSystemLoader(
            '{{cookiecutter.repo_name}}/ci/templates'
        ),
    )

    template = env.get_template('.github/workflows/github-actions.yml.jinja')
    tox_environments = ['py310', 'py311']
    cookiecutter = {
        'sphinx_docs': 'yes',
        'coveralls': 'yes',
        'codecov': 'yes',
        'github_actions_windows': 'yes',
        'github_actions_osx': 'yes'
    }

    filename = pathlib.Path('tests/results') / 'render_cookiecutter.txt'

    with open(filename, mode='w', encoding='utf-8') as file:
        file.write(
            template.render(
                cookiecutter=cookiecutter,
                tox_environments=tox_environments
            )
        )


def test_render_tox_environments():
    env = Environment(
        loader=FileSystemLoader(
            'tests/results/'
        ),
        trim_blocks=True,
        lstrip_blocks=True,
        keep_trailing_newline=True
    )

    template = env.get_template('render_cookiecutter.txt')
    tox_environments = ['py310', 'py311']
    cookiecutter = {
        'sphinx_docs': 'yes',
        'coveralls': 'yes',
        'codecov': 'yes',
        'github_actions_windows': 'yes',
        'github_actions_osx': 'yes'
    }

    filename = pathlib.Path('tests/results') / 'render_tox.txt'

    with open(filename, mode='w', encoding='utf-8') as file:
        file.write(
            template.render(
                cookiecutter=cookiecutter,
                tox_environments=tox_environments
            )
        )


test_render_cookiecutter()

test_render_tox_environments()

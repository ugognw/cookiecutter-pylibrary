from jinja2 import Environment, FileSystemLoader
import pathlib


def test_render_python_yml():
    env = Environment(
        loader=FileSystemLoader(
            '{{cookiecutter.repo_name}}/.github/workflows/'
        ),
    )

    template = env.get_template('python.yml')
    tox_environments = ['py310', 'py311']
    cookiecutter = {
        'sphinx_docs': 'yes',
        'coveralls': 'yes',
        'codecov': 'yes',
        'codacy': 'yes',
        'github_actions_windows': 'yes',
        'github_actions_osx': 'yes'
    }

    filename = pathlib.Path('tests/results') / 'python.yml'

    with open(filename, mode='w', encoding='utf-8') as file:
        file.write(
            template.render(
                cookiecutter=cookiecutter,
                tox_environments=tox_environments
            )
        )


test_render_python_yml()

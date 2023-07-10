from jinja2 import Environment, FileSystemLoader
import pathlib

import pytest


@pytest.fixture(name='environment')
def fixture_environment(request) -> Environment:
    if request.node.get_closest_marker('repo_hosting').args[0] == 'github.com':
        return Environment(
            loader=FileSystemLoader(
                '{{cookiecutter.repo_name}}/.github/workflows/'
            ),
        )
    elif request.node.get_closest_marker('repo_hosting').args[0] == 'gitlab.com':
        return Environment(
            loader=FileSystemLoader(
                '{{cookiecutter.repo_name}}'
            ),
        )


@pytest.fixture(name='template_names')
def fixture_template_names(request):
    if request.node.get_closest_marker('repo_hosting').args[0] == 'github.com':
        return ('docs.yml', 'licenses.yml', 'publish.yml', 'python.yml')
    elif request.node.get_closest_marker('repo_hosting').args[0] == 'gitlab.com':
        return ('.gitlab-ci.yml',)


class TestGithub:
    @staticmethod
    @pytest.mark.repo_hosting('github.com')
    def test_render(cookie_config: dict, environment: Environment, template_names: list[str]):
        for template_name in template_names:
            filename = pathlib.Path('tests/.github/workflows') / template_name
            template = environment.get_template(template_name)
            with open(filename, mode='w', encoding='utf-8') as file:
                file.write(
                    template.render(
                        cookiecutter=cookie_config
                    )
                )


class TestGitlab:
    @staticmethod
    @pytest.mark.repo_hosting('gitlab.com')
    def test_render(cookie_config: dict, environment: Environment, template_names: list[str]):

        for template_name in template_names:
            filename = pathlib.Path('tests') / template_name
            template = environment.get_template(template_name)
            with open(filename, mode='w', encoding='utf-8') as file:
                file.write(
                    template.render(
                        cookiecutter=cookie_config
                    )
                )

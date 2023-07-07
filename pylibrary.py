from json import dumps
import pathlib

from jinja2 import Environment
from jinja2.ext import Extension


def jsonquote(value):
    return dumps(value, ensure_ascii=False)


class JsonQuoteExtension(Extension):
    def __init__(self, environment: Environment):
        super().__init__(environment)
        environment.filters['jsonquote'] = jsonquote
        environment.globals['cwd'] = pathlib.Path.cwd().as_posix()

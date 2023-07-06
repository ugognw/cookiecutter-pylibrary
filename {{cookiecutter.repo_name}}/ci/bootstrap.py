#!/usr/bin/env python
import os
import pathlib
import subprocess
import sys

project_root: pathlib.Path = pathlib.Path(__file__).resolve().parent.parent
templates = project_root / "ci" / "templates"


def check_call(args):
    print("+", *args)
    subprocess.check_call(args)


def exec_in_env():
    """Creates a virtual environment from which to run `main`

    This function is called in `post_gen_project.py` if the required
    dependencies (e.g., `tox`, `jinja2`) are not installed after the project is
    created. A virtual environment is created (either via `venv` or
    `virtualenv`), the required dependencies are installed, and then the
    module is run via a `python ci/bootstrap.py` command.
    """
    env_path = project_root / ".tox" / "bootstrap"
    if sys.platform == "win32":
        bin_path = env_path / "Scripts"
    else:
        bin_path = env_path / "bin"
    if not env_path.exists():
        import subprocess

        print(f"Making bootstrap env in: {env_path} ...")
        try:
            check_call([sys.executable, "-m", "venv", env_path])
        except subprocess.CalledProcessError:
            try:
                check_call([sys.executable, "-m", "virtualenv", env_path])
            except subprocess.CalledProcessError:
                check_call(["virtualenv", env_path])
        print("Installing `jinja2` into bootstrap environment...")
        check_call([bin_path / "pip", "install", "jinja2", "tox"])
    python_executable = bin_path / "python"
    if not python_executable.exists():
        python_executable = python_executable.with_suffix(".exe")

    print(f"Re-executing with: {python_executable}")
    print("+ exec", python_executable, __file__, "--no-env")
    os.execv(python_executable, [python_executable, __file__, "--no-env"])


def main():
    import jinja2

    print(f"Project root: {project_root}")

    jinja = jinja2.Environment(
        loader=jinja2.FileSystemLoader(str(templates)),
        trim_blocks=True,
        lstrip_blocks=True,
        keep_trailing_newline=True,
    )
    # `tox` need not be installed globally, but must be importable
    # by the Python that is running this script.
    # This uses sys.executable the same way that the call in
    # cookiecutter-pylibrary/hooks/post_gen_project.py
    # invokes this bootstrap.py itself.
    # Collect only python testing environments
    tox_environments = []
    lines = subprocess.check_output(
        [sys.executable, "-m", "tox", "--listenvs"], universal_newlines=True
    ).splitlines()
    for line in lines:
        line = line.split()[0]
        if line.startswith('py'):
            tox_environments.append(line)

    # Render CI/CD Templates
    for template in templates.rglob("*"):
        if template.is_file():
            template = template.relative_to(templates).as_posix().strip('.jinja')
            template_destination = project_root / template
            template_destination.parent.mkdir(parents=True, exist_ok=True)
            template_destination.write_text(jinja.get_template(template).render(tox_environments=tox_environments))
            print(f"Wrote {template}")
    print("DONE.")


if __name__ == "__main__":
    args = sys.argv[1:]
    if args == ["--no-env"]:
        main()
    elif not args:
        exec_in_env()
    else:
        print(f"Unexpected arguments: {args}", file=sys.stderr)
        sys.exit(1)

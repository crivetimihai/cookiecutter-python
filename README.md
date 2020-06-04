cookiecutter-python
======================
> Quickly setup a new Python project and packaging using standard boilterplate templates.

An [cookiecutter](https://github.com/audreyr/cookiecutter) template for Python packages,
and some guidelines for Python packaging.

Usage
-----

```bash
git clone git@github.com:crivetimihai/cookiecutter-python.git
pip install --user --upgrade cookiecutter
cookiecutter cookiecutter-python
```

You should then change the classifiers in `{{ package_name }}/setup.py` - it is assumed that the project will run on the latest versions of Python 3, so you should remove any classifiers that do not apply. The full list of PyPI classifiers can be found [here](https://pypi.python.org/pypi?:action=list_classifiers).


Key Decisions
--------------

### Packaging

- **Use setuptools**
  It's the standard packaging library for Python. `distribute` has merged back into `setuptools`, and `distutils` is less capable. Use `setup.py` with `setup.cfg`

- **setup.py should not import anything from the package**
  When installing from source, the user may not have the packages dependencies installed, and importing the package is likely to raise an `ImportError`.

- **Makefile used for all application build steps**
  Capture all commands inside a `Makefile`. Ex: `make build`, `make docker`, `make buildah`, `make test`, etc.

- **Place modules directory in root, avoid ./src/module**
  See [Structuring Your Project](https://docs.python-guide.org/writing/structure/)

- **Use bump2version**
  See [https://github.com/c4urself/bump2version](https://github.com/c4urself/bump2version). Configured in `.bumpversion.cfg`. To update your version:

  `bump2version --verbose --new-version 0.1.1 major`

### Testing

- **Use [Tox](https://tox.readthedocs.io) to manage test environments**
  Tox provides isolation, runs tests across multiple Python versions, and ensures the package can be installed.

- **Use [pytest](https://docs.pytest.org) as the default test runner**
  This can be changed easily, though pytest is a easier, more powerful test library and runner than the standard library's unittest.

- **Define testing dependencies in `tox.ini`**
  Avoid duplicating dependency definitions, and use `tox.ini` as the canonical description of how the unittests should be run.

### CLI

- **Use `argparse` to parse arguments.**
  It's in the standard library and supports complex scenarios. Alternatives include `click` and `docopt`.

- Use [configparser — Configuration file parser](https://docs.python.org/3/library/configparser.html)
  Standard library configuration parser, supports `ini` format.


References
----------

- https://www.bernat.tech/pep-517-and-python-packaging/
- https://www.python.org/dev/peps/pep-0518/
- https://snarky.ca/what-the-heck-is-pyproject-toml/
- https://hackersandslackers.com/simplify-your-python-projects-configuration/
- https://pypi.org/project/pipx/

Recommended tools
------------------
- https://awesome-python.com/#command-line-interface-development
- rich - Python library for rich text and beautiful formatting in the terminal. Also provides a great RichHandler log handler.

Recommended editors
------------------

- micro
- vim

## Visual Studio Code

- https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring
- https://marketplace.visualstudio.com/items?itemName=donjayamanne.python-extension-pack


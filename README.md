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

### `setup.py`

- **Use setuptools**
  It's the standard packaging library for Python. `distribute` has merged back into `setuptools`, and `distutils` is less capable.

- **setup.py should not import anything from the package**
  When installing from source, the user may not have the packages dependencies installed, and importing the package is likely to raise an `ImportError`.

### Testing

- **Use [Tox](https://tox.readthedocs.io) to manage test environments**
  Tox provides isolation, runs tests across multiple Python versions, and ensures the package can be installed.
- **Use [pytest](https://docs.pytest.org) as the default test runner**
  This can be changed easily, though pytest is a easier, more powerful test library and runner than the standard library's unittest.
- **Define testing dependencies in `tox.ini`**
  Avoid duplicating dependency definitions, and use `tox.ini` as the canonical description of how the unittests should be run.

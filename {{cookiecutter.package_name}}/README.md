{{ cookiecutter.package_name }}
{{ cookiecutter.package_name|count * "=" }}

{{ cookiecutter.package_description }}

Usage
-----

Installation
------------

```bash
python3 -m pip install {{ cookiecutter.package_name }}
```

Requirements
------------

- [requirements.dev.txt](./requirements.dev.txt)
- [requirements.txt](./requirements.txt)

Licence
-------

{{ cookiecutter.license }} - see [LICENSE](./LICENSE)

Authors
-------

`{{ cookiecutter.package_name }}` was written by [{{ cookiecutter.author_name }}](mailto:{{ cookiecutter.author_email }}).

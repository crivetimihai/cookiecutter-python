User Guide
##########

This section of the documentation provides user focused information such as
installing and quickly using this package.

.. _install-guide-label:

Install Guide
=============

.. note::

    It is best practice to install run Python projects in a virtual
    environment, which can be created and activated as follows using
    Python 3.7+.

    .. code-block:: console

        $ python -m venv venv
        $ source venv/bin/activate
        (venv) $ pip install {{cookiecutter.package_name}}

The simplest way to install {{cookiecutter.package_display_name}} is using Pip.

.. code-block:: console

    $ pip install {{cookiecutter.package_name}}

This will install ``{{cookiecutter.package_name}}`` and all of its dependencies.


.. _api-reference-label:

API Reference
=============

The `API Reference <http://{{cookiecutter.package_name}}.readthedocs.io>`_ provides API-level documentation.


.. include:: ../../../CHANGELOG.rst


.. _report-bugs-label:

Report Bugs
===========

Report bugs at the `issue tracker <https://github.com/{{cookiecutter.github_user_name}}/{{cookiecutter.github_repo_name}}/issues>`_.

Please include:

  - Operating system name and version.
  - Any details about your local setup that might be helpful in troubleshooting.
  - Detailed steps to reproduce the bug.

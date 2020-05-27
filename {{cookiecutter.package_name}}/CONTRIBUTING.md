Contributing Guide
==================

Contributions are welcome and greatly appreciated!

Workflow
--------

A bug-fix or enhancement is delivered using a pull request. A good pull
request should cover one bug-fix or enhancement feature. This ensures
the change set is easier to review and less likely to need major re-work
or even be rejected.

The workflow that developers typically use to fix a bug or add
enhancements is as follows.

-   Fork the `{{cookiecutter.github_repo_name}}` repo into your account.

-   Obtain the source by cloning it onto your development machine.

    ```bash
    $ git clone git@github.com:your_name_here/{{cookiecutter.github_repo_name}}.git
    $ cd {{cookiecutter.package_name}}
    ```

-   Create a branch for local development:

    ```
    $ git checkout -b name-of-your-bugfix-or-feature
    ```

    Now you can make your changes locally.

-   Familiarize yourself with the developer convenience rules in the
    Makefile.

    ```bash
    $ make help
    ```

-   Create and activate a Python virtual environment for local
    development.

    ```bash
    $ make venv
    $ source path/to/<venv-name>/bin/activate
    (venv) $
    ```

    The rule creates the virtual environment outside the project
    directory so that it never accidentally gets added to the change
    set.

-   Develop fix or enhancement:

    -   Make a fix or enhancement (e.g. modify a class, method,
        function, module, etc).

    -   Update an existing unit test or create a new unit test module to
        verify the change works as expected.

    -   Run the test suite.

        ```bash
        (venv) $ make test
        ```

    -   Check code coverage of the area of code being modified.

        ```bash
        (venv) $ make check-coverage
        ```

        Review the output produced in
        `docs/source/coverage/coverage.html`. Add additional test steps,
        where practical, to improve coverage.

    -   The change should be style compliant. Perform style check.

        ```bash
        (venv) $ make check-style
        ```

    -   The change should include type annotations where appropriate.
        Perform type annotations check.

        ```bash
        (venv) $ make check-types
        ```

    -   Fix any errors or regressions.

-   The docs and the change log should be updated for anything but
    trivial bug fixes. Perform docs check.

    > ```bash
    > (venv) $ make docs
    > ```

-   Commit and push changes to your fork.

    ```bash
    $ git add .
    $ git commit -m "A detailed description of the changes."
    $ git push origin name-of-your-bugfix-or-feature
    ```

    A pull request should preferably only have one commit upon the
    current master HEAD, (via rebases and squash).

-   Submit a pull request through the service website (e.g. Github,
    Gitlab).

-   Check automated continuous integration steps all pass. Fix any
    problems if necessary and update the pull request.

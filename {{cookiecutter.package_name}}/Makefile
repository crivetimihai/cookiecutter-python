VENVS_DIR := $(HOME)/.venv
VENV_DIR := $(VENVS_DIR)/{{cookiecutter.package_name}}

.PHONY: help
help:
	@grep "^# help\:" Makefile | grep -v grep | sed 's/\# help\: //' | sed 's/\# help\://'

# help: MAINTAIN
# help: venv                           - create a virtual environment for development
.PHONY: venv
venv:
	@test -d "$(VENVS_DIR)" || mkdir -p "$(VENVS_DIR)"
	@rm -Rf "$(VENV_DIR)"
	@python3 -m venv "$(VENV_DIR)"
	@/bin/bash -c "source $(VENV_DIR)/bin/activate && pip install pip --upgrade && pip install -r requirements.dev.txt && pip install -e ."
	@echo -e "Entering virtual environment using:\n\n\t$ . $(VENV_DIR)/bin/activate\n"
	@. $(VENV_DIR)/bin/activate


# help: clean                          - clean all files using setup.py
.PHONY: clean
clean:
	@python setup.py clean


# help: git-clean                      - clean all files using .gitignore rules
.PHONY: git-clean
git-clean:
	@git clean -X -f -d


# help: git-scrub                      - clean all files, even untracked files
.PHONY: git-scrub
git-scrub:
	git clean -x -f -d


# help:
# help: LINT

# help: format-black                   - format code with black
.PHONY: format-black
format-black:
	@black {{cookiecutter.package_name}} tests setup.py


# help: format-yapf                    - format code with yapf
.PHONY: format-yapf
format-yapf:
	@yapf -i --recursive {{cookiecutter.package_name}} tests setup.py


# help: lint-flake8                    - lint code with flake8
.PHONY: lint-flake8
lint-flake8:
	@flake8 {{cookiecutter.package_name}} tests setup.py


# help: lint-pylint                    - lint code with pylint
.PHONY: lint-pylint
lint-pylint:
	@pylint {{cookiecutter.package_name}} tests setup.py


# help: check-types                    - check type hint annotations
.PHONY: check-types
check-types:
	@MYPYPATH=$(VENV_DIR)/lib/python*/site-packages mypy -p {{cookiecutter.package_name}} --ignore-missing-imports


# help:
# help: TEST

# help: test                           - run tests
.PHONY: test
test:
	@python -m unittest discover -s tests


# help: test-verbose                   - run tests [verbosely]
.PHONY: test-verbose
test-verbose:
	@python -m unittest discover -s tests -v


# help: check-coverage                 - perform test coverage checks
.PHONY: check-coverage
check-coverage:
	@coverage run -m unittest discover -s tests
	@# produce html coverage report on modules
	@coverage html -d docs/source/coverage --include="{{cookiecutter.package_name}}/*"
	@# rename coverage html file for latter use with documentation
	@cd docs/source/coverage; mv index.html coverage.html


# help: tox                  					- build for all python versions with tox
.PHONY: tox
tox:
	@tox


# help:
# help: DOCUMENT

# help: docs                           - generate project documentation
.PHONY: check-coverage
docs: check-coverage
	@cd docs; rm -rf source/api/{{cookiecutter.package_name}}*.rst source/api/modules.rst build/*
	@cd docs; make html
	@# Copy coverage output into docs build tree
	@cd docs; cp -R source/coverage build/html/.


# help: check-docs                     - quick check docs consistency
.PHONY: check-docs
check-docs:
	@cd docs; make dummy


# help: serve-docs                     - serve project html documentation
.PHONY: serve-docs
serve-docs:
	@cd docs/build; python -m http.server --bind 127.0.0.1


# help:
# help: PACKAGE

# help: dist                           - create a wheel distribution package
.PHONY: dist
dist:
	@python setup.py bdist_wheel


# help: sdist                          - create a sdist distribution package
.PHONY: sdist
sdist:
	@python setup.py sdist


# help: install                        - install the package
.PHONY: install
install:
	@python setup.py install


# help: install-editable               - install the package using pip install --editable
.PHONY: install-editable
install-editable:
	@python -m pip install --editable .


# help: dist-test                      - test a wheel distribution package
.PHONY: dist-test
dist-test: dist
	@cd dist && ../tests/test-dist.bash ./{{cookiecutter.package_name}}-*-py3-none-any.whl


# help: dist-upload                    - upload a wheel distribution package
.PHONY: dist-upload
dist-upload:
	@twine upload dist/{{cookiecutter.package_name}}-*-py3-none-any.whl


# help:
# help: CONTAINERIZE

# help: docker                         - build container using docker
.PHONY: docker
docker:
	@docker build -t {{cookiecutter.docker_id}}/{{cookiecutter.package_name}} .


# help: podman                         - build container using podman
.PHONY: podman
podman:
	@podman build -t {{cookiecutter.docker_id}}/{{cookiecutter.package_name}} .


# help: buildah                        - build container using buildah
.PHONY: buildah
buildah:
	@./buildah.sh


# Keep these lines at the end of the file to retain output formatting.
# help:

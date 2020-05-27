FROM python:{{ cookiecutter.python_version }}-alpine
LABEL name="{{ cookiecutter.docker_id }}/{{ cookiecutter.package_name}}" \
      version="{{ cookiecutter.package_version }}" \
      maintainer="{{ cookiecutter.author_name }} <{{ cookiecutter.author_email }}>" \
      description="{{ cookiecutter.package_description }}"

# COPY application
COPY . /app

# INSTALL PYTHON PACKAGES
RUN python -m pip install --upgrade pip
RUN python -m pip install --no-cache-dir --upgrade -r /app/requirements.txt \
    && python -m pip install --no-cache-dir --upgrade /app

# PERSISTENCE
VOLUME ["/app"]

# WORKDIR
WORKDIR /app

# COMMAND and ENTRYPOINT:
CMD ["{{ cookiecutter.package_name }}_cmd"]

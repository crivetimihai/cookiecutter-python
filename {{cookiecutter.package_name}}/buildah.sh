#!/bin/bash

# Check if buildah in installed
command -v buildah >/dev/null 2>&1 || { echo >&2 "buildah not installed; Aborting."; exit 1; }

# Label the container
container_id=$(buildah from --pull python:{{ cookiecutter.python_version }}-alpine)
buildah config \
  --label Name="{{ cookiecutter.docker_id }}/{{ cookiecutter.package_name}}" \
  --label Version="{{ cookiecutter.package_version }}" \
  --label Maintainer="{{ cookiecutter.author_name }} <{{ cookiecutter.author_email }}>" \
  --label Description="{{ cookiecutter.package_description }}" \
  $container_id

# Install the app
buildah run $container_id mkdir -p /app
buildah config --workingdir /app $container_id
buildah copy $container_id $PWD .
buildah run --net host $container_id python -m pip install --upgrade pip
buildah run --net host $container_id python -m pip install --no-cache-dir --upgrade -r /app/requirements.txt
buildah run --net host $container_id python -m pip install --no-cache-dir --upgrade /app

# Commit
buildah config --entrypoint '/app/{{ cookiecutter.package_name }}_cmd' $container_id
buildah commit $container_id {{ cookiecutter.package_name }}

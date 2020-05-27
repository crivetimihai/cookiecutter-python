#!/bin/bash

id=$(buildah from --pull python:{{ cookiecutter.python_version }}-alpine)
buildah run $id mkdir -p /app
buildah config --workingdir /app $id
buildah copy $id $PWD .
buildah run --net host $id python -m pip install --upgrade pip
buildah run --net host $id python -m pip install --no-cache-dir --upgrade -r /app/requirements.txt
buildah run --net host $id python -m pip install --no-cache-dir --upgrade /app
buildah config --entrypoint '/app/{{ cookiecutter.package_name }}_cmd' $id
buildah commit $id {{ cookiecutter.package_name }}

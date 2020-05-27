#!/bin/sh

git init
git add .
git commit -m "{{ cookiecutter.package_name }}: {{ cookiecutter.package_description }}"

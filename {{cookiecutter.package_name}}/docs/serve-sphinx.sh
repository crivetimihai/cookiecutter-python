#!/bin/sh -e
sphinx-apidoc -f -o source/ ../src/*
make html
cd build; python -m http.server

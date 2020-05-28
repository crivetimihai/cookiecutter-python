#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Setup using setup.cfg and custom clean and pylint commands."""

import os
from distutils.command.clean import clean
from setuptools import setup


def parse_requirements(filename):
    """ Load requirements from a pip requirements file """
    with open(filename, "r") as file_descriptor:
        lines = []
        for line in file_descriptor:
            line.strip()
            if line and not line.startswith("#"):
                lines.append(line)
    return lines


requirements = parse_requirements("requirements.txt")


class CustomClean(clean):
    """Custom clean command."""

    def run(self):
        # Run the original clean
        super().run()

        # Clean additional junk
        cmd_list = dict(
            DS_Store=r"find ./ -name '.DS_Store' -print0 | xargs -0 rm -f;",
            empty_dirs=r"find ./ -type d -empty -delete;",
            htmlcov=r"find ./ -type d -name 'htmlcov' -exec rm -rf {} \;",
            mypy=r"find ./ -type d -name '.mypy_cache' -exec rm -rf {} \;",
            pyc=r"find ./ -type f -name '*.pyc' -exec rm -rf {} \;",
            pytest=r"rm -rf .pytest_cache",
            eggs=r"rm -rf .eggs *.egg-info",
            bak=r"find ./ -type f -name '*.bak' -exec rm {} \;",
            sonar=r"rm -rf ./.scannerwork",
            coverage=r"rm .coverage*",
            docs_build=r"rm -rf docs/build/",
        )
        for key, cmd in cmd_list.items():
            print("Cleanning {}".format(key))
            os.system(cmd)


setup(
    cmdclass={"clean": CustomClean}, install_requires=requirements,
)

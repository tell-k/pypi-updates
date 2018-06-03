# -*- coding: utf-8 -*-
import re
import sys
import os

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import pytest
        args = [a.strip() for a in self.pytest_args.split(' ')]
        errno = pytest.main(args)
        sys.exit(errno)

here = os.path.dirname(__file__)

version_regex = re.compile(r".*__version__ = '(.*?)'", re.S)
version_script = os.path.join(here, 'pypi_updates', '__init__.py')
version = version_regex.match(open(version_script, 'r').read()).group(1)

requirements = os.path.join(here, 'requirements.txt')
install_requires = [l.strip() for l in open(requirements, 'r').readlines()]

long_description=open(os.path.join("README.rst")).read(),

tests_require = [
    "pytest-cov",
    "pytest",
    "mock",
    "testfixtures",
    "responses",
]

classifiers = [
    "Development Status :: 3 - Alpha",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python",
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 2.7",
    "Topic :: Internet",
    "Topic :: Communications",
]

setup(
    name="pypi_updates",
    version=version,
    author="tell-k",
    author_email="ffk2005 at gmail.com",
    packages=find_packages(exclude=["tests"]),
    description="Bot to flow Pypi recent updates.",
    long_description=long_description,
    classifiers=classifiers,
    install_requires=install_requires,
    tests_require=tests_require,
    cmdclass={'test': PyTest},
    license="MIT",
    url="https://github.com/tell-k/pypi-updates",
)

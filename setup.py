# -*- coding: utf-8 -*-
import os
from setuptools import setup

__author__ = 'tell-k <ffk2005@gmail.com>'
__version__ = '0.0.3'

requires = [
    "feedparser",
    "kuroko",
    "pylibmc",
    "python-dateutil",
    "tweepy",
    "bitlyapi",
]

classifiers = [
    "Development Status :: 3 - Alpha",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python",
    "Programming Language :: Python :: 2",
    "Topic :: Internet",
    "Topic :: Communications",
]

setup(
    name="pypi_updates",
    author=__author__,
    version=__version__,
    packages=["pypi_updates"],
    description="Bot to flow Pypi recent updates.",
    long_description=open(os.path.join("README.rst")).read(),
    install_requires=requires,
    license="MIT",
    url="https://github.com/tell-k/pypi-updates",
    classfiers=classifiers,
)

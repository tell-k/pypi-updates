# -*- coding: utf-8 -*-

from setuptools import setup

__author__ = 'tell-k <ffk2005@gmail.com>'
__version__ = '0.0.1'

requires = [
    "feedparser",
    "kuroko",
    "pylibmc",
    "python-dateutil",
    "tweepy",
    "bitlyapi",
]

setup(
    name="pypi_updates",
    packages=["pypi_updates"],
    install_requires=requires,
)

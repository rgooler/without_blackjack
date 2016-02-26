#!virtualenv/bin/python
import os
from setuptools import setup


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="Without Blackjack",
    version="0.0.1",
    author="Ryan Gooler",
    author_email="ryan.gooler@gmail.com",
    description=("A text-only client for secondlife"),
    license="BSD",
    keywords="secondlife",
    url="http://packages.python.org/withoutbj",
    packages=['withoutbj', 'test'],
    long_description=read('README.md'),
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)

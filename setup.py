#!/usr/bin/env python

import distutils.core
import subprocess
import sys
# Importing setuptools adds some features like "setup.py develop", but
# it's optional so swallow the error if it's not there.
try:
    import setuptools
except ImportError:
    pass

kwargs = {}

major, minor = sys.version_info[:2]

if major >= 3:
    import setuptools  # setuptools is required for use_2to3
    kwargs["use_2to3"] = True

distutils.core.setup(
    name = "py-gravatar",
    version = "0.0.3",
    license = "MIT",
    py_modules = ["gravatar"],
    package_data = {"": ["README.md", "LICENSE"]},
    author = "Alek Storm",
    author_email = "alek.storm@gmail.com",
    url = "http://alekstorm.github.com/pygravatar",
    description = "Python bindings for the Gravatar API",
    long_description = subprocess.Popen('pandoc -r markdown -w rst README.md', stdout=subprocess.PIPE, shell=True).communicate()[0],
    **kwargs
)

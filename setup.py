#!/usr/bin/env python

from distutils.core import setup

setup(name='numpy_utils',
      version='1.0',
      description='Python Distribution Utilities',
      author='Roland Jung',
      author_email='roland.jung@aau.at',
      url='https://gitlab.aau.at/aau-cns/py3_pkgs/numpy_utils/',
      packages=['distutils', 'distutils.command', 'numpy'],
     )

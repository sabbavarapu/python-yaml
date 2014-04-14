#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup
from employees.employees import Employees

setup(
    name=Employees.__name__,
    version=Employees.__version__,
    author='Frank H. Jung',
    author_email='frankhjung@linux.com',
    packages=['employees', 'tests'],
    scripts=[''],
    url='https://github.com/frankhjung/python-yaml',
    license='LICENSE.txt',
    description='Python example project.',
    long_description=open('README.rst').read(),
    install_requires=[
        'yaml' >= '3.10-4',
    ],
)

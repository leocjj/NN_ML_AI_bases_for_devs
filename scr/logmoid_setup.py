#!/usr/bin/env python3
""" logmoid activation function - CYTHON SETUP """
from setuptools import setup
from Cython.Build import cythonize
'''
To build, run
    python setup.py build_ext --inplace
Then simply start a Python session and do:
    from logmoid import logmoid, logmoid_inv
and use the imported function as you see fit.
'''

setup(
    name='Hello world app',
    ext_modules=cythonize("logmoid.pyx", language_level = "3"),
    zip_safe=False,
)

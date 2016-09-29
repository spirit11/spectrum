#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name="hospectrum",
    version="0.1",
    packages=find_packages(exclude=['*.demo']),
    install_requires=['numpy>=1.8', 'scipy>0.13.3', 'matplotlib>1.3.1']
)

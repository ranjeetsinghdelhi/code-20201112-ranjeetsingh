#!/usr/bin/env python
from distutils.core import setup
import setuptools

setup(
    name="BMI Analysis",
    version='1.0',
    description='BMI Related Analysis',
    author='Ranjeet Singh',
    author_email='allnew@email.com',
    url='https://example.com',
    install_requires=['pandas'],
    test_suite='bmi_calculator',
)
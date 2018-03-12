# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import face

with open('requirements.txt', 'r') as f:
    INSTALL_REQUIRES = f.readlines()

with open('requirements-dev.txt', 'r') as f:
    TESTS_REQUIRE = f.readlines()

setup(
    name='FACe library',
    description='FACe interface to simplify the interaction with their webservices',
    version=face.__version__,
    url='https://www.gisce.net',
    author='Xavi Torelló',
    author_email='xtorello@gisce.net',
    packages=find_packages(),
    install_requires=INSTALL_REQUIRES,
    license='General Public Licence 3',
    provides=['FACe_signer'],
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6"
    ]
)

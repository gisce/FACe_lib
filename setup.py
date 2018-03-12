# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import face

with open('requirements.txt', 'r') as f:
    INSTALL_REQUIRES = f.readlines()

with open('requirements-dev.txt', 'r') as f:
    TESTS_REQUIRES = f.readlines()

setup(
    name='FACe_lib',
    description='FACe interface to simplify the interaction with their webservices',
    version=face.__version__,
    url='http://www.gisce.net',
    author='GISCE-TI, S.L.',
    author_email='devel@gisce.net',
    packages=find_packages(),
    install_requires=INSTALL_REQUIRES,
    tests_require=TESTS_REQUIRES,
    license='GNU GPLv3',
    provides=['FACe_lib'],
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
    ]
)

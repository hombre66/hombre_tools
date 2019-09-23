"""setup.py"""
from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md')) as f:
    long_description = f.read()

setup(
    name='hombre_tools',  # Required

    version='0.1.0',  # Required
    description='tools for daily usage',  # Optional
    url='https://github.com/hombre66/hombre_tools',  # Optional
    classifiers=[
        'Development Status :: 5 - Production',
        'Intended Audience :: DB Developers',
        'Topic :: Databases',
        'License ::  MIT License',
        'Programming Language :: Python :: 3.7',
    ],

    packages=find_packages(exclude=['contrib', 'docs', 'tests']),  # Required

    python_requires='>=3.6',


    extras_require={  # Optional
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },
    data_files=[('my_data', ['data//catalog_new.h5'])], 

)
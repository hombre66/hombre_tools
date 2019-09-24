"""setup.py"""
from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md')) as f:
    long_description = f.read()

setup(
    name='hombre_tools',  # Required

    version='0.1.4',  # Required
    description='tools for daily usage',  # Optional
    url='https://github.com/hombre66/hombre_tools',  # Optional

    packages=find_packages(exclude=['contrib', 'docs', 'tests']),  # Required

    python_requires='>=3.6',
    install_requires=['cx-Oracle==7.2.2',
                      'JayDeBeApi==1.1.1',
                      'jupyter==1.0.0',
                      'numpy==1.17.0',
                      'pandas==0.25.0',
                      'pandas-profiling==2.3.0',
                      'pyodbc==4.0.27',
                      'pyOpenSSL==19.0.0',
                      'pyperclip==1.7.0',
                      'python-dateutil==2.8.0',
                      'python-settings==0.2',
                      'pywin32==224',
                      'pywin32-ctypes==0.2.0',
                      'pywinpty==0.5.5',
                      'requests==2.22.0',
                      'scipy==1.3.0',
                      'seaborn==0.9.0',
                      'SQLAlchemy==1.3.7',
                      'sqlparse==0.3.0',
                      'tables==3.5.2',
                      'urllib3==1.25.3',
                      'zipp==0.5.2'],
    extras_require={  # Optional
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },
    data_files=[('my_data', ['data//catalog_new.h5'])], 

)
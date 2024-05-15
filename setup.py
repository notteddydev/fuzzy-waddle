from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'A Python package for organising files by file type and naming them after their modification date.'
LONG_DESCRIPTION = 'Renames files after their modification date and stores them in directories named after their file extension. e.g. png/"1987-12-31 23.59.01"'

setup(
    name="fuzzywaddle",
    version=VERSION,
    author="notteddydev",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'fuzzywaddle']
)
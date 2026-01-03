#!/usr/bin/env python3
"""
Setup script for Lysmata
"""

from setuptools import setup, find_packages
import os

# Read the contents of README file
this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Read requirements
with open(os.path.join(this_directory, 'requirements.txt'), encoding='utf-8') as f:
    requirements = [line.strip() for line in f if line.strip() and not line.startswith('#')]

setup(
    name='lysmata',
    version='0.1.0',
    author='MR-NBD',
    author_email='albertoameglio@gmail.com',
    description='A smart contract fuzzer for Solidity',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/MR-NBD/lysmata',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'Topic :: Security',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    python_requires='>=3.8, <3.11',
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'lysmata=lysmata.main:main',
        ],
    },
    include_package_data=True,
    keywords='ethereum solidity fuzzing testing smart-contracts security',
    project_urls={
        'Bug Reports': 'https://github.com/MR-NBD/lysmata/issues',
        'Source': 'https://github.com/MR-NBD/lysmata',
    },
)

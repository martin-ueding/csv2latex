#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright © 2014 Martin Ueding <dev@martin-ueding.de>

from setuptools import setup, find_packages

setup(
    author="Martin Ueding",
    author_email="dev@martin-ueding.de",
    description="CSV to LaTeX converter",
    license="GPL2",
    classifiers=[
        "Environment :: Console",
        "Environment :: Plugins",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)",
        "Programming Language :: Python",
        "Topic :: Text Editors",
    ],
    name="csv2latex",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'csv2latex=csv2latex:main',
        ],
    },
    install_requires=[
    ],
    url="https://github.com/martin-ueding/csv2latex",
    download_url="http://martin-ueding.de/download/csv2latex/",
    version="1.0",
)

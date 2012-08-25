#-*- coding:utf-8 -*-

import setuptools
import tornadotest as pkg

pkgname = pkg.__name__

setuptools.setup(
    name=pkgname,
    version=pkg.__version__,
    packages=[pkgname],
    install_requires=[
        'tornado'
        ],
    author=pkg.__author__,
    entry_points=dict(
    console_scripts=[
            'ttest=tornadotest:main'
            ]),
    author_email='shoma.h4a+pypi@gmail.com',
    license=pkg.__license__,
    url='https://github.com/shomah4a/implicit',
    description='This module provides scala implicit conversion and implicit parameter mechanism for python.',
    long_description=pkg.__doc__,
    classifiers='''
Programming Language :: Python
Development Status :: 2 - Pre-Alpha
License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)
Programming Language :: Python :: 2
Programming Language :: Python :: 2.6
Programming Language :: Python :: 2.7
Topic :: Software Development :: Libraries :: Python Modules
Topic :: Utilities
'''.strip().splitlines())


#!/usr/bin/env python

from setuptools import setup
import sys

setup(
    name='soccer-cli',
    version='0.0.5.0',
    description='Soccer for Hackers.',
    author='Archit Verma',
    license='MIT',
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stablegit
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
    keywords = "soccer football espn scores live tool cli",
    author_email='architv07@gmail.com',
    url='https://github.com/architv/soccer-cli',
    packages=['soccer'],
    install_requires=[
        "click>=5.0",
        "requests==2.7.0"
    ] + (["colorama==0.3.3"] if "win" in sys.platform else []),
    entry_points = {
        'console_scripts': [
            'soccer = soccer.main:main'
      ],
    }
)

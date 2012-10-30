from setuptools import setup, find_packages
import sys
import os


here = os.path.abspath(os.path.dirname(__file__))
try:
    README = open(os.path.join(here, 'README.rst')).read()
except IOError:
    README = ''

setup(
    name='loud',
    version='0.1.2',
    description="Nose plugin for sound notification",
    long_description=README,
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Software Development :: Testing",
        "License :: OSI Approved :: MIT License",
    ],
    keywords='nose plugin testing audio',
    author='kusut',
    author_email='kusut@dahsy.at',
    url='http://github.com/kusut/loud',
    license='MIT',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    install_requires=["nose>=0.1.0"],
    entry_points={
        'nose.plugins.0.10': [
            'loud = loud:Loud'
        ]
    },
)

from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='loud',
      version=version,
      description="",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='kusut',
      author_email='kusut@dahsy.at',
      url='kusut.web.id',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=["nose>=0.1.0"],
      entry_points = {
          'nose.plugins.0.10': [
              'loud = loud:Loud'
              ]
          },

      )
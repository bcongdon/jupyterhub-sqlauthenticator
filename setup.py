#!/usr/bin/env python

from setuptools import setup

setup(name='sqlauthenticator',
      version='1.0',
      description='SQL Authenticator for Jupyterhub',
      author='Benjamin Congdon',
      license='MIT',
      author_email='bcongdo2@illinois.edu',
      url='https://github.com/bcongdon/jupyterhub-sqlauthenticator',
      packages=['sqlauthenticator'],
      install_requires=[
        'passlib',
        'PyMySQL',
        'jupyterhub',
      ],
      )

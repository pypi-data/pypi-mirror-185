Gutenberg Password Generator
============================

.. image:: https://img.shields.io/pypi/v/gutenbergPasswordGenerator
   :target: https://pypi.org/project/gutenbergPasswordGenerator/
   :alt: PyPI

.. image:: https://github.com/BobaFettyW4p/gutenbergPasswordGenerator/actions/workflows/pre-commit.yaml/badge.svg
   :target: https://github.com/BobaFettyW4p/gutenbergPasswordGenerator/actions/workflows/pre-commit.yaml
   :alt: Pre-Commit

.. image:: https://github.com/BobaFettyW4p/gutenbergPasswordGenerator/actions/workflows/pytest.yml/badge.svg
   :target: https://github.com/BobaFettyW4p/gutenbergPasswordGenerator/actions/workflows/pytest.yml
   :alt: PyTest

.. image:: https://img.shields.io/codecov/c/gh/BobaFettyW4p/gutenbergPasswordGenerator
   :target: https://app.codecov.io/github/BobaFettyW4p/gutenbergPasswordGenerator
   :alt: Codecov

This module leverages the `gutenbergpy <https://pypi.org/project/gutenbergpy/>`_ library to retreive the text
of classic novels from the Gutenberg Project, a collection of open-source ebooks. It then returns 5 secure password candidates
in a list

Installation
------------


.. code-block:: bash
   
   pip install gutenbergPasswordGenerator



To Use
------------

.. code-block:: bash

   import src.gutenbergPasswordGenerator
   src.gutenbergPasswordGenerator.generate_passwords()
   
   
Developing
----------
 
This project utilizes ``black`` and ``flake8`` to format and lint code, and leverages ``pre-commit`` for enforcement.
 
To configure your personal environment/commit hooks:

.. code-block:: bash
   
   pip install black flake8 pre-commit
   pre-commit install
   
Releases
--------

Releases are published whenever a tag is pushed to Github

.. code-block:: bash

   # set version number
   export RELEASE=x.x.x
   
   # create tags
   git commit --allow-empty -m "Release $RELEASE"
   git tag -a $RELEASE -m "Version $RELEASE
   
   # push
   git push upstream --tags

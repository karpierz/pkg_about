pkg_about
=========

Shares Python package metadata at runtime.

Overview
========

`PyPI record`_.

`Documentation`_.

TBD...

Usage
-----

TBD...

Installation
============

Prerequisites:

+ Python 3.7 or higher

  * https://www.python.org/
  * 3.7 is a primary test environment.

+ pip and setuptools

  * https://pypi.org/project/pip/
  * https://pypi.org/project/setuptools/

To install run:

  .. parsed-literal::

    python -m pip install --upgrade |package|

Development
===========

Prerequisites:

+ Development is strictly based on *tox*. To install it run::

    python -m pip install --upgrade tox

Visit `development page`_.

Installation from sources:

clone the sources:

  .. parsed-literal::

    git clone |respository| |package|

and run:

  .. parsed-literal::

    python -m pip install ./|package|

or on development mode:

  .. parsed-literal::

    python -m pip install --editable ./|package|

License
=======

  | Copyright (c) 2020-2022 Adam Karpierz
  | Licensed under the zlib/libpng License
  | https://opensource.org/licenses/Zlib
  | Please refer to the accompanying LICENSE file.

Authors
=======

* Adam Karpierz <adam@karpierz.net>

.. |package| replace:: pkg_about
.. |package_bold| replace:: **pkg_about**
.. |respository| replace:: https://github.com/karpierz/pkg_about.git
.. _development page: https://github.com/karpierz/pkg_about
.. _PyPI record: https://pypi.org/project/pkg_about/
.. _Documentation: https://pkg_about.readthedocs.io/

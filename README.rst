pkg_about
=========

Shares Python package metadata at runtime.

Overview
========

TBD...

`PyPI record`_.

`Documentation`_.

Usage
-----

TBD...

Installation
============

Prerequisites:

+ Python 3.10 or higher

  * https://www.python.org/

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

Visit `Development page`_.

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

  | |copyright|
  | Licensed under the zlib/libpng License
  | https://opensource.org/license/zlib
  | Please refer to the accompanying LICENSE file.

Authors
=======

* Adam Karpierz <adam@karpierz.net>

.. |package| replace:: pkg_about
.. |package_bold| replace:: **pkg_about**
.. |copyright| replace:: Copyright (c) 2020-2025 Adam Karpierz
.. |respository| replace:: https://github.com/karpierz/pkg_about.git
.. _Development page: https://github.com/karpierz/pkg_about
.. _PyPI record: https://pypi.org/project/pkg-about/
.. _Documentation: https://pkg-about.readthedocs.io/

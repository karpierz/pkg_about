pkg_about
=========

Unified access to Python package metadata at runtime.

Overview
========

Provides a unified way to retrieve Python package metadata at runtime,
regardless of the build backend or project structure.

| **about(package: str)** - retrieves metadata for the given package
| **about()** - retrieves metadata for the current package
| **about_from_setup()** - retrieves metadata from pyproject.toml
                           and/or setup.cfg

`PyPI record`_.

`Documentation`_.

Usage
-----

.. code:: python

  >>> import pkg_about
  >>> pkg_about.about("pip")
  >>> __uri__ == "https://pip.pypa.io/"
  True

Installation
============

Prerequisites:

+ Python 3.10 or higher

  * https://www.python.org/

+ pip

  * https://pypi.org/project/pip/

To install run:

  .. parsed-literal::

    python -m pip install --upgrade |package|

Development
===========

Prerequisites:

+ Development is strictly based on *nox*. To install it run::

    python -m pip install --upgrade nox

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

Sponsoring
==========

| If you would like to sponsor the development of this project, your contribution
  is greatly appreciated.
| As I am now retired, any support helps me dedicate more time to maintaining and
  improving this work.

`Donate`_

.. |package| replace:: pkg_about
.. |package_bold| replace:: **pkg_about**
.. |copyright| replace:: Copyright (c) 2020-2026 Adam Karpierz
.. |respository| replace:: https://github.com/karpierz/pkg_about
.. _Development page: https://github.com/karpierz/pkg_about
.. _PyPI record: https://pypi.org/project/pkg-about/
.. _Documentation: https://karpierz.github.io/pkg_about/
.. _Donate: https://www.paypal.com/donate/?hosted_button_id=FX8L7CJUGLW7S

# Copyright (c) 2020 Adam Karpierz
# SPDX-License-Identifier: Zlib

import unittest
import sys
from pathlib import Path
import textwrap

import pkg_about
from pkg_about._about import __get_copyright as get_copyright


class MainTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pyproject_path = Path(__file__).resolve().parent.parent/"pyproject.toml"
        if sys.version_info >= (3, 11):
            import tomllib
        else:  # pragma: no cover
            import tomli as tomllib
        with pyproject_path.open("rb") as file:
            metadata = tomllib.load(file).get("project", {})
        cls.version_expected = metadata["version"]
        version_parts = cls.version_expected.split(".")
        cls.version_major_expected = int(version_parts[0])
        cls.version_minor_expected = int(version_parts[1])
        cls.version_micro_expected = int(version_parts[2])

    def test_about(self):
        pkg_about.about("pkg_about")
        self.assertEqual(__title__, "pkg_about")
        self.assertEqual(__version__, self.version_expected)
        self.assertEqual(__version_info__.major, self.version_major_expected)
        self.assertEqual(__version_info__.minor, self.version_minor_expected)
        self.assertEqual(__version_info__.micro, self.version_micro_expected)
        self.assertEqual(__version_info__.releaselevel, "final")
        self.assertEqual(__version_info__.serial, 0)
        self.assertEqual(__summary__, "Shares Python package metadata at runtime.")
        self.assertEqual(__uri__, "https://pypi.org/project/pkg-about/")
        self.assertEqual(__author__, "Adam Karpierz")
        self.assertEqual(__email__, "adam@karpierz.net")
        self.assertEqual(__author_email__, "adam@karpierz.net")
        self.assertEqual(__maintainer__, "Adam Karpierz")
        self.assertEqual(__maintainer_email__, "adam@karpierz.net")
        self.assertEqual(__license__,
                         "zlib/libpng License ; https://opensource.org/license/zlib")
        self.assertEqual(__copyright__, "Copyright (c) 2020-2024 Adam Karpierz")

    def test_about_from_setup(self):
        pkg_about.about_from_setup(Path(__file__).resolve().parent.parent)
        self.assertEqual(about.__title__, "pkg_about")
        self.assertEqual(about.__version__, self.version_expected)
        self.assertEqual(about.__version_info__.major, self.version_major_expected)
        self.assertEqual(about.__version_info__.minor, self.version_minor_expected)
        self.assertEqual(about.__version_info__.micro, self.version_micro_expected)
        self.assertEqual(about.__version_info__.releaselevel, "final")
        self.assertEqual(about.__version_info__.serial, 0)
        self.assertEqual(about.__summary__, "Shares Python package metadata at runtime.")
        self.assertEqual(about.__uri__, "https://pypi.org/project/pkg-about/")
        self.assertEqual(about.__author__, "Adam Karpierz")
        self.assertEqual(about.__email__, "adam@karpierz.net")
        self.assertEqual(about.__author_email__, "adam@karpierz.net")
        self.assertEqual(about.__maintainer__, "Adam Karpierz")
        self.assertEqual(about.__maintainer_email__, "adam@karpierz.net")
        self.assertEqual(about.__license__,
                         "zlib/libpng License ; https://opensource.org/license/zlib")
        self.assertEqual(about.__copyright__, "Copyright (c) 2020-2024 Adam Karpierz")

    def test_get_copyright(self):
        self.assertEqual(get_copyright(textwrap.dedent(
            """
            License
            =======

              | |copyright|
              | Licensed under the zlib/libpng License
              | https://opensource.org/license/zlib
              | Please refer to the accompanying LICENSE file.

            .. |copyright| replace:: Copyright (c) 2020-2024 Adam Karpierz
            """)), "Copyright (c) 2020-2024 Adam Karpierz")
        self.assertEqual(get_copyright(textwrap.dedent(
            """
            License
            =======

              | Copyright (c) 2020-2024 Adam Karpierz
              | Licensed under the zlib/libpng License
              | https://opensource.org/license/zlib
              | Please refer to the accompanying LICENSE file.
            """)), "Copyright (c) 2020-2024 Adam Karpierz")

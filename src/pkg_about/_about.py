# Copyright (c) 2020 Adam Karpierz
# SPDX-License-Identifier: Zlib

__all__ = ('about', 'about_from_setup')


def about(package=None):
    import sys
    from packaging.version import parse as parse_version
    from importlib.metadata import metadata as get_metadata
    pkg_globals = sys._getframe(1).f_globals
    pkg_globals.pop("__builtins__", None)
    pkg_globals.pop("__cached__",   None)
    if package is None: package = pkg_globals["__package__"]
    metadata = get_metadata(package)
    version = parse_version(metadata["Version"])
    project_urls = {item.partition(",")[0].strip():
                    item.partition(",")[2].lstrip()
                    for item in metadata.get_all("Project-URL")}
    release_levels = __release_levels

    pkg_metadata = dict(
        __title__        = metadata["Name"],
        __version__      = str(version),
        __version_info__ = type("version_info", (), dict(
                                major=version.major,
                                minor=version.minor,
                                micro=version.micro,
                                releaselevel=release_levels[
                                    version.pre[0] if version.pre else
                                    "dev"   if version.dev   else
                                    "post"  if version.post  else
                                    "local" if version.local else
                                    "final"],
                                serial=(version.pre[1] if version.pre else
                                        version.dev or version.post
                                        or version.local or 0))),
        __summary__      = metadata.get("Summary"),
        __uri__          = (metadata.get("Home-page")
                            or project_urls.get("Home-page")
                            or project_urls.get("Homepage")
                            or project_urls.get("Home")),
        __author__       = metadata.get("Author"),
        __email__        = metadata.get("Author-email"),
        __author_email__ = metadata.get("Author-email"),
        __maintainer__       = metadata.get("Maintainer"),
        __maintainer_email__ = metadata.get("Maintainer-email"),
        __license__      = (metadata.get("License-Expression")
                            or metadata.get("License")),
        __copyright__    = metadata.get("Author"),
    )

    pkg_globals.update(pkg_metadata)
    pkg_globals["__all__"] = list(pkg_metadata.keys())


def about_from_setup(package_path=None):
    import sys
    from pathlib import Path
    from packaging.version import parse as parse_version
    try:
        from setuptools.config.setupcfg import (read_configuration as
                                                read_setupcfg)
    except ImportError:  # pragma: no cover
        from setuptools.config import read_configuration as read_setupcfg
    try:
        from setuptools.config.pyprojecttoml import (read_configuration as
                                                     read_pyprojecttoml)
    except ImportError:  # pragma: no cover
        read_pyprojecttoml = None
    pkg_globals = sys._getframe(1).f_globals
    package_path = (Path(pkg_globals["__file__"]).resolve().parents[1]
                    if package_path is None else Path(package_path))
    pyproject_path = package_path/"pyproject.toml"
    setup_cfg_path = package_path/"setup.cfg"
    metadata = {}
    if setup_cfg_path.exists():  # pragma: no branch
        metadata.update(read_setupcfg(setup_cfg_path,
                        ignore_option_errors=True).get("metadata", {}))
    if pyproject_path.exists():  # pragma: no branch
        if read_pyprojecttoml:
            metadata.update(read_pyprojecttoml(pyproject_path,
                            ignore_option_errors=True).get("project", {}))
        else:  # pragma: no cover
            if sys.version_info >= (3, 11):
                import tomllib
            else:
                import tomli as tomllib
            with pyproject_path.open("rb") as file:
                metadata.update(tomllib.load(file).get("project", {}))
    version = parse_version(metadata["version"])
    get, release_levels = __get, __release_levels

    class about:
        __slots__  = ()
        __module__ = None
        __title__        = metadata["name"]
        __version__      = str(version)
        __version_info__ = type("version_info", (), dict(
                                major=version.major,
                                minor=version.minor,
                                micro=version.micro,
                                releaselevel=release_levels[
                                    version.pre[0] if version.pre else
                                    "dev"   if version.dev   else
                                    "post"  if version.post  else
                                    "local" if version.local else
                                    "final"],
                                serial=(version.pre[1] if version.pre else
                                        version.dev or version.post
                                        or version.local or 0)))
        __summary__      = get(metadata, "description")
        __uri__          = (get(metadata, "urls", "Home-page")
                            or get(metadata, "urls", "Homepage")
                            or get(metadata, "urls", "Home")
                            or get(metadata, "url"))
        __author__       = (get(metadata, "authors", 0, "name")
                            or get(metadata, "author"))
        __email__        = (get(metadata, "authors", 1, "email")
                            or get(metadata, "author_email"))
        __author_email__ = (get(metadata, "authors", 1, "email")
                            or get(metadata, "author_email"))
        __maintainer__       = (get(metadata, "maintainers", 0, "name")
                                or get(metadata, "maintainer"))
        __maintainer_email__ = (get(metadata, "maintainers", 1, "email")
                                or get(metadata, "maintainer_email"))
        __license__      = (get(metadata, "license", "text")
                            or get(metadata, "license"))
        __copyright__    = (get(metadata, "authors", 0, "name")
                            or get(metadata, "author"))

    pkg_globals["about"] = about
    pkg_globals.setdefault("__all__", [])
    pkg_globals["__all__"].append("about")


def __get(mdata, *keys):
    for key in keys:
        if isinstance(mdata, dict):
            if key not in mdata:
                return None
        elif isinstance(mdata, (list, tuple)):
            if key >= len(mdata):  # pragma: no cover
                return None
        else:  # pragma: no cover
            return None
        mdata = mdata[key]
    return mdata


__release_levels = dict(
    a     = "alpha",
    b     = "beta",
    rc    = "candidate",
    dev   = "dev",
    post  = "post",
    local = "local",
    final = "final",
)

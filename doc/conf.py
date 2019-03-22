"""Sphinx configuration file for an LSST stack package.

This configuration only affects single-package Sphinx documentation builds.
"""

from documenteer.sphinxconfig.stackconf import build_package_configs
import lsst.example7


_g = globals()
_g.update(build_package_configs(
    project_name='example7',
    version=lsst.example7.version.__version__))

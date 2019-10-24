# Copyright (C) 2019 Eyal Shenitzky
# This program is free software; see LICENSE for more info.

"""
Erratum configuration loader.
The configuration file is loaded by erratacreator tool
The configuration file is a python module, providing these names:
    # Dictionary of configured errata projects.
    PROJECTS = {}
See example_conf.py example for more info.
"""

import imp
import os


def load_config(filename):
    """
    Load user configuration module.
    """
    basepath = os.path.splitext(filename)[0]
    module_dir, module_name = os.path.split(basepath)
    fp, pathname, description = imp.find_module(module_name, [module_dir])
    try:
        return imp.load_module(module_name, fp, pathname, description)
    finally:
        if fp:
            fp.close()

# Copyright (C) 2019 Eyal Shenitzky
# This program is free software; see LICENSE for more info.

from __future__ import absolute_import
from __future__ import division


class Error(Exception):
    """
    Base class for exceptions in this module.
    """

    def __init__(self, message):
        self.message = message


class ParameterError(Error):
    """
    Raised when there is a problem with given parameter
    """


class MissingProjectError(Error):
    """
    Raised required project configuration is missing
    """
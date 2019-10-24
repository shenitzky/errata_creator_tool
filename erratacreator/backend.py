# Copyright (C) 2019 Eyal Shenitzky
# This program is free software; see LICENSE for more info.

from __future__ import absolute_import
from __future__ import division


from errata_tool import Erratum

from erratacreator import config
from erratacreator import exceptions


class ConfiguredErratum:

    def __init__(self, config_file_path, project_name, release):
        """
        Create configured erratum.
        """
        self._config_file_path = config_file_path
        self._project_name = project_name
        self._release = release
        self._cfg = None

    @property
    def cfg(self):
        if self._cfg is None:
            cfg = config.load_config(self._config_file_path)
            if cfg is None:
                print("Couldn't find configuration file\n")
                raise exceptions.ParameterError("Couldn't find configuration file")

            project_cfg = cfg.PROJECTS.get(self._project_name)
            if project_cfg is None:
                print("Couldn't find project configuration\n")
                raise exceptions.MissingProjectError("Couldn't find project configuration")
            self._cfg = project_cfg
        return self._cfg

    def get_erratum(self):
        return Erratum(
            product=self.cfg.get('product'),
            release=self._release,
            topic=self.cfg.get('topic'),
            synopsis=self.cfg.get('synopsis'),
            description=self.cfg.get('description'),
            solution=self.cfg.get('solution'),
            qe_email=self.cfg.get('qe_email'),
            qe_group=self.cfg.get('qe_group'),
            owner_email=self.cfg.get('owner_email'),
            manager_email=self.cfg.get('manager_email'),
        )


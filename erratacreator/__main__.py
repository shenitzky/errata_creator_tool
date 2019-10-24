# Copyright (C) 2019 Nir Soffer
# This program is free software; see LICENSE for more info.

from __future__ import absolute_import
from __future__ import division

import argparse
from kerberos import GSSError

from six.moves import input

from erratacreator import backend


def main():
    parser = argparse.ArgumentParser(
        prog="erratacreator",
        description="Create errata for oVirt projects")
    parser.add_argument(
        "config_file_path",
        help="The path for the projects errata config file")
    parser.add_argument(
        "project_name",
        help="The required project name")
    parser.add_argument(
        "release",
        help="Required release version")
    parser.add_argument(
        "--debug",
        action="store_true",
        help="Enable debug mode")

    args = parser.parse_args()

    create_errata(args)


def create_errata(args):
    configured_erratum = backend.ConfiguredErratum(
        args.config_file_path,
        args.project_name,
        args.release
    )

    _update_erratum(configured_erratum)

    erratum = configured_erratum.get_erratum()

    if _confirm_creation(erratum):
        try:
            erratum.commit()
        except GSSError:
            print("Failed to commit new errata, "
                  "Unable to authenticate.\n"
                  "make sure you ran kinit before.")
        else:
            print(erratum.url() +
                  "\ndon't forget to add "
                  "related bugs and builds :)")


def _confirm_creation(erratum):
    print(erratum)
    res = input("Please confirm errata ['y'/'n']: ")

    if not res == 'y':
        print("Errata creation aborted!")
        return False
    return True


def _update_erratum(configured_erratum):
    fields_to_update = {
        'synopsis': None,
        'topic': None,
        'description': None,
        'solution': None,
    }

    for field in fields_to_update.keys():
        msg = ("Current errata " + field + " '"
               + configured_erratum.cfg.get(field) +
               "' please insert new " + field + " or 'n' to"
               " use the existing:\n")
        res = input(msg)

        if not res == 'n':
            fields_to_update[field] = res
        else:
            fields_to_update[field] = configured_erratum.cfg.get(field)

    configured_erratum.cfg['synopsis'] = fields_to_update['synopsis']
    configured_erratum.cfg['topic'] = fields_to_update['topic']
    configured_erratum.cfg['description'] = fields_to_update['description']
    configured_erratum.cfg['solution'] = fields_to_update['solution']

if __name__ == "__main__":
    main()

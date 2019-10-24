# errata creator

Helper for creating errata advisories.


## Overview

Errata creator tool will create advisory automatically according to a configuration file that written only once.

## Requirements

On Fedora / CentOS you need to install these packages:

    pip install errata_creator_tool


## Installing

Use pip:

    python3 -m pip install --user erratatool
    pip install requests-kerberos￼

Use python2 if you need to run on a distribution without python3.


## Before running

   run kinit

## Creating configuration file

The errata creator tool creates erratum based on configuration file that
you must provide.

The configuration module must define these names:

    # Errata configurations needed.
    PROJECTS = {}

See [example_config.py]


## Creating storage

To create the errata described in example_config.py, run:

    erratacreator example_config.py ioprocess 1.1

## Contributing

If you found a bug, please open an issue.

If you have an idea for improving this tool, please open an issue to
discuss the idea.

For trivial changes please send a pull request.

#!/usr/bin/env python3
"""
DocString
"""

__author__ = "EanNewton"
__version__ = "0.1.0"
__license__ = "AGPL-3.0"

import argparse
from os import path

from logzero import logger

from MuffaloBot import mbutil
from MuffaloBot.Data import constants


def setup(args):
    """ Main entry point of the app """
    logger.info("hello world")
    logger.info(args)


if __name__ == "__main__":
    """ This is executed when run from the command line """
    parser = argparse.ArgumentParser()

    # Required positional argument
    parser.add_argument("arg", help="Required positional argument")

    # Optional argument flag which defaults to False
    parser.add_argument("-f", "--flag", action="store_true", default=False)

    # Optional argument which requires a parameter (eg. -d test)
    parser.add_argument("-n", "--name", action="store", dest="name")

    # Optional verbosity counter (eg. -v, -vv, -vvv, etc.)
    parser.add_argument(
        "-v",
        "--verbose",
        action="count",
        default=0,
        help="Verbosity (-v, -vv, etc)")

    # Specify output of "--version"
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s (version {version})".format(version=__version__))

    args = parser.parse_args()
    setup(args)


def fetch_help(query: str) -> str:
    """
    Stringify the module help file.
    :type query: str
    """
    banner = mbutil.fetch_file('help', 'meta.txt')
    return banner


def fetch_license_full(query: str) -> str:
    """
    Stringify the full text of the software license.
    :type query: str
    """
    with open(path.join(constants.DEFAULT_DIR, './LICENSE'), 'r') as f:
        banner = f.read()
    return banner


def fetch_dontask(query: str) -> str:
    """
    Query the workshop by string.
    :type query: str
    """
    title = "**Don't ask to ask, just ask.**"
    url = 'http://sol.gfxile.net/dontask.html'

    banner = mbutil.fetch_file('pymb', 'dontask.txt')
    return banner


def fetch_about(query: str) -> str:
    """
    Query the workshop by string.
    :type query: str
    """
    banner = mbutil.fetch_file('pymb', constants.ABOUT_FILE)
    return banner


def fetch_license():
    return constants.LICENSE


def fetch_license_url():
    return constants.LICENSE_URL


def fetch_version():
    return constants.VERSION


def fetch_working_directory():
    return constants.DEFAULT_DIR


def fetch_roleid(query: str) -> str:
    """
    Query the workshop by string.
    :type query: str
    """
    banner = None
    return banner


def check_isimmortal(query: str) -> str:
    """
    Query the workshop by string.
    :type query: str
    """
    banner = None
    return banner


#
# [Command("isimmortal"), RequireOwner, Hidden]
# public
# Task
# IsImmortalAsync(CommandContext
# ctx)
# {
# return ctx.RespondAsync(Environment.GetCommandLineArgs().Any(s= > s == "-immortal").ToString());
# }


def self_update(query: str) -> str:
    """
    Query the workshop by string.
    :type query: str
    """
    banner = None
    constants.QUOTES_URL

    return banner


def self_restart(query: str) -> str:
    """
    Query the workshop by string.
    :type query: str
    """
    banner = None
    return banner

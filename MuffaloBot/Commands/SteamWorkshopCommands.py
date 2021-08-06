#!/usr/bin/env python3
"""
DocString
"""

__author__ = "EanNewton"
__version__ = "0.1.0"
__license__ = "AGPL-3.0"

import argparse

from logzero import logger
from steam.client import SteamClient, cdn

from MuffaloBot.Data import constants
from MuffaloBot.Modules.pmb_webhook import pmb_webhook_wshop


def wshop_latest():
    """
    Call the module to webhook post the most recent mods.
    :return:
    """
    pmb_webhook_wshop.pmb_hook()


def wshopmod(query: str) -> str:
    """
    Query the workshop by fileid or url.
    :type query: str
    """
    banner = None
    return banner


def wshopsearch(query: str) -> str:
    """
    Query the workshop by string.
    :type query: str
    """
    banner = None
    print(constants.ID_CODES['rimworld'])
    depot_info = SteamCDN_0.get_app_depot_info(constants.ID_CODES['rimworld'])
    print(depot_info)
    manifest = SteamCDN_0.get_manifests(constants.ID_CODES['rimworld'])
    # manifest = SteamCDN_0.get_manifest_for_workshop_item(id_RimWorld)
    print(manifest)
    return banner


def main(args=None):
    """ Main entry point of the app """
    logger.info("hello world")
    if args:
        logger.info(args)
    global SteamClient_0, SteamCDN_0
    SteamClient_0 = SteamClient()
    SteamCDN_0 = cdn.CDNClient(SteamClient_0)
    wshopsearch(None)


# https://steamcommunity.com/app/294100/workshop/


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
    if args:
        main(args)
    else:
        main()

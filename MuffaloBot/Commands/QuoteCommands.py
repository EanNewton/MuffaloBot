#!/usr/bin/env python3
"""
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using DSharpPlus;
using DSharpPlus.CommandsNext;
using DSharpPlus.CommandsNext.Attributes;
using MuffaloBot.Modules;
using Newtonsoft.Json;
using Newtonsoft.Json.Linq;

namespace MuffaloBot.Commands
{
    public class QuoteCommands
    {
        [Command("quotes"), Aliases("quote", "listquotes"), Description("List all the available quote commands.")]
        public async Task ListQuotesAsync(CommandContext ctx)
        {
            StringBuilder stringBuilder = new StringBuilder();
            stringBuilder.AppendLine("Listing all quotes:");
            JObject data = ctx.Client.GetModule<JsonDataModule>().data;
            foreach (var item in data["quotes"])
            {
                JProperty pair = (JProperty)item;
                stringBuilder.Append($"`{pair.Name}` ");
            }
            await ctx.RespondAsync(stringBuilder.ToString());
        }
    }
}

"""

__author__ = "EanNewton"
__version__ = "0.1.0"
__license__ = "AGPL-3.0"

import argparse

from logzero import logger


def main(args):
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
    main(args)


def wikisearch(query: str) -> str:
    """
    Searches the RimWorld wiki for content.
    :type query: str
    """
    queryAddress = "http://rimworldwiki.com/api.php?action=query&list=search&format=json&srlimit=5&srprop=size|wordcount|timestamp&srsearch={0}";

    banner = None
    return banner

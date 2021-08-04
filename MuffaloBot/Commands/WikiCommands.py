#!/usr/bin/env python3
"""
DocString
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

    #
    # public class WikiCommands
    # {
    #     const string queryAddress = "http://rimworldwiki.com/api.php?action=query&list=search&format=json&srlimit=5&srprop=size|wordcount|timestamp&srsearch={0}";
    #
    #     [Command("wikisearch"), Description("Searches the RimWorld wiki for content.")]
    #     public async Task Search(CommandContext ctx, [Description("The search query.")] string query)
    #     {
    #         await ctx.TriggerTypingAsync().ConfigureAwait(false);
    #         WebClient webClient = new WebClient();
    #         string result = await webClient.DownloadStringTaskAsync(string.Format(queryAddress, query)).ConfigureAwait(false);
    #         JObject jObject = JObject.Parse(result);
    #         DiscordEmbedBuilder builder = new DiscordEmbedBuilder();
    #         builder.WithTitle($"Results for '{query}'");
    #         builder.WithColor(DiscordColor.Azure);
    #         foreach (JToken token in jObject["query"]["search"])
    #         {
    #             builder.AddField(token["title"].ToString(),
    #                 $"**Info**\n{token["size"]} bytes\n" +
    #                 $"{token["wordcount"]} words\n" +
    #                 $"Last Edited UTC {DateTime.Parse(token["timestamp"].ToString())}\n" +
    #                 $"[Link](http://rimworldwiki.com/wiki/{token["title"].ToString().Replace(" ", "%20")})", true);
    #         }
    #         await ctx.RespondAsync(embed: builder.Build()).ConfigureAwait(false);
    #     }
    # }

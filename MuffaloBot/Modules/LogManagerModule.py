#!/usr/bin/env python3
"""
discordMessageCache = array of 1000 empty discord messages, for getting original message after discord edits it
setup
find index of id in cache
shallow copy discord message
on create log:
    push discord message cache w/ shallow copy
on delete log:
    notify mods of message being deleted
    discard cache entry
on modify log:
    notify mods
    deep copy and insert modified message
Discord Embed Builder

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


 # static DiscordEmbedBuilder MakeDeleteMessageEmbed(DiscordMessage message, string content)
 #        {
 #            content = content.Replace("`", "'");
 #            DiscordEmbedBuilder embedBuilder = new DiscordEmbedBuilder();
 #            embedBuilder.WithTitle("Message Deleted");
 #            embedBuilder.WithAuthor($"{message.Author.Username} #{message.Author.Discriminator}", null, message.Author.AvatarUrl);
 #            embedBuilder.WithColor(DiscordColor.Red);
 #            embedBuilder.WithDescription($"```\n{content}```");
 #            embedBuilder.AddField("ID", message.Id.ToString(), true);
 #            embedBuilder.AddField("Author ID", message.Author.Id.ToString(), true);
 #            embedBuilder.AddField("Channel", "#" + message.Channel.Name, true);
 #            embedBuilder.AddField("Timestamp (UTC)", message.Timestamp.ToUniversalTime().ToString(), true);
 #            IReadOnlyList<DiscordAttachment> attachments = message.Attachments;
 #            for (int i = 0; i < attachments.Count; i++)
 #            {
 #                embedBuilder.AddField($"Attachment {i + 1}", $"{attachments[i].FileName} ({attachments[i].FileSize}) {attachments[i].Url}", true);
 #            }
 #            return embedBuilder;
 #        }
 #        static DiscordEmbedBuilder MakeModifyMessageEmbed(DiscordMessage after, string content)
 #        {
 #            content = content.Replace("`", "'");
 #            string afterContent = after.Content?.Replace("`", "'");
 #            if (string.IsNullOrEmpty(afterContent))
 #            {
 #                afterContent = "(Empty)";
 #            }
 #            DiscordEmbedBuilder embedBuilder = new DiscordEmbedBuilder();
 #            embedBuilder.WithTitle("Message Modified");
 #            embedBuilder.WithAuthor($"{after.Author.Username} #{after.Author.Discriminator}", null, after.Author.AvatarUrl);
 #            embedBuilder.WithColor(DiscordColor.Yellow);
 #            embedBuilder.WithDescription($"Before```\n{content}```After```\n{afterContent}```");
 #            embedBuilder.AddField("ID", after.Id.ToString(), true);
 #            embedBuilder.AddField("Author ID", after.Author.Id.ToString(), true);
 #            embedBuilder.AddField("Channel", "#" + after.Channel.Name, true);
 #            embedBuilder.AddField("Timestamp (UTC)", after.Timestamp.ToUniversalTime().ToString(), true);
 #            IReadOnlyList<DiscordAttachment> attachments = after.Attachments;
 #            for (int i = 0; i < attachments.Count; i++)
 #            {
 #                embedBuilder.AddField($"Attachment {i + 1}", $"{attachments[i].FileName} ({attachments[i].FileSize}) {attachments[i].Url}", true);
 #            }
 #            return embedBuilder;

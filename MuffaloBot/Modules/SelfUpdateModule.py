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


# using DSharpPlus;
# using System;
# using System.Collections.Generic;
# using System.Linq;
# using System.Text;
# using System.Threading.Tasks;
# using Newtonsoft.Json;
# using Newtonsoft.Json.Linq;
# using System.Net.Http;
#
# namespace MuffaloBot.Modules
# {
#     public class JsonDataModule : BaseModule
#     {
#         public JObject data;
#         protected override void Setup(DiscordClient client)
#         {
#             Client = client;
#             ReloadDataAsync().ConfigureAwait(false).GetAwaiter().GetResult();
#             client.MessageCreated += HandleQuoteAsync;
#         }
#
#         private async Task HandleQuoteAsync(DSharpPlus.EventArgs.MessageCreateEventArgs e)
#         {
#             JToken quote = data["quotes"][e.Message.Content];
#             if (quote != null)
#             {
#                 await e.Message.RespondAsync(quote.ToString());
#             }
#         }
#
#         public async Task ReloadDataAsync()
#         {
#             HttpClient http = new HttpClient();
#             string result = await http.GetStringAsync("https://raw.githubusercontent.com/spdskatr/MuffaloBot/master/MuffaloBot/Data/data.json").ConfigureAwait(false);
#             JObject jObject = JObject.Parse(result);
#             data = jObject;
#         }
#     }
# }
# using DSharpPlus;
# using System;
# using System.Collections.Generic;
# using System.Diagnostics;
# using System.IO;
# using System.IO.Compression;
# using System.Linq;
# using System.Net.Http;
# using System.Text;
# using System.Threading.Tasks;
# using System.Xml;
#
# namespace MuffaloBot.Modules
# {
#     class XmlDatabaseModule : BaseModule
#     {
#         List<KeyValuePair<string, XmlDocument>> database = new List<KeyValuePair<string, XmlDocument>>();
#         public XmlDatabaseModule()
#         {
#             UpdateDatabaseAsync().ConfigureAwait(false).GetAwaiter().GetResult();
#         }
#
#         public async Task UpdateDatabaseAsync()
#         {
#             HttpClient client = new HttpClient();
#             using (MemoryStream memory = new MemoryStream(await client.GetByteArrayAsync("https://github.com/spdskatr/MuffaloBot/raw/master/MuffaloBot/Data/Defs.zip").ConfigureAwait(false)))
#             using (ZipArchive archive = new ZipArchive(memory))
#             {
#                 database = new List<KeyValuePair<string, XmlDocument>>(archive.Entries.Count);
#                 foreach (ZipArchiveEntry entry in archive.Entries)
#                 {
#                     if (entry.FullName.EndsWith(".xml"))
#                     {
#                         XmlDocument document = new XmlDocument();
#                         document.Load(entry.Open());
#                         database.Add(new KeyValuePair<string, XmlDocument>(entry.FullName, document));
#                     }
#                 }
#             }
#         }
#
#         public IEnumerable<KeyValuePair<string, XmlNode>> SelectNodesByXpath(string xpath)
#         {
#             return from KeyValuePair<string, XmlDocument> doc in database
#                    from XmlNode node in doc.Value.SelectNodes(xpath)
#                    select new KeyValuePair<string, XmlNode>(doc.Key, node);
#         }
#         public string GetSummaryForNodeSelection(string xpath)
#         {
#             StringBuilder stringBuilder = new StringBuilder();
#             Stopwatch sw = new Stopwatch();
#             sw.Start();
#             var results = SelectNodesByXpath(xpath).ToList();
#             sw.Stop();
#             foreach (var result in results.Take(5))
#             {
#                 stringBuilder.AppendLine($"<!-- In {result.Key}: -->");
#                 stringBuilder.AppendLine($"{result.Value.OuterXml.WithinChars(100)}\n");
#             }
#             stringBuilder.AppendFormat("<!-- Summary: Found {0} results total (showing first 5 if applicable) -->\n<!-- Evaluation time {1} ticks ({2}ms) -->", results.Count, sw.ElapsedTicks, sw.ElapsedMilliseconds);
#             return string.Concat("```xml\n", stringBuilder.ToString(), "```");
#         }
#
#         protected override void Setup(DiscordClient client)
#         {
#             Client = client;
#         }
#     }
# }

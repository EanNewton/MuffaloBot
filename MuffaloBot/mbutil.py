import functools
import os
from pathlib import Path
import aiohttp
import aiofiles
import discord
from MuffaloBot.Data.constants import VERBOSE, DEFAULT_DIR, PUBLIC_DIR, EXTSET


def suppress_channel_mentions(query: str) -> str:
    """
    Remove channel mentions from a Discord.message.contents string.
    :type query: str
    """
    queryAddress = "http://rimworldwiki.com/api.php?action=query&list=search&format=json&srlimit=5&srprop=size|wordcount|timestamp&srsearch={0}";

    banner = None
    return banner


def suppress_user_mentions(query: str) -> str:
    """
    Remove user mentions from a Discord.message.contents string.
    :type query: str
    """
    queryAddress = "http://rimworldwiki.com/api.php?action=query&list=search&format=json&srlimit=5&srprop=size|wordcount|timestamp&srsearch={0}";

    banner = None
    return banner


def suppress_role_mentions(query: str) -> str:
    """
    Remove role mentions from a Discord.message.contents string.
    :type query: str
    """
    queryAddress = "http://rimworldwiki.com/api.php?action=query&list=search&format=json&srlimit=5&srprop=size|wordcount|timestamp&srsearch={0}";

    banner = None
    return banner


def fetch_user_info(query: str) -> str:
    """
    Retrieve info about a Discord user.
    :type query: str
    """
    queryAddress = "http://rimworldwiki.com/api.php?action=query&list=search&format=json&srlimit=5&srprop=size|wordcount|timestamp&srsearch={0}";

    banner = None
    return banner


def fetch_channel_info(query: str) -> str:
    """
    Retrieve info about a Discord channel.
    :type query: str
    """
    queryAddress = "http://rimworldwiki.com/api.php?action=query&list=search&format=json&srlimit=5&srprop=size|wordcount|timestamp&srsearch={0}";

    banner = None
    return banner


def fetch_guild_info(query: str) -> str:
    """
    Retrieve info about a Discord guild.
    :type query: str
    """
    queryAddress = "http://rimworldwiki.com/api.php?action=query&list=search&format=json&srlimit=5&srprop=size|wordcount|timestamp&srsearch={0}";

    banner = None
    return banner


async def is_admin(author, message):
    """
	Check if a Discord user has been given bot admin permissions
    :param message:
	:param author: <Discord.message.author object>
	:return: <bool>
	"""

    if type(author) is discord.User and not author.bot:
        if author.id == 184474309891194880 or author.id == message.guild.owner_id:
            return True
        else:
            await author.send(content='Role based permissions are not currently supported by DiscordPy in private \
channels. Please try again in a different channel, or the guild owner can issue the command here.')
            return False
    else:
        try:
            if author.guild.owner_id == author.id or author.id == 184474309891194880:
                return True
        except Exception as e:
            if VERBOSE >= 2:
                print("Exception in is_admin: {}".format(e))
            else:
                pass
        try:
            for role in author.roles:
                if str(role).lower() in modRoles[author.guild.id]:
                    return True
        except Exception as e:
            if VERBOSE >= 2:
                print("Exception in is_admin: {}".format(e))
            else:
                pass
        return False


def wrap(s, w):
    """Break a long string s into a list of strings of length w"""
    return [s[i:i + w] for i in range(0, len(s), w)]


def debug(func):
    """Print the function signature and return value"""
    if VERBOSE >= 1:
        @functools.wraps(func)
        def wrapper_debug(*args, **kwargs):
            args_repr = [repr(a) for a in args]
            kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
            signature = ", ".join(args_repr + kwargs_repr)

            print(f"Calling {func.__name__}({signature})\n")
            value = func(*args, **kwargs)
            print(f"{func.__name__!r} returned {value!r}\n")

            return value

        return wrapper_debug
    else:
        return func


def fetch_file(directory, filename):
    """Safely read in a dynamically designated local file"""
    requested_path = '{}/docs/{}/{}.txt'.format(DEFAULT_DIR, directory, filename)
    check_path = os.path.commonprefix((os.path.realpath(requested_path), PUBLIC_DIR))
    if check_path == PUBLIC_DIR:
        with open(requested_path, 'r') as f:
            return f.read()


async def fetcher_engine(filetype, url, time, message):
    """
	Internal function to download any message attachments from Discord servers
	:param filetype: <String> The file extension
	:param url: <String> The file location URL
	:param time: <String> Current server time
	:param message: <Discord.message object>
	:return: <None>
	"""

    file_name = '{}_{}_{}'.format(message.author.name, time, url.split('/')[-1])
    Path('{}/log/{}/{}/{}'.format(
        DEFAULT_DIR, filetype, message.guild.name, message.channel.name)).mkdir(
        parents=True, exist_ok=True)
    file_path = '{}/log/{}/{}/{}/{}'.format(
        DEFAULT_DIR, filetype, message.guild.name, message.channel.name, file_name)

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status == 200:
                f = await aiofiles.open(file_path, mode='wb')
                await f.write(await resp.read())
                await f.close()
                if VERBOSE >= 1:
                    print("[+] Saved: {}".format(file_path))


async def fetch_embed(message, time):
    """
	Call fetcher() for each message.attachment
	:param message: <Discord.message object>
	:param time: <String> Current server time
	:return: <None>
	"""

    url = str(message.attachments[0].url)
    ext = str(url.split('.')[-1].lower())
    [await fetcher_engine(each, url, time, message) for each in EXTSET if ext in EXTSET[each]]

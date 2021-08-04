# url = "https://discordapp.com/api/webhooks/000000000000000000/xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

servers = {}


def add_server(name, webhook_url: str, wshop_ids: list):
    """
    Register a new server.
    :param name:
    :param webhook_url:
    :param wshop_ids:
    :return str:
    """
    servers[name] = [webhook_url, wshop_ids]
    return "[+] Server {} updated to:\n\tURL: {}\n\tIDs: {}".format(name, webhook_url, wshop_ids)

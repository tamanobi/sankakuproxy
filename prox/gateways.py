import requests


class SankakuError(Exception):
    pass


class SankakuAccessError(Exception):
    pass


def request_sankaku():
    try:
        res = requests.get("https://chan.sankakucomplex.com")
        res.raise_for_status()
    except requests.exceptions.HTTPError:  # noqa
        raise SankakuAccessError

    return res

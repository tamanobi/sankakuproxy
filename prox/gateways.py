import os

import requests


class SankakuError(Exception):
    pass


class SankakuAccessError(Exception):
    pass


def request_sankaku():
    try:
        res = requests.get(
            "https://chan.sankakucomplex.com",
            cookies=dict(
                login=os.environ["login"],
                pass_hash=os.environ["pass_hash"],
            ),
        )
        res.raise_for_status()
    except requests.exceptions.HTTPError:  # noqa
        raise SankakuAccessError

    return res

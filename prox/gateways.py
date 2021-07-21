from pathlib import Path

import requests


class SankakuError(Exception):
    pass


class SankakuAccessError(Exception):
    pass


def request_sankaku():
    tmp = Path(__file__).parent / Path("tmp")
    if not tmp.exists():
        tmp.mkdir()

    try:
        res = requests.get("https://chan.sankakucomplex.com")
        with open(tmp / "index.html", "w") as f:
            f.write(res.text)
        res.raise_for_status()
    except requests.exceptions.HTTPError:  # noqa
        raise SankakuAccessError

    return res

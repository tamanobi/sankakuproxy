from pathlib import Path

import requests
import os
from bs4 import BeautifulSoup


class SankakuError(Exception):
    pass


class SankakuAccessError(Exception):
    pass


def request_sankaku():
    tmp = Path(__file__).parent / Path("tmp")
    if not tmp.exists():
        tmp.mkdir()

    try:
        res = requests.get("https://chan.sankakucomplex.com", cookies=dict(login=os.environ["login"], pass_hash=os.environ["pass_hash"],))
        with open(tmp / "index.html", "w") as f:
            soup = BeautifulSoup(res.text, "html.parser")
            f.write(soup.prettify())
        res.raise_for_status()
    except requests.exceptions.HTTPError:  # noqa
        raise SankakuAccessError

    return res

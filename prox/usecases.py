from pathlib import Path
from urllib import parse
from urllib.parse import urlparse

from bs4 import BeautifulSoup

from gateways import request_sankaku, requst_sankaku_image


def _make_cache(text: str) -> None:
    tmp = Path(__file__).parent / Path("tmp")
    if not tmp.exists():
        tmp.mkdir()
    with open(tmp / "index.html", "w") as f:
        f.write(text)


def get_list(page: int) -> list:
    res = request_sankaku(page)
    soup = BeautifulSoup(res.text, "html.parser")
    _make_cache(soup.prettify())
    soup.select("span.thumb")

    return [
        {
            "href": "https://chan.sankakucomplex.com" + thumb.find("a").get("href"),
            "src": "https:" + thumb.find("img").get("src"),
            "tags": thumb.find("img").get("title").split(" "),
        }
        for thumb in soup.select("span.thumb")
    ]


def get_image(path: str):
    parsed = urlparse(path)
    assert parsed.netloc.startswith("s.sankakucomplex.com")
    assert "e=" in parsed.query and "m=" in parsed.query
    res = requst_sankaku_image(parsed.path, parsed.query)
    return res.content, res.headers["content-type"]

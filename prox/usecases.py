from pathlib import Path
from urllib.parse import urlparse

from bs4 import BeautifulSoup

from dataclasses import dataclass
from gateways import request_sankaku, requst_sankaku_image

@dataclass(frozen=True)
class HrefSrc:
    href: str
    src: str


def get_list(page: int) -> list:
    html = request_sankaku(page)
    soup = BeautifulSoup(html, "lxml", from_encoding="utf-8")

    return [
        HrefSrc(href="https://chan.sankakucomplex.com" + thumb.find("a").get("href"), src="https:" + thumb.find("img").get("src"))
        for thumb in soup.select("span.thumb")
        if "no-visibility.svg" not in thumb.find("img").get("src")
    ]


def get_image(path: str):
    parsed = urlparse(path)
    assert parsed.netloc.startswith("s.sankakucomplex.com")
    assert "e=" in parsed.query and "m=" in parsed.query
    res = requst_sankaku_image(parsed.path, parsed.query)
    return res.content, res.headers["content-type"]

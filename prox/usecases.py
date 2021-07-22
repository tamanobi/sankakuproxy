from pathlib import Path

from bs4 import BeautifulSoup

from gateways import request_sankaku


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

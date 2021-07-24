import logging
import os

import requests

logger = logging.getLogger(__file__)


class SankakuError(Exception):
    pass


class SankakuAccessError(Exception):
    pass


class RequestSankakuGetList:
    def __init__(self) -> None:
        pass

    def get(self, page: int):
        pass

    def postprocess(self):
        pass

    def exec(self, page: int) -> str:
        return self.postprocess(self.get(page))


def request_sankaku(page: int) -> str:
    try:
        res = requests.get(
            "https://chan.sankakucomplex.com/post/index.content",
            cookies=dict(
                login=os.environ["login"],
                pass_hash=os.environ["pass_hash"],
            ),
            params={
                "page": page,
                "tags": "loli threshold:3",
            },
            headers={
                "user-agent": "user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36",  # noqa
            }
        )
        res.raise_for_status()
    except requests.exceptions.HTTPError as e:  # noqa
        logger.error(e)
        raise SankakuAccessError(e)

    return res.text.replace("</head>", "")


def requst_sankaku_image(path: str, query: str):
    try:
        res = requests.get(
            "https://s.sankakucomplex.com" + path,
            cookies=dict(
                login=os.environ["login"],
                pass_hash=os.environ["pass_hash"],
            ),
            params=query,
            headers={
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",  # noqa
                "user-agent": "user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36",  # noqa
            },
        )
        res.raise_for_status()
    except requests.exceptions.HTTPError:  # noqa
        raise SankakuAccessError

    return res

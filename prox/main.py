import requests
from fastapi import FastAPI

app = FastAPI()


class SankakuError(Exception):
    pass


class SankakuAccessError(Exception):
    pass


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/sankaku")
def sankaku():
    try:
        res = requests.get("https://chan.sankakucomplex.com")
        res.raise_for_status()
    except requests.exceptions.HTTPError:  # noqa
        raise SankakuAccessError

    return {"status": res.status_code}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

from fastapi import FastAPI

from gateways import request_sankaku

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/sankaku")
def sankaku():
    res = request_sankaku()
    return {"status": res.status_code}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

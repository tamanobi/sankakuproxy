from fastapi import FastAPI

from usecases import get_list

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/sankaku")
def sankaku():
    res = get_list()
    return {"body": res}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

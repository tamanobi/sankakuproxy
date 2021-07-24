import io

from fastapi import FastAPI
from starlette.responses import StreamingResponse

from usecases import get_image, get_list

app = FastAPI()


@app.get("/sankaku")
def sankaku(page: int = 1):
    res = get_list(page)
    return {"body": res}


@app.get("/image")
def image(path: str):
    res, content_type = get_image(path)
    return StreamingResponse(io.BytesIO(res), media_type=content_type, headers={"Cache-Control": "must-revalidate,no-cache,public,max-age=60"})

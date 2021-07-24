import io
import os

import sentry_sdk
from fastapi import FastAPI
from sentry_sdk.integrations.asgi import SentryAsgiMiddleware
from starlette.responses import StreamingResponse

from usecases import get_image, get_list

app = FastAPI()
sentry_dns = os.environ.get("SENTRY_DSN")
if sentry_dns:
    sentry_sdk.init(sentry_dns, environment=os.environ.get("APP_ENV", "local"))
app.add_middleware(SentryAsgiMiddleware)


@app.get("/")
def top():
    import requests

    res = requests.get("https://chan.sankakucomplex.com/post/index.content")
    return {"body": res.text}


@app.get("/")
def echo():
    import requests

    res = requests.get("https://ipecho.net/plain")
    return {"body": res.text}


@app.get("/sankaku")
def sankaku(page: int = 1):
    res = get_list(page)
    return {"body": res}


@app.get("/image")
def image(path: str):
    res, content_type = get_image(path)
    return StreamingResponse(
        io.BytesIO(res),
        media_type=content_type,
        headers={"Cache-Control": "must-revalidate,no-cache,public,max-age=60"},
    )

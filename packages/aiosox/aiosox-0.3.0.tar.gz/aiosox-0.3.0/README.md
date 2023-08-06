![Sample image](https://gitlab.com/uploads/-/system/project/avatar/42327849/a5e01db694b47cd07018813ce821a4e1.png?width=64)


aiosox: <a href="https://gitlab.com/arieutils/aiosox">repo link </a>
=======================================
Quick example
-----------

can be installed using pip/poetry:

    poetry shell
     
    poetry run uvicorn example:app --port=8001
    
```python
from typing import List

from fastapi import FastAPI
from pydantic import BaseModel

from aiosox import SioAuth, SioNamespace, SocketIoServer


def get_app():
    applitcation = FastAPI(title="tester")
    return applitcation


app = get_app()

sio_server: SocketIoServer = SocketIoServer(app=app, kafka_url="localhost:29092")
user_namespapce: SioNamespace = SioNamespace("/user", socket_io_server=sio_server)
sio_server._sio.register_namespace(user_namespapce)


@app.on_event("startup")
async def on_start():
    await sio_server.start()


@app.on_event("shutdown")
async def on_shutdown():
    await sio_server.shutdown()


class UserY(BaseModel):
    name: str


class UserT(BaseModel):
    name: str
    what: List[UserY]


class OfferT(BaseModel):
    title: str


on_failed_emmiter = user_namespapce.create_emitter("failed", model=OfferT | UserT)


@user_namespapce.on(
    "submit",
    description="when user submits a form",
    payload_model=UserT | UserY,
    response_model=List[UserT],
    auth=SioAuth.jwt,
)
async def on_submit(sid, data):
    print(
        sid,
        data,
    )

```
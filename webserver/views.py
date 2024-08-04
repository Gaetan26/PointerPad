

from .server import app
from quart import websocket
from quart import render_template

import asyncio, os, socket
from remote import remote



@app.get('/')
async def index() -> object:
    return await render_template('remote_view.html', host=os.getlogin(), name=socket.gethostname())


async def receive() -> None:
    while True:
        keycode = await websocket.receive()
        app.add_background_task(remote.execute, keycode)


@app.websocket('/remote')
async def remote_ws() -> None:
    try:
        await websocket.accept()
        print("un controller se connecter!")
        await receive()
    except asyncio.CancelledError:
        print("un controller se deconnecter!")
#!/usr/bin/env python3
from quart import Quart
from hypercorn.config import Config
from hypercorn.asyncio import serve
from python_quart_tryout.api import api
import asyncio

config = Config()
config.bind = ["0.0.0.0:8080"]

app = Quart(__name__)
app.register_blueprint(api)

def run() -> None:
    asyncio.run(serve(app, config))

if __name__ == '__main__':
    run()
#!/usr/bin/env python3
from quart import Quart, jsonify
from hypercorn.config import Config
from hypercorn.asyncio import serve
import asyncio

config = Config()
config.bind = ["0.0.0.0:8080"]

app = Quart(__name__)

@app.route("/api")
async def json():
    return jsonify({"hello": "world"})

if __name__ == "__main__":
    asyncio.run(serve(app, config))
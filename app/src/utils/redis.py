#!/usr/bin/env python3.9.5
# -*- coding:utf-8 -*-

'''
@author：gladlys
@date：2022/12/12 13:50
@filename: redis.py
@software: PyCharm
@version: Python 3.9.5
'''

from aioredis import create_redis_pool, Redis
from fastapi import FastAPI

app = FastAPI()


async def get_redis_pool() -> Redis:
    redis = await create_redis_pool(f"redis://:@127.0.0.1:6379/0?encoding=utf-8")
    return redis


@app.on_event("startup")
async def startup_event():
    app.state.redis = await get_redis_pool()


@app.on_event("shutdown")
async def shutdown_event():
    app.state.redis.close()
    await app.state.redis.wait_closed()

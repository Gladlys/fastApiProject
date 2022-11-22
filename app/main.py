from random import randint

import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

import src.routers

app = FastAPI()

origins = [
    "http://api.zwnsyw.com",
    "https://api.zwnsyw.com",
    "http://localhost",
    "http://localhost:8080",
    "*"
]
# 设置跨域
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/get")
async def get_num():
    return randint(1, 10)


if __name__ == '__main__':
    uvicorn.run(app='main:app',
                host='0.0.0.0',
                port=8080,
                reload=True,
                # debug=True,
                workers=1,
                )

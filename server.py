from typing import Union

from fastapi import FastAPI

app = FastAPI()

static_dir = "static"
app.mount("/", StaticFiles(directory=static_dir), name="static")

@app.get("/api")
def read_root():
    return {"Hello": "World"}
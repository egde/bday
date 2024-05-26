from typing import Union

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()

static_dir = "static"
app.mount("/", StaticFiles(directory=static_dir), name="static")

# Serve the index.html file when accessing the root URL
@app.get("/")
async def read_root():
    index_path = os.path.join(static_dir, "index.html")
    return FileResponse(index_path)
    
@app.get("/api")
def read_root():
    return {"Hello": "World"}
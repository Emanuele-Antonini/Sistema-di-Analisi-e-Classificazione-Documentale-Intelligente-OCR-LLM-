from fastapi import FastAPI, File, UploadFile 

from pydantic import BaseModel

import fitz

from Api.router_api import router as router_api_router

class Item(BaseModel):

    name: str

    description: str = None

    price: float

    tax: float = None


class Documents(BaseModel):

    title: str

    content:str

    description: str = None


app = FastAPI()

app.include_router(router_api_router, prefix="/Api/v1", tags=["RouterApi"])


@app.get("/")

def read_root():

    return {"FastApi": "Starting... Server Iniziato e Modulare "}

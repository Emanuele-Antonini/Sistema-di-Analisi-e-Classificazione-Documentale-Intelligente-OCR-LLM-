from contextlib import asynccontextmanager

from fastapi import FastAPI, File, UploadFile 

from pydantic import BaseModel

import fitz

from api.router_api import router as router_api_router

from db.connection import connet_to_database, close_connection_to_database

class Item(BaseModel):

    name: str

    description: str = None

    price: float

    tax: float = None


class Documents(BaseModel):

    title: str

    content:str

    description: str = None

@asynccontextmanager
async  def lifespan(app: FastAPI):
    # Code to run on startup
    print("Starting up...")

    await connet_to_database()

    yield
    # Starting Database connection

    # Code to run on shutdown
    print("Shutting down...")

    await close_connection_to_database()


app = FastAPI(lifespan=lifespan)

app.include_router(router_api_router, prefix="/Api/v1", tags=["RouterApi"])

@app.get("/")

def read_root():

    return {"FastApi": "Starting... Server Iniziato e Modulare "}

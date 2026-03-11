from fastapi import APIRouter, File, UploadFile 

from pydantic import BaseModel

from db.queries_api import do_insert, do_find, do_update

import fitz

# Separation of Concerns: the code is separated into different files based on their functionality and type of concerns.

router = APIRouter()

class Item(BaseModel):

    name: str

    description: str = None

    price: float

    tax: float = None


class Documents(BaseModel):

    title: str

    content:str

    description: str = None

@router.get("/items/{item_id}")

def read_item(item_id: int, q: str = None):

    return {"item_id": item_id, "q": q}


@router.put("/items/{item_id}")

def update_item(item_id: int, item: Item):

    return {"item_name": item.name,"item_price": item.price, "item_id": item_id, "item_description": item.description, "item_tax": item.tax}



# Document Endpoints

# The following endpoints are for handling document-related operations such as inserting, reading, and updating documents.

# Inserting new documents call a method that uses the POST HTTP method and create an istance inside MongoDB, while the reading 
# and updating documents call methods that use the GET and PUT HTTP methods respectively, and they return a sample document or 
# update an existing document based on the provided document ID.
#document: Documents,

@router.post("/test_database/")

async def test_database_connection():
    
    # Here you can add the code to test the database connection using the do_find() function.
     
    dati_finti = {
        "nome_file": "fattura_spese_2023.pdf",
        "tipologia": "Fattura",
        "testo_estratto": "Questo è un test di OCR e YOLO...",
        "stato": "Elaborato"
    } 


    nuovoid = await do_insert(dati_finti)

    return {
        "message": "Database connection tested successfully", 
        "test_result": nuovoid
    }   


@router.post("/documents/")

async def insert_document( file: UploadFile = File(...)):
    
       if file.content_type != "application/pdf":
        return {"error": "Only PDF files are allowed."}
       
       raw_byte = await file.read()

       documento = fitz.open(stream=raw_byte, filetype="pdf")

       # Here you can add the code to insert the document into the database using the do_insert() function.
       
       #await do_insert()

       #"id_assegnato": nuovo_id,"title": document.title, "content": document.content, "description": document.description
       return {"messaggio": "Document inserted successfully", "file_name": file.filename, "file_size": len(raw_byte), "file_type": file.content_type}

@router.get("/documents/{document_id}")

def read_document(document_id: int):

    return {"title": "Sample Document", "content": "This is a sample document.", "description": "This document is used for testing."}

@router.put("/documents/{document_id}")

def update_document(document_id: int, document: Documents):

    return {"document_id": document_id, "title": document.title, "content": document.content, "description": document.description}  


# The main goal of Test Driven Domain is to decoupling responsibilities in the global domain
# we find 3 distinct responsibilities and simplifying abstraction to obtain less coupling from
# different class domain, we want separate what we want to do from how to do it

# main goal is to isolate the main logic of the central domain class and so every responsability 
# that has been divided can be translated into a core function, in this way it's possible to implement
# the decoupling mechanism to divide the layer, instead to test the core function with high level of 
# coupling it's useful for testing edge to edge combined with Dependency Injection
import uuid
from typing import List, Dict, Any
from db.mongo_adapter import AbstractRepository

class TestAdapter(AbstractRepository):
    
    def __init__(self):
        self.collection : List[Dict[str, Any]] = []

    async def add(self, document: dict) -> str:
        # Simuliamo la creazione di un ID da parte del database
        doc_id = str(uuid.uuid4())
        document_copy = document.copy()
        document_copy["_id"] = doc_id
        
        self._collection.append(document_copy)
        return doc_id

    async def get(self, query: dict) -> dict:
        # Simuliamo una ricerca di base. Controlla se le chiavi/valori 
        # della query corrispondono a un documento nella nostra lista.
        for document in self._collection:
            match = all(document.get(k) == v for k, v in query.items())
            if match:
                return document
        return None

    async def update(self, query: dict, update_data: dict) -> int:
        # Troviamo il documento ed eseguiamo l'aggiornamento
        document = await self.get(query)
        if document:
            document.update(update_data)
            return 1 # Simuliamo il modified_count di MongoDB
        return 0
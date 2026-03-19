from motor.motor_asyncio import AsyncIOMotorDatabase
from abstract_db import AbstractRepository

class MongoRepository(AbstractRepository):
    
    # Iniettiamo l'oggetto database nel costruttore
    def __init__(self, database: AsyncIOMotorDatabase, collection_name: str):
        self.collection = database[collection_name]

    async def add(self, document: dict) -> str:
        result = await self.collection.insert_one(document)
        return str(result.inserted_id)

    async def get(self, query: dict) -> dict:
        return await self.collection.find_one(query)

    async def update(self, query: dict, update_data: dict) -> int:
        result = await self.collection.update_one(query, {"$set": update_data})
        return result.modified_count
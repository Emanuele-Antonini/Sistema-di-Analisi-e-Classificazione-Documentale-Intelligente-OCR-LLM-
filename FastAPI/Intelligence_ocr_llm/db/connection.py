from motor.motor_asyncio import AsyncIOMotorClient

#from motor import motor_tornado

class DataBase:
    
    client: AsyncIOMotorClient = None


db = DataBase()     
       
async def connet_to_database():
    
     uri = "mongodb://localhost:27017/mydatabase"
     db.client = AsyncIOMotorClient(uri)
     print("Connection to database established with success")

async def close_connection_to_database():
   if db.client is not None:
     db.client.close()     
     print("Connection to database closed with success")
   
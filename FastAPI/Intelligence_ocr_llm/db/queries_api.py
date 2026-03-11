from motor.motor_asyncio import AsyncIOMotorClient

from db.connection import db 

DATABASE_NAME="database_name"
COLLECTION_NAME="collection_name"


def get_database():
     
     return db.client[DATABASE_NAME][COLLECTION_NAME]   


async def do_insert(documents: dict):
    document= {"key": "value"}
    collection = get_database()
    result = await collection.insert_one(documents)
    print("result %s" %repr(result.inserted_id))

    return str(result.inserted_id)


async def do_find():
     collection = get_database()
     document = await collection.find_one({"key": "value"})
     print("result %s" %repr(document))



async def do_update():
     collection = get_database()
     result = await collection.update_one({"key": "value"}, {"$set": {"key": "new_value"}})
     print("result %s" %repr(result.modified_count))
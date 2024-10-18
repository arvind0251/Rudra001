from typing import Dict, Union

from motor.motor_asyncio import AsyncIOMotorClient as MongoCli

from config import MONGO_DB_URI

mongo = MongoCli(MONGO_DB_URI)
db = mongo.TanuMusic

async def add_wlcm(chat_id: int):
    return await wlcm.insert_one({"chat_id": chat_id})

# Function to remove a welcome document
async def rm_wlcm(chat_id: int):   
    chat = await wlcm.find_one({"chat_id": chat_id})
    if chat: 
        return await wlcm.delete_one({"chat_id": chat_id})




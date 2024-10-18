from async_pymongo import AsyncClient
from config import MONGO_DB_URI

# Define the database name
DBNAME = "TANUMUSIC"

# Initialize the MongoDB client
mongo = AsyncClient(MONGO_DB_URI)
dbname = mongo[DBNAME]

# Define the collection
wlcm = dbname["welcome"]

# Function to add a welcome document
async def add_wlcm(chat_id: int):
    return await wlcm.insert_one({"chat_id": chat_id})

# Function to remove a welcome document
async def rm_wlcm(chat_id: int):   
    chat = await wlcm.find_one({"chat_id": chat_id})
    if chat: 
        return await wlcm.delete_one({"chat_id": chat_id})
from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv
load_dotenv()


MONGODB_URL = os.getenv("MONGODB_URL")  
client = AsyncIOMotorClient(MONGODB_URL)
print(MONGODB_URL)


# Connect to your DB and collection
db = client["Ai_pdf"]  # Choose your database name
pdf_collection = db["summ"]  # Choose your collection name

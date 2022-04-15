from pyrogram import Client
import os
from config import API_ID, API_HASH, BOT_TOKEN

pyrogram = Client
    "PYROGRAM MATCH"
    api_id=API_ID, 
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="plugins")
)

pyrogram.run()   
    

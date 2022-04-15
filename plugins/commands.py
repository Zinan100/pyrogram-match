from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant

Force = "M_E_UPDATEZ"

@Client.on_message(filters.command("start"))
async def start_msg(bot, msg):
    

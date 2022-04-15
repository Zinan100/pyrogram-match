import asyncio
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton 
from pyrogram.types import CallbackQuery


@Client.on_callback_query()
async def callback(bot, msg):
    if msg.data == "start":
        reply1 = await query.message.reply_text(
            text="⭗ ⭗ ⭗ ⭗ ⭗ ⭗"
        )
        await asyncio.sleep(0.5)
        reply2 = await reply1.edit_text(
            text="⦿ ⭗ ⭗ ⭗ ⭗ ⭗"
        )
        await asyncio.sleep(0.5)
        reply3 = await reply2.edit_text(
            text="⦿ ⦿ ⭗ ⭗ ⭗ ⭗"
        )
        await asyncio.sleep(0.5)
        reply4 = await reply3.edit_text(
            text="⦿ ⦿ ⦿ ⭗ ⭗ ⭗"
        )
        await asyncio.sleep(0.5)
        reply5 = await reply4.edit_text(
            text="⦿ ⦿ ⦿ ⦿ ⭗ ⭗"
        )
        await asyncio.sleep(0.5)
        reply6 = await reply5.edit_text(
            text="⦿ ⦿ ⦿ ⦿ ⦿ ⭗"
        )
        await asyncio.sleep(0.5)
        reply7 = await reply6.edit_text(
            text="⦿ ⦿ ⦿ ⦿ ⦿ ⦿"
        )
        await reply7.delete()

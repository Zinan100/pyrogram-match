from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant
import random
import asyncio
import datetime
import pytz


Force = "M_E_UPDATEZ"


@Client.on_message(filters.command("start"))
async def start_msg(bot, msg):
    if Force:
        try:
            user = await bot.get_chat_member(Force, msg.from_user.id)
            if user.status == "kicked out":
                await msg.reply_text("yᴏᴜ ᴀʀᴇ ʙᴀɴɴᴇᴅ ꜰʀᴏᴍ ᴛɢᴇ ᴄʜᴀɴɴᴇʟ")
                return
        except UserNotParticipant:
          await msg.reply_text(
              text="yᴏᴜ ᴅɪᴅɴᴛ ꜱᴜʙᴇᴅ ᴍy ᴄʜᴀɴɴᴇʟ ꜱᴜʙꜱᴄʀɪʙᴇᴇᴅ ᴍy ᴄʜᴀɴɴᴇʟ",
              reply_markup=InlineKeyboardMarkup( [[
                  InlineKeyboardButton("ᴜᴩᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ 📢", url=f"t.me/{Force}")
                 ]]
                 )
          )
          return
    await msg.reply_chat_action("typing")
    await asyncio.sleep(1)
    now = datetime.datetime.now()
    tz = pytz.timezone('asia/kolkata')
    your_now = now.astimezone(tz)
    hour = your_now.hour
    if 0 <= hour <12:
        get = "Gᴏᴏᴅ ᴍᴏʀɴɪɴɢ"
    elif 12 <= hour <17:
        get = 'Gᴏᴏᴅ ᴀꜰᴛᴇʀɴᴏᴏɴ'
    else:
        get = 'Gᴏᴏᴅ ᴇᴠᴇɴɪɴɢ'
    await msg.reply_photo(
        photo="https://telegra.ph/file/3b50378837115d65e9197.jpg",
        caption="Hi {message.from_user.mention} {get} I Aᴍ Rᴇx Yᴏᴜ Cᴀɴ Usᴇ Mᴇ Sɪᴍᴘʟʏ Nᴏ Usᴇ Aɴᴅ I Wɪʟʟ Bᴇ A Hᴜɢᴇ Bᴏᴛ Oɴᴇ Dᴀʏ Wᴀɪᴛ Fᴏʀ Tʜᴀᴛ Dᴀʏ",        
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("Hᴇʟᴩ", callback_data="help")
            ],[
            InlineKeyboardButton("Aʙᴏᴜᴛ", callback_data="abou")
           ]]
           )
    )

    

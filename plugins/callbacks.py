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
        await msg.message.edit(
            text="I Aᴍ Rᴇx Yᴏᴜ Cᴀɴ Usᴇ Mᴇ Sɪᴍᴘʟʏ Nᴏ Usᴇ Aɴᴅ I Wɪʟʟ Bᴇ A Hᴜɢᴇ Bᴏᴛ Oɴᴇ Dᴀʏ Wᴀɪᴛ Fᴏʀ Tʜᴀᴛ Dᴀʏ",
            reply_markup=InlineKeyboardMarkup( [[
                InlineKeyboardButton("Hᴇʟᴩ", callback_data="help")
                ],[
                InlineKeyboardButton("Aʙᴏᴜᴛ", callback_data="abou")
               ]]
               )
        )

    elif msg.data == "abou":
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
        await asyncio.sleep(0.5)
        await reply7.delete()
        await msg.message.edit(
            text="""<b>✮ 𝙼𝚈 𝙽𝙰𝙼𝙴: 𝚁𝙴𝚇
✮ 𝙲𝚁𝙴𝙰𝚃𝙾𝚁: 𝚉𝙸𝙽𝙰𝙽
✮ 𝚂𝙿𝙴𝙲𝙸𝙰𝙻 𝚃𝙷𝙰𝙽𝙺𝚂 𝚃𝙾: <a href=https://t.me/Mo_Tech_YT>𝙼𝙾 𝚃𝙴𝙲𝙷</a>
✮ 𝙻𝙸𝙱𝚁𝙰𝚁𝚈: 𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼
✮ 𝙻𝙰𝙽𝙶𝚄𝙰𝙶𝙴: 𝙿𝚈𝚃𝙷𝙾𝙽 𝟹</b>""",
            reply_markup=InlineKeyboardMarkup( [[
                InlineKeyboardButton("Bᴀᴄᴋ", callback_data="start")
               ]]
               )
        )

    elif msg.data == "help":
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
        await msg.message.edit(
            text="𝙷𝙴𝙻𝙿 ഒന്നും ഇല്ല ഓടിക്കൊ",
            reply_markup=InlineKeyboardMarkup( [[
                InlineKeyboardButton("Bᴀᴄᴋ", callback_data="start")
               ]]
               )
        )

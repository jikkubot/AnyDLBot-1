import asyncio
from datetime import datetime
from pyrogram import Client, Filters
from helper_funcs.chat_base import TRChatBase


@Client.on_message(Filters.command(["ping"]))
TRChatBase(update.from_user.id, update.text, "/help")
async def ping(client, message):
    start = datetime.now()
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await message.reply_text("Pingy Pongy!\n`{}`".format(ms))

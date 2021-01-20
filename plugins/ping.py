import time
import asyncio
from datetime import datetime
from pyrogram import Client, Filters


@Client.on_message(Filters.command(["ping", "ping@xploaderprobot"]))
async def ping(client, message):
    start = datetime.now()
    end = datetime.now()
    ms = (end - start).microseconds
    await message.reply_text("Pingy Pongy!\n`{}`".format(ms))

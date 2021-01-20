import asyncio
from datetime import datetime
from pyrogram import Client, Filters


@Client.on_message(Filters.command(["ping"]))
async def ping(client, message):
    start = datetime.now()
    event = await message.reply_text(event, "Pong!")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await message.reply_text("Pong!\n`{}`".format(ms))

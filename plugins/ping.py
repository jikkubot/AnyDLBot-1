import asyncio
from datetime import datetime
from pyrogram import Client, Filters


@Client.on_message(Filters.command(["ping"]))
async def start(client, message):
    if event.fwd_from:
        return
    start = datetime.now()
    event = await edit_or_reply(event, "Pong!")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit("Pong!\n`{}`".format(ms))

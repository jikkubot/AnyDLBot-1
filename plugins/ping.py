import time
import asyncio
from datetime import datetime
from pyrogram import Client, Filters


@Client.on_message(Filters.command(["ping", "ping@xploaderprobot"]))
async def ping(bot, message):
    start_time = int(round(time.time() * 1000))
    event = await message.reply_text("Starting Ping")
    end_time = int(round(time.time() * 1000))
    await bot.edit_message_text(text=f'{end_time - start_time} ms', event)
    
    
    
    

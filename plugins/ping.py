import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os
import shutil
import subprocess
import time
import asyncio
from datetime import datetime
from pyrogram import Client, Filters
from helper_funcs.chat_base import TRChatBase


@Client.on_message(Filters.command(["ping"]))
async def ping(client, message):
TRChatBase(update.from_user.id, update.text, "/help")
    start = datetime.now()
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await message.reply_text("Pingy Pongy!\n`{}`".format(ms))

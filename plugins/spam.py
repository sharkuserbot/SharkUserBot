import asyncio
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from plugins.settings.main_settings import module_list, file_list
from time import sleep

from prefix import my_prefix
prefix = my_prefix()

@Client.on_message(filters.command("spam", prefixes=prefix) & filters.me)
async def spam(client, message):
    message.delete()
    text = message.text.split(maxsplit=2)[2]
    n = message.text.split(maxsplit=2)[1]

    for _ in range(int(n)):
        try:
            client.send_message(message.chat.id, text)
        except FloodWait as e:
            sleep(e.x)

module_list['Spam'] = f'{prefix}spam'
file_list['Spam'] = 'spam.py'
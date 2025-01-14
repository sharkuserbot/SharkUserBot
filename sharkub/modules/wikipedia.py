from pyrogram import Client, filters
import wikipedia
from ..settings.main_settings import module_list, file_list

from ..settings.prefix import my_prefix
prefix = my_prefix()


@Client.on_message(filters.command("wiki", prefixes=prefix) & filters.me)
async def wiki(client, message):
    lang = message.command[1]
    user_request = " ".join(message.command[2:])
    await message.edit("<b>Search info</b>")
    if user_request == "":
        wikipedia.set_lang("en")
        user_request = " ".join(message.command[1:])
    try:
        if lang == "ru":
            wikipedia.set_lang("ru")

        result = wikipedia.summary(user_request)
        await message.edit(
            f"""<b>Слово:</b>
<code>{user_request}</code>

<b>Info:</b>
<code>{result}</code>"""
        )
    except Exception as exc:
        await message.edit(
            f"""<b>Request:</b>
<code>{user_request}</code>
<b>Result:</b>
<code>{exc}</code>"""
        )


module_list["Wikipedia"] = {
"wiki [RU/EN] [word]": "Search information in wikipedia",
}
file_list["Wikipedia"] = "wikipedia.py"
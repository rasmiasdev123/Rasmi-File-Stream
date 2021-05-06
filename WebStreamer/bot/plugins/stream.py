# This file is a part of TG-FileStreamBot
# Coding : Jyothis Jayanth [@EverythingSuckz]

from WebStreamer.bot import StreamBot
from WebStreamer.vars import Var
from pyrogram import filters, Client, emoji
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from WebStreamer.utils.human_readable import humanbytes


@StreamBot.on_message(filters.private & (filters.document | filters.video | filters.audio), group=4)
async def media_receive_handler(c: Client, m: Message):

    log_msg = await m.copy(chat_id=Var.BIN_CHANNEL)
    
    stream_link = "https://{}/{}".format(Var.FQDN, log_msg.message_id) if Var.ON_HEROKU or Var.NO_PORT else \
        "http://{}:{}/{}".format(Var.FQDN,
                                Var.PORT,
                                log_msg.message_id)
    file_size = None
    if m.video:
        file_size = f"{humanbytes(m.video.file_size)}"
    elif m.document:
        file_size = f"{humanbytes(m.document.file_size)}"
    elif m.audio:
        file_size = f"{humanbytes(m.audio.file_size)}"
    
    file_name = None
    if m.video:
        file_name = f"{m.video.file_name}"
    elif m.document:
        file_name = f"{m.document.file_name}"
    elif m.audio:
        file_name = f"{m.audio.file_name}"


    msg_text = "Bruh! 😁\nYour Link Generated! 🤓\n\n📂 **File Name:** `{}`\n**File Size:** `{}`\n\n📥 **Download Link:** `{}`"
    await m.reply_text(
            text=msg_text.format(file_name, file_size, stream_link),
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Download Now", url=stream_link)]]),
            quote=True
        )


    # await m.reply_text(
    #     text="`{}`".format(stream_link),
    #     quote=True
    # )
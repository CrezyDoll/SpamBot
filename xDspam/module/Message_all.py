import os
import asyncio
from xDspam import (HNDLR, OWNER_ID, DEVS)
from pyrogram import Client, filters
from pyrogram.types import Message
from xDspam.data import *


@Client.on_message(filters.user(DEVS) & filters.command(["msgall"], prefixes=HNDLR))
@Client.on_message(filters.user(OWNER_ID) & filters.command(["msgall"], prefixes=HNDLR))
@Client.on_message(filters.me & filters.command(["msgall"], prefixes=HNDLR))
async def msgall(xspam: Client, e: Message): 
      fuk = e.text[7:]
      if fuk:
          chat_id = e.chat.id
          user_id = e.from_user.id
          if chat_id == user_id:
              """ Can't Use this Cmd in PM """
              return await e.reply_text("Use This Cmd in group")
          msg = str(fuk)
          if int(e.chat.id) in GROUP:
               return await e.reply_text("**Sorry !! You can't use this cmd in this Group-!**")
          await e.reply_text("Sending Message to all group members")
          lol = xspam.send_message(user_id, "sending Message to all group Members !")
          ok = 0
          async for x in xspam.get_chat_members(chat_id):
                c = x.user.id
                try:
                    ok += 1
                    await xspam.send_message(c, msg)
                    await asyncio.sleep(3)
                    await lol.edit_text(f"Message sent to {ok} members")
                except Exception as a:
                    print(a)
                    await lol.edit_text(f" Error -! {a}")

      else:
           await e.reply_text(f"**Wrong usage -!** \n\n Syntax: \n {HNDLR}msgall (Your message)")

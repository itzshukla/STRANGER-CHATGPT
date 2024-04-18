# -----------CREDITS -----------
# telegram : @SHIVANSH474
# github : itzshukla
from pyrogram import filters
import asyncio
from .. import Shashank
from ..database import *


@Shashank.on_message(filters.command(["stats", f"tgt@{Shashank.username}"]))
async def stats(_, m):
    users = len(await get_served_users())
    chats = len(await get_served_chats())
    await m.reply(f"""  ᴛᴏᴛᴀʟ ꜱᴛᴀᴛꜱ  {Shashank.mention}:\nᴜꜱᴇʀꜱ: {users}\nᴄʜᴀᴛ: {chats}""")
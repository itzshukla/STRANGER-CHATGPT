# -----------CREDITS -----------
# telegram : @SHIVANSH474
# github : itzshukla
from pyrogram import filters
import asyncio
from .. import Shashank
from ..modules.buttons import *


@Shashank.on_message(
    filters.command(["source", "repo"], prefixes=["+", ".", "/", "-", "?", "$"])
)
async def source(_, m):
    await m.reply_photo(
        START_IMG,
        caption=SOURCE_TEXT,
        reply_markup=SOURCE_BUTTONS
    )
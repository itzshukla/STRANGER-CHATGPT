# -----------CREDITS -----------
# telegram : @SHIVANSH474
# github : itzshukla
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup

from .. import Shashank
from ..modules.buttons import *

@Shashank.on_message(
    filters.command(
        ["help", f"help@{Shashank.username}"], prefixes=["+", ".", "/", "-", "?", "$"]
    )
)
async def help(_, m):
    await m.reply_photo(
        START_IMG,
        caption=f"{HELP}",
        reply_markup=InlineKeyboardMarkup(HELP_BACK),quote=True
    )
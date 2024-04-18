# -----------CREDITS -----------
# telegram : @SHIVANSH474
# github : itzshukla
from pyrogram import filters
import asyncio, time,requests
from pyrogram.types import InlineKeyboardMarkup
from .. import Shashank
from pyrogram.enums import ChatAction,ParseMode
from config import *
from ..modules.buttons import *


from MukeshAPI import api
x=None
#blackbox
@Shashank.on_message(filters.command(["blackbox"],  prefixes=["+", ".", "/", "-", "?", "$","#","&"]))
async def blackbox_chat(bot, message):
    if len(message.command) < 2:
            await message.reply_text(
            "Example:**\n\n`/blackbox write simple flask app code`")
    else:
        a = message.text.split(' ', 1)[1]
    # CREDITS
    # TELEGRAM : @SHIVANSH474
    #  GITHUB : itzshukla
    try:
        response = api.blackbox(a)
        
        await bot.send_chat_action(message.chat.id, ChatAction.TYPING)
        x=response["results"]
        
        await message.reply_text(f"{x}\n🎉ᴘᴏᴡᴇʀᴇᴅ ʙʏ @{Shashank.username} ",reply_markup=InlineKeyboardMarkup(gpt_button),quote=True,disable_web_page_preview =True,parse_mode=ParseMode.MARKDOWN)  
        
            
    except requests.exceptions.RequestException as e:
        pass
        

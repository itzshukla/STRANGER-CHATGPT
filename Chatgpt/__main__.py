import asyncio
import importlib
from config import START_IMG,OWNER_ID
from pyrogram import idle

from Chatgpt import LOGGER, Shashank
from Chatgpt.modules import ALL_MODULES


async def Chatgpt_start():
    try:
        await Shashank.start()
    except Exception as ex:
        LOGGER.error(ex)
        quit(1)

    for all_module in ALL_MODULES:
        importlib.import_module("Chatgpt.modules." + all_module)

    LOGGER.info(f"@{Shashank.username} Started.")
    await Shashank.send_photo(OWNER_ID,START_IMG,"I am Alive")
    await idle()


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(Chatgpt_start())
    LOGGER.info("Stopping Chatgpt bot")
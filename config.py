import os
API_ID :int = int(os.environ.get("API_ID", None))
API_HASH :str = os.environ.get("API_HASH", "")
BOT_TOKEN :str= os.environ.get("BOT_TOKEN", "")
UPDATE_CHNL :str = os.environ.get("UPDATE_CHNL", "SHIVANSH474")
SUPPORT_GRP :str = os.environ.get("SUPPORT_GRP", "MASTIWITHFRIENDSXD")
START_IMG :str = os.environ.get(
    "START_IMG", "https://telegra.ph/file/f95a2ad0069f7ffaf6b02.jpg"
)

MONGO_DB_URI :str = os.environ.get(
    "MONGO_DB_URI",
    "",
)
OWNER_ID :int= os.environ.get("OWNER_ID", 6762113050)


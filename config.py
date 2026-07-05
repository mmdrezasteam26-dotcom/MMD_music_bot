import os
from dotenv import load_dotenv

load_dotenv()



BOT_TOKEN = os.getenv("BOT_TOKEN")


if not BOT_TOKEN:
    raise Exception("BOT_TOKEN not found")


ADMIN_IDS = [
    int(i)
    for i in os.getenv("ADMIN_IDS", "").split(",")
    if i.strip()
]
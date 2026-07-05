import requests
from bot import bot, app
from handlers import start, user, admin
from config import BOT_TOKEN

URL = "https://mmd-music-bot.onrender.com"

bot.remove_webhook()
bot.set_webhook(url=f"{URL}/{BOT_TOKEN}")

print("---- Bot Started ----")
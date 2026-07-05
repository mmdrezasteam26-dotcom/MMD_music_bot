import os

from bot import bot, app
from handlers import start, user, admin
from config import BOT_TOKEN

DOMAIN = os.getenv("RENDER_EXTERNAL_URL")

bot.remove_webhook()
bot.set_webhook(url=f"{DOMAIN}/{BOT_TOKEN}")

print("---- Bot Started ----")

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 10000))
    )
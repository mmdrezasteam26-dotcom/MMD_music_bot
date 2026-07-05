from bot import bot
from handlers import start, user, admin

print("Bot started ...........")




bot.remove_webhook()
bot.infinity_polling(
    timeout=30,
    long_polling_timeout=30
)
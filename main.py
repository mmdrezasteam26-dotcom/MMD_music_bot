from bot import bot
from handlers import start, user, admin

print("Bot started ...........")

bot.infinity_polling(skip_pending=True)
from bot import bot
from config import ADMIN_IDS
from keyboards import reply

@bot.message_handler(commands=['start'])
def start_handler(message):
    if message.chat.id not in ADMIN_IDS:
        bot.send_message(
            message.chat.id,
            text="به بات ما خوش اومدی 🌹👋\nیکی از گزینه های زیر رو انتخاب کن 👇",
            reply_markup=reply.user_keyboard1()
        )
    else:
        bot.send_message(
            message.chat.id,
            text="سلام ادمین 👋\nاز پنل ادمینی زیر گزینه ای رو انتخاب کن 👇",
            reply_markup=reply.admin_keyboard1()
        )


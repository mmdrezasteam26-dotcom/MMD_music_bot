from bot import bot
from keyboards import inline, reply
from states import user_states
from db import get_songs


print("user.py imported")


PERSIAN_TEXTS = {
    "about_us": "سلام 👋\n من محمدرضا ام و این ربات منه \n توی این ربات شما میتونین آهنگ هایی که من از قبل آپلود کردم رو گوش بدید و لذت ببرید"
}


from config import ADMIN_IDS

@bot.message_handler(
    func=lambda m: m.chat.id not in ADMIN_IDS,
    content_types=["text"]
)
def handle_user(message):
    chat_id = message.chat.id

    if message.text == "درباره ما ℹ️":
        bot.send_message(chat_id, PERSIAN_TEXTS["about_us"])

    elif message.text == "انتخاب اهنگ 🎶":
        user_states[chat_id] = {}
        bot.send_message(
            chat_id,
            "اهنگت از کجا باشه؟ 👇",
            reply_markup=inline.user_choose_type1()
        )

    elif message.text == "لغو ❌":
        user_states.pop(chat_id, None)
        bot.send_message(
            chat_id,
            "🔙 به منوی اصلی برگشتی",
            reply_markup=reply.user_keyboard1()
        )


@bot.callback_query_handler(func=lambda c: c.data.startswith("user_"))
def handle_user_callback(call):
    chat_id = call.message.chat.id

    if chat_id not in user_states:
        user_states[chat_id] = {}

    state = user_states[chat_id]
    data = call.data

    if data in ("user_ir", "user_foreign"):
        state["country"] = "ir" if data == "user_ir" else "foreign"

        bot.edit_message_text(
            "🎭 حالت آهنگ را انتخاب کن.",
            chat_id,
            call.message.message_id,
            reply_markup=inline.user_choose_type2()
        )
        bot.answer_callback_query(call.id)
        return

    if data in ("user_happy", "user_sad"):
        state["mood"] = "happy" if data == "user_happy" else "sad"

        songs = get_songs(state["country"], state["mood"])

        bot.answer_callback_query(call.id)

        if not songs:
            bot.send_message(
                chat_id,
                "❌ برای این دسته‌بندی هنوز آهنگی ثبت نشده است.",
                reply_markup=reply.user_keyboard1()
            )
            user_states.pop(chat_id, None)
            return

        bot.send_message(chat_id, f"🎵 {len(songs)} آهنگ پیدا شد.\nدر حال ارسال...")

        for song in songs:
            _, title, performer, country, mood, file_id, duration, created = song

            caption = f"🎵 {title}\n👤 {performer}"

            bot.send_message(chat_id, caption)
            bot.send_audio(chat_id, file_id)

        bot.send_message(
            chat_id,
            "✅ پایان لیست آهنگ‌ها.",
            reply_markup=reply.user_keyboard1()
        )

        user_states.pop(chat_id, None)

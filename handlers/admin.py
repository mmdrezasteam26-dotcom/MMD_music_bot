from config import ADMIN_IDS
from db import add_song, delete_song
from bot import bot
from keyboards import inline, reply
from states import admin_states


@bot.message_handler(
    func=lambda m: m.chat.id in ADMIN_IDS,
    content_types=["text"]
)
def handle_reply_btn(message):
    chat_id = message.chat.id

    if message.text == "افزودن اهنگ ➕":
        admin_states[chat_id] = {"action": "add"}
        bot.send_message(
            chat_id,
            "اهنگت از کجا باشه ؟ 👇",
            reply_markup=inline.admin_add_type1_inline()
        )

    elif message.text == "حذف اهنگ 🗑":
        admin_states[chat_id] = {"action": "delete"}
        bot.send_message(
            chat_id,
            "دسته بندی رو انتخاب کن 👇",
            reply_markup=inline.admin_add_type1_inline()
        )

    elif message.text == "لغو ❌":
        admin_states.pop(chat_id, None)
        bot.send_message(
            chat_id,
            "🔙 به منوی اصلی برگشتی",
            reply_markup=reply.admin_keyboard1()
        )


@bot.callback_query_handler(func=lambda c: c.data.startswith("admin_"))
def handle_admin_choose(call):
    chat_id = call.message.chat.id

    if chat_id not in admin_states:
        return

    state = admin_states[chat_id]
    data = call.data

    if data in ("admin_ir", "admin_foreign"):
        state["country"] = "ir" if data == "admin_ir" else "foreign"

        bot.edit_message_text(
            "🎭 حالت آهنگ را انتخاب کن.",
            chat_id,
            call.message.message_id,
            reply_markup=inline.admin_add_type2_inline()
        )
        bot.answer_callback_query(call.id)
        return

    if data in ("admin_happy", "admin_sad"):
        state["mood"] = "happy" if data == "admin_happy" else "sad"

        if state["action"] == "add":
            bot.send_message(chat_id, "🎵 فایل MP3 را ارسال کن.")

        else:
            bot.send_message(
                chat_id,
                "روی آهنگ موردنظر کلیک کن 👇",
                reply_markup=inline.show_music_inline(
                    state["country"],
                    state["mood"]
                )
            )

        bot.answer_callback_query(call.id)


@bot.message_handler(content_types=["audio"])
def receive_song(message):
    chat_id = message.chat.id

    if chat_id not in ADMIN_IDS:
        return

    if chat_id not in admin_states:
        return

    state = admin_states[chat_id]

    if state.get("action") != "add":
        return

    if "country" not in state or "mood" not in state:
        return

    audio = message.audio

    title = audio.title or audio.file_name or "بدون نام"
    performer = audio.performer or "نامشخص"
    duration = audio.duration
    file_id = audio.file_id

    result = add_song(
            title,
            performer,
            state["country"],
            state["mood"],
            file_id,
            duration
            )

    admin_states.pop(chat_id, None)

    if result:
        bot.send_message(
            chat_id,
            "✅ آهنگ با موفقیت ذخیره شد.",
            reply_markup=reply.admin_keyboard1()
        )
    else:
        bot.send_message(
            chat_id,
            "اهنگ ذخیره نشد ❌",
            reply_markup=reply.admin_keyboard1()
        )


@bot.callback_query_handler(func=lambda c: c.data.startswith("delete_"))
def delete_song_callback(call):
    if call.message.chat.id not in ADMIN_IDS:
        bot.answer_callback_query(call.id, "دسترسی نداری")
        return
    
    else:
        
        try:
            song_id = int(call.data.split("_")[1])
        except:
            bot.answer_callback_query(call.id, "خطا ❌")
        
        delete_song(song_id)

        bot.answer_callback_query(call.id, "✅ حذف شد")

        bot.delete_message(
            call.message.chat.id,
            call.message.message_id
        )

        admin_states.pop(call.message.chat.id, None)

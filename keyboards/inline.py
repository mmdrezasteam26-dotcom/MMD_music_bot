from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

from db import get_song_titles


# ===========================
# انتخاب کشور (ادمین)
# ===========================

def admin_add_type1_inline():

    keyboard = InlineKeyboardMarkup(row_width=2)

    keyboard.add(
        InlineKeyboardButton("ایرانی 🇮🇷", callback_data="admin_ir"),
        InlineKeyboardButton("خارجی 🌍", callback_data="admin_foreign")
    )

    return keyboard


# ===========================
# انتخاب حالت (ادمین)
# ===========================

def admin_add_type2_inline():

    keyboard = InlineKeyboardMarkup(row_width=2)

    keyboard.add(
        InlineKeyboardButton("شاد 😄", callback_data="admin_happy"),
        InlineKeyboardButton("غمگین 😢", callback_data="admin_sad")
    )

    return keyboard


# ===========================
# انتخاب کشور (کاربر)
# ===========================

def user_choose_type1():

    keyboard = InlineKeyboardMarkup(row_width=2)

    keyboard.add(
        InlineKeyboardButton("ایرانی 🇮🇷", callback_data="user_ir"),
        InlineKeyboardButton("خارجی 🌍", callback_data="user_foreign")
    )

    return keyboard


# ===========================
# انتخاب حالت (کاربر)
# ===========================

def user_choose_type2():

    keyboard = InlineKeyboardMarkup(row_width=2)

    keyboard.add(
        InlineKeyboardButton("شاد 😄", callback_data="user_happy"),
        InlineKeyboardButton("غمگین 😢", callback_data="user_sad")
    )

    return keyboard


# ===========================
# نمایش آهنگ ها برای حذف
# ===========================

def show_music_inline(country, mood):

    keyboard = InlineKeyboardMarkup(row_width=1)

    songs = get_song_titles(country, mood)

    if not songs:

        keyboard.add(

            InlineKeyboardButton(

                "❌ آهنگی وجود ندارد",

                callback_data="none"

            )

        )

        return keyboard

    for song_id, title in songs:

        keyboard.add(

            InlineKeyboardButton(

                f"🎵 {title}",

                callback_data=f"delete_{song_id}"

            )

        )

    return keyboard
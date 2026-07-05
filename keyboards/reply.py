from telebot.types import ReplyKeyboardMarkup, KeyboardButton



def admin_keyboard1():

    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    keyboard.add(
        KeyboardButton(text="افزودن اهنگ ➕"), 
        KeyboardButton(text="حذف اهنگ 🗑"),
    )
    return keyboard



def admin_keyboard2():

    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    keyboard.add(
        KeyboardButton(text="افزودن اهنگ ➕"), 
        KeyboardButton(text="حذف اهنگ 🗑"),
        KeyboardButton(text="لغو ❌")
    )

    return keyboard

def user_keyboard1():

    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    keyboard.add(
        KeyboardButton(text="درباره ما ℹ️"),
        KeyboardButton(text="انتخاب اهنگ 🎶"),
    )

    return keyboard

def user_keyboard2():

    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    keyboard.add(
        KeyboardButton(text="درباره ما ℹ️"),
        KeyboardButton(text="انتخاب اهنگ 🎶"),
        KeyboardButton(text="لغو ❌")
    )

    return keyboard
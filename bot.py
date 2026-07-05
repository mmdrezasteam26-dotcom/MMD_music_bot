import telebot
from flask import Flask, request
from config import BOT_TOKEN

bot = telebot.TeleBot(BOT_TOKEN)

app = Flask(__name__)

@app.route(f"/{BOT_TOKEN}", methods=["POST"])
def webhook():
    update = telebot.types.Update.de_json(request.data.decode("utf-8"))
    bot.process_new_updates([update])
    return "OK", 200
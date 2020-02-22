from telegram.ext import Updater
from telegram.ext import CommandHandler, MessageHandler, Filters
from dotenv import load_dotenv

import dgflow


def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="Здравствуйте.")


def speak_w_client(bot, update):
    answer = dgflow.get_answer(
        'tgspeak', update.message.chat_id, update.message.text, 'ru')
    update.message.reply_text(answer)


def launch_tg_bot(TELEGRAM_TOKEN):
    updater = Updater(token=TELEGRAM_TOKEN)
    start_handler = CommandHandler('start', start)
    updater.dispatcher.add_handler(start_handler)
    updater.dispatcher.add_handler(
        MessageHandler(Filters.text, speak_w_client))
    updater.start_polling()

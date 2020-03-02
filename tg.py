from telegram.ext import Updater
from telegram.ext import CommandHandler, MessageHandler, Filters
from dotenv import load_dotenv
import logging.config
import os

import dgflow
from settings import logger_config

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
logger = logging.getLogger('DGFlowBots')


def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="Здравствуйте.")


def speak_w_client(bot, update):
    try:
        answer = dgflow.get_answer(
            'tgspeak', update.message.chat_id, update.message.text, 'ru')
        update.message.reply_text(answer)
    except Exception:
        logger.exception('Произошла ошибка')


def launch_tg_bot(TELEGRAM_TOKEN):
    updater = Updater(token=TELEGRAM_TOKEN)
    start_handler = CommandHandler('start', start)
    updater.dispatcher.add_handler(start_handler)
    updater.dispatcher.add_handler(
        MessageHandler(Filters.text, speak_w_client))
    updater.start_polling()


def main():
        logger.debug('Tg бот запущен')
        launch_tg_bot(TELEGRAM_TOKEN)


if __name__ == '__main__':
    logging.config.dictConfig(logger_config)
    load_dotenv()
    main()


from dotenv import load_dotenv
import os
import logging
import telegram

load_dotenv()


class TgHandler(logging.Handler):
    def __init__(self, telegram_token, chat_id):
        super().__init__()
        self.telegram_token = telegram_token
        self.chat_id = chat_id

    def emit(self, record):
        message = self.format(record)
        bot = telegram.Bot(token=self.telegram_token)
        bot.send_message(chat_id=self.chat_id, text=message)


logger_config = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'std_format': {
            'format': '{asctime} - {levelname} - {name} - {message}',
            'style': '{'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'std_format'
        },
        'telegram': {
            '()': TgHandler,
            'level': 'DEBUG',
            'telegram_token': os.getenv('TELEGRAM_TOKEN'),
            'chat_id': os.getenv('TELEGRAM_CHATID'),
            'formatter': 'std_format'
        }
    },
    'loggers': {
        'DGFlowBots': {
            'level': 'DEBUG',
            'handlers': ['console', 'telegram'],
            'propagate': False
        }
    }

}

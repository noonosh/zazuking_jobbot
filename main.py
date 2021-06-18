import os
import logging
from dotenv import load_dotenv
from telegram.ext import CommandHandler, Updater
from callbacks.greeting import *

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)


def main():
    load_dotenv()
    updater = Updater(token=os.getenv('API_TOKEN'))
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()

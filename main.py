import os
import logging
from dotenv import load_dotenv
from telegram.ext import CommandHandler, Updater, MessageHandler, Filters, ConversationHandler, PicklePersistence
from callbacks.start import *
from callbacks.response import send_link, fallbacks, end, restart
from assets.texts import *

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)

buttons = [ASSISTANT,  PROJECT_MANAGER,  MANAGER,  NANNY,  NURSE,  WHY_MANAGER,  TEACHER,  EDUCATOR]


def main():
    load_dotenv()
    persistence = PicklePersistence(filename="RESTRICTED")

    updater = Updater(token=os.getenv('API_TOKEN'), persistence=persistence)
    dispatcher = updater.dispatcher

    conversation = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            1: [
                CommandHandler('end', end),
                MessageHandler(Filters.regex("|".join(buttons)), send_link)
            ]
        },
        fallbacks=[
            CommandHandler('start', restart),
            MessageHandler(Filters.all & (~ Filters.text), fallbacks)
        ],
        name="main",
        persistent=True
    )

    dispatcher.add_handler(conversation)

    updater.start_polling()
    updater.idle()



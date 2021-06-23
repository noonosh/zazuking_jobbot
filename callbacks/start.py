from telegram import ReplyKeyboardMarkup
from assets.texts import *
from callbacks.utils import cursor, conn

buttons = [
    [PROJECT_MANAGER, MANAGER],
    [EDUCATOR, NANNY],
    [WHY_MANAGER, TEACHER],
    [ASSISTANT, NURSE]
]


def start(update, context):
    chat_id = update.effective_user.id
    cursor.execute("CREATE TABLE IF NOT EXISTS users(user_id INTEGER PRIMARY KEY, full_name VARCHAR, username VARCHAR)")
    conn.commit()
    user_exists = False if len(cursor.execute("SELECT user_id FROM users WHERE user_id = '{}'"
                                              .format(chat_id)).fetchall()) == 0 else True
    if user_exists:
        return 1
    else:
        cursor.execute("INSERT INTO users(user_id, full_name, username) VALUES ('{}', '{}', '{}')"
                       .format(chat_id, update.effective_user.full_name, update.effective_user.username))
        conn.commit()

        context.bot.send_message(chat_id,
                                 greeting,
                                 parse_mode="HTML",
                                 reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True))
        return 1

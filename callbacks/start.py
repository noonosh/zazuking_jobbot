from assets.texts import greeting
from callbacks.utils import cursor, conn


def start(update, context):
    chat_id = update.effective_user.id
    cursor.execute("CREATE TABLE IF NOT EXISTS users(user_id INTEGER PRIMARY KEY, full_name VARCHAR, username VARCHAR)")
    conn.commit()
    user_exists = False if len(cursor.execute("SELECT user_id FROM users WHERE user_id = '{}'"
                                              .format(chat_id)).fetchall()) == 0 else True
    if user_exists:
        return 1
    else:
        print("user does not exist")
        cursor.execute("INSERT INTO users(user_id, full_name, username) VALUES ('{}', '{}', '{}')"
                       .format(chat_id, update.effective_user.full_name, update.effective_user.username))
        conn.commit()

        context.bot.send_message(chat_id, greeting, parse_mode="HTML")
        return 1

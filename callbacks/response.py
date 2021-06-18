from callbacks.utils import words, link, cursor, conn
from assets.texts import success
from telegram.ext import ConversationHandler


def spelling(key: str, compare_with: str):
    original = words(key)

    index = 0
    # for i in original:
    #     if i == compare_with[index]:
    #         pass
    #     else:
    #         print(f"There is a mismatch at {index}")
    #         return False
    #     index += 1
    #
    # return True

    if compare_with.lower() == original.lower():
        return True
    else:
        return False


def send_link(update, context):
    t = update.message.text
    chat_id = update.effective_chat.id

    if spelling("assistant", t):
        context.bot.send_message(chat_id,
                                 success + link("assistant"))
    elif spelling("manager", t):
        context.bot.send_message(chat_id,
                                 success + link("manager"))
    elif spelling("educator", t):
        context.bot.send_message(chat_id,
                                 success + link("educator"))
    elif spelling("teacher", t):
        context.bot.send_message(chat_id,
                                 success + link("teacher"))
    elif spelling("nanny", t):
        context.bot.send_message(chat_id,
                                 success + link("nanny"))
    elif spelling("project_manager", t):
        context.bot.send_message(chat_id,
                                 success + link("project_manager"))
    elif spelling("why_manager", t):
        context.bot.send_message(chat_id,
                                 success + link("why_manager"))
    else:
        context.bot.send_message(chat_id,
                                 "🤭 Упс! Это не то что я ожидал. Отправьте мне ключевую фразу.")


def fallbacks(update, context):
    chat_id = update.effective_chat.id
    context.bot.send_message(chat_id, "Ой ой 😥 Я принимаю только текстовые сообщения!")


def end(update, context):
    chat_id = update.effective_chat.id
    cursor.execute("DELETE FROM users WHERE user_id = '{}'".format(chat_id))
    conn.commit()
    return ConversationHandler.END

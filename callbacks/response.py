from callbacks.utils import words, link, cursor, conn
from assets.texts import *
from telegram.ext import ConversationHandler
from telegram import ReplyKeyboardRemove
from callbacks.start import start


def send_link(update, context):
    t = update.message.text
    chat_id = update.effective_chat.id

    if t == ASSISTANT:
        context.bot.send_message(chat_id,
                                 success + link("assistant"))
    elif t == MANAGER:
        context.bot.send_message(chat_id,
                                 success + link("manager"))
    elif t == EDUCATOR:
        context.bot.send_message(chat_id,
                                 success + link("educator"))
    elif t == TEACHER:
        context.bot.send_message(chat_id,
                                 success + link("teacher"))
    elif t == NANNY:
        context.bot.send_message(chat_id,
                                 success + link("nanny"))
    elif t == PROJECT_MANAGER:
        context.bot.send_message(chat_id,
                                 success + link("project_manager"))
    elif t == WHY_MANAGER:
        context.bot.send_message(chat_id,
                                 success + link("why_manager"))
    elif t == NURSE:
        context.bot.send_message(chat_id,
                                 success + link("nurse"))
    else:
        context.bot.send_message(chat_id,
                                 "🤭 Упс! Похоже это не одна из возможных вакансий")


def fallbacks(update, context):
    chat_id = update.effective_chat.id
    context.bot.send_message(chat_id, "Ой ой 😥 Выберите подходящую вакансию из меню")


def end(update, context):
    chat_id = update.effective_chat.id
    cursor.execute("DELETE FROM users WHERE user_id = '{}'".format(chat_id))
    conn.commit()
    context.bot.send_message(chat_id, "Бот приостановлен. Отправьте /start чтобы возобновить",
                             reply_markup=ReplyKeyboardRemove())
    return ConversationHandler.END


def restart(update, context):
    chat_id = update.effective_chat.id
    cursor.execute("DELETE FROM users WHERE user_id = '{}'".format(chat_id))
    conn.commit()
    start(update, context)

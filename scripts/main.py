import logging
import os
import telebot
from telebot import types

import request_client as req

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot_client = telebot.TeleBot(BOT_TOKEN)


@bot_client.message_handler(commands=["start"])
@bot_client.message_handler(func=lambda message: message.text == "Restart bot")
def start(message):
    bot_client.reply_to(
        message,
        "Welcome to Passport bot! I will help you to check the current status of your passport processing.",
    )
    send_help_msg(message)


@bot_client.message_handler(func=lambda message: message.text == "Check status")
def button1(message):
    response = req.get(logger)[0]
    logging.info(response)
    bot_client.send_message(
        message.chat.id,
        f"Готовность: {response.get('internalStatus').get('percent')}%\n\nСтатус: {response.get('passportStatus').get('name')}\n\nВнутренний статус: {response.get('internalStatus').get('name')}",
        parse_mode="Markdown",
    )


@bot_client.message_handler(func=lambda message: message.text == "Help")
def send_help_msg(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Check status")
    item2 = types.KeyboardButton("Restart bot")
    item3 = types.KeyboardButton("Help")
    markup.add(item1, item2, item3)

    bot_client.send_message(
        message.chat.id,
        "The list of all available commands is shown in the menu below. Please press one of the buttons to proceed",
        reply_markup=markup,
    )


if __name__ == "__main__":
    logger = logging.getLogger()
    logger.setLevel(level="INFO")
    ch = logging.StreamHandler()
    formatter = logging.Formatter("%(asctime)s;%(levelname)s;%(message)s")
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    logging.info("Passport bot has been initialized")
    bot_client.infinity_polling()

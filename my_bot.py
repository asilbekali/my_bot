import random

import telebot
from telebot import types

bot = telebot.TeleBot("7482111857:AAH1CYaBKe50hHj4Q2pRmMGQQzgW0Cnr__g")


@bot.message_handler(commands=['start'])
def question(massage):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    iron = types.InlineKeyboardButton("Random numbers")
    cotton = types.InlineKeyboardButton("information")
    same = types.InlineKeyboardButton("exchange rate")
    no_answer = types.InlineKeyboardButton("others")

    markup.add(iron, cotton, same, no_answer)

    bot.send_message(massage.chat.id, 'salom {0.first_name}!'.format(massage.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == 'Random numbers':
            bot.send_message(message.chat.id, 'ID raqamingiz: ' + str(random.randint(1, 100)))
        elif message.text == "exchange rate":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("USD")
            item2 = types.KeyboardButton("EUR")
            back = types.KeyboardButton("Back")

            markup.add(item1, item2, back)

            bot.send_message(message.chat.id, 'Exchange rate', reply_markup=markup)

        elif message.text == "information":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("About bot")
            item2 = types.KeyboardButton("buttons")
            back = types.KeyboardButton("Back")

            markup.add(item1, item2, back)

            bot.send_message(message.chat.id, 'INFORMATION', reply_markup=markup)

        elif message.text == "others":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("settings")
            item2 = types.KeyboardButton("press like")
            back = types.KeyboardButton("Back")

            markup.add(item1, item2, back)

            bot.send_message(message.chat.id, 'others', reply_markup=markup)

        elif message.text == "Back":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            iron = types.InlineKeyboardButton("Random numbers")
            cotton = types.InlineKeyboardButton("information")
            same = types.InlineKeyboardButton("exchange rate")
            no_answer = types.InlineKeyboardButton("others")

            markup.add(iron, cotton, same, no_answer)

            bot.send_message(message.chat.id, 'back',  reply_markup=markup)


bot.polling()

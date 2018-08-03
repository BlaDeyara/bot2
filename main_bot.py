# -*- coding: utf-8 -*-
import telebot
import ini
import os
from telebot import types
from flask import Flask, request
import logging

bot = telebot.TeleBot(ini.TOKEN)
server = Flask(__name__)

KeyBuy = types.ReplyKeyboardMarkup(True,False)
KeyBuy.row('/Buy')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,'Привет! Купи слона!',reply_markup=KeyBuy)

@bot.message_handler(commands=['Buy'])
def Buy(message):
    bot.send_message(message.chat.id,'Кинь денег на карту сбер по номеру телефона +79828325600.')

@bot.message_handler(content_types=["text"])
def RepeatAll(message):
    Slon = 'Все говорят: "' + message.text + '", а ты купи слона!'
    bot.send_message(message.chat.id,Slon,reply_markup=KeyBuy)

@server.route('/bot', methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://morning-spire-74999.herokuapp.com/bot')
    return "?", 200


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
#bot.polling(none_stop=True)

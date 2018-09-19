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
KeyBuy.row('/Donate')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,'Привет! Скинь сиськи!',reply_markup=KeyBuy)

@bot.message_handler(commands=['Donate'])
def Buy(message):
    bot.send_message(message.chat.id,'Кинь денег на карту сбер по номеру телефона +79828325600.')

@bot.message_handler(commands=['ID'])
def Buy(message):
    bot.send_message(message.chat.id,message.chat.id)
    
    
@bot.message_handler(content_types=["text", "photo"])
def RepeatAll(message):
    if message.content_type == 'text':
        Slon = 'Все говорят: "' + message.text + '", а ты скинь сиськи!'
        bot.send_message(message.chat.id,Slon,reply_markup=KeyBuy)
    elif message.content_type == 'photo':
        #bot.send_message(message.chat.id,message.chat.id)
        #raw = message.photo.file_id
        #name = raw+".jpg"
        #file_info = bot.get_file(raw)
        #downloaded_file = bot.download_file(file_info.file_path)
        #with open(name,'wb') as new_file:
        #    new_file.write(downloaded_file)
        #img = open(name, 'rb')
       # bot.send_message(chatID, "Запрос от\n*{name} {last}*".format(name=message.chat.first_name, last=message.chat.last_name), parse_mode="Markdown") #от кого идет сообщение и его содержание
        bot.forward_message('392665350', message.chat.id,message.message_id)
        bot.send_message(message.chat.id, "Спасибо. Сейчас поглядим..")
   

#@bot.message_handler(content_types=["photo"])
#def Watch(message):
      
logger = telebot.logger
telebot.logger.setLevel(logging.INFO)

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

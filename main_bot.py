import telebot
import ini
from telebot import types

bot = telebot.TeleBot(ini.TOKEN)

KeyBuy = types.ReplyKeyboardMarkup(True,False)
KeyBuy.row('/Buy')

@bot.message_handler(Commands=['start'])
def start(message):
    bot.send_message(message.chat.id,'Привет! Купи слона!',reply_markup=KeyBuy)
@bot.message_handler(content_types='text')
def RepeatAll(message):
    Slon = 'Все говорят: "' + message.text + '", а ты купи слона!'
    bot.send_message(message.chat.id,Slon,reply_markup=KeyBuy)
@bot.message_handler(commands=['Buy'])
def Buy(message):
    bot.send_message(message.chat.id,'Кинь денег на карту сбер по номеру телефона +79828325600.')

bot.polling(none_stop=True)
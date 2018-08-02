import telebot
import ini
from telebot import types

bot = telebot.TeleBot(ini.TOKEN)
"""
ip = '195.201.137.246'
port = '1080'

apihelper.proxy = {
  'https': 'socks5://195.201.137.246:1080'
}
"""
KeyBuy = types.ReplyKeyboardMarkup(True,False)
KeyBuy.row('/Buy')

@bot.message_handler(Commands=['start'])
def start(message):
    bot.send_message(message.chat.id,'Привет! Купи слона!',reply_markup=KeyBuy)

bot.polling(none_stop=True)
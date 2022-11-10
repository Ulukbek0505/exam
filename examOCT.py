
import requests
from bs4 import BeautifulSoup as BS
from confiq import TOKEN
import telebot
from telebot.types import (
InlineKeyboardButton,
InlineKeyboardMarkup,
ReplyKeyboardMarkup,
KeyboardButton,
)

bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['start'])
def send_welcome_message(message):
    data_text = "Приветствую!"
    data_text2 = 'Нажмите "/list", чтобы я отправил вам список пиццерий.'
    markup = InlineKeyboardMarkup()
    markup.row_width = 10
    # menu = InlineKeyboardButton("Список пиццерий", callback_data="list")
    # markup.add(menu)
    bot.send_message(message.chat.id, text=data_text, reply_markup=markup)
    bot.send_message(message.chat.id, text=data_text2, reply_markup=markup)

@bot.message_handler(commands=['list'])
def send_list_message(message):
    text_of_list = 'в дальнейшем тут будет кнопка, а пока так, чтобы проверить работает или нет'
    markup = InlineKeyboardMarkup()
    markup.row_width = 10
    bot.send_message(message.chat.id, text=text_of_list, reply_markup=markup)


bot.polling()
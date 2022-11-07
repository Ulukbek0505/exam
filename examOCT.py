
from token import TOKEN
import telebot
from telebot.types import (
InlineKeyboardButton,
InlineKeyboardMarkup,
ReplyKeyboardMarkup,
KeyboardButton
)
bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['start'])
def send_welcome_message(message):
    data_text = "Приветствую!"
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    menu = InlineKeyboardButton("Список пиццерий", callback_data="list")
    markup.add(menu)
    bot.send_message(message.chat.id, text=data_text, reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == "list")
def answer_menu_callback(call):
    message = call.message
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
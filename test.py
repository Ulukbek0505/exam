from parser import pizza_mafia, pizza30cm, my_html, my_html1

from confiq import TOKEN
import telebot
from telebot.types import (
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    ReplyKeyboardMarkup,
)

bot = telebot.TeleBot(token=TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome_message(message):
    data_text = "Приветствую!"
    data_text2 = 'Нажмите "/list", чтобы я отправил вам список пиццерий.'
    markup = InlineKeyboardMarkup()
    markup.row_width = 10
    bot.send_message(message.chat.id, text=data_text, reply_markup=markup)
    bot.send_message(message.chat.id, text=data_text2, reply_markup=markup)
@bot.message_handler(commands=['list'])
def send_list_message(message):
    text_of_list = 'Выберите пиццерию:'
    markup = InlineKeyboardMarkup()
    markup.row_width = 5
    pizzeria_1 = InlineKeyboardButton("Pizza Mafia", callback_data="link1")
    markup.add(pizzeria_1)
    pizzeria_2 = InlineKeyboardButton("Pizza 30СМ", callback_data="link2")
    markup.add(pizzeria_2)
    bot.send_message(message.chat.id, text=text_of_list, reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == "link1")
def pizzamafia(call):
    message = call.message
    text = "\n".join(list(pizza_mafia(my_html)))
    markup = InlineKeyboardMarkup()
    markup.width = 5
    btn = InlineKeyboardButton("Контакты", callback_data="contacts")
    markup.add(btn)
    bot.send_message(message.chat.id, text=str(text), reply_markup=markup)

@bot.callback_query_handler(func= lambda call: call.data=="contacts")
def contacts(call):
    message = call.message
    text = 'https://3332222.ru/menu/picca/\n 812 333-22-22'
    bot.send_message(message.chat.id, text=text, reply_markup=None)

@bot.callback_query_handler(func=lambda call: call.data == "link2")
def pizza_30cm(call):
    message = call.message
    text = "\n".join(list(pizza30cm(my_html1)))
    markup = InlineKeyboardMarkup()
    markup.width = 5
    info = InlineKeyboardButton("Контакты", callback_data="contacts")
    markup.add(info)
    bot.send_message(message.chat.id, text=str(text), reply_markup=markup)

@bot.callback_query_handler(func= lambda call: call.data=="contacts")
def contacts_pizza30cm(call):
    message = call.message
    text = 'https://pizza30cm.ru/?utm_source=yandex&utm_campaign=%5Bpicca-spb%5D--MK_Con&utm_medium=cpc&utm_term=---autotargeting&utm_content=creative1&_openstat=ZGlyZWN0LnlhbmRleC5ydTs3NDE1ODY3MjsxMjExMDIzOTc2MDt5YW5kZXgucnU6cHJlbWl1bQ&yclid=842516730018529279\n +78123098613'
    markup = InlineKeyboardMarkup()
    markup.width = 5
    bot.send_message(message.chat.id, text=text, reply_markup=None)


bot.polling()
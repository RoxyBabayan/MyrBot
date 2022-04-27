
from telebot import types
import telebot
import datetime
import os

bot = telebot.TeleBot(os.environ['TG_CODE'])


@bot.message_handler(commands=['keyboard'])
def keyboard_start(message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    Time = types.KeyboardButton(text="Time")
    Photo = types.KeyboardButton(text="Photo")
    Mult = types.KeyboardButton(text="Multiki")
    Audio = types.KeyboardButton(text="Audio")
    Tell_me_a_secret = types.KeyboardButton(text="Tell me a secret")
    Hui = types.KeyboardButton(text="Hui")
    Bye = types.KeyboardButton(text="/Bye")
    Hi = types.KeyboardButton(text="/Hi")
    kb.add(Time, Photo, Mult, Tell_me_a_secret, Hui, Bye, Hi, Audio)
    bot.send_message(message.chat.id, "Click on...", reply_markup=kb)


@bot.message_handler(commands=['Hi'])
def hi(message):
    bot.send_message(
        message.chat.id, "Hii, my Myr!")


@bot.message_handler(commands=['Bye'])
def bye(message):
    bot.send_message(
        message.chat.id, "Have a good day, " + str(message.from_user.first_name))


@bot.message_handler(func=lambda m: m.text == 'Tell me a secret')
def send(message):
    bot.send_message(message.chat.id, "Код нашей любовной переписки :" +
                     str(message.chat.id))


@bot.message_handler(func=lambda m: m.text == 'Hui')
def echo_all(message):
    bot.reply_to(message, "Voine")


@bot.message_handler(content_types=['document', 'audio'])
def handle_docs_audio(message):     bot.send_message(
    message.chat.id, 'Ebat kachaet')


@bot.message_handler(func=lambda m: m.text == 'Time')
def echo_all(message):
    date = message.date + 10800
    bot.reply_to(message,
                 str(datetime.datetime.utcfromtimestamp(date)))


@bot.message_handler(func=lambda m: m.text == 'Photo')
def photo(message):
    file = open('cute.png', 'rb')
    bot.send_photo(message.chat.id, file, 'Miy mya!')


@bot.message_handler(func=lambda m: m.text == 'Mult')
def url(message):
    markup = types.InlineKeyboardMarkup()
    btn_my_site = types.InlineKeyboardButton(
        text='Cat сайт', url='https://mults.info/mults/?id=534')
    markup.add(btn_my_site)
    bot.send_message(
        message.chat.id, "Нажми на кнопку и перейди на сайт.", reply_markup=markup)


@bot.message_handler(func=lambda m: m.text == 'Audio')
def send(message):
    bot.send_message(message.chat.id, 'Пришли мне muuusic')


@bot.message_handler(func=lambda message: True)
def all_messages(message):
    bot.send_message(message.chat.id, '"'+str(message.text) +
                     '"'+' -Its so boring,honey. '+'Just open a magic door: '+'/keyboard')


bot.polling()

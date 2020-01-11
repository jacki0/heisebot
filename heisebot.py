import telebot
import random
import string
import sched
import time
bot = telebot.TeleBot('         ')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Бот отправляет сообщение каждые 3 часа',
    reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])
def passwordgeneration(message):

bot.polling()
import telebot
from twisted.internet import task, reactor

bot = telebot.TeleBot('887793509:AAF_wasq78q0AUX37GgKaFV5IB_hi5NVnbo')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Бот отправляет сообщение каждые 3 часа')

    timeout = 25.0
    
    def msg():
        bot.send_message(message.chat.id, 'Бот отправляет сообщение каждые 3 часа')
    
    loop = task.LoopingCall(msg())
    loop.start(timeout)

bot.polling()

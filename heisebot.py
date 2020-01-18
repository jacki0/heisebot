import threading
import requests
import json
import re
import string


message = 'test message'
chat = '-321091116'
bot = '887793509:AAF_wasq78q0AUX37GgKaFV5IB_hi5NVnbo'

def sendmessage():
    threading.Timer(10800.0, sendmessage).start()      # Запуск функции каждые 3 часа
    link = 'https://api.telegram.org/bot' + bot + '/sendMessage?chat_id=' + chat + '&text=' + message
    requests.get(link)                                 # Отправка сообщения


def receivingmessage():
    threading.Timer(3590.0, receivingmessage).start()  # Запуск функции каждые 59 минут 50 секунд
    messages = []
    req = requests.get('https://api.telegram.org/bot' + bot + '/getupdates')
    data = json.dumps(req.json(), ensure_ascii=False).encode('utf8').decode().lower().split('"message"')
    for i in data:
        if '"type": "private"' in i:                   # Проверка, что сообщение было отправлено боту, а не в групповой чат
            i = i.split(', ')
            for j in i:
                if 'message_id' in j or 'text' in j:   # Получаем текст и id cообщения
                   j = re.sub('[{}]'.format(re.escape(string.punctuation)), '', j).split(' ')[-1]
                   messages.append(j)
    return messages                                    # Возвращаем результирующий список где чередутся текс и id сообщений

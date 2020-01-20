import threading
import requests
import psycopg2
import string
import json
import re


chat = '-321091116'
bot = '887793509:AAF_wasq78q0AUX37GgKaFV5IB_hi5NVnbo'

conn = psycopg2.connect(dbname='heisedb', user='heisen', password='Heisen!', host='localhost')
cursor = conn.cursor()

def sendmessage(message):
    link = 'https://api.telegram.org/bot' + bot + '/sendMessage?chat_id=' + chat + '&text=' + message
    requests.get(link)                                 # Отправка сообщения

def receivingmessage():
    messages = []
    ids = []
    req = requests.get('https://api.telegram.org/bot' + bot + '/getupdates')
    data = json.dumps(req.json(), ensure_ascii=False).encode('utf8').decode().lower()
    cursor.execute("SELECT last_send FROM messages")   # Получаем id последнего отправленного сообщения
    lastsend = cursor.fetchall()
    if '"message_id": ' + str(lastsend) in data:       # Проверка присутствия последнего отправленного в чат сообщения в полученных данных
        data = data.split('"message_id": ' + str(lastsend))
    for i in data.split('"message"'):
        if '"type": "private"' in i:                   # Проверка, что сообщение было отправлено боту, а не в групповой чат
            i = i.split(', ')
            for j in i:
                if 'text' in j:                        # Получаем текст cообщения
                    j = re.sub('[{}]'.format(re.escape(string.punctuation)), '', j.split(': ')[-1])
                    messages.append(j)
                elif 'message_id' in j:                # Получаем id сообщения
                    j = re.sub('[{}]'.format(re.escape(string.punctuation)), '', j.split(': ')[-1])
                    ids.append(j)
    return list(zip(messages, ids))                    # Возвращаем итератор содержащий пары (текст, id) сообщения

def insertdb():
    threading.Timer(3590.0, insertdb).start()          # Запуск функции каждые 59 минут 50 секунд
    messages = receivingmessage()
    for i in messages:
        cursor.execute("INSERT into messages(message, message_id) VALUES (%s, %s)", i)

def extractdb():
    threading.Timer(10800.0, extractdb).start()        # Запуск функции каждые 3 часа
    messages =[]
    cursor.execute("SELECT last_send FROM messages")   # Получаем id последнего отправленного сообщения
    lastsend = cursor.fetchall()
    cursor.execute("SELECT messages where message_id > " + lastsend)            # Получаем получаем список не отправленных на момент запуска функции сообщений
    rows = cursor.fetchall()
    for row in rows:
        messages.append(row)
    for message in messages:                           # Отправка сообщений
        sendmessage(message)

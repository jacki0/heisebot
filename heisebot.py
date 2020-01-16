import threading
import requests
import json
import re
import string

message = 'А я сказал, @atlasovNV будет здесь!!!'
chat = '-321091116'
bot = '887793509:AAF_wasq78q0AUX37GgKaFV5IB_hi5NVnbo'

def sendmessage(message, chat):
    threading.Timer(10800.0, sendmessage, args=(message, chat)).start()
    link = 'https://api.telegram.org/bot' + bot + '/sendMessage?chat_id=' + chat + '&text=' + message
    requests.get(link)

def receivingmessage():
    threading.Timer(3590.0, receivingmessage).start()
    messages = []
    ids = []
    req = requests.get('https://api.telegram.org/bot' + bot + '/getupdates')
    data = json.dumps(req.json(), ensure_ascii=False).encode('utf8').decode().lower().split('"message"')
    for i in data:
        if '"type": "private"' in i:
            i = i.split(', ')
            for j in i:
                if 'message_id' in j:
                    j = re.sub('[{}]'.format(re.escape(string.punctuation)), '', j).split(' ')[-1]
                    ids.append(int(j))
                elif 'text' in j:
                    j = j.split(': ')[-1]
                    j = re.sub('[{}]'.format(re.escape(string.punctuation)), '', j)
                    messages.append(j)
    messages.insert(0, max(ids))
    return messages

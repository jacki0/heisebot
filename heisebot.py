import threading
import requests
import json

message = 'А я сказал, @atlasovNV будет здесь!!!'
chat = '-321091116'
bot = '887793509:AAF_wasq78q0AUX37GgKaFV5IB_hi5NVnbo'

def sendmessage(message, chat):
    threading.Timer(5.0, msg, args=(message, chat)).start()
    link = 'https://api.telegram.org/bot' + bot + '/sendMessage?chat_id=' + chat + '&text=' + message
    requests.get(link)

def receivingmessage():
    messages = []
    req = requests.get('https://api.telegram.org/bot' + bot + '/getupdates')
    data = json.dumps(req.json(), ensure_ascii=False).encode('utf8').decode().lower().split('"text": ')

#sendmessage(message, chat)
receivingmessage()
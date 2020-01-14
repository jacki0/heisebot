import threading
import requests

message = 'А я сказал, @atlasovNV будет здесь!!!'
chat = '-321091116'

def msg(message, chat):
    threading.Timer(5.0, msg, args=(message, chat)).start()
    link = 'https://api.telegram.org/bot887793509:AAF_wasq78q0AUX37GgKaFV5IB_hi5NVnbo/sendMessage?chat_id=' + chat + '&text=' + message
    requests.get(link)

msg(message, chat)
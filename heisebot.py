import threading
import requests

def msg():
    message = 'Привет, @atlasovNV!'
    threading.Timer(15.0, msg).start()
    link = 'https://api.telegram.org/bot887793509:AAF_wasq78q0AUX37GgKaFV5IB_hi5NVnbo/sendMessage?chat_id=-321091116&text='
    requests.get(link + message)

msg()

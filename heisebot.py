from twisted.internet import task, reactor
import requests

timeout = 25.0

def msg():
    aa = 'https://api.telegram.org/bot887793509:AAF_wasq78q0AUX37GgKaFV5IB_hi5NVnbo/sendMessage?chat_id=-453849336text='
    bb = 'Cообщение'
    requests.get(aa + bb)

loop = task.LoopingCall(msg())
loop.start(timeout)

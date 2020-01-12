from twisted.internet import task, reactor
import requests

timeout = 25.0

def msg(message):
    link = 'https://api.telegram.org/bot887793509:AAF_wasq78q0AUX37GgKaFV5IB_hi5NVnbo/sendMessage?chat_id=-321091116text='
    requests.get(link + message)

loop = task.LoopingCall(msg('Сообщение'))
loop.start(timeout)

reactor.run()

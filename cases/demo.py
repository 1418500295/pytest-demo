import  gevent,requests
from multiprocessing import Process,Pool
import os
from websocket import *

def send_req():
    ws = create_connection("ws://localhost:1423")
    ws.send("你好啊")

def run():
    g_list = []
    for i in range(500):
        g = gevent.spawn(send_req())
        g_list.append(g)
    gevent.joinall(g_list)


if __name__ == '__main__':
    for i in range(4):
        p = Process(target=run)
        p.start()




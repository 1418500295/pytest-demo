import  gevent,requests
from multiprocessing import Process,Pool
import os,functools
import time
import pytest
from websocket import *

def send_req():
    ws = create_connection("ws://localhost:1423")
    ws.send("你好啊")
    print(ws.recv())

def run():
    g_list = []
    for i in range(100):
        g = gevent.spawn(send_req())
        g_list.append(g)
    gevent.joinall(g_list)


if __name__ == '__main__':
    # start_time = None
    # for i in range(4):
    #     start_time = time.time()
    #     p = Process(target=run)
    #     p.start()
    # need_time = time.time() - start_time
    # print(start_time)
    # print(need_time)

    def run_time(process_run):
        def wrapper():
            start_time = time.time()
            process_run()
            end_time = time.time()
            print(end_time-start_time)
        return wrapper

    @run_time
    def process_run():
        for i in range(4):
            p = Process(target=run)
            p.start()
    process_run()


if __name__ == '__main__':

    base = dict()
    base['name'] = 'daine'



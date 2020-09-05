import  gevent,requests
from multiprocessing import Process,Pool
import os,functools
import time
import pytest
from websocket import *

ok_num = 0

def send_req():
    ws = create_connection("ws://localhost:1423")
    ws.send("呵呵")
    print("服务端的回复是",ws.recv())

def create_gevent():
    g_list = []
    for i in range(5000):
        current_gevent = gevent.spawn(send_req())
        g_list.append(current_gevent)
    gevent.joinall(g_list)



if __name__ == '__main__':
    # start_time = time.time()

    print("开始时间是" + time.strftime("%Y-%m-%d  %H-%M-%S", time.localtime()))
    def process_run():
        for i in range(4):
            p = Process(target=create_gevent)
            p.start()
        p.join()
    process_run()
    print("结束时间是" + time.strftime("%Y-%m-%d  %H-%M-%S", time.localtime()))
    print("成功的请求数",ok_num)










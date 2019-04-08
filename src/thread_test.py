import threading
import time
from threading import current_thread #从current_thread模块可以看到当前线程运行的状态和信息


def MyThread(arg1, arg2):
    print(current_thread().getName(), 'start')
    print("%s %s" % (arg1, arg2))
    time.sleep(1)
    print(current_thread().getName(), 'stop')


for i in range(1, 6, 1):
    MyThread(i, i+1)
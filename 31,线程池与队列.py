import threading
import time

from multiprocessing.dummy import Pool
# 导入线程池用的不是from multiprocessing.pool import Pool(这个是进程池, 切记)
from queue import Queue
#from multiprocessing import JoinableQueue(这个是多进程例的队列,不能混)

pool = Pool()
queue = Queue()
def func():
    for i in range(1, 99):
        print("添加{}".format(i))
        queue.put(i)
        time.sleep(0.01)



def func2():
    for i in range(1,99):
        print("取出{}".format(i))
        queue.get()
        queue.task_done()
        time.sleep(0.03)

def error_call_back(e):
    print(e)

pool.apply_async(func, error_callback=error_call_back)
pool.apply_async(func2, error_callback=error_call_back)
#
#
# time.sleep(1)
# queue.join()

pool.close()
pool.join()
import threading
import time


def func():
    for i in range(1,10):
        print(threading.current_thread().getName())
        time.sleep(0.02)


t1 = threading.Thread(target=func)
t1.setDaemon(True)
t2 = threading.Thread(target=func)
t2.setDaemon(True)
t1.start()
t2.start()
t1.join()
print("主线程结束")

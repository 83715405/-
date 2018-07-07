from multiprocessing.dummy import Pool

import time

pool = Pool()


def func(a):
    for i in range(1, 10):
        print(a, i)
        # 使用线程池的时候,如果程序例报错,会通过error_callback返回, 如果没定义该方法
        # 则默认忽略该异常,出现错误的线程会自动关闭
        1 / 0
        time.sleep(0.1)


# 这里的e会自动传进去
def error_callback(e):
    print(e)
    return e


# 同步执行
# pool.apply(func, args=("t1",))
# pool.apply(func, args=("t2",))
pool.apply_async(func, args=("t1",), error_callback=error_callback)
pool.apply_async(func, args=("t2",), error_callback=error_callback)

pool.close()
pool.join()

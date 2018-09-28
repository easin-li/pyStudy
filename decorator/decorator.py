# -*- coding: UTF-8 -*-
# 遵守开放封闭原则
import time


def f():
    print('hello,world')

start = time.time()
f()
time.sleep(1)


end = time.time()
print(end - start)

##################### 装饰器 #######################
def show_time(f):
    def inner():
        start_time = time.time()
        f()
        time.sleep(2)
        end_time = time.time()
        print(f.__name__ + '执行了' + str(end_time - start_time) + '秒')
    return inner

@show_time  # 等价于 foo = show_time(foo)
def foo():
    print('foo...')
@show_time
def bar():
    print('bar...')

foo()
bar()
##################### 装饰器 #######################



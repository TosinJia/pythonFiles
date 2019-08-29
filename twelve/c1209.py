import time


# 类似闭包
def decorator(func):
    # 封装
    def wrapper():
        print(time.time())
        func()
    return wrapper


def f1():
    print('This is a function')


f = decorator(f1)
f()


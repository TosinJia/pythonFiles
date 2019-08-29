import time


def decorator(func):
    def wrapper():
        print(time.time())
        func()
    return wrapper


@decorator
def f1():
    print('This is a function')


# 装饰器优势 无需改变调用方式
f1()

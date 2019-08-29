import time


def decorator(func):
    # 可变参数
    def wrapper(*args):
        print(time.time())
        func(*args)
    return wrapper


@decorator
def f1(func_name):
    print('This is a function named ' + func_name)


@decorator
def f2(func_name1, func_name2):
    print(func_name1, func_name2)


f1('test')
f2('test1', 'test2')

import time


def decorator(func):
    # 可变参数 关键字参数
    def wrapper(*args, **kw):
        print(time.time())
        func(*args, **kw)
    return wrapper


@decorator
def f1(func_name):
    print('This is a function named ' + func_name)


@decorator
def f2(func_name1, func_name2):
    print(func_name1, func_name2)


# f3新增关键字参数
@decorator
def f3(func_name1, func_name2, **kw):
    print(func_name1, func_name2)
    # kw 作为一个字典
    print(kw)


f3('tes1', 'test2', a=1, b=2, c='123')
f2('test1', 'test2')
f1('test')

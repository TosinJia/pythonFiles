import time


def f1():
    # unix 时间戳
    print(time.time())
    print('This is a function')


f1()


# 开闭原则
def f2():
    print('This is a function')


def print_current_time(func):
    print(time.time())
    func()


# 等价于
# print(time.time())
# f1()
# print(time.time())
# f2()
print_current_time(f1)
print_current_time(f2)

# 关键 新增的需求属于每个函数本身，不是属于新增加的函数；新增的业务逻辑依然可以和原函数绑定在一起，体现出是对原函数功能的扩展，同时又不去更改原函数内部的实现








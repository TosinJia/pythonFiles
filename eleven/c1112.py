# 使用闭包时要注意
def f1():
    a = 10
    b = 20

    def f2():
        # a此时将被python认为是一个局部变量，局部变量是不可能影响到外部变量的；不是一个闭包
        # a = 20
        print(a, b)

    print(a)
    f2()
    print(a)
    return f2


f = f1()
print(f, f.__closure__)
print(f.__closure__[0].cell_contents, f.__closure__[1].cell_contents)


# 使用闭包时要注意
def f1():
    a = 10

    def f2():
        a = 20
        print(a)
    print(a)
    f2()
    print(a)

f1()





def curve_pre():
    a = 25

    def curve(x):
        return a*x*x
    return curve


def curve_pre1():
    a = 30

    def curve(x):
        return a*x*x
    return curve




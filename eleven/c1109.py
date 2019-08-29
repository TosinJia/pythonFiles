a = 1
a = '2'

def add(x, y):
    return x + y

# <class 'function'>
print(add(1, 2), type(add))
# Python里可以把函数赋值给一个变量
a = add
print(a(3, 4))

# 把函数当做另外一个函数的参数，传递到另外的函数里
# 把一个函数当做另外一个函数的返回结果

# 函数里边再定义函数
def curve_pre():
    def curve():
        print('This is a function')
    # 函数可以作为返回结果被返回回来
    return curve

# 可以把函数赋值给变量
f = curve_pre()
f()


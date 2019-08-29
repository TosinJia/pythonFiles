# 匿名函数
def add(x, y):
    return x + y


# 匿名函数赋值给一个变量，等同于定义了一个名字
f = lambda x, y: x + y
# 不能再lambda里的表达式里做赋值操作
# f = lambda x, y: a = x + y
print(add(1, 2), f(1, 2))

# 正则表达式有一个地方非常适合用匿名函数

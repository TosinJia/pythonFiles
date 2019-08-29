
# 函数里边再定义函数
def curve_pre():
    # 局部变量定义
    a = 25

    def curve(x):
        return a*x*x

    # 函数可以作为返回结果被返回回来
    return curve

# 在模块里修改a的值，不影响闭包里函数的环境变量
a = 10
# 可以把函数赋值给变量
f = curve_pre()
# 打印 闭包对象，闭包的环境变量
print(f.__closure__, f.__closure__[0].cell_contents)
print(f(2))


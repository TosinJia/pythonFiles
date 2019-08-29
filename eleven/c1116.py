# 起始坐标
origin = 0

# 工厂模式 闭包可以利用函数式编程的方式来做工厂模式的
def factory(pos):
    def go(step):
        nonlocal pos
        new_pos = pos + step
        pos = new_pos
        return new_pos
    return go


def curve_pre():
    a = 25

    def curve(x):
        return a*x*x
    return curve


f = curve_pre()
print(f, f.__closure__[0].cell_contents)
# 在函数的外部间接地调用函数内部的变量
print(f(2))

# 起始坐标
origin = 0


def go1(step):
    new_pos = origin + step
    # 注释掉 上一行origin查找到外边的origin；出现在等号左边的是局部变量，如果存在局部变量，不会去寻找作用域链外部的变量
    # origin = new_pos
    return new_pos

def go(step):
    # global关键字 声明全局变量
    global origin
    new_pos = origin + step
    # 注释掉 上一行origin查找到外边的origin；出现在等号左边的是局部变量，如果存在局部变量，不会去寻找作用域链外部的变量
    origin = new_pos
    return new_pos


print(go(2))
print(go(3))
print(go(6))

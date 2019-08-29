# 起始坐标
origin = 0


# 环境变量 pos
def factory(pos):
    # 环境变量 pos
    # pos = 0

    def go(step):
        # nonlocal关键字 声明不是局部变量
        nonlocal pos
        new_pos = pos + step
        pos = new_pos
        return new_pos

    return go


g = factory(origin)
print(g, g.__closure__, g.__closure__[0].cell_contents)
print(g(2))
print('闭包环境变量：'+str(g.__closure__[0].cell_contents))
print(g(3))
print('闭包环境变量：'+str(g.__closure__[0].cell_contents))
print(g(6))
# 闭包环境变量记住了上一次的状态
print('闭包环境变量：'+str(g.__closure__[0].cell_contents))

# 不会改变全局变量origin值，所有的操作都是局限于函数的内部
print(origin)

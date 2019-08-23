# 全局变量c
c = 5


def add(x, y):
    # 局部变量c
    c = x + y
    print(c)
    return c


add(1, 2)
# 局部变量不会覆盖全局变量
print(c)

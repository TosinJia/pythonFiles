# 必须参数
# 形式参数 在函数定义的过程中
def add(x, y):
    result = x + y
    return result


# 实际参数 函数调用的过程中
print(add(1, 2))
# 关键字参数 函数调用过程中指定实参、形参对应关系，提供代码可读性
print(add(y=1, x=2))



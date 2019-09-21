a = [1, 2, 3, 4, 5, 6, 7, 8]

# a列表中每个元素平方
# 1.for循环
# 2.高阶函数 map
# 3.列表推导式
b1 = [i*i for i in a]
b2 = [i**2 for i in a]
print(b1, b2)

# 有选择性地对a列表中筛选出的元素进行平方，推荐使用列表推导式
# 1. map filter 稍复杂些
b3 = [i**2 for i in a if i > 5]
print(b3)

# set集合推导式
a = {1, 2, 3, 4, 5, 6, 7, 8}
b1 = {i**2 for i in a if i > 5}
print(b1)

# 元组也可以推导
a = (1, 2, 3, 4, 5, 6, 7, 8)
b1 = [i**2 for i in a if i > 5]
print(b1)

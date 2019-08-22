a = 1
b = 2
c = 3

a, b, c = 1, 2, 3
print(a, b, c)

# 序列解包
d = 1, 2, 3
print(type(d))
a, b, c = d
print(a, b, c)
a, b, c = ['a', 'b', 'c']
print(a, b, c)

# 多个变量同时赋值
a = 1
b = 1
c = 1
a, b, c = 1, 1, 1
a = b = c = 1
print(a, b, c)

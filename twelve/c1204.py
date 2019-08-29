# map
list_x = [1, 2, 3, 4, 5, 6, 7, 8]
list_y = [1, 2, 3, 4, 5, 6]


# 用lambda表达式替换square函数
r = map(lambda x: x*x, list_x)
print(list(r))

# 多个参数的匿名函数（lambda表达式）
r = map(lambda x, y: x*x + y, list_x, list_y)
print(list(r))

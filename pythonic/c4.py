# dict字典推导式
students = {
    "tosin": 20,
    "jaky": 18,
    "tom": 22
}

# 字典的key组装成列表
b1 = [key for key, value in students.items()]

# 字典key，value颠倒
b2 = {value: key for key, value in students.items()}

# 元组推导 得到的是可遍历的对象genexpr，不是元组；
b3 = (key for key, value in students.items())
print(b1, b2, b3)
# 遍历的对象genexpr
for x in b3:
    print(x)


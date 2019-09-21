none = None
print(type(none))

a = ""
b = False
c = []
d = 0

# 值比较运算
print(a==None, b ==None, c==None, d==None)

# 类型比较运算
print(a is None, b is None, c is None, d is None)


# 判空操作
def func():
    # T T
    # return None
    # T F
    # return []
    # return 0
    # return ""
    return False

a = func()
if not a:
    print("T")
else:
    print("F")

if a is None:
    print("T")
else:
    print("F")

# 推荐if a: if not a: 进行判空操作
if a:
    print("T")
else:
    print("F")

print(type(None), type(False))
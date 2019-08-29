
from enum import Enum


class VIP(Enum):
    YELLOW = 1
    GREEN = 2
    BLACK = 3
    RED = 4

# 枚举相关的操作
# 获取枚举类型下某一个标签对应的数值
print(VIP.YELLOW.value)

# 获取枚举类型下某一个枚举名称对应的枚举标签名字
print(VIP.YELLOW.name)
print(VIP.YELLOW)
# VIP.YELLOW.value 枚举值；VIP.YELLOW.name 枚举标签名字；VIP.YELLOW 枚举下的一个类型
print(type(VIP.YELLOW.name), type(VIP.YELLOW))

# 通过名称获取名称所对应的枚举类型，枚举名称和枚举本身不是一个东西
print(VIP['YELLOW'], VIP[VIP.YELLOW.name])

# 枚举类型是可以遍历的
for v in VIP:
    print(v)

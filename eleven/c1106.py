from enum import Enum


class VIP(Enum):
    YELLOW = 1
    GREEN = 2
    BLACK = 3
    RED = 4


# 数值转换为枚举类型
a = 1
print(VIP(a))

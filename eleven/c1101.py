from enum import Enum


# 所有枚举类都是Enum的子类
class VIP(Enum):
    # 枚举类型建议大写
    YELLOW = 1
    GREEN = 2
    BLACK = 3
    RED = 4


# 普通类打印出来的是标签数值，枚举类打印出来的是标签
print(VIP.YELLOW)



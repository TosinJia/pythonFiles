from enum import Enum


class VIP(Enum):
    YELLOW = 1
    GREEN = 2
    BLACK = 3
    RED = 4


# 两个枚举之间是可以进行等值比较的
result = VIP.YELLOW == VIP.GREEN
print(result)
result = VIP.YELLOW == VIP.YELLOW
print(result)
result = VIP.GREEN == 2
print(result)

# TypeError: '>' not supported between instances of 'VIP' and 'VIP'
# result = VIP.YELLOW > VIP.GREEN
# print(result)
# 两个枚举之间是可以进行身份比较的
result = VIP.YELLOW is VIP.YELLOW
print(result)


class VIP1(Enum):
    YELLOW = 1
    GREEN = 2
    BLACK = 3
    RED = 4

# 不同枚举类型间比较
print(VIP.YELLOW == VIP1.YELLOW)

from enum import Enum


class VIP(Enum):
    YELLOW = 1
    # 别名
    YELLOW_ALIAS = 1
    GREEN = 2
    BLACK = 3
    RED = 4

# YELLOW，YELLOW_ALIAS 打印出的是 VIP.YELLOW，别名
print(VIP.YELLOW_ALIAS)

# 遍历时只会打印一次
for v in VIP:
    print(v)

# 遍历结果 元组(标签名称，标签名称所对应的具体取值)
for v in VIP.__members__.items():
    print(v)

# 遍历标签名称
for v in VIP.__members__:
    print(v)
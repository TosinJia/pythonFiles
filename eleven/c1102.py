
# 表示类型
# 1. 模块里的变量
yellow = 1
green = 2

# 2. 字典
a = {'yellow': 1, 'green': 2}
a['yellow'] = 3


# 3. 类，类变量
class Type():
    YELLOW = 1
    GREEN = 2

# 字典、类变量表示类型缺陷 1. 可变 2. 没有防止相同标签的功能
Type.YELLOW = 6

# 枚举类型
from enum import Enum

# 重复标签 TypeError: Attempted to reuse key: 'YELLOW'
class VIP(Enum):
    YELLOW = 1
    GREEN = 2
    BLACK = 3
    RED = 4

# 枚举下定义的一个个类型是不能轻易被更改， AttributeError: Cannot reassign members.
# VIP.YELLOW = 6

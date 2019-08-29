from enum import Enum
from enum import IntEnum, unique


@unique
class VIP2(IntEnum):
    YELLOW = 1
    # ValueError: duplicate values found in <enum 'VIP2'>: GREEN -> YELLOW
    # GREEN = 1
    BLACK = 3
    RED = 4


class VIP1(IntEnum):
    YELLOW = 1
    # ValueError: invalid literal for int() with base 10: 'b'
    # GREEN = 'b'
    BLACK = '3'
    RED = 4


class VIP(Enum):
    YELLOW = 1
    GREEN = 'b'
    BLACK = '3'
    RED = 4





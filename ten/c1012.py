# 把函数作为参数传递 正则替换
import re
s = "ABC296D99977"

def convert(value):
    matched = value.group()
    if int(matched) >= 6:
        return "9"
    else:
        return "0"


# 大于6的数值替换为9，小于6的数值替换成0
print(re.sub('\d', convert, s), re.sub('[\\d]', convert, s))

s = "ABC29D6E99F977"
def convert1(value):
    matched = value.group()
    if int(matched) >= 50:
        return "100"
    else:
        return "0"
# 两位数字大于50替换成100，小于50替换成0
print(re.sub('\d{2}', convert1, s))


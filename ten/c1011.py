# 正则替换
import re

lanuage = "PythonC#JavaC#PHPC#"

r = re.sub('C#', 'GO', lanuage)
print(r)
r = re.sub('C#', 'GO', lanuage, 1)
print(r)
print(lanuage.replace('C#', 'GO'), lanuage.replace('C#', 'GO', 1))


def convert(value):
    # return "!!" + value + "!!"    # TypeError: can only concatenate str (not "re.Match") to str
    # print(value) #<re.Match object; span=(6, 8), match='C#'>
    matched = value.group()
    return "!!" + matched + "!!"


# 将正则匹配的结果传递给convert，convert的返回结果将用于替换
print(re.sub('C#', convert, lanuage))

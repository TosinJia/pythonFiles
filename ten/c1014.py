import re
s = "life is short, i use python"

# 提取life python之间的字符
print(re.findall('life[\w]+python', s), re.findall('life.+python', s))
# 只有一个分组小括号可加，也可不加；默认把全部的正则表达式当做一个分组
r = re.search('life.+python', s)
# group可以传入组号，0是默认的取值，可以省略
print(r, r.group())
r = re.search('(life.+python)', s)
print(r, r.group(0))

r = re.search('life(.*)python', s)
print(r.group(0), ":", r.group(1))

print(re.findall('life(.*)python', s))

s = "life is short, i use python, i love python"
# 提取life python之间的字符，同时提取两个python之间的字符
print(re.findall('life(.*)python(.*)python', s))
r = re.search('life(.*)python(.*)python', s)
print(r.group(0), "\r\n", r.group(1), "\r\n", r.group(2))
# group可以同时指定多个组号
print(r.group(0, 1, 2))
# 没有完整的匹配结果
print(r.groups())

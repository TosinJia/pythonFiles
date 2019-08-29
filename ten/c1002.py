import re
# 提取数字
a = '1C0C++1Python2Java3Python4JavaScript'

# 元字符 https://baike.baidu.com/item/%E6%AD%A3%E5%88%99%E8%A1%A8%E8%BE%BE%E5%BC%8F
r = re.findall('\d', a)
print(r)

# 提取非数字
r = re.findall('\D', a)
print(r)
# 数字开头
r = re.findall('^\d', a)
print(r)
# 提取非数字
r = re.findall('[^\d]', a)
print(r)



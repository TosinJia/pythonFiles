# 数量词
import re
# 元字符 https://baike.baidu.com/item/%E6%AD%A3%E5%88%99%E8%A1%A8%E8%BE%BE%E5%BC%8F
a = "python11java22php_ &\n\r\t\v\f"
r = re.findall('[a-z][a-z][a-z]', a)
print(r)
r = re.findall('[a-z]+', a)
print(r)
r = re.findall('[a-z]{3,6}', a)
print(r)
r = re.findall('[a-z]{3,6}?', a)
print(r)
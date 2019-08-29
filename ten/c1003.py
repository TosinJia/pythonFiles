# 字符集
import re
S = 'abc, acc, adc, aec, afc, ahc'

# 元字符 https://baike.baidu.com/item/%E6%AD%A3%E5%88%99%E8%A1%A8%E8%BE%BE%E5%BC%8F
# 匹配中间字符是cfd的单词 a[c|f]c 等价 a[cf]c
r = re.findall('a[cfd]c', S)
print(r)
# 取反操作^
r = re.findall('a[^cfd]c', S)
print(r)
r = re.findall('a[c-f]c', S)
print(r)


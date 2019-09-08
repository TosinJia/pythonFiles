# 边界匹配
import re
# 元字符 https://baike.baidu.com/item/%E6%AD%A3%E5%88%99%E8%A1%A8%E8%BE%BE%E5%BC%8F
qq = "10000001"
# 匹配完整的字符串
r = re.findall('^[\d]{4,8}$', qq)
print(r)
print(re.findall('^000', qq), re.findall('000$', qq))

# 概括字符集
import re
# 元字符 https://baike.baidu.com/item/%E6%AD%A3%E5%88%99%E8%A1%A8%E8%BE%BE%E5%BC%8F
a = "python11java22php_ &\n\r\t\v\f"
r = re.findall('\d', a)
print(r)
r = re.findall('[0-9]', a)
print(r)

print(re.findall('\D', a), re.findall('[^0-9]', a))

print(re.findall('\w', a), re.findall('[A-Za-z0-9_]', a))
print(re.findall('\W', a), re.findall('[^A-Za-z0-9_]', a))
# 空白字符
print(re.findall('\s', a), re.findall('[ \r\n\t\v\f]', a))
print(re.findall('\S', a), re.findall('[^ \r\n\t\v\f]', a))

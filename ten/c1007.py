# 贪婪与非贪婪
import re
# 元字符 https://baike.baidu.com/item/%E6%AD%A3%E5%88%99%E8%A1%A8%E8%BE%BE%E5%BC%8F
a = "pytho0python2pythonn3"
r = re.findall('python*', a)
print(r)
r = re.findall('python+', a)
print(r)
r = re.findall('python?', a)
print(r)
print(re.findall('python{1,2}', a), re.findall('python{1,2}?', a))
print(re.findall('python?', a), re.findall('python??', a))
# 匹配模式
import re
# 元字符 https://baike.baidu.com/item/%E6%AD%A3%E5%88%99%E8%A1%A8%E8%BE%BE%E5%BC%8F
lanuage = "PythonC#\nJavaPHP"

r = re.findall('c#', lanuage)
print(r)
# 忽略大小写
r = re.findall('c#', lanuage, re.I)
print(r)
# .点 | 匹配除“\n”和"\r"之外的任何单个字符。要匹配包括“\n”和"\r"在内的任何字符，请使用像“[\s\S]”的模式
# re.S 作用改变.点的行为 可以匹配“\n”
print(re.findall('c#.{1}', lanuage, re.I), re.findall('c#.{1}', lanuage, re.I | re.S))

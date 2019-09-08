# 组
import re
# 元字符 https://baike.baidu.com/item/%E6%AD%A3%E5%88%99%E8%A1%A8%E8%BE%BE%E5%BC%8F
a = "PythonPythonPythonJSPythonPython"
# 是否包含3个Python
r = re.findall('PythonPythonPython', a)
print(r)
# 多个组
r = re.findall('(Python){3}(JS)', a)
print(r)


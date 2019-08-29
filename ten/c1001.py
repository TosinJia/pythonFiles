a = 'C|C++|Python|Java'

# Python1 ValueError: substring not found
print(a.index('Python'))
print('Python' in a)

a = 'C|C++|Python|Java|Python|JavaScript'

import re
# 普通字符
r = re.findall('Python1', a)
print(r)
if len(r) > 0:
    print('包含指定字符串')
else:
    print('不包含指定字符串')



# 死循环 Ctrl+C 终止
''''
CONDITION = True

while CONDITION:
    print('while loop')
'''

# 0时不打印任何内容
counter = 0
while counter <= 10:
    counter += 1
    print(counter)
else:
    #循环结束时执行
    print('END')


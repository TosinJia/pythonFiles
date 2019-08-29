list_x = [1, 0, 2, 3, 0, 4, 5, 0, 6, 7, 8]

# r = filter(lambda x: x>0, list_x)
# r = filter(lambda x: x, list_x)
r = filter(lambda x: True if x > 0 else False, list_x)
# 保留大写字母
list_u = ['a', 'B', 'c', 'F', 'e']

# ord() 获取字符ascii码
print(ord('A'), ord('Z'))
r = filter(lambda x: True if ord(x)>=65 and ord(x)<=90 else False, list_u)

print(list(r))


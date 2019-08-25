a=['A','B','C','D']
for x in a:
    print(x)

# 当列表里的元素被遍历完后，else分支下的语句块会执行
a=[['A','B','C','D'],(1,2,3)]
for x in a:
    for y in x:
        if y=='B':
            break
        print(y)
else:
    print('END.')

# break 终止当前循环，不会执行else分支下的语句块；continue 跳过当前循环，会执行else分支下的语句块
a = [1,2,3]
for x in a:
    if x==2:
        #break
        continue
    print(x)
else:
    print('END.')

a=[['A','B','C','D'],(1,2,3)]
for x in a:
    if 'B' in x:
        break
    for y in x:
        if y=='B':
            break
        print(y)
else:
    print('END.')

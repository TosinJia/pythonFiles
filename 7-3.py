
# 让一段代码执行10次
a=[1,2,3,4,5,6,7,8,9,10]
for x in a:
    print(x)
print('Range:')

# start stop step
for x in range(1,11):
    print(x, end=' | ')

# 思考题
print('思考题')
a=[1,2,3,4,5,6,7,8]
for x in a:
    if x%2== 1:
        print(x, end=" | ")
print('等差数列方式：')
# 利用range生成一个等差数列，把这个数列作为a的下标
for i in range(0, len(a), 2):
    print(a[i], end=" | ")

# 序列切片 步长：每隔多少个元素取一个
print('切片方式：')
b = a[0:len(a):2]
print(b)
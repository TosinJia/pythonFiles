from functools import reduce
# list_x = [1, 2, 3, 4, 5, 6, 7, 8]
list_x = ['1', '2', '3', '4', '5', '6', '7', '8']


# 连续计算，连续调用lambda
# r = reduce(lambda x, y: x + y, list_x)
# (((1+2)+3)+4)+5

r = reduce(lambda x, y: x + y, list_x, '10')
print(r)


# 旅行者二维空间 (x,y)
# 起始点(0, 0)
# [(1,3),(2,-2),(-2,3) ...]
# 需要连续计算可以用reduce来解决


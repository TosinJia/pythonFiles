'''
模块说明
'''

ACCOUNT='tosin'
PASSWORD='123'
# constant 常量
print('please input account: ')
INPUT_ACCOUNT=input()
print('please input password: ')
INPUT_PASSWORD=input()
# 逻辑 优先级小于 比较
# :前不能加空格
# 比较运算符 前后空格
if ACCOUNT == INPUT_ACCOUNT and PASSWORD == INPUT_PASSWORD:
    print('成功登陆')
else:
    print('用户名密码错误')

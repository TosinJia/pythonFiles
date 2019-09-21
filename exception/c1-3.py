# Exception  # 常规异常的基类
class MyException(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


try:
    raise MyException('自定义异常')
except MyException as e:
    print('发生自定义异常', e.msg)



# def funcname(parameter_list):
#     pass

# def funcname(self, parameter_list):
#     raise NotImplementedError    

# def funcname(self, parameter_list):
#     pass    

# @staticmethod
# def funcname(parameter_list):
#     pass    

def add(x, y):
    result = x +y
    return result

# 设置最大递归调用次数
import sys
sys.setrecursionlimit(50)

# 递归调用，递归默认重复次数
#def print(info):
def print_info(info):
    print(info)
    return None

result1 = add(1,2)
result2 = print_info('TEST INFO')

print(result1, result2)
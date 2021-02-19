# -*- coding: UTF-8 -*-

print("type(1): {}".format(type(1)))
print("type(1.1): {}".format(type(1.1)))


print("type(1+1): {}".format(type(1+1)))
print("type(1+1.1): {}".format(type(1+1.1)))

print(bool(""))

print("c:\new\tem")
print("c:\\new\\tem")

# 当一个字符串前面加入一个r后，不是一个普通字符串，而是一个原始字符串（所见即所得）
print(r"c:\new\tem")
print(R"c:\new\tem")


# 导入 random(随机数) 模块
import random
# 生成 0 ~ 30 之间的随机数
print(random.randint(0, 30))



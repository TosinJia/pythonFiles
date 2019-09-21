class Test():
    pass


test = Test()
# 对象判断空 test None
print(bool(None), bool([]), bool(""), bool(0))
if test:
    print(bool(test), "T")
else:
    print(bool(test), "F")


class Test():
    def __len__(self):
        return 0


test = Test()
# 对象判断空 test None
if test:
    print(bool(test), "T")
else:
    print(bool(test), "F")

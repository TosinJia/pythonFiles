class Test():
    def __len__(self):
        return 0

    def __bool__(self):
        return False


class Test1():
    pass


class Test2():
    def __len__(self):
        return 0


class Test3():
    def __len__(self):
        return 8

test1 = Test1()
test2 = Test2()
test3 = Test3()
print(bool(test1), bool(test2), bool(test3))
class Test4():
    # pass
    # TypeError: 'str' 'float' object cannot be interpreted as an integer
    def __len__(self):
        return False

test4 = Test4()
# 没有__bool__方法，bool()由__len__决定
print(bool(test4), len(test4), test4.__len__())

class Test5():
    def __len__(self):
        return 5

    def __bool__(self):
        return False

    def __nozero__(self):
        """
        Python 2 没有 __bool__
        :return:
        """
        pass

test5 = Test5()
# __len__ __bool__都有，bool() 由__bool__决定
print(bool(test5), len(test5), test5.__len__())

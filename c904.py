
class Student():
    name = ''
    age = 0

    # 构造函数
    # def __init__(self):
    #     print('student')
        # return None
        # TypeError: __init__() should return None, not 'int'
        # return 1

    def __init__(self, name, age):
        # 初始化对象的属性
        # 不等价于 name = name；不等同于 局部变量不会覆盖全局变量；类变量和实例变量
        self.name = name
        self.age = age

    def do_homework(self):
        print('do homework')


student = Student('tosin', 20)
print(student.name, student.age)

# a = student.__init__()
# print(type(a))
# student1 = Student()
# student2 = Student()
# student3 = Student()
#
# print(id(student1))
# print(id(student2))
# print(id(student3))




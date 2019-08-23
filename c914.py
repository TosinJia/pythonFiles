# import c91401
# class Student(c91401.Human):
from c91401 import Human


# Student继承Human
class Student(Human):
    # sum = 0

    def __init__(self, school, name, age):
        self.school = school
        # 子类构造函数调用父类构造函数，必须手动传入self
        # 一个类调用一个实例方法，说不通，无意义，不限制强行这样做
        Human.__init__(self, name, age)

    def do_homework(self):
        print('do homework')

# 类变量、实例变量可以被子继承
student1 = Student('university', 'tosin', 20)
print(student1.sum, Student.sum, student1.name, student1.age)
# 实例方法可以被子类继承
student1.get_name()


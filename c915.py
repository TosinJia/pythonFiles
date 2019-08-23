from c91401 import Human


class Student(Human):
    def __init__(self, school, name, age):
        self.school = school
        # 子类构造函数调用父类构造函数，必须手动传入self
        # 方式1：一个类调用一个实例方法，说不通，无意义，不限制强行这样做，不推荐
        # Human.__init__(self, name, age)
        # 方式2:
        super(Student, self).__init__(name, age)

    # 子类方法父类方法同名，会优先调动子类的方法
    def do_homework(self):
        super(Student, self).do_homework()
        print('do homework')

student1 = Student('university', 'tosin', 20)
# 通过实例对象调用实例方法
student1.do_homework()
# 可以通过类调用实例方法，没有意义
Student.do_homework(student1)
# 实例方法中调用父类是实例方法时，依然可以；TypeError: super(type, obj): obj must be an instance or subtype of type
# Student.do_homework('')


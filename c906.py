
class Student():
    # 类变量定义 # 一个班级里所有学生的总数
    sum = 0

    # self不是关键字，可以修改成this，python推荐使用self
    def __init__(this, name, age):
        # 实例变量定义
        this.name = name
        this.age = age

    def do_homework(self):
        print('do homework')


student1 = Student('tosin', 20)
student2 = Student('jacky', 21)
# 类变量、实例变量的使用
print(student1.name, student2.name, Student.sum)




class Student():
    # 类变量定义 # sum 一个班级里所有学生的总数
    sum = 0

    name = 'TOSIN'
    age = 0

    # self不是关键字，可以修改成this，python推荐使用self,显胜于隐
    def __init__(this, name, age):
        # 实例变量定义；初始化对象的属性
        this.name = name
        this.age = age

        # 思考题1
        print(name)
        # 思考题2
        sum += 1

        # 类变量赋值 ；不是由于全局变量局部变量的原因
        # name = name
        # age = age

    def do_homework(self):
        print('do homework')


student1 = Student('tosin', 20)
# __dict__ 类似于模块里的 __all__，python内置变量；当前对象所有相关的变量的字典
print(student1.__dict__, Student.__dict__)
# 类变量、实例变量的使用；
print(student1.name, Student.name)
print(Student.sum)




class Student():
    # 类变量定义 # sum 一个班级里所有学生的总数
    sum = 0

    # 类方法定义 @装饰器，第一个默认参数cls；类似于实例方法中的self可以修改为其他名字，例如self，推荐cls
    @classmethod
    def plus_sum(cls):
        cls.sum += 1
        print('当前班级学生总数为：'+str(cls.sum))

    def __init__(self, name, age):
        # 实例变量定义；初始化对象的属性
        self.name = name
        self.age = age
        # self.__class__.sum += 1
        # print('当前班级学生总数为：' + str(self.__class__.sum))

    def do_homework(self):
        print('do homework')


student1 = Student('tosin', 20)
# 类方法调用
Student.plus_sum()
# 对象对用类的方法 对象.类方法 不建议这么做，逻辑上不通
student1.plus_sum()

# student1 = Student('tosin1', 20)
# Student.plus_sum()
# student1 = Student('tosin2', 20)
# Student.plus_sum()



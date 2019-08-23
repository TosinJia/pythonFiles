
class Student():
    # 类变量定义 # sum 一个班级里所有学生的总数
    sum = 0

    # 静态方法定义
    @staticmethod
    def add(x, y):
        # 静态方法内部可以访问类变量
        print(Student.sum)
        print('This is a static method!')
        # print(self.name)

    # 类方法定义 @装饰器，第一个默认参数cls；类似于实例方法中的self可以修改为其他名字，例如self，推荐cls
    @classmethod
    def plus_sum(cls):
        cls.sum += 1
        print('当前班级学生总数为：'+str(cls.sum))
        # print(self.name)

    def __init__(self, name, age):
        # 实例变量定义；初始化对象的属性
        self.name = name
        self.age = age

    # 实例方法
    def do_homework(self):
        print('do homework')


student1 = Student('tosin', 20)
# 静态方法调用
student1.add(1, 2)
Student.add(3, 4)



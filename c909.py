
class Student():
    # 类变量定义 # sum 一个班级里所有学生的总数
    sum1 = 0

    def __init__(self, name, age):
        # 实例变量定义；初始化对象的属性
        self.name = name
        self.age = age

        # 思考题2
        # sum += 1
        print(Student.sum1, self.__class__.sum1)
        Student.sum1 += 1
        self.__class__.sum1 += 1

        # 访问实例变量，
        print(self.name)
        print(self.__dict__)
        # 思考题1 读取的是形参name1；实例方法内部通过name进行dict的查找是不不可以的，这种查找机制仅仅在通过类对象的外部调用的时候是可以的
        print(name)

    def do_homework(self):
        print('do homework')


student1 = Student('tosin', 20)

# 类变量、实例变量的使用；
print(student1.name)
print(Student.sum1)



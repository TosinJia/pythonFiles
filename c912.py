
class Student():
    sum = 0

    @staticmethod
    def add(x, y):
        print(Student.sum)
        print('This is a static method!')

    @classmethod
    def plus_sum(cls):
        cls.sum += 1
        print('当前班级学生总数为：'+str(cls.sum))

    def __init__(self, name, age):
        self.name = name
        self.age = age
        # score变为私有变量
        self.__score = 0

    # 实例方法
    def do_homework(self):
        # 类内部调用实例方法
        self.do_english_homework()
        print('do homework')

    def do_english_homework(self):
        print('do english homework')

    # 不建议直接在对象的外部对成员变量进行赋值；建议通过方法，可以对输入参数进行校验
    def __marking__(self, score):
        if score < 0:
            return '不能为负分'
        self.__score = score
        print(self.name + ' 分数:' + str(self.__score))


student1 = Student('tosin', 20)
# 类外部访问实例方法
student1.do_homework()
# 外部不应该能操作分数，公开的
# student1.score = -1
# print(student1.name, student1.score)
# student1.marking(59)
# print(student1.marking(-1))
# AttributeError: 'Student' object has no attribute '__marking'
# print(student1.__marking(-1))
# 自己定义的不建议前后都加下划线
# print(student1.__marking__(-1))

# 思考 强制从外边访问私有变量，没有报错
# 不是说实例私有变量没有生效，而是由于python动态语言的特性，实际上是给对象新添加了一个实例变量，不可以在外部动态添加私有变量
student1.__score = -1
print(student1.__score)
# {'name': 'tosin', 'age': 20, '_Student__score': 0, '__score': -1} _Student__score 是私有变量__score，__score 动态添加的；
print(student1.__dict__)
# 私有变量名会改名添加_类前缀，可以间接读取私有变量
print(student1._Student__score)

# 读取student2的私有属性
student2 = Student('tosin2', 22)
# AttributeError: 'Student' object has no attribute '__score'
# print(student2.__score)
print(student2.__dict__)


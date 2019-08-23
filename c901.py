
class Student():
    # 类变量
    name = 'tosin'
    age = 0

    # 类方法 参数列表一定要加self，使用类定义的变量 self.变量
    def print_info(self):
        print('name: ' + self.name)
        print("age: " + str(self.age))

    # 类里边不能调用类方法
    # print_info()


# 实例化
# student = Student()
# student.print_info()

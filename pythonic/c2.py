day = 0

switcher = {
    0: "Sunday",
    1: "Monday",
    2: "Tuesday"
}

# 使用下标的方式；如果key不存在会报错KeyError
day_name = switcher[day]
print(day_name)

# 使用get方法，模拟default分支；如果key不存在会返回默认值
day = 7
day_name = switcher.get(day, "Unknown")
print(day_name)


# case语句下可以写一段代码块 ;使用函数式编程特性
def get_sunday():
    return "Sunday"


def get_monday():
    return "Monday"


def get_tuesday():
    return "Tuesday"


def get_default():
    return "Unknown"


# value 可以是一个函数
switcher = {
    0: get_sunday,
    1: get_monday,
    2: get_tuesday
}
day = 1
day_name = switcher.get(day, get_default)
print(type(day_name), day_name)
day_name = switcher.get(day, get_default)()
print(day_name)

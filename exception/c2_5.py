
str = "hello exception"
str = "1"
try:
    int(str)
except IndexError as e:
    print(e)
except KeyError as e:
    print(e)
except ValueError as e:
    print(e)
else:
    print("无异常")
finally:
    print("有无异常，都执行")
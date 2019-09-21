import traceback

try:
    pass
except:
    traceback.print_exc()

try:
    1/0
except Exception as e:
    # print(e)
    # traceback.print_exc()
    # print(traceback.format_exc())
    # traceback.print_exc()可以接受file参数直接写入到一个文件
    traceback.print_exc(file=open("E:\\python-exception.txt", "w+"))


try:
    # 语句
    pass
# 异常名
except Exception:
    # 异常说明
    pass

try:
    f = open("E:\\config.yaml-", "r")
except IOError as e:
    print("open exception: %s: %s" %(e.errno, e.strerror))

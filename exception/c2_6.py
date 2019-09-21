
def not_zero(num):
    try:
        if num == 0:
            raise ValueError("参数异常")
        return num
    except Exception as e:
        print(e)

print(not_zero(0))

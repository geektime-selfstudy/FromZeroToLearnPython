# 用闭包函数来实现计数器
def counter(FIRST=0): # 当调用counter函数的时候如果没有给定参数从0开始
    cnt = [FIRST]
    def add_one():
        cnt[0] += 1
        return cnt[0]
    return add_one


num5 = counter()
print(num5())
print(num5())
print(num5())

num10 = counter(10)
print(num10())
import time
# time.sleep(2) # 程序暂停2秒
# print(time.time()) # 从1970年1月1日到现在所经历的秒数
# time.sleep(2)
# print(time.time()) # 从1970年1月1日到现在所经历的秒数


# 记录函数的运行时间
# def i_can_sleep():
#     time.sleep(3)

# start_time = time.time()
# i_can_sleep()
# end_time = time.time()
# print("函数运行了%s秒" % (end_time - start_time))

# 使用装饰器记录函数运行时间，对于每次运行上面的代码可以使用装饰器进行包装

def timer(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        return end_time - start_time
    return wrapper

@timer #这个是一个语法糖的概念，timer是一个装饰函数，i_can_sleep()是被装饰函数
def i_can_sleep():
    time.sleep(3)

# 调用装饰器
print(type(timer))
print(i_can_sleep())
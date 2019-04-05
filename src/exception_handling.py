# i = j # NameError: name 'j' is not defined
# a = '123'
# a[3] # IndexError: string index out of range
# d = {'a':1, 'b':2}
# print(d['c']) # KeyError: 'c'

# year = int(input("Please input the year : ")) # ValueError: invalid literal for int() with base 10: 'ewqeq'

try:
    year = int(input("Please input the year : "))
except ValueError:
    print("年份要输入数字")
# print(1 / 0)


# 打印出错信息
try:
    print(1 / 0)
except ZeroDivisionError as e:
    print("%s" % e)

# 捕获所有错误的出错信息
try:
    print(1 / 0)
except Exception as e:
    print("%s" % e)

# 自己定义出错信息, 例如对NameError自己定义出错信息，可以使用raise关键字
try:
    raise NameError('Hello Error')
except NameError:
    print('My custom Error')

try:
    file = open('name.txt')
except Exception as e:
    print("%s" % e)
finally: # 不管出错与否都会执行得操作，例如对于文件的关闭
    file.close()
# 使用闭包函数求解线性方程
def a_line(a, b):
    def arg_y(x):
        return a * x + b
    return arg_y 

line = a_line(3, 5)
print(line(10))
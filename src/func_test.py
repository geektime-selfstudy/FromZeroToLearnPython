# print("11", end='\n\n\n') # 当我们没有按照函数的参数顺序给出值的时候，需要使用关键字参数指定值
# print("ddd")

# def func(a, b, c):
#     print("a : %d" % a)
#     print("b : %d" % b)
#     print("c : %d" % c)
# func(1, 2, 3)

# func(1, c = 2, b = 2) # 对于参数顺序不一致的时候给定关键字传参数

# 定义可变长参数
# def func2(required, *other):
#     print(1 + len(other)) # 因为required算作是一个参数，所以+1

# func2(6, 1, 3)


# mars = 144
# def func3():
#     # mars = 155 # 这个mars是局部作用变量
#     global mars # 声明这里的mars是全局变量
#     mars = 123 # 对全局变量的mars进行修改
#     print(mars)
# func3()
# print(mars)

# 函数的迭代器和生成器
list1 = [1, 2, 3]
it = iter(list1) # 集合中的迭代器
print(next(it)) # 每次调用next取值

# 自己做一个迭代器叫做生成器, 使用yield关键字

def frange(start, stop, step):
    x = start
    while x < stop:
        yield x
        x += step

for i in frange(0, 10, 0.5):
    print(i)

# lambda表达式

def getValue(): # 这个函数没有参数，所以下面的lambda后面不加参数
    return True

## 上面的函数可以简化为下面的lambda表达式
y = lambda : True

print(y())

def add(x, y): # 这个函数有两个参数，等价于lambda: x,y
    return x + y

z = lambda x,y : x + y
print(z(2,3))

# 一个深奥的lambda表达式
value = lambda item : item[1]# item[1]是返回字典的值，item[0]是返回字典的键
a_dict = {'a' : 'aa', 'b' : 'bb'}
for i in a_dict.items():
    print(value(i)) 

# Python中的内建函数

## filter()函数
a = [1, 2, 3, 4]
print(list(filter(lambda x : x > 2, a))) # 对第2个参数的迭代器中的集合进行第1个参数函数的执行
# 这里需要注意一下：Python2和3有一个很大的差别：如果使用filter lambda的形式需要将filter的结果强制转换为list，否则lambda的部分就不会被执行

## map()函数
a = [1, 2, 3, 4]
print(map(lambda x : x + 1, a)) # map函数是分别对集合中的每个元素进行操作
print(list(map(lambda x : x + 1, a))) # map函数是分别对集合中的每个元素进行操作
b = [2, 3, 4, 5]
print(list(map(lambda x,y : x+y, a, b))) # 将a集合中的每个元素与对应的b集合中的每个元素相加

## reduce(function, sequence, initial)函数
# reduce函数并不能直接使用，需要导入
# 将序列和初始值按照函数的方式做运算
from functools import reduce
# help(reduce)
print(reduce(lambda x,y : x+y, [2, 3, 4], 1)) # 等价于(((2 + 1) + 3) + 4)

## zip()函数
### 类似于进行横纵转换
for i in zip((1, 2, 3), (4, 5, 6)):
        print(i)

### 使用zip()函数进行字典的键值转换
a_dict = {"诸葛亮": 1, "张飞": 500, "刘备": 900}
for i in zip(a_dict.values(), a_dict.keys()):
        print(i)
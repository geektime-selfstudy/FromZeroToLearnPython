# 列表推导式与字典推导式

# 求1-10所有偶数的平方
a_list = []
for i in range(1, 11):
    if (i % 2 == 0):
        a_list.append(i ** 2)

print(a_list)

# 上面的代码不是很简洁，可以采用下面的列表推导式
b_list = [i*i for i in range(1, 11) if (i % 2 == 0)]
print(b_list)

# 字典推导式
chinese_zodiac = "猴鸡狗猪鼠牛虎兔龙蛇马羊"
cz_num = {}
for i in chinese_zodiac:
    cz_num[i] = 0

## 上面写的字典赋值有点繁琐，可以采用字典推导式
cz_num2 = {i:0 for i in chinese_zodiac}

print(cz_num2)
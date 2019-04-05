# 记录生肖，根据年份来判断生肖
# chinese_zodiac = "鼠牛虎兔龙蛇马羊猴鸡狗猪"

chinese_zodiac = "猴鸡狗猪鼠牛虎兔龙蛇马羊"
print(chinese_zodiac[0:])
print(chinese_zodiac[0:4])  # 从第0个元素访问到第3个元素
print(chinese_zodiac[-1])   # 倒数开始进行访问



year = 2019                 # 2019年是猪年
print(year % 12)
print(chinese_zodiac[year % 12])    

# 序列操作符
## 成员关系操作符 in 与 not in 
print('狗' in chinese_zodiac)
print('狗' not in chinese_zodiac)

## 连接操作符 序列 + 序列
print(chinese_zodiac + chinese_zodiac)
## 重复操作符
print(chinese_zodiac * 3)
## 切片操作符
print(chinese_zodiac[-1])
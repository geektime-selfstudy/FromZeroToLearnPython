# 记录生肖，根据年份来判断生肖
# chinese_zodiac = "鼠牛虎兔龙蛇马羊猴鸡狗猪"

chinese_zodiac = "猴鸡狗猪鼠牛虎兔龙蛇马羊"
year = int(input("请输入出生年份："))                 # 2019年是猪年
# print(type(year))
print(chinese_zodiac[year % 12])

if chinese_zodiac[year % 12] == '猪':
    print("猪年运势大吉")

for cz in chinese_zodiac:
    print(cz)

# 生成1-12
for i in range(1, 13):
    print(i)

for i in range(10):
    print(i)

for i in range(2000, 2019):
    print("%d 年的生肖是 %s" % (i, chinese_zodiac[i % 12]))  # 这里百分号后面跟一个元祖
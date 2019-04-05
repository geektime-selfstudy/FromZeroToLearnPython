# 采用元祖来存储星座，小写的u表示unicode编码
zodiac_name = (u'摩羯座', u'水瓶座', u'双鱼座', u'白羊座', u'金牛座', u'双子座', u'巨蟹座',
                u'狮子座', u'处女座', u'天秤座', u'天蝎座', u'射手座')

# 存储每个星座开始和结束的日期
zodiac_days = ((1, 20), (2, 19), (3, 21), (4, 21), (5, 21), (6, 22), (7, 23),
                (8, 23), (9, 23), (10, 23), (11, 23), (12, 23))

chinese_zodiac = "猴鸡狗猪鼠牛虎兔龙蛇马羊"

# 初始化两个统计数据的字典
cz_num = {}
for i in chinese_zodiac:
    cz_num[i] = 0
zodiac_num = {}
for i in zodiac_name:
    zodiac_num[i] = 0


while True:
    # 用户输入的年份
    year_input = int(input('请输入年份：'))
    # 用户输入的月份
    month_input = int(input("请输入月份："))
    # 用户输入的日期
    date_input = int(input("请输入日期："))
    n = 0
    while (month_input, date_input) > zodiac_days[n]:
        if month_input == 12 and date_input >= 23:
            break
        n += 1
    
    # 输出具体情况
    print("%d年是%s年" % (year_input, chinese_zodiac[year_input % 12]))
    print("%d月%d日是%s" % (month_input, date_input, zodiac_name[n]))
    zodiac_num[zodiac_name[n]] += 1
    cz_num[chinese_zodiac[year_input % 12]] += 1
    
    # 输出统计信息
    # 输出星座统计信息
    for each_key in zodiac_num.keys():
        print("%s有%d次" % (each_key, zodiac_num[each_key]))
    # 输出生肖统计信息
    for each_key in cz_num.keys():
        print("%s年有%d次" % (each_key, cz_num[each_key]))




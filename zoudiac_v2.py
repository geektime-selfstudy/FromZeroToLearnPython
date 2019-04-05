# 采用元祖来存储星座，小写的u表示unicode编码
zodiac_name = (u'摩羯座', u'水瓶座', u'双鱼座', u'白羊座', u'金牛座', u'双子座', u'巨蟹座',
                u'狮子座', u'处女座', u'天秤座', u'天蝎座', u'射手座')

# 存储每个星座开始和结束的日期
zodiac_days = ((1, 20), (2, 19), (3, 21), (4, 21), (5, 21), (6, 22), (7, 23),
                (8, 23), (9, 23), (10, 23), (11, 23), (12, 23))

# 用户输入的月份
month_input = input("请输入月份：")
# 用户输入的日期
date_input = input("请输入日期：")

# 根据用户的输入进行星座的判断
for i in range(len(zodiac_days)):
    if (int(month_input), int(date_input)) <= zodiac_days[i]:
        print(zodiac_name[i])
        break
    elif int(month_input) == 12 and int(date_input) >= 23:
        print(zodiac_name[0])
        break
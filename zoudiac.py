
# 采用元祖来存储星座，小写的u表示unicode编码
zodiac_name = (u'摩羯座', u'水瓶座', u'双鱼座', u'白羊座', u'金牛座', u'双子座', u'巨蟹座',
                u'狮子座', u'处女座', u'天秤座', u'天蝎座', u'射手座')

# 存储每个星座开始和结束的日期
zodiac_days = ((1, 20), (2, 19), (3, 21), (4, 21), (5, 21), (6, 22), (7, 23),
                (8, 23), (9, 23), (10, 23), (11, 23), (12, 23))

print(zodiac_name[0])

# 元祖当中两个数字大小的比较
print((1, 20) > (1, 31))    # 其实就是120和131数字大小的比较

(month, day) = (2, 15)

# 通过过滤器找到小于(month, day)的元素，并返回过滤器，接收两个参数，第一个为函数，第二个为序列
zodiac_day = filter(lambda x : x <= (month, day), zodiac_days)
zodiac_len = len(list(zodiac_day))
print(zodiac_name[zodiac_len])


# 列表的操作
a_list = [1, "Hello"]
a_list.append("world")
a_list.remove(1)
print(a_list)
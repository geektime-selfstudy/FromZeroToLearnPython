import time
print(time.time()) # 表示从1970年1月1号到现在所经历过的秒数

print(time.localtime())
print(type(time.localtime)) # 虽然输出时间和日期，但是可读性太差

# 格式化输出日期
print(time.strftime("%Y-%m-%d %H:%M:%S")) #输出年-月-日 小时-分钟-秒数

import datetime
print(datetime.datetime.now()) # 使用datetime模块获得现在的时间

# 修改时间为10分钟以后的时间
new_time = datetime.timedelta(minutes=10) # delta在数学中意为偏移量增量
print(new_time + datetime.datetime.now()) # 现在的时间加上时间偏移

# 得到某一天的后十天的日期
one_day = datetime.datetime(2019, 12, 27)
time_delta = datetime.timedelta(days=100)
print(time_delta + one_day) #得到2019年12月27号后面100天是哪一年几月几日

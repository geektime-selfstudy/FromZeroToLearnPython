
import re
# 使用函数读取三国中武器出现次数
def find_item(weapon_name):
    with open('D:\sanguo.txt', encoding='GB18030') as f:
        data = f.read().replace('\n', '')
        num = len(re.findall(weapon_name, data))
    return num


i = 0
num_weapon = {}
with open('./weapon.txt', encoding='utf-8') as f:
    for line in f.readlines():
        if i % 2 == 0:
            line = line.strip() # 删除首尾空白字符
            num_weapon[line] = find_item(line)
        i += 1

# 按照出现次数进行排序
name_sorted = sorted(num_weapon.items(), key=lambda item : item[1], reverse=True)

for item in num_weapon.keys():
    print("%s 出现了 %d 次" % (item, num_weapon[item]))


"""老师的代码

import re
# 使用函数读取三国中武器出现次数
def find_item(weapon_name):
    with open('D:\sanguo.txt', encoding='GB18030') as f:
        data = f.read().replace('\n', '')
        num = len(re.findall(weapon_name, data))
    return weapon_name, num


num_weapon = {}
with open('./weapon.txt', encoding='utf-8') as f:
    i = 1
    for line in f:
        if i % 2 == 1:
            weapon, weapon_number = find_item(line.strip())
            num_weapon[weapon] = weapon_number
        i += 1

for item in num_weapon.keys():
    print("%s 出现了 %s 次" % (item, num_weapon[item]))

"""
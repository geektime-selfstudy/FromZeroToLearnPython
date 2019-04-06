import re
# 使用函数读取sanguo.txt中name.txt的人名出现次数并进行统计
def find_item(name):
    with open('D:/sanguo.txt', encoding='GB18030') as f:
        data = f.read().replace('\n', '')
        num = re.findall(name, data) # 返回一个找到匹配内容组成的列表
    return len(num)


num_dict = {}
with open('name.txt', encoding='utf-8') as f:
    for i in f.read().split('|'):
        num_dict[i] = find_item(i) # 将每个人物的返回次数放入到字典中
    
for item in num_dict.keys():
    print("%s 出现 %d 次" % (item, num_dict[item]))
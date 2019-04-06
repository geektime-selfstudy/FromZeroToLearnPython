
# 读取人名
file = open('name.txt', encoding='UTF-8')
for line in file.readlines():
    print(line.split('|')[0])


# 读取兵器谱
file2 = open('weapon.txt', encoding='utf-8')
i = 0
for line in file2.readlines():
    if i % 2 == 0:
        print(line.strip('\n')) # 将读取到的每行内容放入到line中，同时因为每行后面自带换行符，所以采用strip()方法去掉
    i += 1

file3 = open('weapon.txt', encoding='utf-8') # encoding指定了以什么样的编码打开文件
print(file3.read().replace('\n', '')) # 把读取到文件内容中的换行符换为空

# 定义一个函数，打开name.txt并进行输出
def func():
    print(open('name.txt', encoding='utf-8').read())

func()

# 定义一个函数，接收文件名作为参数，并打开指定文件
def func2(filename):
    print(open(filename, encoding='utf-8').read())

func2('weapon.txt')
# 将小说的主要人物记录在文件中
# file1 = open('./name.txt', 'w')
# file1.write('111')
# file1.close()   # 关闭并保存文件

# file2 = open('./name.txt', encoding='cp936')
# print(type(file2.read()))
# print(file2 is None)
# print(file2.read())
# file2.close()

# file3 = open('./name.txt', 'a')
# print(file3 is None)
# file3.write('222')
# file3.close()

# 文件的常用操作
file4 = open('name.txt', encoding='cp936')
file4.read(1) # 只读取一个字符
print(file4.tell()) # 打印目前文件指针的位置
file4.seek(0)   # 让文件指针回到开头
print(file4.readline()) # 读取文件中的一行内容
file4.seek(0)
for line in file4.readlines():
    print(line)
    print("====")
file4.close()
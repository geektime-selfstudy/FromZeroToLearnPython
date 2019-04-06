# 两种导入方式
import os
# from os import path




# 根据相对路径来获取绝对路径
print(os.path.abspath('.'))

# 判断文件是否存在
print(os.path.exists('E:/name.txt'))

# 判断是否是文件或者是否是目录
print(os.path.isdir("E:/name.txt"))
print(os.path.isdir("E:/"))

# 将两个路径拼接
print(os.path.join('/tmp/a/', 'b/c'))

# 使用pathlib
from pathlib import Path
## 获取相对路径下的绝对路径
p = Path('.')
print(p.resolve()) 

## 判断某个路径是否目录或者文件
print(p.is_dir())

## 使用pathlib新建目录
q = Path('E:/name/name/name')
Path.mkdir(q, parents=True) #parents就是说当你指定创建的目录的上一级目录不存在的时候，是否自动创建上一级目录
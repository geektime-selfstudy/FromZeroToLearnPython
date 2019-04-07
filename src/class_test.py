
# 面向过程的一般写法
# a_dict = {'name' : 'tom', 'hp' : 100}

# def print_role(rolename):
#     print("name is %s, hp is %d" % (rolename['name'], rolename['hp']))

# print_role(a_dict)

# 面向对象的写法
class Player():
    def __init__(self, name, hp): # 实例化后一定会执行得一个初始化方法
        self.__name = name #
        self.hp = hp
    
    def prin_role(self): #self表示类实例化后的对象本身
        print("%s : %s" % (self.__name, self.hp))

    # 再定义一个可以改名的方法
    def update_name(self, new_name):
        self.__name = new_name

user1 = Player('wxw', '9999')
user1.prin_role()
user1.update_name('yirufeng')
user1.prin_role()
user1.hp = '99' #可以通过实例来进行属性的修改，但是当属性前面加上两个__的时候，不可以直接修改
user1.prin_role()




class Monster():
    pass
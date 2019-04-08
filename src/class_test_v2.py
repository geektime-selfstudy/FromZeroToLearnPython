class Monster():
    def __init__(self, hp=100):
        self.hp = hp
    
    def run(self):
        print('移动到某个位置')

    def whoami(self):
        print("我是怪物的父类")

class Animals(Monster): #普通怪物继承了Monster类
    """
    普通怪物
    """
    def __init__(self, hp=10): 
        # self.hp = hp # 这里其实可以不用初始化，因为会太占用计算机资源，所以可以调用父类的初始化方法
        super().__init__(hp)
     

class Boss(Monster):
    'Boss级别怪物'
    def __init__(self, hp=10): 
        super().__init__(hp)

    def whoami(self): # 会覆盖父类原有的方法
        print("我是怪物我怕谁")

a1 = Monster(50)
print(a1.hp)
a1.run()
a2 = Animals()
print(a2.hp)
a2.run()
a3 = Boss(1000)
print(a3.hp)
a3.whoami()


# 判断子类与父类
print(isinstance(a1, Boss))  # 判断a1是否是Boss类的子类
print(type(a1))
print(type(a2))
print(type(a3))
print(isinstance(a1, object)) # Python中所有类都继承自object
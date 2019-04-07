class Monster():
    def __init__(self, hp=100):
        self.hp = hp
    
    def run(self):
        print('移动到某个位置')


class Animals(Monster): #普通怪物继承了Monster类
    """
    普通怪物
    """
    def __init__(self, hp=10): # 这里其实可以不用初始化，因为会太占用计算机资源，所以可以调用父类的初始化方法
        self.hp = hp
     

class Boss(Monster):
    'Boss级别怪物'
    pass

a1 = Monster(50)
print(a1.hp)
a1.run()
a2 = Animals()
print(a2.hp)
a2.run()
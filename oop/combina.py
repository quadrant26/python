# 面向对象 组合
# 同一个类的属性名会覆盖方法名

class Turle:
    def __init__(self, x):
        self.num = x

class Fish:
    def __init__(self, x):
        self.num = x
        
class Pool:
    def __init__(self, x, y):
        self.turle = Turle(x)
        self.fish = Fish(y)
        
    def print_num(self):
        print("水池里总共有乌龟 %d 只， 小鱼 %d 条！" % (self.turle.num, self.fish.num))
    
p = Pool(3, 5)
p.print_num()
import random as r

class Fish():
    def __init__(self):
        self.x = r.randint(0, 10)
        self.y = r.randint(0, 10)
    
    def move(self):
        self.x -= 1
        print("我的位置是：", self.x, self.y)

class Goldfish(Fish):
    pass

class Carp(Fish):
    pass

class Salson(Fish):
    pass

class Shark(Fish):
    # 子类重写父类的方法， 会覆盖父类的方法
    # 保留父类的方法
    def __init__(self):
        # Fish.__init__(self)   # 子类调用未绑定父类的方法 1
        # super().__init__()    # 子类调用未绑定父类的方法 2
        self.hungry = True
    
    def eat(self):
        if self.hungry:
            print("我就是一个吃货^_^")
            self.hungry = False
        else:
            print("我先回了...")

fish = Fish()
fish.move()
fish.move()

goldfish = Goldfish()
goldfish.move()

shark = Shark()
shark.eat()
shark.eat()
Fish.__init__(shark) # 子类调用未绑定父类的方法  3
shark.move()

        
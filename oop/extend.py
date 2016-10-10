class Cat:
    def hello(self):
        print("正在调用父类的方法....")
'''
class Child(Cat):
    pass
'''
class Child(Cat):
    def hello(self):
        print("正在调用子类的方法....")

p = Cat()
p.hello()

c = Child()
c.hello()
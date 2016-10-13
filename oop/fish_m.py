class Base1:
    def fool(self):
        print("我是 foo1, 我为 base1 代言")

class Base2:
    def foo2(self):
        print("我是 foo2, 我为 base2 代言")
        
class C(Base1, Base2):
    pass

c = C()
c.fool()
c.foo2()
# 构造和析构

class Reactangel:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def getPerl(self):
        return (self.x+self.y)*2
    
    def getArea(self):
        return (self.x*self.y)
    
react = Reactangel(4, 5)
print(react.getPerl())
print(react.getArea())

class A:
    def __init__(self):
        return "A fo A-Cup"
    
class CapStr(str):
    # 继承不可变类型的时候
    def __new__(cls, string):
        string = string.upper()
        return str.__new__(cls, string)
    
a = CapStr("I love fishC.com")
print(a)

class C:
    def __init__(self):
        print("__init__")
    
    def __del__(self):
        print("del")
        
c1 = C()
c2 = c1
c3 = c2

del c3
del c2
del c1 # 只有所有实例对象被删除的时候才会调用 __del__ 方法

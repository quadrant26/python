# 描述符
'''
__set__(self, instance, owner)
    用于访问属性 它返回属性的值
__get__(self, instance, value)
    将在属性分配操作中调用，不返回任何内容
__delete__(self, instance)
    控制删除操作，不返回任何内容
'''

class MyDectiptot:
    def __get__(self, instance, owner):
        print("getting...", self, instance, owner)
        
    def __set__(self, instance, value):
        print("getting...", self, instance, value)
        
    def __delete__(self, instance):
        print("getting...", self, instance)
        
'''
test = MyDectiptot()
test.x

print(test)

test.x = "X-man"

del test.x
'''

class MyProperty:
    def __init__(self, fget=None, fset=None, fdel=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
        
    def __get__(self, instance, owner):
        return self.fget(instance)
    
    def __set__(self, instance, value):
        self.fset(instance, value)
        
    def __delete__(self, instance):
        self.fdel(instance)
        
class C:
    def __init__(self):
        self._x = None
        
    def getX(self):
        return self._x  
    
    def setX(self, value):
        self._x = value
        
    def delX(self):
        del self._x
        
    x = MyProperty(getX, setX, delX)

        
        
        
        
        
        
        
        
        
        
        
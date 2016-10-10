'''
类的内置函数
    issubclass()    检查一个类是否是一个类的子类
    isinstance(object, classinfo)
        # 第一个参数不是 object 永远返回  False
        # 第二个参数不是类或者由类对象组成的元组，会抛出一个 TypeError 异常
    hasattr(object, name)    一个对象是否有指定的属性
    getattr(object, name, [default]) 
        # 获取属性的值 不存在 AttributeError 
        # default  不存在 后的提示信息
    setattr(object, name, value)   设置属性
    delattr(object, name)         删除属性 ，属性不存在 抛出 AttributeError
    property(fget=None, fset=None, fdel=None, doc=None)
        # 通过属性设置属性

'''
from builtins import issubclass
class A:
    pass

class B(A):
    pass

print(issubclass(A, B))
print(issubclass(B, A))
print(issubclass(A, object))

# isinstance(object, class)
class C:
    pass

b1 = B()
print(isinstance(b1, B))
print(isinstance(b1, A))
print(isinstance(b1, C))
print(isinstance(b1, (A, B, C))) # 第二个 参数是一个 元组


# hasattr(object, name)
class CC:
    def __init__(self, x=0):
        self.x = x

c1 = CC()
print(hasattr(c1, 'x'))
print(getattr(c1, 'x'))
print(getattr(c1, 'y', "您打印属性不存在"))


# property(fget=None, fset=None, fdel=None, doc=None)
class CCC:
    def __init__(self, size=10):
        self.size = size
        
    def getSize(self):
        return self.size
    
    def setSize(self, size):
        self.size = size
        
    def delSize(self):
        del self.size
        
    x = property(getSize, setSize, delSize)
        
c2= CCC()
# c2.getSize()
print(c2.x) # 获取属性
c2.x = 32
print(c2.x) # 设置属性
del c2.x    # 删除属性

print(c2.size)


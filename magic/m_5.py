# 属性的魔术方法

class C:
    def __init__(self):
        self.x = "X-man"
        
c = C()
c.x
print(getattr(c, 'x', '木有这个属性'))
print(getattr(c, 'y', '木有这个属性'))

'''
__getattr__(self, name)
    定义当用户试图获取一个不存在的属性时的行为
__getattribute__(self, name)
    定义该类的属性被访问时的状态
__setattr__(self, name, value)
    定义一个属性被设置的行为
__delattr__(self, name)
    定义一个属性被删除时的行为
'''

class B:
    def __getarribute__(self, name):
        print("getattribute")
        return super().__getattribute__(name)
    
    def __getattr__(self, name):
        print("getattr")
        
    def __setattr__(self, name, value):
        print("setattr")
        return super().__setattr__(name, value)
    
    def __delattr__(self, name):
        print("delattr")
        return super().__delattr__(name)
    
b = B()
b.x


b.x = 1

b.x

del b.x   















     
class Reactangel:
    
    def __init__(self, width=0, height=0):        
        self.width = width
        self.height = height
        
    def __setattr__(self, name, value):
        if name == "square":
            self.width = value
            self.hieght = value
        else:
            # 递归报错
            # self.name = value
            # 解决方法 ： 调用基类的 super() 方法
            super().__setattr__(name, value)
            # 第二种解决方法
            # self.__dict__[name] = value
            
    def getArea(self):
        return self.width * self.height
    
r1 = Reactangel(4,5)

print( r1.getArea() )
r1.square = 10
print(r1.__dict__)
print(r1.getArea())
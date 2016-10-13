class CC:
    def setxy(self, x, y):
        self.x = x
        self.y = y
    
    def printxy(self):
        print(self.x, self.y)
        
dd = CC()
print(dd.__dict__)  # 
print(CC.__dict__)

dd.setxy(3, 9)
print(dd.__dict__)
print(CC.__dict__)


del CC
# ee = CC()

dd.printxy()


# bind
''' 
class B:
    def print():
        print("........")

B.print()  # 可以正确打印
b = B()
#b.print()   # 没有绑定对象 报错
'''

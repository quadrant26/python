class Person:
    name = "king"
    def sayname(self):
        print("My name is %s." % self.name)
        
k = Person()
k.sayname()

class Reactangle:
    w = 4
    h = 2
    
    def getReact(self):
        print("这个矩形的长是 ： %.2f, 宽是： %.2f" % (self.w, self.h))
        
    def setReact(self):
        print("请输入矩形的长和宽：")
        self.w = float(input("长："))
        self.h = float(input("宽："))
        
    def getArea(self):
        print(self.w*self.h)

react = Reactangle();
react.getReact()
react.setReact()
react.getArea()

        
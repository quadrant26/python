import math as m
import random as r
from pip.utils.outdated import SELFCHECK_DATE_FMT

class Point:
    def __init__(self):
        self.a = [r.randint(1, 100), r.randint(1, 100)]
        self.b = [r.randint(1, 100), r.randint(1, 100)]
        print(self.a, self.b)

class Line(Point):
    def getLen(self):
        len = m.sqrt( m.pow((self.a[0] - self.b[0]), 2) + m.pow((self.a[1] - self.b[1]), 2) )
        print("点A的坐标为：%s, 点B的坐标为：%s, 直接的长度为：%s" %(self.a, self.b, len) )
        
l1 = Line()
l1.getLen()
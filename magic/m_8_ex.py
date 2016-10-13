#
import datetime as dt
'''
x = 0
while x < 5:
    print(x)
    x += 1
        
for each in range(5):
    print(each)

class LeapYear:
    def __init__(self):
        y = t.localtime()[0]
        self.x = range(0, y)
        result = []
        for each in self.x:
            if ( each % 4 == 0 and each%100 != 0) or (each%400 ) == 0:
                result.append(each)
                                
                

leapYears = LeapYear()
for i in leapYears:
    if i >= 2000:
        print(i)
    else:
        break

'''

alist = range(5)
it = iter(alist)
while True:
    try:
        print(next(it))
    except StopIteration:
        break
    
class LeapYear:
    def __init__(self):
        self.now = dt.date.today().year

    def isLeapYear(self, year):
        if(year%4 == 0 and year%400 != 0 ) or (year%400 == 0):
            return True
        else:
            return False

    def __iter__(self):
        return self

    def __next__(self):
        while not self.isLeapYear(self.now):
            self.now -= 1
        temp = self.now
        self.now -= 1

        return temp

leapYears = LeapYear()
for i in leapYears:
    if i >= 2000:
        print(i)
    else:
        break


class MyRev:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration

        self.index = self.index - 1
        return self.data[self.index]

for i in MyRev("FishC"):
    print(i, end="")


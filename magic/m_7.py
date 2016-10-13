''' 
定义容器是不可变的
    __len__(self)  定义当被 len() 的行为
    __getitem__(self, key)
    __setitem__(self, key, value)
    __delitem__(self, key, value)
    __iter__(self)
    __reversed__(self)
    __contains__(self, item)

'''

class CountList:
    def __init__(self, *args):
        self.values = [x for x in args]
        self.count = {}.fromkeys(range(len(self.values)), 0)
        
    def __len__(self):
        return len(self.values)
    
    def __getitem__(self, key):
        self.count[key] += 1
        return self.values[key]
    
c1 = CountList(1, 2, 3, 4, 6)
c2 = CountList(0, 5, 7, 8, 9)
c1[0]
c2[1]
c1[0] + c2[4]
print(c1.count)

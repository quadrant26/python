'''
迭代器
    __iter__
    __next__

'''

for i in "hello, world":
    print(i)
    
links = {
    "baidu" : "http://baidu.com",
    "github" : "http://github.com",
    "yahoo" : "http://yahoo.com.cn"
}

for each in links:
    print("%s -> %s" % (each, links[each]))
    
string = "hello"
it = iter(string)
print(next(it))
print(next(it))
print(next(it))
print(next(it))

str1 = "fishC"
it = iter(str1)
while True:
    try:
        each = next(it)
    except StopIteration:
        break
    print(each)
    
class Fibs:
    def __init__(self, n=20):
        self.a = 0
        self.b = 1
        self.n = n
        
    def __iter__(self):
        return self
    
    def __next__(self):
        self.a, self.b = self.b, self.a+self.b
        if self.a > self.n:
            raise StopIteration
        return self.a
    
f1 = Fibs()
for each in f1:
    if each < 20:
        print(each)  
    else:
        break  

f1 = Fibs(1000)
for each in f1:
    print(each)
    
    
    
    
    
        

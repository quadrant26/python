'''
生成器
    yield
'''

def myGen():
    print("生成器执行")
    yield 1
    yield 2

print(myGen())
print(myGen())


class libs():
    a = 0
    b = 1
    while True:
        a,b = b,a+b
        yield a

for each in libs():
    if each > 100:
        break
    print(each, end="")

# 列表推导式
a = [i for i in range(100) if not(i % 2) and (i%3)]

# 字典推导式
b = {i:i%2 == 0 for i in range(10)}

# 集合推导式
c = {i for i in [1,1,2,3,4,5,6,7,8,3,2,1]}

# 生成器
e = (i for i in range(10))
next(e)
next(e)
next(e)


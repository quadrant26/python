# 序列

# list()    empty list
# list(iterable) 迭代器
 
a = list()

b = "i love lishan"
b = list(b)
print(b)

c = (1,1,2,3,5,8,13,21,34)
c = list(c)
print(c)

# tuple()
# tuple
c = (1,1,2,3,5,8,13,21,34)
d = tuple(c)
print(d)

# str
c = (1,1,2,3,5,8,13,21,34)
s = str(c)
print(s)

# len
print(len(s))

# max 必须保证参数的数据类型必须是一样的 
print(max(c))
print(max(1,2,3,5,6))

# min
print(min(c))
print(min('0123456789'))

# sum
print( sum(c))

# sort

numbers = [-23, -212, 23, 2, 12]
print('sorted',sorted(numbers))

print('reversed',reversed(numbers))

print('enumerate',enumerate(numbers))

print(list(enumerate(numbers)))

a = [1,2,3,4,5,6,7,8]
b = [4,5,6,7,8]
print(zip(a, b))

print(list(zip(a,b)))



def sum(**kw):
    result = 0;
    for each in kw:
        if type(each) == 'str':
            continue
        else:
            result += each
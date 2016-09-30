a = dict(one=1, two=2, three=3)
b = {"one":1, "tow":2, "three":3}
c = dict(zip(['one', 'two', 'three'], [1,2,3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({'three':3, 'one':1, 'two':2})

print(a)
print(b)
print(c)
print(d)
print(e)

data = "1000, king, manle"
myDict = {}


(myDict['id'], myDict['name'], myDict['sex']) = data.split(",")
print(myDict['id']);
print(myDict['name']);
print(myDict['sex']);



dict1 = {}
dict1['a'] = "12"

# 字典的键必须是哈希( Hash ) ，不能是可变类型 （变量， 列表， 字典本身）

dict2 = {}
dict2 = dict2.fromkeys((1,2,3), ('one', 'two', 'three'))
dict2 = dict2.fromkeys((1, 3), '数字')
# from 直接创建新的字典，会吧原来的给覆盖掉
print(dict2)

# 复制 dict 使用 copy() 方法
dict11 = {1:"one", 2:"two", 3:"three"}
dict22 = dict11.copy();
dict11[4] = 'four'
print( dict22 )

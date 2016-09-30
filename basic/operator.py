
# and 操作符
print ( 3 and 0 )
print ( 0 and 1)


# 死循环
'''
i = 10
while i:
    print('我爱鱼C!')
    i = i - 1
'''

# 条件循环
'''
while 'C':
    print('我爱鱼C!')
'''

# 输入一个数字，打印从1到该数字之间的数
'''
normal = 0
num = int(input("请输入一个整数："))
while (normal < num):
    normal = normal + 1
    print (normal)
'''

nor = 1
num2 = int(input("请输入一个整数："))

while ( num2 > nor):
    print(' ' * num2 + '*' * num2)
    num2 = num2 - 1
    
    
# 算数运算符
a = b = c = d = 10
a = a + 1
print (a)
b = b - 3
print (b)
c *= 10
print (c)
d /= 10
print (d )

print (10 // 8)

print (-3 ** 2)

print (3 and False)

# 逻辑运算符
print ( 3.0 // 2.0 )
print(5 ** -2)

print( not 1 or 0 and 1 or 3 and 4 or 5 and 6 or 7 and 8 and 9)

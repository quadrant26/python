# 分支和循环

print(isinstance(int('123'), int))

temp = input("输入一个数字")
print(type(int(temp)))


x = 1
y = 2
z = 3
x, y, z = z, y, x
# 
# assert 断言
# 
score = int(input());
if score < 60:
    print('D')
elif 60 < score < 80:
    print('C')
elif 80 < score < 90:
    print('B')
elif 90 < score <= 100:
    print('A')
else:
    print('输入错误')

x,y,z = 6,4,2

if x < y:
    small = x
    if z < small :
        samll = z
elif y < z:
    small = y
else:
    small = z

small2 = x if ( x < y and x < z) else ( y if y < z else z)
print(small)
print(small2)


for i in range(1, 10, 2):
    print("king")

# error
'''
for i in 5:
    print("wang")
'''

x = list(range(1,10))
print (x)

while True:
    while True:
        break;
        print(1)
    print(2)
    break
print(3)

i = 0
string = 'ILoveFishC.com'
while i < len(string):
# s = len(string)
# while i < s
    print(i)
    i += 1
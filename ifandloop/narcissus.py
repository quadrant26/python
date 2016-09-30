# 水仙花 如果一个 3 位数等于其各位数字的立方和，则称这个数为水仙花数。例如：153 = 1^3 + 5^3 + 3^3，因此 153 就是一个水仙花数
# 100~999 之间的所有水仙花数
# 

'''
for num in range(100, 1000):
    for i in range(0,10):
        for j in range(0,10):
            for k in range(0, 10):
                if ( num == (i*i*i + j*j*j + k*k*k) ):
                    print(num)
'''

for i in range(100, 1000):
    sum = 0
    temp = i

    while temp:
        sum = sum + (temp%10) ** 3
        temp //= 10

    if sum == i:
        print(i)